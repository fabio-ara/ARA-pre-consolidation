# ADR-0005 — Bounded MCP authoring gateway

**Status:** accepted

## Decision

Expose MCP through a dedicated gateway over application services. The agent never accesses database tables, object-storage paths or secrets directly.

Tool pattern:

1. discover capability summaries;
2. fetch selected contracts and authorized context;
3. prepare scoped operation;
4. validate deterministically;
5. write with request ID and expected revision;
6. return receipt, new revision and structured recovery information.

## Security and governance

- OIDC/OAuth authorization and workspace capability checks;
- per-tool and per-target scopes;
- bounded pagination/response size;
- no authority inherited from chat memory;
- provider/model/tool/instruction provenance;
- agent cannot approve/publish without explicit user-authorized operation;
- no confidential cross-workspace retrieval.

## Consequences

ChatGPT and other providers are replaceable clients of the same gateway. ARA remains the deterministic inspection/approval surface.
