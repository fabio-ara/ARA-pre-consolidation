# Instrumentação cientificamente útil e operacionalmente viável no ARA

**Estado:** síntese de pesquisa para orientar o pré-backlog; não executável  
**Data:** 5 de agosto de 2026  
**Escopo:** proveniência, autoria/contribuição, learning analytics, versionamento e custo de processamento  
**Relação:** refina as áreas Q, R e S e complementa `course-level-version-graph-accepted-decisions-v1.pt-BR.md`.

## 1. Pergunta de projeto

O ARA pretende expandir o AraLearn para uma plataforma de pesquisa educacional em que pesquisadores possam selecionar parâmetros, configurar condições, acompanhar trajetórias de autoria e estudo e comparar revisões do mesmo curso.

A questão não é decidir agora todas as pesquisas futuras. É decidir quais classes de evidência o sistema precisa ser capaz de preservar para não inviabilizar pesquisas posteriores.

Ao mesmo tempo, a instrumentação não pode:

- duplicar o esforço cognitivo do GPT autoral;
- exigir uma segunda análise semântica completa a cada operação;
- aumentar de forma descontrolada tokens, latência e custo;
- armazenar indiscriminadamente todas as conversas, contextos e eventos de interface;
- prejudicar planejamento, construção, auditoria, reparo e reauditoria;
- converter proxies não validados em afirmações de autoria, criticidade ou qualidade.

## 2. Resultado principal da revisão

A direção mais defensável é separar quatro responsabilidades:

```text
agente autoral
- planeja, constrói, audita, repara e reaudita

backend/MCP
- registra fatos já conhecidos de forma determinística

instrumentação educacional
- emite eventos mínimos, estruturados e extensíveis

processo analítico posterior
- deriva métricas e aplica esquemas de codificação quando necessário
```

A literatura e os padrões consultados convergem para modelos incrementais e extensíveis, não para interpretação integral em tempo real:

- W3C PROV parte de `Entity`, `Activity` e `Agent` e permite qualificações adicionais somente quando necessárias;
- xAPI usa statements imutáveis com núcleo `actor + verb + object`, podendo acrescentar `result`, `context`, `authority` e extensões;
- Caliper Analytics organiza eventos em perfis de domínio, permitindo um vocabulário comum sem exigir que toda interação seja semanticamente reavaliada por LLM;
- CRediT mostra que contribuições podem ser descritas por papéis estruturados sem que isso determine automaticamente autoria.

## 3. Decisão arquitetural recomendada

O ARA deve nascer **research-ready**, mas não **research-maximalist**.

Isso significa:

- capacidade ampla de instrumentação;
- coleta operacional mínima por padrão;
- extensões ativáveis por workspace, implantação ou protocolo;
- evidências primárias referenciáveis;
- esquemas e métricas versionados;
- separação entre registro operacional e interpretação científica;
- ausência de segunda chamada obrigatória ao GPT apenas para telemetria.

## 4. Quatro camadas de registro

### 4.1 Evidência primária referenciada

O sistema deve ser capaz de reconstruir a operação por referências imutáveis:

- revisão-base;
- proposta do agente;
- mensagem ou decisão humana;
- findings e observações utilizados;
- objetos-alvo;
- diff executado;
- revisão resultante;
- reauditoria ou validação posterior;
- configuração efetiva do agente.

Esses elementos não precisam ser copiados integralmente para cada evento. Devem ser referenciados.

### 4.2 Evento operacional mínimo

Núcleo obrigatório e barato:

```text
EventRecord
- event_id
- schema_version
- occurred_at
- stored_at
- actor_ref
- actor_type: person | software_agent | system
- verb
- object_ref
- object_type
- course_revision_ref
- operation_ref
- session_ref opcional
- authority_ref
- result_summary opcional
- context_refs[]
```

Esse desenho é compatível conceitualmente com xAPI e Caliper, mas deve permanecer específico ao domínio do ARA.

### 4.3 Receipt de transformação

