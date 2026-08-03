# Backlog e fluxo de trabalho do ARA

**Estado:** documento operacional vigente  
**Idioma:** `pt-BR`  
**Última revisão:** 3 de agosto de 2026

## 1. Caminho

```text
#3 evidência contínua
→ #4 taxonomia — concluída
→ #5 pesquisa/analytics — concluída
→ #6 produto/domínio — concluída
→ #7 arquitetura/ADRs — concluída
→ #8 UX/UI — atual
→ #9 releases/backlog executável
→ implementação
```

## 2. Autoridade

Especificação aprovada da fase → ADR → issue operacional → síntese → evidência → histórico → conversa.

Implementação não pode inventar comportamento, entidade, arquitetura ou tela.

## 3. Baselines

- `ara.configuration-taxonomy.v1`;
- `ara.research-framework.v1`;
- `docs/product/product-requirements-v1.md`;
- `docs/product/domain-model-v1.md`;
- `docs/architecture/reference-architecture-v1.md`;
- ADRs `0001`–`0007`;
- manifests das Issues #4–#7.

## 4. Arquitetura aceita

- TypeScript strict monorepo;
- React/Vite installable PWA;
- IndexedDB local projection/outbox;
- Service Worker + Cache API;
- OPFS optional adapter after profiling;
- PostgreSQL connected metadata/relations/policies;
- S3-compatible immutable artifacts;
- OIDC connected identity;
- revision/operation-log sync with explicit conflict;
- bounded MCP application gateway;
- optional segregated research data plane;
- trusted capability registry; no course-supplied code.

Managed and self-hosted profiles share domain/package conformance. Supabase is a managed adapter candidate only.

## 5. Trabalho atual — Issue #8

Issue #8 must produce screen-level contracts and evaluated prototypes for:

- learner library and folders;
- course download/materialization and offline study;
- card cycle, feedback, progress, study review and resumption;
- configuration profiles/overlays/overrides and effective diff;
- ARA authoring workspace + chat/MCP operation status;
- microsequence/placement/dependency composition;
- comments/findings, review, repair and publication;
- protocols, participants, instruments and question-oriented analytics;
- workspace roles and institutional/public/confidential administration;
- sync, conflict, unavailable capability, permission and failure;
- locale/accessibility/responsive behavior.

Every journey needs mobile/desktop/offline/permission/error states and visible strings in en, pt-BR and pt-PT.

## 6. Quality and boundaries

- Galaxy A07-class first-scope benchmark;
- baseline study without connection/LLM;
- accessibility target WCAG 2.2 AA plus manual AT review;
- no universal LMS dashboard;
- no decorative gamification;
- usability does not establish learning effectiveness;
- UX findings cannot change domain/architecture without explicit return.

## 7. Next

After Issue #8, Issue #9 defines branch protection, CI, releases, migration, evidence packages and executable Codex issues.

Issues #50/#53 remain accidental `not_planned`; experiments #36–#40 non-normative; #42 deferred.
