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
→ #79 versionamento, Storage e economia — pesquisa focal
→ #81 grafo, acesso e autoria sem burocracia — pesquisa focal
→ #9 planejamento de implementação — futuro
```

As frentes focais não são issues de código.

## 2. Trabalho atual

### Issue #77

Configuração modular do agente, perfis de domínio, knowledge, MCP, observações, diffs e analytics educacionais.

### Issue #79

Objetos imutáveis, metadata versus artifact storage, deduplicação, workloads, retenção, custo, backup e portabilidade.

### Issue #81

- diário local e checkpoints automáticos;
- revisões imutáveis e restauração não destrutiva;
- grafo visível e clicável;
- análise vertical e horizontal;
- público/privado por nó;
- pessoas e grupos em privados;
- descendente não amplia acesso herdado;
- revogação ancestral bloqueia descendentes sem apagá-los;
- benchmark de stack de grafo;
- requisitos de BaaS para Storage, metadata e projeções de acesso.

## 3. Pré-backlog v4

Composição:

- A–P: 171 itens;
- Q: 26 itens;
- R: 10 itens;
- S: 26 itens.

Total: **233 itens candidatos em 19 áreas**.

Manifesto: `research/data/ara-draft-backlog-v4-manifest.json`.

Documentos:

- `docs/ideation/draft-backlog-v1.pt-BR.md`;
- `docs/ideation/draft-backlog-agent-profiles-analytics-v2.pt-BR.md`;
- `docs/ideation/draft-backlog-versioning-storage-v1.pt-BR.md`;
- `docs/ideation/draft-backlog-version-graph-access-v1.pt-BR.md`.

Registries correspondentes permanecem em `research/data/`.

Nenhum item possui prioridade, sprint, release ou autorização para implementação.

## 4. Direções incorporadas

### Autoria

```text
editar localmente
→ autosave
→ checkpoint automático
→ sync
→ revisão imutável
```

A plataforma não exige mensagem, aprovação ou confirmação a cada alteração.

### Histórico

- revisão forma DAG;
- restauração cria nova revisão;
- caminhos posteriores permanecem;
- grafo pode ser mostrado diretamente;
- operações, observações, acesso e pesquisa podem ser camadas.

### Acesso

```text
Público
ou
Privado + pessoas/grupos
```

A audiência do descendente é limitada por todos os pais e contêineres necessários. Pode restringir, nunca ampliar. Revogação ancestral pode bloquear descendentes, inclusive para o autor derivado, sem apagar a história.

Nome técnico candidato: **controle de acesso derivacional com atenuação monotônica**.

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

## 5. Dependências conceituais

### Área Q

Objetos de agente, contexto, observações e analytics.

### Área R

Granularidade, workload, Storage, banco, retenção e custo.

### Área S

1. validar audiência e revogação;
2. definir checkpoints e revisões;
3. definir DAG, restore e merge;
4. medir granularidade;
5. prototipar grafo;
6. validar UX de acesso;
7. definir contextos vertical/horizontal;
8. revisar baselines.

## 6. Entrada futura em desenvolvimento

A Issue #9 somente será ativada após decisão explícita do proprietário.

Será necessário:

- revisar o pré-backlog v4;
- promover somente itens decididos;
- revisar produto, domínio, arquitetura e UX;
- medir workloads;
- selecionar infraestrutura por ADR;
- criar issues executáveis novas.

## 7. Regras permanentes

- possibilidade não vira requisito automaticamente;
- item de pré-backlog não autoriza código;
- AraLearn é referência funcional e contraste;
- publicação não significa conclusão definitiva;
- restauração não apaga história;
- contexto legível não concede escrita;
- derivação não amplia audiência;
- autor derivado não contorna revogação ancestral;
- observações não são votação;
- output do GPT não é autoridade científica;
- histórico operacional exige protocolo para pesquisa;
- fontes externas não são armazenadas automaticamente;
- free tier não define a arquitetura;
- provider e stack exigem evidência e decisão posterior.

## 8. Registros históricos

#36–#40 permanecem experimentos não normativos; #42 permanece adiado. #50 e #53 são placeholders `not_planned`.

Issues #59–#74 continuam encerradas como `not_planned`.

## 9. Próxima ação

Executar em paralelo:

1. cenários e casos de borda de #81;
2. workload e granularidade de #79;
3. pacotes de contexto e analytics de #77;
4. protótipos comparativos de grafo;
5. revisão do pré-backlog v4 pelo proprietário.

Não iniciar desenvolvimento nem contratar infraestrutura sem mudança explícita de fase.
