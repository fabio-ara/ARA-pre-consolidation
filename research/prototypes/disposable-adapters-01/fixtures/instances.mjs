import { createHash } from "node:crypto";
const digest = (text) => `sha256:${createHash("sha256").update(text).digest("hex")}`;

export const mathInstance = {
  contract: "ara.component-prototype", version: "0.1.0", componentRef: "org.ara.prototype.semantic-expression@0.1.0", family: "semantic-mathematics",
  representation: { kind: "semantic-expression", languageTag: "pt-BR", expression: { kind: "add", args: [{ kind: "multiply", args: [{ kind: "number", value: 2 }, { kind: "symbol", name: "x" }] }, { kind: "number", value: 6 }] }, accessibleText: "dois x mais seis", variables: ["x"], assumptions: ["x is real"] },
  activity: { id: "math-factor", objective: "Produzir forma fatorada equivalente.", phase: "independent-practice", operation: "factor", prompt: "Escreva uma forma fatorada equivalente a 2x + 6.", scaffolds: [] },
  response: { id: "math-response", inputFormat: "infix-text", originalInput: "2*(x+3)", submittedExpression: null },
  validator: { id: "math-validator", validityChecks: ["parseable", "symbols-declared"], propertyTests: [{ criterionId: "equivalence", test: "equivalent-to-reference", referenceExpression: { kind: "add", args: [{ kind: "multiply", args: [{ kind: "number", value: 2 }, { kind: "symbol", name: "x" }] }, { kind: "number", value: 6 }] }, weight: 0.7 }, { criterionId: "factorized-form", test: "required-form", requiredForm: "factorized", weight: 0.3 }], authority: "deterministic-validator", interpretationPreviewRequired: true },
  feedback: { timing: "after-confirmation", items: [], scoreIndependent: true, retryPolicy: "unlimited-formative" },
  runtimeRequirements: { kind: "deterministic-local", network: "none", filesystem: "none", execution: "trusted-validator" }, securityBoundary: { courseSuppliedCode: "forbidden", learnerCode: "forbidden" }, accessibility: { keyboard: "required" }, offlineProfile: { grade: "full" }
};

export const relationalInstance = {
  contract: "ara.component-prototype", version: "0.1.0", componentRef: "org.ara.prototype.relational-construction@0.1.0", family: "relational-construction",
  representation: { kind: "relational-construction", initialState: { grammar: "graph-theory", nodes: ["A","B","C","D"].map((id) => ({ id, kind: "vertex", label: id })), edges: [], semanticConstraints: ["simple-undirected-graph"] }, rendererPolicy: { persistCoordinates: false, layoutAuthority: "renderer-derived" } },
  activity: { id: "graph-path", objective: "Construir caminho A–B–D.", phase: "guided-practice", operation: "construct-path", prompt: "Adicione A–B e B–D.", allowedOperations: ["add-edge", "remove-edge"], scaffolds: [] },
  response: { id: "graph-response", finalState: { grammar: "graph-theory", nodes: ["A","B","C","D"].map((id) => ({ id, kind: "vertex", label: id })), edges: [], semanticConstraints: ["simple-undirected-graph"] }, operationLog: [] },
  validator: { id: "graph-validator", structuralChecks: ["unique-ids", "endpoints-exist", "allowed-operations-only"], predicates: [{ criterionId: "path-a-d", predicate: "path-exists", parameters: { from: "A", to: "D", maxEdges: 2 }, weight: 0.6 }, { criterionId: "exact-edges", predicate: "edge-set-equals", parameters: { edges: [["A","B"],["B","D"]] }, weight: 0.4 }], authority: "deterministic-validator", validateSemanticStateOnly: true },
  feedback: { timing: "after-confirmation", items: [], scoreIndependent: true, retryPolicy: "unlimited-formative" },
  runtimeRequirements: { kind: "deterministic-local", network: "none", filesystem: "none", execution: "declarative" }, securityBoundary: { courseSuppliedCode: "forbidden", learnerCode: "forbidden" }, accessibility: { keyboard: "required", nonDragAlternative: "required" }, offlineProfile: { grade: "full" }
};

