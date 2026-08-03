# ADR-0006 — Optional segregated research data plane

**Status:** accepted

## Decision

Personal baseline has no central event requirement. Research-enabled deployments add an adapter that accepts only protocol-authorized events/instruments and stores them in a purpose/access-separated data plane.

First implementation may use a separate PostgreSQL schema/database and immutable export packages. A specialized analytics warehouse/LRS is deferred until representative workloads justify it.

## Rules

- operational logs and research evidence are separate streams;
- event definitions are versioned and mapped to protocol/condition;
- identity/pseudonymization keys are segregated;
- withdrawal, retention, export and access policies are enforced before queries;
- Caliper/xAPI mappings are export/ingest adapters;
- measures are calculated from versioned definitions, not embedded in raw events;
- no predictive intervention in v1.
