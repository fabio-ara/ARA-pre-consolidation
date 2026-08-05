# Correção versionada da área Q — AraLearn, evals e versionamento

**Estado:** candidato para discussão; não executável  
**Versão:** 2  
**Base preservada:** `draft-backlog-agent-profiles-analytics-v1.pt-BR.md`  
**Issue principal:** #77  
**Dependência de versionamento:** #79

## Regra de leitura

A área Q continua possuindo 26 itens. Esta versão substitui somente Q01, Q10, Q26 e a sequência de investigação. Q02–Q09 e Q11–Q25 permanecem como no v1.

A correção impede interpretar o AraLearn como implementação modular equivalente. O predecessor é referência funcional, evidência de limitações e fonte de casos de contraste.

## Q01 — Inventário contrastivo da configuração monolítica do AraLearn

Mapear instruções do GPT, knowledge atual, papéis, prompts implícitos, tools MCP, resources/contratos, contexto, providers e fluxos de autoria/auditoria.

O inventário deve distinguir:

- jornadas que funcionam e não devem regredir silenciosamente;
- limitações e acoplamentos que motivam o ARA;
- exemplos reais de operações e falhas;
- amostras de payload e workload;
- objetos que somente existirão no ARA.

Não deve presumir que o AraLearn contenha versões equivalentes de `AgentProfile`, `PromptTemplate`, `KnowledgeCollection`, `EvalSuite` ou `AgentConfigurationSnapshot`.

## Q10 — Evals orientados às tarefas-alvo do ARA

Criar:

- tarefas-alvo;
- casos controlados e sintéticos;
- invariantes estruturais, pedagógicos e de autorização;
- rubricas e critérios verificáveis;
- repetições e análise de estabilidade;
- casos positivos, negativos, limítrofes e de regressão.

Jornadas e falhas observadas no AraLearn podem integrar o corpus como contraste, mas não como fixtures de uma arquitetura modular equivalente. Um score único não decide ativação de perfil.

## Q26 — Casos de contraste AraLearn → ARA modular

Usar jornadas funcionais, operações observadas, limitações, falhas e amostras de payload do AraLearn para:

- identificar invariantes que o proprietário deseja preservar;
- demonstrar problemas que a modularização pretende resolver;
- formular tarefas e cenários do ARA;
- evitar regressões perceptíveis na experiência;
- alimentar a simulação de storage e custo da área R.

Não exigir paridade interna, equivalência de configuração ou reprodução integral do predecessor.

## Sequência corrigida

1. concluir Q01 como inventário contrastivo;
2. definir Q02–Q09 em documentação e exemplos controlados;
3. construir Q10 a partir das tarefas-alvo do ARA;
4. usar Q26 para continuidade das jornadas aceitas e contraste das limitações;
5. aprofundar Q14–Q19 com cenários participativos;
6. aprofundar Q20–Q25 por desenhos de pesquisa prioritários;
7. entregar requisitos de persistência e retenção à área R/#79;
8. revisar requisitos, domínio, arquitetura e UX antes da implementação.

## Efeito no pré-backlog

- quantidade da área Q: **26**, sem alteração;
- área R acrescentada: **10 itens**;
- pré-backlog v3: **207 itens em 18 áreas**;
- manifesto: `research/data/ara-draft-backlog-v3-manifest.json`.
