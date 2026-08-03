export function mathJsonToAra(value) {
  if (typeof value === "number") return { kind: "number", value };
  if (typeof value === "string") return { kind: "symbol", name: value };
  if (!Array.isArray(value) || value.length === 0) throw new Error("Unsupported MathJSON value.");
  const [head, ...args] = value;
  const mapped = args.map(mathJsonToAra);
  if (head === "Add") return { kind: "add", args: mapped };
  if (head === "Multiply") return { kind: "multiply", args: mapped };
  if (head === "Power" && mapped.length === 2) return { kind: "power", base: mapped[0], exponent: mapped[1] };
  if (head === "Divide" && mapped.length === 2) return { kind: "divide", numerator: mapped[0], denominator: mapped[1] };
  throw new Error(`Unsupported MathJSON head ${String(head)}.`);
}

export function araToMathJson(node) {
  if (node.kind === "number") return node.value;
  if (node.kind === "symbol") return node.name;
  if (node.kind === "add") return ["Add", ...node.args.map(araToMathJson)];
  if (node.kind === "multiply") return ["Multiply", ...node.args.map(araToMathJson)];
  if (node.kind === "power") return ["Power", araToMathJson(node.base), araToMathJson(node.exponent)];
  if (node.kind === "divide") return ["Divide", araToMathJson(node.numerator), araToMathJson(node.denominator)];
  throw new Error(`Unsupported ARA expression kind ${node.kind}.`);
}

export function exportMathLiveResponse({ baseResponse, mathfieldState }) {
  const response = structuredClone(baseResponse);
  response.inputFormat = "math-json";
  response.originalInput = String(mathfieldState.latex ?? "");
  response.submittedExpression = mathJsonToAra(mathfieldState.mathJson);
  response.interpretationPreview = String(mathfieldState.spokenText ?? mathfieldState.latex ?? "");
  // Selection, virtual-keyboard state, menu state and DOM references are intentionally excluded.
  return response;
}

export function importMathLiveState(response) {
  return {
    latex: response.originalInput,
    mathJson: araToMathJson(response.submittedExpression),
  };
}
