# Síntese integrada final da Issue #4 — primeira taxonomia de configuração do ARA

**Issue governante:** #4  
**Versão:** `ara.configuration-taxonomy.v1`  
**Data:** 3 de agosto de 2026  
**Estado:** `accepted-normative-handoff` para as Issues #5 e #6; não autoriza engenharia.

## 1. Finalidade

Este documento integra os Pacotes P1–P5 em uma primeira taxonomia coerente e versionada para o ARA.

A integração não substitui os registros originais. As definições, valores, evidência, dependências, incompatibilidades e implicações de cada parâmetro permanecem nos CSVs P1–P5. O registro mestre acrescenta somente:

- identidade canônica;
- origem;
- família integrada;
- camada de incidência;
- domínio de autoridade;
- alias de namespace quando necessário;
- vínculo de rastreabilidade.

A taxonomia aceita **205 parâmetros de origem e 205 parâmetros canônicos**. Não foi encontrado nenhum identificador exatamente duplicado. Sobreposições semânticas foram preservadas quando incidiam sobre objetos, escopos ou autoridades diferentes.

## 2. Conclusão principal

O ARA não deve representar parametrização como:

```text
um formulário plano
→ um JSON monolítico com todas as opções
→ um renderer que tenta interpretar tudo
```

O modelo conceitual aceito é:

```text
catálogo versionado de parâmetros
+ perfil-base nomeado
+ overlays compatíveis
+ políticas e locks de maior autoridade
+ overrides esparsos por escopo
+ conteúdo e composição versionados
+ capacidades efetivamente disponíveis
→ resolução determinística
→ configuração efetiva e snapshot reproduzível
```

Há cinco camadas principais de incidência e uma camada transversal de direitos:

1. `runtime-effective-configuration`;
2. `content-materialization`;
3. `composition-dependencies`;
4. `lifecycle-governance`;
5. `research-condition`;
6. `rights-accessibility`, transversal.

Essas camadas não devem ser confundidas.

## 3. Resultado da integração

| Item | Resultado |
|---|---:|
| parâmetros P1 | 21 |
| parâmetros P2 | 36 |
| parâmetros P3 | 50 |
| parâmetros P4 | 31 |
| parâmetros P5 | 67 |
| parâmetros de origem | 205 |
| parâmetros canônicos | 205 |
| duplicatas exatas | 0 |
| aliases de integração | 18 |
| ocorrências de perfis nos pacotes | 43 |
| perfis canônicos únicos | 38 |
| candidatos adiados únicos | 36 |
| princípios rejeitados consolidados | 41 |
| cenários integrados validados | 15 |

A aceitação de uma dimensão significa que a variação precisa poder ser representada, explicada, versionada e reproduzida. Não significa que todos os valores serão implementados ou expostos no primeiro release.

## 4. Harmonização de namespaces

Dois usos diferentes de `review` apareceram nos pacotes:

- P2: revisão de aprendizagem, agenda e espaçamento;
- P5: revisão editorial, pedagógica e institucional.

Eles não são a mesma entidade. Para impedir ambiguidade no modelo integrado, adotam-se aliases canônicos:

| pacote | identificador de origem | identificador canônico |
|---|---|---|
| P2 | `review.trigger` | `study_review.trigger` |
| P2 | `review.schedule_policy` | `study_review.schedule_policy` |
| P2 | `review.interval_pattern` | `study_review.interval_pattern` |
| P2 | `review.target_horizon` | `study_review.target_horizon` |
| P2 | `review.load_budget` | `study_review.load_budget` |
| P2 | `review.deferral_policy` | `study_review.deferral_policy` |
| P2 | `review.item_relation` | `study_review.item_relation` |
| P2 | `review.failure_policy` | `study_review.failure_policy` |
| P4 | `withdrawal.policy` | `participant.withdrawal_policy` |
| P4 | `export.policy` | `research_export.policy` |
| P5 | `review.type` | `authoring_review.type` |
| P5 | `review.rubric` | `authoring_review.rubric` |
| P5 | `review.scope` | `authoring_review.scope` |
| P5 | `review.independence` | `authoring_review.independence` |
| P5 | `review.reviewer_qualification` | `authoring_review.reviewer_qualification` |
| P5 | `review.outcome` | `authoring_review.outcome` |
| P5 | `review.finding_record` | `authoring_review.finding_record` |
| P5 | `review.approval_policy` | `authoring_review.approval_policy` |

Os identificadores de origem continuam válidos para interpretar os artefatos P1–P5. O registro integrado é a autoridade para novos handoffs.

## 5. Camadas de incidência

