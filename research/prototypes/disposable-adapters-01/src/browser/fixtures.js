export const mathInstance = {
  contract: "ara.component-prototype", version: "0.1.0", componentRef: "org.ara.prototype.semantic-expression@0.1.0", family: "semantic-mathematics",
  representation: { kind: "semantic-expression", languageTag: "pt-BR", expression: { kind: "add", args: [{ kind: "multiply", args: [{ kind: "number", value: 2 }, { kind: "symbol", name: "x" }] }, { kind: "number", value: 6 }] }, variables: ["x"] },
  activity: { id: "math-factor", objective: "Produzir forma fatorada equivalente.", phase: "independent-practice", operation: "factor", prompt: "Escreva uma forma fatorada equivalente a 2x + 6." },
  response: { id: "math-response", inputFormat: "infix-text", originalInput: "2*(x+3)", submittedExpression: null },
  validator: { id: "math-validator", propertyTests: [{ criterionId: "equivalence", test: "equivalent-to-reference", referenceExpression: { kind: "add", args: [{ kind: "multiply", args: [{ kind: "number", value: 2 }, { kind: "symbol", name: "x" }] }, { kind: "number", value: 6 }] }, weight: 0.7 }, { criterionId: "factorized-form", test: "required-form", requiredForm: "factorized", weight: 0.3 }] },
  feedback: { items: [], scoreIndependent: true, retryPolicy: "unlimited-formative" }
};

export const relationalInstance = {
  contract: "ara.component-prototype", version: "0.1.0", componentRef: "org.ara.prototype.relational-construction@0.1.0", family: "relational-construction",
  representation: { kind: "relational-construction", initialState: { grammar: "graph-theory", nodes: ["A","B","C","D"].map((id) => ({ id, kind: "vertex", label: id })), edges: [], semanticConstraints: ["simple-undirected-graph"] }, rendererPolicy: { persistCoordinates: false, layoutAuthority: "renderer-derived" } },
  activity: { id: "graph-path", objective: "Construir caminho A–B–D.", phase: "guided-practice", operation: "construct-path", prompt: "Adicione A–B e B–D.", allowedOperations: ["add-edge", "remove-edge"] },
  response: { id: "graph-response", finalState: { grammar: "graph-theory", nodes: ["A","B","C","D"].map((id) => ({ id, kind: "vertex", label: id })), edges: [], semanticConstraints: ["simple-undirected-graph"] }, operationLog: [] },
  validator: { id: "graph-validator", predicates: [{ criterionId: "path-a-d", predicate: "path-exists", parameters: { from: "A", to: "D", maxEdges: 2 }, weight: 0.6 }, { criterionId: "exact-edges", predicate: "edge-set-equals", parameters: { edges: [["A","B"],["B","D"]] }, weight: 0.4 }] },
  feedback: { items: [], scoreIndependent: true, retryPolicy: "unlimited-formative" }
};

export const programmingInstance = {
  contract: "ara.component-prototype", version: "0.1.0", componentRef: "org.ara.prototype.executable-javascript@0.1.0", family: "executable-programming",
  representation: { kind: "code-workspace", language: "javascript", runtimeProfile: "browser-worker-javascript", files: [{ path: "main.js", content: "function sumEven(values) {\n  return 0;\n}\n", editable: true, language: "javascript" }], entryPoint: "main.js", problemStatement: "Implemente sumEven." },
  response: { id: "code-response", files: [{ path: "main.js", content: "function sumEven(values) {\n  return 0;\n}\n", editable: true, language: "javascript" }], requestedRun: true },
  validator: { testSuites: [{ suiteId: "public", visibility: "public", tests: [{ testId: "basic", functionName: "sumEven", input: [1,2,3,4], expected: 6 }] }], hiddenTestsProtected: true },
  runtimeRequirements: { timeLimitMs: 500 }
};

export const sourceContent = "A biblioteca deve ampliar o horário. Muitos estudantes trabalham durante o dia e só conseguem estudar à noite.";

export async function createSourceInstance() {
  const digest = "sha256:90a00fed32303f2d62c117342309e5ed97fcb4eb1a83285867d1d5fbe068f9b1";
  return {
    contract: "ara.component-prototype", version: "0.1.0", componentRef: "org.ara.prototype.source-argument@0.1.0", family: "source-argument",
    representation: { kind: "source-set", sources: [{ id: "src-1", title: "Proposta de ampliação", languageTag: "pt-BR", content: sourceContent, digest, citation: "Fonte didática." }] },
    response: { id: "source-response", annotations: [], argumentNodes: [], links: [] },
    validator: { rubricCriteria: [{ criterionId: "relevance", authority: "human-review", weight: 0.4 }, { criterionId: "warrant", authority: "human-review", weight: 0.6 }] },
    feedback: { items: [], scoreIndependent: true, retryPolicy: "author-configured" }
  };
}
