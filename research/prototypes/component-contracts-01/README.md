# First-principles component-contract prototypes — round 01

This directory contains schema-level prototypes governed by GitHub Issue #36.

## Purpose

The prototypes test whether ARA can share a narrow component envelope while preserving irreducible domain semantics. They do not select a production stack and do not import the AraLearn v4 resource schemas.

The common envelope separates:

- component manifest and provenance;
- representation;
- activity;
- learner response;
- validity;
- criterion outcomes;
- feedback;
- optional runtime;
- security boundary;
- accessibility;
- offline profile;
- localization.

Four contrasting component families are represented:

1. semantic mathematics;
2. relational construction;
3. executable programming;
4. source annotation and evidence-based argument.

## Files

### Schemas

- `schemas/common.schema.json`
- `schemas/component-manifest.schema.json`
- `schemas/semantic-mathematics.schema.json`
- `schemas/relational-construction.schema.json`
- `schemas/executable-programming.schema.json`
- `schemas/source-argument.schema.json`
- `schemas/microsequence-prototype.schema.json`

Each domain schema defines separate `representation`, `activity`, `response` and `validator` subschemas. Feedback uses the shared typed contract.

### Examples

- `examples/manifests.json`: one manifest per component family.
- `examples/component-instances.json`: one complete component instance per family.
- `examples/validation-scenarios.json`: invalid, partial, runtime-error, correct and review-required outcomes.
- `examples/microsequences.json`: theory, guided-practice and independent-practice cards for each family.

## Validation

The committed validation report records 19 successful checks. To reproduce locally:

```bash
python -m pip install "jsonschema>=4.26,<5"
python research/prototypes/component-contracts-01/validate_examples.py
```

The script validates four manifests, four component instances, four microsequences and seven validation-result scenarios.

## Normative limits of this prototype

- Course JSON may reference installed component capabilities but may not contain executable component code.
- Renderer geometry is not canonical content.
- Probabilistic assistance cannot produce a final authoritative decision.
- Feedback and scoring are separate.
- A structurally valid schema instance is not evidence that a pedagogical design is effective.
- Runtime validators still need cross-document checks that JSON Schema alone cannot express.
- Video and binary-media generation remain outside the baseline.
