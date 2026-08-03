# Síntese integrada da configuração de referência do AraLearn e do horizonte externo — rodada 01

**Data:** 3 de agosto de 2026  
**Issue:** #30 (`[31] Synthesize the AraLearn reference configuration and the external possibility space`)  
**Natureza:** síntese decisória de pesquisa; não é contrato de produto, arquitetura ou autorização de implementação  
**Idioma canônico de trabalho:** `pt-BR`

## 1. Conclusão principal

A direção recomendada para ARA é uma **plataforma de aprendizagem, autoria e investigação configurável, com núcleo estrutural pequeno e capacidades tipadas governadas por camadas**, que preserve o AraLearn como primeira configuração funcional sem transformar suas escolhas em limites universais.

A pesquisa não sustenta nenhum dos dois extremos:

1. copiar o AraLearn e apenas acrescentar interruptores para suas escolhas atuais;
2. construir antes do produto uma plataforma universal de componentes, runtimes e gramáticas disciplinares.

O caminho recomendado é:

```text
núcleo educacional e operacional reconhecível
+ perfis e parâmetros explícitos
+ catálogos separados de representação, prática, instrumentos e capacidades
+ extensibilidade governada
+ sínteses decisórias antes de contratos e protótipos
```

A primeira taxonomia de #4 deve, portanto, incluir tanto:

- dimensões já materializadas ou fixadas no AraLearn;
- dimensões descobertas externamente, inclusive quando o AraLearn não possuir valor correspondente.

Porém, a descoberta de uma dimensão não significa que ela será implementada. Cada possibilidade deve percorrer estados de maturidade, receber uma recomendação e ser posteriormente aceita, adiada ou rejeitada.

## 2. Caminho recomendado

Recomenda-se organizar o produto futuro em cinco espaços conceituais, ainda não convertidos em contratos normativos:

1. **estrutura de aprendizagem e curso** — curso, módulo, lição, microssequência, card e relações de progressão;
2. **configuração pedagógica e de governança** — parâmetros, autoridade, precedência, condições de pesquisa, acessibilidade e políticas institucionais;
3. **conteúdo e representações** — recursos declarativos que preservam estruturas relevantes ao conhecimento;
4. **prática, resposta, validação e feedback** — tarefas do estudante e formas de produzir e avaliar evidência de aprendizagem;
5. **instrumentos e capacidades opcionais** — calculadoras, dicionários, analisadores, runtimes, simulações, serviços conectados, instrumentos de pesquisa e outras capacidades cuja presença depende do curso e do perfil de implantação.

Essa separação evita dois erros observados no desenvolvimento anterior:

- fazer uma representação carregar simultaneamente atividade, resposta, validação, runtime e governança;
- transformar qualquer instrumento especializado em obrigação do núcleo móvel e offline.

A taxonomia de #4 deve começar por configurações e políticas, enquanto #6 decidirá as entidades normativas e #7 decidirá a arquitetura e os mecanismos de extensão.

## 3. Fontes e método

### 3.1 Fontes internas principais

A síntese utilizou:

- `novas_diretrizes.md`, memória do primeiro brainstorming;
- `documento_visao_inicial_sucessor_aralearn.md`, documento-mestre inicial;
- auditoria canônica dos 18 `resources` do AraLearn;
- inventário de recursos e matriz de cobertura disciplinar;
- sínteses sobre recuperação, espaçamento, quizzes, formatos de resposta e feedback;
- matriz de sistemas, atividades, feedback, progressão e consequências;
- benchmark de 21 sistemas ou famílias de sistemas;
- mapa de 16 fontes acadêmicas sobre ambientes estruturados, múltiplas representações, avaliação, autoria, simulações e respostas abertas;
- enquadramento provisório do gênero da ARA;
- protótipos de contratos e adapters apenas como evidência exploratória e negativa.

As memórias privadas foram usadas somente para requisitos e intenções não sensíveis. Elementos biográficos sensíveis não foram reproduzidos.

### 3.2 Amostragem

Foi adotada amostragem intencional de variação máxima. A finalidade não foi estimar a prevalência de funcionalidades nem construir uma ontologia universal, mas revelar alternativas e tensões capazes de alterar o recorte do produto.

A amostra consolidada compreendeu:

- **literatura:** revisões e estudos centrais sobre recuperação, espaçamento, feedback, formatos de resposta, múltiplas representações, sistemas tutores, autoria, simulação, programação e texto aberto;
- **plataformas e sistemas:** 21 sistemas formalmente comparados, além de antecedentes situados como Anki, Duolingo, LingoDeer, SoloLearn, Mimo, Moodle e MOOCs;
- **domínios:** 16 cenários auditados no AraLearn e ao menos oito famílias epistemicamente contrastantes no benchmark externo;
- **stakeholders:** sete papéis analisados por cenário e documentação — sem alegação de entrevistas;
- **implantações:** uso pessoal, pesquisa gerenciada, ensino formal, autogerenciamento institucional, conteúdo confidencial e publicação aberta.

O arquivo `ara-representative-sampling-01.csv` registra a cobertura e o estado de saturação de cada estrato.

### 3.3 Critério de suficiência

A rodada foi considerada suficiente para recomendar a entrada em #4 porque:

- todos os estratos definidos na Issue #30 estão representados;
- foram encontrados casos contrastantes dentro dos estratos centrais;
- os acréscimos mais recentes passaram a repetir tensões já observadas — por exemplo, representação versus resposta, determinismo versus avaliação aberta e offline versus runtime conectado;
- as lacunas restantes são relevantes para decisões futuras, mas não alteram a recomendação de uma plataforma em camadas e extensível por capacidades governadas.

A saturação é **aproximada**, não definitiva. Não foi atingida para:

- evidência empírica direta de stakeholders além do autor;
- acessibilidade real de interações construtivas complexas;
- exigências específicas de cada instituição candidata;
- desempenho de capacidades avançadas em aparelho modesto;
- validade educacional de avaliação automatizada aberta por IA.

Essas incertezas não impedem iniciar a taxonomia; impedem aceitar prematuramente determinadas capacidades.

## 4. Eixo A — configuração de referência do AraLearn

### 4.1 Estrutura e progressão

O AraLearn materializa a gramática:

```text
projeto → curso → módulo → lição → microssequência → card
```

Na experiência de estudo, curso, módulo, lição, microssequência e card constituem a cadeia relevante. A microssequência é a unidade local de progressão, e o card é a unidade ordenada de conteúdo e interação.

A separação entre cards de teoria e prática é uma escolha estrutural forte da configuração de referência. Ela favorece autoria por IA, previsibilidade móvel e auditoria, mas ainda precisa ser tratada em #4 e #6 como ponto de partida empírico, não como eficácia comprovada.

**Classificação:** `reference-profile` e `structural-candidate`.

### 4.2 Sessões móveis e retomada

A configuração privilegia:

- estudo no smartphone;
- interrupção sem perda do ponto;
- progressão rápida;
- rolagem vertical quando necessária;
- conteúdo disponível offline;
- baixo atrito entre cards.

Esses aspectos respondem diretamente às condições de uso que originaram o produto. A pesquisa externa reforça que “mobile” não é apenas tamanho de tela: envolve contexto fragmentado, interação curta, conectividade e retomada.

**Classificação:** continuidade móvel e offline como `structural-candidate`; duração, segmentação e ritmo como `parameter-candidate`.

### 4.3 Prática de baixa consequência

A configuração permite responder, limpar, tentar novamente, revelar a resposta e avançar sem nota acumulada. Não há ranking ou penalização cumulativa.

A literatura diferencia recuperação, risco, nota, tentativas, feedback e obrigatoriedade. Portanto, o perfil AraLearn deve ser preservado, mas seus componentes não devem continuar fundidos numa única política.

**Parâmetros candidatos:** número de tentativas, revelação, penalização, contribuição para nota, obrigatoriedade, consulta, ajuda, momento do feedback e progressão após erro.

### 4.4 Estado de estudo e telemetria

O AraLearn registra cursor, conclusão estrutural, marca `Rever` e observação situada. Não registra tempo, tentativas, acertos ou erros.

Essa política protege contra inferências indevidas e reduz vigilância. Entretanto, ARA pretende suportar protocolos de pesquisa e instituições que podem necessitar de outros dados.

**Classificação:** minimalismo atual como `reference-profile`; coleta configurável e governada como `parameter-candidate` e `core-capability-candidate`; coleta irrestrita por padrão como `not-recommended`.

### 4.5 Recursos estruturados

O AraLearn implementa 18 recursos textuais e estruturados. Seus pontos fortes são:

- conteúdo JSON portável;
- schemas fechados;
- geometria calculada pelo renderer;
- validação determinística;
- composição conservadora;
- cobertura real de diversos domínios.

