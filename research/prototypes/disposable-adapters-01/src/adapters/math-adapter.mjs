import { DisposableAdapter, buildValidation, deepClone } from "../core/adapter.mjs";

const TOKEN = /\s*(?:(\d+(?:\.\d+)?)|([A-Za-z][A-Za-z0-9_]*)|(.))/gy;

export function parseExpression(input) {
  const tokens = [];
  let index = 0;
  while (index < input.length) {
    TOKEN.lastIndex = index;
    const match = TOKEN.exec(input);
    if (!match) throw syntax(`Unexpected token at ${index}.`, index);
    const [raw, number, symbol, other] = match;
    index += raw.length;
    if (number) tokens.push({ type: "number", value: Number(number), at: match.index });
    else if (symbol) tokens.push({ type: "symbol", value: symbol, at: match.index });
    else if ("+-*/^()".includes(other)) tokens.push({ type: other, value: other, at: match.index });
    else throw syntax(`Unsupported character ${JSON.stringify(other)}.`, match.index);
  }
  tokens.push({ type: "eof", at: input.length });
  let cursor = 0;
  const peek = () => tokens[cursor];
  const take = (type) => {
    const token = tokens[cursor];
    if (token.type !== type) throw syntax(`Expected ${type}, found ${token.type}.`, token.at);
    cursor += 1;
    return token;
  };

  function startsPrimary(token) {
    return token.type === "number" || token.type === "symbol" || token.type === "(";
  }

  function parseAdd() {
    let node = parseMultiply();
    const args = [node];
    while (peek().type === "+" || peek().type === "-") {
      const op = take(peek().type).type;
      const rhs = parseMultiply();
      args.push(op === "+" ? rhs : { kind: "multiply", args: [{ kind: "number", value: -1 }, rhs] });
    }
    return args.length === 1 ? node : { kind: "add", args: flatten("add", args) };
  }

  function parseMultiply() {
    let node = parsePower();
    const args = [node];
    while (peek().type === "*" || peek().type === "/" || startsPrimary(peek())) {
      if (peek().type === "/") {
        take("/");
        const rhs = parsePower();
        node = { kind: "divide", numerator: args.length === 1 ? args[0] : { kind: "multiply", args: flatten("multiply", args) }, denominator: rhs };
        args.splice(0, args.length, node);
      } else {
        if (peek().type === "*") take("*");
        args.push(parsePower());
      }
    }
    return args.length === 1 ? args[0] : { kind: "multiply", args: flatten("multiply", args) };
  }

  function parsePower() {
    let node = parseUnary();
    if (peek().type === "^") {
      take("^");
      node = { kind: "power", base: node, exponent: parsePower() };
    }
    return node;
  }

  function parseUnary() {
    if (peek().type === "+") {
      take("+");
      return parseUnary();
    }
    if (peek().type === "-") {
      take("-");
      return { kind: "multiply", args: [{ kind: "number", value: -1 }, parseUnary()] };
    }
    return parsePrimary();
  }

  function parsePrimary() {
    if (peek().type === "number") return { kind: "number", value: take("number").value };
    if (peek().type === "symbol") return { kind: "symbol", name: take("symbol").value };
    if (peek().type === "(") {
      take("(");
      const node = parseAdd();
      take(")");
      return node;
    }
    throw syntax(`Expected an expression, found ${peek().type}.`, peek().at);
  }

  const ast = parseAdd();
  take("eof");
  return ast;
}

function flatten(kind, args) {
  return args.flatMap((item) => (item.kind === kind ? item.args : [item]));
}

function syntax(message, at) {
  const error = new SyntaxError(message);
  error.position = at;
  return error;
}

export function expressionToText(node, parent = null) {
  switch (node.kind) {
    case "number": return String(node.value);
    case "symbol": return node.name;
    case "add": {
      const text = node.args.map((arg) => expressionToText(arg, "add")).join(" + ").replace(/\+ -1 \* /g, "- ");
      return parent === "multiply" || parent === "power" ? `(${text})` : text;
    }
    case "multiply": {
      const text = node.args.map((arg) => expressionToText(arg, "multiply")).join(" * ");
      return parent === "power" ? `(${text})` : text;
    }
    case "divide": return `(${expressionToText(node.numerator)}) / (${expressionToText(node.denominator)})`;
    case "power": return `${expressionToText(node.base, "power")} ^ ${expressionToText(node.exponent, "power")}`;
    default: throw new Error(`Unsupported expression kind ${node.kind}.`);
  }
}

