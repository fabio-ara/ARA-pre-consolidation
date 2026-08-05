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
- versionamento e Storage;
- autoria local-first e sem burocracia;
- grafo visível de versões;
- acesso derivacional com público/privado;
- pré-backlog v4 com **233 itens candidatos em 19 áreas**.

Manifestos principais:

- `research/data/ara-ideation-draft-manifest-v1.json`;
- `research/data/ara-draft-backlog-v4-manifest.json`;
- `research/data/agent-profiles-participatory-analytics-manifest-v1.json`;
- `research/data/versioning-storage-economics-manifest-v1.json`;
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

Investiga:

- objetos versionados e imutáveis;
- metadata, artifact storage e local store;
- deduplicação, manifests e retenção;
- workloads e custos;
- Supabase e alternativas portáteis;
- backup, exportação e restore.

A hipótese central continua não normativa:

```text
metadata relacional pequena
+ artefatos imutáveis
+ materialização local
+ retenção/GC explícitos
+ export/restore provider-neutral
```

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

### Resultado comparativo inicial

Não existe um único modelo com todas as regras propostas. Foram encontrados precedentes em:

- GitLab: visibilidade de filho não supera a do pai;
- AWS Organizations: guardrails herdados e interseção de permissões;
- OAuth/macaroons: delegação atenuada;
- Decentralized Label Model e derived-data control: políticas que acompanham informação;
- Zanzibar/OpenFGA: relações entre sujeitos, grupos e objetos;
- W3C PROV e Git: proveniência e DAGs;
- lakeFS: semântica Git-like sobre object storage;
- local-first: edição local e sync posterior.

Nome técnico candidato:

> controle de acesso derivacional com atenuação monotônica

A regra de bloquear o autor de uma derivação após revogação ancestral é específica do ARA e precisa de avaliação própria.

### Saídas iniciais

- síntese: `docs/ideation/version-graph-derivative-access-low-friction-authorship-v1.pt-BR.md`;
- decisões da conversa: `docs/ideation/conversation-decisions-since-pr80-v1.pt-BR.md`;
- correção da idealização: `docs/ideation/product-idealization-versioning-access-correction-v2.pt-BR.md`;
- stacks de grafo: `docs/ideation/version-graph-ui-options-v1.pt-BR.md`;
- protocolo: `research/searches/2026-08-05-derivative-access-version-graph-protocol.md`;
- corpus: `research/data/derivative-access-version-graph-evidence-corpus-v1.csv`;
- bibliografia: `research/library/derivative-access-version-graph-v1.bib`;
- área S: `docs/ideation/draft-backlog-version-graph-access-v1.pt-BR.md`.

## Relações entre as frentes

- #77 define objetos, contexto, operações e analytics;
- #79 mede como armazenar e operar as versões;
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

1. validar o modelo de audiência com cenários e casos de borda;
2. definir checkpoint, revisão, restore e merge;
3. medir granularidade e workload sob #79;
4. prototipar Mermaid, Cytoscape.js e React Flow/ELK;
5. avaliar cache e invalidação de acesso efetivo;
6. definir pacotes de contexto vertical e horizontal;
7. revisar produto, domínio, arquitetura e UX;
8. somente depois discutir implementação.

## Não autorizações

A fase atual não autoriza:

- código, schema ou endpoint de produção;
- contratação ou seleção de provider;
- escolha de biblioteca de grafo;
- migração do AraLearn;
- coleta de participantes;
- uso automático do histórico operacional como dado de pesquisa;
- hard delete após revogação;
- matriz geral de permissões ou confirmações por edição.
