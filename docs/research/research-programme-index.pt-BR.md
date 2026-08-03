# Índice canônico do programa de pesquisa

**Estado:** canônico para planejamento de pesquisa  
**Idioma:** `pt-BR`  
**Última revisão:** 3 de agosto de 2026

## 1. Finalidade

Este índice organiza a pesquisa necessária para definir o ARA sem transferir ao proprietário o trabalho de interpretar corpus bruto. Cada pacote entrega conclusão, recomendação, alternativas, riscos, incertezas, parâmetros, perfis e handoffs. A pesquisa é ampla e finita: busca evidência suficiente para decidir.

## 2. Pacotes da Issue #4

### P1 — concluído — PR #45

**Escopo:** prática, resposta, tentativas, reveal, feedback, consequências e acessibilidade.  
**Resultado:** 21 dimensões; perfil AraLearn não punitivo; prática separada de medição; telemetry adiada; ranking público rejeitado.

### P2 — concluído — PR #47

**Escopo:** progressão, mastery, sequência, ritmo, spacing, revisão, exemplos, scaffolding, segmentação e retomada.  
**Resultado:** 36 dimensões; conclusão estrutural separada de mastery; sequência separada de ritmo; spacing separado de interleaving; scheduler e adaptação automática adiados.

### P3 — concluído — PR #48

**Escopo:** autonomia, autorregulação, adaptação, acessibilidade e assistência por IA.  
**Resultado:** 34 fontes, 50 dimensões e nove perfis; shared control; acessibilidade como baseline; IA delimitada; `preview-only`/`recommend-and-confirm`; ciclo `suggestion → draft → validated-structure → audited → human-approved → published`; GPT+MCP e ARA como canais complementares.

### P4 — concluído — PR #49

**Escopo:** instrumentação, condições experimentais, analytics e governança.  
**Resultado:** 36 fontes, 31 dimensões e nove perfis. Cadeia obrigatória:

```text
finalidade → protocolo → condição → evento/instrumento
→ medida → constructo → interpretação → decisão/intervenção
```

Eventos são seletivos; analytics pessoais, pedagógicos, de pesquisa e operacionais permanecem separados; variantes exigem snapshots e diffs; coleta, event store, dashboards, predição e early warning foram adiados.

### P5 — concluído — PR desta branch

**Escopo:** autoria, revisão, auditoria, reparo, anotações, versões, reutilização, publicação, licenciamento e governança institucional.

**Resultado:** 43 fontes, 67 dimensões e 11 perfis. Decisões principais:

- autoria é sequência governada de contribuições, estados e decisões;
- GPT+MCP e ARA são canais complementares;
- planejamento, construção, validação, auditoria, reparo, reauditoria, aprovação e publicação permanecem distintos;
- o mesmo GPT pode exercer papéis em rodadas separadas, mas não herda autoridade de aprovação/publicação;
- contexto é mínimo, autorizado e versionado; memória do chat não concede acesso;
- grounding, source anchors, contribution attribution e provenance são explícitos;
- findings e comentários possuem alvo, motivação, visibilidade, estado e vínculo de resolução;
- reparo semântico cria revisão; publicado/condição bloqueada não sofre mutação silenciosa;
- referência, cópia, fork, adaptação e tradução são modos diferentes;
- atualizações usam notify/preview, não propagação automática;
- `published` declara audiência; withdrawal, supersession, archive e deletion são distintos;
- licenças e materiais de terceiros são registrados por escopo;
- workspaces, papéis, separação de deveres e gates variam por perfil e risco;
- administração usa linguagem pedagógica e filas orientadas a perguntas;
- schemas, banco, Storage, sync, MCP e UI permanecem adiados.

Artefatos P5:

- `research/searches/2026-08-03-p5-autoria-revisao-publicacao-protocolo.md`;
- `research/data/p5-evidence-corpus-01.csv`;
- `research/data/p5-parameter-records-01.csv`;
- `research/data/p5-profile-comparison-01.csv`;
- `research/data/p5-decision-synthesis-01.json`;
- `research/pt-BR/p5-sintese-autoria-revisao-publicacao-governanca-01.md`;
- `research/library/referencias-autoria-revisao-publicacao.bib`.

Os artefatos estruturados prevalecem sobre resumos posteriores.

## 3. Hipóteses transversais preservadas

Permanecem `discovered`, não normativas:

- parâmetros de runtime, conteúdo/materialização, composição/dependências, lifecycle e condição;
- microssequência versionada como candidata a unidade autoral/reutilizável;
- curso como composição versionada de ocorrências contextuais;
- snapshot offline autossuficiente;
- estado por curso/versão/posição/card;
- catálogo + perfil + overrides esparsos;
- cursos derivados com invariantes e diffs;
- administração em linguagem pedagógica.

A Issue #6 decidirá o domínio, a #7 a arquitetura e a #8 a UX.

## 4. Próxima entrega: síntese final da Issue #4

Antes de avançar para #5, integrar P1–P5 em uma primeira taxonomia coerente e versionada. A síntese final deverá:

- deduplicar e harmonizar os parâmetros aceitos;
- organizar famílias e níveis de incidência;
- consolidar perfis e overlays;
- formalizar autoridade, precedência, consentimento, locking e override;
- registrar dependências, incompatibilidades e combinações não suportadas;
- distinguir configuração, conteúdo/materialização, composição, lifecycle e condição experimental;
- definir effective configuration e snapshots em nível conceitual;
- preservar aceitos, adiados e rejeitados com rationale;
- validar cenários pessoais, acadêmicos, institucionais, confidenciais e offline;
- produzir handoff normativo para #5 e requisitos candidatos para #6;
- não definir schema, arquitetura, UX ou implementação.

## 5. Frentes posteriores

- **Issue #5:** protocolos, participantes, assignment, eventos, instrumentos, medidas, constructos, interpretações, direitos, governança, exportação e equivalência.
- **Issue #6:** atores, jornadas, entidades, composição, versões, referências, autoria, observações, auditoria, reparo, publicação, reutilização, retirada e integração da taxonomia.
- **Issue #7:** persistência, materialização, manifests, IndexedDB e alternativas, sincronização, provenance, providers, managed/self-hosted, custos e exit strategy.
- **Issue #8:** formulários, perfis, progressive disclosure, rendering em tempo real, versões, diffs, comments, review queues, analytics por papel, acessibilidade e offline.
- **Issue #9:** releases, quality gates, migração, rollback, evidence packages e backlog executável.

## 6. Critérios de suficiência

Uma frente pode avançar quando possui fontes confiáveis, casos contrastantes, stakeholders/contextos decisivos, saturação decisória, incertezas explícitas e rastreabilidade. Nenhuma fonte indispensável pode ser substituída por suposição.

## 7. Próxima entrega verificável

A próxima entrega é a **síntese integrada final da Issue #4**. Nenhum código, schema, adapter, coleta, dashboard, arquitetura ou UX é autorizado.