### 5.1 Runtime e configuração efetiva

Abrange decisões que mudam a experiência de estudo ou avaliação sem exigir necessariamente uma nova redação do conteúdo:

- prática, resposta e validade;
- tentativas, pistas, reveal e feedback;
- consequências e visibilidade de pontuação;
- progressão, ritmo e review de aprendizagem;
- retomada;
- autonomia e suportes de autorregulação;
- opções de acessibilidade;
- aplicação de adaptação ou assistência por IA.

Uma mudança runtime pode exigir novo snapshot de condição, mas não deve ser tratada automaticamente como nova versão textual do conteúdo.

### 5.2 Conteúdo e materialização

Abrange decisões que mudam o artefato autoral:

- concentração, extensão, segmentação e granularidade;
- distribuição teoria–prática;
- exemplos, explicações e scaffolds incorporados;
- geração, tradução, adaptação ou reparo de cards e microssequências;
- conteúdo criado ou transformado por IA;
- variantes de conteúdo produzidas para pesquisa.

Esses parâmetros não são switches de renderer. Sua aplicação cria uma revisão, derivação ou variante identificável.

### 5.3 Composição e dependências

Abrange:

- ordem e pré-requisitos;
- branching e interleaving;
- ocorrências contextuais de unidades;
- reuse, reference, copy e fork;
- relações entre microssequências e cursos;
- snapshots de sequência;
- impactos de atualização em consumidores;
- composição de variantes comparativas.

Uma alteração nessa camada cria nova versão da composição, mesmo que as revisões das unidades referenciadas permaneçam iguais.

### 5.4 Lifecycle e governança

Abrange:

- estados de autoria;
- revisão, findings, comentários e reparo;
- revisões, derivação, diff, merge e rollback;
- publicação, audiência, retirada e exclusão;
- licenciamento e atribuição;
- workspaces, papéis, permissões, aprovação e separação de deveres;
- confidencialidade, retenção, exportação e indisponibilidade.

Publicado não significa público. Responder a uma anotação não significa resolvê-la. Validar schema não significa auditar pedagogicamente.

### 5.5 Condição de pesquisa

Abrange:

- finalidade e protocolo;
- definição e assignment da condição;
- participante, consentimento e retirada;
- eventos e instrumentos autorizados;
- medida, constructo, interpretação e plano de análise;
- missing data, fidelity e outcome;
- provenance e diff de variantes;
- retenção, acesso, exportação e equivalência entre implantações.

A cadeia obrigatória é:

```text
finalidade
→ protocolo
→ condição
→ evento autorizado ou instrumento
→ medida
→ constructo
→ interpretação
→ decisão ou intervenção
```

Nenhum elo é inferido automaticamente do anterior.

### 5.6 Direitos e acessibilidade

Direitos, segurança, acessibilidade, confidencialidade e licenciamento atravessam as demais camadas.

Uma acomodação pode alterar a experiência ou o formato de resposta. Quando isso afetar o constructo ou a comparabilidade, o efeito deve ser registrado; a pessoa não perde o direito por causa da condição experimental.

## 6. Autoridade e precedência

A resolução utiliza a seguinte ordem:

1. lei, segurança, ética, acessibilidade mínima, confidencialidade e restrições de licença;
2. consentimento, recusa, retirada e direitos do participante;
3. protocolo e condição de pesquisa aprovados;
4. política institucional, avaliação, catálogo e publicação;
5. reviews e approvals qualificados exigidos;
6. política do workspace, curso, autor, professor ou tutor;
7. escolha do estudante e acomodação no espaço permitido;
8. perfil-base e defaults determinísticos;
9. regra adaptativa validada e explicitamente autorizada;
10. recomendação de IA;
11. verificação de capacidade técnica.

A capacidade técnica não é autoridade. Quando uma capacidade estiver ausente:

- o sistema usa somente fallback já autorizado;
- ou declara `unsupported`/`unavailable`;
- nunca degrada silenciosamente a condição ou a experiência.

### 6.1 Locks

Um lock deve registrar:

- parâmetro e valor;
- escopo;
- autoridade;
- motivo;
- versão;
- duração ou evento de término;
- possibilidade de override;
- tratamento de conflito.

### 6.2 Overrides

Um override precisa declarar:

- valor substituído;
- valor efetivo;
- escopo;
- origem e autoridade;
- justificativa;
- efeito sobre conteúdo, composição, condição e comparabilidade;
- possibilidade de reversão.

### 6.3 Consentimento

Consentimento não é apenas um valor booleano de interface. Ele precisa ser ligado a finalidade, dados, acesso, retenção, retirada e consequência da recusa.

