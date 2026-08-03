# ARA reference architecture v1

**Status:** accepted architecture baseline from Issue #7  
**Domain:** product/domain v1 from Issue #6  
**Implementation:** not started

## 1. Architecture style

ARA uses a local-first hybrid architecture with ports and adapters.

```text
Web/PWA client
├─ domain/application core (TypeScript)
├─ capability registry
├─ local projection + outbox (IndexedDB)
├─ app/asset cache (Service Worker + Cache API)
└─ optional large local artifacts (OPFS adapter)
        ↕ versioned operations/packages
Application API / Sync service
├─ authorization/policy
├─ metadata & relations (PostgreSQL)
├─ immutable artifact registry (S3-compatible object storage)
├─ MCP authoring gateway
├─ optional research adapters
└─ deployment/operations adapters
```

The domain never imports Supabase, PostgreSQL, IndexedDB, S3, OIDC, React or an LLM SDK.

## 2. Selected implementation baseline

- Language: TypeScript with strict mode across client, shared contracts and services.
- Client: React + Vite as a PWA, with service worker controlled offline shell/assets.
- Local structured state: IndexedDB behind a repository adapter.
- Local large immutable artifacts: IndexedDB Blob initially; OPFS adapter available only when profiling justifies it.
- Remote metadata/relations/policies/operations: PostgreSQL.
- Immutable course versions, microsequence revisions, publication snapshots and assets: content-hashed objects in S3-compatible storage plus metadata in PostgreSQL.
- Identity: OpenID Connect for connected profiles; local personal mode can operate without account until synchronization/sharing is requested.
- API: typed application services; clients do not depend on database schemas.
- Sync: idempotent operation log/outbox, expected revision and compare-and-set; no CRDT or semantic auto-merge in v1.
- MCP: separate scoped gateway over application services; no direct database/Storage access.
- Research: optional, purpose-bound event/instrument adapters; no mandatory event store for personal profile.

## 3. Boundaries

### Domain/application core

Owns identities, versions, placements, configuration resolution, state transitions, validation and authorization intents. It is deterministic where the approved capability is deterministic.

### Client projection

Materializes one or more course/publication versions, effective snapshots, capability manifests and functional study state for offline use. It is disposable/rebuildable from portable packages plus unsynchronized local operations.

### Metadata store

Stores mutable indexes, memberships, channels, references, policies, operation receipts and relations. Immutable content is referenced by digest/version.

### Artifact store

Stores complete immutable objects/assets. Storage-provider versioning is defense/operations, not the domain version identifier.

### Sync

Transfers explicit operations and immutable objects. Domain versions are never updated in place. Conflicts preserve both states and produce deterministic retry, rebase, fork or human resolution options.

### MCP gateway

Lists capability summaries, fetches only selected contracts/context, validates requests, enforces scopes, writes idempotently and returns stable errors/recovery instructions. Provider/model metadata is provenance, not domain authority.

## 4. Deployment profiles

Defined in `docs/architecture/deployment-profiles-v1.md`. They share domain/package semantics and conformance tests; services may be absent only through an explicit capability manifest.

## 5. Security and privacy

- OIDC authentication and short-lived tokens for connected profiles.
- Server-side policy enforcement and least privilege; PostgreSQL RLS may provide defense in depth in adapters.
- Workspace-local roles; no implicit global administrator.
- Signed URLs are short-lived and never exposed as durable domain identifiers.
- Private/confidential artifacts encrypted in transit and at rest; sensitive research data segregated by purpose/access.
- Content Security Policy, dependency integrity, secret scanning and supply-chain controls.
- Course packages are data-only and validated; no arbitrary supplied scripts.
- Audit logs are purpose-bound and separated from educational analytics.

## 6. Offline and caching

- Service worker caches versioned application shell and immutable public/package assets.
- IndexedDB stores normalized indexes, manifests, study state and outbox.
- Download/materialization is atomic: verify manifest/digests/capabilities before activation.
- Previous working app/package version remains available until replacement passes validation.
- Storage pressure is measured; users see package size, availability and removal consequences.
- Clearing origin storage can remove local data; export/sync/backup states are explicit.

## 7. Portability and packages

Portable packages contain manifests for domain/taxonomy versions, content/composition, configuration, capabilities, assets, provenance, licenses and migrations. Research packages add protocol/data dictionaries/evidence metadata.

Packages are canonical data, not database dumps.

## 8. Controlled extensibility

Resource, practice, instrument and connected capabilities are registered by trusted application releases or signed deployment packages. Contracts declare schema, renderer/service, accessibility, validation, failure, package and version requirements. A missing capability never corrupts unrelated course flow.

## 9. Operations

- migrations are explicit and reversible where possible;
- backups cover PostgreSQL plus immutable object inventory/digests;
- restore rehearsals verify cross-store references;
- diagnostics report app, package, database, storage, sync and capability versions;
- managed and self-hosted releases use the same conformance suite;
- no undocumented compatibility path or silent legacy fallback.

## 10. Quality gates

Budgets and workloads are in `research/data/issue7-quality-budgets-v1.csv`. Architecture conformance is defined in `docs/architecture/conformance-plan-v1.md`.
