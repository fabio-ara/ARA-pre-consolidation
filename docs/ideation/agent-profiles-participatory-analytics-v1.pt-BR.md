# Perfis modulares de agente, curadoria participativa e analytics assistidos por IA

**Estado:** síntese inicial para discussão; não normativa  
**Data:** 4 de agosto de 2026  
**Fase:** pré-desenvolvimento  
**Relação com o AraLearn:** preserva a autoria por GPT/MCP e propõe decompor a configuração monolítica atual em objetos versionados e administráveis.

## 1. Problema

O AraLearn comprova que um GPT com instruções, conhecimento e ferramentas MCP pode planejar, construir, auditar e reparar cursos declarativos. Entretanto, a configuração do agente permanece amplamente monolítica:

- instruções gerais e pedagógicas ficam concentradas;
- conhecimento de domínio é acoplado ao GPT configurado;
- catálogo de resources e contratos cresce em conjunto;
- papéis de planejamento, construção, auditoria, reparo e análise dependem de uma mesma base difícil de comparar;
- não há tratamento de prompts, coleções de conhecimento, políticas de contexto e avaliações como objetos versionados do produto;
- observações dos usuários ainda não formam um ciclo completo de síntese, decisão, diff, reparo, reauditoria e aprendizagem institucional;
- analytics pedagógicos, técnicos e experimentais não estão integrados ao aperfeiçoamento dos agentes, resources e cursos.

O ARA precisa preservar a experiência funcional do AraLearn e tornar essa configuração explícita, modular, versionada, testável e administrável sem exigir edição de código.

## 2. Tese

A configuração efetiva de um agente do ARA deve resultar da composição de objetos menores:

```text
base comum do ARA
+ papel da operação
+ perfil de domínio
+ perfil de público/contexto
+ coleções de conhecimento autorizadas
+ prompts/templates especializados
+ catálogo e contratos de capabilities/resources
+ política de contexto e escopo de escrita
+ modelo/provedor e parâmetros
+ rubrica, evals e regras de validação
→ AgentConfigurationSnapshot
```

O snapshot efetivo deve ser persistido junto de cada operação. Isso permite comparar gerações, auditorias e análises sem depender da memória do chat ou de uma configuração externa que possa ter mudado.

## 3. Distinções necessárias

### 3.1 Instrução, conhecimento e operação

- **instruções do agente:** comportamento, limites, papel, processo e critérios;
- **perfil de domínio:** terminologia, práticas epistemicamente adequadas, erros recorrentes, fontes e rubricas específicas;
- **coleção de conhecimento:** corpus versionado e pesquisável, com proveniência, licença e validade temporal;
- **prompt/template:** roteiro reutilizável e parametrizado para uma tarefa;
- **resource MCP:** contexto ou dado recuperável e, em princípio, não mutante pela leitura;
- **tool MCP:** operação tipada que lê ou altera objetos autorizados;
- **contrato JSON/resource package:** semântica determinística de conteúdo, autoria, renderização e validação;
- **política de contexto:** o que é lido integralmente, resumido, indexado ou omitido;
- **escopo de escrita:** os objetos que a operação pode efetivamente alterar.

Essas categorias não devem ser chamadas genericamente de “prompt” na modelagem interna, embora a interface possa usar linguagem simples.

### 3.2 Contexto de leitura e autorização de escrita

A disponibilidade de contexto não concede permissão para mutação.

Exemplo:

```text
operação no card
- escrita: card/resources selecionados
- leitura integral: microssequência atual
- leitura indexada/resumida: microssequências vizinhas e árvore autorizada

operação na microssequência
- escrita: cards e composição interna da microssequência
- leitura integral: microssequência atual
- leitura indexada/resumida: unidades vizinhas, lição e árvore autorizada

operação na lição
- escrita: microssequências selecionadas; criação/reordenação de microssequências somente quando a lição inteira estiver autorizada
- leitura: lição atual e contexto externo necessário, sempre sem mutação fora da lição
```

