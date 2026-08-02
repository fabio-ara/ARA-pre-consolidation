# Expansão do levantamento de sistemas relacionados

**Data:** 2 de agosto de 2026  
**Tipo:** ampliação de escopo e desenho de buscas formais  
**Estado:** consultas preparadas; resultados, contagens e exportações serão registrados em execuções subsequentes  
**Issue governante:** #3

## 1. Motivo da ampliação

O primeiro registro nominal incluiu Anki, Duolingo e SoloLearn. O relato do autor acrescentou:

- LingoDeer para estudo de chinês;
- Encode e Enki para aprendizagem de programação;
- MOOCs do IFRS em Moodle, com teoria mais extensa e questionários de alternativas;
- um semestre de estudo na UNIVESP, também com atividades e questionários em Moodle;
- outros aplicativos de programação, inclusive pagos, sem experiência satisfatória e ainda não identificados com segurança.

A busca não deve ser organizada apenas por marcas. As experiências indicam famílias de sistemas, mecanismos, formatos de conteúdo, contextos institucionais e casos de abandono que precisam ser investigados com terminologia mais ampla.

## 2. Separação das frentes

### Frente A — Flashcards gerais e repetição espaçada

Objetivo: mapear sistemas gerais, autoria de baralhos, recuperação, autoavaliação, agendamento e revisão.

Termos candidatos:

```text
flashcard*
"digital flashcard*"
"electronic flashcard*"
"computer-based flashcard*"
"spaced repetition system*"
"retrieval practice"
Anki
Quizlet
learner-generated
student-generated
teacher-generated
self-rating
```

### Frente B — Aplicativos especializados em línguas

Objetivo: mapear progressão curricular, vocabulário, gramática, escrita, pronúncia, produção, gamificação e aprendizagem móvel.

Termos candidatos:

```text
Duolingo
LingoDeer
"mobile-assisted language learning"
"mobile-assisted vocabulary learning"
language learning app*
vocabulary app*
Chinese learning app*
character learning
writing system
pronunciation practice
grammar instruction
gamification
adaptive practice
```

### Frente C — Aplicativos especializados em programação

Objetivo: mapear microconteúdo, questões, execução de código, feedback, projetos, transferência e aprendizagem autodirigida.

Termos candidatos:

```text
SoloLearn
Encode
Enki
Mimo
Programming Hub
Grasshopper
"programming learning app*"
"coding learning app*"
"mobile programming education"
"mobile-assisted programming learning"
"microlearning programming"
"self-directed programming learning"
"code execution"
"coding exercise*"
"programming practice"
```

Nomes ambíguos, como `Encode` e `Enki`, deverão ser combinados com termos de programação, educação ou aplicativo móvel para reduzir falsos positivos.

### Frente D — Moodle, MOOCs e cursos institucionais

Objetivo: investigar a relação entre exposição teórica, questionários, feedback, progressão, conclusão, certificação e governança institucional.

Termos candidatos:

```text
Moodle
MOOC*
"learning management system*"
"virtual learning environment*"
quiz*
"multiple-choice question*"
"formative assessment"
"immediate feedback"
self-paced
online course
higher education
institutional learning
course completion
dropout
```

Instituições e plataformas específicas serão pesquisadas como casos, mas os resultados serão interpretados no contexto de cada curso e configuração, não como propriedades universais do Moodle.

### Frente E — Satisfação, abandono e experiência negativa

Objetivo: mapear fatores de atrito, baixo valor percebido, abandono, arrependimento de compra e dificuldade de transferência para tarefas reais.

Termos candidatos:

```text
learning app* AND satisfaction
educational app* AND usability
learning app* AND abandonment
mobile learning AND dropout
programming app* AND frustration
programming app* AND usability
learning app* AND "continuance intention"
learning app* AND retention
paid learning app*
subscription AND educational app*
perceived value
purchase regret
```

A experiência negativa do autor será usada para gerar perguntas, não para classificar produtos não identificados.

## 3. Blocos transversais

Cada frente será combinada, conforme a base, com blocos relacionados a:

### População e contexto

```text
student*
learner*
adult learner*
self-directed learner*
higher education
vocational education
professional education
school*
university
workplace learning
```

### Resultados e processos

```text
learning outcome*
retention
transfer
achievement
engagement
motivation
self-regulation
self-efficacy
usability
satisfaction
continuance
completion
dropout
cognitive load
```

### Desenho e recursos

```text
feedback
attempt*
hint*
answer reveal
timing
grading
assessment
question format
microlearning
worked example*
practice
adaptive learning
learner control
gamification
offline
mobile-first
```

## 4. Bases e fontes previstas

A ordem inicial de execução será:

