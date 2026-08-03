import { MathAdapter } from "../adapters/math-adapter.mjs";
import { RelationalAdapter } from "../adapters/relational-adapter.mjs";
import { SourceArgumentAdapter } from "../adapters/source-argument-adapter.mjs";
import { mathInstance, relationalInstance, programmingInstance, createSourceInstance } from "./fixtures.js";

const clone = (value) => structuredClone(value);
const pretty = (value) => JSON.stringify(value, null, 2);

const math = new MathAdapter();
math.load(mathInstance); math.start();
document.querySelector("#math-input").addEventListener("input", (event) => math.importOriginalInput(event.target.value));
document.querySelector("#math-validate").addEventListener("click", async () => {
  math.importOriginalInput(document.querySelector("#math-input").value);
  const result = await math.validate();
  document.querySelector("#math-preview").value = result.evidence.interpretationPreview ?? "não interpretada";
  document.querySelector("#math-status").textContent = statusText(result.finalState, "A expressão está correta e na forma solicitada.");
  document.querySelector("#math-json").textContent = pretty(math.exportResponse());
});

const graph = new RelationalAdapter();
graph.load(relationalInstance); graph.start();
for (const select of [document.querySelector("#edge-from"), document.querySelector("#edge-to")]) {
  for (const node of relationalInstance.representation.initialState.nodes) select.add(new Option(node.label, node.id));
}
document.querySelector("#edge-to").value = "B";
document.querySelector("#edge-add").addEventListener("click", () => {
  const added = graph.addEdge(document.querySelector("#edge-from").value, document.querySelector("#edge-to").value);
  renderGraph(); announce("graph-status", added ? "Aresta adicionada." : "A aresta já existe.");
});
document.querySelector("#edge-remove").addEventListener("click", () => {
  const removed = graph.removeEdge(document.querySelector("#edge-from").value, document.querySelector("#edge-to").value);
  renderGraph(); announce("graph-status", removed ? "Aresta removida." : "A aresta não existe.");
});
document.querySelector("#graph-validate").addEventListener("click", async () => {
  const result = await graph.validate();
  announce("graph-status", statusText(result.finalState, "A construção está correta."));
  renderGraph();
});

function renderGraph() {
  const svg = document.querySelector("#graph-svg");
  [...svg.querySelectorAll("g")].forEach((element) => element.remove());
  const ns = "http://www.w3.org/2000/svg";
  const group = document.createElementNS(ns, "g");
  const response = graph.exportResponse();
  const layout = graph.getDerivedLayout();
  for (const edge of response.finalState.edges) {
    const line = document.createElementNS(ns, "line");
    Object.assign(line, {});
    line.setAttribute("x1", layout[edge.from].x); line.setAttribute("y1", layout[edge.from].y);
    line.setAttribute("x2", layout[edge.to].x); line.setAttribute("y2", layout[edge.to].y);
    line.setAttribute("stroke", "currentColor"); line.setAttribute("stroke-width", "3");
    group.append(line);
  }
  for (const node of response.finalState.nodes) {
    const circle = document.createElementNS(ns, "circle");
    circle.setAttribute("cx", layout[node.id].x); circle.setAttribute("cy", layout[node.id].y); circle.setAttribute("r", "22");
    circle.setAttribute("fill", "Canvas"); circle.setAttribute("stroke", "currentColor"); circle.setAttribute("stroke-width", "2");
    const text = document.createElementNS(ns, "text");
    text.setAttribute("x", layout[node.id].x); text.setAttribute("y", layout[node.id].y + 5); text.setAttribute("text-anchor", "middle"); text.textContent = node.label;
    group.append(circle, text);
  }
  svg.append(group);
  const list = document.querySelector("#edge-list");
  list.replaceChildren(...response.finalState.edges.map((edge) => Object.assign(document.createElement("li"), { textContent: `${edge.from}–${edge.to}` })));
  if (!response.finalState.edges.length) list.append(Object.assign(document.createElement("li"), { textContent: "Nenhuma aresta." }));
  document.querySelector("#graph-json").textContent = pretty(response);
}
renderGraph();

