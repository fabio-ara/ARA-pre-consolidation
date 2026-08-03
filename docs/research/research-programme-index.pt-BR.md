# Índice canônico do programa de pesquisa

**Estado:** canônico para planejamento de pesquisa  
**Idioma:** `pt-BR`  
**Última revisão:** 3 de agosto de 2026

## 1. Finalidade

Este índice organiza a pesquisa necessária para definir o ARA sem transferir ao proprietário o trabalho de interpretar um corpus bruto.

Cada frente deve resultar em:

- conclusão principal;
- caminho recomendado;
- alternativas relevantes;
- alternativas rejeitadas ou adiadas;
- justificativa;
- riscos;
- incertezas que possam alterar a recomendação;
- implicações para parametrização, produto, arquitetura, UX ou avaliação.

A pesquisa é ampla e finita. O objetivo é evidência suficiente para decidir, não exaustão universal.

## 2. Estados de cobertura

| Estado | Significado |
|---|---|
| `baseline-concluído` | Já existe síntese suficiente para iniciar modelagem de candidatos, com limitações registradas. |
| `parcial` | Há evidência útil, mas falta uma síntese focada para decisão normativa. |
| `exploratório` | Existem precedentes ou literatura inicial, insuficientes para decisão. |
| `não-iniciado` | A frente precisa de protocolo e corpus próprios. |
| `contínuo` | A pesquisa permanece aberta e é atualizada quando novas decisões exigirem. |

## 3. Evidência já produzida

### 3.1 Prática de recuperação, flashcards, quizzes e espaçamento

**Estado:** `baseline-concluído` para descoberta de parâmetros; `parcial` para padrões e algoritmos.

Fontes do projeto:

- Issue #14 / PR #15;
- buscas e corpus das Issues #16, #24, #26 e #28;
- sínteses e datasets em `research/`.

Decisões que já podem avançar:

- separar produto, mecanismo, formato e agenda;
- registrar resposta exigida;
- distinguir recuperação, repetição, nota e consequência;
- modelar objetivo temporal e autoridade sobre o agendamento.

Pesquisa adicional necessária antes de padrão normativo:

- algoritmos e controle de revisão;
- adultos trabalhadores;
- Brasil e Portugal;
- transferência e retenção tardia;
- carga de revisão, adiamento e abandono.

### 3.2 Formatos de resposta e feedback

**Estado:** `baseline-concluído` para primeira taxonomia; `parcial` para domínios e respostas abertas.

Fontes:

- Issue #17 / PR #19;
- literatura estruturada de resposta e feedback;
- benchmark externo e auditoria do AraLearn.

Dimensões candidatas:

- reconhecimento, recordação, resposta curta, explicação, resolução e execução;
- validade, correção, crédito parcial e revisão humana;
- conhecimento do resultado, resposta correta, elaboração, pista e exemplo;
- timing, retry, reveal e persistência.

Lacunas:

- respostas abertas e rubricas;
- equidade e validade de avaliação automática;
- feedback adaptado a erro;
- interação com conhecimento prévio e complexidade.

### 3.3 Programação móvel e feedback automatizado

**Estado:** `parcial`.

Fontes:

- Issue #18 / PR #20;
- Coelho et al. e atualização 2023–2026;
- benchmark de sistemas;
- experimentos históricos #36–#41.

Contribuições:

- distinguir ler, prever, completar, escrever, executar, depurar e projetar;
- não equiparar execução a aprendizagem;
- separar tests, static analysis, diagnóstico, rubrica e revisão.

Lacunas:

- aprendizagem e transferência em adultos;
- segurança e custo por perfil;
- acessibilidade móvel;
- ambientes avançados;
- papel de IA generativa.

Programação executável permanece candidata a extensão, não requisito do primeiro recorte.

### 3.4 Representações múltiplas e resources estruturados

**Estado:** `exploratório` com forte material comparativo.

Fontes:

- auditoria AraLearn #31 / PR #32;
- benchmark #33/#34 / PR #35;
- literatura de representações múltiplas e ambientes interativos;
- síntese #30 / PR #43.

Contribuições:

- mais tipos não significam melhor aprendizagem;
- representação, atividade, resposta e feedback devem ser distinguíveis;
- gramáticas de domínio podem ser legítimas;
- coordenação e redundância exigem suporte.

Pesquisa necessária:

- seleção e coordenação de representações;
- autoria por schemas;
- acessibilidade de visualizações;
- resource versus prática/instrumento/capacidade;
- critérios para catálogo inicial e extensão.

A decisão final pertence às Issues #6 e #7, após parâmetros relevantes.

### 3.5 Sistemas, gêneros e extensibilidade

**Estado:** `exploratório` suficiente para excluir extremos, insuficiente para arquitetura.

Fontes:

- Issues #33 e #34 / PR #35;
- 21 sistemas e 16 fontes acadêmicas;
- histórico #36–#42.

Conclusões úteis:

- ARA não é apenas flashcards;
- não deve reivindicar ITS, LMS, simulação ou avaliação geral sem capacidades próprias;
- extensibilidade precisa de governança;
- plugins arbitrários ampliam segurança, operação e acessibilidade.

Lacunas:

- modelos de kernel e packages;
- versionamento e descoberta;
- extensão segura;
- carregamento seletivo por MCP;
- manutenção e migrações;
- comparação de stacks.

Essas decisões são posteriores a #6.

## 4. Pacotes da primeira taxonomia — Issue #4

A Issue #4 deve ser executada em pacotes sucessivos, com uma síntese integrada final. Esses pacotes são subdivisões operacionais da issue, não novas issues automáticas.

### Pacote P1 — prática, resposta, tentativas, revelação, feedback e consequências

**Pergunta:** como descrever condições de prática e resposta sem confundir mecanismo, avaliação e consequência?

Evidência existente:

- forte baseline em #14 e #17;
- corpus formal e síntese de #30;
- exemplos de AraLearn e plataformas externas.

Pesquisa focada necessária:

- retry e error correction;
- answer reveal e geração de erro;
- consequências, notas e stakes;
- relações entre formato de resposta, feedback e aprendizagem;
- acessibilidade das respostas.

Entrega:

- registros de parâmetros candidatos;
- perfil AraLearn;
- modelos alternativos;
- recomendação de primeira versão;
- candidatos aceitos, adiados e rejeitados.

### Pacote P2 — progressão, sequenciamento, espaçamento, revisão, exemplos e scaffolding

**Pergunta:** quem controla a sequência, quando o estudante avança e como apoio e revisão são distribuídos?

Evidência existente:

- espaçamento e quizzes no corpus inicial;
- experiência AraLearn;
- literatura inicial de worked examples e feedback.

Pesquisa focada necessária:

- mastery/progression;
- learner pacing;
- spacing/interleaving;
- worked examples, fading e hints;
- carga cognitiva e segmentação;
- recuperação após interrupção.

Entrega:

- famílias de progressão e revisão;
- regras de autoridade e precedência;
- perfis contrastantes;
- recomendações para o primeiro produto.

### Pacote P3 — autonomia, autorregulação, adaptação, acessibilidade e assistência por IA

**Pergunta:** como separar escolha do estudante, acomodação, política institucional, condição experimental e adaptação algorítmica?

Evidência existente:

- parcial e dispersa;
- experiência AraLearn;
- mapa de sistemas e requisitos da visão.

Pesquisa focada necessária:

- self-regulated learning;
- learner control;
- adaptive learning;
- accessibility accommodations;
- neurodiversidade e condições de uso;
- IA em hints, explicação, autoria e revisão;
- riscos de dependência, erro e autoridade.

Entrega:

- parâmetros e precedência;
- limites de adaptação;
- políticas de transparência e override;
- recomendações de IA por função.

### Pacote P4 — instrumentação, condições experimentais, analytics e governança

**Pergunta:** o que precisa ser configurável para pesquisa, sem transformar o sistema em vigilância?

Evidência existente:

- baseline conceitual na #5 e na visão;
- cautelas do corpus sobre outcomes e inferência.

Pesquisa focada necessária:

- learning analytics;
- event vocabularies;
- research protocols;
- consent, pseudonymization, withdrawal e retention;
- métricas e constructos;
- personal analytics;
- interoperabilidade e exportação;
- ética e legislação aplicável.

Entrega:

- parâmetros de instrumentação;
- autoridade e consentimento;
- proibições de inferência;
- handoff para Issue #5.

### Pacote P5 — autoria, revisão, reparo, publicação e políticas institucionais

**Pergunta:** como configurar quem pode gerar, editar, revisar, aplicar e publicar, inclusive por agentes?

