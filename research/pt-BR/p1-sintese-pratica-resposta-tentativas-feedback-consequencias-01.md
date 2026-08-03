# Pacote P1 — prática, resposta, tentativas, revelação, feedback e consequências

**Versão:** 0.1  
**Data:** 3 de agosto de 2026  
**Issue:** #4  
**Estado:** pacote concluído; parâmetros aceitos para a primeira taxonomia, sujeitos à síntese final da Issue #4  
**Natureza:** síntese crítica e recomendação; não é schema de produção, contrato técnico, UX nem implementação

## 1. Conclusão principal

O ARA não deve possuir um único `exerciseMode`, `feedbackMode` ou `attempts` capaz de representar toda prática.

A evidência e os casos do AraLearn sustentam um modelo composto por dimensões independentes:

```text
finalidade da prática
× demanda cognitiva
× forma da resposta
× validade
× autoridade de avaliação
× política de crédito
× limite e sequência de tentativas
× pistas
× gatilho e conteúdo de revelação
× resultado e conteúdo do feedback
× timing e persistência
× consequência e visibilidade
× acomodação de acessibilidade
× instrumentação autorizada
```

Essas dimensões interagem, mas não devem ser fundidas. O mesmo item de escolha pode servir a prática formativa sem nota, avaliação diagnóstica, condição experimental ou exame somativo; o que muda não é apenas o renderer, mas tentativas, feedback, reveal, autoridade e consequência.

## 2. Caminho recomendado

### 2.1 Aceitar a variação; normatizar seletivamente

A primeira taxonomia deve aceitar os parâmetros necessários para descrever condições defensáveis. Isso não obriga o primeiro produto a implementar todos os valores.

A recomendação é:

1. preservar o AraLearn como perfil formativo, autodirigido e não punitivo;
2. aceitar perfis alternativos de mastery, ensino formal, avaliação somativa e investigação;
3. separar prática para aprender de avaliação para medir;
4. separar formato de resposta de demanda cognitiva;
5. separar validade, correção, crédito e autoridade;
6. representar a sequência completa entre tentativa, feedback, pista, reveal e nova tentativa;
7. manter consequências fora do mecanismo de prática;
8. tratar acessibilidade como camada de autoridade superior, não como preferência cosmética;
9. manter instrumentação desligada por padrão e subordinada a pergunta, consentimento e retenção;
10. adiar decisões de progressão, adaptação, scaffolding geral e analytics detalhados aos pacotes correspondentes.

### 2.2 Perfil inicial recomendado

Para o primeiro perfil ARA derivado do AraLearn:

- finalidade `formative-learning`;
- respostas determinísticas selecionadas ou construídas curtas quando adequadas;
- prática sem nota, ranking ou consequência externa;
- ausência de timer por padrão;
- tentativas não usadas como medida de domínio ou esforço;
- reveal por iniciativa do estudante;
- feedback imediato ou após tentativa, com resposta correta e explicação curta acionável;
- nova tentativa ou revisão posterior sem penalização;
- progresso estrutural separado de acerto;
- nenhuma coleta de tentativas, erros ou tempo por conveniência técnica.

Esse perfil é referência, não default universal para toda implantação.

## 3. Método e suficiência

O pacote utilizou:

- o corpus formal e as sínteses já produzidas pelo ARA;
- a síntese de formatos de resposta e feedback;
- a auditoria do AraLearn;
- documentação e código do AraLearn no commit auditado;
- meta-análises e revisões adicionais sobre quizzing, feedback, answer-until-correct, stakes e ansiedade;
- revisão e orientação oficial de acessibilidade.

O protocolo está em:

- `research/searches/2026-08-03-p1-pratica-resposta-feedback-protocolo.md`.

O corpus estruturado está em:

- `research/data/p1-evidence-corpus-01.csv`.

### 3.1 Saturação por dimensão

