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
- versionamento, retenção e Storage;
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

## Artefatos principais

1. [`aralearn-integral-audit-v1.pt-BR.md`](aralearn-integral-audit-v1.pt-BR.md) — leitura do predecessor.
2. [`ara-product-idealization-v1.pt-BR.md`](ara-product-idealization-v1.pt-BR.md) — idealização inicial.
3. [`product-idealization-versioning-access-correction-v2.pt-BR.md`](product-idealization-versioning-access-correction-v2.pt-BR.md) — correção de lifecycle, acesso e grafo.
4. [`kernel-resource-modularity-v1.pt-BR.md`](kernel-resource-modularity-v1.pt-BR.md) — kernel e packages.
5. [`technology-and-baas-options-v1.pt-BR.md`](technology-and-baas-options-v1.pt-BR.md) — alternativas técnicas.
6. [`versioning-storage-economics-v1.pt-BR.md`](versioning-storage-economics-v1.pt-BR.md) — Storage e economia do versionamento.
7. [`agent-profiles-participatory-analytics-v1.pt-BR.md`](agent-profiles-participatory-analytics-v1.pt-BR.md) — agentes, participação e analytics.
8. [`version-graph-derivative-access-low-friction-authorship-v1.pt-BR.md`](version-graph-derivative-access-low-friction-authorship-v1.pt-BR.md) — síntese do grafo, autoria e acesso.
9. [`conversation-decisions-since-pr80-v1.pt-BR.md`](conversation-decisions-since-pr80-v1.pt-BR.md) — ledger de decisões aceitas, rejeitadas e abertas.
10. [`version-graph-ui-options-v1.pt-BR.md`](version-graph-ui-options-v1.pt-BR.md) — Mermaid, Cytoscape.js, React Flow e ELK.js.
11. [`screens-and-states-v1.pt-BR.md`](screens-and-states-v1.pt-BR.md) — telas e estados anteriores.
12. [`wireframes/`](wireframes/) — esquemas visuais não aprovados.

## Pré-backlog versionado

O pré-backlog v4 é a união explícita de:

- **A–P:** 171 itens iniciais;
- **Q:** 26 itens de agentes, participação e analytics;
- **R:** 10 itens de versionamento, retenção e economia operacional;
- **S:** 26 itens de grafo, autoria sem burocracia e acesso derivacional.

Total: **233 itens candidatos em 19 áreas**.

Manifesto: `research/data/ara-draft-backlog-v4-manifest.json`.

Documentos:

- [`draft-backlog-v1.pt-BR.md`](draft-backlog-v1.pt-BR.md);
- [`draft-backlog-agent-profiles-analytics-v2.pt-BR.md`](draft-backlog-agent-profiles-analytics-v2.pt-BR.md);
- [`draft-backlog-versioning-storage-v1.pt-BR.md`](draft-backlog-versioning-storage-v1.pt-BR.md);
- [`draft-backlog-version-graph-access-v1.pt-BR.md`](draft-backlog-version-graph-access-v1.pt-BR.md).

## Frentes focais

### Issue #77 — agentes e analytics

Investiga configuração modular do agente, perfis de domínio, knowledge, MCP, observações, diffs e pesquisa quantitativa, qualitativa e mista.

### Issue #79 — versionamento e infraestrutura

Investiga objetos imutáveis, metadata versus artifact storage, deduplicação, retenção, workloads, custos, exportação e restore.

### Issue #81 — grafo, autoria e acesso

Investiga:

- diário local e checkpoints automáticos;
- revisões imutáveis e restauração não destrutiva;
- grafo visível e navegável;
- análise vertical e horizontal pelo GPT;
- público/privado por nó;
- pessoas e grupos em nós privados;
- acesso do descendente limitado pelos ancestrais;
- revogação ancestral em cascata;
- stack de visualização e requisitos adicionais de BaaS.

Nome técnico candidato:

> controle de acesso derivacional com atenuação monotônica

A interface comum continua usando apenas Público, Privado e Quem pode acessar.

## Resultado comparativo inicial

A solução não corresponde a um único sistema pronto. Ela combina padrões existentes:

- teto de visibilidade hierárquico;
- guardrails herdados por interseção;
- delegação de escopo atenuado;
- políticas que acompanham informação derivada;
- ACLs baseadas em relações;
- provenance DAG;
- versionamento Git-like sobre object storage.

A regra de retirar do autor derivado o acesso ao próprio descendente quando o ancestral revoga acesso é uma decisão específica do ARA e precisa de validação própria.

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
- logs operacionais não viram dados de pesquisa automaticamente.

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

Pacote #81:

- `research/searches/2026-08-05-derivative-access-version-graph-protocol.md`;
- `research/data/derivative-access-version-graph-evidence-corpus-v1.csv`;
- `research/library/derivative-access-version-graph-v1.bib`;
- `research/data/derivative-access-version-graph-manifest-v1.json`.

## Perguntas abertas prioritárias

1. Quando checkpoints locais viram revisões duráveis?
2. A unidade física ideal é microssequência, card ou combinação?
3. Como funciona um merge com múltiplos pais?
4. Que metadata pode aparecer num nó bloqueado?
5. Como mudanças em grupos afetam snapshots de pesquisa?
6. Como calcular e invalidar audiência efetiva em escala?
7. Qual stack apresenta melhor o grafo no mobile?
8. Que BaaS atende Storage imutável, metadata, acesso e sync?
9. Como reter e coletar lixo sem apagar evidência necessária?
10. Que exceções legais ou de segurança exigem fluxo próprio?
