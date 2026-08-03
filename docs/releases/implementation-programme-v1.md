# ARA implementation programme v1

**Status:** approved implementation sequencing from Issue #9  
**Rule:** releases are end-to-end and usable for their declared profile; infrastructure-only milestones do not count as releases.

## R0 — Repository and executable foundation

Outcome: protected, reproducible TypeScript monorepo with domain/package skeleton, PWA shell, CI, test harnesses and evidence packaging. No learner-facing release claim.

Gates:
- branch/ruleset and required checks active;
- lockfile/toolchain pinned;
- package boundaries enforce architecture;
- domain contracts compile and test;
- empty PWA installs/offline shell works;
- security/accessibility/performance harnesses run.

## R1 — Personal offline study

Outcome: a self-directed learner can import/add a signed/versioned baseline course, materialize it, study theory and deterministic choice/gap practice offline, receive configured feedback, resume, inspect version/profile, and export/remove personal data.

Screens: S01–S10, S27, S36.  
Capabilities: baseline study, library/folders, configuration subset, text/table/formula/code-format resources, choice/gap practice, portability.

R1 excludes account, sync, authoring, event collection and LLM.

## R2 — Visible private authoring and repair

Outcome: an author can create a private workspace/course, compose placements and dependencies, build microsequences manually or through bounded MCP, render drafts in ARA, comment, audit, repair, re-audit, approve and publish a private snapshot.

Screens: S11–S28, S36.  
Includes version/diff/provenance/licensing basics and private preview/publication. No multi-user collaboration.

## R3 — Connected sync and collaboration

Outcome: connected users use OIDC, synchronize across devices, resolve explicit conflicts, collaborate through workspace roles/reviews/approvals, and operate managed or self-hosted adapters with equivalent package/domain semantics.

Screens: S15–S28, S34–S36.  
Includes PostgreSQL/S3-compatible adapters, sync/outbox, workspace membership, audience publication, backup/restore baseline.

## R4 — Research, formal teaching and institutional profiles

Outcome: researchers define version-locked protocols/conditions/instruments/events/measures and export governed packages; formal teaching supports assignments/cohorts and authorized question-oriented views; confidential self-hosted profile enforces restricted integrations and operations.

Screens: S29–S36 plus relevant Study screens.  
No predictive early warning or automatic causal inference.

## R5 — Open publication and controlled capabilities

Outcome: open/OER publication, public catalogue/reference acquisition, per-scope licensing/provenance, trusted capability packages and selected evidence-backed optional resources/runtimes.

The first optional capability enters only through its own requirement, ADR, screen contract, conformance and workload evidence.

## Dependency rule

```text
R0 → R1 → R2 → R3 → R4 → R5
```

A release may begin preparatory design/test fixtures before the prior release ships, but no dependent production feature merges until prior gates pass.

## Release evidence

Every release publishes the package defined in `release-evidence-v1.md`, known limitations and explicit unsupported capabilities. Passing conformance does not establish learning effectiveness.
