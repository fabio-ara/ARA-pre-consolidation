# Auditoria canônica dos `resources` do AraLearn — rodada 01

**Data:** 3 de agosto de 2026  
**Issue:** #31 (`[32] Audit the canonical AraLearn resource contracts`)  
**Fonte auditada:** `fabio-ara/AraLearn`  
**Commit de referência:** `9bff37eee3ba80263084328dc5897d26c7ca3d5a`  
**Estado:** auditoria inicial concluída; decisões para a ARA são provisórias e não alteram o AraLearn

## 1. Finalidade e limite

Esta auditoria registra o contrato realmente implementado no AraLearn para impedir que a futura taxonomia da ARA seja reconstruída por memória, analogia com flashcards comerciais ou extrapolação de funcionalidades inexistentes.

A fonte de verdade foi confrontada em cinco camadas:

1. documentação pública do contrato;
2. registry normativo dos recursos e da autoria;
3. mecanismos de lacuna e prática estruturada;
4. validação, round-trip relacional e renderização;
5. cenários disciplinares executáveis dos testes.

Quando uma capacidade não aparece nessas camadas, ela não é tratada como funcionalidade do AraLearn.

O resultado descreve o **baseline implementado**. Ele não estabelece eficácia pedagógica, não encerra a taxonomia da ARA e não transforma limitações atuais em regras universais.

## 2. Contratos e autoridade técnica

O documento de curso usa:

- `aralearn.contract`, versão `4`;
- hierarquia `project → course → module → lesson → microsequence → card`;
- um único `resource` principal por card;
- `kind: theory | exercise`;
- `exercise: none | gap | choice`.

O registry declara:

- `aralearn.resources.v4`;
- `aralearn.authoring-resources.v4`;
- 18 recursos canônicos;
- limites semânticos e móveis;
- schemas fechados com rejeição de propriedades desconhecidas;
- critérios de uso e de não uso;
- operações autorais;
- alvos formais de lacuna.

`RESOURCE_TYPES` é derivado diretamente do registry. O teste disciplinar verifica que a lista é idêntica no domínio, no contrato, na persistência relacional, na geração, na autoria e no enum SQL.

## 3. Conceitos que não devem ser confundidos

### `card`

Unidade ordenada dentro de uma microssequência. Orquestra conteúdo, interação e feedback. Não é sinônimo de flashcard.

### `resource`

Representação semântica estruturada. Preserva texto, grade, hierarquia, conectividade, notação, sequência, alinhamento linguístico ou outra estrutura necessária à operação.

### `exercise`

Mecânica geral declarada pelo card:

- `none`: exposição ou exemplo;
- `gap`: resposta localizada num campo do próprio recurso;
- `choice`: confirmação de um conjunto de alternativas.

`gap` não é um recurso.

### `response`

No baseline há três modelos efetivos:

1. alternativa autoral em uma lacuna;
2. texto literal numa lacuna, com variantes enumeradas;
3. seleção `single` ou `multiple` por conjunto exato.

O `flow` acrescenta prática estruturada de forma, texto de nó e rótulo projetado de aresta.

Não há regex, equivalência semântica, correção por LLM durante o estudo, crédito parcial implícito ou resposta aberta avaliada por rubrica.

### `feedback`

- `after`: explicação posterior canônica do card;
- `options[].feedback`: explicação local opcional;
- resultado só aparece após confirmação;
- `afterBlocks`: de 1 a 5 blocos estruturados adicionais.

A existência desses campos não significa que conteúdo, timing e função do feedback já estejam modelados como parâmetros pedagógicos independentes. Isso pertence à taxonomia da ARA.

### `composite`

Coordena de 2 a 5 blocos que precisam permanecer juntos. Não aceita outro `composite` como bloco. Um exercício `choice` possui exatamente um bloco de escolha; um exercício `gap` não usa bloco de escolha.

## 4. Catálogo canônico

| Recurso | Estrutura principal | Exercícios | Decisão provisória |
|---|---|---|---|
| `paragraph` | texto contínuo | `none`, `gap` | preservar |
| `choice` | alternativas comparáveis | `choice` | preservar |
| `composite` | blocos inseparáveis | `none`, `gap`, `choice` | preservar |
| `code` | linguagem, linhas e indentação | `none`, `gap`, `choice` | preservar |
| `table` | linhas e colunas | `none`, `gap`, `choice` | preservar |
| `flow` | sequência, decisão, ramos e laços | `none`, `gap`, `choice` | revisar |
| `tree` | hierarquia de pai único | `none`, `gap`, `choice` | preservar |
| `graph` | vértices e arestas | `none`, `gap`, `choice` | revisar |
| `relation_map` | dois conjuntos e relações | `none`, `gap`, `choice` | preservar |
| `matrix` | grade ou sequência de grades | `none`, `gap`, `choice` | preservar |
| `plane` | eixos, pontos e vetores | `none`, `gap`, `choice` | revisar |
| `formula` | AST matemática ou química | `none`, `gap`, `choice` | preservar |
| `chart` | séries e eixos quantitativos | `none`, `gap`, `choice` | revisar |
| `sequence` | ordem, cronologia ou ciclo | `none`, `gap`, `choice` | preservar |
| `annotated_text` | segmentos e notas locais | `none`, `gap`, `choice` | preservar |
| `linguistic_example` | forma, leitura, IPA, glosa e tradução | `none`, `gap`, `choice` | preservar |
| `system_map` | limites, grupos, componentes e conexões | `none`, `gap`, `choice` | revisar |
| `reaction` | reagentes, produtos e condições | `none`, `gap`, `choice` | preservar |

