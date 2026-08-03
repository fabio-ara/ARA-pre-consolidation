import test from "node:test";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { exportMathLiveResponse, importMathLiveState } from "../src/mathlive-boundary-adapter.mjs";
import { exportCytoscapeResponse, importCytoscapeElements } from "../src/cytoscape-boundary-adapter.mjs";
import { exportRecogitoResponse, importRecogitoAnnotations } from "../src/recogito-boundary-adapter.mjs";
import { mathLiveState, cytoscapeElements, recogitoAnnotations } from "../fixtures/external-states.mjs";

const contractRoot = new URL("../../component-contracts-02/", import.meta.url);
const families = ["semantic-mathematics", "relational-construction", "executable-programming", "source-argument"];
const instances = await Promise.all(families.map(async (family) =>
  JSON.parse(await readFile(new URL(`examples/instances/${family}.json`, contractRoot), "utf8"))
));
const byFamily = Object.fromEntries(instances.map((instance) => [instance.family, instance]));

test("MathLive-oriented state exports only ARA canonical response fields", () => {
  const base = byFamily["semantic-mathematics"].response;
  const response = exportMathLiveResponse({ baseResponse: base, mathfieldState: mathLiveState });
  assert.equal(response.submittedExpression.kind, "multiply");
  assert.equal(JSON.stringify(response).includes("virtualKeyboardVisible"), false);
  assert.equal(JSON.stringify(response).includes("selection"), false);
  assert.deepEqual(importMathLiveState(response).mathJson, mathLiveState.mathJson);
});

test("Cytoscape-oriented state strips renderer geometry and library state", () => {
  const base = byFamily["relational-construction"].response;
  const response = exportCytoscapeResponse({ baseResponse: base, elements: cytoscapeElements });
  const serialized = JSON.stringify(response);
  for (const forbidden of ["position", "selected", "classes", "style", "scratch"]) {
    assert.equal(serialized.includes(`"${forbidden}"`), false);
  }
  assert.deepEqual(response.finalState.edges.map((edge) => [edge.from, edge.to]), [["A", "B"], ["B", "D"]]);
  const imported = importCytoscapeElements(response, { A: { x: 1, y: 2 } });
  assert.deepEqual(imported.find((item) => item.data.id === "A").position, { x: 1, y: 2 });
  assert.equal("position" in response.finalState.nodes[0], false);
});

test("Recogito-oriented annotations map W3C selectors without DOM state", () => {
  const base = byFamily["source-argument"].response;
  const sourceDigest = byFamily["source-argument"].representation.sources[0].digest;
  const response = exportRecogitoResponse({
    baseResponse: base,
    annotations: recogitoAnnotations,
    sourceByTarget: { "dom:#source-1": { sourceId: "src-1", sourceDigest } },
  });
  const annotation = response.annotations[0];
  assert.equal(annotation.selector.quote, "Muitos estudantes trabalham durante o dia");
  assert.equal(annotation.selector.sourceDigest, sourceDigest);
  assert.equal(JSON.stringify(response).includes("internalStoreState"), false);
  const imported = importRecogitoAnnotations(response, { "src-1": "dom:#source-1" });
  assert.equal(imported[0].target.selector[0].type, "TextQuoteSelector");
});

test("external adapter replacement does not change canonical course documents", () => {
  const originalCourseSide = instances.map(({ response, ...courseSide }) => courseSide);
  exportMathLiveResponse({ baseResponse: byFamily["semantic-mathematics"].response, mathfieldState: mathLiveState });
  exportCytoscapeResponse({ baseResponse: byFamily["relational-construction"].response, elements: cytoscapeElements });
  exportRecogitoResponse({
    baseResponse: byFamily["source-argument"].response,
    annotations: recogitoAnnotations,
    sourceByTarget: {
      "dom:#source-1": {
        sourceId: "src-1",
        sourceDigest: byFamily["source-argument"].representation.sources[0].digest,
      },
    },
  });
  const after = instances.map(({ response, ...courseSide }) => courseSide);
  assert.deepEqual(after, originalCourseSide);
});