Não se propõe assistência de autoria acima da lição enquanto o maior objeto criável for a microssequência.

## 4. Objetos candidatos

### 4.1 AgentProfile

Identidade administrativa de uma configuração reutilizável.

Campos candidatos:

- ID, nome, finalidade e estado;
- papel ou conjunto de papéis;
- domínio e público;
- versões ativas e históricas;
- autoridade responsável;
- deployments e workspaces permitidos.

### 4.2 AgentProfileVersion

Revisão imutável contendo:

- instruções comuns e específicas;
- referências a DomainProfileVersion;
- prompt/template versions;
- KnowledgeCollectionSnapshots;
- tools/resources/capabilities permitidos;
- política de contexto e escrita;
- modelo/provedor e parâmetros relevantes;
- rubricas, eval suites e limitações;
- justificativa, autor, data e relação com a versão anterior.

### 4.3 DomainProfileVersion

Configuração especializada por domínio ou prática, como:

- computação e programação;
- redes e infraestrutura;
- matemática e estatística;
- línguas e linguística;
- análise de fontes históricas;
- procedimentos administrativos;
- concursos e bancas específicas.

Pode definir vocabulário, fontes prioritárias, resources adequados, práticas, validação, rubricas, tipos de erro e contraindicações. Um domínio não deve impor uma pedagogia única; parâmetros e condições continuam separados.

### 4.4 KnowledgeCollectionSnapshot

Coleção versionada de fontes e materiais:

- itens e versões;
- status de acesso e revisão;
- proveniência, licença e validade;
- índices e embeddings derivados;
- política de atualização e retenção;
- filtros por domínio, curso, instituição ou confidencialidade.

### 4.5 PromptTemplateVersion

Template parametrizado, versionado e testável, associado a tarefa e perfil. Deve registrar:

- texto e argumentos;
- papel e pré-condições;
- recursos e tools esperados;
- exemplos e contraexemplos;
- versão do modelo usada em evals;
- justificativa e histórico;
- resultados, limitações e rollback.

### 4.6 AgentOperation

Cada execução registra:

- alvo e revisão lidos;
- escopo de escrita;
- contexto integral e recuperado;
- snapshots de configuração;
- modelo, provider e tool versions;
- instrução do usuário;
- artefatos produzidos;
- validações, findings e diffs;
- decisão humana e revisão resultante.

## 5. Papéis e subpapéis

Os papéis devem representar responsabilidade e autoridade, não necessariamente contas ou GPTs distintos.

### Autoria e curadoria

- planejador de curso;
- autor/construtor;
- editor manual;
- revisor de domínio;
- auditor pedagógico;
- auditor técnico/contratual;
- reparador;
- reauditor;
- curador de fontes e licenças;
- aprovador/publicador.

### Engenharia e avaliação do agente

O termo provisório mais preciso é **avaliador e curador de configurações de agente**, em vez de presumir que toda atividade seja “engenharia de prompt”. Subpapéis:

- investigador de prompting e instruções;
- curador de knowledge collections;
- avaliador de retrieval e contexto;
- avaliador de tools e contratos MCP;
- designer de evals e casos de teste;
- analista de falhas e regressões;
- administrador de versões e ativações.

### Pesquisa educacional

- designer de protocolo e condições;
- curador de instrumentos e medidas;
- analista quantitativo;
- analista qualitativo;
- integrador de métodos mistos;
- intérprete e redator de limitações;
- revisor metodológico e ético.

O mesmo GPT pode assumir papéis diferentes em rodadas separadas, contra versões persistidas, sem converter análise em aprovação automática.

## 6. Curadoria participativa

Usuários autorizados podem registrar observações situadas em curso, módulo, lição, microssequência, card, resource, prática, relação, configuração ou versão.

Cada observação deve preservar:

- alvo e versão exatos;
- autor/papel ou pseudônimo autorizado;
- tipo e finalidade;
- texto, exemplo, fonte ou evidência;
- visibilidade e uso permitido;
- relação com outras observações;
- estado e decisão.

A força de uma contribuição não deriva de popularidade, extensão textual ou eloquência. Critérios candidatos incluem:

- precisão e reprodutibilidade;
- evidência ou fonte verificável;
- pertinência de domínio;
- gravidade e alcance;
- independência e confirmações;
- contraexemplos e conflitos;
- qualificação exigida para o tipo de decisão.

O GPT pode agrupar, deduplicar, contrastar e recomendar classificação, mas deve preservar observações minoritárias e divergentes. A saída é um conjunto de findings e recomendações auditáveis, não um plebiscito automático.

## 7. Diffs e ciclo de melhoria

```text
observações situadas
→ corpus congelado por alvo/versão
→ codificação e síntese assistidas
→ findings procedentes, parciais, conflitantes ou insuficientes
→ proposta de reparo
→ diff semântico e de configuração
→ auditoria independente
→ decisão humana
→ nova revisão
→ monitoramento e reavaliação
```

O diff deve distinguir:

- conteúdo e fontes;
- composição e ordem;
- resources/practices/feedback;
- parâmetros e condições;
- configuração do agente;
- knowledge/retrieval;
- tools/contratos MCP;
- mudança técnica sem efeito pedagógico conhecido;
- mudança potencialmente pedagógica que exige avaliação própria.

## 8. Analytics de autoria e sistema

Perguntas candidatas:

- quais classes de observação e finding são recorrentes;
- quais resources, contratos ou renderers concentram problemas;
- quais perfis de domínio ou templates produzem regressões;
- quais falhas decorrem de instrução, knowledge, retrieval, contexto, tool, schema, modelo ou conteúdo-fonte;
- quais reparos resolvem o problema e quais o reintroduzem;
- quando um novo resource ou uma revisão de contrato é preferível a ajustar instruções;
- como resultados variam por modelo, provider, versão e configuração;
- quais recomendações devem ir ao professor, proprietário ou equipe de desenvolvimento.

Esses analytics não devem transformar correlações operacionais em conclusões pedagógicas sem desenho apropriado.

## 9. Analytics educacional e pesquisa

O ARA deve permitir análise quantitativa, qualitativa e mista dentro de protocolos versionados.

### Quantitativa

- estatísticas descritivas e incerteza;
- comparação entre grupos/condições;
- tamanhos de efeito;
- testes e modelos adequados ao desenho;
- verificação de pressupostos;
- missingness, attrition e fidelity;
- análises de sensibilidade;
- distinção entre análise planejada e exploratória.

### Qualitativa

- organização e busca do corpus;
- codificação assistida;
- agrupamento de observações e respostas abertas;
- síntese de temas e divergências;
- seleção rastreável de evidências;
- memos, reflexividade e revisão humana;
- comparação entre codificadores humanos e agentes quando aplicável.

### Métodos mistos

- integração explícita, não simples justaposição;
- uso de resultados quantitativos para orientar aprofundamento qualitativo e vice-versa;
- matrizes conjuntas e explicações concorrentes;
- preservação de unidade de análise, temporalidade e condições.

## 10. GPT no papel de pesquisador-assistente

O GPT pode auxiliar a:

1. formular pergunta e hipóteses;
2. revisar coerência entre desenho, condição, instrumento e medida;
3. elaborar plano de análise;
4. executar código estatístico reproduzível em ambiente controlado;
5. verificar pressupostos e dados faltantes;
6. propor análises alternativas;
7. codificar e sintetizar dados qualitativos;
8. integrar evidência mista;
9. distinguir resultado, interpretação, conclusão admissível e conclusão não admissível;
10. produzir explicações pedagógicas sobre métodos e limitações.

