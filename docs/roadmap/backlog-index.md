# Backlog e fluxo de trabalho do ARA

**Estado:** implementação preparada; bloqueio administrativo ativo  
**Idioma:** `pt-BR`  
**Última revisão:** 3 de agosto de 2026

## 1. Gates concluídos

```text
#4 taxonomia ✓
→ #5 pesquisa/analytics ✓
→ #6 produto/domínio ✓
→ #7 arquitetura/ADRs ✓
→ #8 UX/UI ✓
→ #9 programa/releases/quality/backlog materializado
```

Baselines e manifestos das Issues #4–#9 são obrigatórios. Issue #3 permanece contínua; #2 paralela.

## 2. Bloqueio atual

**#59 — Enable protected main and verify governance gate**.

A implementação não pode começar antes de:

- aplicar `docs/releases/main-branch-protection-v1.md`;
- exigir PR, histórico linear, resolução de conversas e check `governance`;
- verificar por PR de teste que um check falho impede merge;
- registrar a evidência e fechar #59.

A integração disponível não expõe a mutação de rulesets; isso exige ação administrativa no GitHub.

## 3. Releases e issues executáveis

### R0 — foundation

- #59 proteção da `main`;
- #60 TypeScript monorepo e PWA shell;
- #61 domínio/configuração/pacotes executáveis.

### R1 — personal offline study

- #62 biblioteca e materialização atômica;
- #63 resources/práticas/card cycle;
- #64 estado contextual, review/resume e evidence package.

### R2 — visible private authoring

- #65 workspace/composição/versions/diffs;
- #66 annotations/audit/repair/approval/private publication;
- #67 bounded MCP authoring/audit/repair.

### R3 — connected collaboration

- #68 PostgreSQL/artifact storage/OIDC adapters;
- #69 sync/outbox/conflicts;
- #70 collaboration/publication/operations.

### R4 — research/formal/institutional

- #71 protocols/instruments/authorized evidence;
- #72 formal teaching/confidential institutional profiles.

### R5 — open/capabilities/migration

- #73 public/OER catalogue and controlled capabilities;
- #74 AraLearn migration, cross-profile conformance and ARA v1 evidence.

Canonical dependency registry: `research/data/issue9-implementation-backlog-v1.csv`.

## 4. Regras permanentes de implementação

- somente #59–#74 autorizam código;
- cada PR fecha uma issue e pertence a uma release;
- cada mudança aponta requisitos/entidades, ADRs, jornadas/screen IDs, testes, documentação e rollback;
- implementação não inventa UX, domínio ou fallback;
- nenhum curso fornece código arbitrário;
- conflito semântico não sofre auto-merge;
- evento disponível não autoriza coleta;
- cada release é end-to-end e publica evidence package/known limitations;
- conformidade não demonstra efetividade educacional.

## 5. Quality programme

- `docs/releases/implementation-programme-v1.md`;
- `docs/releases/quality-gates-v1.md`;
- `docs/releases/main-branch-protection-v1.md`;
- `docs/releases/aralearn-migration-v1.md`;
- `docs/releases/release-evidence-v1.md`;
- workflow `governance`, CODEOWNERS e templates em `.github/`;
- manifesto `research/data/issue9-artifact-manifest-v1.json`.

## 6. AraLearn

Migração é explícita, versionada, auditada e source-preserving. ARA não contém runtime legacy/fallback para contratos, banco ou API do AraLearn. Tags importadas são labels/hipóteses até revisão; reparos semânticos entram no workflow de autoria.

## 7. Registros históricos

#36–#40 permanecem experimentos não normativos; #42 permanece adiado. #50 e #53 são placeholders acidentais `not_planned`.

## 8. Próxima ação inequívoca

Aplicar e fechar #59. Depois executar #60; nenhuma outra issue deve iniciar em paralelo fora das dependências registradas.
