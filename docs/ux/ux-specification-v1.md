# ARA complete UX specification v1

**Status:** accepted screen/state baseline from Issue #8  
**Architecture:** Issue #7  
**Implementation:** not started

## 1. Experience principles

1. User sees and controls artifacts; architecture details remain behind advanced inspection.
2. Every consequential action shows target, version, effect, authority and reversibility.
3. Chat/MCP and ARA are complementary; neither hides the other’s operations.
4. Mobile uses one primary task per view; desktop may add resizable contextual panes.
5. Offline is a normal state, not an exceptional error.
6. Profiles and presets precede advanced individual parameters.
7. Errors are local, actionable and preserve work.
8. Accessibility and rights are defaults, not optional modes.
9. State is communicated by text/icon/structure, never color alone.
10. No ranking, streak pressure, decorative gamification or surveillance language.

## 2. Global information architecture

Role/capability-dependent top-level destinations:

- **Study** — library, course, current study and personal settings;
- **Create** — workspaces, course drafts, composition and previews;
- **Review** — comments, findings, approvals and publication queues;
- **Research** — protocols, conditions, instruments and authorized analytics;
- **Admin** — workspace members, policies, deployment health and backups;
- **Search** — authorized courses, microsequences, sources and catalogue;
- **Activity/Sync** — operations, offline queue, conflicts and capability status.

Only destinations supported by the active profile and permissions appear. Their absence is explained in capability inspection.

## 3. Responsive shell

### Mobile

- header: back/context title, connection/sync indicator, overflow;
- bottom navigation: up to five current-role destinations;
- contextual actions in bottom sheet or inline toolbar;
- no essential hover or drag-only operation;
- structure/diff/metadata switch through accessible tabs or disclosure.

### Desktop

- persistent primary navigation;
- content area with optional structure and inspector panes;
- panes are resizable but every function has non-drag keyboard controls and single-column alternative;
- command palette is optional enhancement, never sole access.

## 4. Study journey

1. Library shows references, downloads, current version, offline status and resume point.
2. Course overview shows objectives, structure, prerequisites, version, profile and download size.
3. Materialization displays required/optional capabilities, assets, storage estimate and atomic progress.
4. Study view prioritizes card content and one primary action.
5. Theory resources preserve semantic reading order and alternatives.
6. Practice view shows task, representation, response and explicit submission.
7. Feedback state is distinct from next/complete; reveal and retry follow effective configuration.
8. Resume restores placement/card and explains material version changes.
9. Review queue is personal and non-punitive unless an approved course policy states otherwise.
10. Personal data/settings expose local/synced state, export and delete consequences.

## 5. Configuration journey

Wizard:

1. purpose/profile context;
2. recommended base profile;
3. overlays: accessibility, offline, research, institutional;
4. guided high-impact choices;
5. advanced grouped parameters;
6. effective diff and consequences;
7. conflicts/unsupported capabilities;
8. apply as new snapshot or content/composition derivation where required.

Each control states scope and controlling authority. Locked values show reason and source. Content-transforming choices warn that new revisions will be generated/audited.

## 6. Authoring journey

### Workspace

- course structure and placements;
- selected artifact preview;
- comments/findings;
- versions/diff/metadata;
- operation/activity status;
- chat handoff/action entry.

### Staged workflow

```text
brief → plan → build part → inspect → audit → approve repair
→ repair → re-audit → ready/approve → preview/publish
```

The user can interrupt, select another target, request details or perform deterministic reorganization. Agent activity is labelled `suggestion`, `draft`, `validated-structure`, `needs_review`, `audited`, etc.

### Composition

Course structure displays placements, not hidden copies. Search results show origin, revision, context, licence, review status and affected courses. Actions: reference, copy, fork, adapt or translate; each explains update behavior.

Dependencies have graph and hierarchical/list alternatives. Creating an edge requires type, target and optional rationale. Circular/missing relationships are explicit findings.

## 7. Review, repair and publication

- review inbox grouped by question and urgency, not one quality score;
- review screen freezes target version/scope/rubric;
- finding form: target, criterion, type, severity, impact, recommendation and visibility;
- audit mode cannot edit content;
- repair mode shows only authorized findings and selected target;
- re-audit compares repaired version against original findings and regressions;
- approval and publication are separate dialogs/actions;
- publication preview shows audience, snapshot/version, capabilities, licence, unresolved findings and rollback/withdrawal route.

## 8. Research and analytics

Protocol builder follows the Issue #5 chain. It never starts with an event catalogue.

1. question/purpose;
2. population/rights;
3. conditions/assignment;
4. content/configuration/composition snapshot;
5. instruments;
6. authorized events;
7. outcomes/measures/constructs;
8. analysis/missingness/fidelity;
9. retention/access/export;
10. review and freeze.

Analytics starts from named questions. Every visualization exposes definition, denominator, window, missingness, allowed interpretation and export scope. Personal analytics is private opt-in.

## 9. Administration

Role-oriented queues:

- members/access;
- approval/publication;
- confidential/export requests;
- licences/third-party materials;
- storage/packages;
- sync/conflicts;
- backup/restore/update;
- research rights/retention.

The default UI never exposes table names, object keys, RLS or IndexedDB stores.

## 10. Offline, sync and conflicts

Connection banner states `offline`, `online`, `syncing`, `attention required` or `up to date`.

Offline operations show local completion and queue status. Closing/reloading must not imply loss.

Conflict view explains:

- local intent;
- current connected revision;
- non-conflicting changes;
- choices: reapply, create fork, keep remote, export local, request review;
- why automatic merge was not used.

## 11. Failure and permission

Every failed action preserves inputs and provides:

- plain-language summary;
- target/location;
- whether work is saved locally;
- retry/recovery action;
- permission/capability owner when relevant;
- technical details in disclosure.

Unavailable connected capability never blocks unrelated baseline study.

## 12. Screen contracts

`research/data/issue8-screen-contracts-v1.csv` is normative for screen ID, actors, purpose, required data, actions, states and accessibility. `issue8-journey-screen-matrix-v1.csv` validates coverage.

## 13. Prototype

`prototypes/ux-v1/` is an accessible static prototype for structure and state walkthroughs. It is non-production and not a visual-style commitment beyond the tokens and interaction rules documented here.

## 14. Validation

Required before implementation:

- keyboard-only and screen-reader walkthroughs;
- 320 CSS px reflow and 400% zoom;
- touch-target/drag alternatives;
- Galaxy A07-class physical-device walkthrough;
- pt-BR/pt-PT/English expansion;
- offline/failure/permission simulations;
- comprehension tests for reference/copy/fork, effective configuration, publication audience and sync conflict;
- expert accessibility audit plus representative user evaluation.

Passing UX conformance does not establish educational effectiveness.