O ARA não deve representar o GPT como pesquisador autônomo ou autoridade científica. Toda análise registra configuração, dados, código, outputs, decisões humanas e limitações. Resultados estocásticos relevantes exigem repetição ou avaliação de estabilidade.

## 11. Interface administrativa

A administração comum deve evitar exposição de código ou grandes prompts monolíticos. Superfícies candidatas:

- selecionar perfil de domínio, papel e finalidade;
- escolher coleções de conhecimento e fontes;
- ver resources/tools disponíveis;
- comparar versões e consequências;
- executar uma suíte de casos de teste;
- ativar, retirar ou restaurar versão;
- abrir detalhes avançados somente quando necessário.

O proprietário ou administrador avançado pode editar instruções integrais, templates, coleções e evals em formulários versionados. O autor comum vê linguagem de tarefa e consequências.

## 12. Caminho candidato de implantação

1. inventariar a configuração monolítica do AraLearn: instruções, knowledge, tools, contratos, papéis e fluxos;
2. separar conceitualmente o que pertence à base comum, domínio, tarefa, contexto, tool e knowledge;
3. criar objetos versionados apenas em documentação e fixtures;
4. definir eval corpus com casos reais do AraLearn;
5. testar composição equivalente à configuração atual para garantir continuidade;
6. introduzir um primeiro perfil de domínio sem alterar o fluxo público;
7. persistir snapshots de configuração nas operações;
8. implementar diffs e avaliação de regressão;
9. integrar observações participativas e analytics de autoria;
10. implementar analytics de pesquisa somente com protocolo, direitos e evidência definidos.

## 13. Riscos

- transformar modularidade em centenas de opções visíveis;
- confundir prompt, conhecimento, resource pedagógico e tool;
- permitir que configuração técnica vire decisão pedagógica silenciosa;
- usar observações como votação;
- deixar o GPT avaliar a própria saída sem independência;
- alterar prompts ou knowledge automaticamente a partir de analytics;
- executar análises estatísticas inadequadas ou inventar causalidade;
- expor dados de participantes a providers ou perfis não autorizados;
- perder reprodutibilidade por mudanças de modelo, prompt, retrieval ou corpus;
- construir um sistema genérico de agentes em vez de resolver o fluxo educacional do ARA.

## 14. Decisões preliminares

- **preservar:** GPT/MCP como canal de autoria, auditoria e reparo observado no AraLearn;
- **separar:** instruções, domínio, knowledge, prompts, contexto, tools, contracts, evals e modelo;
- **propor:** perfis e snapshots versionados administráveis como dados;
- **propor:** assistência por IA nos níveis de card, microssequência e lição, com leitura e escrita separadas;
- **propor:** curadoria participativa com observações argumentadas, conflitos preservados e decisão humana;
- **propor:** analytics de autoria/sistema separados de analytics de pesquisa;
- **propor:** GPT como pesquisador-assistente, não autoridade final;
- **investigar:** terminologia, modelo de composição, contexto indexado, métricas de qualidade e confiabilidade;
- **rejeitar como padrão:** atualização autônoma de prompts, knowledge, resources ou publicações.

## 15. Evidência e limitações

A síntese inicial é apoiada por revisões e estudos sobre prompting, RAG educacional, GenAI em learning analytics, human-centred LA/AIED, análise qualitativa assistida por LLM, raciocínio estatístico/causal, reproducibilidade e especificações oficiais de MCP/evals. O protocolo e o corpus estão em:

- `research/searches/2026-08-04-agent-profiles-participatory-analytics-protocol.md`;
- `research/data/agent-profiles-participatory-analytics-evidence-corpus-v1.csv`;
- `research/library/agent-profiles-participatory-analytics-v1.bib`.

Este levantamento é uma revisão de escopo inicial, não uma revisão sistemática concluída. Algumas fontes recentes são preprints e devem permanecer classificadas como tal. Novas decisões exigem aprofundamento focal e, quando necessário, acesso a textos completos.
