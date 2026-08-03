# Backlog e fluxo de trabalho do ARA

**Estado:** documento operacional vigente  
**Idioma:** `pt-BR`  
**Última revisão:** 3 de agosto de 2026

## 1. Navegação principal

1. `docs/vision/product-vision.pt-BR.md` — produto pretendido;
2. `docs/research/research-programme-index.pt-BR.md` — pesquisa e pacotes decisórios;
3. este documento — fases, autoridade, rastreabilidade e regras.

Issues são unidades autorizadas e autossuficientes. Pesquisa, decisão, produto, arquitetura, UX e implementação permanecem separados.

## 2. Autoridade

Para comportamento atual e engenharia:

1. especificação aprovada da fase;
2. ADR ou decisão estratégica aceita;
3. issue operacional vigente e este índice;
4. síntese decisória;
5. evidência/dataset;
6. issue, PR ou protótipo histórico;
7. conversa não registrada.

Fontes primárias prevalecem para afirmar o que ocorreu. Ausência de classificação não torna artefato normativo.

## 3. Caminho linear

```text
#3 evidência
→ síntese/recomendação
→ #4 taxonomia
→ #5 protocolos e analytics
→ #6 produto e domínio
→ #7 arquitetura e ADRs
→ #8 UX/UI
→ #9 releases/implementação
→ avaliação
```

A Issue #2 corre em paralelo quando questões jurídicas/institucionais forem relevantes.

## 4. Issues principais

| Issue | Fase | Estado | Saída |
|---|---:|---|---|
| #10 | 00 | aberta | roadmap, gates e regras |
| #2 | 10 | paralela | propriedade intelectual, licenciamento e identidade |
| #3 | 20 | contínua | protocolos, corpora, bibliografia e sínteses |
| #4 | 30 | ativa/fase final | parâmetros, perfis e síntese integrada |
| #5 | 40 | futura | protocolos, eventos, instrumentos, medidas e governança |
| #6 | 50 | futura | requisitos, atores, jornadas, entidades e estados |
| #7 | 60 | futura | arquitetura, stack, perfis e ADRs |
| #8 | 70 | futura | jornadas, telas, estados e acessibilidade |
| #9 | 80 | futura | releases e backlog executável |

## 5. Issue #4 — pacotes concluídos

- **P1 — PR #45:** 21 dimensões de prática, resposta, tentativas, reveal, feedback, consequências e acessibilidade.
- **P2 — PR #47:** 36 dimensões de progressão, mastery, sequência, ritmo, spacing, revisão, exemplos, scaffolding, segmentação e retomada.
- **P3 — PR #48:** 50 dimensões e nove perfis de autonomia, autorregulação, adaptação, acessibilidade e IA.
- **P4 — PR #49:** 31 dimensões e nove perfis de protocolos, condições, eventos, instrumentos, medidas, constructos, interpretações, provenance e analytics.
- **P5 — PR #51:** 67 dimensões e 11 perfis de autoria, review, repair, annotation, versioning, reuse, publication, licensing e governance.

Os artefatos em `research/data/p1-*` a `p5-*`, as sínteses, os protocolos e as bibliografias prevalecem sobre resumos.

## 6. Decisões P5 vigentes

- autoria ocorre por estados e decisões versionados;
- GPT+MCP e ARA são canais complementares;
- planejamento, construção, validação, auditoria, reparo, reauditoria, aprovação e publicação são distintos;
- agentes não herdam autoridade de aprovação/publicação;
- contexto precisa de escopo, autorização e snapshot;
- grounding, source anchors, attribution e provenance são explícitos;
- comments/findings têm alvo, motivação, visibilidade, status e resolution link;
- reparo semântico cria revisão e exige regression/reaudit conforme risco;
- published/condition snapshots não são mutados silenciosamente;
- referência, cópia, fork, adaptação e tradução são distintos;
- atualização usa notify/preview; não propagação automática;
- publicação possui audiência e gates;
- withdrawal, deletion, archive e supersession são diferentes;
- licença, atribuição, compatibilidade e material de terceiros são por escopo;
- workspaces e papéis são locais; separation of duties varia por risco;
- administração usa linguagem pedagógica e progressive disclosure;
- MCP, schema, storage, sync, UI e arquitetura permanecem adiados.

