# Briefing para redesenho dos resources a partir de primeiros princípios

**Data local:** 2 de agosto de 2026  
**Issues:** #30, #33 e #34  
**Estado:** requisitos de investigação e prototipagem; nenhuma stack selecionada

## 1. Decisão de partida

Os dezoito `resources` do AraLearn não serão migrados automaticamente. Cada um passa a ser um caso legado que poderá:

- preservar uma ideia;
- ter a implementação substituída;
- ser dividido em gramáticas distintas;
- ser absorvido por uma gramática maior;
- tornar-se apenas uma representação;
- tornar-se apenas um modelo de resposta;
- ser retirado.

O novo modelo não começa por uma lista de widgets. Começa pelas práticas dos domínios, pelos documentos que precisam ser representados e pelas respostas que o estudante deve produzir.

## 2. Unidades fundamentais

### 2.1 `learningDocument`

Documento educacional versionado que preserva curso, módulo, lição, microssequência e card. O card continua sendo unidade de orquestração, não sinônimo de representação.

### 2.2 `representation`

Documento semântico que descreve o objeto apresentado ou manipulado:

- texto;
- expressão;
- tabela ou dataset;
- grafo;
- construção geométrica;
- mapa;
- circuito;
- partitura;
- molécula;
- reação;
- fonte anotável;
- modelo de simulação.

A representação não define automaticamente a tarefa.

### 2.3 `activity`

Declara o que o estudante deve fazer:

- selecionar;
- completar;
- ordenar;
- classificar;
- construir;
- editar;
- conectar;
- executar;
- simular;
- anotar;
- explicar;
- justificar;
- comparar;
- diagnosticar.

### 2.4 `responseDocument`

Registra a produção do estudante em forma própria:

- conjunto de opções;
- texto;
- expressão matemática;
- número e unidade;
- código;
- grafo ou circuito construído;
- coordenadas ou construção geométrica;
- ordenação;
- anotações sobre fonte;
- parâmetros e observações de simulação;
- argumento estruturado;
- arquivo ou artefato externo autorizado.

A resposta não deve ser reconstruída a partir de eventos de interface quando um estado semântico pode ser persistido diretamente.

### 2.5 `validator`

Componente que recebe representação, atividade, resposta e contexto e devolve resultados tipados. Pode ser:

- literal;
- conjunto exato;
- numérico com tolerância;
- equivalência simbólica;
- predicado geométrico;
- predicado de grafo;
- testes de programa;
- simulação determinística;
- regras linguísticas;
- rubrica humana;
- assistência probabilística não autoritativa.

### 2.6 `feedbackPolicy`

Transforma resultados do validador em informação para o estudante. Deve separar:

- verificação;
- diagnóstico;
- explicação;
- pista;
- próximo passo;
- exemplo comparativo;
- visualização do erro;
- encaminhamento para revisão humana.

### 2.7 `runtimeCapability`

Capacidade opcional necessária para execução ou manipulação avançada:

- CAS;
- Python/WebAssembly;
- motor geométrico;
- motor de grafos;
- simulador;
- análise linguística;
- renderização molecular;
- mapas e dados espaciais.

O runtime não deve residir no JSON do curso.

### 2.8 `rendererAdapter`

Transforma representação e estado em interface. Não é autoridade de conteúdo nem de avaliação. Geometria, cor e layout permanecem derivados sempre que possível.

## 3. Ciclo de resposta

O estado de uma resposta precisa ser mais rico que correto/incorreto:

```text
empty
→ syntactically-invalid
→ valid-unassessed
→ assessed
   ├─ unsupported
   ├─ incorrect
   ├─ partially-satisfied
   ├─ correct
   └─ requires-review
```

Cada transição registra:

- componente e versão;
- entrada original;
- interpretação normalizada;
- predicados avaliados;
- resultados;
- feedback entregue;
- autoridade da decisão;
- data e versão da configuração efetiva.

## 4. Contrato de componente

Um componente instalado deverá possuir manifesto semelhante a:

```json
{
  "componentId": "ara.math.expression",
  "version": "1.0.0",
  "representationKinds": ["math-expression"],
  "activityKinds": ["construct", "transform", "compare"],
  "responseKinds": ["math-expression"],
  "validators": ["syntax", "equivalence", "properties"],
  "renderers": ["web"],
  "runtimeRequirements": ["ara.runtime.symbolic-math"],
  "accessibility": {
    "keyboard": "required",
    "screenReader": "required",
    "alternativeRepresentation": "required"
  },
  "offline": {
    "grade": "local-after-package-download"
  },
  "security": {
    "courseSuppliedCode": false,
    "network": "none"
  }
}
```

Esse exemplo é conceitual. O schema definitivo depende do modelo de domínio e da arquitetura.

## 5. Registro e confiança

### 5.1 Componentes internos

Mantidos no repositório ARA, revisados e publicados com a plataforma.

### 5.2 Adapters aprovados

Integram bibliotecas externas, mas possuem wrapper, testes e versão controlados pela ARA.

### 5.3 Componentes institucionais

Podem ser instalados por uma implantação após revisão local. Não se tornam parte automática do catálogo público.

### 5.4 Código de curso

O curso não fornece JavaScript, Python de infraestrutura, HTML livre, iframe ou pacote executável. Ele referencia componentes disponíveis e fornece apenas dados aceitos pelos schemas.

### 5.5 Código produzido pelo estudante

É conteúdo de resposta e só executa num sandbox explicitamente autorizado, com recursos e rede limitados.

## 6. Gramáticas candidatas para protótipos

### 6.1 Matemática semântica

**Representação:** MathJSON ou AST equivalente.  
**Resposta:** expressão construída por teclado acessível.  
**Validação:** sintaxe, equivalência e propriedades.  
**Precedentes:** STACK, Numbas e MathLive.

Prova mínima:

- mostrar interpretação antes de corrigir;
- distinguir equivalência de forma exigida;
- aceitar unidades e tolerâncias quando aplicável;
- produzir feedback por propriedade.

### 6.2 Geometria e gráficos

**Representação:** objetos, restrições e relações.  
**Resposta:** construção ou manipulação.  
**Validação:** predicados geométricos.  
**Precedentes:** JSXGraph e Perseus Interactive Graph.

Prova mínima:

- criar e mover ponto por teclado e toque;
- persistir coordenadas/relações, não pixels;
- validar propriedade independente do layout.

### 6.3 Grafos, autômatos e redes

**Representação:** nós, arestas e semântica de domínio.  
**Resposta:** seleção, edição ou construção.  
**Validação:** conectividade, caminho, linguagem aceita, causalidade ou outra propriedade.  
**Precedente:** Cytoscape.js.

Prova mínima:

- separar motor de grafo de gramática de autômato/circuito;
- oferecer alternativa acessível à manipulação visual;
- registrar estado final e operações relevantes.

### 6.4 Programação executável

**Representação:** documento de código, entradas e ambiente.  
**Resposta:** código editado.  
**Validação:** parsing, execução, testes e análise estática.  
**Precedentes:** Pyodide, Papyros, OpenDSA e Blockly.

Prova mínima:

- worker isolado;
- limite de tempo/memória;
- stdout/stderr controlados;
- testes públicos e protegidos;
- feedback distinto para sintaxe, execução e lógica.

### 6.5 Anotação, fonte e argumento

**Representação:** documento com seletores estáveis.  
**Resposta:** anotações, tags, relações e justificativas.  
**Validação:** presença de evidência, correspondência a rubrica ou revisão.  
**Precedente:** Recogito Text Annotator.

Prova mínima:

- selecionar trechos por teclado;
- persistir citação e offsets;
- suportar múltiplas evidências;
- distinguir avaliação humana de assistência automática.

### 6.6 Dados espaciais e mapas

**Representação:** camadas, geometrias, propriedades e proveniência.  
**Resposta:** seleção espacial, marcação, rota ou comparação.  
**Validação:** predicados espaciais.  
**Precedente:** Leaflet.

Prova mínima:

- mapa com alternativa textual/tabular;
- pacote offline ou ausência explicitada;
- atribuição e origem dos dados;
- resposta sem dependência de pixel.

### 6.7 Química e estruturas moleculares

