# Contributing to ARA

[English](CONTRIBUTING.md) | [Português do Brasil](CONTRIBUTING.pt-BR.md) | [Português de Portugal](CONTRIBUTING.pt-PT.md)

ARA is being developed as an educational platform, research infrastructure and public technical artifact. Contributions must preserve traceability among evidence, decisions, requirements, implementation and validation.

## Before starting

Read:

- [Repository governance](docs/governance/repository-governance.md)
- [Language policy](docs/governance/language-policy.md)
- [Licensing boundaries](LICENSING.md)
- [Trademark policy](TRADEMARKS.md)

Substantial work must have an approved GitHub Issue. Do not implement requirements that exist only in a conversation, message or local note.

## Issues

Use the repository issue forms. An executable issue must define the problem, scope, dependencies, acceptance criteria, validation, documentation and relevant research, pedagogical, data, security, accessibility or legal implications.

If new work is discovered outside scope, create a linked issue instead of expanding the current change silently.

## Branches

Use English, lowercase and kebab-case:

```text
docs/initial-governance
research/scoping-review
feat/pedagogical-profiles
fix/course-versioning
```

## Commits

Use Conventional Commits in English, in the imperative mood, without a final period:

```text
docs: define multilingual documentation policy
research: add literature review protocol
feat: add pedagogical profile schema
fix: preserve course configuration on export
```

Keep commits coherent and reviewable. Do not combine unrelated work.

## Pull requests

Every non-trivial pull request must:

- reference its governing issue;
- explain the problem and solution;
- stay within scope;
- include relevant validation and tests;
- update documentation in the same change;
- state language variants updated or pending;
- identify data, security, accessibility, licensing and legal effects;
- record limitations and follow-up issues;
- avoid undocumented fallbacks, compatibility paths and legacy behavior.

## Evidence and research

Do not present personal preference, inference or implementation behavior as established educational evidence. Distinguish:

- source-supported evidence;
- reasoned inference;
- design hypothesis;
- personal or institutional preference;
- empirical result produced by ARA.

Do not publish restricted full-text articles, books, participant data, institutional confidential material or sensitive personal records. Preserve lawful metadata, citations, extraction notes and derived analyses instead.

## Documentation languages

Engineering work uses English. Stable public documentation is maintained in English, Brazilian Portuguese and European Portuguese when applicable. Working research documents normally use Brazilian Portuguese as their canonical drafting language.

## Licensing

By contributing code, you agree that it is provided under `AGPL-3.0-or-later`, unless a file explicitly states another compatible license. Project documentation is provided under `CC BY 4.0`, unless otherwise stated.

Contributors must have the right to submit their work. Third-party code, media, instruments, datasets and educational materials require explicit provenance and compatible terms.

The ARA name, kanji, logo and visual identity are governed separately and are not licensed by the code or documentation licenses.
