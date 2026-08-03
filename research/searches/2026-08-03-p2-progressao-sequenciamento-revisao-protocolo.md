# Protocolo focado P2 — progressão, sequenciamento, revisão, exemplos e scaffolding

**Versão:** 0.1  
**Data:** 3 de agosto de 2026  
**Issue governante:** #4  
**Fase:** 30 — taxonomia de parametrização  
**Tipo:** pesquisa focada e síntese decisória  
**Autoridade:** `evidence` e `decision-synthesis`; os parâmetros aceitos alimentam a síntese final da Issue #4  
**Não autoriza:** código, algoritmo de produção, schema, scheduler, banco, notificações, adaptação automática, UX, stack ou nova issue

## 1. Pergunta decisória

Como o ARA deve representar progressão, critérios de mastery, autoridade sobre sequência e ritmo, distribuição temporal de revisão, intercalação, exemplos resolvidos, scaffolding, segmentação e retomada após interrupção sem:

- confundir conclusão estrutural com aprendizagem;
- impor um único modelo de mastery;
- reduzir learner control a uma escolha binária;
- tratar spacing e interleaving como a mesma intervenção;
- converter recomendações gerais em algoritmo universal;
- remover apoio com base em inferências não validadas;
- transformar estudo fragmentado em vigilância comportamental?

## 2. Decisões que o pacote pretende informar

P2 deve recomendar:

1. quais dimensões entram na primeira taxonomia;
2. quais valores caracterizam o perfil AraLearn;
3. quais perfis alternativos são conceitualmente defensáveis;
4. como autoridade, locking, override e acessibilidade interagem;
5. quais candidatos permanecem adiados para P3, P4, #5, #6, #7 ou #8;
6. quais simplificações devem ser rejeitadas;
7. quais incertezas podem alterar a recomendação.

P2 não seleciona o recorte de implementação nem um algoritmo.

## 3. Entradas obrigatórias

### 3.1 Evidência interna

- visão vigente do ARA;
- Issue #4;
- síntese integrada da Issue #30;
- Pacote P1 e seus 21 parâmetros aceitos;
- documentação e código auditado do AraLearn no commit `9bff37e`;
- programa de pesquisa e backlog vigentes.

### 3.2 Handoff do P1

P2 recebe explicitamente:

- `practice.purpose`;
- `attempts.retry_target`;
- `hints.access`;
- `consequence.level`;
- perfil `self-directed-mastery`;
- incertezas sobre mastery, equivalência de itens e revisão posterior.

P2 não reabre nem altera as decisões do P1.

## 4. Estratos da amostragem

A amostragem deliberada cobre nove estratos:

1. mastery learning e progressão por critério;
2. learner control, pacing e sequence control;
3. distributed/spaced practice e agenda de revisão;
4. interleaving e discriminação entre categorias;
5. worked examples e transição para resolução independente;
6. scaffolding, fading e expertise reversal;
7. segmentação e carga cognitiva;
8. interrupção, retomada e preservação de contexto;
9. AraLearn e o estudante-trabalhador em estudo mobile/offline.

Cada estrato deve conter pelo menos:

- uma revisão sistemática, meta-análise ou síntese integradora quando disponível;
- um caso contrastante, limite ou resultado nulo;
- uma implicação direta para a decisão taxonômica.

## 5. Busca focada

A rodada é um complemento decisório ao corpus formal já existente, não uma nova revisão sistemática independente.

Frentes de busca, em inglês e português:

- `"mastery learning" meta-analysis threshold progression remediation`;
- `"mastery learning" engineering systematic review reassessment workload`;
- `"learner control" meta-analysis pacing sequence`;
- `segmenting effect meta-analysis learner paced cognitive load`;
- `"distributed practice" classroom meta-analysis spacing schedule`;
- `"spaced digital education" systematic review`;
- `spacing second language meta-analysis equal expanding`;
- `spacing interleaving distinct systematic review`;
- `interleaving meta-analysis similarity discrimination classroom`;
- `"worked example effect" fading problem solving expertise reversal`;
- `"computer-based scaffolding" meta-analysis fading`;
- `interruption resumption context cue working memory`;
- `mobile reading interruption review preview`.

