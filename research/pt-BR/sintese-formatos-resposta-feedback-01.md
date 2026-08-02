# Formatos de resposta e configurações de feedback — síntese focada 01

**Versão:** 0.1  
**Data:** 2 de agosto de 2026  
**Issue:** #17  
**Estado:** síntese focada inicial; deverá ser ampliada pelos resultados formais da Issue #16

## 1. Pergunta de trabalho

Que dimensões precisam ser distinguidas para representar, configurar e investigar formatos de resposta e feedback na Plataforma ARA sem reduzir toda prática a múltipla escolha ou a um card de pergunta e resposta?

A síntese separa quatro problemas frequentemente confundidos:

1. **exigência cognitiva da resposta:** reconhecer, recuperar, produzir, explicar, resolver ou executar;
2. **forma de pontuação:** comparação exata, conjunto de respostas, teste automatizado, rubrica ou avaliação humana;
3. **conteúdo do feedback:** resultado, resposta correta, explicação, pista, exemplo ou orientação para nova tentativa;
4. **momento e ciclo do feedback:** imediato, após o item, após um conjunto, atrasado ou em revisão posterior.

Resultados psicométricos de avaliações, efeitos de prática, satisfação, carga cognitiva e aprendizagem não serão tratados como desfechos equivalentes.

## 2. Fontes centrais e profundidade de acesso

| ID | Fonte | Contribuição | Estado de acesso |
|---|---|---|---|
| RF01 | Eisenkraemer, Jaeger e Stein (2013) | revisão do efeito de testagem por formatos de recordação e reconhecimento | texto integral aberto |
| RF02 | Pan e Rickard (2018) | meta-análise de transferência após prática de recuperação | resumo, metadados e manuscrito autoral localizado |
| RF03 | Breuer, Scherndl e Ortner (2023) | meta-análises de formatos abertos e fechados em avaliação | texto integral aberto |
| RF04 | Sher et al. (2026) | meta-análise de respostas muito curtas e múltipla escolha | texto integral aberto |
| RF05 | van der Kleij, Feskens e Eggen (2015) | meta-análise de conteúdo do feedback em ambientes computacionais | resumo detalhado e metadados verificados |
| RF06 | Kandemir et al. (2026) | meta-análise de feedback imediato versus atrasado | resumo completo, métodos e dados abertos; artigo integral restrito |
| RF07 | Agarwal et al. (2025) | meta-análise de recuperação versus elaboração | resumo detalhado e metadados verificados |
| RF08 | Gao et al. (2023) | revisão de avaliação automática de respostas textuais | manuscrito aberto; revisão de 93 estudos |

A síntese não presume que uma comparação de notas entre formatos demonstre qual formato produz mais aprendizagem. Uma questão pode ser melhor para avaliação independente do conhecimento, mas não necessariamente melhor como atividade de prática; o inverso também é possível.

## 3. Taxonomia inicial dos formatos de resposta

### 3.1 Reconhecimento fechado

O estudante seleciona uma resposta entre opções apresentadas.

Subtipos:

- verdadeiro ou falso;
- escolha única;
- múltiplas respostas;
- associação;
- seleção em imagem, tabela, matriz, grafo ou diagrama;
- resposta até acertar, com eliminação progressiva ou crédito parcial.

Vantagens operacionais:

- correção determinística;
- baixo custo de aplicação;
- comparabilidade e velocidade;
- facilidade para apresentar distratores diagnósticos.

Riscos:

- pistas produzidas pelas alternativas;
- acerto por reconhecimento ou eliminação;
- exposição a alternativas incorretas;
- falsa equivalência entre acerto e domínio independente;
- dificuldade de distinguir conhecimento parcial de adivinhação sem modelagem específica.

A revisão de Eisenkraemer, Jaeger e Stein concluiu que testes de reconhecimento e de recordação podem produzir efeito de testagem, mas que tarefas de produção tendem a gerar benefícios maiores. A mesma revisão destaca que feedback em múltipla escolha ajuda a reduzir a retenção de alternativas incorretas.

### 3.2 Recordação curta construída

O estudante produz uma palavra, expressão, número, fórmula ou resposta muito curta.

Subtipos:

- lacuna;
- resposta curta exata;
- resposta com variantes aceitas;
- resposta numérica com tolerância e unidade;
- resposta muito curta sem alternativas visíveis.

A meta-análise de Sher et al. reuniu seis coortes de três estudos, totalizando 1.191 participantes em educação de profissionais de saúde. A análise inicial apresentou heterogeneidade extrema; após retirada de um conjunto discrepante, estudantes obtiveram notas menores nas questões de resposta muito curta que em múltipla escolha. Isso é compatível com menor efeito de pistas, mas não demonstra que o formato cause mais aprendizagem. A mesma revisão encontrou discriminação forte e confiabilidade aceitável para respostas muito curtas, enquanto os efeitos de prática permaneceram inconclusivos.

Implicação: **nota menor não deve ser interpretada automaticamente como pior questão ou pior aprendizagem**. Pode indicar maior exigência de produção independente.

### 3.3 Recordação livre, explicação e justificativa

O estudante produz texto ou representação sem um conjunto pequeno de respostas pré-especificado.

Subtipos:

- definição;
- explicação causal;
- justificativa de escolha;
- comparação;
- resumo;
- explicação de erro;
- solução discursiva;
- construção de tabela, mapa, fluxo ou outra representação.

Esses formatos podem revelar raciocínio e modelos mentais que permanecem invisíveis na múltipla escolha. Entretanto, introduzem problemas de correção:

- pluralidade de respostas válidas;
- necessidade de rubricas;
- consistência entre avaliadores;
- sensibilidade a escrita, idioma e conhecimento periférico;
- custo de correção;
- risco de avaliações automatizadas opacas ou injustas.

A revisão de Gao et al. mostra forte crescimento de sistemas automáticos para respostas textuais no ensino pós-secundário, mas não autoriza supor que qualquer modelo automático produza pontuação ou feedback válido. A Plataforma ARA deverá registrar método de avaliação, versão do avaliador, confiança, possibilidade de contestação e destino da resposta.

### 3.4 Resolução e produção estruturada

O estudante realiza uma sequência de operações ou constrói uma resposta verificável.

Exemplos:

- cálculo numérico ou simbólico;
- ordenação de etapas;
- montagem de expressão;
- preenchimento de tabela;
- manipulação de grafo, árvore, matriz, fluxo ou plano cartesiano;
- classificação com justificativa;
- resolução por etapas.

A pontuação pode considerar resultado, processo ou ambos. Uma resposta final correta não comprova procedimento correto, e um erro aritmético final pode ocultar raciocínio adequado. Portanto, a plataforma precisa poder representar:

- etapas esperadas;
- invariantes;
- tolerâncias;
- caminhos alternativos;
- crédito parcial;
- ponto do primeiro erro;
- feedback por etapa.

### 3.5 Execução e desempenho autêntico

O estudante produz algo executável ou observável.

Exemplos:

- escrever e executar código;
- depurar;
- escrever consulta;
- configurar um sistema;
- produzir arquivo;
- pronunciar ou gravar fala;
- realizar procedimento demonstrável.

A pontuação pode usar testes, análise estática, comparação de saída, rubrica, inspeção humana ou combinação. Para programação, é necessário separar:

- sintaxe;
- resultado em testes públicos;
- resultado em testes ocultos;
- legibilidade;
- complexidade;
- segurança;
- explicação do código;
- transferência para problema novo.

## 4. Formato da prática e formato da avaliação final

Pan e Rickard sintetizaram 192 efeitos de transferência, extraídos de 122 experimentos e 67 trabalhos, com 10.382 participantes. O efeito médio de transferência da prática de recuperação em comparação com reexposição foi `d = 0,40`, mas variou conforme a congruência entre respostas de prática e de teste, o grau de elaboração e o desempenho inicial.

Isso impede uma regra simplista segundo a qual “resposta aberta sempre transfere” ou “múltipla escolha não produz aprendizagem”. A ARA deverá registrar separadamente:

- formato da prática;
- formato do pós-teste;
- proximidade entre item praticado e item avaliado;
- repetição literal versus item equivalente;
- retenção versus transferência;
- tempo entre prática e avaliação.

## 5. Formato altera a medida

