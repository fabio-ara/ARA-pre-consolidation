# Idealização do ARA — índice do rascunho para discussão

**Estado:** rascunho não normativo, pré-desenvolvimento  
**Data de corte inicial:** 3 de agosto de 2026  
**Extensão atual:** 5 de agosto de 2026  
**Finalidade:** materializar propostas, evidências e decisões para discussão antes de qualquer backlog definitivo.

## O que este conjunto representa

Este diretório descreve uma possível evolução do AraLearn para o ARA. Ele reúne:

- auditoria do predecessor;
- experiência de estudo e autoria;
- kernel, packages e adapters;
- parametrização e analytics;
- perfis modulares de agente;
- versionamento como princípio de autoria, colaboração e pesquisa;
- alternativas de armazenamento do histórico e seus impactos;
- autoria local-first e sem burocracia;
- grafo visível de versões e derivações;
- acesso público/privado com lista simples para privados;
- atenuação de acesso ao longo das derivações;
- rascunho amplo de pré-backlog;
- telas e wireframes para discussão.

## O que este conjunto não representa

Não é:

- backlog definitivo;
- issue executável para Codex;
- arquitetura ou stack selecionada;
- autorização para desenvolvimento;
- alegação de efetividade educacional;
- alegação de que o AraLearn possua arquitetura modular equivalente;
- autorização para alterar configurações ou conteúdos autonomamente;
- representação do GPT como autoridade científica;
- seleção ou contratação de BaaS, banco, object storage ou biblioteca de grafo;
- sistema de armazenamento das fontes externas usadas para gerar cursos.

## Tese central de versionamento

O versionamento foi adotado para reduzir burocracia, não para introduzir um ritual de commits.

```text
trabalho rápido e local
→ autosave e undo/redo
→ checkpoints automáticos
→ revisões duráveis e imutáveis
→ restauração sem destruição
→ grafo investigável
```

Ele sustenta:

- autoria impulsiva sem perda;
- conhecimento permanentemente provisório;
- análise vertical de uma linhagem pelo GPT;
- análise horizontal de observações e derivações;
- reprodução de condições de pesquisa;
- evolução de prompts, perfis, knowledge e contracts;
- colaboração, offline e sync;
- acesso e revogação sem apagar a trajetória.

A síntese v2 registra razões, escalas de histórico, alternativas e impactos em banco, Storage, IndexedDB, front-end e GPT.

## Artefatos principais

1. [`aralearn-integral-audit-v1.pt-BR.md`](aralearn-integral-audit-v1.pt-BR.md) — leitura do predecessor.
2. [`ara-product-idealization-v1.pt-BR.md`](ara-product-idealization-v1.pt-BR.md) — idealização inicial.
3. [`product-idealization-versioning-access-correction-v2.pt-BR.md`](product-idealization-versioning-access-correction-v2.pt-BR.md) — correção de lifecycle, acesso e grafo.
4. [`kernel-resource-modularity-v1.pt-BR.md`](kernel-resource-modularity-v1.pt-BR.md) — kernel e packages.
5. [`technology-and-baas-options-v1.pt-BR.md`](technology-and-baas-options-v1.pt-BR.md) — alternativas técnicas.
6. [`versioning-storage-economics-v1.pt-BR.md`](versioning-storage-economics-v1.pt-BR.md) — primeira síntese de Storage e economia.
7. [`versioning-rationale-alternatives-storage-impact-v2.pt-BR.md`](versioning-rationale-alternatives-storage-impact-v2.pt-BR.md) — razões, modelos de versionamento e impacto arquitetural.
8. [`agent-profiles-participatory-analytics-v1.pt-BR.md`](agent-profiles-participatory-analytics-v1.pt-BR.md) — agentes, participação e analytics.
9. [`version-graph-derivative-access-low-friction-authorship-v1.pt-BR.md`](version-graph-derivative-access-low-friction-authorship-v1.pt-BR.md) — síntese do grafo, autoria e acesso.
10. [`conversation-decisions-since-pr80-v1.pt-BR.md`](conversation-decisions-since-pr80-v1.pt-BR.md) — ledger de decisões aceitas, rejeitadas e abertas.
11. [`version-graph-ui-options-v1.pt-BR.md`](version-graph-ui-options-v1.pt-BR.md) — Mermaid, Cytoscape.js, React Flow e ELK.js.
12. [`screens-and-states-v1.pt-BR.md`](screens-and-states-v1.pt-BR.md) — telas e estados anteriores.
13. [`wireframes/`](wireframes/) — esquemas visuais não aprovados.

## Alternativas de versionamento registradas

A síntese v2 distingue:

1. sobrescrita do estado atual + log;
2. snapshots completos no banco;
3. snapshots completos no object storage;
4. objetos endereçados por conteúdo + manifests;
5. cadeias de deltas/patches;
6. event sourcing integral;
7. versionamento nativo de bucket;
8. tabelas temporais no banco;
9. repositório Git verdadeiro;
10. camada Git-like sobre object storage.

A combinação candidata — ainda não aprovada — é:

```text
revisões editoriais imutáveis
+ artifacts content-addressed quando vantajoso
+ manifests hierárquicos
+ operation log append-only
+ projeções materializadas
+ IndexedDB local-first
```

## Impacto arquitetural

### Banco de dados

Deve guardar metadata pequena e transacional:

- lineages, revisions, DAG e refs;
- placements e composição;
- operações, autoria e diffs resumidos;
- acesso declarado e audiência efetiva;
- índices, sync e retenção.