let activeBrowserWorker = null;
const publicTests = programmingInstance.validator.testSuites[0].tests.map((test) => ({ testId: test.testId, functionName: test.functionName, args: [test.input], expected: test.expected }));
document.querySelector("#code-run").addEventListener("click", async () => {
  const code = document.querySelector("#code-input").value;
  programmingInstance.response.files[0].content = code;
  document.querySelector("#code-json").textContent = pretty(programmingInstance.response);
  announce("code-status", "Executando testes públicos…");
  const result = await runBrowserCode(code, publicTests, programmingInstance.runtimeRequirements.timeLimitMs);
  if (result.state === "timeout") announce("code-status", "Execução interrompida por limite de tempo.");
  else if (result.state === "runtime-error") announce("code-status", `${result.name === "SyntaxError" ? "Entrada inválida" : "Erro de runtime"}: ${result.error}`);
  else {
    const allPass = result.results.every((test) => test.state === "passed");
    announce("code-status", allPass ? "Testes públicos corretos. A suíte protegida permanece fora do cliente." : "Há falhas nos testes públicos.");
  }
  document.querySelector("#code-output").textContent = pretty(result);
});
document.querySelector("#code-stop").addEventListener("click", () => {
  activeBrowserWorker?.terminate(); activeBrowserWorker = null; announce("code-status", "Execução interrompida pelo estudante.");
});

function runBrowserCode(code, tests, timeLimitMs) {
  return new Promise((resolve) => {
    const worker = new Worker(new URL("./programming-worker.js", import.meta.url));
    activeBrowserWorker = worker;
    const timer = setTimeout(() => { worker.terminate(); activeBrowserWorker = null; resolve({ state: "timeout" }); }, timeLimitMs + 100);
    worker.onmessage = (event) => { clearTimeout(timer); worker.terminate(); activeBrowserWorker = null; resolve(event.data); };
    worker.onerror = (event) => { clearTimeout(timer); worker.terminate(); activeBrowserWorker = null; resolve({ state: "runtime-error", name: "WorkerError", error: event.message }); };
    worker.postMessage({ code, tests, functionNames: ["sumEven"], outputLimit: 64 });
  });
}

const sourceInstance = await createSourceInstance();
const source = new SourceArgumentAdapter();
source.load(sourceInstance); source.start();
const sourceText = document.querySelector("#source-text");
sourceText.value = sourceInstance.representation.sources[0].content;
let currentAnnotation = null;
document.querySelector("#capture-selection").addEventListener("click", () => {
  const start = sourceText.selectionStart; const end = sourceText.selectionEnd;
  if (start === end) { announce("source-status", "Selecione um trecho antes de continuar."); return; }
  currentAnnotation = source.createAnnotation({ sourceId: "src-1", start, end, body: document.querySelector("#annotation-body").value });
  document.querySelector("#selected-quote").value = currentAnnotation.selector.quote;
  document.querySelector("#source-json").textContent = pretty(source.exportResponse());
  announce("source-status", "Trecho selecionado e registrado.");
});
document.querySelector("#source-validate").addEventListener("click", async () => {
  if (!currentAnnotation) { announce("source-status", "Registre uma evidência primeiro."); return; }
  source.response.annotations[0].body = document.querySelector("#annotation-body").value;
  source.setArgument({ claim: document.querySelector("#claim-input").value, reason: document.querySelector("#reason-input").value, annotationId: currentAnnotation.id });
  const result = await source.validate();
  announce("source-status", result.finalState === "review-required" ? "Integridade confirmada. Qualidade argumentativa enviada para revisão humana." : statusText(result.finalState));
  document.querySelector("#source-json").textContent = pretty(source.exportResponse());
});

function announce(id, text) { document.querySelector(`#${id}`).textContent = text; }
function statusText(state, correct = "Resposta correta.") {
  return ({ correct, partial: "Resposta válida e parcialmente satisfatória.", incorrect: "Resposta válida, mas incorreta.", invalid: "Resposta inválida; corrija a interpretação ou a estrutura.", unsupported: "Capacidade não disponível neste adapter.", "review-required": "Resposta válida e aguardando revisão." })[state] ?? state;
}

window.__araAdapters = { math, graph, source, programmingInstance, runBrowserCode, clone };
