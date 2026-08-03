# Pacote P2 — progressão, sequenciamento, revisão, exemplos e scaffolding

**Versão:** 0.1  
**Data:** 3 de agosto de 2026  
**Issue:** #4  
**Estado:** pacote concluído; parâmetros aceitos para a primeira taxonomia, sujeitos à síntese final da Issue #4  
**Natureza:** síntese crítica e recomendação; não é algoritmo, schema de produção, contrato técnico, UX nem implementação

## 1. Conclusão principal

O ARA não deve possuir um único `progressionMode`, `masteryMode`, `reviewMode` ou `scaffoldingLevel`.

A literatura e o perfil funcional do AraLearn sustentam um modelo composto:

```text
semântica do estado
× modo de progressão
× evidência e critério
× escopo da alegação
× remediação, override e rechecagem
× autoridade e política de sequência
× pré-requisitos, ordem, ramificação e intercalação
× autoridade sobre ritmo
× gatilho, agenda e horizonte de revisão
× intervalo, carga, adiamento e item de revisão
× disponibilidade, posição e completude de exemplos
× tipo, acesso e fading de scaffolds
× segmentação
× estado, pista e apoio de retomada
```

Essas dimensões interagem, mas não são equivalentes.

- concluir um card não significa dominar um conceito;
- mastery não é um número universal de respostas corretas;
- ritmo do estudante não equivale a liberdade irrestrita de reordenar conteúdo;
- spacing distribui exposições no tempo; interleaving mistura categorias ou problemas para exigir discriminação;
- exemplo resolvido não substitui toda prática independente;
- fading não pode retirar informação essencial nem depender de um estimador não validado;
- interrupção não é evidência de desengajamento.

## 2. Caminho recomendado

### 2.1 Arquitetura conceitual da configuração

A primeira taxonomia deve aceitar as dimensões necessárias para descrever condições defensáveis e reproduzíveis. A primeira release não precisa expor todos os valores.

Recomenda-se:

1. preservar a conclusão estrutural do AraLearn como referência, explicitamente separada de mastery;
2. admitir progressão por critério em perfis formais, desde que evidência, critério, escopo, remediação, override e rechecagem sejam declarados;
3. tratar `mastery` como alegação contextual e versionada, não como estado natural do estudante;
4. separar autoridade sobre sequência de autoridade sobre ritmo;
5. adotar shared control como direção geral: autor organiza a estrutura; estudante controla ritmo e escolhas permitidas; instituição ou protocolo pode bloquear valores explicitamente;
6. separar temporal spacing de interleaving;
7. representar objetivo de retenção, agenda, intervalos, carga e adiamento, sem selecionar algoritmo universal;
8. usar interleaving quando houver objetivo discriminativo e plausibilidade de domínio, não como padrão geral;
9. oferecer exemplos e scaffolds de modo mais forte para novatos e tarefas complexas, com passagem para resolução independente;
10. tornar fading explícito, reversível e rastreável;
11. preservar segmentação semanticamente coerente e learner-paced como referência;
12. oferecer retomada determinística e não punitiva para estudo fragmentado;
13. adiar adaptação automática e inferência comportamental.

### 2.2 Perfil inicial derivado do AraLearn

No perfil `aralearn-reference`:

- `progression.mode = structural-completion`;
- estados de navegação não usam `mastered` ou `passed`;
- a sequência é autoral, com dependências declaradas e escolha do estudante sobre onde estudar;
- o ritmo é controlado pelo estudante;
- não há hard gate de mastery;
- revisão surge por colocação autoral ou marcação voluntária do estudante;
- não há scheduler adaptativo;
- exemplos e apoio são escritos pelo autor quando necessários;
- fading ocorre na composição didática, não por inferência de telemetria;
- microssequências e cards são segmentos coerentes;
- o cursor local permite retomar;
- ausência, tempo e retomada não são interpretados como esforço, dificuldade ou domínio.

Esse perfil continua sendo referência, não default universal para cursos formais, avaliações ou protocolos.

## 3. Método, corpus e suficiência

O protocolo está em:

- `research/searches/2026-08-03-p2-progressao-sequenciamento-revisao-protocolo.md`.

O corpus estruturado está em:

- `research/data/p2-evidence-corpus-01.csv`.

Foram integrados:

- AraLearn e o Pacote P1;
- meta-análises e revisões sobre mastery learning;
- learner control e pacing;
- spacing aplicado em sala e em ambientes digitais;
- spacing em aprendizagem de línguas;
- interleaving e seus moderadores;
- worked examples e fading;
- expertise reversal;
- computer-based scaffolding;
- segmentação;
- interrupção e retomada.