1. **PubMed/MEDLINE:** saúde, educação médica, flashcards, repetição espaçada e aplicativos;
2. **ERIC:** educação, avaliação, tecnologia educacional, línguas, MOOCs e LMS;
3. **ACM Digital Library:** aprendizagem de programação, interação, sistemas e UX;
4. **IEEE Xplore:** tecnologia educacional, mobile learning, sistemas adaptativos e programação;
5. **Scopus e Web of Science:** busca multidisciplinar e rastreamento de citações, conforme acesso;
6. **PsycINFO:** memória, recuperação, autorregulação, motivação e experiência, conforme acesso;
7. **SciELO, Redalyc e Portal de Periódicos CAPES:** produção brasileira e latino-americana;
8. **RCAAP e repositórios portugueses:** teses, dissertações e produção institucional;
9. **Google Scholar e busca web:** descoberta suplementar, literatura cinzenta e rastreamento, sem substituir bases formais;
10. **sites oficiais:** descrição atual dos produtos, termos, documentação e posicionamento, nunca como prova independente de eficácia.

## 5. Estratégias-piloto

### 5.1 Flashcards e mecanismos

```text
(flashcard* OR "digital flashcard*" OR "electronic flashcard*" OR
 "spaced repetition" OR "retrieval practice" OR Anki OR Quizlet)
AND
(learn* OR education OR student* OR instruction OR assessment)
```

### 5.2 Aplicativos de línguas

```text
(Duolingo OR LingoDeer OR "language learning app*" OR
 "mobile-assisted language learning" OR "mobile-assisted vocabulary learning")
AND
(learn* OR outcome* OR retention OR motivation OR engagement OR usability)
```

### 5.3 Aplicativos de programação

```text
(SoloLearn OR "Encode app" OR "Enki app" OR Mimo OR
 "programming learning app*" OR "coding learning app*" OR
 "mobile programming education")
AND
(learn* OR practice OR feedback OR self-directed OR usability OR transfer)
```

### 5.4 Moodle, MOOCs e questionários

```text
(Moodle OR MOOC* OR "learning management system*" OR
 "virtual learning environment*")
AND
(quiz* OR "multiple-choice question*" OR "formative assessment" OR feedback)
AND
(learn* OR completion OR engagement OR self-regulation OR achievement)
```

### 5.5 Experiência, satisfação e abandono

```text
("learning app*" OR "educational app*" OR "programming app*" OR
 "language learning app*")
AND
(usability OR satisfaction OR frustration OR abandonment OR dropout OR
 "continuance intention" OR "perceived value")
```

As strings serão adaptadas aos vocabulários controlados, sintaxe, campos e limites de cada base. Alterações após testes de sensibilidade serão preservadas, e não substituídas silenciosamente.

## 6. Dados obrigatórios em cada execução

Cada busca executada deverá registrar:

- identificador da execução;
- frente temática;
- base, plataforma e coleção;
- data e horário;
- string exata;
- campos pesquisados;
- vocabulário controlado;
- filtros e limites;
- quantidade total retornada;
- formato e nome do arquivo exportado;
- número de registros importados;
- duplicatas removidas;
- alterações de sensibilidade;
- observações sobre falhas, limitações ou acesso;
- responsável pela execução.

Nenhuma contagem será estimada ou reconstruída posteriormente sem identificação explícita.

## 7. Regras de triagem adicionais

Além dos critérios gerais do protocolo mestre:

- sistemas específicos serão incluídos quando contribuírem para descrever funcionalidades, experiência, adoção ou resultados;
- fontes oficiais serão classificadas como documentação do fornecedor;
- estudos produzidos, financiados ou divulgados pelo fornecedor terão procedência registrada;
- estudos sobre um aplicativo não serão generalizados automaticamente para seu domínio;
- estudos sobre Moodle serão ligados à configuração pedagógica concreta examinada;
- experiências pessoais não serão inseridas como resultados de pesquisa;
- nomes de aplicativos não recordados com segurança não serão publicados;
- insatisfação e abandono serão tratados como fenômenos dignos de pesquisa, não como falha moral do estudante.

## 8. Produtos esperados

A execução dessas frentes deverá produzir:

1. mapa de sistemas relacionados;
2. vocabulário controlado de características e mecanismos;
3. matriz produto–domínio–atividade–feedback–progressão–evidência;
4. síntese de estudos de experiência e usabilidade;
5. síntese sobre flashcards, recuperação e espaçamento;
6. síntese sobre aprendizagem móvel de línguas;
7. síntese sobre aprendizagem móvel de programação;
8. síntese sobre Moodle, MOOCs, teoria e questionários;
9. mapa de satisfação, abandono e continuidade;
10. implicações provisórias para a taxonomia de parâmetros da Issue #4.

## 9. Limites atuais

Este documento amplia e prepara o levantamento; não registra resultados formais nem contagens ainda não executadas. As características dos produtos adicionais devem ser verificadas em fontes oficiais e independentes antes de serem afirmadas como fatos. A memória do autor é preservada como antecedente situado e poderá ser refinada quando nomes, versões e períodos de uso forem recordados com segurança.