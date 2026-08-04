# Telas, controles e estados — rascunho visual do ARA

**Estado:** wireframes para discussão, não especificação de implementação  
**Estilo:** monocromático, linhas simples, conteúdo antes de decoração  
**Princípio:** cada tela responde a uma pergunta do usuário.

## 1. Regras visuais do rascunho

- uma ação primária por contexto no mobile;
- texto e ícone, não ícone isolado em ações críticas;
- navegação inferior somente para áreas realmente disponíveis ao perfil;
- detalhes técnicos em “Detalhes”, não na superfície principal;
- status por texto e forma, nunca apenas cor;
- listas e formulários antes de gráficos;
- alternativa em lista para grafo, árvore, flow, dependências e diff;
- drawers/sheets no mobile; panes no desktop;
- botões destrutivos separados e com consequência explícita;
- estado offline sempre visível, mas não alarmista.

## 2. Áreas candidatas

```text
Biblioteca — estudar e organizar
Criar      — construir e configurar
Revisar    — comentários, findings, auditoria e reparo
Pesquisar  — protocolos, condições e evidência
Administrar — pessoas, capabilities, storage e diagnóstico
```

O perfil pessoal pode mostrar apenas Biblioteca e Criar. As áreas restantes aparecem por papel/capability.

## 3. Catálogo de telas

### S01 — Entrada e perfil local

**Pergunta:** “Quero usar neste dispositivo ou entrar numa conta?”  
**Controles:** `Usar localmente`, `Entrar`, `Criar conta`, `Importar backup`.  
**Estados:** primeiro uso, sessão expirada, offline, dados locais existentes.  
**Nota:** conta não deve ser pressuposto técnico antes da decisão de produto.

### S02 — Biblioteca / Continuar

**Pergunta:** “Onde retomo?”  
**Controles:** buscar, continuar, abrir curso, filtrar downloads, adicionar/importar.  
**Estados:** vazia, offline, sincronizando, storage warning, atualização disponível.  
**Wireframe:** [`wireframes/01-library.svg`](wireframes/01-library.svg).

### S03 — Curso

**Pergunta:** “O que é este curso e como está neste dispositivo?”  
**Controles:** continuar/baixar/atualizar, ver estrutura, parâmetros, versão, fontes, remover local.  
**Estados:** somente remoto, baixando, pronto offline, update, capability ausente.  
**Wireframe:** [`wireframes/02-course-overview.svg`](wireframes/02-course-overview.svg).

### S04 — Estrutura do curso

**Pergunta:** “Como o curso está organizado e do que cada parte depende?”  
**Controles:** expandir, abrir placement, alternar estrutura/dependências/lista.  
**Estados:** completa, dependência ausente, ciclo, placement indisponível.

### S05 — Materialização offline

**Pergunta:** “O que será baixado e quanto ocupa?”  
**Controles:** confirmar, cancelar, pausar, tentar novamente, manter versão anterior.  
**Estados:** verificando, baixando, instalando, falhou, pronto, espaço insuficiente.

### S06 — Card de estudo

**Pergunta:** “O que devo compreender ou fazer agora?”  
**Controles:** responder, confirmar, limpar, revelar, observar, rever, anterior/próximo.  
**Estados:** teoria, prática, resposta editada, feedback, offline, fallback.  
**Wireframe:** [`wireframes/03-study-card.svg`](wireframes/03-study-card.svg).

### S07 — Retomada e mudança de versão

**Pergunta:** “Onde parei e o que mudou?”  
**Controles:** continuar, ver mudanças, manter versão anterior, atualizar.  
**Estados:** mesma versão, placement movido, unidade atualizada, unidade removida.

### S08 — Rever

**Pergunta:** “O que marquei para retomar?”  
**Controles:** abrir, adiar, retirar marca, filtrar curso/assunto.  
**Estados:** vazia, itens disponíveis, package ausente, offline.

### S09 — Observação situada

**Pergunta:** “Que dúvida ou problema quero registrar aqui?”  
**Controles:** categoria, texto, visibilidade, salvar, retirar.  
**Estados:** nova, enviada, resposta recebida, correction linked, target superseded.

### S10 — Dados pessoais e armazenamento local

**Pergunta:** “O que existe neste dispositivo e o que posso remover/exportar?”  
**Controles:** exportar, remover download, apagar rascunho, solicitar exclusão remota.  
**Estados:** local-only, sincronizado, pendente, retido por protocolo, erro.

### S11 — Workspaces

**Pergunta:** “O que está em construção?”  
**Controles:** abrir, criar, buscar, filtrar por papel/status, importar conteúdo.  
**Estados:** vazio, local-only, compartilhado, conflito, sem acesso.

### S12 — Visão do workspace

**Pergunta:** “Qual é o estado do curso, das unidades e das operações?”  
**Controles:** abrir plano, composição, unidades, operações, findings, publicações.  
**Estados:** planejado, parcialmente materializado, em auditoria, pronto, publicado.  
**Wireframe:** [`wireframes/06-authoring-workspace.svg`](wireframes/06-authoring-workspace.svg).