export const programmingInstance = {
  contract: "ara.component-prototype", version: "0.1.0", componentRef: "org.ara.prototype.executable-javascript@0.1.0", family: "executable-programming",
  representation: { kind: "code-workspace", language: "javascript", runtimeProfile: "browser-worker-javascript", files: [{ path: "main.js", content: "function sumEven(values) {\n  return 0;\n}\n", editable: true, language: "javascript" }], entryPoint: "main.js", publicTests: ["sumEven([1,2,3,4]) === 6"], problemStatement: "Implemente sumEven." },
  activity: { id: "code-implement", objective: "Implementar e testar função.", phase: "independent-practice", operation: "implement", prompt: "Some apenas inteiros pares.", scaffolds: [] },
  response: { id: "code-response", files: [{ path: "main.js", content: "function sumEven(values) {\n  return 0;\n}\n", editable: true, language: "javascript" }], requestedRun: true, stdin: [] },
  validator: { id: "code-validator", validityPipeline: ["decode", "parse", "resource-policy"], testSuites: [{ suiteId: "public", visibility: "public", tests: [{ testId: "basic", kind: "unit", functionName: "sumEven", input: [1,2,3,4], expected: 6 }], weight: 0.4 }, { suiteId: "protected", visibility: "protected", tests: [], weight: 0.6 }], authority: "deterministic-validator", hiddenTestsProtected: true, styleDiagnosticsAuthority: "non-final" },
  feedback: { timing: "after-attempt", items: [], scoreIndependent: true, retryPolicy: "unlimited-formative" },
  runtimeRequirements: { kind: "sandboxed-worker", network: "none", filesystem: "ephemeral-readwrite", execution: "sandboxed-code", timeLimitMs: 500, memoryLimitMiB: 32 }, securityBoundary: { courseSuppliedCode: "forbidden", learnerCode: "sandboxed" }, accessibility: { keyboard: "required" }, offlineProfile: { grade: "full" }
};

const sourceContent = "A biblioteca deve ampliar o horário. Muitos estudantes trabalham durante o dia e só conseguem estudar à noite.";
export const sourceInstance = {
  contract: "ara.component-prototype", version: "0.1.0", componentRef: "org.ara.prototype.source-argument@0.1.0", family: "source-argument",
  representation: { kind: "source-set", sources: [{ id: "src-1", title: "Proposta de ampliação", languageTag: "pt-BR", content: sourceContent, digest: digest(sourceContent), citation: "Fonte didática." }] },
  activity: { id: "source-argument", objective: "Selecionar evidência e justificar.", phase: "independent-practice", operation: "construct-argument", prompt: "Selecione evidência e formule uma razão.", rubricId: "rubric-1", scaffolds: [] },
  response: { id: "source-response", annotations: [], argumentNodes: [], links: [] },
  validator: { id: "source-validator", deterministicChecks: ["source-digest-matches", "selector-resolves", "links-resolve", "evidence-linked"], rubricCriteria: [{ criterionId: "relevance", description: "Evidência relevante.", authority: "human-review", weight: 0.4 }, { criterionId: "warrant", description: "Razão explica o vínculo.", authority: "human-review", weight: 0.6 }], finalAuthority: "human-review", probabilisticAssistanceAllowed: true, assistanceCannotFinalize: true },
  feedback: { timing: "after-review", items: [], scoreIndependent: true, retryPolicy: "author-configured" },
  runtimeRequirements: { kind: "human-review", network: "none", filesystem: "none", execution: "none" }, securityBoundary: { courseSuppliedCode: "forbidden", learnerCode: "forbidden" }, accessibility: { keyboard: "required" }, offlineProfile: { grade: "full" }
};

export const protectedProgrammingTests = [
  { testId: "negative", functionName: "sumEven", args: [[-4,-3,1,2]], expected: -2 },
  { testId: "empty", functionName: "sumEven", args: [[]], expected: 0 }
];