## 7. Configuração efetiva

### 7.1 Entradas

A resolução conceitual recebe:

- versão da taxonomia;
- perfil de implantação e capacidades;
- perfil-base;
- overlays;
- política institucional e do workspace;
- configuração do curso;
- locks do protocolo/condição;
- overrides de módulo, lição, microssequência, ocorrência, card ou resource;
- preferências e acomodações do estudante;
- decisões adaptativas ou propostas de IA aceitas;
- estado de disponibilidade e fallback.

### 7.2 Algoritmo conceitual

```text
1. validar versão, ids, valores e escopos
2. classificar camada de incidência
3. aplicar restrições legais, de direitos, acessibilidade, licença e confidencialidade
4. aplicar consentimento e retirada
5. aplicar locks de protocolo
6. aplicar políticas institucionais e gates
7. aplicar políticas de workspace/curso/autor
8. aplicar escolhas e acomodações permitidas
9. preencher lacunas com perfil e defaults
10. considerar regra adaptativa ou proposta de IA autorizada
11. validar dependências e incompatibilidades
12. validar capacidades e fallback
13. emitir snapshot, warnings, conflitos ou estado não suportado
```

### 7.3 Snapshot mínimo

Um snapshot reproduzível deve identificar conceitualmente:

- `taxonomyVersion`;
- perfil-base e overlays;
- perfil de implantação;
- valores efetivos, escopo e origem;
- locks e overrides;
- políticas institucionais;
- referências a preferências e acomodações protegidas;
- propostas adaptativas/IA aceitas;
- manifesto de versões de conteúdo;
- manifesto da composição e dependências;
- capacidades e fallbacks;
- instrumentos e eventos autorizados;
- provenance e derivação;
- warnings e combinações não suportadas;
- data, autoridade e identidade da decisão.

O schema e a persistência desses elementos pertencem às Issues #6 e #7.

## 8. Conteúdo, composição e o JSON de curso

A taxonomia não exige inserir os 205 parâmetros em cada artefato.

A direção aceita é:

```text
perfil versionado
+ sparse overrides
+ referências a conteúdo/composição
+ locks de condição
→ configuração efetiva resolvida
```

O GPT deve receber somente:

- metadados resumidos;
- perfil aplicável;
- parâmetros relacionados à operação atual;
- contratos específicos;
- contexto autorizado;
- diffs e findings necessários.

Parâmetros que transformam conteúdo devem orientar geração ou revisão e produzir nova versão. Parâmetros de runtime podem permanecer fora do conteúdo materializado, desde que o snapshot preserve sua resolução.

## 9. Microssequências e curso composto

A integração preserva como hipótese obrigatória, ainda não como decisão de domínio:

```text
microssequência versionada
→ ocorrência/posição em composição de curso
→ composição versionada
→ snapshot local autossuficiente
→ estado contextual por curso/versão/posição/card
```

Essa hipótese é compatível com:

- autoria e reparo granular;
- contexto seletivo para GPT+MCP;
- reutilização com provenance;
- cursos derivados sob parâmetros diferentes;
- dependências explícitas;
- materialização offline;
- comparação entre condições.

A Issue #6 deve aceitar, revisar ou rejeitar explicitamente:

- a microssequência como unidade reutilizável;
- a identidade de ocorrência/placement;
- a relação entre curso completo e unidades independentes;
- reference, copy, fork e snapshot;
- transferência ou não de estado entre cursos.

A Issue #7 decidirá persistência, IndexedDB ou alternativa, sincronização, deduplicação, revogação e deletion.

## 10. Perfis e overlays

Perfis são configurações nomeadas, versionadas e explicáveis. A taxonomia mantém 38 perfis canônicos originados dos cinco pacotes.

### AI-assistance

- `ai-assisted-authoring`
- `ai-assisted-study`
- `institutional-governed-ai`
- `personal-ai-assisted-author`

### accessibility-rights

- `accessibility-first-overlay`
- `accessibility-overlay`
- `accessibility-quality-overlay`
- `participant-rights-overlay`

### authoring-publication-governance

- `collaborative-course-team`
- `external-expert-review-overlay`
- `institutional-controlled-publication`
- `institutional-quality-assurance`
- `open-oer-publication`
- `personal-manual-author`

### formal-teaching-assessment

- `formal-formative-course`
- `formal-mastery-course`
- `summative-institutional`
- `summative-prerequisite-course`
- `teacher-guided-shared-control`

### institutional-confidential

- `confidential-institutional`

### offline-mobile