| Dimensão | Estado | Justificativa |
|---|---|---|
| prática de recuperação e quizzes | alcançada para taxonomia inicial | revisões amplas de laboratório e sala; moderadores conhecidos; lacunas não criam nova família de parâmetro |
| formato de resposta | alcançada para taxonomia inicial | evidência de aprendizagem e medida distingue respostas selecionadas, curtas e abertas |
| conteúdo do feedback | alcançada | meta-análises convergem para separar KR, KCR, elaboração e AUC; elaboração tende a ser mais útil que resultado isolado |
| timing do feedback | alcançada para aceitar o parâmetro; não para escolher valor universal | meta-análise de 2026 rejeita vencedor médio universal e identifica moderação contextual |
| tentativas e answer-until-correct | aproximada | há meta-análise e estudos centrais, mas grande concentração em escolha e domínios específicos |
| answer reveal | aproximada | evidência sustenta correção e risco de distratores, mas sequência ótima depende de tarefa e objetivo |
| consequences/stakes | aproximada | quizzes e stakes possuem sínteses, mas causalidade, motivação, ansiedade e seleção continuam misturadas |
| acessibilidade da resposta | não alcançada para catálogo completo; suficiente para invariantes | revisão e normas sustentam acomodações, correção acessível e múltiplos meios; faltam estudos por interação e domínio |

A insuficiência residual não impede a taxonomia inicial porque foi preservada como incerteza e não como escolha arbitrária.

## 4. O que a literatura permite afirmar

### 4.1 Quizzing é família de intervenção, não especificação de produto

Yang et al. (2021) sintetizaram 222 estudos e 48.478 estudantes e encontraram benefício médio de quizzes em contextos de sala. O efeito variou com:

- comparador;
- consistência entre formato da prática e avaliação;
- feedback corretivo;
- número de repetições;
- correspondência do material;
- local e momento da aplicação;
- duração e desenho do estudo.

A consequência para ARA é direta: `quiz=true` não descreve a condição.

Gonçalves, Muniz e Jaeger (2025) compararam recuperação a atividades elaborativas eficazes. A vantagem média da recuperação foi pequena e dependente de feedback. Isso impede que ARA adote prática de recuperação como única forma de estudo ativo.

### 4.2 Resposta selecionada e construída não são intercambiáveis

Breuer, Scherndl e Ortner (2023) encontraram correlação alta entre resultados de formatos abertos e fechados, mas diferenças sistemáticas de escores. Respostas fechadas tendem a produzir notas maiores, sem que isso indique melhor aprendizagem.

Sher et al. (2026), em corpus pequeno de educação em saúde, encontraram notas menores em respostas muito curtas do que em múltipla escolha, compatíveis com menor cueing. A transferência para ARA é conceitual:

- resposta mais difícil pode medir produção mais independente;
- nota menor não é evidência de pior design;
- limiares não devem atravessar formatos sem calibração;
- formato da prática e formato do pós-teste precisam ser registrados.

A taxonomia separa:

- `response.cognitive_demand`;
- `response.form`;
- `evaluation.credit_policy`.

### 4.3 Múltipla escolha pode ensinar e também expor erro

Revisões e estudos de testing effect mostram que múltipla escolha pode favorecer retenção. Ela também expõe distratores. Quando uma alternativa incorreta é selecionada ou lembrada, feedback corretivo reduz intrusões posteriores.

Portanto:

- distratores precisam ser pedagogicamente plausíveis, mas governados;
- prática selecionada não deve terminar em resultado incorreto sem correção quando o objetivo é aprender;
- `feedback.result` e `feedback.content` precisam ser distintos;
- mostrar `incorreto` sem resposta, pista ou explicação é valor permitido, mas fraco como padrão formativo.

### 4.4 Feedback elaborado é geralmente preferível a resultado isolado

Van der Kleij et al. (2015) e Mertens, Finn e Lindner (2022) convergem em uma hierarquia aproximada:

```text
feedback elaborado
> resposta correta / answer-until-correct em muitos contextos
> simples conhecimento de resultado
```

