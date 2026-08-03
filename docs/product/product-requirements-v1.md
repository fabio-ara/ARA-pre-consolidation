# ARA product requirements baseline v1

**Status:** accepted normative baseline from Issue #6  
**Depends on:** `ara.configuration-taxonomy.v1`, `ara.research-framework.v1`  
**Does not select:** framework, database, storage provider, synchronization library or UI.

## Product thesis

ARA is the direct successor to AraLearn: a mobile-first, offline-capable environment for structured study and visible human-controlled course authorship assisted by GPT+MCP. It is one product expressed through deployment and capability profiles.

## Core user outcomes

1. A learner can add or receive a course version, materialize it, study offline, resume safely and control personal data.
2. An author can plan and build courses from versioned microsequences, inspect every artifact in ARA, comment, audit, repair and publish explicitly.
3. A teacher/tutor can use approved courses and authorized information without universal surveillance.
4. A researcher can create reproducible variants and governed protocols without changing personal baseline behavior.
5. An institution can operate confidential or public workspaces through local roles, policy, export and lifecycle controls.
6. The product can move between managed and self-hosted infrastructure without changing domain meaning.

## Functional requirement groups

### Study
- library/folder/reference management;
- course materialization and offline availability;
- theory/practice cards and deterministic feedback;
- progress/resumption by placement/card occurrence;
- configuration and accessibility application;
- explicit unavailable-capability behavior;
- personal export and deletion controls.

### Content and composition
- immutable course and microsequence versions;
- placements and typed dependencies;
- resource/practice/response/validator/feedback separation;
- reference/copy/fork/adaptation/translation;
- version and configuration diffs;
- portable imports/exports.

### Authorship
- ARA and chat/MCP as complementary inputs;
- bounded context and capability discovery;
- scoped/idempotent operations with expected revisions;
- comments/findings, audit, repair and re-audit;
- approval and audience-specific publication;
- provenance, sources, licensing and confidentiality.

### Research
- objects and invariants from `ara.research-framework.v1`;
- data-minimal baseline;
- version-locked conditions and rights;
- authorized events/instruments and portable research packages.

### Institutional
- workspaces and local roles;
- policy/approval/separation-of-duties;
- confidential content and restricted providers;
- catalogue/open publication where enabled;
- retention, withdrawal, revocation, backup/export obligations.

## Non-functional requirements

- first-scope benchmark on a Galaxy A07-class modest device;
- reliable offline baseline and interruption recovery;
- accessibility and keyboard/assistive alternatives;
- en, pt-BR and pt-PT;
- bounded package, memory and network budgets;
- deterministic validation and reproducible snapshots;
- least privilege, purpose binding and explicit data boundaries;
- provider independence and documented exit;
- backup, restore, migration and rollback;
- no arbitrary executable code supplied by course artifacts.

## Scope classification

The normative capability registry is `research/data/issue6-capability-classification-v1.csv`. Acceptance into the domain does not require first-release implementation.

## Validation

Sixteen scenarios pass conceptual domain review in `research/data/issue6-scenario-validation-v1.csv`. Passing does not establish technical feasibility, usability or educational effectiveness.
