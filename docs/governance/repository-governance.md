# Repository governance

[English](repository-governance.md) | [Português do Brasil](repository-governance.pt-BR.md) | [Português de Portugal](repository-governance.pt-PT.md)

## Canonical sources

The repository is the authoritative record of the ARA project. Requirements, decisions, research assumptions and implementation work must not depend on private conversations, temporary prompts or undocumented instructions.

The canonical hierarchy is:

1. approved project vision and governance documents;
2. Architecture Decision Records and research decision records;
3. GitHub Issues in the canonical backlog;
4. pull requests, commits, tests and released evidence.

When sources conflict, the newer explicitly approved decision must identify and supersede the older one.

## Issues as the canonical backlog

All planned work must be represented by a GitHub Issue before substantial execution begins. Issues are not informal reminders; together they form the product, research, legal, documentation and engineering backlog.

Every executable issue must state, as applicable:

- context and problem;
- intended outcome;
- evidence, sources or governing decision;
- scope;
- out of scope;
- dependencies;
- pedagogical and research implications;
- data, privacy, security, accessibility and legal implications;
- implementation or investigation plan;
- acceptance criteria;
- tests or validation method;
- documentation to update;
- evidence to preserve.

Work discovered outside the approved scope must become a linked issue. It must not be silently absorbed into the current change.

## Roadmap structure

A start-here roadmap issue indexes the project phases and dependencies. Large themes use umbrella issues; implementable work uses smaller issues that can be completed and reviewed coherently.

The initial phase order is:

1. governance, intellectual property and evidence infrastructure;
2. bibliographic and institutional mapping;
3. pedagogical parameter taxonomy;
4. research protocols, instrumentation and analytics;
5. product requirements and domain model;
6. reference architecture and deployment profiles;
7. complete UX and accessibility specification;
8. implementation, validation and releases.

The order may change only through a documented decision that records consequences and dependencies.

## Pull requests

Every non-trivial pull request must:

- reference at least one issue;
- remain within the approved scope;
- explain the change and its consequences;
- include or update relevant tests;
- update affected documentation in the same cycle;
- identify unresolved limitations and follow-up issues;
- preserve the applicable language variants;
- avoid undocumented compatibility layers, fallbacks or legacy paths.

A pull request is not complete merely because code compiles. Completion is determined by the issue's acceptance criteria and required evidence.

## Enforcement layers

Issues alone do not mechanically enforce repository rules. Enforcement is cumulative:

1. this governance policy;
2. `CONTRIBUTING.md`;
3. mandatory issue forms;
4. the pull request template;
5. branch protection and required reviews;
6. automated checks for tests, documentation, licensing and traceability;
7. release criteria and evidence audits.

Branch protection and CI rules will be introduced before implementation work begins. Until then, maintainers must apply the same requirements manually.

## Decision and evidence records

Significant decisions must preserve:

- the problem;
- alternatives considered;
- evidence and sources;
- the chosen decision;
- limitations and risks;
- reversibility;
- affected requirements;
- associated issues, pull requests and releases.

Research conclusions must distinguish evidence, inference, hypothesis and personal preference. Software tests demonstrate conformity with a specification, not educational effectiveness.

## Documentation boundaries

The repository may contain public and private-source-derived documentation, but it must not publish restricted articles, books, institutional material, personal data or sensitive biographical information without authorization. Metadata, extraction records, analyses and citations may be stored when lawful and appropriate.

## No hidden requirements

A contributor must be able to understand the current task by reading the repository. Any instruction that changes scope, architecture, pedagogy, legal treatment, data collection or release behavior must be recorded in the relevant issue or governing document before it is implemented.
