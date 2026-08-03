# ADR-0007 — Controlled capability packages

**Status:** accepted

## Decision

Extensibility uses a trusted registry of versioned capability definitions. Course packages contain data and capability requirements, never executable application code.

A capability implementation enters a deployment through a reviewed application release or signed administrator-installed package whose code executes within predefined boundaries.

Each capability declares:

- ID/version and supported domain/taxonomy versions;
- data schema and validation;
- renderer/service/runtime boundary;
- accessibility and alternatives;
- offline/package behavior;
- security/privacy/cost effects;
- events it may emit without authorizing collection;
- unavailable/fallback semantics;
- migrations and conformance tests.

## Consequences

Resources and practices can evolve without kernel growth, while supply-chain risk and context overload remain controlled. Heavy runtimes are profile-scoped and never silently added to baseline bundles.