Nenhum recurso foi marcado para retirada nesta rodada. “Revisar” significa preservar a necessidade representacional, mas reavaliar contrato, interação, universalidade ou apresentação antes de incorporá-lo à ARA.

## 5. Limites transversais confirmados

### 5.1 O baseline é JSON textual e estruturado

Não existem recursos canônicos de:

- imagem;
- áudio;
- vídeo;
- iframe;
- arquivo binário;
- execução de código;
- simulação;
- laboratório virtual.

O teste de renderização verifica explicitamente que os 18 recursos não produzem `<script>`, `<img>` ou `<iframe>` a partir do conteúdo.

Texto para fala permanece apenas uma hipótese futura de **rendição derivada do texto canônico**, não um resource e não conteúdo binário embutido no JSON.

### 5.2 O renderer detém a geometria

A autoria fornece entidades, relações, presets semânticos e destaques por ID. Não fornece coordenadas visuais, cor ou HTML livre para `flow`, `graph`, `system_map` e demais estruturas. Isso preserva consistência móvel, segurança e portabilidade.

### 5.3 Campos desconhecidos não sobrevivem silenciosamente

Os schemas usam propriedades fechadas e o teste de round-trip injeta um campo inexistente em cada resource para confirmar que a persistência o rejeita em vez de descartá-lo.

### 5.4 A prática é localizada, mas ainda restrita

As lacunas podem ocupar células, código, rótulos, pesos, valores matriciais, folhas de fórmula e muitos outros campos. Entretanto, vários atos disciplinares ainda não são respostas estruturadas:

- construir um grafo;
- posicionar um ponto;
- reordenar etapas;
- desenhar um fluxo;
- escrever e executar código;
- produzir uma prova;
- anotar livremente um texto;
- balancear uma reação com validação química.

Hoje essas atividades precisam ser aproximadas por lacuna ou escolha.

## 6. Pontos fortes do contrato

1. **Separação entre semântica e geometria:** a estrutura sobrevive a diferentes renderizações.
2. **Portabilidade e offline:** o curso permanece um documento JSON autocontido.
3. **Autocontenção da prática:** os testes exigem que os dados variáveis necessários estejam no próprio card.
4. **Segurança:** marcação fornecida pelo conteúdo é escapada.
5. **Internacionalização:** BCP 47, direção textual, Unicode, RTL e escrita vertical já fazem parte do baseline.
6. **Granularidade da lacuna:** a resposta ocorre dentro da representação, não numa pergunta genérica separada.
7. **Cobertura disciplinar real:** o fixture inclui programação, matemática, química, estatística, redes, processos, biologia, economia, idiomas, direito, engenharia, história, argumentação e arquitetura de sistemas.
8. **Composição conservadora:** `composite` coordena representações sem abrir um renderer arbitrário.

## 7. Limitações com impacto na ARA

### 7.1 Atividade não é entidade de primeira classe

O registry descreve operações como “completar código”, “interpretar dependência” e “localizar outlier”, mas o contrato do card registra principalmente representação e mecânica (`none`, `gap`, `choice`). A ARA precisa decidir se `activity` será uma entidade explícita, um vocabulário controlado ou apenas metadado de autoria.

### 7.2 Respostas estruturadas são escassas

A riqueza representacional é maior que a riqueza das respostas. Em muitos resources, o estudante observa uma estrutura e responde por escolha. Uma plataforma mais universal precisará investigar respostas estruturadas sem abandonar determinismo, acessibilidade móvel e uso offline.

### 7.3 `system_map` está semanticamente estreito

A intenção documentada inclui cadeias logísticas e sistemas sociotécnicos, mas os kinds de componentes são:

`client`, `service`, `database`, `queue`, `storage`, `gateway`, `worker`, `external`.

Esses valores são fortemente orientados a arquitetura de software. A ARA deve generalizar por extensão tipada ou separar perfis de domínio, sem substituir semântica por strings livres.

### 7.4 `chart` limita prática nos dados

Lacunas alcançam rótulos e unidades de eixo e nome de série, mas não valores ou pontos. Isso restringe tarefas de leitura e produção quantitativa.

