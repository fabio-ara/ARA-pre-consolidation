# Benchmark de sistemas estruturados e interativos — rodada 01

**Data local:** 2 de agosto de 2026  
**Issues:** #33 e #34  
**Estado:** benchmark exploratório concluído para 21 sistemas ou famílias de sistemas

## 1. Finalidade

Esta rodada compara sistemas maduros que enfrentam problemas ausentes ou apenas parcialmente representados no AraLearn. O objetivo não é escolher uma stack nem copiar uma plataforma. É identificar separações arquiteturais, gramáticas de domínio, modelos de resposta, validadores e contratos de extensão que precisam ser compreendidos antes de reconstruir os `resources` da ARA.

Os dezoito `resources` do AraLearn são tratados aqui como **corpus legado situado**. Eles registram demandas efetivamente atendidas, em grande parte relacionadas a TADS e estudo técnico, mas não constituem uma ontologia dos domínios do conhecimento nem uma decisão de herança.

## 2. Método e fontes

Foram auditados repositórios oficiais, em revisões ou commits fixados no manifesto `cross-domain-repository-manifest-01.csv`. A leitura priorizou:

1. representação canônica do conteúdo ou do estado;
2. ação e resposta produzidas pelo estudante;
3. validação e avaliação;
4. feedback;
5. autoria e extensão;
6. separação entre modelo, runtime e renderer;
7. acessibilidade, dispositivos móveis e funcionamento local;
8. segurança e licenciamento.

O benchmark contém **21 sistemas**, distribuídos por mais de oito famílias técnicas e cobrindo matemática, programação, química, biologia molecular, física, geografia, música, eletrônica digital, línguas, humanidades, ciência de dados e estruturas de dados.

Capacidade técnica não foi interpretada como evidência de aprendizagem. A evidência acadêmica complementar está em `structured-learning-literature-01.csv`.

## 3. Khan Academy: o caso Perseus

Khan Academy não deve ser reduzida aos vídeos. O repositório Perseus declara-se como o sistema de exercícios da plataforma: recebe um problema em seu formato, apresenta-o, recolhe a interação e atribui resultado.

A arquitetura observada separa:

- schemas dos widgets;
- componentes de interação;
- estado de entrada do usuário;
- editores autorais;
- validadores e scorers específicos;
- documentação de acessibilidade;
- testes unitários e visuais;
- registro dos widgets.

O catálogo inclui, entre outros, expressão matemática, entrada numérica, categorização, ordenação, matriz, reta numérica, gráfico interativo, programas, resposta livre, simulação PhET e rotulagem de imagem.

A lição para a ARA não é importar esse catálogo. É reconhecer que **representação e exercício podem formar um sistema tipado extensível**, com pontuação fora do renderer. O próprio Perseus também mostra riscos: widgets legados heterogêneos, dependências institucionais, recursos de mídia e iframe incompatíveis com o baseline seguro e textual da ARA.

## 4. Avaliação matemática: Numbas, STACK, MathLive e JSXGraph

### 4.1 Numbas

Numbas usa um documento JSON para exames, questões, partes, feedback e diagnóstico. Seus tipos personalizados podem declarar:

- widget de entrada;
- script de correção;
- settings autorais;
- extensões;
- uso como lacuna ou passo;
- relação com objetivos e tópicos diagnósticos.

A principal contribuição conceitual é tratar uma questão como composição de **partes de resposta**, não como uma única forma visual.

### 4.2 STACK

STACK apresenta a distinção mais importante desta rodada: **validade não é correção**. O estudante pode produzir uma expressão matematicamente interpretável ou uma entrada sintaticamente problemática antes de qualquer julgamento de correção. A plataforma pode mostrar como interpretou a resposta, aplicar testes de propriedades matemáticas, oferecer crédito parcial, trabalhar com várias entradas e usar árvores de resposta.

Esse desenho evita reduzir matemática a alternativas ou igualdade textual. Também mostra que um validador de domínio deve responder a perguntas como:

- a expressão é válida?
- é equivalente?
- está fatorada?
- possui as unidades corretas?
- preserva uma propriedade exigida?
- o erro de uma parte pode ser carregado para a seguinte sem destruir toda a avaliação?

STACK é uma referência conceitual forte, mas sua dependência de Moodle, Maxima e GPL não o transforma automaticamente em componente a reutilizar.

### 4.3 MathLive

MathLive fornece entrada matemática editável, teclado móvel, acessibilidade, fala matemática e intercâmbio entre LaTeX, MathML, ASCIIMath, Typst e MathJSON. A separação relevante é entre:

- componente de entrada;
- representação matemática;
- renderização;
- validação posterior.

