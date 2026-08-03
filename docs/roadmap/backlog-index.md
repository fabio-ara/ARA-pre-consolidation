# Backlog e fluxo de trabalho do ARA

**Estado:** gate final de preparação  
**Idioma:** `pt-BR`  
**Última revisão:** 3 de agosto de 2026

## 1. Caminho

```text
#4 taxonomia — concluída
→ #5 pesquisa/analytics — concluída
→ #6 produto/domínio — concluída
→ #7 arquitetura — concluída
→ #8 UX/UI — concluída
→ #9 releases/quality/backlog — atual
→ implementação
```

A Issue #3 permanece contínua e a #2 paralela.

## 2. Baselines obrigatórias

- `research/data/issue4-final-artifact-manifest-v1.json`;
- `research/data/issue5-artifact-manifest-v1.json`;
- `research/data/issue6-artifact-manifest-v1.json`;
- `research/data/issue7-artifact-manifest-v1.json`;
- `research/data/issue8-artifact-manifest-v1.json`.

Issues de implementação devem apontar entidade/requisito, ADR, screen IDs, release, aceite, testes, docs e rollback.

## 3. UX aprovada

- task/question-oriented IA;
- mobile one-primary-task and desktop contextual panes;
- Study/Create/Review/Research/Admin based on role/capability;
- offline, sync, conflict and failure first-class;
- 36 screen contracts;
- 15 journeys;
- accessibility/localization/design tokens;
- structural prototype;
- evaluation plan.

Implementation may refine presentation within approved behavior. Semantic or journey changes return to #6/#7/#8.

## 4. Work current — Issue #9

Required outputs:

- functional release sequence;
- repository/module boundaries;
- CI and branch protection policy;
- Definition of Done;
- security/privacy/accessibility/performance gates;
- package/migration/rollback plan;
- evidence package format;
- AraLearn migration strategy;
- issue templates for Codex;
- executable implementation issues with explicit dependencies.

## 5. Permanent controls

- no direct implementation from umbrella issues;
- no hidden legacy/fallback/compatibility;
- no course-supplied code;
- no auto-merge of semantic conflicts;
- no telemetry because event exists;
- no UX invention by implementation;
- no educational-effectiveness claim from conformance tests;
- every release works end-to-end for its declared profile.

## 6. Historical records

Experiments #36–#40 remain non-normative; #42 deferred. Issues #50/#53 are accidental `not_planned` placeholders.

## 7. Next

Conclude Issue #9. Only its approved implementation subissues may start product code.
