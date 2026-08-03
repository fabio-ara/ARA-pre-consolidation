# Contratos de componentes 0.2 e avaliação de adapters externos — rodada 01

**Data local:** 3 de agosto de 2026  
**Issue:** #40  
**Estado:** revisão contratual concluída; avaliação externa concluída no nível de fonte e fronteira; execução dos runtimes externos pendente

## 1. Finalidade

A rodada anterior demonstrou que quatro famílias distintas podem usar um ciclo comum sem transformar uma biblioteca de renderização em autoridade sobre o conteúdo:

```text
load
→ start
→ importResponse
→ exportResponse
→ validate
→ produceFeedback
→ dispose
```

Também revelou que o contrato `0.1` era insuficiente para declarar migração, disponibilidade, localização da validação, garantia de isolamento, estado derivado, acessibilidade por operação, custo do pacote e tratamento das evidências de validação.

Esta rodada produz o contrato `0.2`, testa a migração dos quatro protótipos e avalia três candidatos externos atrás da mesma fronteira canônica. A avaliação externa não constitui seleção de stack.

## 2. Resultado contratual

Foram publicados seis schemas fechados:

1. definições comuns;
2. manifest de componente;
3. matemática semântica;
4. construção relacional;
5. programação executável;
6. anotação de fontes e argumentação.

O envelope comum continua separando:

```text
representation
activity
response
validity
criterion outcomes
feedback
validation location
runtime
security
accessibility
offline
provenance
```

As gramáticas de domínio permanecem próprias. O contrato não tenta expressar matemática, grafos, programas e argumentos por uma estrutura universal única.

## 3. Decisões sobre as dez alterações

Todas as dez alterações receberam decisão rastreável. Nove foram aceitas diretamente e uma foi aceita com reformulação.

### 3.1 Versão de adapter e canonicalização

Cada resposta registra:

```json
{
  "adapterVersion": "0.2.0",
  "canonicalizationVersion": "0.2.0"
}
```

A versão do componente não basta para definir como um estado de interface foi reduzido ao documento canônico. A canonicalização pode mudar sem que o renderer ou o componente mudem na mesma cadência.

### 3.2 Garantia de isolamento e elegibilidade produtiva

`runtimeRequirements` passa a distinguir:

- o tipo funcional de runtime;
- a garantia de isolamento declarada;
- a elegibilidade produtiva;
- a versão reproduzível;
- limites independentes.

Um Worker ou `vm` migrado recebe `isolationAssurance: cooperative` e `productionEligibility: rejected`. O contrato deixa de permitir que a palavra “sandbox” funcione como alegação de segurança.

### 3.3 Localização da validação

A validação pode ocorrer em:

- `client-public`;
- `trusted-host-protected`;
- `human-review`;
- `probabilistic-assistance`.

Localização, autoridade e obrigatoriedade são campos distintos. Um teste executado no cliente pode ser determinístico sem ser protegido. Uma sugestão probabilística pode ocorrer no host sem adquirir autoridade final.

### 3.4 Estado derivado

`derivedStatePolicy` declara:

- se o estado é recomputável;
- por quanto tempo pode ser armazenado;
- quais campos são proibidos no documento canônico.

Entre os campos proibidos nesta rodada estão coordenadas, layout, estado de renderer, handles de Worker e objetos de bibliotecas.

### 3.5 Disponibilidade de capacidade

Uma resposta pode registrar que uma capacidade está:

- disponível;
- indisponível;
- degradada;
- dependente de rede;
- dependente de host.

O resultado `unsupported` exige procedência. A ausência de um validador numa implantação não transforma uma resposta estruturalmente válida em resposta incorreta.

### 3.6 Seletores de fonte

A política registra a ordem de resolução:

```text
offset
→ quote-context
→ manual-review
```

Empates produzem `ambiguous-non-silent`. O adapter não escolhe arbitrariamente uma ocorrência repetida.

### 3.7 Acessibilidade por operação

Os booleanos gerais foram substituídos por registros por operação. Cada operação precisa declarar:

- caminho por teclado;
- alternativa não visual;
- anúncio de estado;
- gestão de foco;
- comportamento de reflow;
- limites conhecidos.

Isso não prova conformidade. Torna o requisito verificável e impede que “keyboard: required” esconda a ausência de um caminho operacional.

### 3.8 Perfil medido de pacote

O manifest pode registrar bytes, inicialização, heap, método, ambiente, data e limitações. Um valor não medido é permitido, mas deve aparecer explicitamente como `not-measured`.

### 3.9 Evidências de validação

A política distingue visibilidade, retenção, redação e tipos protegidos. Testes protegidos, notas de revisão, traces probabilísticos, diagnósticos de segurança e dados pessoais não recebem a mesma política.

### 3.10 Limites de runtime

Tempo, memória, bytes de saída, quantidade de mensagens, cancelamento, rede e sistema de arquivos passam a ser campos independentes.

## 4. Migração de 0.1 para 0.2

O migrador cobre as quatro famílias da rodada anterior. Foram versionados:

- quatro documentos `0.1`;
- quatro resultados esperados `0.2`;
- migrador executável;
- testes determinísticos de equivalência documental.

A migração:

- preserva representação, atividade e resposta;
- adiciona metadados de canonicalização;
- converte acessibilidade para requisitos por operação;
- adiciona política de estado derivado;
- adiciona localização da validação;
- remove testes protegidos embutidos no documento de programação;
- substitui-os por uma referência de host;
- marca o runtime de referência como não produtivo;
- adiciona política explícita de seletores.

A migração não é uma migração geral de cursos do AraLearn. Ela cobre apenas os quatro protótipos `0.1`.

## 5. Avaliação externa: método

Foram usados:

1. repositórios oficiais em commits fixados;
2. `package.json`, tipos, documentação de API e fixtures oficiais;
3. adapters de fronteira produzidos pelo projeto;
4. testes de substituição com estados que reproduzem as estruturas documentadas;
5. verificação de que campos externos não entram no JSON canônico.

As bibliotecas não foram baixadas nem executadas no navegador desta rodada. O ambiente não conseguiu resolver os hosts externos e o mirror de pacotes não forneceu os candidatos. Isso é registrado como limitação do ambiente, não como defeito das bibliotecas.

## 6. MathLive e intercâmbio matemático

O commit auditado declara MathLive `0.110.0`, licença MIT e um web component para entrada matemática. A superfície examinada inclui o pacote, a documentação de API e o elemento público de mathfield.

O adapter de fronteira demonstra:

```text
estado do mathfield
→ entrada original
→ MathJSON orientado
→ AST matemático canônico da ARA
```

Seleção, teclado virtual, menus e referências ao DOM são descartados.

A direção inversa também foi testada para o subconjunto de números, símbolos, adição, multiplicação, divisão e potência.

**Resultado:** candidato compatível no nível de fronteira.

**Limite:** o widget produz entrada e representação. Ele não é autoridade para equivalência, demonstração ou correção.

**Pendente:** bundle real, teclado móvel, fala matemática, leitor de tela, conversão completa e integração com motor simbólico.

## 7. Cytoscape.js

O commit auditado contém pacote `3.35.0-unstable`; a versão estável publicada observada foi `3.34.0`. O snapshot foi útil para auditar tipos, modelo de elementos, operação sem renderer e artefato ESM, mas não deve ser a versão de uma futura execução comparativa.

O adapter converte:

```text
Cytoscape elements
→ nodes e edges canônicos
```

São descartados:

- `position`;
- estilo;
- classes;
- seleção;
- scratch data;
- estado de layout.

A importação pode receber um layout derivado sem gravá-lo na resposta.

**Resultado:** candidato compatível no nível de fronteira.

**Limite:** um motor de grafos não define a gramática de autômatos, argumentos, circuitos, árvores de prova ou mapas causais.

**Pendente:** pin de versão estável, bundle, inicialização, teclado, alternativa linear, grafos densos e adapters de gramática disciplinar.

## 8. Recogito Text Annotator

O monorepo auditado declara versão `4.2.5` e licença BSD-3-Clause. A leitura incluiu o modelo W3C, o adapter de formato e fixtures oficiais.

O adapter converte:

- `TextQuoteSelector`;
- `TextPositionSelector`;
- corpos de comentário;
- corpos de tag;

para a anotação canônica da ARA. Ranges DOM, geometrias de highlight, stores e estado do editor são descartados.

A conversão inversa também foi testada.

**Resultado:** candidato compatível no nível de fronteira.

**Limite:** capturar uma anotação não avalia a pertinência da evidência nem a qualidade do argumento.

**Pendente:** execução real, seleção por teclado e leitor de tela, citações sobrepostas, re-resolução, conflitos e fluxos de revisão.

## 9. Validação

A rodada registrou:

- 15 validações JSON Schema;
- 6 testes de migração e invariantes contratuais;
- 4 testes de adapters de fronteira;
- zero falhas.

Os testes confirmaram:

- metadados de versão;
- retirada de testes protegidos do curso;
- estado visual não canônico;
- ambiguidade não silenciosa;
- autoridade separada de localização;
- substituição de adapter sem mudança do documento do curso;
- conversão de MathJSON orientado;
- remoção da geometria do Cytoscape;
- conversão de seletores W3C do Recogito.

Não foram executados testes de runtime das três bibliotecas.

## 10. Conclusões

O contrato `0.2` é mais preciso que `0.1` e preserva a separação entre gramática de domínio e infraestrutura.

Os três candidatos permanecem:

```text
source-compatible
boundary-tested
runtime-not-yet-tested
not-selected
```

A Issue #40 não deve ser encerrada nesta rodada. Ainda faltam build real, execução no navegador, medições, offline, walkthrough manual de acessibilidade e avaliação de custo de saída.

## 11. Próximo trabalho

A próxima unidade deve executar os candidatos em ambiente com resolução de pacotes, usando versões estáveis fixadas e o mesmo documento canônico. A comparação deve medir:

- bytes instalados e transferidos;
- inicialização;
- memória;
- requisições;
- funcionamento offline;
- navegação por teclado;
- árvore de acessibilidade;
- reflow;
- campos externos descartados;
- esforço de adapter;
- custo de substituição.

O resultado poderá aceitar, rejeitar ou manter candidatos em avaliação. Nenhuma decisão deve ser inferida apenas da compatibilidade de fonte.