A riqueza representacional é maior que a riqueza das respostas. Muitos atos disciplinares são aproximados por lacuna ou escolha.

**Classificação:** princípio de representação estruturada como `structural-candidate`; cada recurso como `reference-profile` e candidato a revisão; catálogo atual como limite universal, `not-recommended`.

### 4.6 Respostas e validação

O baseline efetivo possui:

- lacuna literal com variantes enumeradas;
- escolha simples ou múltipla por conjunto exato;
- pequena prática estruturada específica de fluxo.

Não possui equivalência semântica, crédito parcial geral, construção livre, execução, rubrica aberta ou avaliação por LLM durante o estudo.

A evidência sobre formatos de resposta mostra que respostas selecionadas e construídas não são intercambiáveis. O formato afeta demanda, medição, possibilidade de adivinhação e feedback.

**Classificação:** lacuna e escolha como `reference-profile`; novos formatos determinísticos como `parameter-candidate` e `core-capability-candidate`; avaliação aberta automática como `research-only` ou `connected-capability-candidate`.

### 4.7 Feedback

O AraLearn possui feedback posterior e feedback local opcional por alternativa. O contrato ainda não representa independentemente todas as dimensões de conteúdo, timing, persistência e retry.

A síntese externa indica que feedback de resultado, resposta correta, elaboração, explicação de erro, pista e exemplo resolvido devem ser separados. Não há um timing universalmente superior.

**Classificação:** feedback estruturado como `structural-candidate`; suas dimensões como `parameter-candidate`.

### 4.8 Autoria, auditoria e reparo

A configuração combina:

- autoria estrutural por ChatGPT com MCP;
- operações delimitadas e schemas exatos;
- auditoria independente;
- reparo aprovado;
- reauditoria;
- assistência contextual granular;
- publicação explícita e autoridade humana.

Esse fluxo é uma contribuição central do predecessor e deve permanecer reconhecível. A pesquisa externa sobre autoria reforça que ferramentas para não programadores e contratos específicos precisam ser avaliados pela qualidade da autoria, não apenas pela validade técnica.

**Classificação:** `structural-candidate` e `core-capability-candidate`.

### 4.9 Observações e curadoria

Observações situadas por card permitem dúvida, possível erro, confusão, sugestão ou comentário. Elas servem como insumo para reparo, não como nota.

A ampliação para recurso, conjunto de cards, microssequência e estruturas maiores é coerente com o documento de visão.

**Classificação:** observação situada como `reference-profile`; escopo, fluxo, visibilidade e tratamento como `parameter-candidate`.

### 4.10 Publicação e governança

O AraLearn diferencia autoria privada, publicação e catálogo. O sucessor precisa atender também conteúdo pessoal, institucional, confidencial, público, comercial e experimental.

**Classificação:** publicação explícita e proveniência como `structural-candidate`; visibilidade, aprovação, retenção e direitos como `parameter-candidate` e `core-capability-candidate`.

## 5. Eixo B — possibilidades externas ausentes ou parciais

### 5.1 Configurações pedagógicas

A literatura e as plataformas revelam dimensões que não aparecem como políticas independentes no AraLearn:

- agenda fixa, algorítmica, protocolar ou controlada pelo estudante;
- progressão livre, por domínio, por conclusão, por desempenho ou por pré-requisito;
- feedback imediato, por conjunto ou posterior;
- pistas graduadas e retirada de apoio;
- exemplos resolvidos e problemas parcialmente resolvidos;
- avaliação diagnóstica, formativa e somativa;
- nota, crédito parcial e consequência acadêmica;
- julgamento de confiança;
- adaptação automatizada distinta de personalização escolhida;
- comparação social, colaboração e revisão por pares;
- condição experimental bloqueada distinta de preferência pessoal.

Essas dimensões devem entrar na descoberta de #4 mesmo quando o AraLearn não possuir valor correspondente explícito.

### 5.2 Formas de resposta e prática

Sistemas externos mostram respostas como:

- correspondência;
- ordenação;
- classificação;
- seleção de evidência;
- resposta numérica;
- expressão matemática;
- matriz;
- construção relacional ou geométrica;
- escrita e execução de código;
- anotação de fonte;
- resposta textual curta ou extensa;
- tarefas compostas e multipartes;
- interação com modelo ou simulação.

A recomendação não é incorporar todas ao núcleo. É distinguir:

- formatos simples e determinísticos com ampla reutilização;
- gramáticas de domínio justificadas;
- respostas abertas que exigem rubrica, humano ou assistência probabilística;
- interações dependentes de runtime.

### 5.3 Recursos e representações disciplinares

O benchmark evidencia estruturas que não podem ser representadas adequadamente apenas por texto ou por um grafo genérico:

- notação musical;
- mapas geográficos;
- moléculas tridimensionais;
- circuitos lógicos;
- construções geométricas;
- expressões matemáticas editáveis;
- simulações de fenômenos;
- fontes anotáveis;
- modelos manipuláveis.

Isso sustenta um catálogo extensível e a legitimidade de gramáticas de domínio, mas não a implementação antecipada de todas elas.

### 5.4 Instrumentos

As diretrizes e os sistemas comparados apontam instrumentos que devem ser conceitualmente separados de recursos do curso:

- calculadoras;
- dicionários e gramáticas;
- analisadores linguísticos;
- ambientes de código;
- visualizadores científicos;
- ferramentas de anotação;
- escalas, questionários, rubricas, entrevistas e diários de pesquisa;
- verificadores especializados.

Um instrumento pode ser usado durante estudo, autoria, avaliação ou pesquisa. Sua presença, permissão, rede, persistência e influência na validação podem tornar-se parâmetros ou políticas de capacidade.

### 5.5 Avaliação e autoridade

A pesquisa externa exige distinguir:

- validade sintática ou estrutural;
- correção determinística;
- satisfação parcial de critérios;
- feedback diagnóstico;
- avaliação humana;
- assistência probabilística;
- decisão institucional ou nota.

A principal recomendação é que autoridade nunca seja inferida do renderer ou do modelo de entrada. Entretanto, a forma final dessa separação pertence a #6 e #7.

### 5.6 Acessibilidade

Acessibilidade não pode ser um campo genérico anexado a um recurso. Precisa abranger:

- operação por teclado;
- alternativas a arrastar;
- leitura linear equivalente;
- estrutura semântica;
- reflow;
- anúncios de estado;
- linguagem e direção de escrita;
- contraste e movimento;
- acomodações que possam prevalecer sobre políticas de curso quando necessário.

A pesquisa ainda não sustenta quais interações avançadas são aceitáveis no primeiro recorte. Acessibilidade deve funcionar como requisito transversal e fonte de parâmetros.

### 5.7 Stakeholders e instituição

O AraLearn foi otimizado para um autor-estudante. ARA precisa também representar tensões de:

- professor que define política de curso;
- estudante que possui preferências e acomodações;
- pesquisador que bloqueia uma condição;
- participante que consente e pode retirar-se;
- revisor que não é autor;
- instituição que restringe IA, compartilhamento e localização de dados;
- administrador que precisa operar backup, restauração e atualização.

Esses papéis revelam parâmetros de autoridade e governança inexistentes ou apenas parciais no predecessor.

### 5.8 Perfis de implantação

A mesma semântica precisa atravessar:

- uso pessoal móvel e offline;
- pesquisa gerenciada;
- ensino formal;
- implantação institucional autogerenciada;
- conteúdo confidencial;
- publicação aberta.

A variedade de perfis não justifica produtos desconectados. Justifica capacidades e políticas explícitas.

## 6. Tensões decisórias

### 6.1 Simplicidade versus poder expressivo

Contratos pequenos favorecem MCP, validação e reparo. Gramáticas especializadas podem preservar melhor a epistemologia de um domínio. A solução recomendada é composição e carregamento seletivo de contratos, não um schema monolítico nem liberdade irrestrita.

### 6.2 Offline versus capacidades conectadas

O estudo básico deve permanecer viável offline. Algumas avaliações, fontes, runtimes ou serviços podem depender de rede. A solução recomendada é declarar disponibilidade, finalidade e fallback por capacidade e perfil, sem fingir equivalência quando ela não existe.

### 6.3 Controle do estudante versus política e pesquisa

A autonomia do estudante é central, mas cursos, instituições e protocolos podem bloquear valores. A taxonomia precisa representar autoridade, precedência, consentimento e acomodação, não apenas preferências.

### 6.4 Determinismo versus avaliação aberta

Determinismo é adequado a muitas práticas e reduz custo e ambiguidade. Não cobre toda evidência de aprendizagem. Respostas abertas devem ser admitidas como possibilidade, mas sua autoridade precisa ser humana, rubricada ou probabilística de forma explícita.

### 6.5 Núcleo estável versus extensibilidade

