# Protocolo inicial — perfis modulares de agente, curadoria participativa e analytics assistidos por IA

**Data da busca exploratória:** 4 de agosto de 2026  
**Estado:** protocolo de revisão de escopo inicial; execução parcial documentada  
**Idioma de trabalho:** `pt-BR`  
**Relação:** informa a nova frente de pesquisa sobre configuração modular de agentes, conhecimento por domínio, observações participativas, diffs e analytics quantitativos/qualitativos.

## 1. Objetivo

Mapear evidência e precedentes suficientes para decidir se o ARA deve representar como objetos versionados e administráveis:

- instruções e perfis de agente;
- prompts/templates parametrizados;
- coleções de conhecimento e retrieval por domínio;
- policies de contexto e escopo de escrita;
- ferramentas/resources MCP e contratos JSON;
- evals e comparação de configurações;
- observações participativas e síntese argumentativa;
- analytics de autoria, sistema e pesquisa educacional;
- assistência por LLM em análise quantitativa, qualitativa e mista.

O objetivo não é selecionar uma biblioteca, provider, modelo ou schema final.

## 2. Perguntas de pesquisa

1. Que componentes de uma configuração de agente precisam ser separados para permitir versionamento, comparação, reprodutibilidade e administração sem código?
2. Como profiles, prompt templates, resources, tools e knowledge collections podem ser descobertos e compostos sem produzir uma nova configuração monolítica?
3. Que evidência sustenta perfis de domínio, RAG/knowledge grounding e adaptação de instruções em educação?
4. Como registrar modelo, prompt, contexto, retrieval, tools, dados e outputs de forma suficiente para avaliação e reprodução?
5. Como observações de usuários podem alimentar curadoria participativa sem serem tratadas como votos ou verdades?
6. Que usos de LLMs em codificação, análise temática e métodos mistos são defensáveis, e quais exigem revisão humana?
7. Quais limites atuais existem para raciocínio estatístico, causal e científico por LLMs?
8. Como separar analytics de autoria/sistema de analytics educacional e de pesquisa?
9. Que mecanismos de human-centred learning analytics, transparência, agência e governança devem entrar no produto?
10. Qual sequência de investigação e implantação preserva o AraLearn funcional e reduz risco de sobrearquitetura?

## 3. Frentes temáticas

### F1 — Arquitetura e composição de agentes

- prompt engineering e prompt reporting;
- system/developer instructions;
- roles e workflows;
- model/tool/context configuration;
- versionamento, evals, traces e reprodutibilidade;
- MCP prompts, resources e tools.

### F2 — Conhecimento e adaptação por domínio

- retrieval-augmented generation;
- domain adaptation;
- knowledge-base curation;
- grounding, provenance e atualização;
- context selection e retrieval evaluation;
- aplicações educacionais específicas.

### F3 — Participação, observações e curadoria

- human-centred LA/AIED;
- participatory design e co-design;
- stakeholder feedback;
- argumentação, discordância e decisão;
- transparência, agência e confiança.

### F4 — Analytics de autoria e sistema

- avaliação de prompts e workflows;
- análise de falhas por modelo/contexto/tool/schema;
- regressões e diffs;
- reliability/repeatability;
- recomendações para professores, curadores e desenvolvedores.

### F5 — Pesquisa quantitativa assistida por LLM

- statistical and causal reasoning;
- geração e verificação de código estatístico;
- pressupostos, missingness, efeito e incerteza;
- reproducibilidade e stability;
- interpretação científica e limites.

### F6 — Pesquisa qualitativa e métodos mistos

- coding e thematic analysis;
- sentiment e classificação;
- reflexividade, contexto e latent meaning;
- reliability e comparação com humanos;
- integração entre dados quantitativos e qualitativos.

### F7 — Ética, privacidade e governança

- consentimento e finalidade;
- minimização e acesso;
- dados de participantes;
- explicabilidade e contestação;
- viés, fairness e sobredependência;
- papéis humanos e autoridade final.

## 4. Fontes e bases

### Acadêmicas

- ERIC;
- Scopus e Web of Science quando houver acesso;
- ACM Digital Library;
- IEEE Xplore;
- ACL Anthology;
- PubMed/PMC para métodos e avaliações aplicáveis;
- Crossref/DOI e repositórios institucionais;
- arXiv e medRxiv somente com status de preprint explícito.

### Técnicas e normativas

