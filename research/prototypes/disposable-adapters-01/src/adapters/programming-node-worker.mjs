import { parentPort, workerData } from "node:worker_threads";
import vm from "node:vm";

const output = [];
const safeConsole = Object.freeze({
  log: (...items) => {
    if (output.length >= workerData.outputLimit) throw new Error("OUTPUT_LIMIT");
    output.push(items.map(String).join(" "));
  },
});

try {
  const context = vm.createContext({ console: safeConsole, globalThis: null });
  context.globalThis = context;
  const exportNames = workerData.functionNames;
  const source = `"use strict";\n${workerData.code}\n;globalThis.__araExports = {${exportNames.join(",")}};`;
  const script = new vm.Script(source, { filename: "learner.js" });
  script.runInContext(context, { timeout: workerData.timeLimitMs });
  const exported = context.__araExports;
  const results = workerData.tests.map((test) => {
    const fn = exported[test.functionName];
    if (typeof fn !== "function") return { testId: test.testId, state: "failed", error: "FUNCTION_MISSING" };
    try {
      const actual = fn(...test.args);
      const passed = JSON.stringify(actual) === JSON.stringify(test.expected);
      return { testId: test.testId, state: passed ? "passed" : "failed", actual, expected: test.expected };
    } catch (error) {
      return { testId: test.testId, state: "error", error: error.message };
    }
  });
  parentPort.postMessage({ state: "completed", output, results });
} catch (error) {
  parentPort.postMessage({ state: "runtime-error", output, error: error.message, name: error.name });
}
