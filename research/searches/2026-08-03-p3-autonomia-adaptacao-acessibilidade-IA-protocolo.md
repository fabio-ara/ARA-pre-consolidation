# Protocolo focado P3 — autonomia, autorregulação, adaptação, acessibilidade e assistência por IA

**Issue governante:** #4  
**Pacote:** P3  
**Data:** 3 de agosto de 2026  
**Idioma:** `pt-BR`  
**Estado:** concluído para a primeira taxonomia; não autoriza implementação.

## 1. Pergunta decisória

Como o ARA deve representar autonomia, apoio à autorregulação, adaptação, acessibilidade e assistência por IA sem:

- confundir autonomia com liberdade irrestrita;
- confundir adaptação com acomodação;
- inferir estados do estudante a partir de sinais inválidos;
- retirar autoridade humana;
- tornar a IA professora, avaliadora ou publicadora por padrão;
- exigir que o GPT ou o usuário declare todo o catálogo de parâmetros;
- comprometer acessibilidade, privacidade, offline, reprodutibilidade ou pesquisa comparativa?

## 2. Decisões que o pacote deve informar

P3 informa:

1. quais dimensões precisam existir na primeira taxonomia;
2. quais valores compõem o perfil AraLearn;
3. quais perfis contrastantes são necessários;
4. quem pode escolher, recomendar, bloquear, aplicar, contestar e desfazer configurações;
5. quais funções de IA podem ser representadas sem aceitar tecnologia, modelo ou provedor;
6. quais requisitos de acessibilidade possuem precedência;
7. quais candidatos devem ser adiados para P4, P5, #5, #6, #7 ou #8;
8. como o modelo de interação chat/MCP + ARA deve aparecer na visão do produto;
9. quais dados e inferências são proibidos antes do modelo de analytics.

## 3. Entradas obrigatórias do projeto

Foram tratadas como fontes internas:

- visão canônica do produto;
- Issue #4;
- síntese e parâmetros de P1;
- síntese e parâmetros de P2;
- auditoria do AraLearn;
- modelo didático e estado de estudo não punitivo do AraLearn;
- comentários recentes da Issue #4 sobre:
  - parâmetros transformadores de conteúdo;
  - microssequências versionadas e curso como composição;
  - materialização offline;
  - perfis, overrides esparsos e administração leiga;
  - dois canais de entrada: chat/MCP e ARA;
  - GPT construtor, auditor, reparador e usuário com maior controle.

As observações recentes foram tratadas como intenção de produto ou hipótese explícita, não como arquitetura já aceita.

## 4. Frentes de evidência

### F1 — autorregulação

- modelos de self-regulated learning;
- objetivos, planejamento, monitoramento, estratégia e reflexão;
- busca de ajuda e autoavaliação;
- intervenções digitais e online;
- diferenças por nível educacional e contexto.

### F2 — autonomia e learner control

- autonomia apoiada;
- learner control;
- shared control;
- advisement;
- escolha, ritmo, ordem e revisão como dimensões separadas;
- riscos de overload e abandono.

### F3 — adaptação

- intelligent tutoring systems;
- adaptive learning;
- learner models;
- evidência e moderadores;
- recomendação versus aplicação;
- transparência, override, rollback e fallback.

### F4 — acessibilidade e UDL

- WCAG 2.2;
- UDL Guidelines 3.0;
- desenho inclusivo;
- alternativas de percepção, ação e expressão;
- acomodação, equivalência e preservação de constructo;
- tecnologias assistivas;
- privacidade de dados de acessibilidade.

### F5 — IA para aprendizagem

- tutores generativos;
- efeitos positivos;
- danos por substituição de esforço;
- transparência e disclaimers;
- metacognição e self-explanation;
- assistência sob demanda.

### F6 — interação humano–IA

- automação e overreliance;
- cognitive forcing;
- editabilidade;
- contestabilidade;
- human oversight;
- explicações e confiança;
- falhas e incerteza.

### F7 — governança e risco

- UNESCO;
- NIST AI RMF;
- NIST GenAI Profile;
- limites de uso;
- documentação de finalidade, atores, riscos e avaliação.

### F8 — autoria GPT + MCP + ARA

- funções de IA;
- escopo de contexto;
- grounding;
- estados de saída;
- validação determinística;
- auditoria independente;
- revisão humana;
- reparo localizado;
- provenance;
- interface em tempo real;
- operações determinísticas do usuário.

## 5. Estratégia de busca

Foram usadas buscas por título, DOI, tema e domínio em fontes oficiais e acadêmicas.

Consultas representativas:

```text
self regulated learning online learning systematic review meta analysis
learner control educational technology meta-analysis
shared control adaptive learning technology
intelligent tutoring systems learning outcomes meta-analysis
technology enhanced adaptive learning moderators meta-analysis
generative AI without guardrails can harm learning
AI tutoring randomized controlled trial learning outcomes
learner LLM transparency disclaimers reliability
guidelines for human AI interaction
cognitive forcing overreliance AI
automation bias AI decision support empirical study
algorithm aversion user modification
CAST UDL Guidelines 3.0
WCAG 2.2 W3C Recommendation
UDL effectiveness systematic review meta-analysis
AI students learning disabilities systematic review
UNESCO generative AI education research guidance
NIST AI RMF 1.0
NIST Generative AI Profile
```

## 6. Fontes e estado de acesso

O corpus estruturado contém 34 fontes.

Estados usados:

- texto integral;
- texto integral oficial;
- manuscrito do autor;
- resumo e metadados;
- capítulo/resumo;
- padrão normativo;
- orientação oficial.

Nenhuma fonte foi tratada como lida integralmente quando apenas resumo ou metadados estavam disponíveis.

## 7. Amostragem

A amostra cobre:

- teoria de SRL;
- meta-análises;
- estudos de campo;
- intervenções em ITS;
- RCTs de GenAI;
- resultados positivos e negativos;
- HCI;
- acessibilidade;
- normas técnicas;
- orientações internacionais;
- estudantes, autores, professores, tutores, pesquisadores e instituições;
- ensino básico, secundário e superior;
- autoria e estudo.

Não pretende cobrir:

- toda aplicação de IA educacional;
- toda deficiência ou acomodação;
- toda legislação;
- toda técnica de adaptive learning;
- toda interface humano–IA;
- todo modelo de self-regulation.

## 8. Critérios de inclusão

Foram incluídas fontes que:

- definem constructos ou modelos necessários;
- sintetizam efeitos ou moderadores;
- testam controles, transparência ou assistência;
- documentam riscos;
- fornecem requisitos técnicos de acessibilidade;
- fornecem orientação oficial;
- contrastam benefícios e danos;
- informam diretamente um parâmetro, perfil ou não autorização.

## 9. Critérios de exclusão

Foram excluídos como base principal:

- páginas promocionais sem método;
- opiniões sem fonte;
- catálogos comerciais;
- rankings;
- resultados não relacionados à decisão;
- propostas puramente técnicas sem interação humana;
- notícias quando havia fonte primária;
- métricas de engajamento sem constructo;
- claims de “personalização” sem definição.

## 10. Critério de suficiência

P3 avançou quando:

1. todas as oito frentes continham fonte confiável;
2. havia resultados positivos e negativos sobre IA;
3. havia evidência contra learner control universal;
4. havia fontes que mostravam limites de human oversight e explicações;
5. acessibilidade possuía padrão técnico, framework educacional e pesquisa;
6. novos artigos já não alteravam a estrutura principal dos parâmetros;
7. as incertezas remanescentes eram de algoritmo, produto, domínio, arquitetura, UX ou avaliação;
8. a recomendação podia ser formulada sem selecionar tecnologia.

## 11. Regras de interpretação

- Correlação de estratégia com resultado não prova efeito causal.
- Metanálise de ITS não valida LLM.
- Resultado positivo de um tutor não autoriza IA autônoma.
- Resultado negativo de uma interface não rejeita toda IA educacional.
- UDL não é sinônimo de menu infinito de opções.
- WCAG não demonstra efetividade pedagógica.
- Human-in-the-loop não garante correção.
- Explicação não garante confiança calibrada.
- Confiança de modelo não é probabilidade de correção para o usuário.
- Assistência acessível não deve exigir diagnóstico público.
- Acomodação não é adaptação algorítmica.
- Preferência não é constructo.
- Uso de ajuda não é déficit.
- Interrupção, tempo ou tentativa não medem motivação.

## 12. Validação do pacote

O pacote deve satisfazer:

- corpus com acesso e limites;
- parâmetros sem duplicidade semântica deliberada;
- perfil AraLearn;
- perfis contrastantes;
- precedência;
- aceitos, adiados e rejeitados;
- decisão estruturada;
- handoffs;
- não autorizações;
- atualização da visão, programa de pesquisa, backlog e READMEs;
- ausência de código, schema, UI ou seleção de stack.

## 13. Não autorizações

P3 não autoriza:

- learner model;
- adaptive engine;
- LLM;
- provider;
- MCP tool;
- banco ou Storage;
- IndexedDB schema;
- telemetry;
- dashboard;
- interface;
- automática publicação;
- AI grading;
- fine-tuning;
- detecção de emoção, deficiência, expertise ou struggle;
- uso cruzado de cursos;
- implementação.

## 14. Saídas

- `research/data/p3-evidence-corpus-01.csv`;
- `research/data/p3-parameter-records-01.csv`;
- `research/data/p3-profile-comparison-01.csv`;
- `research/data/p3-decision-synthesis-01.json`;
- `research/pt-BR/p3-sintese-autonomia-adaptacao-acessibilidade-IA-01.md`;
- `research/library/referencias-autonomia-adaptacao-acessibilidade-IA.bib`;
- atualização dos três documentos principais e dos READMEs.
