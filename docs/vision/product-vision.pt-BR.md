# Visão canônica atual do produto ARA

**Estado:** canônico para produto e domínio  
**Idioma de trabalho:** `pt-BR`  
**Última consolidação:** 3 de agosto de 2026  
**Autoridade:** integra a visão inicial, a síntese da Issue #30, `ara.configuration-taxonomy.v1`, `ara.research-framework.v1` e o modelo normativo da Issue #6.

## 1. Definição

ARA — Ambiente de Recursos de Aprendizagem / Learning Resources Environment — é o sucessor direto do AraLearn.

É uma plataforma aberta, configurável, mobile-first e offline-capable para:

- estudo autodirigido estruturado;
- autoria, revisão, auditoria e reparo assistidos por GPT+MCP;
- visualização e controle humano determinístico no ARA;
- ensino formal e tutoria quando habilitados;
- pesquisa educacional reproduzível;
- publicação pessoal, institucional, confidencial ou aberta;
- implantação gerenciada ou autogerenciada sem dependência do domínio em um provedor.

ARA preserva o perfil funcional do AraLearn — não punitivo, data-minimal, mobile/offline e human-in-the-loop — como primeira configuração completa, não como regra universal.

## 2. Estrutura educacional e composição

A estrutura inicial é:

```text
course → module → lesson → placement → microsequence revision → card
```

Decisões normativas:

- `MicrosequenceRevision` é a unidade autoral reutilizável inicial; não é declarada átomo universal permanente;
- `Placement` representa a ocorrência contextual de uma revisão em determinado curso;
- `CourseVersion` é um objeto pedagógico completo e imutável por sua composição, objetivos, dependências, configuração, provenance e publicação;
- conteúdo reutilizado pode aparecer em diversos cursos sem compartilhar automaticamente progresso ou mastery;
- dependências e cobertura usam referências estáveis e relações tipadas; tags textuais são apenas auxiliares de busca;
- alterações semânticas criam novas revisões; alterações de composição criam nova versão de curso.

Estado de estudo é contextual:

```text
learner/library context
+ study assignment
+ course version
+ placement
+ card occurrence
→ functional study state
```

## 3. Conteúdo e prática

Os seguintes conceitos permanecem separados:

- `ResourceInstance`: representação declarativa;
- `PracticeDefinition`: tarefa e operação cognitiva;
- `ResponseDefinition`: forma de resposta;
- `ValidatorPolicy`: validação determinística ou delimitada;
- `FeedbackPolicy`: conteúdo, momento e persistência do feedback.

Artefatos de curso não fornecem código executável arbitrário para renderers ou validators.

## 4. Parametrização

ARA utiliza `ara.configuration-taxonomy.v1`:

```text
taxonomy
+ base profile
+ overlays
+ policies/locks
+ sparse scoped overrides
+ content/composition versions
+ capability manifest
→ deterministic resolution
→ EffectiveConfigurationSnapshot
```

As camadas são:

1. runtime/configuração efetiva;
2. conteúdo/materialização;
3. composição/dependências;
4. lifecycle/governança;
5. condição de pesquisa;
6. direitos e acessibilidade, transversal.

Parâmetros transformadores de conteúdo ou composição não são switches de interface. Eles produzem novas revisões, derivações, variantes ou snapshots.

Acessibilidade, consentimento, retirada, segurança, confidencialidade e licença têm precedência. Capacidade indisponível não autoriza fallback silencioso.

## 5. Autoria por dois canais

### Chat + GPT/MCP

Usado para:

- definir objetivo, público, escopo e parâmetros;
- planejar partes e dependências;
- buscar contexto autorizado;
- criar microssequências e cards;
- auditar, reparar e reauditar;
- comparar versões e variantes.

O agente opera com alvo explícito, contexto mínimo, autorização, request id, expected revision, provenance e função delimitada.

### ARA

É a superfície operacional para:

- renderizar artefatos em evolução;
- navegar por curso, placement, microssequência, card e resource;
- visualizar versões, diffs, configuração e provenance;
- registrar comentários e findings situados;
- mover/reorganizar ocorrências quando permitido;
- aceitar, rejeitar ou aplicar alterações;
- aprovar e publicar explicitamente.

Validação, auditoria, reparo, reauditoria, aprovação e publicação são operações distintas. IA não promove nem publica a própria saída.

## 6. Pesquisa e analytics

ARA utiliza `ara.research-framework.v1`:

```text
question/purpose
→ protocol
→ condition/assignment
→ authorized event or instrument
→ evidence
→ measure
→ construct
→ interpretation
→ decision/intervention
```

Evento disponível não autoriza coleta. O perfil pessoal permanece data-minimal. Analytics pessoais, pedagógicos, de pesquisa e operacionais têm finalidade, autoridade, visibilidade e retenção separadas.

Condições de pesquisa preservam snapshots de conteúdo, composição, configuração, capacidades, instrumentos e eventos autorizados.

## 7. Lifecycle, organização e publicação

- lineage, revision, placement e publication snapshot são identidades distintas;
- folders, collections, programmes e catalogues organizam referências sem copiar ou alterar a identidade do curso;
- reference, copy, fork, adaptation e translation são relações diferentes;
- published não significa necessariamente public;
- withdrawal, supersession, archive, access revocation e hard deletion são operações distintas;
- licenciamento e atribuição podem variar por curso, microssequência, card, resource e asset;
- workspaces possuem papéis e políticas locais; não existe autoridade global implícita.

## 8. Capabilities e perfis

As capacidades são classificadas como:

- core;
- optional local;
- optional connected;
- research experimental;
- deferred;
- out of scope;
- prohibited.

O baseline inclui estudo offline, biblioteca, recursos estruturados, práticas determinísticas, configuração, autoria visível, versões, publicação e portabilidade. Sync, colaboração, pesquisa, coortes, catálogo, runtimes e IA entram por release e perfil aprovados.

## 9. Qualidade obrigatória

- benchmark de primeiro escopo em dispositivo Android modesto da classe Galaxy A07;
- estudo baseline sem LLM ou API conectada;
- retomada segura após interrupção;
- acessibilidade e alternativas assistivas;
- interface em inglês, `pt-BR` e `pt-PT`, independente do idioma do curso;
- contratos versionados e validação determinística;
- least privilege, purpose binding e proteção de conteúdo confidencial;
- importação/exportação portável;
- backup, restauração, migração e rollback;
- ausência de fallback, compatibilidade ou legado não documentados.

## 10. Gate de implementação

Sequência obrigatória:

```text
pesquisa e taxonomia — concluídas
→ protocolos e analytics — concluídos
→ requisitos e domínio — concluídos pela Issue #6
→ arquitetura e ADRs — Issue #7
→ UX/UI completa — Issue #8
→ releases e quality gates — Issue #9
→ implementação
```

A definição de produto não seleciona framework, banco, Storage, IndexedDB, sincronização, provedor de identidade, LLM ou biblioteca de UI. Essas decisões pertencem às Issues #7 e #8.
