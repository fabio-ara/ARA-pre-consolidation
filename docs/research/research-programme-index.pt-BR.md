# Índice canônico do programa de pesquisa

**Estado:** pesquisa, produto, arquitetura e UX concluídos  
**Idioma:** `pt-BR`  
**Última revisão:** 3 de agosto de 2026

## Baselines

| Issue | Saída | Manifesto |
|---|---|---|
| #4 | `ara.configuration-taxonomy.v1` | `research/data/issue4-final-artifact-manifest-v1.json` |
| #5 | `ara.research-framework.v1` | `research/data/issue5-artifact-manifest-v1.json` |
| #6 | requisitos e domínio v1 | `research/data/issue6-artifact-manifest-v1.json` |
| #7 | arquitetura e ADRs v1 | `research/data/issue7-artifact-manifest-v1.json` |
| #8 | UX, acessibilidade e protótipo v1 | `research/data/issue8-artifact-manifest-v1.json` |

## UX aceita

- 36 telas/contratos e estados;
- 15 jornadas cobertas;
- mobile-first com panes contextuais no desktop;
- profiles/overlays antes de parâmetros avançados;
- autoria GPT+MCP + inspeção/controle no ARA;
- placement/revision/diff/provenance visíveis;
- audit/repair/approval/publication separados;
- offline/sync/conflict/capability/permission como estados normais;
- analytics orientados por pergunta e papel;
- WCAG 2.2 AA target e alternativas não visuais;
- strings críticas em en, pt-BR e pt-PT;
- protótipo em `prototypes/ux-v1/`;
- evaluation plan sem autorização automática de participantes.

## Próxima e última fase de preparação — Issue #9

Issue #9 deverá:

- definir releases verticais e dependências;
- estabelecer branch protection e revisão obrigatória;
- criar CI para lint, typecheck, tests, package/schema, accessibility, security, dependency, build/budgets e docs;
- definir Definition of Done e quality gates;
- criar estratégia de migração AraLearn → ARA sem legado oculto;
- definir backup, rollback, evidence package e release notes;
- criar issues de implementação autossuficientes para Codex;
- impedir que implementação comece fora da sequência aprovada.

## Pesquisa contínua

A Issue #3 permanece disponível para lacunas específicas descobertas na implementação/avaliação. Mudanças nas baselines exigem nova versão e decisão.
