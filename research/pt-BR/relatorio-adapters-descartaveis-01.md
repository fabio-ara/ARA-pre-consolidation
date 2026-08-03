# Relatório dos adapters descartáveis — rodada 01

**Data local:** 3 de agosto de 2026  
**Issue:** #38  
**Estado:** rodada de adapters de referência concluída; não constitui seleção de stack nem implementação produtiva

## 1. Finalidade

A rodada anterior demonstrou, em nível de schema, que matemática semântica, construção relacional, programação executável e anotação de fontes podem compartilhar um envelope contratual sem compartilhar a mesma gramática disciplinar.

Esta rodada tentou falsificar essa conclusão por meio de quatro adapters executáveis. O objetivo não foi criar componentes finais, mas verificar se um adapter consegue:

1. receber uma instância canônica;
2. iniciar uma atividade;
3. importar e exportar resposta;
4. separar validade de correção ou revisão;
5. produzir feedback;
6. descartar estado visual ou de runtime;
7. operar sem introduzir campos próprios do renderer no JSON da ARA.

## 2. Método

Foi criado um pacote sem dependências JavaScript externas, executado com:

- Node.js 22.16.0;
- Python 3.13.5 e Playwright;
- Chromium 144.0.7559.96.

A ausência de dependências externas nesta rodada foi deliberada. Ela permitiu testar o contrato antes de testar bibliotecas específicas. MathLive, Cytoscape.js, Pyodide, Papyros e Recogito continuam candidatos de benchmark, não dependências escolhidas.

O pacote contém:

- uma interface comum de lifecycle;
- quatro adapters;
- fixtures canônicas;
- testes Node;
- demonstração independente e offline;
- walkthrough em navegador;
- medições;
- análise de segurança, acessibilidade, licenças e alterações contratuais.

## 3. Lifecycle comum

Os quatro adapters implementam:

```text
load(instance)
start()
importResponse(response)
exportResponse()
validate(options)
produceFeedback(validation)
dispose()
```

O método decisivo é `exportResponse()`. Ele define a fronteira canônica e exclui:

- coordenadas e layout;
- handles de worker;
- estado transitório da interface;
- testes protegidos;
- detalhes internos de interpretação;
- objetos específicos de bibliotecas.

Esse lifecycle funcionou nas quatro famílias. Portanto, o contrato comum não precisa ser uma gramática universal de `resource`.

## 4. Matemática semântica

O adapter implementa uma gramática mínima de expressões com:

- números;
- símbolos;
- adição;
- multiplicação;
- divisão;
- potência;
- parênteses;
- multiplicação implícita em casos simples.

O fluxo testado foi:

```text
entrada textual
→ parsing
→ AST semântica
→ prévia de interpretação
→ símbolos declarados
→ testes de propriedades
→ resultado e feedback
```

Foram observados três estados distintos:

1. `2*(x+` — inválido, pois não pode ser interpretado;
2. `2*x+6` — válido e equivalente, mas não na forma fatorada solicitada;
3. `2*(x+3)` — válido, equivalente e na forma requerida.

Isso confirma que validade, equivalência e forma de resposta são critérios diferentes.

### Limite crítico

A equivalência foi demonstrada por avaliação em pontos determinísticos. Esse método é útil para testar o lifecycle, mas **não é prova matemática geral**. O validador de referência foi, por isso, rejeitado como solução produtiva. Uma implementação real exigirá motor simbólico governado, escopo explícito de expressões e testes contra casos de fronteira.

## 5. Construção relacional

O adapter representa:

- nós;
- arestas;
- restrições semânticas;
- histórico opcional de operações.

O renderer calcula um layout circular, mas esse layout fica em `derivedState`. A resposta exportada não contém `x`, `y`, `layout`, `position` ou `rendererState`.

O cenário exigiu construir exatamente:

```text
A — B — D
```

A validação verificou:

- IDs únicos;
- existência dos endpoints;
- operações permitidas;
- caminho de A até D com no máximo duas arestas;
- igualdade exata do conjunto de arestas.

