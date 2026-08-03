# Enquadramento provisório do gênero da ARA — rodada 01

**Data local:** 2 de agosto de 2026  
**Issue:** #34  
**Estado:** enquadramento exploratório; não define a pergunta final de investigação

## 1. Problema de classificação

A busca inicial do programa partiu de flashcards, prática de recuperação, espaçamento, Anki e Quizlet. Esse recorte descreve uma configuração possível da ARA, mas não o gênero completo da plataforma.

A ARA pretende organizar cursos por microssequências e cards, coordenando representações estruturadas, atividades, respostas, validação e feedback. Conforme o componente usado, ela poderá sustentar desde recuperação simples até construção geométrica, execução de código, anotação de fontes, manipulação de modelos ou avaliação matemática semântica.

Por isso, classificá-la apenas como “plataforma de flashcards” produziria três distorções:

1. transformaria um formato de prática em identidade do sistema;
2. ocultaria representações e respostas específicas de domínio;
3. conduziria a pesquisa bibliográfica somente para produtos comerciais de repetição.

## 2. Gêneros vizinhos

### 2.1 Sistema de flashcards ou prática de recuperação

Caracteriza sistemas centrados em pares, prompts curtos, recuperação, repetição e agendamento. ARA pode oferecer esse perfil, mas não se reduz a ele.

**Relação com a ARA:** configuração pedagógica e família de atividades, não gênero abrangente.

### 2.2 Sistema de avaliação formativa computadorizada

Organiza tarefas, respostas, validação, pontuação e feedback. Numbas, STACK e Perseus demonstram várias formas desse gênero.

**Relação com a ARA:** dimensão central. Contudo, ARA também inclui organização curricular, teoria, exemplos, autoria e estudo autodirigido.

### 2.3 Ambiente interativo de aprendizagem

Combina conteúdo, ação do estudante e resposta do sistema. É uma categoria ampla, capaz de incluir manipulação, exploração, construção e feedback.

**Relação com a ARA:** categoria descritiva adequada, desde que “interativo” não seja usado como alegação de eficácia.

### 2.4 Ambiente ou ferramenta de autoria de recursos educacionais interativos

Permite que autores construam, validem, versionem e publiquem atividades. H5P, XBlock, Numbas e sistemas de autoria para tutores inteligentes pertencem parcialmente a essa família.

**Relação com a ARA:** dimensão central. A autoria por JSON estruturado, interface e integrações precisa ser considerada parte do artefato, não etapa externa.

### 2.5 Infraestrutura de recursos educacionais abertos interativos

Combina portabilidade, licenciamento, reutilização, adaptação e execução de objetos interativos.

**Relação com a ARA:** hipótese forte para o projeto aberto. Depende de contratos de licença, proveniência, exportação e compatibilidade ainda a definir.

### 2.6 Sistema tutor inteligente

Em geral, envolve modelo do domínio, modelo do estudante, estratégia tutorial e ciclo de adaptação/feedback. A literatura encontra efeitos médios favoráveis em vários contextos, mas a categoria é heterogênea e sensível ao comparador e ao resultado usado.

**Relação com a ARA:** não é categoria-base. Uma implantação poderá adquirir capacidades tutoriais quando possuir explicitamente modelos e políticas adaptativas. Recomendar o próximo card por regra simples não basta para reivindicar o gênero.

### 2.7 Sistema de aprendizagem adaptativa

Ajusta conteúdo, sequência, dificuldade ou apoio com base em dados e regras.

**Relação com a ARA:** capacidade opcional futura. Personalização escolhida pelo estudante e adaptação algorítmica devem permanecer distintas.

### 2.8 Ambiente de simulação ou laboratório virtual

Representa um modelo, permite manipular variáveis, observar mudanças e, eventualmente, testar hipóteses ou executar procedimentos.

**Relação com a ARA:** família opcional de componentes. Um gráfico animado ou controle visual não constitui simulação sem modelo e estado explícitos.

### 2.9 LMS ou ambiente virtual de aprendizagem

Administra cursos, turmas, inscrições, comunicação, entrega e acompanhamento institucional.

**Relação com a ARA:** a adoção institucional pode exigir funções próximas, mas a identidade principal permanece centrada em recursos, estudo, autoria e investigação. ARA não precisa reproduzir todo o escopo administrativo de um LMS.

### 2.10 Ambiente de aprendizagem multimídia

A literatura de aprendizagem multimídia estuda combinações de palavras, imagens e outras representações. “Multimídia” não significa obrigatoriamente vídeo.

**Relação com a ARA:** parte da fundamentação para coordenação representacional. O baseline textual e JSON pode combinar texto, notação, diagramas e visualizações sem produzir vídeo. Vídeo permanece fora do baseline.

## 3. Khan Academy e Perseus

Khan Academy é um ecossistema que reúne vídeos, textos, exercícios e outros recursos. Para esta investigação, o precedente mais próximo não é o catálogo de vídeos, mas o Perseus: sistema de exercícios com widgets tipados, entrada do estudante, validação, scoring e edição.

Isso sustenta duas conclusões:

1. a presença de vídeos numa plataforma não determina o gênero de seu sistema de exercícios;
2. uma arquitetura de atividades pode ser estudada separadamente da arquitetura de mídia.

ARA não precisa adicionar vídeo para ocupar um espaço semelhante de atividades interativas. Também não deve copiar a taxonomia de widgets do Perseus sem analisar domínios, acessibilidade, dependências e limitações.

## 4. Hipótese de gênero principal

O enquadramento provisório mais abrangente é:

> **ambiente aberto e configurável de aprendizagem e autoria de recursos estruturados e interativos**

Em inglês técnico de trabalho:

> **open configurable structured interactive learning and authoring environment**

Essa formulação é deliberadamente composta:

- **ambiente:** reúne percurso, conteúdo, atividade e estado;
- **aberto:** código e documentação possuem licenças abertas, sem presumir licença automática para todo conteúdo do usuário;
- **configurável:** decisões pedagógicas, de avaliação e de execução podem formar perfis explícitos;
- **aprendizagem:** suporta estudo autodirigido e institucional;
- **autoria:** permite construir e revisar recursos e cursos;
- **recursos estruturados:** conteúdo e respostas possuem semântica tipada;
- **interativos:** estudante produz ações e respostas que podem alterar estado ou receber validação.

Esse gênero não é uma categoria bibliométrica estabelecida. É uma hipótese descritiva de projeto que precisa ser refinada contra literatura e avaliação com usuários e especialistas.

## 5. Perfis que podem coexistir

Uma mesma plataforma pode materializar perfis distintos sem mudar de identidade:

| Perfil | Capacidades predominantes |
|---|---|
| recuperação e revisão | prompts, lacunas, escolhas, espaçamento |
| aprendizagem guiada | fundamentos, exemplos resolvidos, fading e feedback |
| avaliação formativa | respostas construídas, validadores e diagnóstico |
| programação | edição, execução, testes e depuração |
| matemática | entrada semântica, equivalência, unidades e construção geométrica |
| análise de fontes | seleção, anotação, evidência e argumentação |
| exploração científica | modelos, parâmetros, observações e simulações |
| autoria e investigação | variações, condições, instrumentação e exportação |

O gênero não deve ser inferido a partir de um único curso ou perfil.

## 6. Evidência acadêmica pertinente

A rodada exploratória identificou frentes que superam a literatura de flashcards:

- múltiplas representações externas e sua coordenação;
- sistemas tutores inteligentes e resultados de aprendizagem;
- ferramentas de autoria para sistemas tutoriais;
- avaliação computadorizada com respostas construídas;
- simulação e laboratórios virtuais;
- avaliação e feedback automáticos em programação;
- respostas textuais abertas;
- representação do conhecimento em ambientes digitais;
- representações específicas de química e outros domínios.

Essas literaturas não podem ser fundidas em uma única estimativa de eficácia. Elas oferecem funções diferentes:

- definir constructos;
- identificar moderadores e condições de fronteira;
- justificar requisitos disciplinares;
- sugerir formas de avaliação;
- revelar riscos de desenho;
- orientar protocolos empíricos.

## 7. O que a ARA ainda não é

Na fase atual, não se deve afirmar publicamente que ARA seja:

- um sistema tutor inteligente completo;
- uma plataforma adaptativa comprovada;
- um laboratório virtual;
- um LMS completo;
- uma plataforma multimídia;
- um sistema de avaliação automática geral;
- uma solução eficaz para qualquer domínio.

Essas categorias exigem capacidades e evidências próprias.

## 8. Implicações para a pesquisa bibliográfica

A estratégia passa a ter três níveis:

1. **gênero e arquitetura:** ambientes interativos, autoria, avaliação e componentes;
2. **mecanismos transversais:** feedback, exemplos, recuperação, espaçamento, controle do estudante e adaptação;
3. **gramáticas de domínio:** matemática, programação, química, física, línguas, humanidades, música, mapas, circuitos e aprendizagem profissional.

O corpus de flashcards permanece válido no segundo nível, mas não governa os outros dois.

## 9. Enquadramento para futuras dissertações

O tema final do mestrado não está definido. Este enquadramento permite perguntas diferentes, por exemplo:

- desenho e validação de uma arquitetura de recursos estruturados;
- autoria de atividades interativas por especialistas não programadores;
- comparação entre respostas selecionadas e construídas;
- estudo de microsequências configuráveis;
- acessibilidade de interações estruturadas em dispositivos móveis;
- uso da ARA como infraestrutura para desenho de investigação.

Nenhuma dessas possibilidades é escolhida nesta rodada.

## 10. Decisão de trabalho

Até revisão posterior, a documentação deve:

- evitar “plataforma de flashcards” como definição geral;
- usar “ambiente de recursos de aprendizagem” como nome institucional do projeto;
- empregar o gênero provisório acima em textos de pesquisa quando necessário;
- qualificar funções tutoriais, adaptativas, avaliativas ou simulacionais como capacidades específicas;
- separar afirmações sobre arquitetura de afirmações sobre aprendizagem.