Para cada nova revisão materializada:

```text
TransformationReceipt
- base_course_revision_ref
- result_course_revision_ref
- operation_type
- trigger_type
- target_refs[]
- proposed_item_count
- accepted_as_proposed_count
- rejected_count
- modified_count
- added_target_count
- deliberation_round_count
- created_object_count
- changed_object_count
- removed_object_count
- validation_status
- finding_resolution_counts
- regression_count quando houver reauditoria
- human_authorizer_ref
- software_agent_configuration_ref
```

Esses campos devem ser produzidos, sempre que possível, pelo backend e pelas próprias ferramentas MCP.

### 4.4 Codificação analítica versionada

Interpretações como autoria ratificadora, intervenção deliberativa, criticidade ou coprodução devem ser registradas separadamente:

```text
AnalyticalCoding
- coding_id
- target_event_or_operation_ref
- coding_scheme_ref
- coding_scheme_version
- variables
- coder_ref
- coder_type
- confidence opcional
- evidence_refs[]
- validation_status
```

Uma codificação analítica nunca sobrescreve o evento original.

## 5. O que deve ser quantificável desde o início

### 5.1 Autoria e contribuição observáveis

- quem iniciou a operação;
- quem propôs alteração;
- quem autorizou;
- número de itens propostos;
- aceitos sem modificação;
- rejeitados;
- modificados;
- novos requisitos ou alvos;
- número de rodadas;
- objetos criados, alterados e removidos;
- extensão estrutural do diff;
- reversões posteriores;
- persistência da alteração.

### 5.2 Qualidade da produção do agente

- finding confirmado ou refutado;
- diagnóstico aceito, modificado ou rejeitado;
- escopo correto ou excessivo;
- proposta executada integral ou parcialmente;
- finding resolvido;
- regressões introduzidas;
- reauditorias até estabilização;
- alteração revertida posteriormente;
- rubrica e perfil de agente usados;
- tipo de objeto e dimensão de qualidade afetados.

### 5.3 Experiência educacional

- revisão exata do curso realizada;
- composição e parâmetros efetivos;
- ordem e seleção de cards;
- respostas, resultados e feedback;
- tentativas quando configuradas;
- observações situadas;
- interrupções e retomadas relevantes;
- intervenções do agente;
- avaliação subjetiva por dimensão;
- problemas técnicos relevantes;
- turma, condição ou protocolo.

## 6. O que não deve exigir processamento adicional do GPT

O backend já conhece ou pode calcular:

- IDs, timestamps e autoria autenticada;
- versão-base e versão-resultante;
- objetos lidos e alterados;
- ferramenta MCP chamada;
- escopo autorizado;
- diff estrutural;
- contagem de objetos;
- número de rodadas;
- itens aceitos/rejeitados quando a decisão for estruturada;
- validações determinísticas;
- links entre finding, observação, reparo e reauditoria.

Esses dados não devem ser reenviados ao GPT para que ele os descreva.

## 7. O que pode ser produzido pelo GPT sem chamada adicional

Quando o agente já precisa interpretar linguagem natural para executar corretamente, ele pode retornar um envelope estruturado mínimo junto da resposta normal:

```text
DecisionParse
- accepted_refs[]
- rejected_refs[]
- modified_refs[]
- added_requirements[]
- added_target_refs[]
- unresolved_ambiguities[]
```

Regras:

- mesmo ciclo de inferência;
- poucos campos;
- sem justificativa longa adicional;
- validação pelo MCP;
- possibilidade de correção pela interface;
- nenhuma classificação de autoria ou criticidade em tempo real.

## 8. O que deve ser diferido para análise sob demanda

- classificação de autoria passiva ou crítica;
- análise argumentativa detalhada;
- inferência de dependência da IA;
- avaliação de qualidade global da interação;
- clustering semântico de milhares de operações;
- comparação longitudinal de linhagens;
- process mining;
- codificação qualitativa;
- análise causal;
- explicações científicas.

