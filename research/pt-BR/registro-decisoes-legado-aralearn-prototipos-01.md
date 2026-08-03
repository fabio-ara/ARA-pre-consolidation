# Registro de decisões sobre conceitos legados do AraLearn — protótipos 01

**Data local:** 3 de agosto de 2026  
**Issue:** #36  
**Autoridade:** decisão provisória de pesquisa e arquitetura; não constitui migração automática

## Decisão principal

Os 18 `resources` do AraLearn e seus mecanismos auxiliares não são importados como tipos da ARA. Cada conceito é reclassificado segundo uma destas operações:

- reter conceito;
- dividir responsabilidades;
- substituir implementação;
- fundir primitivas e preservar gramática;
- expandir domínio;
- retirar falsa generalidade.

A matriz integral está em `research/data/aralearn-legacy-concept-decisions-02.csv`.

## Decisões estruturais

### `choice`

Deixa de ser presumido como representação. Torna-se um possível modelo de resposta e validação aplicável a diferentes representações.

### `composite`

Deixa de ser um recurso visual específico. Composição passa para o modelo de atividade multipartes e para a orquestração do card ou da microssequência.

### `gap`

Passa a ser um adapter de resposta localizado num alvo semanticamente permitido. Lacuna não define a representação nem a correção.

### `after`

É substituído por feedback tipado com alvo, conteúdo, autoridade, momento e relação independente com pontuação.

### `code`

É dividido em representação estática, documento editável, runtime, validação, testes e feedback. Nenhuma dessas responsabilidades pode ser reconstituída por um campo único.

### `formula`

É substituído por uma família de matemática semântica. A representação visual pode usar uma biblioteca, mas a autoridade permanece no documento matemático e nos validadores de propriedades.

### `graph`, `tree`, `flow` e `relation_map`

Podem compartilhar primitivas relacionais, porém não são reduzidos a uma gramática universal. Hierarquia, controle de fluxo, relações bipartidas, autômatos, mapas causais e argumentos preservam restrições próprias.

### `plane`

É substituído por uma futura gramática de construção geométrica ou coordenada. O resultado textual não é resposta suficiente para atividades de posicionamento ou transformação.

### `chart`

É dividido em dados, transformação, visualização, ação do estudante e validação. Rótulos não podem ser os únicos alvos interativos.

### `sequence`

É dividido entre ordem genérica, cronologia e procedimento. A presença de uma sequência linear não torna as três atividades equivalentes.

### `annotated_text`

É dividido em documento-fonte, anotações do autor, anotações do estudante, seletores e revisão. O protótipo desta rodada implementa o modelo conceitual da resposta do estudante.

### `system_map`

É retirado como recurso genericamente universal. Arquitetura de sistemas, circuitos, modelos causais e outros domínios podem compartilhar um motor relacional, mas precisam de gramáticas explícitas.

### `reaction`

É preservado somente como semente de uma gramática química mais ampla, capaz de coordenar equação, partículas, observações e transformações.

## Conceitos que sobrevivem

Sobrevivem, após redefinição:

- card como unidade de orquestração;
- microssequência como unidade de progressão;
- conteúdo estruturado e fechado por schema;
- renderer determinístico;
- prática autocontida;
- feedback próximo ao alvo;
- Unicode e metadados linguísticos;
- rejeição de HTML e código arbitrário fornecido pelo curso.

## Conceitos não decididos

Esta rodada não decide:

- bibliotecas finais;
- linguagem do frontend;
- CAS;
- motor de grafos ou geometria;
- runtime de programação;
- formato matemático canônico definitivo;
- política institucional de revisão humana;
- compatibilidade com cursos AraLearn;
- migração de dados.

Essas decisões dependem dos adapters experimentais, das Issues #4, #6, #7 e #8 e das buscas bibliográficas formais por frente.
