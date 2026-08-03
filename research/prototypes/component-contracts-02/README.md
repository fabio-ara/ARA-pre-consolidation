# ARA component contracts — version 0.2

This package revises the schema-level research contracts from version `0.1` after the disposable-adapter round.

## Normative boundary

The contract separates:

- canonical representation;
- activity;
- learner response;
- validity and criterion outcomes;
- feedback;
- validation location and authority;
- runtime and isolation claims;
- derived renderer/runtime state;
- accessibility alternatives by operation;
- offline capability;
- package measurements;
- evidence visibility and retention.

Course documents may reference installed and approved components. They do not carry component implementation code, protected tests, renderer geometry or library-specific objects.

## Version 0.2 changes

The package adds:

1. `adapterVersion` and `canonicalizationVersion` in responses;
2. explicit capability availability and unsupported provenance;
3. validation locations for public client checks, protected host checks, human review and optional probabilistic assistance;
4. `derivedStatePolicy`;
5. operation-level accessibility alternatives;
6. measured package profiles;
7. validation-evidence visibility and retention;
8. explicit runtime isolation and production eligibility;
9. independent time, memory, output, cancellation, network and filesystem limits;
10. non-silent source-selector ambiguity.

## Migration

`migrations/migrate-0.1-to-0.2.mjs` performs the research migration for the four prototype families. It removes embedded protected programming tests, marks research Worker/`vm` isolation as non-production, and preserves representation, activity and learner response meaning.

```bash
node migrations/migrate-0.1-to-0.2.mjs \
  migrations/fixtures-0.1/semantic-mathematics.json \
  /tmp/semantic-mathematics-0.2.json
```

## Validation

```bash
python validate_examples.py
npm test
```

The schemas are research artifacts. Passing validation does not establish educational effectiveness, production security or accessibility conformance.