export function evaluateExpression(node, variables = {}) {
  switch (node.kind) {
    case "number": return node.value;
    case "symbol": {
      if (!(node.name in variables)) throw new Error(`Missing value for ${node.name}.`);
      return variables[node.name];
    }
    case "add": return node.args.reduce((sum, item) => sum + evaluateExpression(item, variables), 0);
    case "multiply": return node.args.reduce((product, item) => product * evaluateExpression(item, variables), 1);
    case "divide": return evaluateExpression(node.numerator, variables) / evaluateExpression(node.denominator, variables);
    case "power": return evaluateExpression(node.base, variables) ** evaluateExpression(node.exponent, variables);
    default: throw new Error(`Unsupported expression kind ${node.kind}.`);
  }
}

function collectSymbols(node, result = new Set()) {
  if (node.kind === "symbol") result.add(node.name);
  for (const child of node.args ?? []) collectSymbols(child, result);
  if (node.base) collectSymbols(node.base, result);
  if (node.exponent) collectSymbols(node.exponent, result);
  if (node.numerator) collectSymbols(node.numerator, result);
  if (node.denominator) collectSymbols(node.denominator, result);
  return result;
}

function equivalent(left, right) {
  const symbols = [...new Set([...collectSymbols(left), ...collectSymbols(right)])];
  const samples = [-3, -1, 0, 1, 2, 4, 7];
  for (let i = 0; i < samples.length; i += 1) {
    const vars = Object.fromEntries(symbols.map((symbol, index) => [symbol, samples[(i + index) % samples.length]]));
    const a = evaluateExpression(left, vars);
    const b = evaluateExpression(right, vars);
    if (!Number.isFinite(a) || !Number.isFinite(b) || Math.abs(a - b) > 1e-9 * Math.max(1, Math.abs(a), Math.abs(b))) return false;
  }
  return true;
}

export class MathAdapter extends DisposableAdapter {
  constructor() {
    super({ id: "reference-semantic-math", family: "semantic-mathematics" });
  }

  interpret(input) {
    try {
      const ast = parseExpression(input);
      return { state: "valid", ast, preview: expressionToText(ast), issues: [] };
    } catch (error) {
      return { state: "invalid", ast: null, preview: null, issues: [{ code: "parse-error", message: error.message, position: error.position ?? null }] };
    }
  }

  importOriginalInput(input) {
    const interpreted = this.interpret(input);
    this.response = {
      ...(this.response ?? { id: "math-response" }),
      inputFormat: "infix-text",
      originalInput: input,
      submittedExpression: interpreted.ast,
    };
    this.derivedState.interpretation = interpreted;
    return interpreted;
  }

  async validate() {
    const input = this.response?.originalInput ?? "";
    const interpretation = this.interpret(input);
    if (interpretation.state === "invalid") {
      return buildValidation({
        validity: { state: "invalid", issues: interpretation.issues },
        authority: "deterministic-validator",
        evidence: { interpretationPreview: null },
        feedback: [{ kind: "interpretation-preview", content: "A expressão ainda não pôde ser interpretada." }],
      });
    }
    const allowed = new Set(this.instance.representation.variables ?? []);
    const undeclared = [...collectSymbols(interpretation.ast)].filter((symbol) => !allowed.has(symbol));
    if (undeclared.length) {
      return buildValidation({
        validity: { state: "invalid", issues: [{ code: "undeclared-symbol", symbols: undeclared }] },
        authority: "deterministic-validator",
        evidence: { interpretationPreview: interpretation.preview },
      });
    }
    const criteria = this.instance.validator.propertyTests.map((test) => {
      if (test.test === "equivalent-to-reference") {
        return { criterionId: test.criterionId, state: equivalent(interpolation(test.referenceExpression), interpretation.ast) ? "satisfied" : "not-satisfied", weight: test.weight };
      }
      if (test.test === "required-form") {
        const factorized = interpretation.ast.kind === "multiply" && interpretation.ast.args.length >= 2 && interpretation.ast.args.some((arg) => arg.kind === "add");
        return { criterionId: test.criterionId, state: factorized ? "satisfied" : "not-satisfied", weight: test.weight };
      }
      return { criterionId: test.criterionId, state: "unsupported", weight: test.weight };
    });
    return buildValidation({
      validity: { state: "valid", issues: [] },
      criteria,
      authority: "deterministic-validator",
      evidence: { interpretationPreview: interpretation.preview, semanticExpression: deepClone(interpretation.ast) },
      feedback: [{ kind: "interpretation-preview", content: `Interpretação: ${interpretation.preview}` }],
    });
  }
}

function interpolation(value) {
  return deepClone(value);
}
