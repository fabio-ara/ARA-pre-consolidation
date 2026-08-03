# Índice canônico do programa de pesquisa

**Estado:** baselines e programa de implementação concluídos  
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
| #9 | releases, quality gates e backlog v1 | `research/data/issue9-artifact-manifest-v1.json` |

## Programa de implementação

Seis releases verticais foram aprovadas:

- R0 — proteção, toolchain/PWA e domínio/pacotes;
- R1 — estudo pessoal offline;
- R2 — autoria privada visível e MCP delimitado;
- R3 — sync, colaboração e operações conectadas;
- R4 — pesquisa, ensino formal e perfil institucional confidencial;
- R5 — publicação aberta, capabilities controladas, migração e evidência ARA v1.

As únicas issues executáveis são #59–#74, na ordem registrada em `research/data/issue9-implementation-backlog-v1.csv`.

## Estado atual

Todo o trabalho de pesquisa, definição, arquitetura, UX e planejamento está materializado. A implementação de código está bloqueada por **#59 — Enable protected main and verify governance gate**.

O conector GitHub disponível nesta sessão não permite configurar rulesets/branch protection. O administrador do repositório deve aplicar `docs/releases/main-branch-protection-v1.md`, verificar que o check `governance` bloqueia merge quando falha e fechar #59. Somente então #60 pode começar.

## Pesquisa contínua

A Issue #3 permanece disponível para lacunas específicas encontradas na implementação ou avaliação. Nenhuma descoberta reabre automaticamente as baselines; mudanças exigem versão, evidência e decisão.