Breuer, Scherndl e Ortner sintetizaram 102 estudos e 392 efeitos sobre avaliações abertas e fechadas. Os escores dos dois formatos apresentaram correlação positiva alta (`r = 0,67`), mas as avaliações fechadas produziram notas significativamente maiores (`d_av = -0,65`, considerando a codificação usada pelos autores). Respostas curtas abertas se correlacionaram mais fortemente com formatos fechados que ensaios.

Esse resultado é psicométrico: formatos podem medir constructos relacionados, porém não intercambiáveis. Consequências para ARA:

- não comparar notas de perfis diferentes sem ajuste e documentação;
- não usar o mesmo limiar de domínio para formatos com demandas distintas;
- registrar presença e qualidade de distratores;
- distinguir avaliação de aprendizagem de atividade para aprender;
- preservar idioma, extensão permitida, tempo e recursos disponíveis.

## 6. Conteúdo do feedback

A meta-análise de van der Kleij, Feskens e Eggen reuniu 40 estudos e 70 efeitos em ambientes computacionais. Os efeitos médios reportados foram:

- **conhecimento do resultado/correção:** `0,05`;
- **apresentação da resposta correta:** `0,32`;
- **feedback elaborado, com explicação:** `0,49`.

O feedback elaborado mostrou vantagem maior em resultados de ordem superior. Isso não significa que toda explicação longa seja boa. A elaboração precisa ser pertinente, compreensível e utilizável.

### 6.1 Camadas propostas

1. **sem feedback:** a resposta é registrada sem informação posterior;
2. **conhecimento do resultado:** correto, incorreto ou parcialmente correto;
3. **resposta correta:** exibe a solução ou resposta esperada;
4. **explicação conceitual:** explica por que a resposta está correta;
5. **explicação do erro:** relaciona a resposta dada a um erro ou concepção provável;
6. **pista:** fornece apoio sem revelar toda a resposta;
7. **exemplo resolvido:** demonstra procedimento em item semelhante ou no próprio item;
8. **feedback por etapa:** identifica onde o processo se desviou;
9. **recomendação de estudo:** liga o erro a conteúdo, pré-requisito ou revisão;
10. **feedback social ou humano:** docente, par, tutor ou avaliador;
11. **feedback automatizado probabilístico:** requer indicação de origem, confiança e contestação.

### 6.2 Dimensões independentes

- conteúdo;
- granularidade;
- momento;
- origem;
- persistência;
- visibilidade;
- personalização;
- ação posterior permitida;
- relação com nova tentativa;
- consequência sobre nota ou progressão.

## 7. O momento do feedback não possui vencedor universal

Kandemir et al. analisaram 51 estudos e 160 efeitos de aprendizagem assistida por computador. Os atrasos variaram de um segundo a sete dias ou de um a sessenta itens intermediários. O efeito médio de feedback imediato versus atrasado foi praticamente nulo (`g = 0,03`, IC95% `[-0,08; 0,13]`, `p = 0,61`). Nível educacional, domínio e restrições de tempo de resposta moderaram resultados; estudos com atrasos de um dia ou mais foram relativamente poucos.

Portanto, o parâmetro “imediato versus atrasado” é insuficiente. A plataforma deverá representar:

- atraso em tempo;
- atraso em número de itens;
- feedback antes ou depois de nova tentativa;
- feedback por item ou por conjunto;
- possibilidade de antecipação ativa da resposta;
- disponibilidade posterior para revisão;
- domínio e complexidade da tarefa;
- correção inicial do estudante.

## 8. Recuperação só pode ser interpretada com feedback e condição comparadora

Uma meta-análise de 2025 comparou prática de recuperação a atividades elaborativas em 44 estudos e 142 comparações. A vantagem média da recuperação foi pequena (`g = 0,14`) e tornou-se maior quando havia feedback (`g = 0,50`). Sem feedback, atividades elaborativas puderam superar a recuperação.

Isso reforça duas decisões metodológicas:

- “fazer perguntas” não é intervenção suficientemente descrita;
- a condição comparadora precisa ser especificada: releitura, explicação, mapa conceitual, discussão, exemplo ou outro estudo ativo.

