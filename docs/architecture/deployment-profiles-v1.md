# ARA deployment profiles v1

All profiles use the same domain identities, portable packages, configuration resolution and conformance semantics.

## Personal mobile/offline

- installable PWA/static delivery;
- local library, course packages and study state;
- no account, sync, event store or LLM required;
- optional user-controlled export/import;
- optional connected authorship only when explicitly configured.

## Managed personal/authoring

- OIDC/account;
- PostgreSQL metadata and S3-compatible artifacts;
- sync across devices;
- private workspaces and GPT+MCP gateway;
- managed adapter may use Supabase services, but application/domain APIs remain provider-independent.

## Academic/research managed

- participant governance and condition locks;
- segregated research data adapters;
- consent/withdrawal, retention, export and audit;
- protocol-specific event/instrument collection;
- reproducible version manifests and conformance evidence.

## Formal teaching/cohort

- organizations, workspaces, enrolment/assignments;
- author/reviewer/approver roles;
- authorized learner support and reporting;
- assessment and accessibility policies;
- no individual surveillance or ranking by default.

## Institutional self-hosted/confidential

- containerized application services;
- institution-controlled PostgreSQL, S3-compatible storage and OIDC provider;
- restricted providers/gateways;
- backup, restore, monitoring, update and rollback duties;
- confidential content, local keys/policies and auditable export.

## Public/open publication

- immutable public snapshots and licence/provenance manifests;
- CDN/object delivery;
- catalogue index separated from authoring and participant data;
- public package verification and supersession/withdrawal channels.

## Capability rules

Each deployment publishes a signed/versioned CapabilityManifest. Course activation fails explicitly for missing required capabilities. Optional connected functions use only declared fallbacks. Profiles cannot change domain meaning or disable rights/accessibility baselines.