Evidência existente:

- experiência AraLearn e MCP;
- histórico de fluxos administrativos;
- literatura inicial de authoring tools.

Pesquisa focada necessária:

- human-AI authoring;
- quality assurance;
- provenance e source anchoring;
- revisão por pares e especialistas;
- permissões e workspaces;
- publicação, versionamento e retirada;
- ambientes institucionais.

Entrega:

- parâmetros de autoria e governança;
- perfis pessoais e institucionais;
- limites de autoridade do agente;
- requisitos candidatos para #6.

## 5. Frentes posteriores à taxonomia

### Issue #5 — protocolos, instrumentos e analytics

Pacotes previstos:

- modelos de pesquisa;
- participantes e consentimento;
- condições e assignment;
- instrumentos quantitativos e qualitativos;
- eventos e medidas;
- interpretação e inferências proibidas;
- exportação e equivalência entre implantações.

Cada pacote exigirá literatura metodológica própria.

### Issue #6 — produto e domínio

Pesquisa necessária:

- domain-driven design e modelagem de sistemas educacionais;
- autoria e lifecycle de conteúdo;
- versionamento e proveniência;
- bibliotecas e organização;
- colaboração e papéis/capacidades;
- portabilidade e interoperabilidade;
- requisitos institucionais.

A Issue #6 não deve ser apenas uma sessão de modelagem técnica: decisões de domínio pedagógicas, administrativas e de pesquisa precisam de ancoragem.

### Issue #7 — arquitetura e stack

Pesquisa técnica comparativa necessária:

- arquiteturas modulares e plugin/package systems;
- web/mobile/offline;
- sincronização local-remota;
- schemas e contratos;
- carregamento dinâmico;
- MCP e agent tooling;
- segurança de extensões e runtimes;
- deployment managed/self-hosted;
- observabilidade, backup e atualização;
- stacks candidatas e custos.

Saída: recomendações e ADRs, não catálogo bruto de tecnologias.

### Issue #8 — UX/UI

Pesquisa necessária:

- mobile learning UX;
- progressive disclosure;
- configuração complexa;
- accessibility e assistive technology;
- interruption recovery;
- authoring interfaces;
- research/admin UX;
- multilingual design;
- usability and comprehension methods.

### Issue #9 — releases e implementação

Pesquisa e boas práticas necessárias:

- release slicing;
- trunk/branch strategy;
- CI/CD;
- quality gates;
- security and accessibility testing;
- migration and rollback;
- evidence packages;
- open-source contribution governance.

## 6. Critérios gerais de suficiência

Uma frente pode avançar para recomendação quando:

1. possui pelo menos uma síntese confiável ou conjunto justificado de fontes primárias;
2. contém casos contrastantes e limites;
3. cobre os stakeholders e contextos relevantes à decisão;
4. não surge nova categoria decisiva após duas adições sucessivas ao corpus;
5. incertezas remanescentes estão explícitas;
6. a recomendação pode ser alterada futuramente sem destruir silenciosamente rastreabilidade;
7. nenhuma fonte inacessível indispensável está sendo substituída por suposição.

## 7. Papel de Fabio

Fabio deverá receber:

- síntese;
- recomendação;
- justificativa;
- alternativas relevantes;
- riscos;
- incertezas decisivas.

Não deverá receber como produto final:

- lista extensa de artigos sem integração;
- catálogo de plataformas sem recomendação;
- formulário de centenas de parâmetros sem priorização;
- pergunta genérica para decidir arquitetura sem análise.

Sua decisão será solicitada quando evidência e análise não resolverem conflito estratégico ou valorativo.

## 8. Próxima entrega verificável

A próxima entrega é o **Pacote P1 da Issue #4**, seguido pelos demais pacotes e por uma síntese final da taxonomia.

P1 deverá produzir:

- protocolo de pesquisa focado;
- corpus e registro de fontes;
- síntese crítica;
- parâmetros de prática, resposta, tentativa, revelação, feedback e consequência;
- valores AraLearn e alternativas externas;
- autoridade, precedência e conflitos;
- perfis contrastantes;
- recomendações aceitas, adiadas e rejeitadas;
- arquivo estruturado reutilizável pela Issue #5 e pela Issue #6.

Nenhum código, schema de produção, adapter ou UX será implementado nessa entrega.