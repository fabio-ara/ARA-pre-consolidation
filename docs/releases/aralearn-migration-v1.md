# AraLearn → ARA migration strategy v1

## Principles

- AraLearn remains an operational predecessor and evidence source, not runtime legacy inside ARA.
- Migration is explicit, versioned, testable and one-way per package version unless a separate ARA→AraLearn exporter is deliberately specified.
- No hidden fallback to AraLearn contracts, database or API.
- Original exports and migration reports are preserved for audit/rollback.

## Stages

1. **Inventory** — courses, revisions, resources, practices, sources, comments, publications, user-state fields and unsupported records.
2. **Export freeze** — produce canonical AraLearn JSON/assets plus digests and source revision IDs.
3. **Parse/validate** — classify valid, repairable, ambiguous and unsupported inputs without mutation.
4. **Semantic mapping** — convert hierarchy to CourseVersion/Placement/MicrosequenceRevision/Card and separate resource/practice/response/validator/feedback.
5. **Configuration mapping** — apply explicit AraLearn reference profile and record absent/unknown parameters.
6. **Provenance/licensing** — preserve sources, authorship, publication, assets and restrictions.
7. **Repair queue** — schema/mechanical repairs are deterministic; pedagogical/semantic repairs require author/audit workflow.
8. **Package generation** — create ARA portable package and migration report.
9. **Conformance** — round-trip package load, offline study fixtures, version/digest checks and representative visual/content audit.
10. **Acceptance** — user approves import; original remains external archive, not fallback.

## Mapping decisions

- AraLearn microsesequence identity becomes a MicrosequenceLineage and initial revision.
- Course-local occurrence becomes Placement.
- Current publication/revision becomes explicit CourseVersion/PublicationSnapshot where evidence supports it.
- Textual tags are imported as labels and dependency hypotheses, never silently promoted to typed prerequisite edges.
- Comments become annotations only when target/version/visibility can be resolved; ambiguous comments enter review.
- Progress migrates only as structural functional state tied to the imported course version/placement; no mastery inference.
- Archived/deleted distinctions are preserved in the report; no automatic hard delete.

## Release sequencing

- R0: parser fixtures and inventory tooling;
- R1: baseline private course/package import;
- R2: sources/comments/authoring lineage and audit queues;
- R3: connected publications/workspaces;
- later: optional advanced resources only after capability approval.

## Rollback

Migration never mutates the AraLearn source. Deleting an imported ARA package removes only the ARA target according to its lifecycle policy. Connected batch migrations require backup/restore rehearsal and idempotent source IDs.