**Representação:** equação, molécula, estrutura e níveis representacionais.  
**Resposta:** coeficientes, relações ou manipulação de modelo.  
**Validação:** conservação, correspondência e predicados químicos explicitamente suportados.  
**Precedentes:** PhET e Mol*.

Prova mínima:

- coordenar simbólico e submicroscópico;
- não prometer inferência química além do validador;
- registrar estado e seleção sem depender de screenshot.

### 6.8 Música

**Representação:** MusicXML ou gramática equivalente.  
**Resposta:** identificação, edição ou produção de nota/ritmo.  
**Validação:** propriedades musicais.  
**Precedente:** OpenSheetMusicDisplay.

Prova mínima:

- renderizar partitura e alternativa Braille/textual;
- produzir resposta sem áudio obrigatório;
- separar playback opcional do conteúdo canônico.

### 6.9 Línguas e produção textual

**Representação:** texto, unidades linguísticas e metadados de idioma.  
**Resposta:** produção, anotação ou transformação.  
**Validação:** regras objetivas, rubrica ou revisão.  
**Precedentes:** LanguageTool e Recogito.

Prova mínima:

- preservar pt-BR, pt-PT, RTL e sistemas não latinos;
- apresentar diagnósticos como sugestões locais;
- não converter corretor gramatical em medida de competência.

### 6.10 Circuitos

**Representação:** componentes, portas, fios e estado.  
**Resposta:** circuito construído.  
**Validação:** topologia e comportamento.  
**Precedente:** CircuitVerse.

Prova mínima:

- construção sem depender exclusivamente de drag-and-drop;
- simulação determinística;
- validação por comportamento e, quando necessário, estrutura.

## 7. Migração conceitual dos resources legados

| AraLearn | Hipótese de destino |
|---|---|
| `paragraph` | bloco documental, não atividade |
| `choice` | modelo de resposta selecionada |
| `composite` | composição geral do card |
| `code` | representação de código; execução é capability |
| `table` | representação tabular/dataset com respostas próprias |
| `flow` | dividir gramática de processo, pseudocódigo e atividade de construção |
| `tree` | gramáticas hierárquicas especializadas sobre primitivas relacionais |
| `graph` | motor relacional + gramática de domínio + respostas construtivas |
| `relation_map` | possível atividade de matching/relação, não necessariamente representação isolada |
| `matrix` | estrutura matemática/tabular, com entrada semântica |
| `plane` | substituir por construção geométrica mais geral |
| `formula` | substituir por expressão semântica e input apropriado |
| `chart` | visualização de dataset; separar dados, chart e atividade |
| `sequence` | representação de ordem; ordenar é modelo de resposta |
| `annotated_text` | documento anotável e resposta por annotation |
| `linguistic_example` | uma gramática linguística entre várias |
| `system_map` | dividir limites/arquitetura de um motor genérico e gramáticas específicas |
| `reaction` | parte de família química multirrepresentacional |

Nenhuma linha é decisão final.

## 8. Requisitos de acessibilidade

Cada componente precisa declarar e testar:

- navegação integral por teclado;
- foco visível e não oculto;
- semântica para leitor de tela;
- alternativa à posição visual;
- alternativa ao arrastar;
- reflow e zoom;
- descrição de estruturas complexas;
- contraste e estado não dependente somente de cor;
- redução de movimento;
- internacionalização e direção de texto.

A acessibilidade não pode ser delegada genericamente ao renderer.

## 9. Requisitos offline e móveis

O manifesto deverá classificar:

- tamanho do pacote;
- dados externos necessários;
- cacheabilidade;
- necessidade de worker, WebAssembly ou servidor;
- suporte completo, parcial ou inexistente offline;
- memória e CPU esperadas;
- comportamento quando a capability não está instalada.

Cursos devem poder declarar requisitos e oferecer alternativa quando possível.

## 10. Próxima entrega

A próxima issue deverá produzir schemas conceituais e protótipos descartáveis para quatro trilhas iniciais:

1. matemática semântica;
2. construção relacional/geométrica;
3. programação executável;
4. anotação e argumento baseado em fonte.

Essas quatro cobrem respostas simbólicas, construtivas, executáveis e discursivas. Somente após compará-las será possível definir um núcleo comum sem generalização prematura.
