# ARA normative domain model v1

## Central decision

```text
CourseLineage
→ CourseVersion (immutable pedagogical composition)
   → ModuleNode / LessonNode
   → Placement
      → MicrosequenceRevision
         → Card
            → ResourceInstance
            → PracticeDefinition
            → ResponseDefinition
            → ValidatorPolicy
            → FeedbackPolicy
```

`MicrosequenceRevision` is the initial reusable authored unit. `Placement` supplies course context. `CourseVersion` remains a complete pedagogical object.

## Identity and versions

- Lineage is stable identity across revisions.
- Revision/version is immutable content.
- Placement is contextual occurrence.
- PublicationSnapshot is immutable audience release.
- CourseReference points without copying.
- StudyAssignment binds a learner/library context to one course version/channel.
- StudyState is contextual and does not attach mastery globally to reusable content.

## Dependency graph

Typed relations may connect concepts, placements, revisions and courses. Initial relation families include prerequisite, introduces, explains, exemplifies, practises, assesses, revisits, contrasts, misconception, derives, supersedes and reuses. Exact vocabulary remains versioned and domain-scoped; no universal ontology is claimed.

## Mutable and immutable boundaries

Mutable:
- AuthoringWorkspaceState;
- pending operations and annotations;
- local functional state;
- moving publication channels.

Immutable once created:
- MicrosequenceRevision;
- CourseVersion;
- EffectiveConfigurationSnapshot;
- Protocol/Condition approval snapshot;
- PublicationSnapshot;
- Evidence/ResearchPackage version.

## State ownership

```text
learner/library context
+ study assignment
+ course version
+ placement
+ card
→ functional study state
```

Cross-course reuse never transfers mastery automatically. A later accepted policy may use explicit evidence/claim equivalence.

## Configuration

Taxonomy version, profile, overlays, policy/locks, sparse overrides, content/composition versions and capability manifest resolve to an EffectiveConfigurationSnapshot. Content-transforming changes create new revisions; composition changes create a new CourseVersion.

## Research

Issue #5 objects are optional-profile domain entities. Research events are not required by personal study. Operational logs and research evidence remain purpose-separated.

## Lifecycle

Drafting, review, repair, approval and publication are distinct. Published artifacts are superseded or withdrawn; they are not edited in place. Hard deletion requires impact, license, confidentiality and retention review.

## Organization

Folders, collections, programmes and catalogues organize references. They do not create hidden copies or rewrite pedagogical structure.

## Capabilities

CapabilityDefinition and CapabilityManifest make absence explicit. Built-in/local/connected/experimental classes share domain semantics but different availability and failure behavior.

## Canonical registries

- entities: `research/data/issue6-domain-entities-v1.csv`;
- invariants: `research/data/issue6-invariants-v1.csv`;
- states: `research/data/issue6-state-machines-v1.json`;
- journeys: `research/data/issue6-journey-registry-v1.csv`;
- capabilities: `research/data/issue6-capability-classification-v1.csv`.
