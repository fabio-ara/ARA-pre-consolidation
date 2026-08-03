
import { readFile, writeFile } from "node:fs/promises";

const createdAt = "2026-08-03T04:45:00Z";

const familyPolicy = {
  "semantic-mathematics": {
    validationLocations: [
      { kind: "client-public", authority: "deterministic-validator", required: true, capabilityId: "semantic-math-validator" }
    ],
    runtimeKind: "deterministic-local",
    productionEligibility: "conditionally-eligible",
    availability: { state: "available", source: "component-manifest", evaluatedAt: createdAt },
    operations: [
      {
        operation: "enter-expression",
        keyboard: "Physical and virtual keyboard input.",
        nonvisual: "Semantic input with interpretation preview.",
        statusAnnouncement: "Announce parsed form and validity.",
        focusManagement: "Return focus to the first issue.",
        reflow: "Input and preview reflow.",
        knownLimits: ["Requires notation and locale testing."]
      }
    ],
    textAlternative: "Accessible reading of the canonical expression is required."
  },
  "relational-construction": {
    validationLocations: [
      { kind: "client-public", authority: "deterministic-validator", required: true, capabilityId: "relational-predicate-engine" }
    ],
    runtimeKind: "deterministic-local",
    productionEligibility: "conditionally-eligible",
    availability: { state: "available", source: "component-manifest", evaluatedAt: createdAt },
    operations: [
      {
        operation: "edit-relation",
        keyboard: "Endpoint controls and action buttons.",
        nonvisual: "Linear node-edge editor.",
        statusAnnouncement: "Announce mutations and current state.",
        focusManagement: "Restore focus after mutation.",
        reflow: "Use an equivalent linear view for bidimensional content.",
        knownLimits: ["Dense graphs require specialist evaluation."]
      }
    ],
    textAlternative: "A linear node-edge representation is mandatory."
  },
  "executable-programming": {
    validationLocations: [
      { kind: "client-public", authority: "deterministic-validator", required: false, capabilityId: "public-test-runner", notes: "Convenience only; not a security boundary." },
      { kind: "trusted-host-protected", authority: "deterministic-validator", required: true, capabilityId: "protected-test-service" }
    ],
    runtimeKind: "sandboxed-execution",
    productionEligibility: "rejected",
    availability: { state: "requires-host", source: "deployment-profile", reason: "Protected validation requires a trusted host.", evaluatedAt: createdAt },
    operations: [
      {
        operation: "edit-run-cancel",
        keyboard: "Editor, run, cancel and diagnostic navigation.",
        nonvisual: "Code, diagnostics and results are exposed as text.",
        statusAnnouncement: "Announce syntax, runtime, cancellation and test states.",
        focusManagement: "Preserve cursor and navigate to diagnostics.",
        reflow: "The page reflows while the editor may scroll internally.",
        knownLimits: ["A production editor and isolation service remain unselected."]
      }
    ],
    textAlternative: "Code, diagnostics and test outcomes require text equivalents."
  },
  "source-argument": {
    validationLocations: [
      { kind: "client-public", authority: "deterministic-validator", required: true, capabilityId: "selector-integrity" },
      { kind: "human-review", authority: "human-review", required: true, capabilityId: "argument-rubric" },
      { kind: "probabilistic-assistance", authority: "probabilistic-assistance", required: false, capabilityId: "language-suggestions" }
    ],
    runtimeKind: "human-review",
    productionEligibility: "conditionally-eligible",
    availability: { state: "available", source: "component-manifest", evaluatedAt: createdAt },
    operations: [
      {
        operation: "select-and-link-evidence",
        keyboard: "Keyboard range selection or explicit selector fields.",
        nonvisual: "Quote-context selector and argument relations use linear forms.",
        statusAnnouncement: "Announce selection, resolution and review state.",
        focusManagement: "Move to annotation or relation controls.",
        reflow: "Source and forms reflow.",
        knownLimits: ["Assistive-technology range selection requires later validation."]
      }
    ],
    textAlternative: "Sources, annotations and relations require linear text equivalents."
  }
};

const derivedStatePolicy = {
  recomputable: true,
  cacheLifetime: "session",
  canonicalForbiddenFields: ["layout", "x", "y", "position", "rendererState", "workerHandle", "libraryObject"],
  notes: "Renderer and runtime state are disposable and never authoritative."
};

const validationEvidencePolicy = {
  defaultVisibility: "learner",
  retention: "attempt",
  redactionRequired: true,
  protectedKinds: ["protected-tests", "review-notes", "probabilistic-trace", "security-diagnostics"]
};