Um núcleo cheio de todos os campos possíveis repetiria o contrato monolítico. Um ecossistema de código arbitrário ampliaria segurança e manutenção. A solução recomendada é um núcleo coeso e capacidades tipadas, aprovadas e versionadas, com arquitetura final a decidir em #7.

### 6.6 Analytics versus privacidade

Eventos ricos permitem pesquisa e intervenção, mas podem produzir vigilância e inferências indevidas. Cada protocolo deve declarar pergunta, evento, fórmula, retenção, acesso e inferências proibidas.

### 6.7 Experiência pessoal versus adoção institucional

A simplicidade do uso pessoal não deve ser perdida por causa de governança institucional. Funções avançadas devem aparecer por perfil, capacidade e revelação progressiva.

## 7. Alternativas consideradas

### Alternativa A — AraLearn parametrizado apenas por decomposição

**Decisão:** não recomendada.

Preservaria simplicidade e reduziria risco técnico, mas limitaria o espaço de possibilidades às escolhas já feitas pelo autor e às práticas `gap`/`choice`. Não atenderia à finalidade acadêmica de investigar configurações distintas nem a necessidades disciplinares e institucionais ainda ausentes.

### Alternativa B — plataforma universal de componentes antes do domínio

**Decisão:** adiada e não recomendada como rota atual.

Ampliaria a cobertura potencial, mas produziria contratos complexos, custos móveis, riscos de segurança e dependências antes de haver requisitos e prioridades. A sequência #36–#42 mostrou como cada protótipo cria novas pendências sem provar valor de produto.

### Alternativa C — núcleo AraLearn reconhecível com extensibilidade governada por camadas

**Decisão:** recomendada.

Combina continuidade empírica, descoberta externa, parametrização, pesquisa reproduzível e capacidade futura de expansão. Permite que #4 descubra parâmetros amplos, #6 escolha o domínio e #7 compare arquiteturas sem congelar prematuramente uma stack.

### Alternativa D — adotar um ecossistema existente como H5P, Moodle ou Open edX

**Decisão:** não recomendada como identidade arquitetural; manter como precedentes ou integrações futuras.

Esses sistemas oferecem capacidades maduras, mas trazem modelos, dependências, segurança, mídia e operações que não correspondem necessariamente ao núcleo móvel, autoral e offline do ARA.

## 8. Recomendação de classificação inicial

### 8.1 Preservar como perfil de referência

- curso → módulo → lição → microssequência → card;
- teoria e prática separadas;
- estudo móvel, retomável e offline;
- baixa consequência, tentativas livres e resposta revelável;
- recursos estruturados;
- validação determinística onde aplicável;
- observações situadas;
- autoria por MCP;
- auditoria, reparo e reauditoria;
- publicação explícita;
- telemetria mínima.

Preservar como perfil não significa universalizar.

### 8.2 Levar à #4 como famílias prioritárias de parâmetros

- granularidade e extensão;
- sequenciamento e progressão;
- prática e formato de resposta;
- tentativas, ajuda, consulta e revelação;
- feedback em conteúdo, timing e persistência;
- risco, nota, crédito parcial e consequência;
- exemplos, pistas, apoio e retirada de apoio;
- recuperação, revisão, espaçamento e intercalação;
- autonomia, autoridade, precedência e locking;
- acessibilidade e acomodação;
- IA em autoria, reparo, feedback e avaliação;
- fontes, proveniência e confiança;
- observações, revisão e publicação;
- instrumentos autorizados;
- coleta, retenção, visualização e interpretação de analytics;
- idioma, variante e terminologia institucional;
- visibilidade, confidencialidade e compartilhamento.

### 8.3 Considerar para o núcleo funcional, sem autorizar implementação ainda

- importação e estudo de cursos portáveis;
- aplicação de configuração efetiva;
- práticas determinísticas além de lacuna e escolha, especialmente correspondência, ordenação, classificação, identificação de erro, resposta numérica e resposta curta delimitada;
- feedback configurável;
- observação e reparo;
- proveniência básica;
- instrumentação governada;
- declaração de capacidade disponível ou indisponível.

### 8.4 Considerar como extensões ou capacidades opcionais

- entrada e validação matemática semântica;
- construção de grafos, geometria e circuitos;
- execução de código;
- anotação livre de fontes;
- mapas;
- música;
- moléculas e visualização científica;
- simulações;
- TTS, áudio, fala e pronúncia;
- avaliação textual por rubrica, humano ou assistência probabilística;
- ferramentas externas especializadas.

