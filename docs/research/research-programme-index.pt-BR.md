# Índice canônico do programa de pesquisa

**Estado:** baselines conceituais concluídas; frentes focais em investigação; pré-desenvolvimento  
**Idioma:** `pt-BR`  
**Última revisão:** 5 de agosto de 2026

## Baselines disponíveis

| Issue | Saída | Manifesto |
|---|---|---|
| #4 | `ara.configuration-taxonomy.v1` | `research/data/issue4-final-artifact-manifest-v1.json` |
| #5 | `ara.research-framework.v1` | `research/data/issue5-artifact-manifest-v1.json` |
| #6 | requisitos e domínio v1 | `research/data/issue6-artifact-manifest-v1.json` |
| #7 | arquitetura e ADRs v1 | `research/data/issue7-artifact-manifest-v1.json` |
| #8 | UX, acessibilidade e protótipo v1 | `research/data/issue8-artifact-manifest-v1.json` |

As baselines não autorizam implementação e podem receber correções versionadas.

## Rascunho integrado

O conjunto [`docs/ideation/`](../ideation/README.md) materializa:

- auditoria do AraLearn;
- idealização do ARA;
- kernel, packages e adapters;
- agentes modulares e analytics;
- versionamento como mecanismo de autoria, investigação e pesquisa;
- alternativas de histórico e impacto em banco, Storage, local store e front-end;
- autoria local-first e sem burocracia;
- grafo visível de versões;
- acesso derivacional com público/privado;
- pré-backlog v5 com **243 itens candidatos em 19 áreas**.

Manifestos principais:

- `research/data/ara-ideation-draft-manifest-v1.json`;
- `research/data/ara-draft-backlog-v5-manifest.json`;
- `research/data/agent-profiles-participatory-analytics-manifest-v1.json`;
- `research/data/versioning-rationale-architecture-manifest-v2.json`;
- `research/data/derivative-access-version-graph-manifest-v1.json`.

## Frente focal — Issue #77

Investiga:

- decomposição da configuração monolítica GPT/MCP;
- perfis de domínio, prompts/templates e knowledge;
- contexto de leitura e escopo de escrita;
- observações participativas e diffs;
- analytics de autoria e pesquisa;
- GPT como pesquisador-assistente.

O AraLearn é referência funcional e contraste; evals partem de tarefas-alvo do ARA.

## Frente focal — Issue #79

### Correção de escopo

A Issue #79 não trata apenas de provider, quota ou Storage. Ela pesquisa o versionamento desde a razão de produto até a economia operacional.

O ARA precisa de histórico para:

- permitir edição rápida, impulsiva e reversível;
- evitar confirmações e aprovações para cada alteração;
- preservar erros, reparos, restaurações e derivações;
- sustentar investigação vertical e horizontal pelo GPT;
- fixar condições de pesquisa;
- versionar configurações de agentes;
- permitir autoria offline e sincronização segura;
- relacionar conteúdo, acesso e proveniência.

### Escalas do histórico

```text
diário local no IndexedDB
→ checkpoint automático
→ revisão durável e imutável
→ grafo navegável
```

### Alternativas comparadas

- estado atual + log;
- snapshots completos no banco;
- snapshots completos no object storage;
- content addressing + manifests;
- deltas/patches;
- event sourcing integral;
- versionamento nativo do bucket;
- tabelas temporais;
- Git verdadeiro;
- camada Git-like sobre object storage.

### Hipótese combinada

```text
revisões editoriais imutáveis
+ manifests e deduplicação quando vantajosos
+ operation log para intenção/proveniência
+ projeções materializadas
+ IndexedDB local-first
```

Essa hipótese não é arquitetura aprovada.

### Impacto a medir

#### Banco

- linhas, arestas e índices;
- refs atuais e concorrência;
- RLS/autorização e audiência efetiva;
- invalidations após revogação;
- WAL, backup, CPU e projeções.

#### Object storage

- GB e quantidade de objetos;
- PUT/GET/LIST;
- latência de objetos pequenos;
- órfãos, digests e integridade;
- signed URLs, lifecycle, cold storage e restore.

#### Local e front-end

- diário, cache, outbox e materialização;
- checkpoints e idempotência;
- read models para histórico, grafo e diffs;
- pacotes de contexto vertical/horizontal para a LLM.

### Saídas v2

- síntese: `docs/ideation/versioning-rationale-alternatives-storage-impact-v2.pt-BR.md`;
- área R v2: `docs/ideation/draft-backlog-versioning-storage-v2.pt-BR.md`;
- razões: `research/data/versioning-requirement-ledger-v2.csv`;
- alternativas: `research/data/versioning-alternative-impact-matrix-v2.csv`;
- registry R v2: `research/data/ara-draft-backlog-versioning-storage-v2.csv`;
- manifesto: `research/data/versioning-rationale-architecture-manifest-v2.json`.

## Frente focal — Issue #81

Investiga a composição de padrões que sustenta o novo modelo de autoria e acesso:

```text
version DAG
+ local journal/checkpoints
+ public | private
+ lista de usuários/grupos
+ teto herdado de audiência
+ revogação em cascata
+ grafo navegável
```

Nome técnico candidato:

> controle de acesso derivacional com atenuação monotônica

A regra de bloquear o autor de uma derivação após revogação ancestral é específica do ARA e precisa de avaliação própria.

## Relações entre as frentes

- #77 define objetos, contexto, operações e analytics;
- #79 define por que versionar, compara mecanismos e mede custos;
- #81 define experiência, grafo e acesso herdado;
- resultados podem motivar revisões de #5–#8;
- #10 continua sendo o gate de fase.

## Estado do trabalho

O projeto permanece anterior ao desenvolvimento. Não há release, CI de produto, issue executável ou cronograma de implementação ativo.

## Pesquisa contínua

A Issue #3 permanece disponível para:

- aprofundar literatura e repositórios;
- revisar parametrização, domínio, arquitetura e UX;
- aprofundar #77, #79 e #81;
- solicitar textos completos quando necessários;
- registrar novos cenários, riscos e dúvidas.

## Próxima sequência

1. definir política de diário, checkpoint e revisão durável;
2. inventariar objetos versionados e granularidades;
3. comparar snapshots completos e content-addressed manifests;
4. gerar workloads de banco, Storage e sync;
5. medir custo de acesso, grafo e projeções;
6. prototipar o grafo no front-end;
7. definir pacotes de contexto vertical e horizontal;
8. testar exportação e restore;
9. revisar produto, domínio, arquitetura e UX;
10. somente depois discutir implementação.

## Não autorizações

A fase atual não autoriza:

- código, schema ou endpoint de produção;
- contratação ou seleção de provider;
- escolha de mecanismo de versionamento ou biblioteca de grafo;
- migração do AraLearn;
- coleta de participantes;
- uso automático do histórico operacional como dado de pesquisa;
- hard delete após revogação;
- matriz geral de permissões ou confirmações por edição.