A interface utiliza seletores e botões. O estudante não precisa arrastar elementos. Também existe uma lista linear de arestas como alternativa ao SVG.

### Resultado

O princípio de estado semântico independente do renderer foi confirmado. O adapter permanece um precedente contratual viável, mas não escolhe um motor de grafos. Estruturas densas e gramáticas especializadas — autômatos, argumentos, circuitos ou redes causais — ainda exigem avaliação própria.

## 6. Programação executável

Foram implementados dois ambientes de referência:

- Node worker com `vm` para testes locais e suíte protegida injetada pelo host;
- Web Worker em navegador para testes públicos.

O cenário usa JavaScript, permitido pelo schema da família, e distingue:

- erro de parsing;
- falha de teste;
- satisfação parcial;
- sucesso;
- timeout;
- interrupção pelo estudante.

Os testes protegidos residem fora da resposta e fora do conteúdo servido ao navegador. O JSON exportado contém somente o código submetido e o pedido de execução.

### Resultado de segurança

O lifecycle e a separação dos testes foram demonstrados, mas o runtime foi **rejeitado para produção**.

Razões:

- Web Worker isola execução da interface, mas não é sandbox de segurança;
- Node `vm` não deve ser tratado como fronteira contra código hostil;
- remover APIs como `fetch` não impede todas as formas de escape;
- o navegador não oferece limite rígido de memória por Worker;
- testes realmente protegidos não podem ser secretos num pacote estático entregue ao cliente.

A nomenclatura `sandboxed-worker` mostrou-se excessivamente vaga. O contrato precisa registrar nível de garantia, localização da validação e elegibilidade produtiva.

## 7. Anotação de fonte e argumento

O adapter usa:

- fonte versionada por SHA-256;
- seletor com citação, offsets, prefixo e sufixo;
- anotação do estudante;
- reivindicação e razão;
- links `supports` e `uses-evidence`.

O cenário alterou deliberadamente os offsets da anotação. O trecho foi reencontrado pelo par citação–contexto e a resposta permaneceu válida.

A validação determinística verificou:

- digest da fonte;
- resolução do seletor;
- existência dos links;
- ligação entre evidência e razão.

A relevância da evidência e a qualidade da justificativa permaneceram em `review-required`, sob autoridade humana.

### Resultado

A separação entre integridade documental e qualidade argumentativa foi confirmada. Ainda são necessários:

- política de versões imutáveis da fonte;
- tratamento de citações repetidas e ambíguas;
- avaliação com leitor de tela para seleção de intervalos;
- fluxo institucional de revisão e devolução.

## 8. Validação executada

### Testes Node

Foram executados cinco testes:

1. matemática inválida, parcial e correta;
2. round-trip relacional sem geometria;
3. proteção dos testes de programação;
4. parsing, falha e timeout de programação;
5. re-resolução de seletor e revisão humana.

Resultado: **5 de 5 aprovados**.

### Walkthrough em Chromium

Foram executadas quinze verificações:

- três estados matemáticos;
- construção relacional correta;
- ausência de geometria no JSON;
- visualização linear de arestas;
- falha e sucesso em teste público;
- ausência de teste protegido na resposta;
- timeout;
- handoff para revisão humana;
- re-resolução de seletor;
- ordem de foco;
- regiões de status;
- reflow a 320 CSS pixels.

Resultado: **15 de 15 aprovadas**.

Esses resultados não constituem conformidade de acessibilidade. Não houve estudo com usuários nem avaliação completa em tecnologias assistivas.

## 9. Medições

A demonstração independente possui 46.023 bytes e não fez solicitações externas. Na execução observada:

- inicialização: aproximadamente 163,55 ms;
- heap JavaScript usado após o walkthrough: aproximadamente 3,27 MB;
- heap total reportado: aproximadamente 5,85 MB.

