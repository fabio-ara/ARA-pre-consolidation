# ARA release evidence package v1

Every release tag references an immutable evidence manifest containing:

## Identity

- release/version/commit/tag;
- domain, taxonomy, research-framework and package versions;
- build environment, Node/pnpm/browser/tool versions;
- source and dependency lock digests.

## Scope

- implementation issues and PRs;
- journeys/screens/capabilities included;
- unsupported/deferred capabilities;
- migrations and data changes;
- deployment profiles claimed.

## Automated evidence

- lint/typecheck/unit/integration/E2E results;
- package/domain/conformance fixtures;
- accessibility automated reports;
- security/dependency/license reports;
- build/bundle/package budgets;
- offline/sync/failure injection;
- managed/self-hosted conformance where applicable.

## Manual evidence

- review record;
- critical keyboard/assistive-tech walkthroughs;
- Galaxy A07-class performance/usability run for user-facing releases;
- backup/restore/rollback rehearsal for connected releases;
- locale review;
- migration sample audit.

## Operations

- deployment artifacts/images and checksums/attestations;
- installation/update/backup/restore instructions;
- rollback target and procedure;
- diagnostics sample;
- known incidents/risks.

## Limitations

Explicitly state what was not tested, workload bounds, open accessibility/usability findings, incompatible previous versions and whether educational evaluation exists. Conformance must never be described as evidence of learning effectiveness.

## Retention

Evidence manifests and essential reports remain attached to releases or an approved immutable research/artifact store. Sensitive security or participant evidence uses restricted references rather than public attachment.