Essa hierarquia não autoriza explicações longas ou automáticas. Feedback útil deve ser:

- relacionado à tarefa;
- compreensível;
- acionável;
- proporcional à complexidade;
- compatível com nova tentativa ou revisão;
- claro quanto à origem e autoridade.

O ARA deve permitir composição em camadas:

1. estado de validade;
2. resultado;
3. resposta correta;
4. explicação conceitual;
5. erro específico;
6. pista;
7. exemplo resolvido;
8. feedback por etapa;
9. recomendação de estudo;
10. comentário humano.

### 4.5 Feedback também importa para respostas corretas

Butler, Karpicke e Roediger (2008) mostraram que feedback aumentou retenção de respostas corretas dadas com baixa confiança, além de corrigir erros.

Isso impede a regra:

```text
se correto → não mostrar feedback
```

Uma resposta correta pode resultar de:

- conhecimento estável;
- reconhecimento por pista;
- eliminação;
- adivinhação;
- raciocínio defeituoso com resultado correto;
- baixa confiança.

ARA não precisa solicitar confiança em toda prática. Entretanto, deve permitir feedback conceitual também após acerto e preservar `response.confidence_elicitation` como candidato adiado para P3/P4.

### 4.6 Não existe vencedor universal para timing

Kandemir et al. (2026) analisaram 51 estudos e 160 efeitos. O efeito médio entre feedback imediato e atrasado foi praticamente nulo, com moderação por nível, domínio e restrição de tempo.

`immediate` versus `delayed` é descrição insuficiente. A taxonomia precisa indicar:

- após qual tentativa;
- após item ou conjunto;
- número de itens de atraso;
- duração temporal;
- liberação manual;
- disponibilidade em revisão;
- se o estudante pode tentar novamente antes do feedback.

Para o perfil pessoal determinístico, feedback imediato/after-attempt é recomendado por fricção e correção. Isso é decisão de perfil, não lei pedagógica.

### 4.7 Tentativas precisam de sequência, não só de número

`3 tentativas` não informa o tratamento. Entre tentativas o estudante pode receber:

- nada;
- apenas válido/inválido;
- correto/incorreto;
- pista;
- eliminação de alternativa;
- resposta correta;
- explicação;
- item equivalente.

AUC e IF-AT mostram que responder até acertar pode fornecer feedback imediato e crédito parcial. A meta-análise de Chang e Li (2019) encontrou vantagem sobre múltipla escolha convencional no corpus analisado. Mertens et al. também encontraram efeitos favoráveis para AUC em parte das comparações.

Entretanto, AUC não deve ser universal porque:

- é fortemente associado a tarefas selecionadas;
- pode converter tentativas em busca por eliminação;
- mede processo diferente de tentativa única;
- precisa de política de crédito;
- pode aumentar ansiedade em alguns contextos;
- a resposta final correta não revela necessariamente conhecimento independente.

A taxonomia aceita:

- `attempts.limit`;
- `attempts.sequence`;
- `attempts.retry_target`;
- `evaluation.credit_policy`.

### 4.8 Reveal pode corrigir e também encerrar recuperação

Revelar a resposta possui efeitos diferentes segundo o momento:

- antes de tentativa;
- por pedido;
- após erro;
- após limite;
- depois do conjunto;
- depois da avaliação;
- em revisão posterior.

A revelação pode:

- impedir persistência de erro;
- reduzir exposição a distrator incorreto;
- oferecer oportunidade de restudo;
- corrigir baixa confiança;
- interromper recuperação adicional;
- invalidar medição independente se ocorrer cedo.

A decisão recomendada é separar:

- `reveal.trigger`;
- `reveal.content`;
- `attempts.sequence`;
- `practice.purpose`.

No perfil AraLearn, reveal por iniciativa do estudante é preservado. Em avaliação somativa, reveal fica bloqueado até a liberação oficial. Em investigação, fica fixado por condição.

### 4.9 Stakes são consequência, não propriedade intrínseca da prática

