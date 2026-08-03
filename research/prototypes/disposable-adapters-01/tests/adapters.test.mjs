import test from "node:test";
import assert from "node:assert/strict";
import { MathAdapter } from "../src/adapters/math-adapter.mjs";
import { RelationalAdapter } from "../src/adapters/relational-adapter.mjs";
import { ProgrammingAdapter } from "../src/adapters/programming-adapter.mjs";
import { SourceArgumentAdapter, resolveSelector } from "../src/adapters/source-argument-adapter.mjs";
import { mathInstance, relationalInstance, programmingInstance, sourceInstance, protectedProgrammingTests } from "../fixtures/instances.mjs";

function active(adapter, instance) { adapter.load(instance); adapter.start(); return adapter; }

test("math separates invalid syntax, interpretation and correctness", async () => {
  const adapter = active(new MathAdapter(), mathInstance);
  adapter.importOriginalInput("2*(x+");
  assert.equal((await adapter.validate()).finalState, "invalid");
  adapter.importOriginalInput("2*x+6");
  assert.equal((await adapter.validate()).finalState, "partial");
  adapter.importOriginalInput("2*(x+3)");
  const result = await adapter.validate();
  assert.equal(result.finalState, "correct");
  assert.match(result.evidence.interpretationPreview, /x \+ 3/);
});

test("relational response round-trips without renderer geometry", async () => {
  const adapter = active(new RelationalAdapter(), relationalInstance);
  adapter.addEdge("A", "B");
  adapter.addEdge("B", "D");
  const exported = adapter.exportResponse();
  assert.equal(JSON.stringify(exported).includes('"x"'), false);
  assert.equal(JSON.stringify(exported).includes("renderer"), false);
  assert.equal((await adapter.validate()).finalState, "correct");
  const clone = active(new RelationalAdapter(), relationalInstance);
  clone.importResponse(exported);
  assert.deepEqual(clone.exportResponse(), exported);
});

test("programming keeps protected tests out of exported response", async () => {
  const adapter = active(new ProgrammingAdapter({ protectedTests: protectedProgrammingTests }), programmingInstance);
  adapter.response.files[0].content = "function sumEven(values) { return values.filter(v => v % 2 === 0).reduce((a,b) => a+b, 0); }";
  const result = await adapter.validate();
  assert.equal(result.finalState, "correct");
  const exported = JSON.stringify(adapter.exportResponse());
  assert.equal(exported.includes("negative"), false);
  assert.equal(exported.includes("protected"), false);
  assert.equal(result.evidence.protectedTestsExported, false);
});

test("programming distinguishes parse error, test failure and timeout", async () => {
  const adapter = active(new ProgrammingAdapter({ protectedTests: protectedProgrammingTests }), programmingInstance);
  adapter.response.files[0].content = "function sumEven(values) {";
  assert.equal((await adapter.validate()).finalState, "invalid");
  adapter.response.files[0].content = "function sumEven(values) { return 0; }";
  assert.equal((await adapter.validate()).finalState, "partial");
  adapter.response.files[0].content = "while (true) {}\nfunction sumEven(values) { return 0; }";
  const timed = await adapter.validate();
  assert.equal(timed.validity.issues[0].code, "runtime-timeout");
});

test("source selector re-resolves and defers quality to human review", async () => {
  const adapter = active(new SourceArgumentAdapter(), sourceInstance);
  const source = sourceInstance.representation.sources[0];
  const start = source.content.indexOf("Muitos estudantes");
  const annotation = adapter.createAnnotation({ sourceId: source.id, start, end: start + "Muitos estudantes trabalham durante o dia".length, body: "Evidência sobre estudantes trabalhadores." });
  annotation.selector.start = 0;
  annotation.selector.end = annotation.selector.quote.length;
  adapter.response.annotations[0] = annotation;
  adapter.setArgument({ claim: "A biblioteca deve ampliar o horário.", reason: "O acesso noturno atende estudantes trabalhadores.", annotationId: annotation.id });
  const result = await adapter.validate();
  assert.equal(result.finalState, "review-required");
  assert.equal(result.evidence.selectors[0].resolution.method, "quote-context");
  assert.equal(resolveSelector(source.content, annotation.selector).state, "resolved");
});

test("all four adapters preserve canonical response round trips", () => {
  const cases = [
    [new MathAdapter(), mathInstance],
    [new RelationalAdapter(), relationalInstance],
    [new ProgrammingAdapter({ protectedTests: protectedProgrammingTests }), programmingInstance],
    [new SourceArgumentAdapter(), sourceInstance],
  ];
  for (const [adapter, instance] of cases) {
    active(adapter, instance);
    const exported = adapter.exportResponse();
    const clone = active(
      adapter instanceof MathAdapter ? new MathAdapter()
        : adapter instanceof RelationalAdapter ? new RelationalAdapter()
          : adapter instanceof ProgrammingAdapter ? new ProgrammingAdapter({ protectedTests: protectedProgrammingTests })
            : new SourceArgumentAdapter(),
      instance,
    );
    clone.importResponse(exported);
    assert.deepEqual(clone.exportResponse(), exported);
  }
});
