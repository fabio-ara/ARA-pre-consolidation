# ARA research protocols, instrumentation and analytics framework v1

**Status:** accepted normative handoff from Issue #5  
**Language:** `pt-BR` working specification  
**Depends on:** `ara.configuration-taxonomy.v1`  
**Does not authorize:** participant collection, production event stores, dashboards, predictive models, architecture, UX implementation or code.

## 1. Decision

ARA shall model research and analytics as a versioned chain:

```text
question and purpose
→ protocol
→ condition and assignment
→ authorized event or instrument
→ evidence record
→ measure
→ construct
→ interpretation
→ decision or intervention
```

No layer is inferred automatically from the previous one.

## 2. Baseline

Personal AraLearn-style study remains data-minimal. The baseline requires only functional local state necessary to resume study and preserve explicit learner choices. Attempt, timing, navigation and AI-interaction histories are not collected merely because they can be emitted.

## 3. Normative objects

The machine-readable conceptual model is in `research/data/issue5-research-framework-v1.json`. It defines ResearchQuestion, Protocol, Condition, Participant, Assignment, EventDefinition, InstrumentDefinition, InstrumentInstance, MeasureDefinition, ConstructDefinition, InterpretationRule, EvidenceRecord and ResearchPackage.

These are domain semantics for Issue #6. They are not production database schemas.

## 4. Protocol

A protocol version fixes:

- questions, purposes and decision uses;
- population and eligibility;
- conditions and assignment method;
- content, composition and configuration versions;
- capabilities and allowed fallbacks;
- instruments and administration schedule;
- authorized events and properties;
- primary, secondary and exploratory outcomes;
- analysis and missing-data plans;
- consent, withdrawal, identity, access, retention and export;
- provenance, deviations and limitations.

A later edit creates a new protocol version. Registration or approval creates an immutable snapshot.

## 5. Conditions and variants

A condition snapshot includes content, composition, effective configuration, capabilities, instruments and event authorization. Course variants must declare invariants and all known differences. Rights-required accommodations are allowed even when a condition is locked; the deviation is recorded and interpreted without penalizing the participant.

## 6. Assignment

Assignment records the participant, condition, method, sequence/strata, authority and time. The terms `randomized`, `counterbalanced`, `concealed`, `quasi-experimental` and `causal` may be used only when their methodological requirements are met.

## 7. Events

The internal vocabulary is intentionally small and versioned. The normative registry is `research/data/issue5-event-vocabulary-v1.csv`.

Caliper and xAPI are interoperability mappings. They do not define ARA constructs or authorize collection. Event definitions include purpose, actor/object, required properties, authorization, retention class and prohibited inferences.

## 8. Instruments

ARA supports assessment instruments, questionnaires, scales, rubrics, confidence judgments, interviews, focus groups, diaries, observations and artifact analysis. The registry is `research/data/issue5-instrument-registry-v1.csv`.

Every instrument records version, language, timing, administration, source/license, scoring or coding, accommodations and construct links. Translation does not imply measurement equivalence.

## 9. Measures and constructs

The normative candidate registry is `research/data/issue5-measure-registry-v1.csv`.

Every measure requires:

- research question;
- formula and denominator;
- unit and unit of analysis;
- observation window;
- source events/instruments;
- missing-data handling;
- limitations;
- permitted and prohibited uses.

Attempts, time, pauses, hint use, delays and navigation do not directly measure engagement, effort, struggle, attention, difficulty or mastery.

Constructs are versioned definitions supported by validity evidence and explicitly linked measures. A measure may be descriptive without supporting a latent construct.

## 10. Missing data and fidelity

The protocol distinguishes not collected, not authorized, not applicable, unavailable capability, technical loss, participant nonresponse, withdrawal and rights-required deviation. Missingness is not assumed random. Fidelity records deviations from conditions without automatically classifying them as participant failure.

## 11. Governance

The normative matrix is `research/data/issue5-governance-matrix-v1.csv`.

Purpose binding, minimization, consent where applicable, withdrawal, identity mode, pseudonymization, retention, access, export, secondary use, incident response and sensitive-data restrictions are explicit.

Pseudonymized data remains personal data. Operational logs are not repurposed for learning analytics without a new authorized purpose.

## 12. Analytics surfaces

Four authorities remain separate:

- **personal:** private, opt-in reflection and study management;
- **teaching/tutoring:** authorized formative questions and aggregates;
- **research:** protocol-bound evidence and analysis;
- **operational:** reliability, sync and security.

Interfaces answer named questions. There is no universal dashboard.

## 13. Export and interoperability

Exports include protocol/version, taxonomy version, data dictionary, semantic mappings, measure definitions, missingness, provenance, access class and limitations.

Candidate mappings:

- Caliper/xAPI for events;
- QTI for assessment artifacts;
- DDI for study/instrument/variable metadata;
- PROV-O for provenance;
- RO-Crate for portable research packages;
- DPV for privacy-processing metadata.

Mappings are versioned and may be lossy. ARA semantics remain authoritative.

## 14. Representative cost envelopes

Issue #7 must size architecture against at least:

- personal baseline: no central event requirement;
- small study: 100 participants, up to 10k authorized events each;
- medium multi-course study: 1k participants, up to 50k events each;
- qualitative study: encrypted attachments/transcripts with restricted access;
- cross-deployment study: versioned exports and conformance evidence.

Storage estimates must include indexes, provenance, instruments, attachments, backups and retention—not only raw JSON size.

## 15. Validation

Twelve scenarios passed conceptual walkthroughs in `research/data/issue5-scenario-validation-v1.csv`. The independent audit is `research/data/issue5-integration-audit-v1.json`.

Passing establishes coherent protocol and analytics semantics. It does not establish educational effectiveness, legal compliance in a specific study, production scalability or usability.
