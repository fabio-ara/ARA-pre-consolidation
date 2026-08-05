# Backlog e fluxo de trabalho do ARA

**Estado:** pré-desenvolvimento; brainstorming, pesquisa e revisão  
**Idioma:** `pt-BR`  
**Última revisão:** 5 de agosto de 2026

## 1. Estado das fases

```text
#3 evidência contínua
→ #4 taxonomia — baseline
→ #5 pesquisa/analytics — baseline
→ #6 produto/domínio — baseline
→ #7 arquitetura — baseline
→ #8 UX/UI — baseline e protótipo não produtivo
→ #77 agentes, participação e analytics — pesquisa focal
→ #79 versionamento, arquitetura de histórico e economia — pesquisa focal
→ #81 grafo, acesso e autoria sem burocracia — pesquisa focal
→ #9 planejamento de implementação — futuro
```

As frentes focais não são issues de código.

## 2. Trabalho atual

### Issue #77

Configuração modular do agente, perfis de domínio, knowledge, MCP, observações, diffs e analytics educacionais.

### Issue #79

O versionamento é investigado como requisito de produto antes da infraestrutura:

- autoria rápida e reversível;
- comportamento impulsivo não destrutivo;
- conhecimento permanentemente provisório;
- análise vertical e horizontal pelo GPT;
- reprodução de pesquisa;
- colaboração, offline e evolução de agentes.

Também compara mecanismos e seus impactos:

- snapshots no banco ou Storage;
- content addressing e manifests;
- deltas/patches;
- operation logs e event sourcing;
- temporal tables;
- bucket versioning;
- Git e camadas Git-like;
- banco, object storage, IndexedDB, sync, front-end, retenção e custo.

### Issue #81

- grafo visível e clicável;
- público/privado por nó;
- pessoas e grupos em privados;
- descendente não amplia acesso herdado;
- revogação ancestral bloqueia descendentes sem apagá-los;
- benchmark de stack de grafo;
- requisitos adicionais de BaaS.

## 3. Pré-backlog v5

Composição:

- A–P: 171 itens;
- Q: 26 itens;
- R v2: 20 itens;
- S: 26 itens.

Total: **243 itens candidatos em 19 áreas**.

Manifesto: `research/data/ara-draft-backlog-v5-manifest.json`.

Documentos:

- `docs/ideation/draft-backlog-v1.pt-BR.md`;
- `docs/ideation/draft-backlog-agent-profiles-analytics-v2.pt-BR.md`;
- `docs/ideation/draft-backlog-versioning-storage-v2.pt-BR.md`;
- `docs/ideation/draft-backlog-version-graph-access-v1.pt-BR.md`.

Registries correspondentes permanecem em `research/data/`.

Nenhum item possui prioridade, sprint, release ou autorização para implementação.

## 4. Direções incorporadas

### Autoria

```text
editar localmente
→ autosave/undo
→ checkpoint automático
→ sync
→ revisão durável e imutável
```

A plataforma não exige mensagem, aprovação ou confirmação a cada alteração.

### Histórico

- revisão forma DAG;
- restauração cria nova revisão;
- caminhos posteriores permanecem;
- grafo pode ser mostrado diretamente;
- operações, observações, acesso e pesquisa podem ser camadas;
- guardar histórico não implica enviá-lo integralmente à LLM.

### Fonte editorial e proveniência

A hipótese combinada é:

```text
revisões imutáveis = fonte editorial
operation log = intenção e proveniência
projeções = leitura eficiente do front-end
```

Event sourcing integral não é presumido.

### Armazenamento

```text
banco
→ lineages, revisions, DAG, refs, acesso, operações e índices

object storage
→ artifacts e manifests imutáveis

IndexedDB
→ diário local, materialização, drafts, cache e outbox
```

Versionamento no Storage não significa ausência de versionamento no banco: a metadata do grafo continua relacional e transacional.

### Acesso

```text
Público
ou
Privado + pessoas/grupos
```

A audiência do descendente é limitada pelos pais e contêineres necessários. Pode restringir, nunca ampliar. Revogação ancestral pode bloquear descendentes sem apagar a história.

### Lifecycle

Publicação não é endpoint final. A plataforma distingue:

- visibilidade;
- audiência;
- disponibilidade;
- revisão atual;
- revisão fixada;
- trajetória.

### Pesquisa

- análise vertical: trajetória de um artefato;
- análise horizontal: observações, branches e participantes;
- uso acadêmico exige protocolo e snapshot;
- histórico operacional não é automaticamente dado de pesquisa.

## 5. Alternativas da área R v2

A área R agora exige comparação explícita de:

1. current state + logs;
2. snapshots completos no banco;
3. snapshots completos no object storage;
4. content-addressed artifacts + manifests;
5. deltas/patches;
6. event sourcing integral;
7. bucket versioning;
8. temporal tables;
9. Git real;
10. Git-like sobre object storage.

A alternativa mais sofisticada não será escolhida sem demonstrar vantagem sobre snapshots simples.

## 6. Impactos obrigatórios a medir

### Banco

- rows, edges e indexes;
- RLS/autorização;
- audience projection e invalidation;
- ref contention;
- WAL, backup e CPU.

### Storage

- GB e object count;
- PUT/GET/LIST;
- latência e egress;
- órfãos, digests e integridade;
- lifecycle, cold storage e restore.

### Local e produto

- política de checkpoints;
- sync idempotente;
- conflito e base revision;
- read models do histórico;
- custo do grafo no mobile;
- context packages para GPT.

## 7. Entrada futura em desenvolvimento

A Issue #9 somente será ativada após decisão explícita do proprietário.

Será necessário:

- revisar o pré-backlog v5;
- promover somente itens decididos;
- revisar produto, domínio, arquitetura e UX;
- medir workloads;
- selecionar mecanismo de versionamento e infraestrutura por ADR;
- criar issues executáveis novas.

## 8. Regras permanentes

- possibilidade não vira requisito automaticamente;
- item de pré-backlog não autoriza código;
- AraLearn é referência funcional e contraste;
- versionamento reduz burocracia, não cria cerimônia;
- publicação não significa conclusão definitiva;
- restauração não apaga história;
- contexto legível não concede escrita;
- derivação não amplia audiência;
- observações não são votação;
- output do GPT não é autoridade científica;
- histórico operacional exige protocolo para pesquisa;
- fontes externas não são armazenadas automaticamente;
- free tier não define a arquitetura;
- provider, stack e mecanismo de versionamento exigem benchmark e decisão posterior.

## 9. Próxima ação

Executar em paralelo:

1. política de diário/checkpoint/revisão;
2. benchmark de granularidade e snapshots;
3. workload de banco, Storage e sync;
4. cenários e casos de borda de acesso;
5. pacotes de contexto e analytics;
6. protótipos comparativos de grafo;
7. revisão do pré-backlog v5 pelo proprietário.

Não iniciar desenvolvimento nem contratar infraestrutura sem mudança explícita de fase.