- especificação e documentação oficial do Model Context Protocol;
- documentação oficial de evals, prompts, agents e ferramentas dos providers avaliados;
- NIST AI RMF e GenAI Profile;
- UNESCO e outras orientações institucionais relevantes;
- padrões de learning analytics, proveniência e pacotes de pesquisa já mapeados pelo ARA.

Documentação oficial demonstra semântica e capacidade técnica, não efetividade pedagógica.

## 5. Strings exploratórias executadas

As buscas web iniciais combinaram, em inglês:

```text
("large language model" OR LLM OR "generative AI")
AND (education OR "learning analytics")
AND (systematic review OR empirical)
```

```text
("prompt engineering" OR "prompt reporting" OR "prompt versioning")
AND (evaluation OR reproducibility OR workflow)
AND (LLM OR "large language model")
```

```text
("retrieval augmented generation" OR RAG)
AND (education OR domain-specific OR knowledge base)
AND (review OR evaluation OR adaptation)
```

```text
("large language model")
AND ("qualitative analysis" OR "thematic analysis" OR coding)
AND (evaluation OR reliability OR protocol)
```

```text
("large language model")
AND (statistical OR causal OR quantitative)
AND (reasoning OR analysis OR benchmark)
```

```text
("human-centred" OR participatory OR co-design)
AND ("learning analytics" OR AIED OR educational technology)
```

```text
site:modelcontextprotocol.io (prompts resources tools specification)
```

```text
site:openai.com OR site:platform.openai.com
(evals prompt datasets traces agents versioning)
```

## 6. Critérios de inclusão

Incluir fontes que:

- definam ou avaliem uma das frentes F1–F7;
- apresentem método, corpus, protocolo, benchmark ou especificação verificável;
- sejam revisões, estudos empíricos, frameworks centrais ou documentação oficial;
- mantenham distinção entre capacidade técnica e efeito educacional;
- sejam suficientemente próximas da decisão do ARA.

## 7. Critérios de exclusão

Excluir ou classificar apenas como contexto:

- marketing sem método ou contrato verificável;
- listas genéricas de dicas de prompting;
- produtos sem documentação técnica suficiente;
- estudos de percepção usados como prova de aprendizagem;
- análises sem informação sobre modelo, prompt, dados ou procedimento;
- resultados cujo texto completo ou metadata não possam ser verificados minimamente;
- alegações de causalidade incompatíveis com o desenho.

## 8. Extração

Cada registro deve conter:

- ID;
- referência;
- ano e status;
- frente temática;
- tipo de evidência;
- objeto e contexto;
- método/corpus;
- principal achado;
- limitações;
- implicação candidata para o ARA;
- decisão que pode informar;
- URL/DOI;
- profundidade de acesso.

## 9. Qualidade e status

Categorias:

- `official-specification`;
- `systematic-review`;
- `peer-reviewed-empirical`;
- `peer-reviewed-framework`;
- `conference-paper`;
- `preprint`;
- `institutional-guidance`.

Preprints não controlam decisões sozinhos. Revisões recentes devem ser confrontadas com estudos primários centrais quando a decisão for material.

## 10. Saturação e suficiência

A rodada inicial é suficiente para abrir a frente e ampliar o pré-backlog quando:

- todas as frentes F1–F7 possuem fontes centrais;
- há pelo menos uma fonte favorável e uma fonte de limitações para usos analíticos por LLM;
- a semântica técnica de prompts/resources/tools está verificada em fontes oficiais;
- os principais riscos de reprodutibilidade, agência e validade estão explícitos;
- existe uma sequência plausível de pesquisa antes de implementação.

Não se declara saturação acadêmica. A revisão deverá ser aprofundada por decisão focal, especialmente para:

- desenho de experimentos e métodos mistos;
- avaliação de RAG/context selection;
- prompt/profile evals;
- síntese argumentativa de observações;
- privacidade e governança institucional.

## 11. Resultado da rodada inicial

A evidência inicial apoia, como hipótese de produto:

1. separar prompts, resources e tools, coerentemente com MCP;
2. versionar configuração, modelo, contexto, knowledge e evals para reprodutibilidade;
3. permitir perfis de domínio e knowledge collections sem criar GPTs monolíticos distintos;
4. tratar participação dos usuários como evidência situada e contestável;
5. usar LLMs como auxiliares de análise qualitativa e quantitativa, com outputs reproduzíveis, revisão humana e limites explícitos;
6. manter analytics técnicos, educacionais e de pesquisa semanticamente separados;
7. não autorizar autoalteração de prompts, knowledge, resources ou publicações.

O corpus estruturado está em `research/data/agent-profiles-participatory-analytics-evidence-corpus-v1.csv`.