Os adapters possuem entre 4,3 KB e 9,2 KB de código-fonte individual. Essas medidas descrevem somente as implementações de referência sem dependências externas. Não predizem o custo de um CAS, Pyodide, MathLive, Cytoscape.js ou editor especializado.

Os deltas de heap medidos em loops Node são ruidosos e não devem ser tratados como picos de memória.

## 10. Acessibilidade

Foram confirmados no protótipo:

- controles alcançáveis por teclado;
- foco visível;
- ordem de foco estável;
- regiões `aria-live`;
- alternativa linear ao grafo;
- ausência de interação obrigatória por arrastar;
- reflow sem overflow horizontal a 320 CSS pixels.

Permanecem abertos:

- leitura de expressões matemáticas e prévia ambígua;
- grafos densos;
- navegação eficiente em editor de código;
- anúncio de traces e diagnósticos;
- seleção de intervalos de texto por leitor de tela;
- avaliação com usuários com deficiência.

## 11. Segurança

Foram aceitos como invariantes:

- curso não fornece código de componente;
- saída do estudante é inserida como texto;
- geometria não é canônica;
- testes protegidos não são exportados;
- timeout e limite de saída produzem estados explícitos;
- fonte e seletor possuem verificação de integridade.

Foi rejeitada a hipótese de que `Worker` ou `vm` seja, por si só, sandbox suficiente. Uma arquitetura produtiva de programação precisará definir, conforme o perfil:

- isolamento em processo, origem ou serviço dedicado;
- política de rede;
- sistema de arquivos;
- limites de CPU, memória e saída;
- pacotes permitidos;
- localização de testes protegidos;
- reprodutibilidade do runtime;
- resposta a abuso.

## 12. Licenças e bibliotecas

Nenhuma biblioteca de runtime externa foi incorporada. O código do protótipo é AGPL-3.0-or-later.

Os seguintes candidatos permanecem referenciados para uma rodada posterior:

- MathLive/MathJSON — MIT;
- Cytoscape.js — MIT;
- Pyodide — MPL-2.0;
- Papyros — MIT;
- Recogito Text Annotator — BSD-3-Clause.

A próxima comparação deverá medir versão, bundle, acessibilidade, contratos, dependências transitivas e substituibilidade. A ausência de dependências nesta rodada não é recomendação para reconstruir todas as capacidades internamente.

## 13. Alterações contratuais propostas

A implementação revelou dez alterações candidatas para uma versão `0.2`:

1. `adapterVersion` e `canonicalizationVersion` na resposta;
2. `isolationAssurance` e `productionEligibility` no runtime;
3. localização da validação: cliente público, host protegido ou revisão humana;
4. política explícita para `derivedState`;
5. estado de capacidade indisponível com proveniência;
6. política de re-resolução e ambiguidade de seletores;
7. alternativas de acessibilidade descritas por operação;
8. perfil medido de pacote, inicialização e memória;
9. visibilidade e retenção das evidências de validação;
10. limites separados de tempo, memória, saída e cancelamento.

Essas alterações ainda são propostas. Devem ser revisadas contra os quatro contratos e, quando possível, contra uma segunda implementação de cada família.

## 14. Conclusão

A rodada confirmou a hipótese principal:

> uma interface comum de componente é viável, desde que não tente substituir as gramáticas específicas dos domínios.

Também produziu duas rejeições importantes:

- a equivalência matemática por amostragem não serve como validador produtivo geral;
- Worker e `vm` não servem como sandbox produtiva de código hostil.

Assim, o protótipo não congela uma stack. Ele melhora o contrato ao mostrar quais fronteiras são reais e quais termos estavam vagos.

## 15. Próximo trabalho

A sequência recomendada é:

1. revisar os contratos para `0.2`;
2. executar um bake-off de bibliotecas atrás do mesmo adapter;
3. especificar a arquitetura de código não confiável e testes protegidos;
4. incorporar as fronteiras confirmadas à taxonomia pedagógica da Issue #4;
5. consolidar depois instrumentação, analytics e modelo de domínio.