### 3.1 Saturação por frente

| Frente | Estado | Interpretação |
|---|---|---|
| mastery e progressão | alcançada para taxonomia inicial | suficiente para aceitar critérios, remediação, override e rechecagem; insuficiente para threshold universal |
| learner control e pacing | alcançada para decomposição | suficiente para separar ritmo, ordem, prática e revisão |
| spacing e revisão | alcançada para família paramétrica | suficiente para aceitar agenda, horizonte e carga; insuficiente para algoritmo |
| interleaving | alcançada para política opcional | benefício moderado e fortemente dependente de material e domínio |
| worked examples | alcançada para princípio de suporte inicial | recomendação forte para novatos em tarefas estruturadas, com necessidade de prática independente |
| scaffolding e fading | alcançada para família paramétrica | suporte possui benefício médio; fading não tem vencedor universal |
| segmentação | alcançada para default coerente e learner-paced | benefício pequeno a moderado, com custo de tempo |
| interrupção e retomada | suficiente para invariantes | preservação de estado e contexto é justificável; formato final depende de UX |

A suficiência é relativa à taxonomia. Não demonstra eficácia universal nem escolhe software.

## 4. AraLearn como configuração de referência

### 4.1 Unidade de progressão

No AraLearn, a microssequência reúne objetivo, dependências, conteúdos, verificações e cards ordenados. Ela ocupa uma escala intermediária entre card isolado e lição ampla.

Isso fornece uma configuração coerente:

- estrutura visível;
- dependências explícitas;
- continuidade autoral;
- etapas manejáveis no celular;
- prática dentro de um percurso.

A conclusão de card ou lição é estado funcional de continuidade. O documento de estado não punitivo proíbe inferir acerto, qualidade, nota ou aprendizagem.

### 4.2 Sequência e autonomia

A ordem é composta pelo autor, mas o estudante escolhe cursos, trilhas e etapas. O sistema não executa uma sequência adaptativa oculta.

Isso revela duas autoridades diferentes:

- **sequência:** estrutura e dependências;
- **ritmo:** quando continuar, pausar e retomar.

P2 preserva essa distinção.

### 4.3 Revisão

AraLearn possui:

- retomadas autorais ao longo da trilha;
- alternância planejada depois de estabelecer cada operação;
- marca pessoal `Rever`;
- cursor e estado local.

Não possui:

- fila espaçada automática;
- algoritmo de scheduling;
- due date pedagógico;
- mastery estimator;
- penalização por atraso;
- histórico de revisão.

### 4.4 Exemplos e apoio

O modelo didático recomenda exemplos resolvidos quando a operação é nova ou complexa, depois prática guiada e prática com menos apoio. A retirada de apoio não remove dados necessários do problema.

A regra é autoral e situada. P2 a transforma em dimensões explícitas sem afirmar que toda tarefa exige o mesmo padrão.

## 5. Mastery e progressão por critério

### 5.1 Mastery é um pacote, não uma flag

A meta-análise clássica de Kulik, Kulik e Bangert-Drowns [P2E03] sintetizou 108 avaliações e encontrou efeitos favoráveis de programas de mastery sobre desempenho e atitudes, frequentemente com maior benefício para estudantes inicialmente mais fracos. Também registrou maior tempo instrucional e problemas de conclusão em parte dos contextos self-paced.

A síntese de Cook et al. [P2E04] encontrou efeitos relevantes em simulação de profissões de saúde. Porém, os programas combinavam:

- padrões explícitos;
- repetição;
- feedback;
- tempo variável;
- prática adicional;
- tarefas e avaliações específicas.

Não é possível transferir esses resultados para um `mastery=true` sem descrever o tratamento.

A revisão de Pérez e Verdín [P2E05] mostra grande diversidade em engenharia, com múltiplas oportunidades de reavaliação, custos de trabalho docente e resultados mistos conforme a medida.

### 5.2 Threshold não é universal

Matayoshi et al. [P2E06] compararam dois thresholds em um sistema adaptativo. O limiar mais alto reduziu inicialmente o esquecimento, mas a diferença diminuiu com o tempo e variou por matéria e dificuldade vivida pelo estudante.

Implicações:

- threshold deve ter identidade e versão;
- precisa indicar qual evidência o alimenta;
- a janela de observação precisa ser conhecida;
- o horizonte de retenção importa;
- overpractice é risco;
- uma estimativa proprietária não é transferível automaticamente;
- `80%`, `90%` ou “três acertos” não podem ser defaults científicos universais.

### 5.3 Modelo recomendado

Separar:

- `progression.mode`;
- `progression.status_semantics`;
- `progression.evidence_basis`;
- `progression.criterion`;
- `progression.evidence_scope`;
- `progression.remediation_policy`;
- `progression.override_policy`;
- `progression.recheck_policy`.

Uma progressão criterion-gated só é válida quando responde:

1. o que se pretende declarar;
2. com qual evidência;
3. em qual conteúdo e horizonte;
4. sob qual regra;
5. que remediação existe;
6. quem pode contestar ou liberar;
7. quando a evidência será rechecada.

### 5.4 Regras de segurança

Rejeitar:

- conclusão estrutural como mastery;
- tempo como domínio;
- quantidade de tentativas como habilidade;
- hard lock irreversível;
- claim global derivado de um item local;
- rechecagem que apaga silenciosamente a história anterior.

## 6. Learner control, sequência e ritmo

### 6.1 Controle não é uma variável binária

A meta-análise de Karich, Burns e Maki [P2E07] encontrou efeito acadêmico médio próximo de zero para learner control em tecnologia educacional. A categoria reunia controles distintos.

Isso não implica retirar autonomia. Implica decompor:

- ritmo;
- ordem;
- escolha de prática;
- acesso a revisão;
- acesso a apoio;
- override;
- ramificação.

Tabbers e de Koeijer [P2E08] encontraram melhor transferência sob learner pacing em uma instrução multimídia, mas com aumento do tempo e diferenças individuais.

### 6.2 Shared control

A direção recomendada é:

```text
autor:
  coerência, dependências, caminhos recomendados, riscos

estudante:
  ritmo, pausa, retomada, revisão pessoal, escolhas permitidas

instituição:
  prazos, requisitos formais, consequências autorizadas

protocolo:
  condições bloqueadas para pesquisa

acessibilidade:
  override quando necessário para acesso equitativo
```

Learner pacing não autoriza automaticamente reordenar pré-requisitos. Author sequencing não autoriza coerção temporal.

### 6.3 Dimensões

- `sequencing.authority`;
- `sequencing.prerequisite_policy`;
- `sequencing.order_policy`;
- `sequencing.branching_policy`;
- `sequencing.interleaving_policy`;
- `sequencing.snapshot_policy`;
- `pacing.authority`;
- `pacing.deadline_policy`.

## 7. Spacing, revisão e carga

### 7.1 Evidência aplicada

Mawson e Kang [P2E10] incluíram 22 relatórios e 31 efeitos de contextos de sala, com efeito moderado em favor de prática distribuída (`d = 0,54`). O número reduzido de estudos limitou análises de moderadores.

Martinengo et al. [P2E11] encontraram benefícios em educação digital de profissionais de saúde, mas com heterogeneidade e risco de viés.

Kim e Webb [P2E12] encontraram efeitos médios a grandes em segunda língua; intervalos maiores favoreceram testes tardios, enquanto agendas equal e expanding não apresentaram vencedor estatístico geral.

Cepeda et al. [P2E28] demonstraram que o intervalo útil varia com o horizonte de retenção.

### 7.2 O que não se pode concluir

Não há base para:

- “revisar sempre amanhã, em sete e trinta dias”;
- expanding como default universal;
- equal spacing como default universal;
- uma fila sem limite;
- due date tratado como obrigação moral;
- atraso interpretado como desengajamento;
- algoritmo fechado apresentado como ciência em si.

### 7.3 Modelo recomendado

Separar:

- `review.trigger`;
- `review.schedule_policy`;
- `review.interval_pattern`;
- `review.target_horizon`;
- `review.load_budget`;
- `review.deferral_policy`;
- `review.item_relation`;
- `review.failure_policy`.

O perfil pessoal deve permitir:

- adiar;
- reduzir carga;
- pausar;
- revisar offline;
- escolher prioridade;
- manter progresso estrutural;
- receber feedback sem punição.

Cursos e protocolos podem restringir, mas precisam declarar consequência, autoridade e acomodação.

### 7.4 Relação entre itens

Repetir o mesmo item, usar uma instância equivalente e avaliar transferência não são a mesma evidência.

`review.item_relation` distingue:

- item idêntico;
- variante superficial;
- mesma operação com novos dados;
- item equivalente;
- discriminação entre conceitos;
- aplicação;
- transferência próxima;
- transferência distante.

Mastery não deve ser inferido somente de repetição literal.

## 8. Spacing e interleaving precisam permanecer separados

Chen, Paas e Sweller [P2E14] argumentam, após revisão de 119 estudos, que spacing e interleaving têm bases distintas.

- spacing: separa episódios no tempo;
- interleaving: alterna categorias ou tipos para apoiar seleção e discriminação.

Brunmair e Richter [P2E15] encontraram efeito médio moderado do interleaving, maior quando categorias semelhantes precisavam ser distinguidas. Blocking venceu em alguns materiais.

Firth, Rivers e Boyle [P2E16] também apontam benefício, mas com corpus predominantemente laboratorial.

Rowlandson e Simpson [P2E17] não encontraram vantagem em dois experimentos de sala com categorias matemáticas específicas.

### Recomendação

`sequencing.interleaving_policy` deve registrar:

- objetivo discriminativo;
- categorias envolvidas;
- similaridade;
- momento de introdução;
- relação com base já estabelecida;
- condição de pesquisa, se aplicável.

No perfil AraLearn, mantém-se `authored-after-foundation`: primeiro estabelecer cada operação; depois intercalar quando houver motivo.

## 9. Exemplos resolvidos e prática independente

### 9.1 Benefício para novatos

Sweller e Cooper [P2E18] mostraram que exemplos resolvidos podem reduzir busca ineficiente na aquisição inicial de álgebra.

Schwonke et al. [P2E19] encontraram benefícios de exemplos com fading mesmo contra condições de resolução apoiada.

Esses resultados sustentam exemplos como recurso didático importante, especialmente para:

- novatos;
- tarefas estruturadas;
- procedimentos novos;
- alta carga de busca;
- relações que precisam ser explicitadas.

### 9.2 Limite: exemplos não substituem fazer

Zeitlhofer e Zumbach [P2E20] encontraram desempenho superior de sequências que incluíam resolução ativa em relação a worked-examples-only, sem uma ordem mista universalmente dominante.

Portanto:

- exemplo é apoio, não resultado final;
- deve existir prática independente;
- posição e quantidade dependem de expertise e tarefa;
- explicação deve ser pertinente, não apenas texto longo;
- completion problems podem criar transição;
- exemplo não prova mastery.

### 9.3 Dimensões

- `examples.availability`;
- `examples.position`;
- `examples.completeness`;
- `examples.explanation_policy`.

## 10. Expertise reversal, scaffolding e fading

### 10.1 Expertise altera o valor do apoio

Tetzlaff et al. [P2E21] sintetizaram expertise-reversal effects. O apoio beneficia novatos de modo mais consistente que prejudica experts, com moderação por domínio e nível educacional.

A conclusão não é remover apoio cedo. É:

- declarar a condição de expertise;
- evitar redundância;
- permitir apoio opcional;
- não inferir expertise de comportamento sem validação;
- restaurar suporte quando necessário.

### 10.2 Scaffolding possui efeito médio, mas formas heterogêneas

Belland et al. [P2E22] sintetizaram 144 estudos e 333 outcomes em STEM problem-centered learning, encontrando efeito cognitivo positivo médio. A lógica de fading não surgiu como moderador universal claro.

Kim, Belland e Walker [P2E23] encontraram efeito pequeno a moderado em PBL STEM com abordagem bayesiana.

Renkl, Atkinson e Große [P2E24] demonstraram como completion problems e fading podem ligar exemplo e resolução.

### 10.3 Modelo recomendado

Separar:

- `scaffolding.type`;
- `scaffolding.access_policy`;
- `scaffolding.fading_policy`.

Tipos podem incluir:

- conceitual;
- procedural;
- estratégico;
- metacognitivo;
- representação;
- decomposição;
- pista;
- exemplo;
- apoio humano.

Acesso pode ser:

- sempre;
- a pedido;
- após erro;
- por oferta humana;
- por regra autoral;
- por protocolo;
- adaptativo candidato.

Fading pode ser:

- nenhum;
- fixo;
- completion;
- por expertise;
- por critério;
- controlado pelo estudante;
- controlado pelo autor;
- restaurável.

### 10.4 Proibições

- não retirar valores, dados ou condições indispensáveis;
- não usar tempo/hesitação como struggle sem validação;
- não ocultar que a condição de apoio mudou;
- não impedir restauração necessária à acessibilidade;
- não converter “menos ajuda” em pontuação moral.