Ainda haverá custo de linhas, arestas, índices, RLS/autorização, invalidação de projeções, concorrência de refs, WAL, backup e CPU. Retirar JSON grande do banco não elimina a necessidade de benchmark relacional.

### Object storage

Deve guardar artifacts e manifests imutáveis. Os riscos principais são:

- muitos objetos pequenos;
- custo por PUT/GET/LIST;
- latência de leituras fragmentadas;
- órfãos e integridade;
- signed URLs e autorização;
- lifecycle, cold storage, backup e restore.

### IndexedDB e sync

Devem sustentar diário local, materialização, drafts, cache e outbox. Autosaves são agrupados em checkpoints e apenas objetos novos são sincronizados.

### Front-end e GPT

A UI usa read models paginados, não varredura de blobs. O GPT recebe pacotes de contexto vertical e horizontal selecionados, não todo o histórico bruto.

## Pré-backlog versionado

O pré-backlog v5 é a união explícita de:

- **A–P:** 171 itens iniciais;
- **Q:** 26 itens de agentes, participação e analytics;
- **R v2:** 20 itens de versionamento, arquitetura de histórico e economia operacional;
- **S:** 26 itens de grafo, autoria sem burocracia e acesso derivacional.

Total: **243 itens candidatos em 19 áreas**.

Manifesto: `research/data/ara-draft-backlog-v5-manifest.json`.

Documentos:

- [`draft-backlog-v1.pt-BR.md`](draft-backlog-v1.pt-BR.md);
- [`draft-backlog-agent-profiles-analytics-v2.pt-BR.md`](draft-backlog-agent-profiles-analytics-v2.pt-BR.md);
- [`draft-backlog-versioning-storage-v2.pt-BR.md`](draft-backlog-versioning-storage-v2.pt-BR.md);
- [`draft-backlog-version-graph-access-v1.pt-BR.md`](draft-backlog-version-graph-access-v1.pt-BR.md).

Registros v2 de versionamento:

- `research/data/versioning-requirement-ledger-v2.csv`;
- `research/data/versioning-alternative-impact-matrix-v2.csv`;
- `research/data/ara-draft-backlog-versioning-storage-v2.csv`;
- `research/data/versioning-rationale-architecture-manifest-v2.json`.

## Frentes focais

### Issue #77 — agentes e analytics

Investiga configuração modular do agente, perfis de domínio, knowledge, MCP, observações, diffs e pesquisa quantitativa, qualitativa e mista.

### Issue #79 — versionamento e infraestrutura

Investiga primeiro **por que e como** versionar e, depois, como sustentar a escolha:

- autoria reversível e sem cerimônia;
- diário, checkpoints e revisões duráveis;
- granularidade e grafo;
- snapshots, manifests, patches, events, temporal tables, Git e Git-like;
- banco versus Storage versus local store;
- retenção, GC, workload, custo, backup, exportação e restore.

### Issue #81 — grafo, autoria e acesso

Investiga:

- grafo visível e navegável;
- análise vertical e horizontal;
- público/privado por nó;
- pessoas e grupos em nós privados;
- acesso do descendente limitado pelos ancestrais;
- revogação ancestral em cascata;
- stack de visualização e requisitos adicionais de BaaS.

Nome técnico candidato:

> controle de acesso derivacional com atenuação monotônica

A interface comum continua usando apenas Público, Privado e Quem pode acessar.

## Regras incorporadas

- o usuário trabalha sem cerimônia e o sistema preserva histórico;
- restauração nunca apaga caminhos posteriores;
- o grafo pode aparecer na interface;
- publicação não é endpoint final;
- descendente pode restringir acesso, nunca ampliá-lo;
- private pode listar pessoas e grupos;
- fontes externas não são armazenadas automaticamente;
- artifact storage guarda conteúdo imutável;
- o banco guarda metadata, edges, refs e projeções;
- logs operacionais não viram dados de pesquisa automaticamente;
- provider e arquitetura somente são selecionados após workload e restore medidos.

## Linguagem de decisão

- **preservar:** valor demonstrado e compatível;
- **reformular:** finalidade mantida, solução aberta;
- **separar:** responsabilidade precisa de fronteira;
- **alternativa a comparar:** opção plausível sem escolha;
- **adiar:** possibilidade legítima não necessária agora;
- **rejeitar como padrão:** contradiz o propósito;
- **questão aberta:** precisa de evidência, protótipo ou decisão.

## Fontes e rastreabilidade

O AraLearn é referência funcional e caso de contraste. Literatura, standards e documentação oficial sustentam as comparações externas. Nenhuma descoberta substitui silenciosamente as baselines #4–#8.

## Perguntas abertas prioritárias

1. Quando checkpoints locais viram revisões duráveis?
2. A unidade física ideal é microssequência, card ou combinação?
3. Snapshots completos são suficientes para o primeiro corte?
4. Quando content addressing compensa sua complexidade?
5. Como funciona um merge com múltiplos pais?
6. Como calcular e invalidar audiência efetiva em escala?
7. Qual object count e request rate são esperados?
8. Como separar analytics transacional e dados de pesquisa?
9. Qual stack apresenta melhor o grafo no mobile?
10. Que BaaS atende artifacts imutáveis, metadata, acesso e sync?
11. Como reter e coletar lixo sem apagar evidência necessária?
12. Que workload deve governar a ADR inicial?
