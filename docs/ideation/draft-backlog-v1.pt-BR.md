# Rascunho amplo de backlog do ARA

**Estado:** candidato para discussão; não executável  
**Granularidade:** áreas, resultados e questões; não sprints nem ordem definitiva  
**Regra:** somente uma revisão posterior com o proprietário poderá promover itens a backlog de desenvolvimento.

## Como ler

Cada item contém:

- **resultado candidato:** valor que o produto poderia entregar;
- **herança:** relação com o AraLearn;
- **decisão necessária:** discussão ainda aberta;
- **dependências conceituais:** conhecimento ou decisão anterior, não bloqueio de GitHub.

Prioridades não foram atribuídas. O registro CSV permite filtrar os itens.

---

## A. Auditoria, continuidade e escopo

### A01 — Inventário funcional verificável do AraLearn

**Resultado candidato:** mapa completo entre jornada, tela, módulo, tabela, Storage, Edge Function, MCP tool, teste e documentação.  
**Herança:** extração, não migração automática.  
**Decisão:** que partes representam o produto-base e que partes são extensões.

### A02 — Corpus de cursos e estados representativos

Selecionar cursos simples/complexos, todos os resources, workspaces, comentários, publicações, estado offline e falhas para servir de fixture futura.

### A03 — Matriz preservar/reformular/separar/retirar

Validar com o proprietário cada decisão da auditoria. Nenhuma ausência de contestação significa aprovação.

### A04 — Limites do produto

Definir o que distingue ARA de LMS, authoring suite, question bank, research platform e content repository. Registrar funções que não entram como padrão.

### A05 — Vocabulário público

Revisar termos como Biblioteca, Coleção, Trilha, Workspace, Microssequência, Placement, Revisão, Publicação, Resource, Practice, Finding e Parâmetro.

### A06 — Cenários de referência

Manter pelo menos: autodidata offline, autor GPT/MCP, professor/tutor, pesquisa comparativa, instituição confidencial e publicação aberta.

---

## B. Kernel e contratos fundamentais

### B01 — Identidades e versões

Definir lineages, revisions, snapshots, digests, aliases e relações de derivação.

### B02 — Hierarquia e composição

Separar organização visual (`module`, `lesson`) de composição (`CourseVersion`, `Placement`).

### B03 — Contrato de microssequência

Definir escopo, metadata, cards, fontes, conceitos e relações permitidas. Decidir se pode conter referências externas ou somente conteúdo incorporado.

### B04 — Contrato de card

Preservar resource/practice/response/validator/feedback distintos e suportar blocos auxiliares sem slots legados.

### B05 — Contrato de artifact/package

Manifesto portátil com versões, dependências, resources exigidos, assets, licença, provenance e configuração.

### B06 — Canonicalização e digest

Definir ordem, normalização, hashing e verificação sem depender de Storage específico.

### B07 — Migrations de contrato

Migrations puras, versionadas, testáveis e sem fallback silencioso.

### B08 — Estados editoriais

Planejado, rascunho, validado estruturalmente, em revisão, auditado, pronto, aprovado, publicado, rejeitado, superado, retirado e arquivado.

### B09 — Policy/authority engine

Resolver direitos, protocolo, instituição, autor, estudante, adaptação, IA e capability disponível.

### B10 — Error model

Erros estruturados: validação, conflito, permissão, capability, offline, quota, corrupção, versão e operação expirada.

---

## C. Resource, practice e capability packages

### C01 — Manifesto de package

ID, versão, compatibilidade, schemas, renderer, accessibility, practices, migrations, budgets, origem e licença.

### C02 — Registry genérico

Descoberta, validação, catálogo compacto, lazy loading e desativação sem switches por resource.

### C03 — Resource conformance kit

Testes comuns de schema, round-trip, rendering, acessibilidade, mobile, offline, practices e migrations.

### C04 — Practice contract

Definir response shapes, lifecycle da tentativa, confirmação, reveal, reset e persistência sem acoplar à representação.

### C05 — Validator contract

Determinístico por padrão; retorno estruturado; sem acesso à rede ou banco.

### C06 — Feedback contract

Feedback geral, por opção/erro, hints e reveal separados da correção.

### C07 — Migração dos resources-base

Candidatos: paragraph, choice, table, code, formula e composite.

### C08 — Migração dos resources estruturais

Flow, tree, graph, relation map, matrix e plane.