function upgradeRuntime(oldRuntime, family, locations) {
  const oldTime = oldRuntime?.timeLimitMs ?? null;
  const oldMemory = oldRuntime?.memoryLimitMiB ?? null;
  return {
    kind: familyPolicy[family].runtimeKind,
    validationLocations: structuredClone(locations),
    isolationAssurance: family === "executable-programming" ? "cooperative" : "none",
    productionEligibility: familyPolicy[family].productionEligibility,
    runtimeVersion: family === "executable-programming"
      ? "reference-only-no-production-runtime"
      : `migrated-${family}-0.2`,
    limits: {
      timeMs: oldTime ?? (family === "source-argument" ? null : 2000),
      memoryMiB: oldMemory ?? (family === "source-argument" ? null : 64),
      outputBytes: 65536,
      outputMessages: 128,
      cancellationRequired: family === "executable-programming" || family === "semantic-mathematics",
      network: oldRuntime?.network === "none" ? "none" : "deployment-policy",
      filesystem: ["none", "ephemeral-readonly", "ephemeral-readwrite"].includes(oldRuntime?.filesystem)
        ? oldRuntime.filesystem
        : "none"
    },
    notes: family === "executable-programming"
      ? "Migrated Worker or vm profiles are research-only and rejected for hostile production execution."
      : "Migrated from contract 0.1."
  };
}

function upgradeAccessibility(oldAccessibility, family) {
  return {
    operations: structuredClone(familyPolicy[family].operations),
    textAlternative: familyPolicy[family].textAlternative,
    knownLimits: Array.isArray(oldAccessibility?.knownLimits) ? structuredClone(oldAccessibility.knownLimits) : []
  };
}

function upgradeProgrammingValidator(validator) {
  const upgraded = structuredClone(validator);
  upgraded.testSuites = (upgraded.testSuites ?? []).map((suite) => {
    if (suite.visibility !== "protected") return suite;
    return {
      suiteId: suite.suiteId,
      visibility: "protected",
      hostReference: `protected-suite:${suite.suiteId}:migrated-v1`,
      weight: suite.weight
    };
  });
  delete upgraded.hiddenTestsProtected;
  upgraded.protectedMaterialInCourse = false;
  upgraded.styleDiagnosticsAuthority ??= "non-final";
  return upgraded;
}

export function migrateComponent01To02(input) {
  if (!input || input.contract !== "ara.component-prototype" || input.version !== "0.1.0") {
    throw new Error("Expected an ARA component prototype at version 0.1.0.");
  }
  const output = structuredClone(input);
  const family = output.family;
  const policy = familyPolicy[family];
  if (!policy) throw new Error(`Unsupported family ${family}.`);

  output.version = "0.2.0";
  output.componentRef = output.componentRef.replace(/@0\.1\.0$/, "@0.2.0");
  output.response.metadata = {
    adapterVersion: "0.2.0",
    canonicalizationVersion: "0.2.0",
    capabilityAvailability: structuredClone(policy.availability)
  };

  output.validator = family === "executable-programming"
    ? upgradeProgrammingValidator(output.validator)
    : structuredClone(output.validator);
  output.validator.validationLocations = structuredClone(policy.validationLocations);

  if (family === "source-argument") {
    output.validator.selectorResolutionPolicy = {
      order: ["offset", "quote-context", "manual-review"],
      ambiguityOutcome: "ambiguous-non-silent",
      sourceVersionPolicy: "immutable-by-digest"
    };
  }

  output.runtimeRequirements = upgradeRuntime(output.runtimeRequirements, family, policy.validationLocations);
  output.accessibility = upgradeAccessibility(output.accessibility, family);
  output.derivedStatePolicy = structuredClone(derivedStatePolicy);
  output.validationEvidencePolicy = structuredClone(validationEvidencePolicy);

  if (family === "executable-programming") {
    output.securityBoundary.learnerCode = "untrusted-isolated";
    output.securityBoundary.trustedComponentCode = "external-governed-service";
    output.securityBoundary.sensitiveData = output.securityBoundary.sensitiveData ?? "forbidden";
    output.securityBoundary.notes = "Migrated research runtime is not a production security boundary.";
    output.offlineProfile = {
      grade: "public-validation-only",
      networkDuringStudy: "optional",
      packageRequirements: ["code-editor", "public-runner"],
      limitations: ["Protected validation requires a trusted host."]
    };
  } else {
    output.securityBoundary.learnerCode = "data-only";
    output.securityBoundary.trustedComponentCode = "installed-approved-adapter";
    output.securityBoundary.sensitiveData = output.securityBoundary.sensitiveData ?? "forbidden";
    output.offlineProfile = {
      grade: output.offlineProfile?.grade === "package-required" ? "package-required" : "full",
      networkDuringStudy: "forbidden",
      packageRequirements: output.offlineProfile?.packageRequirements ?? [`${family}-adapter`],
      limitations: output.offlineProfile?.limitations ?? []
    };
  }
  output.securityBoundary.courseSuppliedCode = "forbidden";
  return output;
}

export function migrateSet01To02(items) {
  return items.map(migrateComponent01To02);
}

if (process.argv[1] && import.meta.url === new URL(`file://${process.argv[1]}`).href) {
  const [inputPath, outputPath] = process.argv.slice(2);
  if (!inputPath || !outputPath) {
    console.error("Usage: node migrate-0.1-to-0.2.mjs INPUT.json OUTPUT.json");
    process.exit(2);
  }
  const input = JSON.parse(await readFile(inputPath, "utf8"));
  const output = migrateComponent01To02(input);
  await writeFile(outputPath, `${JSON.stringify(output, null, 2)}\n`);
}