## 11. Segmentação sem fragmentação

Rey et al. [P2E09] sintetizaram 56 investigações e 88 comparações. A segmentação significativa e coerente apresentou efeitos pequenos a médios sobre retenção e transferência, reduziu carga cognitiva e aumentou tempo de aprendizagem.

Isso sustenta a microssequência, mas não justifica:

- cards arbitrariamente mínimos;
- quebra de unidade sem contexto;
- microlearning como objetivo em si;
- progresso superficial por quantidade de telas.

Dimensões:

- `segmentation.policy`;
- `segmentation.control`.

Recomendação:

- segmentos semanticamente completos;
- dependências e objetivo visíveis;
- learner pacing;
- pausa e retorno;
- possibilidade de segmentos maiores para experts;
- system pacing apenas com justificativa, pausa e replay.

## 12. Interrupção e retomada

Monk, Trafton e Boehm-Davis [P2E25] mostraram que duração e demanda da interrupção aumentam o tempo de retomada.

Foroughi et al. [P2E26] encontraram maior custo de retomada após interrupções mais longas, especialmente entre participantes com menor capacidade de memória de trabalho.

Srivastava et al. [P2E27], em estudos piloto de leitura móvel, encontraram sinais de benefício de reviews/previews após interrupções, com limites de amostra e publicação.

### Invariantes aceitos

O ARA deve preservar:

- posição atual;
- estado funcional necessário;
- objetivo ou breadcrumb;
- conteúdo digitado quando seguro;
- próxima ação compreensível;
- operação offline.

Pode oferecer:

- retomar diretamente;
- revisão breve;
- preview do próximo passo;
- self-check;
- exemplo;
- escolha do estudante.

Não deve:

- inferir motivo da ausência;
- marcar atraso como fracasso;
- gerar remediação automática pela duração;
- coletar histórico apenas para “personalizar”;
- expor ausência a terceiros sem finalidade autorizada.

Dimensões:

- `resumption.state`;
- `resumption.context_cue`;
- `resumption.reentry_support`.

## 13. Parâmetros aceitos

P2 aceita 36 dimensões para a primeira taxonomia.

- **Progressão e mastery:** `progression.mode`, `progression.status_semantics`, `progression.evidence_basis`, `progression.criterion`, `progression.evidence_scope`, `progression.remediation_policy`, `progression.override_policy`, `progression.recheck_policy`.
- **Sequenciamento:** `sequencing.authority`, `sequencing.prerequisite_policy`, `sequencing.order_policy`, `sequencing.branching_policy`, `sequencing.interleaving_policy`, `sequencing.snapshot_policy`.
- **Ritmo:** `pacing.authority`, `pacing.deadline_policy`.
- **Revisão e espaçamento:** `review.trigger`, `review.schedule_policy`, `review.interval_pattern`, `review.target_horizon`, `review.load_budget`, `review.deferral_policy`, `review.item_relation`, `review.failure_policy`.
- **Exemplos resolvidos:** `examples.availability`, `examples.position`, `examples.completeness`, `examples.explanation_policy`.
- **Scaffolding:** `scaffolding.type`, `scaffolding.access_policy`, `scaffolding.fading_policy`.
- **Segmentação:** `segmentation.policy`, `segmentation.control`.
- **Retomada:** `resumption.state`, `resumption.context_cue`, `resumption.reentry_support`.

Os registros completos estão em:

`research/data/p2-parameter-records-01.csv`.

“Aceito” significa que a dimensão é conceitualmente necessária. Valores e implementação continuam seletivos e sujeitos a #6–#9.

## 14. Autoridade e precedência

Ordem recomendada:

```text
lei, segurança, ética e acessibilidade
> consentimento, retirada e direitos do participante
> protocolo de pesquisa aprovado
> política institucional válida
> configuração do autor
> preferência do estudante dentro do espaço permitido
> default do produto
> disponibilidade técnica
```

### Consequências

- ausência técnica nunca deve substituir silenciosamente valor configurado;
- acessibilidade pode exigir override;
- protocolo deve registrar exceção sem revelar informação sensível além do necessário;
- instituição não pode transformar conclusão estrutural em nota sem requisito;
- autor não pode ocultar hard gate;
- estudante controla ritmo no perfil pessoal;
- adaptive rule só recebe autoridade após pesquisa e decisão.

## 15. Perfis contrastantes

O arquivo completo é:

`research/data/p2-profile-comparison-01.csv`.

Perfis:

1. `aralearn-reference`;
2. `self-directed-guided`;
3. `formal-mastery-course`;
4. `summative-prerequisite-course`;
5. `research-locked-sequence`;
6. `novice-support-overlay`;
7. `expert-efficiency-overlay`;
8. `interruptible-mobile-overlay`.

Esses perfis mostram que o mesmo conteúdo pode operar sob condições diferentes sem fundir progressão, ordem, revisão e apoio.

## 16. Alternativas rejeitadas ou adiadas

### Rejeitadas como regra geral

- threshold universal;
- conclusão estrutural como mastery;
- hard gate universal;
- learner control indiferenciado;
- interleaving universal;
- intervalo universal;
- worked-examples-only;
- fading automático por estimativa não validada;
- remoção de informação essencial;
- fila obrigatória sem limite;
- penalização de adiamento em estudo pessoal;
- inferência de engajamento por interrupção;
- promessa de scheduler ótimo.

### Adiadas

- mastery estimator adaptativo;
- scheduler adaptativo;
- branching adaptativo;
- struggle detection;
- fading automático;
- resumo generativo de retomada.

O adiamento não é rejeição permanente. Ele impede que a taxonomia inicial se converta em engenharia sem validade e governança.

## 17. Riscos

- explosão combinatória;
- uso retórico de mastery;
- overpractice;
- abandono por locks ou workload;
- revisão coerciva;
- notificações que geram culpa;
- confusão entre spacing e interleaving;
- excesso de apoio ou retirada precoce;
- exemplos passivos;
- condições de pesquisa irreproduzíveis;
- vigilância por tempo e interrupção;
- acessibilidade tratada como exceção tardia.

## 18. Incertezas decisivas

Permanecem capazes de alterar defaults ou prioridades:

- thresholds por domínio e população;
- evidência válida de item equivalente;
- soft versus hard prerequisites;
- agenda realista para estudo multi-curso e offline;
- orçamento de revisão;
- impacto de adiamento;
- domínios favoráveis a interleaving;
- expertise reversal fora de STEM procedural;
- acessibilidade em smartphones modestos;
- apoio determinístico versus IA na retomada;
- workload docente em mastery;
- transferência para Brasil, Portugal e adultos trabalhadores.

Essas incertezas não impedem a decomposição paramétrica.

## 19. Handoff

### Para P3

- autoridade e learner control;
- expertise e adaptação;
- acesso e fading de scaffolds;
- accessibility overlays;
- limites de inferência;
- candidatos adaptativos adiados.

### Para P4 e Issue #5

- snapshots de sequência e condição;
- mastery claim e evidência;
- review schedule;
- missed/deferral semantics;
- eventos e inferências proibidas;
- struggle e expertise como constructos, não sinais brutos.

### Para Issue #6

- progressão estrutural versus criterion-gated;
- entidades de critério, remediação, override, revisão e perfil;
- capability classes de adaptação;
- lifecycle de snapshots e claims.

### Para Issue #7

- scheduler como hipótese;
- offline review queue;
- versionamento;
- execução de sequência;
- restauração de suporte;
- desempenho móvel;
- nenhum algoritmo selecionado.

### Para Issue #8

- apresentação de locks, critérios e caminhos;
- comparação de perfis;
- fila e adiamento;
- contexto de retomada;
- acesso e restauração de scaffolds;
- comunicação de mastery sem estigma.

## 20. Não autorizações

P2 não autoriza:

- algoritmo de mastery;
- scheduler;
- branching adaptativo;
- notifications;
- schema ou banco;
- coleta de eventos;
- interface de configuração;
- IA para gerar revisão ou resumos;
- detecção de struggle;
- alteração do kernel;
- biblioteca ou stack;
- implementação;
- nova issue.

## 21. Decisão

A evidência não apresenta conflito valorativo que exija escolha do proprietário nesta rodada.

Recomendação aceita para a continuação da Issue #4:

> preservar a progressão estrutural e a retomada não punitiva do AraLearn como referência; admitir mastery, revisão, sequência e apoio como dimensões explícitas e contextuais; usar shared control; normatizar spacing sem algoritmo universal; restringir interleaving a objetivos justificáveis; usar exemplos e scaffolding de modo expertise-sensitive, reversível e rastreável; adiar adaptação automática.

O próximo pacote é P3: autonomia, autorregulação, adaptação, acessibilidade e assistência por IA.