ARA precisa escolher uma forma canônica própria e não permitir que todos os formatos externos se tornem simultaneamente autoridade.

### 4.4 JSXGraph

JSXGraph trabalha com objetos geométricos, gráficos de funções e visualizações manipuláveis. Diferentemente do `plane` legado, o estudante pode construir ou mover objetos. A biblioteca, porém, não define sozinha o que constitui resposta correta. ARA precisará preservar o estado semântico da construção e aplicar predicados educativos separados.

## 5. Modelos relacionais e de construção

### 5.1 Cytoscape.js

Cytoscape.js separa um modelo de teoria dos grafos de um renderer opcional. Pode operar sem interface para executar algoritmos e predicados. Essa arquitetura é mais adequada que persistir coordenadas como conteúdo.

Entretanto, uma rede biológica, um autômato, um circuito e um argumento causal não são a mesma gramática só porque usam nós e ligações. O motor pode ser compartilhado; a semântica de domínio não deve ser apagada.

### 5.2 Blockly

Blockly representa programas com blocos tipados e conectáveis. O estudante produz uma estrutura, não escolhe apenas uma resposta. O projeto também possui plugins e documentação explícita de acessibilidade por teclado e leitor de tela.

A lição é que respostas construtivas podem ter:

- documento serializável;
- restrições estruturais;
- operações permitidas;
- alternativas ao arrastar;
- renderer substituível;
- validação pelo estado final ou pelo histórico de operações.

Blocos não são, contudo, uma metáfora universal. Eles podem ocultar notações disciplinares e reduzir tarefas que exigem escrita simbólica ou argumento contínuo.

### 5.3 CircuitVerse

CircuitVerse mostra uma gramática que o `graph` e o `system_map` do AraLearn não expressam adequadamente: componentes lógicos, portas, fios, entradas, saídas e estado de simulação. Um circuito não é apenas um grafo ilustrado. Sua topologia e seu comportamento podem ser validados de modo determinístico.

## 6. Programação executável

### 6.1 Pyodide

Pyodide permite executar CPython e bibliotecas científicas no navegador por WebAssembly. Ele é um runtime, não uma plataforma de avaliação. ARA precisaria adicionar:

- worker isolado;
- limites de tempo e memória;
- política de rede e arquivos;
- versão reproduzível do ambiente;
- testes públicos e protegidos;
- tradução de erros em feedback pedagógico;
- registro do que foi executado.

### 6.2 Papyros

Papyros organiza editor, execução, entrada, saída e debugger em camadas distintas. Seu estado inclui código, IO, frames de depuração, linguagem e testes. É um precedente mais próximo para uma capacidade educativa de programação, mas ainda não define por si só critérios curriculares ou avaliação válida.

### 6.3 OpenDSA

OpenDSA combina texto de qualidade de livro, visualizações de algoritmos e exercícios avaliados automaticamente. Ele demonstra que narrativa, manipulação e avaliação podem estar coordenadas em uma sequência. Sua arquitetura histórica e seu foco em estruturas de dados impedem tratá-lo como contrato genérico.

## 7. Sistemas extensíveis e autoria

### 7.1 H5P

H5P usa bibliotecas versionadas identificadas por `machineName`, dependências e schemas autorais. O tipo Drag Question mostra uma estrutura que inclui elementos, zonas, relações corretas, feedback local, políticas de tentativa, penalidades e localização.

O modelo é instrutivo para packages tipados, mas também demonstra o risco de extensões abertas:

- código executável por tipo;
- dependências e versões;
- licenças por biblioteca;
- campos de geometria e mídia;
- superfície de segurança ampla;
- qualidade de acessibilidade desigual.

ARA não deve permitir que um curso forneça código de componente. Cursos devem referenciar apenas capacidades instaladas e aprovadas.

### 7.2 Open edX XBlock

XBlock define componentes de courseware implantáveis e hierárquicos. A separação entre componente e runtime é útil. O modelo de plugin Python executável, porém, é pesado para um núcleo móvel, offline e seguro.

### 7.3 Jupyter Widgets

Jupyter Widgets sincroniza modelos de estado com views no navegador e permite bibliotecas especializadas. É um precedente forte para controles e simulações, mas pressupõe kernel e extensões potencialmente arbitrárias. ARA precisa de um contrato muito mais estreito.

## 8. Gramáticas declarativas e notação

### 8.1 Mermaid

Mermaid compila gramáticas textuais em muitos tipos de diagrama. Ele prova que uma representação pode ser declarativa, versionável e independente da geometria. Não prova que uma gramática única é adequada a todos os domínios nem que editar texto declarativo é a melhor tarefa para todo estudante.

### 8.2 OpenSheetMusicDisplay

