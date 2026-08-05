# Índice canônico do programa de pesquisa

**Estado:** baselines conceituais concluídas; nova frente focal em investigação; pré-desenvolvimento  
**Idioma:** `pt-BR`  
**Última revisão:** 4 de agosto de 2026

## Baselines disponíveis

| Issue | Saída | Manifesto |
|---|---|---|
| #4 | `ara.configuration-taxonomy.v1` | `research/data/issue4-final-artifact-manifest-v1.json` |
| #5 | `ara.research-framework.v1` | `research/data/issue5-artifact-manifest-v1.json` |
| #6 | requisitos e domínio v1 | `research/data/issue6-artifact-manifest-v1.json` |
| #7 | arquitetura e ADRs v1 | `research/data/issue7-artifact-manifest-v1.json` |
| #8 | UX, acessibilidade e protótipo v1 | `research/data/issue8-artifact-manifest-v1.json` |

Esses artefatos consolidam o brainstorming e as hipóteses disponíveis até 3 de agosto de 2026. Não autorizam implementação e podem ser revistos de forma versionada antes de qualquer código de produto.

## Rascunho integrado para discussão

O conjunto [`docs/ideation/`](../ideation/README.md) confronta as baselines com o AraLearn funcional e com sistemas e alternativas técnicas externos. Ele materializa:

- auditoria integral do AraLearn no commit `9bff37eee3ba80263084328dc5897d26c7ca3d5a`;
- proposta ampla de experiência do ARA;
- separação candidata entre kernel, packages de resource/practice e adapters;
- comparação de Supabase, outros BaaS, local stores, sync, PWA e wrappers Android;
- 35 decisões preliminares de preservação/reformulação;
- pré-backlog v2 com 197 itens candidatos em 17 áreas;
- 37 telas descritas com controles e estados;
- 12 wireframes SVG minimalistas;
- investigação focal de perfis modulares de agente, curadoria participativa e analytics.

Manifestos:

- `research/data/ara-ideation-draft-manifest-v1.json`;
- `research/data/ara-draft-backlog-v2-manifest.json`;
- `research/data/agent-profiles-participatory-analytics-manifest-v1.json`.

O rascunho não substitui automaticamente as Issues #4–#8. Quando houver divergência, ela constitui matéria para discussão e eventual nova versão, não decisão silenciosa.

## Frente focal ativa — Issue #77

A Issue #77 investiga como preservar a autoria GPT/MCP já validada no AraLearn e decompor sua configuração monolítica em objetos versionados e administráveis:

```text
base comum
+ papel
+ perfil de domínio
+ prompts/templates
+ coleções de conhecimento
+ contexto e escopo de escrita
+ MCP resources/tools/contracts
+ modelo/provider
+ evals
→ AgentConfigurationSnapshot
```

A frente também investiga:

- observações participativas, conflitos e síntese argumentativa;
- diffs, findings, reparos e reauditorias;
- analytics de autoria, agente, resources e sistema;
- análise quantitativa, qualitativa e mista dentro de protocolos;
- GPT como pesquisador-assistente, sem autoridade científica final;
- UX administrativa compreensível e versionamento visível.

### Saídas iniciais

- síntese integrada: `docs/ideation/agent-profiles-participatory-analytics-v1.pt-BR.md`;
- protocolo: `research/searches/2026-08-04-agent-profiles-participatory-analytics-protocol.md`;
- corpus de 34 fontes: `research/data/agent-profiles-participatory-analytics-evidence-corpus-v1.csv`;
- bibliografia: `research/library/agent-profiles-participatory-analytics-v1.bib`;
- síntese de decisão: `research/data/agent-profiles-participatory-analytics-decision-synthesis-v1.json`;
- registries de objetos, papéis, escopos, perguntas, evals, ações e questões abertas;
- área Q do pré-backlog: `docs/ideation/draft-backlog-agent-profiles-analytics-v1.pt-BR.md`.

### Status metodológico

Esta é uma revisão de escopo inicial, não uma revisão sistemática concluída. A evidência inclui especificações oficiais, revisões, estudos empíricos, frameworks e preprints explicitamente classificados. Decisões materiais exigirão aprofundamentos focais, especialmente em:

- avaliação de retrieval e contexto;
- evals de perfis e prompts;
- síntese argumentativa e participação;
- validade da análise qualitativa assistida por LLM;
- raciocínio estatístico, causal e reprodutibilidade;
- privacidade e governança institucional.

## Estado do trabalho

O projeto permanece anterior ao desenvolvimento. Não há release, gate de branch, CI de produto, issue executável ou cronograma de implementação ativo.

A Issue #9 continua sendo uma fase futura. Ela somente deverá ser retomada quando o proprietário decidir explicitamente sair do brainstorming e entrar em planejamento de implementação.

## Pesquisa contínua

A Issue #3 permanece disponível para:

- aprofundar literatura e repositórios;
- revisar decisões de parametrização;
- investigar a composição por microssequências e placements;
- comparar alternativas de domínio, arquitetura ou UX;
- aprofundar a Issue #77 e suas frentes focalizadas;
- registrar novos cenários, riscos e dúvidas do proprietário;
- solicitar textos completos quando sua ausência limitar uma decisão.

Mudanças nas baselines exigem nova versão, evidência e decisão. Nenhuma descoberta gera requisito ou código automaticamente.

## Próxima sequência de pesquisa

1. inventariar a configuração monolítica do AraLearn;
2. validar terminologia e decomposição dos objetos de agente;
3. montar fixtures e evals de continuidade;
4. comparar um primeiro perfil de domínio à configuração geral;
5. aprofundar contexto integral/indexado e escopos de escrita;
6. validar o ciclo de observações, síntese, diff, reparo e reauditoria;
7. selecionar desenhos prioritários para os workbenches quantitativo, qualitativo e misto;
8. propor revisões versionadas de requisitos, domínio, arquitetura e UX.

## Não autorizações

A fase atual não autoriza:

- monorepo, PWA ou backend;
- banco, Storage, IndexedDB ou sincronização;
- endpoints MCP de produção;
- schemas ou migrations de perfis de agente;
- coleta de participantes;
- alteração autônoma de prompts, knowledge, resources ou publicações;
- workflows obrigatórios ou proteção de branch;
- issues de implementação;
- código de produto.