### C09 — Migração dos resources especializados

Chart, sequence, annotated text, linguistic example, system map e reaction.

### C10 — Galeria de packages

Fixture visual/acessível por resource, practice, tema, idioma, viewport e capability state.

### C11 — Package budgets

Tamanho lazy, memória, itens, profundidade, rendering e storage por resource.

### C12 — Política de packages externos

Decidir se o ARA aceitará apenas packages oficiais compilados ou, futuramente, packages assinados instaláveis.

### C13 — Fallback e exportabilidade

Resource ausente deve permitir compreender o conteúdo, baixar package compatível ou exportar, sem quebrar a navegação global.

---

## D. Composição, dependências e reutilização

### D01 — Placement

Representar ocorrência contextual de uma revisão de microssequência dentro de uma versão de curso.

### D02 — Grafo de relações tipadas

Requires, introduces, explains, exemplifies, practises, assesses, revisits, contrasts, misconception, derived, supersedes e reuses.

### D03 — Validação do grafo

IDs, ciclos permitidos/proibidos, escopo, versões e dependências ausentes.

### D04 — Editor de dependências

Visualização simples + lista acessível + explicação de consequências.

### D05 — Reuse por referência

Inserir revisão existente sem duplicar conteúdo.

### D06 — Copy/fork/adaptation/translation

Operações distintas, cada uma com provenance e efeitos claros.

### D07 — Impact analysis

Mostrar cursos/placements afetados por alteração, retirada ou capability ausente.

### D08 — Atualização de referência

Notificar nova revisão; mostrar diff; permitir manter snapshot, atualizar, adaptar ou criar fork.

### D09 — Contexto para GPT

Selecionar predecessores, vizinhos, conceitos, courses autorizados e fontes sem enviar todo o repositório.

### D10 — Distratores fundamentados

Relacionar opções incorretas a misconceptions/conceitos apresentados, sem inferir mastery.

### D11 — Busca de unidades reutilizáveis

Por objetivo, conceito, resource, público, fonte, licença, idioma, status e auditoria.

### D12 — Garbage collection sem perda

Referências, snapshots, retenção, publicação e exclusão segura.

---

## E. Parametrização

### E01 — Catálogo versionado

Importar `ara.configuration-taxonomy.v1` como base de discussão, com aliases e evolução.

### E02 — Perfis-base

AraLearn reference, autodirigido, ensino formal, pesquisa, institucional e publicação.

### E03 — Overlays

Acessibilidade, offline, novice/expert support, participant rights e confidencialidade.

### E04 — Overrides esparsos

Escopos: implantação, workspace, curso, versão, placement, microssequência, card e participante quando permitido.

### E05 — Resolver configuração efetiva

Origem de cada valor, precedência, conflitos, unsupported e snapshot.

### E06 — Formulários em linguagem comum

Perguntas, consequências, recomendações e exemplos; ocultar IDs e armazenamento.

### E07 — Diff de configuração

Mostrar o que muda para estudante, conteúdo, dados, offline e pesquisa.

### E08 — Parâmetros transformadores

Pipeline que cria revisão/variante quando a alteração incide em conteúdo ou composição.

### E09 — Condições bloqueadas

Snapshot de pesquisa/instituição com direitos de override explicitamente preservados.

### E10 — Validação de combinações

Perfis incompatíveis, capabilities ausentes, loops, caminhos impossíveis e efeitos não suportados.

---

## F. Persistência local e offline

### F01 — Comparativo do store local

IndexedDB direto/Dexie versus SQLite/OPFS/PGlite/RxDB em fixtures reais.

### F02 — Materialização atômica

Baixar, verificar, instalar, ativar e reverter curso/package.

### F03 — Cache de assets

Digest, quotas, eviction e compartilhamento entre cursos sem duplicar.

### F04 — Estado pessoal contextual

Assignment/course version/placement/card/practice, sem transferência automática entre contextos.

### F05 — Rascunho local

Autoria offline, revision guard, undo limitado e export.

### F06 — Multi-tab

Coordenação de escrita e leitura sem perda ou corrida.

### F07 — Storage pressure

Estimativa antes do download, limpeza assistida, course/package size e preservação de trabalho.

### F08 — Local-only profile

Avaliar uso sem conta, criação local, export/import e posterior associação opcional.

### F09 — Backup pessoal

Package de biblioteca, estado e autoria com informações claras sobre secrets e dados protegidos.

