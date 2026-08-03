# Protocolo focado P1 — prática, resposta, tentativas, revelação, feedback e consequências

**Data:** 3 de agosto de 2026  
**Issue:** #4  
**Pacote:** P1  
**Idioma:** `pt-BR`  
**Tipo:** síntese focada orientada a decisão, apoiada no corpus formal já existente e em atualização verificável

## 1. Pergunta decisória

Como o ARA deve representar condições de prática e resposta sem confundir:

- mecanismo de aprendizagem;
- forma de expressão do estudante;
- validade e correção;
- número e sequência de tentativas;
- revelação da resposta;
- conteúdo e momento do feedback;
- pontuação e consequência;
- acessibilidade;
- observação para pesquisa?

## 2. Resultado esperado

O pacote deverá produzir:

1. síntese crítica integrada;
2. parâmetros candidatos e parâmetros aceitos para a primeira taxonomia;
3. perfil AraLearn de referência;
4. perfis contrastantes;
5. autoridade, precedência, conflitos e não autorizações;
6. alternativas rejeitadas ou adiadas;
7. riscos e incertezas que possam alterar recomendações;
8. handoff para #5, #6 e #8;
9. nenhum schema de produção, adapter, biblioteca, UX ou código.

## 3. Fontes internas obrigatórias

- visão canônica do produto;
- Issue #4;
- síntese integrada da Issue #30;
- auditoria dos resources do AraLearn;
- documentação do modelo didático e do estado de estudo não punitivo do AraLearn;
- revisão de revisões;
- síntese focada sobre formatos de resposta e feedback;
- corpus formal, extrações e mapa de sobreposição;
- benchmark de sistemas e gêneros;
- experimentos de componentes somente como evidência não normativa.

## 4. Frentes externas

### 4.1 Prática de recuperação e quizzes

Incluir sínteses que permitam distinguir:

- prática versus reexposição ou atividade elaborativa;
- resposta selecionada versus construída;
- retenção versus transferência;
- repetição, feedback e formato do teste;
- prática em sala versus laboratório.

### 4.2 Feedback

Incluir sínteses ou estudos centrais sobre:

- conhecimento do resultado;
- resposta correta;
- feedback elaborado;
- resposta até acertar;
- feedback imediato e atrasado;
- correção de respostas erradas e de baixa confiança;
- riscos de distratores e informação incorreta.

### 4.3 Tentativas, retry e reveal

Incluir evidência sobre:

- tentativa única e múltiplas tentativas;
- answer-until-correct;
- segunda tentativa após pista, resultado ou solução;
- mesmo item versus item equivalente;
- crédito por tentativa;
- efeitos sobre aprendizagem, medida e comportamento.

### 4.4 Consequências e stakes

Incluir:

- quizzes de baixo risco;
- contribuição para nota;
- high stakes;
- ansiedade de teste;
- esforço e motivação;
- risco de transformar prática em medição punitiva.

### 4.5 Acessibilidade

Incluir:

- múltiplos meios de ação e expressão;
- alternativas de resposta;
- tecnologia assistiva;
- tolerância de entrada;
- identificação, correção e reversão de erros;
- tempo e acomodações;
- preservação do constructo avaliado.

## 5. Estratégia de busca e atualização

A rodada utiliza o corpus formal do projeto como base e acrescenta busca dirigida em:

- PubMed;
- ERIC;
- páginas oficiais de periódicos;
- Springer Nature;
- APA / Journal of Educational Psychology;
- Royal Society Open Science;
- W3C WAI;
- CAST;
- repositórios institucionais legítimos.

Consultas orientadoras:

```text
retrieval practice feedback meta-analysis
response format constructed selected meta-analysis
computer-based feedback network meta-analysis answer-until-correct
feedback timing computer-assisted learning meta-analysis
multiple attempts formative assessment feedback
answer reveal corrective feedback multiple choice
low-stakes quizzes grading meta-analysis
stakes feedback testing achievement meta-analysis
test anxiety high stakes meta-analysis
accessible computer-based assessment response systematic review
UDL action expression response accessibility
WCAG input assistance error prevention
```

## 6. Inclusão

Priorizar:

1. meta-análises e revisões sistemáticas;
2. estudos experimentais centrais para lacunas não cobertas por síntese;
3. normas e orientações oficiais de acessibilidade;
4. fontes técnicas primárias quando descrevem o AraLearn;
5. publicações até a data da busca.

Uma fonte entra quando altera ou sustenta ao menos uma decisão sobre parâmetro, valor, conflito, risco ou incerteza.

## 7. Exclusão

Excluir como base decisória principal:

- marketing de produto;
- opinião sem método;
- resultados de satisfação tratados como aprendizagem;
- desempenho de software tratado como eficácia pedagógica;
- estudos de um domínio generalizados sem qualificação;
- avaliação automática tratada como autoridade apenas por acurácia técnica;
- acessibilidade inferida de conformidade automatizada isolada.

## 8. Estrutura de extração

Para cada fonte:

- identificação;
- desenho e tipo de evidência;
- população e domínio;
- intervenção e comparador;
- desfecho;
- achado central;
- limitação decisiva;
- parâmetro ou decisão informada;
- profundidade de acesso;
- estado de verificação.

## 9. Amostragem e suficiência

A amostra é de variação máxima e orientada à decisão.

A frente é suficiente quando:

1. cada dimensão do P1 possui ao menos uma síntese confiável ou conjunto justificado de estudos centrais;
2. há casos contrastantes para resposta, feedback, tentativa, reveal e stakes;
3. acessibilidade está representada por revisão e orientação oficial;
4. duas adições sucessivas não criam nova família de parâmetro nem alteram a recomendação central;
5. lacunas restantes podem ser registradas sem impedir a primeira taxonomia;
6. não há fonte inacessível indispensável sendo substituída por suposição.

Saturação é avaliada por dimensão:

- `alcançada`;
- `aproximada`;
- `não alcançada`.

## 10. Regra de decisão

Uma possibilidade descoberta será classificada como:

- parâmetro aceito para a taxonomia;
- valor recomendado para perfil específico;
- valor permitido, mas não recomendado como padrão;
- candidato adiado;
- não recomendado;
- questão de produto para #6;
- questão de UX para #8;
- questão de instrumentação para #5.

Aceitar um parâmetro significa aceitar a necessidade de representar a variação. Não significa implementar todos os seus valores na primeira release.

## 11. Não autorizações

Este pacote não autoriza:

- schema de curso;
- contrato de practice ou validator;
- alteração do kernel;
- seleção de biblioteca;
- coleta de tentativas;
- dashboard;
- interface de configuração;
- integração de IA para correção;
- implementação de notas, ranking ou gamificação;
- retomada dos adapters experimentais.

## 12. Validação

- rastreabilidade entre afirmação e fonte;
- distinção entre aprendizagem e medida;
- distinção entre disponibilidade de evento e autorização de coleta;
- consistência entre parâmetros, perfis e precedência;
- contraexemplos formativos, somativos, de pesquisa e acessibilidade;
- revisão de que o perfil AraLearn não foi universalizado;
- revisão de que possibilidades externas não viraram requisitos automáticos.
