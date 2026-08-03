# ADR-0001 — TypeScript React PWA client

**Status:** accepted  
**Scope:** first implementation baseline

## Decision

Use a strict TypeScript monorepo. Implement the primary client as React with Vite and an installable PWA/service worker. Keep domain/application packages framework-independent.

## Rationale

- broad maintainability and test tooling;
- component/state ecosystem suitable for structured resources and authoring;
- service-worker/IndexedDB access without native distribution dependency;
- one codebase across managed, self-hosted and personal profiles;
- bounded migration path if the UI framework changes.

## Constraints

- no server-rendering requirement for baseline study;
- route/shell works offline after installation;
- code splitting by authoring/research/optional capability;
- framework objects never enter portable domain packages;
- progressive enhancement and accessible HTML semantics.

## Rejected

- JavaScript without strict typing;
- native-only baseline;
- framework/domain coupling;
- one monolithic bundle containing all optional capabilities.
