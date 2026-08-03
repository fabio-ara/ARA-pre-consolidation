# Índice canônico do programa de pesquisa

**Estado:** baselines concluídas até arquitetura  
**Idioma:** `pt-BR`  
**Última revisão:** 3 de agosto de 2026

## Baselines normativas

| Issue | Baseline | Manifesto |
|---|---|---|
| #4 | `ara.configuration-taxonomy.v1` | `research/data/issue4-final-artifact-manifest-v1.json` |
| #5 | `ara.research-framework.v1` | `research/data/issue5-artifact-manifest-v1.json` |
| #6 | requisitos e domínio v1 | `research/data/issue6-artifact-manifest-v1.json` |
| #7 | arquitetura e perfis v1 | `research/data/issue7-artifact-manifest-v1.json` |

## Arquitetura aceita

```text
TypeScript React/Vite PWA
+ IndexedDB local projection/outbox
+ Service Worker/Cache API
+ PostgreSQL metadata/relations/policies
+ S3-compatible immutable artifacts
+ OIDC connected identity
+ operation-log/revision sync
+ bounded MCP gateway
+ optional segregated research data plane
```

Supabase é um adapter gerenciado candidato; o domínio e as application services permanecem provider-independent. Personal baseline não exige conta, sync, LLM ou event store.

## Próxima fase — Issue #8

A Issue #8 deverá especificar e prototipar:

- architecture of information e navegação;
- todas as jornadas da Issue #6;
- biblioteca, pastas e referências;
- estudo, teoria, prática, feedback, progresso e retomada;
- configuração por perfis, overlays e overrides;
- autoria em tempo real, versões, diffs, comments, findings, repair e publication;
- dependências/placements e composição entre cursos;
- protocolos, consentimento, instrumentos e analytics por pergunta/papel;
- online, offline, sync, conflito, permissões e falhas;
- design tokens, responsive/mobile, teclado e assistive technology;
- en, pt-BR e pt-PT;
- testes de compreensão, usabilidade e acessibilidade.

A UX não altera domínio ou arquitetura silenciosamente. Lacunas voltam à issue apropriada.

## Fase seguinte

A Issue #9 transformará requisitos, ADRs e screen contracts aprovados em releases, CI/quality gates e issues executáveis.

## Pesquisa contínua

A Issue #3 permanece aberta para novas perguntas específicas. Evidência nova exige síntese e decisão versionada; não reabre automaticamente baselines.
