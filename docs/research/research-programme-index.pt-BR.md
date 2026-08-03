# Índice canônico do programa de pesquisa

**Estado:** canônico para planejamento de pesquisa  
**Idioma:** `pt-BR`  
**Última revisão:** 3 de agosto de 2026

## 1. Finalidade

Este índice organiza a pesquisa necessária para definir o ARA sem transferir ao proprietário o trabalho de interpretar corpus bruto.

Cada pacote deve entregar conclusão, recomendação, alternativas, riscos, incertezas decisivas, parâmetros estruturados, perfis e handoffs. A pesquisa é ampla e finita: busca evidência suficiente para decidir, não exaustão universal.

## 2. Estados

- `concluído`: pacote decisório entregue e incorporado;
- `baseline-concluído`: evidência suficiente para iniciar modelagem;
- `parcial`: evidência útil sem síntese decisória completa;
- `exploratório`: precedentes ainda insuficientes;
- `não-iniciado`: exige protocolo próprio;
- `contínuo`: atualizado quando decisões futuras exigirem.

## 3. Pacotes da Issue #4

### P1 — concluído — PR #45

**Escopo:** prática, resposta, tentativas, reveal, feedback, consequências e precedência de acessibilidade.

**Resultado:** 21 dimensões aceitas; perfil AraLearn não punitivo preservado; prática separada de medição e consequência; telemetry de tentativas adiada; ranking público rejeitado.

Artefatos: `research/data/p1-*`, `research/pt-BR/p1-*`, protocolo e bibliografia P1.

### P2 — concluído — PR #47

**Escopo:** progressão, mastery, sequência, ritmo, spacing, revisão, exemplos, scaffolding, segmentação e retomada.

**Resultado:** 36 dimensões aceitas; conclusão estrutural separada de mastery; sequência separada de ritmo; spacing separado de interleaving; scheduler, learner model e detecção automática adiados.

Artefatos: `research/data/p2-*`, `research/pt-BR/p2-*`, protocolo e bibliografia P2.

### P3 — concluído — PR #48

**Escopo:** autonomia, autorregulação, adaptação, acessibilidade e assistência por IA.

**Resultado:** 34 fontes, 50 dimensões e nove perfis; shared control; acessibilidade como baseline e precedência; IA como assistente delimitado; `preview-only` e `recommend-and-confirm`; ciclo `suggestion → draft → validated-structure → audited → human-approved → published`; chat/MCP e ARA como canais complementares.

Artefatos: `research/data/p3-*`, `research/pt-BR/p3-*`, protocolo e bibliografia P3.

### P4 — concluído — PR pendente

**Escopo:** instrumentação, condições experimentais, analytics e governança.

**Resultado:** corpus de 36 fontes, 31 dimensões e nove perfis. A cadeia obrigatória é:

```text
pergunta/finalidade
→ protocolo
→ condição
→ evento autorizado ou instrumento
→ medida
→ constructo
→ interpretação
→ decisão/intervenção
```

Decisões principais:

- perfil AraLearn data-minimal preservado como baseline pessoal;
- protocolos e condições são objetos versionados e reproduzíveis;
- eventos são seletivos e vinculados à finalidade;
- evento, medida, constructo e inferência não se confundem;
- toda medida exige fórmula, unidade, janela, missingness, limites e uso permitido;
- consentimento, retirada, minimização, retenção, acesso e exportação são parâmetros;
- analytics pessoais, pedagógicos, de pesquisa e operacionais têm autoridades separadas;
- painéis respondem perguntas por papel, não expõem um dashboard técnico universal;
- variantes de curso exigem diff de conteúdo, configuração, composição, capacidades e instrumentos;
- Caliper/xAPI são candidatos de mapeamento, não o domínio do ARA;
- telemetria operacional permanece separada de learning analytics;
- event store, métricas de produção, early warning, coleta e dashboards foram adiados.

Artefatos:

- `research/searches/2026-08-03-p4-instrumentacao-analytics-governanca-protocolo.md`;
- `research/data/p4-evidence-corpus-01.csv`;
- `research/data/p4-parameter-records-01.csv`;
- `research/data/p4-profile-comparison-01.csv`;
- `research/data/p4-decision-synthesis-01.json`;
- `research/pt-BR/p4-sintese-instrumentacao-condicoes-analytics-governanca-01.md`;
- `research/library/referencias-instrumentacao-analytics-governanca.bib`.