- `deterministic-offline`
- `interruptible-mobile-overlay`
- `offline-authoring-overlay`
- `offline-research-overlay`

### reference

- `aralearn-reference`

### research

- `qualitative-development`
- `research-between-participant`
- `research-condition`
- `research-locked-authoring`
- `research-locked-condition`
- `research-locked-sequence`
- `research-within-participant`

### self-directed-learning

- `personal-reflective`
- `self-directed-guided`
- `self-directed-mastery`
- `self-directed-reflective`

### support-expertise

- `expert-efficiency-overlay`
- `novice-support-overlay`

### 10.1 Regra de composição

- um perfil-base por configuração efetiva;
- zero ou mais overlays compatíveis;
- overrides esparsos;
- direitos e acessibilidade não podem ser removidos por overlay;
- research locks atingem somente dimensões declaradas;
- perfil institucional não se propaga automaticamente para workspace pessoal;
- aplicação de perfil produz diff e snapshot;
- conflito não é resolvido por ordem de carregamento implícita.

## 11. Dependências e incompatibilidades estruturais

### 11.1 Dependências obrigatórias

- mastery exige evidence basis, criterion, scope, remediation, override e recheck;
- adaptação exige target, trigger, evidence basis, authority, application mode, transparency, override, rollback, snapshot e fallback;
- IA exige function, initiation, context, grounding, status, authority, validation/review, provenance, editability, contestability, data boundary e failure behavior;
- medida exige fórmula, unidade, janela, entradas, missingness, limitações e uso permitido;
- publicação exige revision, audience, gate e authority;
- reuse exige origin, relation, context-fit, licence e update policy;
- reparo exige target, authority, scope, new revision e regression/reaudit policy;
- condição comparativa exige content/configuration/composition/capability/instrument diff.

### 11.2 Combinações não suportadas

- `published` com mutação in-place;
- condition lock com atualização silenciosa;
- AI recommendation com autoridade final implícita;
- accessibility disabled;
- automatic adaptation sem evidence/snapshot/override/rollback;
- consequential assessment sem autoridade, contestação e acomodação;
- event collection sem purpose binding e access/retention;
- reuse por referência com propagação automática não declarada;
- hard delete de conteúdo ainda referenciado ou retido;
- fallback técnico que altera a condição sem registro;
- auditoria que repara na mesma operação e ainda se declara independente.

## 12. Adiados

A integração deduplicou 37 registros de origem em **36 candidatos adiados únicos**.

Famílias principais:

- learner models, mastery estimators, schedulers e branching adaptativo;
- detecção automática de struggle, expertise, emoção ou neurotipo;
- personalização generativa runtime;
- scoring aberto autoritativo por IA;
- event schema, metric catalogue, early warning e participant collection;
- manifesto técnico, content-addressed storage, PROV/C2PA internos;
- verificação automática de fontes e licenças;
- cross-course repair/update e semantic auto-merge;
- marketplace e sistemas de reputação.

O catálogo completo está em `research/data/issue4-final-deferred-candidates-v1.csv`.

## 13. Rejeitados

Foram consolidados 41 princípios rejeitados ou não recomendados. Eles incluem:

- modos monolíticos;
- defaults universais sem contexto;
- inferências de constructo a partir de traces brutos;
- ranking público;
- IA como autoridade final;
- hidden adaptation;
- acessibilidade opcional;
- coleta total de eventos;
- dashboard universal;
- retenção indefinida;
- silent mutation e silent propagation;
- free-text tags como única relação;
- hard delete sem impacto;
- licença de pacote que oculta ativos;
- superadministrador global;
- linguagem técnica como UX primária.

O catálogo completo está em `research/data/issue4-final-rejected-principles-v1.csv`.

## 14. Validação integrada

A taxonomia foi validada conceitualmente em 15 cenários:

1. estudo pessoal AraLearn offline;
2. estudo reflexivo opt-in;
3. curso formal formativo;
4. mastery com soft prerequisites;
5. avaliação somativa institucional;
6. experimento entre participantes com variantes;
7. desenho intraparticipante;
8. acomodação em conflito com condição;
9. construção GPT+MCP e reparo situado no ARA;
10. update de microssequência reutilizada;
11. publicação OER;
12. autoria institucional confidencial;
13. capacidade conectada indisponível offline;
14. withdrawal, deletion e retenção;
15. publicação com separation of duties.

Todos passaram no nível de coerência conceitual. Isso não demonstra:

- efetividade educacional;
- usabilidade;
- viabilidade de armazenamento;
- desempenho;
- segurança de uma implementação;
- validade de instrumentos específicos.