### S13 — Brief e plano

**Pergunta:** “O que este curso pretende cobrir e para quem?”  
**Controles:** editar objetivo/público/escopo, fontes, invariantes, pedir plano ao GPT.  
**Estados:** incompleto, validado, divergência de cobertura, locked by condition.

### S14 — Composição e dependências

**Pergunta:** “Que revisões integram o curso e como se relacionam?”  
**Controles:** adicionar referência, criar unidade, mover placement, criar relação, lista/graph.  
**Estados:** válido, órfão, missing prerequisite, cycle, update available.  
**Wireframe:** [`wireframes/04-structure-dependencies.svg`](wireframes/04-structure-dependencies.svg).

### S15 — Catálogo de unidades reutilizáveis

**Pergunta:** “Já existe uma unidade adequada?”  
**Controles:** buscar, filtros, preview, referenciar, copiar, fork, adaptar.  
**Estados:** sem resultado, sem permissão, licença incompatível, versão superada.

### S16 — Microssequência

**Pergunta:** “Qual é o conteúdo, papel, estado e contexto desta unidade?”  
**Controles:** abrir cards, editar metadata, fontes, relações, versões, pedir GPT.  
**Estados:** planned, draft, audited, used by N courses, superseded.

### S17 — Card em modo Editar

**Pergunta:** “Que parte quero alterar?”  
**Controles:** selecionar card/resource, edição simples, caixa de pedido, preview.  
**Estados:** clean, changed, generating, preview, invalid, stale, applied.

### S18 — Formulário de resource

**Pergunta:** “Quais campos semânticos este resource exige?”  
**Controles:** derivados do package, preview visual/acessível, validar, restaurar.  
**Estados:** válido, incompleto, limite excedido, package ausente.

### S19 — Perfil e parâmetros

**Pergunta:** “Como este curso deve funcionar?”  
**Controles:** contexto, perfil, overlays, busca, avançado, comparar.  
**Estados:** recommended, changed, conflict, rights-required, unsupported.  
**Wireframe:** [`wireframes/05-parameter-profile.svg`](wireframes/05-parameter-profile.svg).

### S20 — Configuração efetiva e diff

**Pergunta:** “De onde vem cada valor e o que mudará?”  
**Controles:** filtrar consequência, origem, escopo, reset override, criar variante.  
**Estados:** runtime-only, content-transforming, composition-changing, locked.

### S21 — Operações GPT/MCP

**Pergunta:** “O que o assistente está fazendo e qual decisão exige?”  
**Controles:** abrir operação, cancelar, fornecer informação, inspecionar contexto, aplicar/rejeitar.  
**Estados:** queued, running, needs-input, preview-ready, applied, failed, stale.  
**Wireframe:** [`wireframes/09-mcp-operations.svg`](wireframes/09-mcp-operations.svg).

### S22 — Preview e diff de versão

**Pergunta:** “O que exatamente mudou?”  
**Controles:** conteúdo/estrutura/configuração, anterior/próximo, aplicar tudo/seleção/rejeitar.  
**Estados:** semantic diff, generated-only, invalid, conflict, regression.  
**Wireframe:** [`wireframes/08-version-diff.svg`](wireframes/08-version-diff.svg).

### S23 — Comentários e findings

**Pergunta:** “Que questões estão abertas e onde?”  
**Controles:** filtros, abrir alvo, aceitar/rejeitar finding, responder, autorizar reparo.  
**Estados:** open, triaged, needs-information, repair-planned, resolved.  
**Wireframe:** [`wireframes/07-comment-repair.svg`](wireframes/07-comment-repair.svg).

### S24 — Auditoria

**Pergunta:** “Que versão, rubrica e escopo serão examinados?”  
**Controles:** selecionar revisão/rubrica/revisor, iniciar, concluir, exportar findings.  
**Estados:** draft, running, incomplete, passed-with-findings, blocked.

### S25 — Reparo e reauditoria

**Pergunta:** “Quais findings serão reparados e o que fica fora do escopo?”  
**Controles:** selecionar findings/alvos, autorizar GPT/manual, preview, regression results.  
**Estados:** authorized, partially repaired, regression, reaudited, unresolved.

### S26 — Aprovação e publicação

**Pergunta:** “O que será publicado, para quem e com quais restrições?”  
**Controles:** audiência, snapshot, licença, offline compatibility, aprovar, publicar.  
**Estados:** private preview, complete private, shared, institutional, public, research locked.

### S27 — Histórico e provenance

**Pergunta:** “De onde veio esta revisão?”  
**Controles:** lineage, timeline, atores, sources, derived relation, abrir diff.  
**Estados:** original, fork, adaptation, translation, superseded.

### S28 — Pessoas e papéis

**Pergunta:** “Quem pode ver ou fazer o quê neste workspace?”  
**Controles:** convidar, alterar papel, retirar, transferir ownership.  
**Estados:** pending invitation, active, expired, last owner, offline cache.

### S29 — Protocolo de pesquisa

