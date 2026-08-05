# Índice canônico do programa de pesquisa

**Estado:** baselines conceituais concluídas; frentes focais em investigação; pré-desenvolvimento  
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

O conjunto [`docs/ideation/`](../ideation/README.md) confronta as baselines com o AraLearn funcional e com sistemas e alternativas externos. Ele materializa:

- auditoria integral do AraLearn;
- proposta ampla de experiência do ARA;
- separação candidata entre kernel, packages e adapters;
- comparações técnicas e de deployment;
- pré-backlog v3 com **207 itens candidatos em 18 áreas**;
- 37 telas descritas e 12 wireframes;
- investigação de perfis modulares de agente, curadoria participativa e analytics;
- investigação de versionamento, retenção, armazenamento e economia operacional.

Manifestos principais:

- `research/data/ara-ideation-draft-manifest-v1.json`;
- `research/data/ara-draft-backlog-v3-manifest.json`;
- `research/data/agent-profiles-participatory-analytics-manifest-v1.json`.

O rascunho não substitui automaticamente as Issues #4–#8. Divergências exigem discussão e eventual revisão versionada.

## Frente focal — Issue #77

A Issue #77 investiga a decomposição da configuração monolítica do GPT/MCP em objetos versionados e administráveis:

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

Também investiga:

- observações participativas e síntese argumentativa;
- diffs, findings, reparos e reauditorias;
- analytics de autoria, agente, resources e sistema;
- pesquisa quantitativa, qualitativa e mista;
- GPT como pesquisador-assistente sob autoridade humana.

### Correção metodológica

O AraLearn é referência funcional e caso de contraste, mas não implementa a arquitetura modular proposta. Portanto:

- não há exigência de fixtures equivalentes;
- evals devem partir de tarefas-alvo, casos controlados, invariantes e exemplos sintéticos;
- jornadas e falhas do AraLearn podem compor casos de contraste;
- continuidade significa preservar somente os invariantes aceitos pelo proprietário, não reproduzir a configuração interna do predecessor.

Documento de correção: `docs/ideation/draft-backlog-agent-profiles-analytics-v2.pt-BR.md`.

### Saídas iniciais

- síntese integrada: `docs/ideation/agent-profiles-participatory-analytics-v1.pt-BR.md`;
- protocolo: `research/searches/2026-08-04-agent-profiles-participatory-analytics-protocol.md`;
- corpus de 34 fontes: `research/data/agent-profiles-participatory-analytics-evidence-corpus-v1.csv`;
- bibliografia: `research/library/agent-profiles-participatory-analytics-v1.bib`;
- síntese de decisão e registries estruturados;
- área Q corrigida: `research/data/ara-draft-backlog-agent-profiles-analytics-v2.csv`.

## Frente focal — Issue #79

A Issue #79 investiga a sustentabilidade do versionamento previsto pelo ARA:

```text
metadata relacional pequena
+ artefatos imutáveis e deduplicados
+ materialização local
+ retenção/GC explícitos
+ exportação e restore provider-neutral
```

Essa direção é hipótese, não arquitetura aceita.

### Perguntas principais

- que objetos são revisionáveis, imutáveis, derivados ou temporários;
- o que reside no banco, object storage ou local store;
- como variantes compartilham revisões sem duplicar cursos;
- como funcionam digest, deduplicação, retenção e garbage collection;
- quanto custam 10 mil, 100 mil e 1 milhão de revisões;
- se Supabase Pro, Supabase + object storage, stack portátil, BaaS alternativo ou local-only é mais adequado;
- como provar backup, exportação e restauração.

### Saídas iniciais

- protocolo: `research/searches/2026-08-04-versioning-storage-economics-protocol.md`;
- evidência oficial: `research/data/versioning-storage-provider-evidence-v1.csv`;
- síntese: `docs/ideation/versioning-storage-economics-v1.pt-BR.md`;
- síntese de decisão: `research/data/versioning-storage-decision-synthesis-v1.json`;
- área R: `docs/ideation/draft-backlog-versioning-storage-v1.pt-BR.md`.

Preços e quotas são fotografias temporais e exigem nova verificação antes de decisão.

## Estado do trabalho

O projeto permanece anterior ao desenvolvimento. Não há release, gate de branch, CI de produto, issue executável ou cronograma de implementação ativo.

A Issue #9 continua futura e somente deverá ser retomada após decisão explícita do proprietário.

## Pesquisa contínua

A Issue #3 permanece disponível para:

- aprofundar literatura e repositórios;
- revisar parametrização, domínio, arquitetura e UX;
- aprofundar #77 e #79;
- investigar composição por microssequências e placements;
- solicitar textos completos quando sua ausência limitar uma decisão;
- registrar novos cenários, riscos e dúvidas.

Nenhuma descoberta gera requisito ou código automaticamente.

## Próxima sequência

1. concluir o inventário contrastivo do AraLearn;
2. definir tarefas-alvo e casos controlados de evals;
3. inventariar objetos versionados do ARA;
4. construir workload sintético e usar payloads do AraLearn apenas como amostra;
5. simular Supabase Free/Pro, Supabase + object storage e alternativa portátil;
6. definir retenção, GC, export e restore;
7. aprofundar perfis de domínio, observações e analytics;
8. propor revisões versionadas das baselines antes de qualquer implementação.

## Não autorizações

A fase atual não autoriza:

- monorepo, PWA ou backend;
- banco, Storage, IndexedDB ou sincronização;
- contratação de plano ou criação de nova conta;
- seleção de provider, database ou object storage;
- endpoints MCP de produção;
- schemas ou migrations;
- coleta de participantes;
- alteração autônoma de prompts, knowledge, resources ou publicações;
- issues de implementação;
- código de produto.
