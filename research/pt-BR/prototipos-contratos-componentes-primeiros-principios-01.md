# Protótipos de contratos de componentes por primeiros princípios — rodada 01

**Data local:** 3 de agosto de 2026  
**Issue:** #36  
**Estado:** prototipagem contratual concluída; nenhuma stack de produção selecionada

## 1. Finalidade

Esta rodada testa uma hipótese derivada do benchmark transdomínio: a ARA pode possuir um envelope comum de componentes sem reduzir matemática, grafos, programação e argumentação à mesma gramática.

Os protótipos não ampliam o catálogo de `resources` do AraLearn. Eles substituem a pergunta “qual novo tipo visual deve ser criado?” por um conjunto de perguntas independentes:

1. qual estrutura de conhecimento precisa ser representada;
2. qual atividade o estudante executa;
3. qual documento de resposta ele produz;
4. o que torna a resposta válida;
5. quais propriedades podem ser avaliadas;
6. qual autoridade pode concluir a avaliação;
7. qual feedback será produzido;
8. qual runtime é necessário;
9. quais requisitos de acessibilidade, segurança e offline condicionam a capacidade.

## 2. Envelope comum

O manifesto `ara.component-manifest` possui versão `0.1.0` e declara:

- identidade e família do componente;
- schemas de representação, atividade, resposta, validação e feedback;
- formas de resposta e autoridades de validação;
- requisitos de runtime;
- fronteira de segurança;
- contrato de acessibilidade;
- perfil offline;
- localização;
- proveniência.

O curso não transporta código de componente. Ele referencia uma capacidade instalada e aprovada, por exemplo:

```json
{
  "componentRef": "org.ara.prototype.semantic-expression@0.1.0"
}
```

Essa regra preserva portabilidade do conteúdo sem transformar o JSON do curso em mecanismo de instalação ou execução arbitrária.

## 3. Ciclo de resposta

Os resultados de validação distinguem os seguintes estados:

```text
empty
invalid
valid-unassessed
unsupported
incorrect
partially-satisfied
correct
review-required
runtime-error
```

A validade possui estado próprio:

```text
empty
invalid-syntax
invalid-structure
invalid-reference
valid
```

Assim, uma entrada pode ser sintaticamente inválida antes de ser matematicamente incorreta; um programa pode compilar e falhar em testes; uma anotação pode resolver corretamente a fonte e ainda exigir revisão humana da argumentação.

## 4. Matemática semântica

### 4.1 Representação

A expressão é armazenada como árvore semântica, com leitura acessível. O texto digitado pelo estudante é preservado como registro de autoria, mas não é a autoridade matemática.

### 4.2 Atividade e resposta

O protótipo admite operações como interpretar, construir equivalente, simplificar, fatorar, resolver e diferenciar. A resposta contém:

- input original;
- formato de entrada;
- expressão interpretada;
- unidades, quando aplicável.

### 4.3 Validade e correção

A fase de validade verifica parsing, símbolos, domínio e unidades. Somente depois são aplicados testes de propriedades:

- equivalência;
- forma requerida;
- tolerância numérica;
- equivalência de unidades;
- domínio.

Uma prévia de interpretação é obrigatória quando a notação digitada pode ser ambígua. Esse princípio deriva do precedente do STACK, mas o contrato não seleciona STACK, Maxima ou outro CAS.

### 4.4 Microsequência

O exemplo contém:

1. fundamento sobre fatoração como transformação equivalente;
2. prática guiada com uma parte do fator fornecida;
3. prática independente com nova expressão.

A retirada de apoio altera a ajuda, não os dados necessários.

## 5. Construção relacional

### 5.1 Estado semântico

O protótipo usa nós, arestas e restrições. Coordenadas não são persistidas como conteúdo canônico:

```json
{
  "persistCoordinates": false,
  "layoutAuthority": "renderer-derived"
}
```

A mesma resposta pode ser apresentada por layout visual, lista linear, tabela de adjacência ou interface não visual.

### 5.2 Atividade e resposta

A atividade declara operações permitidas: adicionar ou remover nó ou aresta, editar rótulo e selecionar elementos. A resposta conserva:

- estado semântico final;
- log opcional de operações.

O log permite estudar estratégia ou oferecer desfazer, mas o resultado pode ser validado pelo estado final quando o percurso não faz parte do objetivo.

### 5.3 Validação

JSON Schema valida a forma geral; o runtime verifica unicidade de IDs, existência de extremos, gramática e operações permitidas. Predicados educativos podem testar:

- existência de caminho;
- conjunto de arestas;
- conectividade;
- ausência de ciclos;
- condição de grau;
- aceitação por autômato.

O motor relacional pode ser compartilhado. As gramáticas de grafo, autômato, mapa causal e argumento permanecem distintas.

## 6. Programação executável

### 6.1 Separação de camadas

O protótipo divide:

- workspace de código;
- editor;
- documento submetido;
- solicitação de execução;
- runtime;
- pipeline de validade;
- suites de testes;
- diagnóstico;
- feedback.

Código estático e código executável deixam de ser o mesmo conceito.

### 6.2 Validade antes dos testes

O pipeline verifica decodificação, parsing, compilação, política de imports e limites de recursos. Testes funcionais não rodam quando a resposta é inválida.