**Pergunta:** “Que pergunta, condição e evidência este estudo autoriza?”  
**Controles:** editar purpose, conditions, assignment, instruments, events, governance.  
**Estados:** draft, ready, locked, amended, closed.  
**Wireframe:** [`wireframes/10-research-protocol.svg`](wireframes/10-research-protocol.svg).

### S30 — Variantes/condições

**Pergunta:** “O que é igual e diferente entre as versões?”  
**Controles:** invariants, intentional diff, content/config/composition, audit equivalence.  
**Estados:** comparable, accidental difference, capability mismatch, locked.

### S31 — Participantes e direitos

**Pergunta:** “Que acesso, consentimento/recusa e retenção se aplicam?”  
**Controles:** eligibility, assignment, status, withdrawal, export/delete request.  
**Estados:** invited, consented, refused, active, withdrawn, retention-only.

### S32 — Instrumentos e evidência

**Pergunta:** “Que instrumentos existem e quando são administrados?”  
**Controles:** criar/importar, schedule, version, accommodation, data preview.  
**Estados:** draft, scheduled, completed, missing, invalidated.

### S33 — Analytics por pergunta

**Pergunta:** “Que pergunta está sendo respondida e com que limitações?”  
**Controles:** pergunta/papel, filtros autorizados, formula/definition, export.  
**Estados:** insufficient data, missingness, aggregate, restricted, stale snapshot.

### S34 — Capabilities e packages

**Pergunta:** “Que resources e serviços esta implantação suporta?”  
**Controles:** catálogo, versão, instalar/ativar/desativar quando permitido, detalhes.  
**Estados:** built-in, lazy available, installed, disabled, incompatible, blocked by policy.

### S35 — Armazenamento e sincronização

**Pergunta:** “Onde estão os dados e há algo pendente?”  
**Controles:** filtro local/remoto, retry, export, clean cache, open affected item.  
**Estados:** offline, synced, pending, rejected, quota warning, corrupted.  
**Wireframe:** [`wireframes/11-sync-offline.svg`](wireframes/11-sync-offline.svg).

### S36 — Administração de storage

**Pergunta:** “O que ocupa espaço e o que será afetado por limpeza/retirada?”  
**Controles:** por tipo/workspace/course/package, impact, archive, remove, export.  
**Estados:** under budget, warning, limit reached, retention lock, orphan candidate.  
**Wireframe:** [`wireframes/12-admin-storage.svg`](wireframes/12-admin-storage.svg).

### S37 — Diagnóstico

**Pergunta:** “Por que esta capability, sync ou publicação não funciona?”  
**Controles:** copy report, retry checks, export diagnostics, show advanced IDs.  
**Estados:** healthy, degraded, incompatible, provider paused, migration needed.

## 4. Estados transversais

| Estado | Comportamento mínimo |
|---|---|
| loading | mantém contexto, texto do que está sendo buscado |
| empty | explica por que está vazio e ação pertinente |
| offline | preserva leitura/escrita local compatível |
| last-known | deixa claro que não concede permissão |
| syncing | não bloqueia trabalho local |
| pending | mostra alvo e possibilidade de retry/cancel |
| conflict | preserva versões e oferece escolhas explícitas |
| denied | explica papel/política sem revelar dados |
| unsupported | identifica capability e alternativa |
| stale | exige reler antes de aplicar |
| invalid | lista erros localizados |
| quota-warning | mostra tamanho/impacto e limpeza possível |
| withdrawn | impede novo acesso conforme política e explica snapshot local |
| superseded | aponta revisão sucessora sem apagar a anterior |
| failed | oferece recuperação, não descarta trabalho |

## 5. Navegação móvel candidata

```text
[Biblioteca] [Criar] [Revisar] [Mais]
```

`Pesquisar` e `Administrar` entram em Mais ou substituem itens conforme papel. Evitar cinco ícones permanentes para perfis simples.

## 6. Desktop

Estrutura candidata:

```text
nav lateral | lista/estrutura | superfície principal | painel contextual opcional
```

A ordem de leitura semântica permanece equivalente ao mobile. Panes não podem criar uma operação impossível na tela estreita.

## 7. Controles críticos e textos

- `Aplicar nova revisão` em vez de “Salvar” quando há derivação;
- `Manter esta versão` em vez de “Ignorar update”;
- `Remover deste dispositivo` distinto de `Retirar da biblioteca` e `Excluir origem`;
- `Usar por referência` distinto de `Criar cópia independente`;
- `Criar adaptação vinculada` distinto de `Editar todos os usos`;
- `Autorizar reparo dos itens selecionados` em vez de “Corrigir tudo”;
- `Publicar snapshot` em vez de “Tornar atual”;
- `Dados coletados nesta condição` em vez de “Tracking”.

## 8. Uso dos wireframes

Os SVGs mostram somente:

- hierarquia;
- agrupamento;
- controles;
- estados;
- linguagem.

Não definem:

- cor final;
- tipografia final;
- ícones finais;
- medidas finais;
- framework;
- quantidade definitiva de abas;
- ordem de implementação.

Registro estruturado: `research/data/ara-screen-catalog-v1.csv`.
