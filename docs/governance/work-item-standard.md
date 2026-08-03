# Work item standard

**Status:** governing template for future issues and substantial pull requests  
**Last reviewed:** 3 August 2026

## 1. Purpose

Every work item must make clear whether it performs research, produces a recommendation, defines a normative specification, tests an uncertainty or implements an approved requirement.

A single issue may contain more than one activity only when their dependency is direct and their outputs remain separately identifiable.

## 2. Required metadata

Every issue must declare:

- **phase:** `00`, `10`, `20`, `25`, `30`, `40`, `50`, `60`, `70`, `80` or `90`;
- **type:** governance, legal research, evidence protocol, extraction, comparative analysis, decision synthesis, taxonomy, product specification, architecture decision, UX specification, exploratory prototype, implementation, validation or evaluation;
- **authority:** governing, normative-pending, evidence, decision-synthesis, historical-experiment or deferred;
- **governing canonical document:** current source that constrains the work;
- **dependencies:** issues, decisions and documents required;
- **canonical output:** document or artifact that will be created or updated;
- **non-authorizations:** what the issue does not permit.

## 3. Common issue structure

```markdown
## Classification
- Phase:
- Type:
- Authority:
- Governing documents:
- Canonical output:

## Context and decision problem

## Intended outcome

## Evidence and prior decisions

## Scope

## Out of scope and non-authorizations

## Dependencies

## Method or proposed approach

## Risks and cross-cutting effects
- pedagogy
- research validity
- privacy and ethics
- accessibility
- security
- mobile and offline
- performance and cost
- licensing
- MCP authorability

## Deliverables

## Acceptance criteria

## Validation

## Documentation and traceability
```

## 4. Research work items

A research issue must include:

### Decision question

State what later decision the research is intended to inform. Research without a decision relationship may still be legitimate, but must be marked `research-only`.

### Search and sampling

Declare as applicable:

- databases;
- source types;
- languages;
- date ranges;
- exact queries;
- platform/system families;
- stakeholder and deployment strata;
- inclusion and exclusion;
- sampling rationale;
- sufficiency or saturation criterion.

### Source status

Distinguish:

- full text;
- accepted manuscript;
- abstract;
- metadata only;
- secondary citation;
- official product documentation;
- personal experience;
- primary code or schema;
- inaccessible source.

### Required synthesis

Research completion requires:

- principal conclusion;
- recommended path;
- alternatives rejected or deferred;
- justification;
- risks;
- uncertainties capable of changing the recommendation;
- evidence limits;
- downstream implication classification.

The project owner must not be handed an undigested corpus as the final deliverable.

## 5. Decision-synthesis work items

A decision synthesis must compare a bounded set of alternatives.

Required decision table:

| Alternative | Benefits | Costs | Evidence | Risks | Reversibility | Recommendation |
|---|---|---|---|---|---|---|

Required final state:

- recommended;
- accepted;
- deferred;
- rejected;
- owner decision required.

Owner decision is required only for unresolved strategic, ethical, pedagogical or value conflicts. The recommended option must be identified.

## 6. Exploratory prototypes

An exploratory prototype requires:

- specific uncertainty;
- evidence or hypothesis;
- reason analysis alone is insufficient;
- falsification criterion;
- smallest adequate prototype;
- explicit non-normative status;
- disposal, retention or adoption rule;
- later phase with authority to accept the result.

A prototype may not:

- select a production stack implicitly;
- create a permanent contract by convenience;
- become a product dependency automatically;
- claim educational effectiveness;
- conceal security or accessibility limitations.

## 7. Product and domain specification

A normative product issue must:

- import accepted parameter and research decisions;
- identify actors and journeys;
- define entities, states, invariants and lifecycle;
- classify core, extension, connected, experimental and out-of-scope capabilities;
- preserve traceability to evidence and recommendations;
- identify architectural and UX questions without deciding them silently;
- update the canonical product requirements or domain model.

## 8. Architecture and stack work

An architecture issue or ADR must state:

- requirement(s) served;
- deployment profile(s);
- durable versus first-scope status;
- representative workloads;
- alternatives compared;
- performance, security, privacy, accessibility, offline, operations and cost implications;
- exit and migration cost;
- prototype evidence if used;
- recommended option;
- accepted decision.

Popularity, current AraLearn usage or prior prototype existence is not sufficient justification.

## 9. UX work

A UX issue must reference:

- actor;
- journey;
- state and transition;
- product requirement;
- parameter behavior;
- permission and failure state;
- mobile, desktop and offline behavior;
- accessibility requirements;
- prototype and evaluation method.

Implementation may not define user-facing behavior absent an approved UX specification.

## 10. Implementation work

Every implementation issue must identify:

- target release;
- requirement identifier;
- domain concept;
- ADR or accepted architecture;
- contract version;
- UX journey/screen where applicable;
- data migration impact;
- security and privacy effect;
- accessibility effect;
- test plan;
- documentation update;
- rollback or failure behavior.

Implementation acceptance requires more than unit tests when the feature affects journeys, accessibility, operations, portability or research semantics.

## 11. Pull request requirements

A substantial PR must state:

- issue(s) addressed;
- canonical documents updated;
- decisions implemented or evidence produced;
- validation executed;
- known limitations;
- migration and rollback effects;
- whether the PR closes the issue;
- follow-up work, without opening it automatically unless authorized.

## 12. Completion rules

An issue closes only when:

- deliverables are committed;
- acceptance criteria are verifiably satisfied;
- limitations are explicit;
- the backlog index is updated;
- the canonical document is updated when required;
- no unfinished acceptance criterion is silently transferred.

Partial research or an environmental blocker must be represented as partial, deferred or inconclusive rather than completed.