## 9. Nova tentativa e revelação

A nova tentativa pode ocorrer:

- antes de qualquer feedback;
- após conhecimento do resultado;
- após pista;
- após resposta correta;
- após explicação;
- com o mesmo item;
- com item equivalente;
- imediatamente ou em revisão posterior.

Essas condições possuem mecanismos diferentes. Revelar a resposta pode interromper recuperação adicional, mas também corrigir erro e evitar consolidação de alternativa incorreta. A ARA deverá registrar a sequência completa de ações, e não somente o número total de tentativas.

## 10. Taxonomia provisória de parâmetros

| Família | Parâmetros candidatos |
|---|---|
| demanda de resposta | reconhecimento, recordação com pista, recordação livre, explicação, resolução, produção, execução |
| estrutura | binária, escolha única, múltipla, lacuna, resposta curta, texto, etapas, objeto estruturado, artefato executável |
| pontuação | exata, variantes, tolerância, conjunto, testes, análise, rubrica, humano, híbrida |
| feedback de resultado | nenhum, correto/incorreto, parcial, nível de confiança |
| feedback de conteúdo | resposta correta, explicação, erro específico, pista, exemplo, recomendação |
| momento | imediato, após item, após conjunto, por tempo, por itens, em revisão posterior |
| tentativa | única, limitada, ilimitada, escalonada por pistas, item equivalente |
| revelação | nunca, a pedido, após limite, automática, somente em revisão |
| consequência | nenhuma, progresso, nota, bloqueio, certificação, condição experimental |
| origem | sistema, autor, docente, par, avaliador automatizado identificado |
| persistência | efêmero, disponível na sessão, histórico pessoal, registro institucional |

## 11. Implicações específicas por domínio

### Línguas

- produção e reconhecimento de vocabulário não são equivalentes;
- tradução, ortografia, pronúncia, escuta e uso em contexto requerem avaliadores diferentes;
- variantes válidas, acentuação, romanização e sistemas de escrita precisam ser explicitados;
- feedback corretivo deve distinguir erro lexical, gramatical, fonológico e ortográfico.

### Programação

- múltipla escolha sobre conceitos não substitui produção e execução;
- resultado correto em testes não garante legibilidade ou compreensão;
- mensagens de compilador são feedback do ambiente, não necessariamente feedback pedagógico;
- pistas, testes públicos, testes ocultos e solução de referência devem ser parâmetros separados;
- respostas produzidas por ferramentas externas não devem ser confundidas com aprendizagem independente.

## 12. Proibições interpretativas

A instrumentação e os relatórios não deverão concluir automaticamente que:

- nota maior em múltipla escolha significa mais conhecimento;
- resposta aberta é sempre pedagogicamente superior;
- maior tempo significa maior esforço ou aprendizagem;
- feedback longo é melhor;
- feedback imediato é sempre melhor;
- uso de pista representa fracasso;
- número de tentativas mede capacidade;
- concordância do avaliador automatizado garante validade;
- satisfação ou preferência prova aprendizagem.

## 13. Lacunas prioritárias

- comparações de formatos em uso autodirigido de adultos;
- estudos em português e em contextos brasileiros ou portugueses;
- efeitos de formato em aprendizagem móvel e sob interrupções;
- explicação de erro versus explicação geral;
- sequências de pista, tentativa e revelação;
- transferência para tarefas autênticas;
- acessibilidade de formatos abertos e fechados;
- validade de avaliação automática multilíngue;
- feedback para representações estruturadas e código;
- efeitos de escolha do próprio estudante sobre formato e feedback.

## 14. Conclusão provisória

A literatura apoia tratar formatos de resposta e feedback como sistemas multidimensionais. Reconhecimento, produção, explicação e execução têm demandas e formas de validação diferentes. Feedback de simples correção, resposta correta e elaboração não são equivalentes; o momento do feedback depende do contexto e não apresenta efeito médio universal. A Plataforma ARA deverá preservar essas dimensões como parâmetros versionados e registrar a condição efetivamente aplicada.

Nenhum parâmetro desta síntese está aprovado como padrão universal. A decisão sobre perfis e precedência pertence à Issue #4, depois da integração com outras frentes de evidência.