A prioridade entre essas famílias deve ser determinada por cursos e perguntas de pesquisa concretos.

### 8.5 Não recomendar

- código arbitrário fornecido pelo curso;
- geometria de renderer como conteúdo canônico por padrão;
- avaliação aberta por LLM apresentada como verdade determinística;
- conexão obrigatória para a progressão básica;
- coleta total de eventos por padrão;
- catálogo universal implementado antes de necessidade;
- dashboard analítico monolítico;
- migração automática dos contratos experimentais 0.2 para o domínio do produto.

## 9. Handoff recomendado para a Issue #4

A #4 deve receber quatro conjuntos, não um único catálogo plano:

1. **perfil AraLearn:** valores atuais e implícitos;
2. **parâmetros externos recorrentes:** dimensões suficientemente definidas para modelagem;
3. **candidatos imaturos:** possibilidades que exigem melhor definição ou evidência;
4. **capacidades dependentes:** dimensões que só fazem sentido quando determinada extensão estiver instalada ou autorizada.

Cada registro deverá indicar:

- relação com AraLearn;
- fonte de descoberta;
- maturidade;
- mecanismo ou finalidade;
- valores alternativos;
- autoridade e precedência;
- riscos e confounds;
- requisitos de instrumentação;
- classificação recomendada;
- decisão posterior.

A primeira versão da taxonomia não precisa aceitar todos os candidatos. Deve ser ampla na descoberta e seletiva na normatização.

## 10. Riscos relevantes

- **sobrecarga de configuração:** um formulário completo pode tornar-se incompreensível se não houver perfis, recomendações e revelação progressiva;
- **explosão combinatória:** parâmetros independentes podem interagir e produzir condições inválidas;
- **MCP hostil:** contratos excessivamente compostos podem aumentar falhas e reparos;
- **fragmentação de extensões:** gramáticas numerosas podem dificultar manutenção e autoria;
- **vigilância:** pesquisa e analytics podem superar a finalidade declarada;
- **adoção institucional:** requisitos de segurança e privacidade podem variar por jurisdição e organização;
- **acessibilidade tardia:** extensões visuais ou construtivas podem ser inviáveis se acessibilidade for tratada depois;
- **falsa universalidade:** amostragem ampla pode ser confundida com cobertura completa;
- **recorte insuficiente:** postergar demais as decisões pode impedir a construção de uma prova de conceito.

## 11. Incertezas que podem alterar a recomendação

As seguintes incertezas podem mudar o recorte, mas não a direção geral:

1. testes com stakeholders podem revelar que a parametrização extensa deve ser mediada por perfis muito mais fortes;
2. testes de MCP podem mostrar que determinados modelos compostos precisam ser divididos em operações menores;
3. benchmarks no Galaxy A07 podem obrigar a separar capacidades por pacotes ou perfis de implantação;
4. requisitos da CETESB, IFSP ou Universidade de Lisboa podem alterar identidade, armazenamento, consentimento ou integrações;
5. um curso ou recorte de dissertação pode tornar uma capacidade avançada prioritária;
6. avaliações de acessibilidade podem excluir ou reformular interações construtivas específicas.

Não há, nesta rodada, conflito estratégico que exija escolha imediata do autor. A recomendação em camadas é dominante sobre as alternativas examinadas.

## 12. Limitações

- não foram realizadas entrevistas ou testes novos com stakeholders;
- a literatura externa possui profundidade de acesso desigual e não forma uma revisão sistemática única;
- os 21 sistemas foram amostrados por contraste e disponibilidade de fonte aberta, não por representatividade estatística;
- alguns domínios, como música, geografia e química submicroscópica, aparecem principalmente como precedentes técnicos;
- os protótipos de componentes não medem valor pedagógico;
- nenhum runtime externo foi executado nesta rodada;
- a síntese recomenda direção e classificação, mas não substitui #4, #6 ou #7.

## 13. Decisão da rodada

**Recomendação aceita como saída de pesquisa:** iniciar a Issue #4 com uma taxonomia de descoberta ampla e maturidade explícita, usando o AraLearn como primeiro perfil e o horizonte externo como fonte equivalente de dimensões.

A rota de produto recomendada é a Alternativa C: núcleo reconhecível, parametrização explícita e extensibilidade governada por camadas.

Nenhum novo contrato, adapter, runtime ou recurso é autorizado por esta síntese.