Sotola e Crede (2021) encontraram associação moderada entre quizzes de baixo risco e desempenho. Efeitos foram maiores quando contribuíam para a nota. Isso não identifica o mecanismo:

- participação;
- regularidade;
- esforço;
- seleção dos estudantes;
- alinhamento com prova;
- recuperação;
- feedback;
- consequência.

Phelps (2019) também encontrou interações entre frequência, stakes e feedback, mas o corpus é amplo e heterogêneo.

Von der Embse et al. (2018) mostraram associação negativa entre ansiedade de teste e resultados educacionais, e ligação entre consequências de alto risco e maior ansiedade.

A recomendação é:

- consequências explícitas e versionadas;
- `none` ou `structural-progress` no perfil pessoal;
- `low-stakes-score` permitido em curso formal;
- notas, certificação e decisões externas em perfil separado;
- ranking público rejeitado na primeira taxonomia ativa;
- nenhum score ou consequência inferido de simples conclusão estrutural.

### 4.10 Acessibilidade altera autoridade e precedência

CAST UDL 3.0 recomenda múltiplos meios de ação e expressão e feedback orientado à ação. W3C WCAG 2.2 exige instruções, identificação de erro, sugestão, confirmação, correção e reversibilidade, além de cautela com limites de tempo.

Leria, Benitez e Fraga (2021) mostram que avaliações computadorizadas ainda criam barreiras importantes para pessoas com deficiência visual.

Consequências para ARA:

- toda resposta precisa de caminho por teclado e tecnologia assistiva;
- erro não pode ser indicado apenas por cor;
- entrada precisa ser preservada após erro;
- foco e anúncio de feedback devem ser previsíveis;
- métodos alternativos de resposta podem ser acomodação;
- tempo adicional pode ter precedência sobre default;
- acomodação não pode ser penalizada silenciosamente;
- quando muda o constructo, a mudança deve ser documentada;
- dados de acomodação são sensíveis e não entram em analytics comuns.

## 5. Perfil AraLearn reconstruído para P1

### 5.1 Evidência funcional

O AraLearn documenta:

- prática dentro da microssequência;
- validação determinística de escolha e lacuna;
- feedback e conteúdo `after`;
- reveal;
- progressão e retomada estruturais;
- ausência de nota, ranking e punição;
- ausência de timer de card;
- nenhuma coleta de abertura, tempo, tentativas, acertos, erros ou resultado;
- conclusão estrutural sem inferência de domínio.

### 5.2 Registro do perfil

| Dimensão | Valor de referência |
|---|---|
| finalidade | `formative-learning` |
| demanda | reconhecimento e recordação com pista, conforme choice/gap |
| forma | escolha única/múltipla e lacuna literal, além de prática estruturada específica do flow |
| validade | implícita nos validators; não modelada como parâmetro geral |
| autoridade | aplicação determinística |
| crédito | sem nota; acerto binário operacional |
| tentativas | não persistidas nem interpretadas; prática não punitiva |
| retry | learner-controlled no card; comportamento exato não deve ser universalizado |
| reveal | disponível por iniciativa do estudante |
| resultado | correto/incorreto após confirmação, quando aplicável |
| conteúdo | explicação canônica `after`; feedback local opcional |
| timing | no ciclo corrente do card |
| consequência | progresso estrutural e possibilidade de marcar para rever; sem score externo |
| telemetry | nenhum histórico de tentativa, resultado ou tempo |

### 5.3 Decisão

O perfil é preservado como `aralearn-reference`. Seus valores não serão copiados para todos os cursos ou implantações.

## 6. Parâmetros aceitos para a primeira taxonomia

Os registros completos estão em:

- `research/data/p1-parameter-records-01.csv`.

### 6.1 Aceitos