### 6.3 Runtime e segurança

O protótipo exige worker isolado, sem rede por padrão, sistema de arquivos efêmero, limite de tempo, limite de memória e versão reproduzível. Testes protegidos não integram o JSON distribuído do curso.

Resultados possíveis incluem erro de sintaxe, falha de teste, execução excedida e correção. Diagnósticos de estilo são explicitamente não finais.

### 6.4 Offline

A capacidade é `package-required`: pode funcionar localmente depois que editor, runtime WebAssembly e test runner forem instalados, mas o custo de pacote e memória precisa ser medido em dispositivos modestos.

## 7. Anotação de fontes e argumento

### 7.1 Fonte estável

Cada fonte possui conteúdo, idioma e digest. A anotação conserva citação, offsets, prefixo, sufixo e digest da versão. Isso permite detectar quando o trecho deixou de corresponder ao documento.

### 7.2 Resposta

O estudante produz:

- anotações;
- propósito da anotação;
- comentário;
- nós de argumento;
- relações de suporte, desafio, qualificação, uso de evidência e conclusão.

O legado `annotated_text` exibia anotações do autor. O novo modelo representa anotações produzidas pelo estudante.

### 7.3 Autoridade

Integridade da fonte, seletores e links pode ser validada deterministicamente. Relevância, qualidade da justificativa e força do argumento permanecem sob revisão humana nesta rodada.

Assistência probabilística pode sugerir problemas locais, mas:

```text
probabilistic assistance ≠ final authority
```

Esse limite impede que uma avaliação linguística ou argumentativa incerta seja apresentada como resultado objetivo.

## 8. Feedback e pontuação

O contrato de feedback declara:

- alvo;
- tipo;
- conteúdo;
- autoridade;
- momento de revelação.

Pontuação é opcional e separada. Uma atividade formativa pode produzir critérios e feedback sem gerar nota. Crédito parcial decorre de critérios explícitos, não de uma mensagem genérica após a tentativa.

## 9. Acessibilidade

Todos os manifests exigem teclado, ordem de foco e leitor de tela. Construções bidimensionais podem usar exceção de reflow somente quando oferecem representação linear equivalente.

O contrato exige alternativa sem arrastar. Isso não significa que qualquer interação construtiva já seja acessível; significa que um componente não poderá declarar conformidade sem demonstrar os caminhos equivalentes.

Programação requer navegação por diagnósticos e saída. Matemática requer interpretação legível. Anotações exigem seleção de intervalo por teclado. Grafos precisam de edição linear de nós e arestas.

## 10. Segurança

A fronteira comum fixa:

```text
courseSuppliedCode: forbidden
```

Componentes externos só podem existir como adapters instalados e aprovados. Código do estudante, quando permitido, roda em sandbox. Rede, arquivos, memória, tempo e retenção são declarados por componente.

Um manifesto não torna um componente seguro: ele torna as exigências auditáveis.

## 11. Funcionamento offline

Os quatro perfis mostram que “offline” não é binário:

- construção relacional e anotação: `full`;
- matemática semântica: `package-required`;
- programação: `package-required`, com custo maior.

Um curso pode permanecer portátil mesmo quando uma implantação não possui determinado runtime. Nesse caso, a plataforma deve declarar a capacidade ausente, não degradar silenciosamente a atividade para múltipla escolha.

## 12. Validação executada

Foram validados com JSON Schema Draft 2020-12:

- 4 manifests;
- 4 instâncias completas;
- 4 microssequências;
- 7 resultados de validação.

Total: 19 documentos, sem erros estruturais.

Os cenários incluem:

- sintaxe matemática inválida;
- expressão correta;
- construção parcialmente satisfatória;
- sintaxe de programa inválida;
- erro de runtime;
- seletor de fonte inválido;
- argumento que exige revisão humana.

Ainda dependem de runtime:

- unicidade e referências cruzadas;
- equivalência matemática;
- predicados relacionais;
- execução e testes;
- resolução de seletores;
- rubricas humanas.

## 13. Resultado do teste transdomínio

O envelope comum funcionou para os quatro casos somente porque permaneceu estreito. As partes compartilháveis são:

- identidade e versão;
- proveniência;
- ciclo de resposta;
- critérios e autoridade;
- feedback;
- runtime;
- segurança;
- acessibilidade;
- offline;
- localização.

Não devem ser unificadas:

- AST e predicados matemáticos;
- estado e predicados relacionais;
- workspace, runtime e testes de programação;
- seletores, anotações, relações argumentativas e rubrica.

A conclusão não é criar um `resource` universal. É criar um protocolo comum para componentes que hospedam gramáticas específicas.

## 14. Próximas decisões

A rodada ainda não seleciona bibliotecas. O próximo movimento técnico deverá produzir adapters descartáveis para um cenário mínimo de cada família e comparar:

- tamanho;
- inicialização;
- qualidade de entrada;
- acessibilidade real;
- serialização;
- isolamento;
- cobertura offline;
- licenciamento;
- esforço de manutenção.

Antes disso, os resultados desta rodada devem informar:

1. a taxonomia de configurações pedagógicas da Issue #4;
2. o modelo de domínio da Issue #6;
3. a arquitetura técnica da Issue #7;
4. o modelo de eventos e analytics da Issue #8.
