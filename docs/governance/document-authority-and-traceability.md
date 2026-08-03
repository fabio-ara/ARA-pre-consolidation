# Document authority and traceability

**Status:** governing documentation policy  
**Last reviewed:** 3 August 2026

## 1. Problem addressed

ARA uses issues, pull requests, source code, research reports, datasets, decisions and future product specifications for several purposes:

- engineering;
- external review;
- project-owner oversight;
- master's research;
- possible future doctoral research;
- guidance for Codex and other development agents.

These records must remain recoverable without allowing historical exploration to govern current implementation accidentally.

## 2. Source classes

### 2.1 Primary historical sources

Records of what happened:

- original vision and brainstorming documents;
- issue bodies and edit history;
- issue comments;
- pull requests and diffs;
- commits and source code;
- search exports, hashes and datasets;
- test outputs;
- correspondence and official records where publishable.

Primary historical sources are authoritative for the fact that a question was asked, a method was used, code was changed or a result was observed. They are not automatically current product requirements.

### 2.2 Evidence artifacts

Records that extract or synthesize evidence:

- review protocols;
- bibliographic records;
- screening and extraction datasets;
- literature syntheses;
- platform benchmarks;
- source audits;
- evaluation reports.

Evidence artifacts inform recommendations. They do not authorize implementation directly.

### 2.3 Decision syntheses

Artifacts that integrate evidence and recommend a path. Required fields:

- principal conclusion;
- recommended path;
- alternatives rejected or deferred;
- justification;
- risks;
- uncertainties that could alter the decision;
- classification of implications.

Decision syntheses guide normative phases but remain distinct from accepted requirements and ADRs.

### 2.4 Canonical current documents

Documents that state the current project understanding or approved specification:

- product vision;
- parameter taxonomy;
- research and analytics model;
- product requirements;
- domain model;
- architecture;
- ADRs and stack decisions;
- UX/UI specification;
- release plan.

These documents govern current downstream work within their approved scope.

### 2.5 Implementation records

- implementation issues;
- code;
- tests;
- migrations;
- release evidence;
- operational documentation.

Implementation records must trace to approved canonical documents and decisions.

## 3. Precedence when records conflict

For current product and engineering behavior, use this order:

1. latest approved canonical specification for the relevant phase;
2. accepted ADR or strategic decision within that specification;
3. current governing roadmap and backlog index;
4. accepted decision synthesis;
5. evidence artifacts;
6. historical issues, PRs and prototypes;
7. unrecorded conversations or memory.

For historical claims about what occurred, primary historical sources prevail over later narrative summaries.

For bibliographic claims, the cited source, extraction record and access status prevail over project prose.

## 4. Normative status vocabulary

Every important artifact or backlog item should use one of:

- `governing`;
- `normative-pending`;
- `accepted-normative`;
- `decision-synthesis`;
- `evidence`;
- `historical-experiment`;
- `deferred`;
- `superseded`;
- `rejected`.

Absence of classification does not make an artifact normative.

## 5. Traceability chain

Normative features must be recoverable through:

```text
problem or research question
→ evidence source(s)
→ extraction or analysis
→ decision synthesis
→ accepted requirement
→ domain concept or policy
→ ADR / architecture decision
→ UX journey and screen
→ release
→ implementation issue
→ code and tests
→ evaluation evidence
```

Not every feature requires every link. Any omitted link must be justified.

## 6. Rules for research

Research work must record:

- question and intended decision;
- protocol or method;
- databases and sources;
- exact searches where applicable;
- dates;
- source-access status;
- inclusion and exclusion;
- extraction;
- limitations;
- synthesis;
- recommendation;
- whether the evidence is sufficient for the pending decision.

Research must not be described as systematic, exhaustive, dual-reviewed or causal unless the method supports that description.

## 7. Rules for Codex and agents

Codex must identify before changing code:

- governing canonical document;
- requirement identifier;
- accepted architecture or ADR;
- relevant UX journey or screen;
- release target;
- acceptance criteria;
- test obligations.

When one is missing, Codex must not invent it. The gap returns to the appropriate product-definition phase.

Historical prototypes may be consulted for:

- failed assumptions;
- reusable tests;
- security findings;
- candidate patterns;
- migration considerations.

They may not be copied into production merely because they already exist.

## 8. Rules for external evaluation

An evaluator should be able to distinguish:

- what the author initially intended;
- how evidence was gathered;
- what changed and why;
- which alternatives were considered;
- which decisions are current;
- what remains uncertain;
- what was implemented and evaluated.

The historical reconstruction provides navigation. Issues, PRs, data and cited sources provide verification.

## 9. Rules for academic reuse

Repository documentation may support master's or doctoral work, but academic texts must:

- formulate their own research question;
- select the relevant corpus;
- cite original scholarship rather than only project summaries;
- distinguish development evidence from educational effectiveness;
- disclose the role of AI assistance;
- respect participant privacy and source licensing;
- avoid presenting future plans as completed results.

## 10. Update procedure

When a current decision changes:

1. create or update the decision synthesis;
2. record why existing evidence no longer suffices or why a trade-off changed;
3. approve the revised decision;
4. update the relevant canonical document;
5. update the backlog index;
6. create migration or implementation work only afterward;
7. preserve the superseded state in history.

Do not silently edit history to imply that the final decision was always intended.