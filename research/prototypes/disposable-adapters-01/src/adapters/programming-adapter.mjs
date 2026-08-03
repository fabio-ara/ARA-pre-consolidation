import { Worker } from "node:worker_threads";
import { DisposableAdapter, buildValidation } from "../core/adapter.mjs";

export class ProgrammingAdapter extends DisposableAdapter {
  constructor({ protectedTests = [] } = {}) {
    super({ id: "reference-executable-javascript", family: "executable-programming" });
    this.protectedTests = structuredClone(protectedTests);
  }

  exportResponse() {
    const response = super.exportResponse();
    delete response.protectedTests;
    delete response.runtimeInternals;
    return response;
  }

  async validate({ includeProtected = true } = {}) {
    const file = this.response?.files?.find((item) => item.path === this.instance.representation.entryPoint);
    if (!file) return buildValidation({ validity: { state: "invalid", issues: [{ code: "entry-point-missing" }] }, authority: "deterministic-validator" });
    const publicTests = flattenTests(this.instance.validator.testSuites.filter((suite) => suite.visibility === "public"));
    const protectedTests = includeProtected ? this.protectedTests : [];
    const allTests = [...publicTests, ...protectedTests];
    const result = await runWorker({
      code: file.content,
      tests: allTests,
      timeLimitMs: this.instance.runtimeRequirements.timeLimitMs ?? 1000,
      memoryLimitMiB: this.instance.runtimeRequirements.memoryLimitMiB ?? 32,
      outputLimit: 64,
    });
    if (result.state === "timeout") return buildValidation({ validity: { state: "invalid", issues: [{ code: "runtime-timeout" }] }, authority: "deterministic-validator", evidence: result });
    if (result.state === "runtime-error") {
      const parseLike = result.name === "SyntaxError";
      const timeoutLike = /timed out|timeout/i.test(result.error ?? "");
      return buildValidation({ validity: { state: "invalid", issues: [{ code: timeoutLike ? "runtime-timeout" : parseLike ? "parse-error" : "runtime-error", message: result.error }] }, authority: "deterministic-validator", evidence: result });
    }
    const criteria = result.results.map((test) => ({ criterionId: test.testId, state: test.state === "passed" ? "satisfied" : "not-satisfied", authority: "deterministic-validator" }));
    if (includeProtected && this.instance.validator.hiddenTestsProtected && this.protectedTests.length === 0) {
      criteria.push({ criterionId: "protected-suite", state: "unsupported", authority: "deterministic-validator" });
    }
    return buildValidation({
      validity: { state: "valid", issues: [] },
      criteria,
      authority: "deterministic-validator",
      evidence: { ...result, protectedTestCount: this.protectedTests.length, protectedTestsExported: false, isolationAssurance: "process-local-v8-isolate-not-security-sandbox" },
      feedback: result.results.filter((test) => test.state !== "passed").map((test) => ({ kind: "test-diagnostic", target: test.testId, content: test.error ?? `Esperado ${JSON.stringify(test.expected)}, obtido ${JSON.stringify(test.actual)}.` })),
    });
  }
}

function flattenTests(suites) {
  return suites.flatMap((suite) => suite.tests.map((test) => ({
    testId: test.testId,
    functionName: test.functionName ?? "sumEven",
    args: Array.isArray(test.input) && (test.input.length === 0 || !Array.isArray(test.input[0])) ? [test.input] : test.input ?? [],
    expected: test.expected,
  })));
}

function runWorker({ code, tests, timeLimitMs, memoryLimitMiB, outputLimit }) {
  return new Promise((resolve) => {
    const worker = new Worker(new URL("./programming-node-worker.mjs", import.meta.url), {
      workerData: {
        code,
        tests,
        functionNames: [...new Set(tests.map((test) => test.functionName))],
        timeLimitMs,
        outputLimit,
      },
      resourceLimits: {
        maxOldGenerationSizeMb: Math.max(8, Math.min(memoryLimitMiB, 64)),
        maxYoungGenerationSizeMb: 4,
        stackSizeMb: 2,
      },
    });
    const timer = setTimeout(async () => {
      await worker.terminate();
      resolve({ state: "timeout" });
    }, timeLimitMs + 100);
    worker.once("message", (message) => {
      clearTimeout(timer);
      resolve(message);
      worker.terminate();
    });
    worker.once("error", (error) => {
      clearTimeout(timer);
      resolve({ state: "runtime-error", error: error.message, name: error.name });
    });
  });
}
