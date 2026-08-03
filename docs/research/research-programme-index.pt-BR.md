# Índice canônico do programa de pesquisa

**Estado:** canônico para planejamento de pesquisa  
**Idioma:** `pt-BR`  
**Última revisão:** 3 de agosto de 2026

## 1. Finalidade

Este índice organiza a pesquisa necessária para definir o ARA sem transferir ao proprietário o trabalho de interpretar um corpus bruto.

Cada frente deverá entregar:

- conclusão principal;
- caminho recomendado;
- alternativas relevantes;
- alternativas adiadas ou rejeitadas;
- justificativa;
- riscos;
- incertezas capazes de alterar a decisão;
- implicações para parametrização, produto, arquitetura, UX ou avaliação.

A pesquisa é ampla e finita. O objetivo é evidência suficiente para decidir, não exaustão universal.

## 2. Estados de cobertura

| Estado | Significado |
|---|---|
| `concluído` | Pacote decisório entregue e incorporado à fase corrente. |
| `baseline-concluído` | Existe síntese suficiente para iniciar modelagem, com limitações registradas. |
| `parcial` | Há evidência útil, mas falta síntese focada. |
| `exploratório` | Existem precedentes ou literatura inicial, insuficientes para decisão normativa. |
| `não-iniciado` | A frente precisa de protocolo e corpus próprios. |
| `contínuo` | A pesquisa permanece aberta quando decisões futuras exigirem atualização. |

## 3. Evidência já produzida

### 3.1 P1 — prática, resposta, tentativas, reveal, feedback e consequências

**Estado:** `concluído` para a primeira taxonomia.  
**PR:** #45.

Artefatos:

- `research/searches/2026-08-03-p1-pratica-resposta-feedback-protocolo.md`;
- `research/data/p1-evidence-corpus-01.csv`;
- `research/data/p1-parameter-records-01.csv`;
- `research/data/p1-profile-comparison-01.csv`;
- `research/data/p1-decision-synthesis-01.json`;
- `research/pt-BR/p1-sintese-pratica-resposta-tentativas-feedback-consequencias-01.md`;
- `research/library/referencias-formatos-feedback.bib`.

Resultado:

- 21 dimensões aceitas;
- prática, resposta, validade, crédito, tentativas, reveal, feedback e consequência separados;
- perfil AraLearn preservado como referência não punitiva;
- acessibilidade com precedência;
- tentativa e confiança não autorizam telemetry;
- ranking público rejeitado;
- nenhuma implementação autorizada.

### 3.2 P2 — progressão, sequência, revisão e apoio

**Estado:** `concluído` para a primeira taxonomia.  
**PR:** #47.

Artefatos:

- `research/searches/2026-08-03-p2-progressao-sequenciamento-revisao-protocolo.md`;
- `research/data/p2-evidence-corpus-01.csv`;
- `research/data/p2-parameter-records-01.csv`;
- `research/data/p2-profile-comparison-01.csv`;
- `research/data/p2-decision-synthesis-01.json`;
- `research/pt-BR/p2-sintese-progressao-sequenciamento-revisao-scaffolding-01.md`;
- `research/library/referencias-progressao-sequenciamento.bib`.

Resultado:

- 36 dimensões aceitas;
- conclusão estrutural separada de mastery;
- evidência, critério, remediação, override e rechecagem explícitos;
- autoridade de sequência separada de ritmo;
- spacing separado de interleaving;
- agenda, horizonte, carga e adiamento separados;
- exemplos, scaffolding, segmentação e retomada representados;
- scheduler, learner model, branching e detecção automática adiados;
- nenhuma implementação autorizada.

### 3.3 P3 — autonomia, autorregulação, adaptação, acessibilidade e IA

**Estado:** `concluído` para a primeira taxonomia.  
**PR:** a registrar após integração.

Artefatos:

- `research/searches/2026-08-03-p3-autonomia-adaptacao-acessibilidade-IA-protocolo.md`;
- `research/data/p3-evidence-corpus-01.csv`;
- `research/data/p3-parameter-records-autonomy-adaptation-01.csv`;
- `research/data/p3-parameter-records-accessibility-ai-01.csv`;
- `research/data/p3-profile-comparison-01.csv`;
- `research/data/p3-decision-synthesis-01.json`;
- `research/pt-BR/p3-sintese-autonomia-adaptacao-acessibilidade-IA-01.md`;
- `research/library/referencias-autonomia-adaptacao-acessibilidade-IA.bib`.

Resultado:

- 34 fontes estruturadas;
- 50 dimensões aceitas;
- nove perfis e overlays;
- autonomia separada de controle irrestrito;
- autorregulação representada por suportes explícitos, não por traço inferido;
- adaptação separada de acomodação e aplicação automática;
- acessibilidade tratada como baseline e precedência;
- IA dividida por função, contexto, status, autoridade, revisão, validação, provenance, dados e falha;
- `preview-only` e `recommend-and-confirm` recomendados para propostas de IA;
- ciclo `suggestion → draft → validated-structure → audited → human-approved → published`;
- chat/MCP e ARA definidos como canais complementares;
- perfis e overrides esparsos recomendados para reduzir carga do GPT e do usuário;
- estudo baseline independente de LLM conectada;
- nenhuma tecnologia, schema, UI ou implementação autorizada.

### 3.4 Evidência contextual e técnica já disponível

Também permanecem como entradas:

- Issue #30 / PR #43 — síntese AraLearn + horizonte externo;
- Issue #31 / PR #32 — auditoria dos resources do AraLearn;
- Issues #33–#34 / PR #35 — benchmark de sistemas e gêneros;
- Issues #36, #38 e #40 — experimentos técnicos não normativos;
- Issue #42 — bake-off adiado, sem resultado de runtime.

Programação executável, representações múltiplas, extensibilidade e runtimes continuam candidatos sujeitos às Issues #6 e #7.

## 4. Pacotes da primeira taxonomia — Issue #4

P1, P2 e P3 estão concluídos. Pacotes são subdivisões operacionais da Issue #4; não geram novas issues automaticamente.

### P4 — próximo pacote

**Escopo:** instrumentação, condições experimentais, analytics e governança.

**Pergunta:** como representar pesquisa e analytics sem confundir evento, medida, constructo e inferência, sem transformar estudo pessoal em vigilância e sem perder comparabilidade entre configurações, variantes, versões e implantações?

P4 deverá receber:

#### De P1

- `telemetry.attempt_capture`;
- confiança opcional;
- prática, resposta, feedback e consequência;
- inferências proibidas sobre tentativa, erro e tempo.

#### De P2

- progressão e mastery claims;
- schedules, load budgets e deferral;
- snapshots de sequência e apoio;
- proibição de inferir struggle ou expertise de sinais brutos.

#### De P3

- autonomia e consentimento;
- adaptação e effective-state snapshots;
- acessibilidade e dados sensíveis;
- funções, contexto, modelo/provedor, output status e cadeia de revisão da IA;
- retenção mínima de chat;
- contestação e override;
- condições com IA bloqueada ou ausente.

#### Das hipóteses de produto registradas após P2

- cursos derivados sob parametrizações diferentes;
- parâmetros de runtime versus conteúdo/materialização;
- composição por microssequências e ocorrências contextuais;
- conteúdo/configuração diffs;
- dependências dentro e entre cursos;
- materialização offline;
- comentários e reparos situados;
- analytics simples por papel;
- custos de armazenamento, eventos e revisão.

Pesquisa focada:

- learning analytics;
- event vocabularies;
- experimentos e condições versionadas;
- assignment e comparabilidade;
- instrumentos quantitativos e qualitativos;
- consentimento, retirada, pseudonimização e retenção;
- medidas, constructos e inferências proibidas;
- personal analytics;
- analytics para professores, tutores e pesquisadores;
- proveniência e equivalência entre implantações;
- custo de coleta, armazenamento e processamento;
- visualização compreensível sem ocultar auditabilidade.

Entrega:

- parâmetros de instrumentação e governança;
- modelo conceitual evento → medida → constructo → interpretação;
- condições e snapshots reproduzíveis;
- personal analytics separado de pesquisa/instituição;
- regras de consentimento, retenção, exportação e acesso;
- métricas candidatas com perguntas e limitações;
- inferências proibidas;
- perfis contrastantes;
- handoff para Issue #5 e #6.