- `practice.purpose`;
- `response.cognitive_demand`;
- `response.form`;
- `response.validity_policy`;
- `evaluation.authority`;
- `evaluation.credit_policy`;
- `attempts.limit`;
- `attempts.sequence`;
- `attempts.retry_target`;
- `hints.access`;
- `reveal.trigger`;
- `reveal.content`;
- `feedback.result`;
- `feedback.content`;
- `feedback.timing`;
- `feedback.persistence`;
- `consequence.level`;
- `consequence.score_visibility`;
- `consequence.aggregation`;
- `accessibility.response_accommodation`;
- `accessibility.time_policy`.

Aceitação significa que a dimensão deve existir na taxonomia. Valores concretos podem permanecer candidatos, recomendados ou adiados.

### 6.2 Adiados

- `telemetry.attempt_capture`: P4 e Issue #5;
- `response.confidence_elicitation`: P3/P4;
- avaliação automática autoritativa de resposta aberta: pesquisa e produto posteriores;
- inferência de misconception a partir de resposta correta: domínio e instrumentos posteriores;
- defaults de `attempts.retry_target`: dependem de P2 e domínios;
- regra geral de agregação de múltiplas tentativas: depende do contexto institucional;
- feedback adaptativo por perfil de estudante: P3;
- analytics de esforço ou persistência: P4, com forte risco de inferência indevida.

### 6.3 Rejeitados nesta primeira versão

- um único `exerciseMode` monolítico;
- correctness-only como default formativo universal;
- tentativa única como default universal;
- tentativas ilimitadas como default universal;
- reveal sempre ou reveal nunca como regra universal;
- feedback imediato ou atrasado como regra universal;
- score, nota ou ranking derivados de conclusão estrutural;
- tentativa contada como atenção, esforço, domínio ou dificuldade;
- grade contribution automática em toda prática;
- ranking/leaderboard como capacidade ativa da primeira taxonomia;
- avaliação probabilística como única autoridade em decisão consequencial;
- coleta de eventos porque o renderer consegue emiti-los.

## 7. Perfis contrastantes

O arquivo estruturado está em:

- `research/data/p1-profile-comparison-01.csv`.

### 7.1 `aralearn-reference`

Autodirigido, não punitivo, offline, feedback no card, reveal por iniciativa, sem nota ou telemetry de tentativa.

### 7.2 `self-directed-mastery`

Alternativa pessoal com retry, pistas escalonadas e possível gate local por evidência atual, sem nota externa.

### 7.3 `formal-formative-course`

Curso com política explícita de tentativas, feedback acionável e score de baixo risco opcional.

### 7.4 `summative-institutional`

Avaliação consequencial separada do estudo normal, com tentativas/reveal controlados, revisão, acomodação, apelação e autoridade definida.

### 7.5 `research-condition`

Configuração versionada e bloqueada por protocolo dentro de consentimento e ética, sem converter participantes em perfis permanentes.

### 7.6 `accessibility-overlay`

Camada transversal que remove barreiras e pode modificar controle, tempo ou modalidade. Não é uma pedagogia separada.

## 8. Autoridade e precedência

### 8.1 Ordem geral

Quando há conflito, aplicar:

1. lei, segurança, ética e acessibilidade obrigatória;
2. consentimento, retirada e direitos do participante;
3. protocolo de pesquisa aprovado;
4. política institucional de avaliação;
5. configuração de curso/autor;
6. preferência do estudante onde o perfil permite;
7. default do produto;
8. disponibilidade técnica da implantação.

Disponibilidade técnica não possui autoridade pedagógica. Se uma capacidade está ausente:

- o sistema declara indisponibilidade;
- não substitui por comportamento diferente em silêncio;
- não altera consequência ou score sem regra;
- oferece alternativa aprovada quando existir.

### 8.2 Conflitos típicos

#### Learner reveal versus summative lock

- pessoal/formativo: learner pode revelar segundo configuração;
- somativo: política pode bloquear até release;
- pesquisa: condição pode bloquear dentro de consentimento;
- acessibilidade não implica reveal antecipado, mas garante acesso ao feedback quando liberado.

#### Learner retry versus grade policy