### 7.5 `plane` não captura construção espacial

A lacuna está limitada ao resultado textual. O estudante não posiciona pontos ou vetores nem produz uma coordenada estrutural.

### 7.6 `flow` possui dois modelos de prática

Há lacunas textuais e um segundo contrato de prática estruturada para forma, texto e rótulo de aresta. A capacidade é relevante, mas aumenta a complexidade do contrato, do renderer, da autoria e da auditoria.

### 7.7 `graph` depende fortemente do layout derivado

A ausência de coordenadas é uma virtude de portabilidade, mas rótulos, cruzamentos e densidade precisam de validação visual e acessível. A limitação relatada pelo uso real deve ser investigada como problema do renderer, não resolvida com geometria livre no JSON.

### 7.8 `code` não é ambiente de programação

O resource preserva código e lacunas, mas não executa, compila, testa, depura nem isola programas. Uma futura capacidade executável deve ser uma frente própria, com segurança, linguagens, limites, offline e feedback definidos.

### 7.9 Áudio não faz parte de `linguistic_example`

O resource preserva IPA, leitura e tradução, mas não som. TTS pode ser avaliado depois como rendição opcional; gravação e avaliação de fala seriam outra capacidade, com implicações de privacidade e validade.

## 8. Cobertura disciplinar auditada

Os testes existentes já fornecem uma matriz melhor que uma lista hipotética. Entre os cenários:

- programação usa `code`;
- cálculo e química simbólica usam `formula`;
- estatística usa `table` e `chart`;
- álgebra linear usa `matrix`;
- grafos e redes usam `graph`;
- geometria analítica usa `plane`;
- processos usam `flow` e `sequence`;
- biologia usa `tree`;
- contabilidade usa `relation_map`;
- idiomas usam `paragraph`, `choice` e `linguistic_example`;
- direito e argumentação usam `paragraph`, `choice` e `annotated_text`;
- engenharia ambiental usa `composite`;
- arquitetura usa `system_map`;
- química de reações usa `reaction`.

Essa cobertura confirma que o AraLearn já é substancialmente mais rico que um sistema de flashcards frente-verso. Ela não demonstra que todos os domínios estejam suficientemente atendidos.

## 9. Decisões provisórias

### Preservar

`paragraph`, `choice`, `composite`, `code`, `table`, `tree`, `relation_map`, `matrix`, `formula`, `sequence`, `annotated_text`, `linguistic_example` e `reaction`.

A preservação diz respeito à função representacional, não a copiar todos os campos sem revisão.

### Revisar

- `flow`: simplificar e validar a coexistência de lacunas e prática estruturada;
- `graph`: melhorar legibilidade e estudar respostas construtivas;
- `plane`: acrescentar respostas coordenadas/geométricas sem drag-and-drop obrigatório;
- `chart`: permitir tarefas sobre dados, não apenas sobre nomes e eixos;
- `system_map`: generalizar semântica de domínio sem aceitar kinds arbitrários.

### Retirar

Nenhum resource nesta etapa.

### Avaliar como capacidade separada

- execução segura de código;
- simulação;
- construção/manipulação estruturada;
- resposta aberta com rubrica;
- TTS derivado de texto;
- gravação e avaliação de fala.

Nenhuma dessas capacidades deve ser descrita como herdada do AraLearn.

## 10. Próximas pesquisas orientadas por lacunas

A busca seguinte não deve usar “flashcard” como termo central. Ela deve ser dividida por problema:

1. múltiplas representações e coordenação;
2. respostas construtivas em diagramas, grafos e geometria;
3. ambientes de programação e feedback automático;
4. representações matemáticas e transição entre registros;
5. leitura e produção de gráficos;
6. química em níveis simbólico, macroscópico e submicroscópico;
7. exemplos linguísticos, TTS e aprendizagem auditiva;
8. acessibilidade de visualizações estruturadas;
9. autoria por schemas tipados;
10. atividades disciplinares e práticas epistêmicas.

## 11. Consequência imediata para a Issue #30

A Issue #30 deve usar o inventário atual como ponto de partida e não como limite. O próximo artefato será a matriz:

`domain × learning objective × activity × representation × response × feedback × evidence status`.

O contrato atual já informa a coluna de representação. As maiores lacunas estão nas colunas de atividade e resposta.

## 12. Fontes internas auditadas

- `README.md`;
- `docs/aralearn-contract.md`;
- `docs/recursos-de-card.md`;
- `docs/modelo-didatico.md`;
- `docs/fundamentacao-pedagogica-dos-resources.md`;
- `src/resources/registry/index.js`;
- `src/resources/registry/authoring.js`;
- `src/core/resourceGaps.js`;
- `src/domain/resources.js`;
- `src/render/renderCardRuntime.js`;
- `tests/v4/disciplinary-scenarios.test.js`;
- `tests/fixtures/disciplinary-scenarios.fixture.js`.
