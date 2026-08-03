# ADR-0003 — Revision and operation-log synchronization

**Status:** accepted

## Decision

Use immutable objects plus an idempotent operation/outbox protocol. Every mutation names target, expected revision, request ID, actor, scope and intent. Shared services apply compare-and-set and return receipts.

Conflicts use:

- retry when identical operation receipt exists;
- reapply onto current revision when intent remains valid;
- explicit fork for competing semantic revisions;
- human selection for structural/semantic conflicts.

Do not use CRDTs or automatic semantic merge in v1.

## Rationale

ARA objects are mostly versioned compositions rather than collaborative character streams. Preserving intent, auditability and publication immutability is more important than automatic convergence.

## Consequences

Personal state may use deterministic field-level merge only where semantics are specified. Offline queues are inspectable, retryable and exportable. Lost operations are never hidden.