## 7. Hipóteses transversais obrigatórias

`discovered`, não normativas:

- parametrização em runtime, conteúdo/materialização, composição/dependências, lifecycle e condição;
- microssequências versionadas e ocorrências contextuais;
- curso como composição versionada;
- snapshot offline autossuficiente;
- estado por curso/versão/posição/card;
- catálogo + perfil + overrides esparsos;
- cursos derivados com invariantes/diffs;
- interface em linguagem pedagógica.

#6 decide domínio; #7 arquitetura; #8 UX.

## 8. Próxima ação: síntese final da Issue #4

Integrar P1–P5 antes de avançar para #5. A entrega deve:

- consolidar e deduplicar parâmetros;
- organizar famílias, níveis e escopos;
- consolidar perfis/overlays;
- definir autoridade, precedência, consentimento, locks e overrides;
- registrar dependências, incompatibilidades e combinações inválidas;
- distinguir configuração, conteúdo/materialização, composição, lifecycle e condição;
- formalizar effective configuration e snapshots conceitualmente;
- preservar aceitos, adiados e rejeitados;
- validar cenários pessoais, acadêmicos, institucionais, confidenciais, públicos e offline;
- produzir handoff para #5 e requisitos candidatos para #6.

Não autoriza schema, arquitetura, UX ou código.

## 9. Experimentos históricos

#36/#37, #38/#39 e #40/#41 permanecem não normativos. #42 permanece adiado. Podem informar falhas, testes e segurança; não definem produto ou stack.

Issue #50 foi um placeholder acidental, fechado imediatamente como `not_planned`; não autoriza trabalho e não integra o backlog.

## 10. Classificação obrigatória

Cada issue declara fase, tipo, autoridade, fontes governantes, dependências, saída verificável e não autorizações.

Autoridades: `governing`, `normative-pending`, `accepted-normative`, `decision-synthesis`, `evidence`, `historical-experiment`, `deferred`, `superseded`, `rejected`.

## 11. Estrutura mínima de issue

```markdown
## Classification
- Phase:
- Type:
- Authority:
- Governing sources:
- Expected output:

## Context and decision problem
## Intended outcome
## Evidence and prior decisions
## Scope
## Out of scope and non-authorizations
## Dependencies
## Method or proposed approach
## Risks and cross-cutting effects
## Deliverables
## Acceptance criteria
## Validation
## Documentation and traceability
```

## 12. Regras por tipo

- **Pesquisa:** pergunta, método, fontes, queries, amostragem, acesso, suficiência, limitações, síntese e recomendação.
- **Síntese:** alternativas, benefícios, custos, evidência, riscos e reversibilidade.
- **Protótipo:** incerteza, hipótese, falsificação, menor escopo e fase responsável; não seleciona stack implicitamente.
- **Produto/domínio:** atores, jornadas, entidades, estados, invariantes e lifecycle.
- **Arquitetura:** requisito, perfil, workloads, alternativas, segurança, privacidade, acessibilidade, offline, custo e ADR.
- **UX:** ator, jornada, estado, requisito, permissão, falha, mobile/offline e acessibilidade.
- **Implementação:** release, requisito, domínio, ADR, contrato, tela, escopo, dados, falhas, aceite, testes e rollback.

## 13. Rastreabilidade

```text
problema → evidência → síntese → requisito → domínio
→ ADR → UX → release → issue → código/testes → avaliação
```

Omissões exigem justificativa.

## 14. Conclusão e PRs

PR substancial registra issues, documentos, evidência/decisão, validação, limitações e follow-up. Issue só conclui quando entregas, critérios e limitações estão explícitos. Pesquisa parcial não é concluída.
