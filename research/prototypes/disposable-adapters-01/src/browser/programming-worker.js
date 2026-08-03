self.fetch = undefined;
self.XMLHttpRequest = undefined;
self.WebSocket = undefined;
self.importScripts = undefined;

self.onmessage = (event) => {
  const { code, tests, functionNames, outputLimit } = event.data;
  const output = [];
  const safeConsole = {
    log: (...items) => {
      if (output.length >= outputLimit) throw new Error("OUTPUT_LIMIT");
      output.push(items.map(String).join(" "));
    },
  };
  try {
    const factory = new Function("console", `"use strict";\n${code}\n;return {${functionNames.join(",")}};`);
    const exported = factory(safeConsole);
    const results = tests.map((test) => {
      const fn = exported[test.functionName];
      if (typeof fn !== "function") return { testId: test.testId, state: "failed", error: "FUNCTION_MISSING" };
      try {
        const actual = fn(...test.args);
        return { testId: test.testId, state: JSON.stringify(actual) === JSON.stringify(test.expected) ? "passed" : "failed", actual, expected: test.expected };
      } catch (error) {
        return { testId: test.testId, state: "error", error: error.message };
      }
    });
    self.postMessage({ state: "completed", output, results });
  } catch (error) {
    self.postMessage({ state: "runtime-error", output, error: error.message, name: error.name });
  }
};