Essas tarefas podem ser executadas:

- em lote;
- sobre amostras;
- sobre períodos selecionados;
- por agentes analíticos especializados;
- sob protocolo;
- com validação humana.

## 9. Taxonomia operacional mínima candidata

A taxonomia inicial deve ser pequena e extensível.

### Operação

- plan
- construct
- audit
- repair
- reaudit
- extend
- reorganize
- consolidate
- restore
- translate
- adapt

### Trigger

- human_request
- audit_finding
- user_observation
- learner_feedback
- analytics_recommendation
- imported_version
- protocol_requirement

### Dimensão ampla de qualidade

- factual_content
- coverage
- pedagogy
- assessment
- language
- accessibility
- structure
- resource_contract
- agent_configuration
- authorization
- technical_experience

### Decisão humana observável

- approved_as_proposed
- approved_with_selection
- approved_with_modification
- rejected
- expanded_scope
- reframed_problem
- deferred

Essas categorias são candidatas e devem ser testadas contra casos reais do AraLearn e exemplos sintéticos antes de congelamento.

## 10. Avaliação subjetiva do curso

Uma nota geral isolada é insuficiente. O ARA deve permitir instrumentos multidimensionais configuráveis, por exemplo:

- qualidade percebida do conteúdo;
- clareza;
- dificuldade;
- utilidade das práticas;
- adequação do feedback;
- organização;
- formato dos resources;
- suporte do agente;
- experiência técnica;
- avaliação geral;
- texto livre;
- referências a objetos específicos.

A avaliação deve apontar para:

- revisão exata do curso;
- condição experimental;
- versão do instrumento;
- momento da aplicação;
- objetos eventualmente citados.

O instrumento não deve ser fixo no kernel: pesquisadores precisam poder definir escalas e itens, preservando versionamento e comparabilidade.

## 11. Configuração de protocolo

O ARA deve permitir que um protocolo ative instrumentação adicional:

```text
ResearchProtocol
- research_question_refs[]
- population_and_sampling
- conditions[]
- parameter_sets[]
- required_event_profiles[]
- subjective_instruments[]
- retention_policy_ref
- consent_and_rights_ref
- pseudonymization_policy_ref
- export_schema_ref
- analysis_plan_refs[]
```

O protocolo escolhe quais capacidades serão efetivamente coletadas. A existência de suporte técnico não implica coleta universal.

## 12. Perfil de custo

### Custo quase nulo para o GPT

- receipts gerados pelo backend;
- IDs e relações;
- diffs;
- contagens;
- status de validação;
- eventos de estudo emitidos pela UI;
- parâmetros efetivos;
- respostas e resultados já processados.

### Custo incremental baixo

- envelope estruturado da decisão humana na mesma resposta;
- tipo amplo de operação;
- dimensão ampla de finding já necessária à auditoria;
- referências aos itens discutidos.

### Custo alto, não obrigatório no fluxo autoral

- resumo semântico de toda a sessão;
- autoria percentual;
- análise de sentimento;
- análise argumentativa;
- classificação de criticidade;
- comparação com histórico integral;
- produção de narrativa de proveniência;
- codificação científica completa.

## 13. Retenção

### Durável por padrão

- revisões e manifests;
- relações de derivação;
- receipts de transformação;
- configuração efetiva do agente;
- findings, observações e decisões diretamente usados;
- eventos educacionais essenciais ao funcionamento;
- instrumentos e parâmetros efetivos;
- referências a protocolos e datasets congelados.

### Configurável

- mensagens completas;
- respostas brutas de LLM;
- contexto recuperado;
- propostas rejeitadas detalhadas;
- eventos finos de navegação;
- anexos;
- telemetry técnica ampliada.

### Transitório

- digitação;
- undo/redo;
- hover, foco e movimentos;
- caches;
- respostas inválidas;
- checkpoints locais não promovidos.

## 14. Critérios de factibilidade antes da implementação

A decisão final do esquema deve ser precedida por benchmarks com:

- curso curto, médio e extenso;
- 10, 100 e 1.000 autores/estudantes;
- 10 mil, 100 mil e 1 milhão de revisões/eventos;
- diferentes níveis de retenção;
- envelopes estruturados ligados e desligados;
- comparação de custo e latência do agente;
- tamanho médio de receipts e events;
- custo de consulta e exportação;
- reconstrução de datasets;
- backup e restore;
- pseudonimização e exclusão conforme política.

Critério de aceitação do envelope adicional do GPT:

- não exigir segunda chamada;
- acréscimo pequeno de tokens;
- ausência de degradação mensurável na qualidade do artefato;
- taxa de parse e validação suficiente;
- possibilidade de fallback para registro não classificado.

## 15. Programa de validação

1. Extrair jornadas reais do AraLearn.
2. Identificar quais fatos o backend já conhece.
3. Prototipar o núcleo de eventos sem LLM adicional.
4. Prototipar o envelope mínimo na mesma chamada.
5. Medir tokens, latência, erro e qualidade do curso.
6. Testar a taxonomia com codificadores humanos e agentes.
7. Verificar concordância e categorias ausentes.
8. Simular perguntas de pesquisa e verificar se os dados bastam.
9. Testar retenção mínima versus extensiva.
10. Somente então produzir esquema candidato e ADR.

## 16. Relação com o pré-backlog

Esta síntese refina, sem aumentar automaticamente a contagem:

### Área Q

- Q08 — contexto e escopo de escrita;
- Q09 — snapshot da configuração do agente;
- Q13 — provenance e diff;
- Q16 — ciclo observação/finding/reparo/reauditoria;
- Q18 — analytics de autoria, agente e sistema;
- Q20–Q24 — pesquisa quantitativa, qualitativa e mista;
- Q25 — governança e direitos;
- Q26 — casos do AraLearn.

### Área R

- R04 — objetos versionados;
- R05 — granularidade;
- R10 — operation log;
- R14 — fronteiras de persistência;
- R17–R20 — projeções, contexto, retenção e workload.

### Área S

- S04–S13 — DAG, projeções e navegação;
- S20–S22 — análise e consolidação;
- S25–S26 — escala e BaaS.

## 17. Decisões aceitas nesta síntese

- O ARA deve ser preparado desde a arquitetura para subsidiar pesquisas educacionais diversas.
- Isso exige registrar classes de evidência, não antecipar uma única pesquisa.
- O registro operacional deve ser quantitativo, semântico, versionado e referenciável.
- O GPT autoral não deve executar uma segunda análise completa para registrar provenance.
- O backend deve produzir a maior parte dos dados.
- O GPT pode emitir somente um envelope mínimo quando a interpretação já for necessária à operação.
- Métricas e codificações complexas são derivadas posteriormente.
- A capacidade de coleta deve ser ampla, mas a coleta efetiva deve ser configurada por finalidade e protocolo.
- Factibilidade deve ser medida com workloads e impacto na qualidade do agente antes de congelar o esquema.

## 18. Fontes iniciais

- W3C. PROV-O: The PROV Ontology. Recommendation, 2013.
- W3C Provenance Working Group. PROV Data Model and related recommendations.
- ADL/xAPI Working Group. Experience API Data Specification.
- 1EdTech Consortium. Caliper Analytics 1.2 and Metric Profiles.
- NISO. CRediT — Contributor Roles Taxonomy, ANSI/NISO Z39.104-2022.

## 19. Limites desta revisão

Esta é uma revisão dirigida inicial, baseada principalmente em padrões e documentação oficial. Ainda são necessários:

- levantamento acadêmico específico sobre autoria e colaboração humano–IA;
- literatura de learning analytics, trace data e process mining;
- instrumentos validados de percepção de qualidade e experiência;
- privacidade e ética em instrumentação educacional;
- casos de plataformas experimentais educacionais;
- validação com jornadas reais e benchmarks do AraLearn.
