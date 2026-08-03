# Backlog e fluxo de trabalho do ARA

**Estado:** documento operacional vigente  
**Idioma:** `pt-BR`  
**Última revisão:** 3 de agosto de 2026

## 1. Autoridade

Ordem para comportamento e engenharia:

1. especificação aprovada da fase;
2. ADR/decisão estratégica;
3. issue operacional vigente;
4. síntese decisória;
5. evidência/dataset;
6. protótipo ou registro histórico;
7. conversa não registrada.

## 2. Caminho

```text
#3 evidência contínua
→ #4 taxonomia — concluída
→ #5 pesquisa/analytics — concluída
→ #6 produto/domínio — concluída
→ #7 arquitetura — atual
→ #8 UX/UI
→ #9 releases/backlog
→ implementação
```

## 3. Estado

| Issue | Estado | Baseline/saída |
|---|---|---|
| #2 | paralela | licença, identidade e questões institucionais |
| #3 | contínua | pesquisa atualizável |
| #4 | concluída | `ara.configuration-taxonomy.v1` |
| #5 | concluída | `ara.research-framework.v1` |
| #6 | concluída | requisitos e modelo de domínio v1 |
| #7 | ativa | arquitetura provider-independent e ADRs |
| #8 | futura | UX, acessibilidade e protótipos |
| #9 | futura | releases, CI e issues executáveis |

## 4. Handoff normativo para #7

A arquitetura deve preservar:

- `MicrosequenceLineage`/`MicrosequenceRevision`;
- `Placement` como ocorrência contextual;
- `CourseVersion` e `PublicationSnapshot` imutáveis;
- estado contextual por learner assignment/course version/placement/card;
- Resource/Practice/Response/Validator/Feedback separados;
- profiles/overlays/overrides/effective snapshot;
- objetos de pesquisa da Issue #5;
- workspaces e papéis locais;
- reference/copy/fork/adaptation/translation;
- typed relations e capability manifests;
- baseline offline/data-minimal sem LLM ou event store obrigatórios.

Manifestos:

- `research/data/issue4-final-artifact-manifest-v1.json`;
- `research/data/issue5-artifact-manifest-v1.json`;
- `research/data/issue6-artifact-manifest-v1.json`.

## 5. Decisões que #7 precisa registrar por ADR

- cliente web/PWA e estratégia de pacote;
- persistência local;
- metadata e immutable artifact stores;
- materialização de course versions;
- sync/outbox/conflitos;
- identity e authorization;
- MCP gateway e capability discovery;
- research event/instrument adapters;
- managed e self-hosted profiles;
- backup/restore/migration/rollback;
- security, privacy, accessibility, performance e cost budgets;
- extensão controlada.

Primeiro-escopo e requisito durável não podem ser confundidos.

## 6. Regras de execução

- Nenhum protótipo histórico vira arquitetura sem requisito + comparação + ADR.
- Curso não contém código arbitrário.
- Conflito semântico não sofre auto-merge silencioso.
- Capacidade ausente é explícita.
- Supabase pode ser adapter gerenciado, nunca domínio.
- Implementação não inventa UX.
- Cada PR substancial inclui decisão, validação, limites e documentação.

## 7. Registros não autorizados

Issues #50 e #53 são placeholders acidentais fechados como `not_planned`. Experimentos #36–#40 permanecem não normativos; #42 permanece adiado.

## 8. Próxima ação

Concluir a **Issue #7** e seus ADRs; depois iniciar #8.
