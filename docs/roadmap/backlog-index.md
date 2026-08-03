# Canonical backlog index

**Status:** canonical navigation document  
**Last reviewed:** 3 August 2026  
**Audience:** project owner, Codex and other development agents, external reviewers, research supervisors and contributors.

## 1. Purpose

GitHub Issues and pull requests preserve the primary history of work. This index states how each item should be interpreted **now**.

It does not replace issue protocols, PR evidence or committed research artifacts. It prevents historical exploration, superseded assumptions and current specifications from being treated as equivalent authorities.

## 2. Authority legend

| Authority | Meaning |
|---|---|
| `governing` | Controls current process or phase order. |
| `normative-pending` | Will produce a future normative specification; its current body is a work mandate, not a completed decision. |
| `evidence` | Completed or continuing research that may inform decisions but does not define the product by itself. |
| `decision-synthesis` | Integrates evidence and provides a current recommendation; later normative phases accept, revise or reject it explicitly. |
| `historical-experiment` | Recoverable exploratory work; non-normative unless adopted later through a product decision and ADR. |
| `deferred` | Legitimate question not active in the current route. |

## 3. Current route

```text
#3 evidence programme
→ completed integrated synthesis (#30 / PR #43)
→ #4 parameter taxonomy
→ #5 research protocols and analytics
→ #6 product requirements and domain model
→ #7 architecture, stack and ADRs
→ #8 UX/UI
→ #9 functional releases and implementation
```

Issue #2 proceeds in parallel when its legal and institutional questions become decision-relevant.

## 4. Governing and future normative issues

| Issue | Logical phase | Type | State | Authority | Expected canonical output | Dependencies | Current interpretation |
|---|---:|---|---|---|---|---|---|
| #10 | 00 | governance and roadmap | open | governing | roadmap, gates and execution rules | repository governance | Start-here issue. Canonical documents take precedence over historical issue wording. Current next work is #4, not the already completed #30. |
| #2 | 10 | legal and identity research | open | normative-pending | IP, licensing, trademark and institutional baseline | governance; official legal/institutional sources | Parallel work. Does not block #4 unless a concrete legal dependency appears. |
| #3 | 20 | master evidence programme | open | governing evidence | protocols, corpora, source status, bibliographies, syntheses and research agenda | governance | Continuing research infrastructure. Not a single review that must be “completed forever”. |
| #4 | 30 | configuration taxonomy | open | normative-pending | parameter taxonomy, reference profiles, maturity and authority rules | #30 synthesis; evidence packages under #3 | **Current active product-definition work.** Must use focused bibliographic packages and recommendations, not raw evidence dumps. |
| #5 | 40 | research protocols and analytics | open | normative-pending | protocol, condition, event, measure, instrument and governance model | accepted #4 taxonomy; evidence under #3 | Future phase. Must distinguish event, measure, construct and inference. |
| #6 | 50 | product requirements and domain | open | normative-pending | product requirements and normative domain model | #4, #5, #30; relevant #2 findings | Accepts or rejects concepts. Historical component contracts do not define the domain. |
| #7 | 60 | architecture and stack | open | normative-pending | reference architecture, stack decisions, deployment profiles and ADRs | accepted #5 and #6 outputs | Separates durable requirements, first-scope constraints, profiles and technical hypotheses. |
| #8 | 70 | UX, accessibility and visual system | open | normative-pending | complete journey, information architecture, screen and visual specifications | #4–#7 | Codex may not invent user-facing behavior during implementation. |
| #9 | 80 | releases and implementation planning | open | normative-pending | release plan and executable implementation backlog | approved #6–#8 | Implementation issues must trace to canonical requirements, decisions, contracts and screens. |

## 5. Decision synthesis

| Issue | PR | State | Authority | Canonical outputs | Current interpretation |
|---|---:|---|---|---|---|
| #30 | #43 | closed/completed | decision-synthesis | `research/pt-BR/sintese-configuracao-aralearn-horizonte-externo-01.md`; decision maps and JSON | Current recommendation: AraLearn reference profile + broad discovery + selective normatization + governed extensibility. Direct input to #4. |

## 6. Evidence programme: protocols, searches and syntheses

| Issue | PR(s) | Type | State | Authority | Main output / role | Limit for current use |
|---|---:|---|---|---|---|---|
| #3 | #11, #12, #13 and all child work | master evidence programme | open | evidence/governing | protocol, antecedents, source schemas and research index | Broad programme; individual findings require synthesis before normatization. |
| #14 | #15 | review of reviews | closed | evidence | first central synthesis on flashcards, retrieval, spacing, quizzes, feedback and mobile programming | Early evidence core; not exhaustive across domains or parameters. |
| #16 | #21, #22, #23 | formal database search | closed | evidence | PubMed/ERIC execution, exports, hashes and deduplication; 1,471 unique publications | Search scope is concentrated in the first fronts. |
| #17 | #19 | focused review | closed | evidence | response formats, scoring, feedback, timing and retry | Initial synthesis; domain transfer requires qualification. |
| #18 | #20 | focused update | closed | evidence | mobile programming update and task matrix | Provisional post-2022 update, not general programming pedagogy. |
| #24 | #25 | screening | closed | evidence | title/abstract screening of 1,471 records | Single-reviewer first pass; relevance is not quality. |
| #26 | #27 | priority extraction | closed | evidence | classification and extraction of 26 priority publications | Some full texts remain unavailable; source status explicit. |
| #28 | #29 | overlap mapping | closed | evidence | primary-publication overlap and non-redundant synthesis core | Bibliographic overlap, not a new meta-analysis. |

