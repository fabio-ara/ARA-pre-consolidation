# Extensão do pré-backlog — grafo de versões, acesso derivacional e autoria sem burocracia

**Estado:** candidato para discussão; não executável  
**Área:** S  
**Issue:** #81

Esta área incorpora a discussão posterior à PR #80 e deve ser lida com as áreas Q e R.

## S01 — Princípio de autoria sem medo

Preservar trabalho rápido e reversível; o sistema assume checkpoints e histórico sem confirmações recorrentes.

## S02 — Diário local no IndexedDB

Manter autosave, undo/redo, estado da interface e operações ainda não sincronizadas com retenção configurável.

## S03 — Política de checkpoints automáticos

Investigar eventos, janelas de inatividade e compactação que transformam trabalho local em checkpoint sem poluir o histórico.

## S04 — Revisões duráveis sincronizadas

Criar revisões imutáveis quando alterações significativas são sincronizadas ou concluídas.

## S05 — Grafo acíclico de revisões

Representar pais, derivações, restaurações e combinações sem impor linha única nem excluir caminhos.

## S06 — Restauração não destrutiva

Restaurar cria nova revisão e preserva as posteriores para comparação e investigação.

## S07 — Grafo visível e navegável

Abrir nós, conteúdo, diff, autoria, operação, observações, acesso e referências de pesquisa.

## S08 — Camadas e filtros do grafo

Alternar versões, operações, observações, acesso e pesquisa sem exibir tudo simultaneamente.

## S09 — Manifesto de microssequência e objetos menores

Avaliar microssequência como unidade editorial e cards/resources como unidades endereçáveis e deduplicáveis.

## S10 — Análise vertical

Montar contexto longitudinal de revisões, operações, reparos, reversões e configurações do agente.

## S11 — Análise horizontal

Compilar observações, branches, participantes e artefatos para identificar convergências e divergências.

## S12 — Ciclo vertical-horizontal

Usar padrão transversal para abrir investigação longitudinal e avaliar reparo posteriormente.

## S13 — Recuperação de contexto do histórico

Selecionar nós, diffs e evidências relevantes sem enviar todo o grafo à LLM.

## S14 — Visibilidade binária por nó

Oferecer apenas Público e Privado em curso, lição, microssequência, card, resource e revisão quando aplicável.

## S15 — Lista de acesso de nó privado

Permitir usuários e grupos nominalmente indicados, com interface simples de busca e remoção.

## S16 — Atenuação monotônica por derivação

Descendente pode restringir, nunca ampliar, a audiência recebida dos pais necessários.

## S17 — Audiência efetiva por interseção

Calcular acesso a partir do nó, pais e contêineres necessários; pesquisar cache e invalidação.

## S18 — Revogação ancestral em cascata

Revogação bloqueia descendentes para o sujeito afetado, inclusive autor derivado, sem apagar o grafo.

## S19 — Nós bloqueados e reativação

Definir metadata visível, motivo, preservação e reativação quando acesso ancestral retorna.

## S20 — Derivações colaborativas

Permitir múltiplos descendentes de uma revisão sob o mesmo teto de acesso, sem edição destrutiva da origem.

## S21 — Acesso e pesquisa reproduzível

Fixar snapshot de audiência, grupos e versões quando um protocolo exigir reprodutibilidade.

## S22 — Lifecycle sem publicação final

Substituir estado final por visibilidade, versão atual, versão fixada, disponibilidade e trajetória.

## S23 — Escopo de artefatos armazenados

Não armazenar automaticamente fontes externas; armazenar artefatos gerados e proveniência interna.

## S24 — Backend compatível com grafo e Storage

Exigir artifact storage imutável, metadata transacional, projeções de acesso, sync e export/restore.

## S25 — Benchmark da stack de grafo

Comparar Mermaid, Cytoscape.js, React Flow, ELK/Dagre e alternativas segundo UX, acessibilidade e escala.

## S26 — Histórico operacional versus evidência de pesquisa

Não reutilizar automaticamente logs e versões como dados acadêmicos; exigir protocolo, finalidade e snapshot.

## Sequência de investigação

1. validar o modelo de audiência e os casos de borda;
2. definir o ledger de revisões e restaurações;
3. medir granularidade e workload com #79;
4. prototipar o grafo em mais de uma stack;
5. validar UX de público/privado, lista e bloqueio;
6. definir pacotes de contexto vertical e horizontal;
7. revisar produto, domínio, arquitetura e UX;
8. somente depois promover itens para implementação.
