# Opções para visualização do grafo de versões

**Estado:** comparação técnica inicial; nenhuma seleção  
**Issue:** #81

## Objetivo

Exibir um DAG de versões com nós clicáveis, pan/zoom, filtros e detalhes situados, sem exigir vocabulário Git.

## Mermaid

**Forças**

- baixo atrito;
- boa integração em Markdown e documentação;
- sintaxe declarativa;
- callbacks e links em nós;
- adequado a protótipos e grafos pequenos.

**Limites**

- interação depende da configuração de segurança;
- menor controle de virtualização, seleção e edição;
- pode ficar difícil em grafos extensos;
- não é uma engine completa de exploração.

**Uso candidato:** protótipo, relatório ou trajetória curta predominantemente de leitura.

## Cytoscape.js

**Forças**

- biblioteca de grafos completa;
- nós, edges, travessia e filtros;
- pan, zoom, eventos e seleção;
- layouts para DAGs, compound graphs e redes grandes;
- extensões para Dagre e ELK.

**Limites**

- exige modelagem e styling próprios;
- componentes ricos dentro de nós requerem trabalho adicional.

**Uso candidato:** exploração investigativa de linhagens, observações e relações.

## React Flow

**Forças**

- nós React customizáveis;
- pan, zoom, seleção e edição já integrados;
- bom para painéis, formulários e ações dentro dos nós;
- adequado a superfícies de autoria.

**Limites**

- menos orientado a algoritmos de análise de grafos;
- layout automático costuma depender de Dagre ou ELK;
- grafos muito grandes exigem avaliação específica.

**Uso candidato:** grafo como editor ou navegador com controles ricos.

## ELK.js

**Forças**

- engine de layout direcionado;
- apropriada para diagramas com fluxo e portas;
- pode rodar em Web Worker;
- complementa renderers.

**Limites**

- não renderiza;
- precisa ser combinado com outra biblioteca;
- configuração de layout pode ser complexa.

## Direção de protótipo

Comparar ao menos:

1. Mermaid para trajetória curta;
2. Cytoscape.js + layout DAG para exploração;
3. React Flow + ELK para nós ricos.

Critérios:

- legibilidade mobile;
- navegação por teclado;
- acessibilidade não visual;
- pan/zoom e foco;
- seleção de nó;
- filtros por camada;
- performance com 100, 1.000 e 10.000 revisões;
- atualização incremental;
- representação de nó bloqueado;
- integração com diff e preview;
- bundle e memória.

Nenhuma stack é autorizada por este documento.