## 15. Perfil AraLearn integrado

O perfil de referência preserva:

- curso → módulo → lição → microssequência → card como estrutura inicial;
- teoria e prática;
- progressão estrutural não punitiva;
- learner pacing;
- reveal solicitado;
- feedback acionável;
- ausência de ranking e nota por padrão;
- ausência de card timer;
- estado funcional mínimo;
- estudo mobile/offline;
- comments situados;
- autoria por partes;
- plan → build → audit → repair → re-audit;
- revisions e publication explícitos;
- GPT+MCP subordinado à autoridade humana;
- ARA como superfície de inspeção e intervenção.

Ele não se torna default universal para contexto formal, pesquisa ou instituição.

## 16. Handoff normativo para a Issue #5

A Issue #5 deve importar sem reabrir:

- finalidade, protocolo, condição, assignment e version lock;
- participante, identity mode, consent e withdrawal;
- event authorization e semantic profile;
- instrument type/admin;
- measure, construct, interpretation, outcome e analysis plan;
- missing data e fidelity;
- provenance e variant diff;
- data purpose, retention, access e export;
- personal analytics, role-oriented questions e explanations;
- intervention policy;
- cross-deployment equivalence;
- operational telemetry separation.

A Issue #5 deverá definir objetos e fórmulas normativos, não alterar a taxonomia pedagógica de P1–P3 nem a governança autoral de P5.

## 17. Requisitos candidatos para a Issue #6

A Issue #6 deverá decidir normativamente:

- profile, overlay, sparse override e effective snapshot;
- autoridade, lock, override, exception e unsupported combination;
- entidades de curso, microssequência, card, placement e dependency;
- conteúdo, composição e variante;
- reference, copy, fork, adaptation e translation;
- workspace, role, permission e approval;
- annotation, finding, review, repair e re-audit;
- revision, publication, withdrawal, supersession, archive e deletion;
- provenance, grounding, source anchor, licence e confidentiality;
- research protocol, condition, participant e evidence;
- personal, private, shared, institutional, confidential e public states;
- capacidade built-in, optional local, connected, unavailable e fallback.

A Issue #6 poderá rejeitar hipóteses de domínio, mas precisará registrar a decisão e a migração conceitual.

## 18. Handoffs para arquitetura e UX

### Issue #7

- resolução determinística de configuração;
- artefatos e snapshots;
- persistência e materialização offline;
- synchronization e conflict handling;
- capability discovery e explicit unavailability;
- context authorization e selective MCP loading;
- provenance, event transport e exports;
- storage/cost budgets;
- managed e self-hosted equivalence.

### Issue #8

- forms por perfil e sparse overrides;
- progressive disclosure;
- previews e diffs de consequência;
- rendering em tempo real da autoria;
- comments/findings/review queues;
- version selection, rollback e publication;
- dependency/composition views;
- analytics por pergunta e papel;
- accessibility, mobile, offline e idiomas;
- explicações de locks, authority, unsupported e fallback.

## 19. Critérios de aceite da Issue #4

| critério | resultado |
|---|---|
| perfil AraLearn versionado | atendido |
| descoberta além do AraLearn | atendido |
| relação de cada parâmetro com AraLearn | preservada nos CSVs de origem |
| maturidade e evidência | preservadas nos registros |
| parâmetros estruturais e comportamentais distinguíveis | atendido pelas camadas |
| design-time, study-time, assessment, research e governance | atendido |
| learner, author, accessibility, institution e protocol separados | atendido |
| precedência, locking, override e consent | atendido |
| snapshots reproduzíveis | definidos conceitualmente |
| conflitos, dependências e unsupported | atendido |
| aceitos, adiados e rejeitados preservados | atendido |
| handoff para #5–#8 | atendido |
| implementação evitada | atendido |

## 20. Estado final e não autorizações

A primeira taxonomia está aceita como handoff normativo. A Issue #4 pode ser encerrada após revisão e merge desta entrega.

Esta síntese não autoriza:

- schema de produção;
- banco ou Storage;
- stores do IndexedDB;
- MCP endpoints;
- stack ou arquitetura;
- UI;
- event store;
- analytics implementados;
- coleta de participantes;
- scheduler, learner model ou adaptação automática;
- cross-course repair ou update automático;
- código ou migração.

Revisões futuras da taxonomia devem:

1. criar nova versão;
2. identificar o parâmetro alterado;
3. preservar aliases e origem;
4. registrar evidência e decisão;
5. avaliar efeitos em perfis, snapshots e estudos existentes;
6. não reescrever silenciosamente P1–P5.
