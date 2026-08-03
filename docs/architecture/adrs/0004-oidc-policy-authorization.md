# ADR-0004 — OIDC identity and policy authorization

**Status:** accepted

## Decision

Connected deployments use OpenID Connect. Domain authorization uses workspace-local roles, capabilities and policy evaluation in application services. Adapter-level controls—including PostgreSQL Row-Level Security where applicable—provide defense in depth, not the sole policy model.

Personal offline mode may operate without identity provider until a connected action is requested.

## Requirements

- short-lived tokens and standard discovery;
- explicit organization/workspace context;
- least privilege and default deny;
- revocation and membership changes take effect at connected boundaries;
- confidential/research scopes and exports require separate permissions;
- durable domain IDs do not contain provider IDs;
- no browser access to privileged database/storage credentials.

## Provider profiles

Managed deployments may use Supabase Auth; self-hosted deployments may use another conformant OIDC provider. Conformance is behavioral, not vendor-specific.
