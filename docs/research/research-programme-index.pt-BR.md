# Índice canônico do programa de pesquisa

**Estado:** baselines conceituais concluídas; pré-desenvolvimento  
**Idioma:** `pt-BR`  
**Última revisão:** 3 de agosto de 2026

## Baselines disponíveis

| Issue | Saída | Manifesto |
|---|---|---|
| #4 | `ara.configuration-taxonomy.v1` | `research/data/issue4-final-artifact-manifest-v1.json` |
| #5 | `ara.research-framework.v1` | `research/data/issue5-artifact-manifest-v1.json` |
| #6 | requisitos e domínio v1 | `research/data/issue6-artifact-manifest-v1.json` |
| #7 | arquitetura e ADRs v1 | `research/data/issue7-artifact-manifest-v1.json` |
| #8 | UX, acessibilidade e protótipo v1 | `research/data/issue8-artifact-manifest-v1.json` |

Esses artefatos consolidam o brainstorming e as hipóteses atuais. Não autorizam implementação e podem ser revistos de forma versionada antes de qualquer código de produto.

## Rascunho integrado para discussão

O conjunto [`docs/ideation/`](../ideation/README.md) confronta as baselines com o AraLearn funcional e com sistemas e alternativas técnicas externos. Ele materializa:

- auditoria integral do AraLearn no commit `9bff37eee3ba80263084328dc5897d26c7ca3d5a`;
- proposta ampla de experiência do ARA;
- separação candidata entre kernel, packages de resource/practice e adapters;
- comparação de Supabase, outros BaaS, local stores, sync, PWA e wrappers Android;
- 35 decisões preliminares de preservação/reformulação;
- 169 itens candidatos de backlog distribuídos em 16 áreas;
- 37 telas descritas com controles e estados;
- 12 wireframes SVG minimalistas;
- 36 fontes registradas;
- auditoria própria e limitações explícitas.

Manifesto: `research/data/ara-ideation-draft-manifest-v1.json`.

O rascunho não substitui automaticamente as Issues #4–#8. Quando houver divergência, ela constitui matéria para discussão e eventual nova versão, não decisão silenciosa.

## Estado do trabalho

O projeto permanece anterior ao desenvolvimento. Não há release, gate de branch, CI de produto, issue executável ou cronograma de implementação ativo.

A Issue #9 continua sendo uma fase futura. Ela somente deverá ser retomada quando o proprietário decidir explicitamente sair do brainstorming e entrar em planejamento de implementação.

## Pesquisa contínua

A Issue #3 permanece disponível para:

- aprofundar literatura e repositórios;
- revisar decisões de parametrização;
- investigar a composição por microssequências e placements;
- comparar alternativas de domínio, arquitetura ou UX;
- registrar novos cenários, riscos e dúvidas do proprietário;
- aprofundar itens do rascunho depois da discussão inicial.

Mudanças nas baselines exigem nova versão, evidência e decisão. Nenhuma descoberta gera requisito ou código automaticamente.

## Não autorizações

A fase atual não autoriza:

- monorepo, PWA ou backend;
- banco, Storage, IndexedDB ou sincronização;
- endpoints MCP de produção;
- migrations;
- workflows obrigatórios ou proteção de branch;
- issues de implementação;
- código de produto.
