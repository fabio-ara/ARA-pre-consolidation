# ADR-0002 — Hybrid storage topology

**Status:** accepted

## Decision

Use:

- IndexedDB for local structured projection, manifests, study state and outbox;
- Cache API for versioned app shell and request/response assets;
- OPFS only through an optional adapter for profiled large-file workloads;
- PostgreSQL for connected metadata, relations, policies, memberships, channels and operation receipts;
- S3-compatible object storage for immutable content versions, publication snapshots and assets.

Domain packages and IDs are independent of physical keys and provider version IDs.

## Rationale

This preserves rich offline queries, immutable artifact distribution, relational integrity/authorization and provider portability without forcing all content into database rows or all metadata into object JSON.

## Consequences

Cross-store integrity is verified by manifests/digests and backup/restore conformance. Supabase can implement the managed PostgreSQL/Auth/Storage adapter but does not define domain semantics.
