import { performance } from "node:perf_hooks";
import { stat, writeFile } from "node:fs/promises";
import { MathAdapter } from "../src/adapters/math-adapter.mjs";
import { RelationalAdapter } from "../src/adapters/relational-adapter.mjs";
import { ProgrammingAdapter } from "../src/adapters/programming-adapter.mjs";
import { SourceArgumentAdapter } from "../src/adapters/source-argument-adapter.mjs";
import { mathInstance, relationalInstance, programmingInstance, sourceInstance, protectedProgrammingTests } from "../fixtures/instances.mjs";

const entries = [
  ["semantic-mathematics", MathAdapter, mathInstance, "src/adapters/math-adapter.mjs"],
  ["relational-construction", RelationalAdapter, relationalInstance, "src/adapters/relational-adapter.mjs"],
  ["executable-programming", class extends ProgrammingAdapter { constructor(){ super({protectedTests: protectedProgrammingTests}); } }, programmingInstance, "src/adapters/programming-adapter.mjs"],
  ["source-argument", SourceArgumentAdapter, sourceInstance, "src/adapters/source-argument-adapter.mjs"],
];
const rows = [];
for (const [family, Adapter, instance, path] of entries) {
  const before = process.memoryUsage().heapUsed;
  const start = performance.now();
  for (let i = 0; i < 500; i += 1) {
    const adapter = new Adapter();
    adapter.load(instance);
    adapter.start();
    adapter.exportResponse();
    adapter.dispose();
  }
  const elapsed = performance.now() - start;
  const after = process.memoryUsage().heapUsed;
  const bytes = (await stat(new URL(`../${path}`, import.meta.url))).size;
  rows.push({ family, sourceBytes: bytes, meanLifecycleMs: elapsed / 500, heapDeltaBytes: after - before, externalRuntimeBytes: 0, networkDuringStudy: "none" });
}
await writeFile(new URL("../reports/measurements.json", import.meta.url), JSON.stringify({ environment: { node: process.version, platform: process.platform, architecture: process.arch }, iterations: 500, rows }, null, 2));
console.log(JSON.stringify(rows, null, 2));
