import { DisposableAdapter, buildValidation, deepClone } from "../core/adapter.mjs";

function normalizePair(a, b, directed = false) {
  return directed || a <= b ? [a, b] : [b, a];
}

function edgeKey(edge) {
  return normalizePair(edge.from, edge.to, edge.directed).join("→");
}

export class RelationalAdapter extends DisposableAdapter {
  constructor() {
    super({ id: "reference-relational-construction", family: "relational-construction" });
  }

  load(instance) {
    super.load(instance);
    if (!this.response?.finalState) {
      this.response = {
        id: "relational-response",
        finalState: deepClone(instance.representation.initialState),
        operationLog: [],
      };
    }
    this.derivedState.layout = this.#deriveLayout();
    return this.snapshot();
  }

  addEdge(from, to, id = `e${this.response.finalState.edges.length + 1}`) {
    const nodes = new Set(this.response.finalState.nodes.map((node) => node.id));
    if (!nodes.has(from) || !nodes.has(to)) throw new Error("Edge endpoint does not exist.");
    const edge = { id, from, to, directed: false, label: `${from}–${to}` };
    if (this.response.finalState.edges.some((candidate) => edgeKey(candidate) === edgeKey(edge))) return false;
    this.response.finalState.edges.push(edge);
    this.response.operationLog.push({ sequence: this.response.operationLog.length + 1, operation: "add-edge", targetIds: [from, to], value: { edgeId: id } });
    this.derivedState.layout = this.#deriveLayout();
    return true;
  }

  removeEdge(from, to) {
    const key = normalizePair(from, to).join("→");
    const before = this.response.finalState.edges.length;
    this.response.finalState.edges = this.response.finalState.edges.filter((edge) => edgeKey(edge) !== key);
    if (before !== this.response.finalState.edges.length) {
      this.response.operationLog.push({ sequence: this.response.operationLog.length + 1, operation: "remove-edge", targetIds: [from, to] });
      return true;
    }
    return false;
  }

  exportResponse() {
    const output = super.exportResponse();
    for (const node of output.finalState.nodes) {
      delete node.x;
      delete node.y;
      delete node.position;
    }
    for (const edge of output.finalState.edges) delete edge.position;
    delete output.layout;
    delete output.rendererState;
    return output;
  }

  getDerivedLayout() {
    return deepClone(this.derivedState.layout);
  }

  async validate() {
    const state = this.response.finalState;
    const issues = [];
    const nodeIds = state.nodes.map((node) => node.id);
    if (new Set(nodeIds).size !== nodeIds.length) issues.push({ code: "duplicate-node-id" });
    const edgeIds = state.edges.map((edge) => edge.id);
    if (new Set(edgeIds).size !== edgeIds.length) issues.push({ code: "duplicate-edge-id" });
    const nodeSet = new Set(nodeIds);
    if (state.edges.some((edge) => !nodeSet.has(edge.from) || !nodeSet.has(edge.to))) issues.push({ code: "missing-endpoint" });
    const allowed = new Set(this.instance.activity.allowedOperations ?? []);
    if (this.response.operationLog.some((operation) => !allowed.has(operation.operation))) issues.push({ code: "operation-not-allowed" });
    if (issues.length) return buildValidation({ validity: { state: "invalid", issues }, authority: "deterministic-validator" });

    const criteria = this.instance.validator.predicates.map((predicate) => {
      let satisfied = false;
      if (predicate.predicate === "path-exists") {
        satisfied = pathExists(state, predicate.parameters.from, predicate.parameters.to, predicate.parameters.maxEdges);
      } else if (predicate.predicate === "edge-set-equals") {
        const expected = new Set(predicate.parameters.edges.map(([a, b]) => normalizePair(a, b).join("→")));
        const actual = new Set(state.edges.map(edgeKey));
        satisfied = expected.size === actual.size && [...expected].every((key) => actual.has(key));
      }
      return { criterionId: predicate.criterionId, state: satisfied ? "satisfied" : "not-satisfied", weight: predicate.weight };
    });
    return buildValidation({
      validity: { state: "valid", issues: [] },
      criteria,
      authority: "deterministic-validator",
      evidence: { semanticState: this.exportResponse().finalState, rendererGeometryCanonical: false },
      feedback: [{ kind: "structural-status", content: `${state.edges.length} aresta(s) na resposta semântica.` }],
    });
  }

  #deriveLayout() {
    const nodes = this.response?.finalState?.nodes ?? [];
    return Object.fromEntries(nodes.map((node, index) => {
      const angle = (Math.PI * 2 * index) / Math.max(1, nodes.length) - Math.PI / 2;
      return [node.id, { x: 150 + 100 * Math.cos(angle), y: 130 + 90 * Math.sin(angle) }];
    }));
  }
}

function pathExists(state, from, to, maxEdges = Infinity) {
  const adjacency = new Map(state.nodes.map((node) => [node.id, []]));
  for (const edge of state.edges) {
    adjacency.get(edge.from)?.push(edge.to);
    if (!edge.directed) adjacency.get(edge.to)?.push(edge.from);
  }
  const queue = [[from, 0]];
  const seen = new Set([from]);
  while (queue.length) {
    const [node, distance] = queue.shift();
    if (node === to) return distance <= maxEdges;
    if (distance >= maxEdges) continue;
    for (const next of adjacency.get(node) ?? []) {
      if (!seen.has(next)) {
        seen.add(next);
        queue.push([next, distance + 1]);
      }
    }
  }
  return false;
}