## 7. AraLearn and external system evidence

| Issue | PR | Type | State | Authority | Main output / role | Current interpretation |
|---|---:|---|---|---|---|---|
| #31 | #32 | source audit | closed | evidence | canonical audit of 18 AraLearn resources and practice limits | Implemented reference baseline. Preserve/revise labels were provisional, not migration decisions. |
| #33 | #35 | comparative system benchmark | closed | evidence | audit of 21 systems and capability families | Useful patterns and counterexamples. `legacy-seed` wording does not make AraLearn disposable. |
| #34 | #35 | scholarly genre mapping | closed | evidence | neighbouring genres and literature beyond flashcards | Contextual framing, not a requirement to implement every genre. |

## 8. Historical component experiments

| Issue | PR | State | Authority | Preserved result | Normative status / reactivation condition |
|---|---:|---|---|---|---|
| #36 | #37 | closed | historical-experiment | component-contract prototypes for four stress families | Non-normative. Reuse requires #6 need and #7 decision. |
| #38 | #39 | closed | historical-experiment | disposable adapters, tests, measurements and negative findings | Non-production. Valid engineering evidence only. |
| #40 | #41 | closed/completed | historical-experiment | version 0.2, migrations, boundary audits and untrusted-code decision record | Protocol and results preserved. Not the ARA course contract. |
| #42 | — | closed/not planned | deferred | full runtime bake-off protocol for MathLive, Cytoscape.js and Recogito | No runtime result exists. May return only after accepted product need and ADR question. |

## 9. Pull request chronology

| PR | Related issue(s) | Primary contribution | Current authority |
|---:|---|---|---|
| #1 | governance | repository governance, language and licensing baseline | governing source |
| #11 | #3 | master bibliographic protocol | evidence infrastructure |
| #12 | #3 | formative app antecedents | evidence |
| #13 | #3 | expanded system antecedents and search fronts | evidence |
| #15 | #14 | first review-of-reviews synthesis | evidence |
| #19 | #17 | response and feedback synthesis | evidence |
| #20 | #18 | mobile programming update | evidence |
| #21 | #16 | formal search preparation | method record |
| #22 | #16 | validation of database exports | evidence/method |
| #23 | #16 | deduplication and final corpus count | evidence/method |
| #25 | #24 | title and abstract screening | evidence |
| #27 | #26 | priority corpus extraction | evidence |
| #29 | #28 | overlap mapping | evidence |
| #32 | #31 | AraLearn source audit | evidence baseline |
| #35 | #33, #34 | external systems and scholarly genres | comparative evidence |
| #37 | #36 | component contracts 0.1 | historical experiment |
| #39 | #38 | disposable adapters | historical experiment |
| #41 | #40 | component contracts 0.2 and boundary audits | historical experiment |
| #43 | #30 | integrated reference/external synthesis | current decision synthesis |

## 10. Current canonical document set

| Document | Status | Purpose |
|---|---|---|
| `docs/vision/product-vision.pt-BR.md` | current | Defines the product the project is trying to build. |
| `docs/history/reconstrucao-historica-pesquisa-decisoes.pt-BR.md` | current | Coherent historical reconstruction with primary-source boundaries. |
| `docs/roadmap/backlog-index.md` | current | Interprets issues and PRs and identifies current route. |
| `docs/governance/document-authority-and-traceability.md` | current | Defines which source governs when records conflict. |
| `docs/governance/work-item-standard.md` | current | Required structure for future research, decision and implementation work. |
| `docs/research/research-programme-index.pt-BR.md` | current | Organizes completed evidence and the next bibliographic packages. |
| Issue #10 | governing issue | Phase order and gates. |
| Issue #30 / PR #43 outputs | decision synthesis | Direct handoff to #4. |

Future canonical documents will be added only when their phases produce substantive content:

- parameter taxonomy;
- research and analytics model;
- product requirements;
- domain model;
- reference architecture;
- stack and ADRs;
- UX/UI specification;
- release plan.

Empty placeholders must not be presented as completed specifications.

## 11. Rules for Codex and development agents

Before work:

1. read `docs/vision/product-vision.pt-BR.md`;
2. read this index;
3. read the relevant current canonical specification;
4. read the governing issue;
5. consult historical issues only for evidence or rationale.

Codex must not:

- infer current requirements from a historical prototype;
- implement from an issue whose authority is `evidence` or `historical-experiment`;
- choose a stack before approved ADRs;
- invent UX;
- convert a research finding directly into code;
- silently revive deferred work.

## 12. Update policy

Update this index when:

- a new issue or PR is created;
- an issue changes authority or phase;
- a decision synthesis is accepted or superseded;
- a canonical document is added or revised;
- a release is planned or completed.

Do not rewrite historical issue protocols merely to match current terminology. Correct their interpretation here and in canonical documents.