OpenSheetMusicDisplay usa MusicXML como modelo canônico e o transforma em partitura. Isso revela uma lacuna profunda do AraLearn: música necessita de uma gramática própria para alturas, durações, compassos, vozes, pautas e tablaturas. Uma `sequence` ou `formula` genérica não preservaria essa epistemologia.

O projeto é renderer, não editor ou avaliador. ARA precisaria separar MusicXML ou outra gramática, entrada musical, validação e feedback.

## 9. Domínios espaciais, científicos e simbólicos

### 9.1 Leaflet

Leaflet oferece mapas interativos, camadas, marcadores e extensões. Abre atividades de geografia, história espacial e ambiente. Traz dependências específicas: tiles, atribuição cartográfica, funcionamento offline, precisão espacial e alternativas não visuais.

### 9.2 Mol*

Mol* separa parsing de formatos científicos, modelos moleculares, queries, estado, representações e UI. Para química e biologia, mostra que uma molécula não deve ser reduzida a imagem ou fórmula textual. O estado científico pode ser consultado e transformado.

### 9.3 PhET — balanceamento de equações

A simulação PhET de balanceamento coordena coeficientes, equação simbólica e contagem visual de moléculas. Ela mostra por que o `reaction` legado cobre somente uma camada simbólica. Uma capacidade de simulação requer modelo, estado, controles, observações e objetivos; não é apenas animação.

## 10. Línguas, texto e humanidades

### 10.1 Recogito Text Annotator

Recogito permite ao estudante selecionar trechos, criar anotações e associar corpos de comentário ou tags. O modelo se aproxima do W3C Web Annotation e preserva alvo, citação e offsets.

Esse precedente permite imaginar respostas como:

- marcar evidência numa fonte;
- classificar função argumentativa;
- vincular comentário ao trecho;
- comparar anotações;
- justificar interpretação.

O `annotated_text` do AraLearn exibe anotações autorais; não representa adequadamente anotações produzidas pelo estudante.

### 10.2 LanguageTool

LanguageTool detecta problemas de ortografia, gramática e estilo em vários idiomas. Pode funcionar como validador auxiliar de produção textual, mas não mede competência linguística nem qualidade argumentativa. Suas sugestões precisam ser tratadas como diagnósticos locais, não como nota global.

## 11. Conclusões transversais

### 11.1 Quantidade de resources não resolve o problema

Um catálogo maior continua pobre se cada item mistura conteúdo, interação e correção. A reconstrução precisa separar:

```text
representação
× atividade
× resposta
× validação
× feedback
× runtime opcional
× renderer
```

### 11.2 Gramáticas de domínio são legítimas

Algumas primitivas podem ser compartilhadas, mas há estruturas irredutíveis:

- MusicXML não é uma sequência genérica;
- circuito não é grafo genérico;
- molécula não é imagem;
- mapa não é plano cartesiano;
- expressão matemática não é texto;
- anotação de fonte não é uma alternativa;
- programa executável não é bloco de código estático.

### 11.3 Validade, correção e feedback são fases separadas

A resposta pode ser:

1. ausente;
2. sintaticamente inválida;
3. válida, mas não avaliável pelo validador selecionado;
4. válida e incorreta em uma propriedade;
5. parcialmente satisfatória;
6. correta;
7. submetida para avaliação humana ou probabilística.

O renderer não deve decidir essas categorias.

### 11.4 Extensibilidade exige governança

A arquitetura deve admitir novas capacidades sem aceitar código arbitrário nos cursos. O caminho sugerido é:

- catálogo instalado de componentes aprovados;
- manifests versionados;
- schemas fechados;
- permissões e requisitos explícitos;
- adapters de renderer e validator;
- assinatura e proveniência;
- testes de acessibilidade e segurança;
- política de offline e tamanho do pacote.

### 11.5 O benchmark não seleciona stack

MathLive, JSXGraph, Cytoscape.js, Pyodide e outras bibliotecas são candidatas a protótipos, não decisões. H5P, STACK, Numbas, Perseus e XBlock são também precedentes arquiteturais, mesmo quando reutilização direta seria inadequada.

## 12. Saída para a próxima etapa

A próxima especificação deverá propor um contrato de componente com, no mínimo:

- `representationSchema`;
- `activitySchema`;
- `responseSchema`;
- `validatorContract`;
- `feedbackContract`;
- `runtimeRequirements`;
- `rendererAdapter`;
- `accessibilityContract`;
- `offlineProfile`;
- `securityBoundary`;
- `localizationContract`;
- `provenance` e versão.

Esse contrato será testado em protótipos conceituais de matemática, grafos/geometria, programação, anotação de fontes, mapas, química/simulação, música, línguas e circuitos antes de qualquer implementação ampla.