- pessoal: learner controla dentro do perfil;
- curso formal: autor/instituição define;
- score oficial precisa de agregação explícita;
- tentativa extra como acomodação não pode ser penalizada sem justificativa de constructo.

#### Research lock versus accessibility

Protocolo não pode remover direito obrigatório. Se a acomodação altera o constructo decisivamente:

- criar condição alternativa;
- analisar separadamente;
- ou não incluir participante, com justificativa ética explícita;
- nunca forçar barreira para preservar desenho experimental.

#### Feedback probabilístico versus autoridade humana

LLM ou classificador pode:

- sugerir;
- diagnosticar provisoriamente;
- priorizar revisão;
- produzir rascunho de feedback.

Não pode, por default:

- emitir nota final de alto risco;
- bloquear progresso institucional;
- afirmar misconception como fato;
- substituir contestação e revisão.

## 9. Implicações para pesquisa e analytics

### 9.1 Eventos não são parâmetros pedagógicos

P1 define comportamentos que podem gerar eventos. Isso não autoriza persistência.

Exemplos de eventos possíveis:

- resposta submetida;
- entrada inválida;
- resultado apresentado;
- pista solicitada;
- reveal solicitado;
- feedback aberto;
- retry iniciado;
- resposta revisada.

Cada evento futuro requer em #5:

- pergunta;
- constructo;
- unidade;
- finalidade;
- autoridade;
- consentimento;
- retenção;
- acesso;
- inferências permitidas e proibidas.

### 9.2 Inferências proibidas por default

Não inferir automaticamente:

- atenção de tempo de resposta;
- esforço de número de tentativas;
- domínio de acerto imediato;
- dificuldade individual de uso de pista;
- deficiência de acomodação utilizada;
- motivação de reveal;
- aprendizagem de conclusão estrutural;
- desonestidade de resposta rápida;
- compreensão de score alto em múltipla escolha.

## 10. Implicações para produto e domínio

A Issue #6 deverá distinguir normativamente:

- practice;
- response;
- response attempt;
- validity result;
- assessment result;
- credit/score;
- feedback;
- hint;
- reveal;
- consequence;
- accommodation;
- configuration snapshot;
- research observation.

P1 não decide se cada conceito será entidade, value object ou policy. Ele demonstra que não podem ser semanticamente fundidos.

## 11. Implicações para arquitetura

A Issue #7 deverá garantir, depois de #6:

- validators capazes de separar invalid/incorrect/partial/correct/review-required;
- políticas de tentativa e feedback configuradas por dados aprovados;
- ausência de lógica pedagógica específica no kernel;
- resposta e feedback offline nas capacidades do baseline;
- reveal e hidden material protegidos conforme perfil;
- capacidade ausente tratada explicitamente;
- probabilistic assistance fora da autoridade determinística;
- instrumentação desacoplada do ciclo funcional;
- acessibilidade como requisito de cada renderer/practice.

Nenhum desses itens seleciona stack.

## 12. Implicações para UX

A Issue #8 deverá especificar:

- instrução de resposta;
- número de tentativas quando relevante;
- consequência antes da submissão;
- estado invalid/incorrect/partial/correct;
- foco e anúncio de feedback;
- preservação da entrada;
- ação clara para tentar, pedir pista, revelar, revisar ou contestar;
- distinção visual e textual entre practice e assessment;
- confirmação antes de submissão irreversível;
- score com significado e limitação;
- acomodações e tempo;
- funcionamento offline e indisponibilidade de capacidade.

Codex não poderá inventar esses estados durante implementação.

## 13. Alternativas descartadas ou adiadas

### 13.1 “Preservar exatamente o AraLearn”

Descartada como modelo total. Preserva-se o perfil, não o limite de respostas e políticas.

### 13.2 “Mastery em tudo”

Adiada como regra geral. Mastery exige definição de evidência, progressão e equivalência de itens, tratadas em P2.

### 13.3 “Toda prática vale nota para aumentar adesão”

