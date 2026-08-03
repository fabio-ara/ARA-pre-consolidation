# Relatório dos adapters descartáveis — rodada 01

**Data local:** 3 de agosto de 2026  
**Issue:** #38  
**Estado:** rodada executável de referência concluída; não constitui seleção de stack nem implementação produtiva

## 1. Finalidade

A rodada de schemas anterior propôs um envelope comum para matemática semântica, construção relacional, programação executável e anotação de fontes. Esta rodada tentou falsificar essa proposta com quatro adapters funcionais e substituíveis.

Cada adapter precisava:

1. carregar uma instância canônica;
2. iniciar a atividade;
3. importar e exportar respostas;
4. separar validade de correção ou revisão;
5. produzir feedback;
6. descartar estado visual ou de runtime;
7. preservar o JSON da ARA sem campos próprios de bibliotecas.

## 2. Método

Foi criado um pacote sem dependências JavaScript externas, executado com Node.js 22.16.0, Python 3.13.5, Playwright e Chromium 144.0.7559.96. A ausência de bibliotecas externas foi deliberada: primeiro se testou o contrato; MathLive, Cytoscape.js, Pyodide, Papyros e Recogito permanecem candidatos para uma rodada comparativa posterior.

O lifecycle comum implementado foi:

```text
load(instance)
start()
importResponse(response)
exportResponse()
validate(options)
produceFeedback(validation)
dispose()
```

`exportResponse()` funciona como fronteira canônica. Coordenadas, layouts, workers, estado transitório, testes protegidos e objetos específicos do renderer ficam fora da resposta.

## 3. Matemática semântica

O adapter de referência interpreta uma gramática mínima de números, símbolos, adição, multiplicação, divisão, potência e parênteses. Foram demonstrados três estados:

- `2*(x+` — entrada inválida;
- `2*x+6` — válida e equivalente, mas fora da forma fatorada solicitada;
- `2*(x+3)` — válida, equivalente e na forma solicitada.

Isso confirma a separação entre interpretação, validade, equivalência e forma requerida.

A equivalência foi testada por amostragem em pontos determinísticos. Esse procedimento serve apenas para testar o lifecycle e **não constitui prova matemática geral**. O validador foi rejeitado para produção; uma implementação real exigirá um motor simbólico governado e um escopo formal de expressões.

## 4. Construção relacional

O adapter persiste nós, arestas, restrições e histórico de operações. O layout circular fica em `derivedState`; a resposta exportada não contém `x`, `y`, `position`, `layout` ou `rendererState`.

O cenário exigiu exatamente as arestas A–B e B–D. A validação verificou IDs, endpoints, operações permitidas, caminho A–D em no máximo duas arestas e igualdade do conjunto de arestas.

Toda operação possui caminho sem arrastar, por seletores e botões. Uma lista linear de arestas oferece alternativa ao SVG. O princípio de estado semântico independente do renderer foi confirmado. Grafos densos e gramáticas como autômatos, circuitos e argumentos ainda exigem avaliação própria.

## 5. Programação executável

Foram usados dois runtimes de referência:

- Node Worker com `vm`, para testes locais e testes protegidos injetados pelo host;
- Web Worker, para testes públicos no navegador.

O fluxo diferencia erro de parsing, falha de teste, satisfação parcial, sucesso, timeout e interrupção. Os testes protegidos não aparecem no curso servido nem na resposta exportada.

O runtime foi, contudo, **rejeitado para produção**. Web Worker não é sandbox de segurança, e Node `vm` não é fronteira adequada contra código hostil. Remover APIs de rede não impede todas as formas de escape, o navegador não oferece limite rígido de memória por Worker e testes secretos não podem permanecer protegidos num pacote estático entregue ao cliente.

A expressão contratual `sandboxed-worker` mostrou-se vaga. O contrato precisa registrar nível de garantia, localização da validação, limites independentes e elegibilidade produtiva.

## 6. Anotação de fonte e argumento

O adapter usa fonte versionada por SHA-256, seletor por citação, offsets, prefixo e sufixo, anotação do estudante, nós argumentativos e relações `supports` e `uses-evidence`.

