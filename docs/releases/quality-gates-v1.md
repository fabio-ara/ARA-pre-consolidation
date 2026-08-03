# ARA quality gates and Definition of Done v1

## Repository gate

Before product code:

- `main` accepts changes only through pull requests;
- force push/deletion disabled;
- linear history/squash policy;
- conversations resolved;
- required `governance` check succeeds;
- when R0 creates code jobs, `lint`, `typecheck`, `unit`, `integration`, `build-budget`, `accessibility`, `security` and `package-conformance` become required after one successful repository run;
- one approval is required when a second eligible maintainer exists; until then, owner PRs require a recorded independent review and no unresolved findings;
- workflow actions pinned to full commit SHAs;
- CODEOWNERS requests review for canonical/architecture/workflow areas.

The current connector cannot enable GitHub rulesets; implementation is blocked until an administrator applies `docs/releases/main-branch-protection-v1.md` in repository settings.

## PR Definition of Done

Every implementation PR:

1. links one executable issue and release;
2. names requirements/domain entities/ADRs/screen IDs;
3. states scope and non-goals;
4. includes implementation and migrations without unrelated cleanup;
5. includes unit/integration/E2E/conformance tests appropriate to the change;
6. covers offline, failure, permission, accessibility and locale effects;
7. updates docs/message keys/package manifests;
8. states data/security/privacy/licensing effects;
9. includes rollback/revert or irreversible-change rationale;
10. records evidence, limitations and follow-up authorized by the issue.

## Required gates by category

### Code quality
- formatting/lint/typecheck;
- boundary/forbidden-import tests;
- deterministic test seeds and no flaky acceptance;
- coverage thresholds introduced per package after baseline, never gamed by low-value tests.

### Domain/package
- schema/contract fixtures and migrations;
- digest/version/identity invariants;
- no unknown silent fallback;
- import/export round trip;
- previous-version compatibility only through documented migrations.

### Accessibility/UX/locales
- automated accessibility floor;
- keyboard tests for composite widgets;
- approved screen/state E2E coverage;
- 320px/zoom/touch-target/locale expansion;
- manual AT evidence for release-critical flows.

### Offline/sync
- no-network E2E;
- atomic materialization and previous-version recovery;
- outbox replay/idempotency/conflict fixtures;
- storage pressure/removal/export.

### Security/privacy
- secret scanning;
- dependency/license review;
- CodeQL/SAST after code exists;
- threat-model updates for new trust boundaries;
- purpose/access/retention tests for research data;
- course package treated as untrusted data.

### Performance
- bundle/package budgets;
- Galaxy A07-class physical-device evidence for release gates;
- memory/transition/materialization measurements;
- workload claims bounded to tested fixtures.

### Operations
- migration dry run;
- backup/restore and rollback rehearsal for connected releases;
- managed/self-hosted conformance;
- diagnostics and known limitations.

## Release gate

A release is complete only when its declared end-to-end journey works in all required states and the evidence package is archived. Unit tests alone are insufficient. Educational effectiveness requires a separate approved evaluation.