### F10 — Diagnostics local

Versões instaladas, espaço, pendências, packages, corrupção e reparo — em camada avançada.

---

## G. Backend, BaaS e sincronização

### G01 — Ports de infraestrutura

Identity, authorization, metadata, artifact, sync, assets, email, agent e research.

### G02 — Adapter Supabase de referência

Mapear o que pode ser reaproveitado do AraLearn sem levar tipos/RPCs para o domínio.

### G03 — Adapter alternativo de prova

Escolher Appwrite, Nhost, PocketBase ou backend mínimo para testar portabilidade, não para duplicar o produto inteiro.

### G04 — Artifact repository

Imutabilidade, digest, metadata, upload, download, retention e inventory separados do fornecedor.

### G05 — Metadata repository

Relações, versões, policies e queries necessárias, sem expor banco ao cliente/agente.

### G06 — Sync protocol

Comparar protocolo próprio, RxDB ou PowerSync; definir authoritative operations e conflicts.

### G07 — Operation receipt

Request ID, base revision, actor, target, result, changed IDs e recovery.

### G08 — Partial sync

Enviar apenas biblioteca/workspaces/cursos autorizados e não replicar catálogo completo ou dados institucionais.

### G09 — Quotas e budgets

Banco, storage, egress, functions, realtime, local storage e package size.

### G10 — Pause/degraded provider

Uso offline durante pausa do free tier; mensagens e recuperação após retorno.

### G11 — Export e exit strategy

Cursos, assets, metadata, usuários autorizados, comentários e research packages sem depender do fornecedor.

### G12 — Self-host profile

Instalação, email, TLS, backup, restore, monitoring, update e secrets — somente quando o perfil for discutido.

---

## H. Identidade, bibliotecas, workspaces e papéis

### H01 — Perfil sem conta

Decidir alcance local e convite posterior a criar conta.

### H02 — Identity adapter

OIDC ou BaaS Auth; sessão não define authority de aplicação.

### H03 — Biblioteca pessoal

Referências, downloads, pastas/trilhas, versão instalada e estado local/remoto.

### H04 — Workspaces

Pessoal, equipe, pesquisa, institucional e confidencial.

### H05 — Papéis locais

Owner, author, contributor, viewer, reviewer, auditor, repairer, approver, publisher, participant e admin.

### H06 — Convites e transferência

Fluxos claros e reversíveis, sem dar acesso a conteúdo confidencial por link indevido.

### H07 — Capabilities por papel

Ações efetivas mostradas na UI e verificadas no backend.

### H08 — Public/private/shared/institutional

Visibilidade separada de estado editorial e audiência.

### H09 — Exclusão de conta/workspace

Consequências para autoria, publicações, referências, snapshots e retention.

### H10 — Administração compreensível

Perguntas e impacto, não ACLs e tabelas.

---

## I. Biblioteca e experiência de estudo

### I01 — Shell mobile-first

Navegação curta, retorno, estados globais e funcionamento sem rede.

### I02 — Biblioteca/Continuar

Cursos, últimas posições, downloads, versões e alertas úteis.

### I03 — Course overview

Objetivo, estrutura, configuração resumida, prerequisites, versão, tamanho e capability requirements.

### I04 — Leitor de card

Conteúdo principal, ações situadas e uma ação primária.

### I05 — Navegação de microssequência

Strip/lista, anterior/próximo, progresso estrutural e retorno seguro.

### I06 — Prática e feedback

Confirmar antes de avaliar, limpar, tentar novamente, revelar e prosseguir conforme configuração.

### I07 — Rever

Fila pessoal não punitiva e retomada de unidades em diferentes placements.

### I08 — Observação

Categorias, texto curto, visibilidade e resposta no contexto.

### I09 — Resume/version change

Resumo do que mudou, placement removido e opção de manter snapshot.

### I10 — Capability unavailable

Fallback/explicação/download/política sem quebrar curso inteiro.

### I11 — Personal data

Export, remoção local, retirada de sync e exclusão remota distintas.

### I12 — Accessibility preferences

Aplicáveis sem disclosure obrigatório e com precedência adequada.

---

## J. Autoria no ARA

### J01 — Workspace overview

Planos, cursos, unidades, operações, findings, publicações e storage.

### J02 — Planejamento de curso

Brief, público, escopo, fontes, parâmetros e invariantes.

### J03 — Composition editor

Placements, ordem, dependências e busca de units.

