import test from "node:test";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { migrateSet01To02 } from "../migrations/migrate-0.1-to-0.2.mjs";

const root = new URL("../", import.meta.url);
const readJson = async (path) => JSON.parse(await readFile(new URL(path, root), "utf8"));
const families = ["executable-programming", "relational-construction", "semantic-mathematics", "source-argument"];
const fixtures = await Promise.all(families.map((family) => readJson(`migrations/fixtures-0.1/${family}.json`)));
const expected = await Promise.all(families.map((family) => readJson(`migrations/expected-0.2/${family}.json`)));

test("migration is deterministic and preserves expected canonical meaning", () => {
  assert.deepEqual(migrateSet01To02(fixtures), expected);
});

test("all migrated responses declare adapter and canonicalization versions", () => {
  for (const document of expected) {
    assert.equal(document.version, "0.2.0");
    assert.equal(document.response.metadata.adapterVersion, "0.2.0");
    assert.equal(document.response.metadata.canonicalizationVersion, "0.2.0");
  }
});

test("renderer and library state remain forbidden from canonical documents", () => {
  for (const document of expected) {
    const forbidden = document.derivedStatePolicy.canonicalForbiddenFields;
    assert.ok(forbidden.includes("layout"));
    assert.ok(forbidden.includes("libraryObject"));
    const serialized = JSON.stringify(document.response);
    for (const field of ["rendererState", "workerHandle", "libraryObject"]) {
      assert.equal(serialized.includes(`"${field}"`), false);
    }
  }
});

test("programming migration removes protected test material from course JSON", () => {
  const programming = expected.find((item) => item.family === "executable-programming");
  const protectedSuite = programming.validator.testSuites.find((suite) => suite.visibility === "protected");
  assert.equal("tests" in protectedSuite, false);
  assert.match(protectedSuite.hostReference, /^protected-suite:/);
  assert.equal(programming.validator.protectedMaterialInCourse, false);
  assert.equal(programming.runtimeRequirements.productionEligibility, "rejected");
  assert.equal(programming.runtimeRequirements.isolationAssurance, "cooperative");
});

test("source selector ambiguity is explicitly non-silent", () => {
  const source = expected.find((item) => item.family === "source-argument");
  assert.equal(source.validator.selectorResolutionPolicy.ambiguityOutcome, "ambiguous-non-silent");
  assert.ok(source.validator.selectorResolutionPolicy.order.includes("manual-review"));
});

test("validation authority and location remain distinct", () => {
  const programming = expected.find((item) => item.family === "executable-programming");
  const source = expected.find((item) => item.family === "source-argument");
  assert.ok(programming.validator.validationLocations.some((item) => item.kind === "trusted-host-protected"));
  assert.ok(source.validator.validationLocations.some((item) => item.kind === "human-review"));
  assert.ok(source.validator.validationLocations.some((item) => item.kind === "probabilistic-assistance" && item.required === false));
});