Os offsets foram alterados deliberadamente. O trecho foi reencontrado pela combinação de citação e contexto, mantendo a integridade da resposta. Digest, seletor e links são verificados deterministicamente; relevância da evidência e qualidade da justificativa permanecem sob revisão humana.

A separação entre integridade documental e avaliação interpretativa foi confirmada. Permanecem abertos o tratamento de citações repetidas, a política de versões imutáveis e a avaliação da seleção de intervalos com tecnologias assistivas.

## 7. Validação executada

### Testes Node

Foram executados seis testes:

1. estados matemáticos inválido, parcial e correto;
2. round-trip relacional sem geometria;
3. proteção dos testes de programação;
4. parsing, falha e timeout de programação;
5. re-resolução de seletor e revisão humana;
6. round-trip canônico explícito nas quatro famílias.

Resultado: **6 de 6 aprovados**.

### Walkthrough em Chromium

Foram executadas quinze verificações sobre estados matemáticos, construção relacional, ausência de geometria, alternativa linear, testes públicos, ausência de testes protegidos, timeout, revisão humana, re-resolução, foco, regiões de status e reflow a 320 CSS pixels.

Resultado: **15 de 15 aprovadas**.

Isso não constitui conformidade de acessibilidade. Não houve estudo com usuários nem avaliação completa com tecnologias assistivas.

## 8. Medições

A demonstração independente gerada possui 46.023 bytes e não realizou solicitações externas. Na execução registrada:

- inicialização aproximada: 163,55 ms;
- heap JavaScript usado após o walkthrough: 3,27 MB;
- heap total reportado: 5,85 MB.

Os adapters individuais possuem entre 4,3 KB e 9,2 KB de código-fonte. Esses números descrevem implementações sem runtimes externos e não predizem o custo de CAS, Pyodide, MathLive, Cytoscape.js ou editores especializados. Deltas de heap medidos em loops Node são ruidosos e não representam picos de memória.

## 9. Acessibilidade e segurança

O protótipo confirmou controles por teclado, foco visível, ordem de foco, regiões `aria-live`, alternativa linear ao grafo, ausência de arrasto obrigatório e reflow sem overflow horizontal a 320 CSS pixels.

Permanecem abertas a leitura semântica de matemática, grafos densos, navegação em editores de código, anúncio de traces e seleção de texto por leitor de tela.

Foram preservados como invariantes:

- curso não fornece código de componente;
- saída do estudante é inserida como texto;
- geometria não é canônica;
- testes protegidos não são exportados;
- timeout e limite de saída têm estados explícitos;
- fonte e seletor têm verificação de integridade.

Worker e `vm` não foram aceitos como sandbox produtiva. Uma arquitetura real deverá definir isolamento, rede, sistema de arquivos, CPU, memória, saída, pacotes, testes protegidos, reprodução do runtime e resposta a abuso.

## 10. Alterações contratuais propostas

A implementação revelou dez alterações candidatas para `0.2`:

1. `adapterVersion` e `canonicalizationVersion`;
2. `isolationAssurance` e `productionEligibility`;
3. localização da validação: cliente público, host protegido ou revisão humana;
4. política explícita para `derivedState`;
5. capacidade indisponível com proveniência;
6. política de re-resolução e ambiguidade de seletores;
7. alternativas de acessibilidade por operação;
8. perfil medido de pacote, inicialização e memória;
9. visibilidade e retenção das evidências de validação;
10. limites separados de tempo, memória, saída e cancelamento.

Essas alterações permanecem propostas até revisão dos contratos e comparação com adapters de bibliotecas externas.

## 11. Conclusão

A interface comum mostrou-se viável sem substituir as gramáticas específicas dos domínios. A rodada também produziu duas rejeições explícitas:

- equivalência matemática por amostragem não serve como validador produtivo geral;
- Worker e `vm` não servem como sandbox produtiva para código hostil.

O próximo trabalho é revisar o contrato para `0.2`, executar um bake-off de bibliotecas atrás da mesma fronteira e especificar separadamente a arquitetura de código não confiável e testes protegidos. Somente depois essas fronteiras devem alimentar a taxonomia pedagógica, a instrumentação e o modelo de domínio.