Fontes de localização e verificação:

- páginas de periódicos e DOI;
- PubMed;
- ERIC;
- repositórios institucionais e manuscritos autorais;
- textos integrais abertos;
- bibliografias já versionadas no projeto.

## 6. Critérios de inclusão

- relação direta com ao menos uma decisão P2;
- revisão, meta-análise, estudo comparativo central, orientação metodológica ou evidência implementada do AraLearn;
- descrição suficiente da intervenção ou construto;
- acesso verificável a texto, resumo detalhado ou registro institucional;
- resultado e limitação extraíveis sem extrapolação;
- casos de resultado nulo ou moderação preservados.

## 7. Critérios de exclusão

- marketing de produto sem descrição verificável;
- listas de “boas práticas” sem relação com a pergunta decisória;
- algoritmos de spacing apresentados como universalmente ótimos sem avaliação correspondente;
- estudos que usam `engagement`, tempo ou conclusão como sinônimo não justificado de aprendizagem;
- duplicatas ou versões preliminares quando a publicação final estava disponível;
- trabalhos cuja contribuição já estava representada sem acrescentar categoria, tensão ou limite relevante.

## 8. Extração

Cada fonte registra:

- identificador;
- referência;
- tipo de evidência;
- escopo e população;
- achado principal;
- limite crítico;
- implicação P2;
- profundidade de acesso.

O arquivo estruturado é:

`research/data/p2-evidence-corpus-01.csv`.

## 9. Critério de suficiência

A rodada pode concluir quando:

1. todos os nove estratos estão cobertos;
2. existem contrastes para mastery, learner control, interleaving e fading;
3. as dimensões necessárias deixam de crescer após duas adições sucessivas por estrato central;
4. a evidência permite separar parâmetros sem escolher algoritmo ou valor universal indevido;
5. incertezas remanescentes estão documentadas;
6. nenhuma fonte inacessível indispensável é substituída por suposição;
7. a recomendação pode ser aplicada à taxonomia sem iniciar engenharia.

Suficiência é relativa à taxonomia inicial, não afirma exaustão da literatura.

## 10. Cenários de validação conceitual

A síntese deve explicar:

- estudo pessoal AraLearn, sem mastery gate;
- estudo pessoal guiado com spacing e livre adiamento;
- curso formal com mastery, remediação e deadline;
- avaliação consequencial com pré-requisitos e appeal;
- protocolo que fixa sequência e agenda;
- novato com exemplos e fading reversível;
- estudante experiente com apoio opcional;
- estudante-trabalhador que retoma após interrupção;
- conflito entre protocolo, instituição, autor, estudante e acomodação.

## 11. Produtos

- protocolo focado;
- corpus estruturado;
- registros de parâmetros;
- comparação de perfis;
- síntese decisória em JSON;
- síntese crítica em `pt-BR`;
- bibliografia;
- atualização do programa de pesquisa e do backlog.

## 12. Limitações antecipadas

- a literatura de mastery combina múltiplos componentes;
- spacing aplicado em sala ainda possui menos estudos que o corpus laboratorial;
- interleaving é fortemente moderado por domínio e material;
- worked examples e scaffolding concentram-se em tarefas procedurais e STEM;
- expertise reversal depende de medidas válidas de conhecimento prévio;
- evidência de interrupção é parcialmente oriunda de tarefas não educacionais;
- contextos brasileiros, portugueses, adultos trabalhadores e smartphones modestos permanecem sub-representados;
- esta rodada não avalia scheduler ou interface reais.

## 13. Regra de interpretação

A aceitação de uma dimensão significa que ela deve ser representável, comparável e rastreável na taxonomia. Não significa:

- default universal;
- feature obrigatória na primeira release;
- autorização para persistir eventos;
- aceitação de um algoritmo;
- eficácia comprovada em todo domínio;
- implementação automática.