### J04 — Microsequence editor

Metadata, cards, sources, relations, status e versões.

### J05 — Card/resource editor

Formulários derivados dos packages, preview e validação.

### J06 — Modo Ler/Editar

Preservar o card montado; seleção e caixa contextual somente em edição.

### J07 — Version history

Lineage, revisão, ator, motivo, diff e relação de derivação.

### J08 — Semantic diff

Conteúdo, estrutura, resources, parameters e composition separados.

### J09 — Manual deterministic operations

Criar, renomear, mover, referenciar, copiar, fork, separar/juntar e retirar.

### J10 — Source/provenance manager

Fontes aprovadas, âncoras, licença e uso por unidade/card.

### J11 — Licence manager

Licença por course/unit/resource/asset e conflitos visíveis.

### J12 — Preview/materialization

Preview local/privado parcial com capability e configuração reais.

---

## K. GPT, MCP e assistência por API

### K01 — Agent gateway

MCP ou protocolo equivalente sobre application services, nunca banco direto.

### K02 — Capability discovery

Lista compacta de operações/packages e contratos sob demanda.

### K03 — Context builder

Alvo, vizinhos, dependencies, sources, invariants, parameters e permissions.

### K04 — Operation object

Queued, running, needs-input, preview-ready, applied, failed, cancelled e superseded.

### K05 — Planner

Produzir plano e cobertura sem criar conteúdo automaticamente.

### K06 — Builder

Materializar unidades em lotes pequenos, persistidos e visíveis.

### K07 — Auditor

Ler revisão congelada e produzir findings sem mutar.

### K08 — Repairer/re-auditor

Escopo explícito, nova revisão e regression checks.

### K09 — Atomic assistance

Criar/reparar card ou microssequência adicional dentro do próprio ARA.

### K10 — Provider adapters

ChatGPT/OpenAI, DeepSeek, Gemini, local/custom como packages conectados.

### K11 — Privacy/data boundary

Não enviar conteúdo/workspace/participante além do contexto autorizado.

### K12 — Cost/context budget

Paginação, summaries, schema compact/full, attachments e limites.

### K13 — Human approval

IA não aprova ou publica sua própria saída.

### K14 — Failure/recovery

Timeout, resposta inválida, stale revision, missing capability, provider offline e retry idempotente.

---

## L. Comentários, revisão, auditoria e publicação

### L01 — Annotation targets

Card, resource, microsequence revision, placement, relation, configuration e course version.

### L02 — Categories/status

Dúvida, possível erro, confuso, sugestão, observação e finding de auditoria; open/triaged/resolved etc.

### L03 — Review types

Self, AI, peer, SME, instructional, accessibility, legal/licensing e institutional.

### L04 — Rubric and scope

Versão, alvo, revisor, independência e authority.

### L05 — Repair authorization

Finding aceito, alvos permitidos e mudanças relacionadas fora do escopo.

### L06 — Re-audit

Problemas resolvidos, regressões e findings superseded.

### L07 — Approval

Authority explícita e separation of duties proporcional.

### L08 — Publication

Private preview, private complete, shared, institutional, public e research-locked.

### L09 — Withdrawal/supersession

Retirar novos acessos, manter snapshots exigidos, apontar sucessor.

### L10 — Deletion

Remover de composição, arquivar, revoke access e hard delete distintos.

---

## M. Pesquisa, instrumentos e analytics

### M01 — Protocol/condition snapshot

Pergunta, finalidade, conteúdo, configuração, capabilities, instrumentos e eventos.

### M02 — Variant derivation

Invariantes, mudanças intencionais e diferenças acidentais.

### M03 — Participant rights

Consentimento quando aplicável, recusa, retirada, retenção e acesso.

### M04 — Event authorization

Evento disponível não significa coleta; schema e purpose por condição.

### M05 — Instruments

Testes, escalas, rubricas, entrevistas, diários, observações e artifacts.

### M06 — Measures

Fórmula, unidade, janela, inputs, missingness, versão, limites e uso.

### M07 — Construct/interpretation registry

Separar evidence, measure, construct, interpretation e intervention.

### M08 — Research export

Package portátil com snapshots, instruments, data dictionary, provenance e limitations.

### M09 — Learner analytics opt-in

Retomada e reflexões pessoais, sem compartilhar automaticamente.

### M10 — Teacher/tutor views

Coverage, dependencies, comments e fidelity; sem ranking por padrão.