P4 não autoriza coleta, banco de eventos, dashboard, fórmulas de produção, experimentos com participantes ou código.

### P5 — futuro

**Escopo:** autoria, revisão, reparo, publicação e políticas institucionais.

Deverá investigar:

- autoria humano–IA;
- planner/builder/auditor/repairer;
- ChatGPT+MCP e ARA como dois canais;
- busca e composição de microssequências;
- contexto autorizado entre cursos;
- source anchoring e grounding;
- comentários e reparo localizado;
- revisão humana, pares e especialistas;
- versões, forks, diffs e publication gates;
- provenance, licenciamento e confidencialidade;
- workspaces, papéis e permissões;
- reutilização e retirada;
- políticas pessoais, acadêmicas e institucionais.

P5 deverá produzir parâmetros e requisitos candidatos, não ferramentas ou contratos de produção.

## 5. Frentes posteriores

### Issue #5 — protocolos, instrumentos e analytics

Consolidará normativamente:

- protocolo, condição e assignment;
- participante e direitos;
- evento, medida, constructo e interpretação;
- instrumentos e evidência qualitativa;
- personal versus research analytics;
- exportação e equivalência;
- governança e custo.

### Issue #6 — produto e domínio

Decidirá:

- atores, jornadas, entidades e estados;
- curso, microssequência, card e composição;
- perfil, override, effective configuration e snapshot;
- versões, ocorrências, referências e provenance;
- autoria, observação, auditoria, reparo e publicação;
- reutilização, forks, compartilhamento, retirada e exclusão;
- conteúdo pessoal, institucional, confidencial e público;
- integração da taxonomia e do modelo de pesquisa.

A premissa provisória de curso como objeto completo deverá ser revisitada explicitamente diante da hipótese de composição por microssequências.

### Issue #7 — arquitetura e stack

Comparará:

- persistência e materialização;
- manifests, artefatos e referências;
- IndexedDB e alternativas locais;
- sincronização e conflitos;
- deduplicação e copy-on-write;
- providers e gateways de IA;
- schemas e contratos;
- MCP e carregamento seletivo;
- managed e self-hosted;
- segurança, backup, atualização e rollback;
- custos e exit strategy.

Saída: recomendações e ADRs, não catálogo bruto.

### Issue #8 — UX/UI

Pesquisará e especificará:

- acompanhamento da autoria em tempo real;
- chat e ARA como canais complementares;
- formulários de parâmetros;
- perfis e progressive disclosure;
- preview, diff, versões e publicação;
- comentários e reparo;
- dependências e composição;
- analytics por papel;
- acessibilidade, mobile, offline e multilinguismo.

### Issue #9 — releases e implementação

Produzirá release slicing, quality gates, segurança, acessibilidade, migração, rollback, evidence packages e issues executáveis pelo Codex.

## 6. Critérios gerais de suficiência

Uma frente pode avançar quando:

1. possui síntese confiável ou conjunto justificado de fontes primárias;
2. contém casos contrastantes e limitações;
3. cobre stakeholders e contextos decisivos;
4. duas adições sucessivas não criam categoria decisiva nem alteram a recomendação;
5. incertezas remanescentes estão explícitas;
6. a decisão pode evoluir sem perder rastreabilidade;
7. nenhuma fonte indispensável é substituída por suposição.

## 7. Papel do proprietário

O proprietário receberá síntese, recomendação, justificativa, alternativas, riscos e incertezas decisivas.

Não receberá como produto final lista extensa de artigos, catálogo sem recomendação ou pergunta genérica para arquitetar sozinho.

Sua decisão será solicitada somente diante de conflito estratégico ou valorativo não resolvido pela evidência.

## 8. Próxima entrega verificável

A próxima entrega é o **Pacote P4 da Issue #4**.

A Issue #4 permanece aberta até P4, P5 e a síntese final da taxonomia. Nenhum código, schema de produção, adapter, analytics ou UX é autorizado durante esses pacotes.