Descartada como default. Nota pode alterar participação, mas também altera fenômeno, ansiedade, estratégia e equidade.

### 13.4 “Sempre permitir infinitas tentativas e melhor nota”

Descartada como universal. É útil em alguns perfis, inadequada para medida e pode produzir score por exploração.

### 13.5 “Resposta correta é feedback suficiente”

Não recomendada como default. Pode corrigir, mas elaboração acionável tende a produzir resultados melhores.

### 13.6 “Feedback imediato é sempre melhor”

Descartada pela meta-análise de timing.

### 13.7 “LLM avalia respostas abertas”

Adiada. Pode auxiliar, mas autoridade, validade, bias, contestação, versão e privacidade precisam de investigação e domínio próprios.

## 14. Riscos relevantes

### 14.1 Explosão combinatória

Muitos parâmetros combináveis podem gerar configurações incoerentes.

Mitigação:

- perfis;
- regras de compatibilidade;
- defaults contextuais;
- progressive disclosure;
- validação de configuração;
- não expor todo candidato em toda release.

### 14.2 Confundir taxonomia com implementação

Aceitar 21 dimensões não significa construir 21 controles ou todas as combinações.

Mitigação:

- maturidade;
- release scope;
- handoff para #6/#8;
- perfis aprovados.

### 14.3 Comparar scores incompatíveis

Respostas abertas e fechadas, múltiplas tentativas e tentativa única medem condições diferentes.

Mitigação:

- snapshot de configuração;
- formato e política de crédito registrados;
- proibir agregação silenciosa.

### 14.4 Feedback excessivo

Elaboração pode virar sobrecarga, resposta pronta ou texto genérico.

Mitigação:

- feedback em camadas;
- concisão;
- ação posterior;
- testes de compreensão;
- adaptação somente quando justificada.

### 14.5 Stakes contaminarem estudo

Nota e ranking podem deslocar motivação e aumentar ansiedade.

Mitigação:

- perfis separados;
- consequências transparentes;
- low stakes como opção, não universal;
- ranking fora da primeira versão.

### 14.6 Acessibilidade como exceção tardia

Adicionar acomodação depois pode invalidar renderer, prática e pesquisa.

Mitigação:

- parâmetro estrutural;
- precedência;
- testes desde contrato e UX;
- participação de usuários posteriormente.

## 15. Incertezas que podem alterar decisões

1. efeitos de unlimited retry em adultos trabalhadores e estudo fragmentado;
2. melhor sequência entre pista, retry, reveal e item equivalente por domínio;
3. impacto de múltiplas tentativas sobre score, equidade e comportamento em cursos formais;
4. uso de resposta equivalente como mastery evidence;
5. feedback multi-dia em contextos reais;
6. acessibilidade de respostas estruturadas complexas em smartphone;
7. validade e contestabilidade de feedback por IA em resposta aberta;
8. diferenças Brasil/Portugal e contextos não WEIRD;
9. custo cognitivo de confidence judgements e explicações obrigatórias;
10. quando time limit é parte legítima do constructo.

Nenhuma dessas incertezas altera a conclusão central de que as dimensões devem ser separadas. Elas podem alterar defaults e perfis.

## 16. Handoff e próxima etapa

P1 fornece à Issue #4:

- 21 parâmetros aceitos;
- 2 candidatos adiados explícitos;
- 1 capacidade rejeitada para a primeira versão (`consequence.ranking`);
- perfil AraLearn;
- cinco perfis/overlays contrastantes;
- precedência;
- riscos e incertezas.

A próxima entrega é o Pacote P2:

> progressão, sequenciamento, espaçamento, revisão, exemplos e scaffolding.

P2 deverá consumir, entre outros:

- `practice.purpose`;
- `attempts.retry_target`;
- `hints.access`;
- `consequence.level`;
- perfil `self-directed-mastery`.

A Issue #4 permanece aberta até P2–P5 e a síntese final da taxonomia.
