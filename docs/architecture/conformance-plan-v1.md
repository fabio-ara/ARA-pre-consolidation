# ARA architecture conformance plan v1

## Required suites

1. **Domain/package conformance** — IDs, versions, digests, placements, configuration snapshots, licenses and capability manifests.
2. **Offline** — installation, atomic materialization, study, resume, removal, storage pressure and previous-version recovery.
3. **Sync** — idempotency, expected revision, outbox replay, fork/reapply conflict paths, revocation and deletion effects.
4. **MCP** — authorization, bounded discovery/context, schema validation, operation receipts, recovery errors and no self-publication.
5. **Security/privacy** — threat model, least privilege, signed URL expiry, content validation, confidential workspace and research-data segregation.
6. **Research** — condition snapshot, event authorization, withdrawal, retention, export and managed/self-hosted semantic equivalence.
7. **Capability** — required/optional/unavailable behavior, offline fallback and no unrelated-flow corruption.
8. **Operations** — install, migration, backup, restore, diagnostics, update and rollback.
9. **Performance/accessibility/locales** — budgets in `issue7-quality-budgets-v1.csv`.

## Representative fixtures

- small AraLearn-style offline course;
- large course with reusable placements/assets;
- conflicting offline authoring operations;
- confidential institutional workspace;
- research condition with authorized events/instruments;
- public OER package with third-party licence scopes;
- unavailable AI/runtime capability;
- migrated AraLearn export.

## Evidence

Every architecture/release claim preserves tool versions, environment, fixture digest, result, limitations and artifacts. Passing conformance is not evidence of learning effectiveness or production scale beyond the tested workload.