### P5 — próximo pacote

**Escopo:** autoria, revisão, auditoria, reparo, publicação e políticas institucionais.

**Pergunta:** como o ARA deve organizar autoria humano–IA, busca e composição de microssequências, contexto autorizado, revisão, comentários, reparo, versões, provenance, publicação, permissões e retirada sem reduzir o controle humano nem sobrecarregar GPT e usuário?

Pesquisa focada:

- human–AI co-authoring e mixed-initiative systems;
- planner, builder, auditor, repairer e reauditor;
- ChatGPT+MCP e ARA como dois canais;
- autoria modular, objetos educacionais e composição curricular;
- busca/reuso/fork de microssequências;
- grounding, source anchoring e provenance;
- comentários situados, revisão e reparo localizado;
- peer/expert review e quality assurance;
- versionamento, diffs, gates, publicação e rollback;
- workspaces, papéis, permissões e separação de deveres;
- licenciamento, confidencialidade, retirada, exclusão e referências;
- políticas pessoais, acadêmicas e institucionais;
- administração simples para autores não técnicos.

Entrega:

- parâmetros e perfis de autoria/governança;
- estados e autoridade do ciclo de produção;
- políticas de contexto, busca, reuse, fork, auditoria, publicação e retirada;
- riscos, alternativas e inferências proibidas;
- handoff para #5, #6, #7 e #8.

P5 não autoriza MCP de produção, schema, UI, banco, Storage, versionamento técnico ou código.

## 4. Hipóteses transversais obrigatórias

As seguintes hipóteses permanecem `discovered`, não normativas:

- níveis de parametrização: runtime, conteúdo/materialização, composição/dependências, ciclo de vida e condição experimental;
- microssequência versionada como candidata a unidade autoral/reutilizável;
- curso como composição versionada de ocorrências contextuais;
- snapshot local autossuficiente para uso offline;
- estado por curso/versão/posição/card, não apenas por microssequência;
- chat/MCP para direção semântica e ARA para visualização e operações determinísticas;
- catálogo versionado + perfil + overrides esparsos;
- administração em linguagem pedagógica, não de banco ou Storage;
- cursos derivados com invariantes e diffs explícitos para pesquisa.

A Issue #6 decidirá o domínio; a #7 decidirá arquitetura e persistência; a #8 decidirá UX.

## 5. Frentes posteriores

### Issue #5

Consolidará protocolo, condição, participant, assignment, eventos, instrumentos, medidas, constructos, interpretações, direitos, governança, exportação e equivalência.

### Issue #6

Definirá atores, jornadas, entidades, estados, composição, versões, referências, autoria, observação, auditoria, reparo, publicação, reutilização, retirada e integração da taxonomia.

### Issue #7

Comparará persistência, materialização, manifests, IndexedDB e alternativas, sincronização, event transport, pseudonimização, adapters, managed/self-hosted, custos e exit strategy.

### Issue #8

Especificará formulários, perfis, progressive disclosure, acompanhamento em tempo real, versões, diffs, comentários, dependências, analytics por papel, acessibilidade e offline.

### Issue #9

Produzirá release slicing, quality gates, migração, rollback, evidence packages e issues executáveis pelo Codex.

## 6. Critérios de suficiência

Uma frente pode avançar quando:

1. possui fontes primárias ou síntese confiável;
2. contém casos contrastantes e limitações;
3. cobre stakeholders e contextos decisivos;
4. novas fontes não criam categoria decisiva nem alteram a recomendação;
5. incertezas remanescentes estão explícitas;
6. a decisão pode evoluir com rastreabilidade;
7. nenhuma fonte indispensável é substituída por suposição.

## 7. Próxima entrega verificável

A próxima entrega é o **Pacote P5 da Issue #4**.

A Issue #4 permanece aberta até P5 e a síntese final da taxonomia. Nenhum código, schema de produção, adapter, coleta, dashboard ou UX é autorizado durante esses pacotes.
