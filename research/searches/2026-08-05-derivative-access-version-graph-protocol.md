# Protocolo de pesquisa — acesso derivacional, grafo de versões e autoria sem burocracia

**Data:** 5 de agosto de 2026  
**Issue:** #81  
**Tipo:** revisão de escopo técnica e interdisciplinar

## Objetivo

Verificar se o modelo proposto para o ARA possui precedentes, em quais contextos eles são adotados e quais limites precisam ser investigados antes de formalização arquitetural.

## Perguntas

1. Existem modelos em que descendentes não podem conceder mais acesso do que receberam?
2. Existem sistemas com teto de visibilidade herdado?
3. Como políticas de múltiplos ancestrais são combinadas?
4. Como restrições acompanham dados derivados?
5. Como ACLs relacionais são avaliadas em grande escala?
6. Como provenance e version DAGs são representados?
7. Como versionamento Git-like funciona sobre object storage?
8. Como trabalho local e histórico são combinados sem cerimônia?
9. Quais bibliotecas suportam um grafo interativo no navegador?

## Frentes e termos

- `hierarchical visibility`;
- `permission guardrails intersection`;
- `attenuated delegation`;
- `scope attenuation`;
- `decentralized label model`;
- `derived data access control`;
- `relationship-based access control`;
- `provenance DAG`;
- `content-addressed version graph`;
- `zero-copy branching object storage`;
- `local-first software`;
- `selective event sourcing`;
- `interactive DAG visualization`.

## Inclusão

- standards e RFCs;
- documentação oficial de sistemas adotados;
- artigos primários;
- sistemas de produção descritos por seus autores;
- documentação oficial de bibliotecas.

## Exclusão

- posts sem fonte primária;
- listas genéricas de ferramentas;
- soluções blockchain sem relação material com a pergunta;
- marketing sem descrição técnica suficiente;
- modelos que apenas reproduzem RBAC global sem derivação.

## Extração

Para cada fonte:

- padrão;
- contexto;
- regra de herança ou delegação;
- regra de revogação;
- escala;
- semelhança com o ARA;
- diferença;
- implicação;
- limite.

## Limitações

- não é revisão sistemática exaustiva;
- a regra de bloquear o autor derivado por revogação ancestral é específica do ARA;
- comparação de performance depende de protótipo;
- não substitui análise jurídica;
- nenhuma biblioteca ou backend é selecionado.