### M11 — Storage/cost model

Protocolos pequenos/médios, retention e segregação de data plane.

### M12 — Cross-deployment conformance

Mesmas semânticas em managed/self-hosted antes de pooling.

---

## N. Telas, design system e acessibilidade

### N01 — Informação arquitetada por tarefa

Biblioteca, Criar, Revisar, Pesquisar e Administrar como capabilities progressivas.

### N02 — Design tokens mínimos

Cor semântica, tipografia, espaço, borda, foco, motion e data series.

### N03 — Component contracts

Buttons, list rows, cards, status chips, dialogs, sheets, forms, tree/list e diff.

### N04 — Mobile/desktop adaptation

Uma tarefa principal no mobile; panes contextuais no desktop.

### N05 — State catalog

Loading, empty, offline, stale, syncing, conflict, denied, unsupported, failed e ready.

### N06 — Keyboard/touch

Alternativas a drag, targets, ordem de foco e one-handed use.

### N07 — Assistive technology

Semantic landmarks, live status, labels, alternatives de graphs/trees/flows.

### N08 — Localization

en, pt-BR, pt-PT; linguagem da interface independente da linguagem do curso.

### N09 — Comprehension testing plan

Termos, parâmetros, versions, reuse e deletion consequences.

### N10 — Wireframe review

Revisar os SVGs deste rascunho antes de qualquer protótipo mais fiel.

---

## O. Aplicação web, app e implantação

### O01 — PWA baseline

Manifest, service worker, asset/package cache e offline shell.

### O02 — GitHub Pages profile

Static artifact, runtime config, callback e cache updates.

### O03 — Other static host profile

MIME, CSP, redirects, service worker e verification.

### O04 — Android wrapper comparison

PWA install, TWA/PWABuilder e Capacitor conforme necessidade nativa.

### O05 — Device benchmark fixture

Galaxy A07-class: startup, card transition, graph/layout, materialization, memory e storage.

### O06 — Secrets/configuration

Public runtime config separada de secrets; provider keys locais ou server side conforme política.

### O07 — Diagnostics

Versão, deployment, adapter, capabilities e service health.

### O08 — Backup/restore concepts

Somente para perfis conectados/institucionais futuros.

---

## P. Migração, validação e adoção futura

### P01 — AraLearn export inventory

Conteúdo, revisões, comments, publications, personal state e unsupported.

### P02 — Semantic mapper

Hierarquia atual para lineage/revision/placement, sem promover tags a dependencies.

### P03 — Resource package mapper

Transformar cada resource v4 em package data compatível.

### P04 — Migration report

Valid, repairable, ambiguous e unsupported; não corrigir pedagogia silenciosamente.

### P05 — Representative course walkthrough

Cursos reais em todas as jornadas e resources.

### P06 — Visual parity review

O que deve parecer contínuo e o que deve mudar.

### P07 — Storage simulation

Quantidade de units/assets/versions/comments/protocol data sob quotas.

### P08 — LLM authoring trials

Construção por partes, context retrieval, graph dependency, audit e repair.

### P09 — Usability studies

Autodidata, professor, tutor e pesquisador; compreensão separada de outcomes educacionais.

### P10 — Decision log

Cada promoção/rejeição deste backlog recebe data, justificativa, alternativas e efeitos.

---

## Questões para ordenar posteriormente

1. O primeiro produto discutido deve ser local-only, conectado ou ambos?
2. Quais 6–8 resources demonstram o package model sem recriar todo AraLearn?
3. A autoria GPT/MCP é requisito do primeiro corte ou entra depois do estudo offline?
4. A composição reutilizável deve preceder a migração de cursos existentes?
5. Até que ponto o painel de storage/admin é necessário numa instalação pessoal?
6. Pesquisa precisa estar no mesmo produto-base ou em capability package?
7. Quais baselines #6–#8 são proposta e quais devem ser reabertas após esta auditoria?
8. O primeiro adapter alternativo deve provar portabilidade de BaaS ou de sync?

## Critério de promoção futura

Um item só deve virar issue de implementação quando possuir:

- problema e público;
- resultado observável;
- relação com AraLearn;
- decisão de produto aceita;
- contrato/domínio correspondente;
- alternativa técnica comparada;
- tela/estado aprovado quando visível;
- efeitos offline, acessibilidade, dados e storage;
- aceite e testes;
- não objetivos e rollback.
