# Language policy

[English](language-policy.md) | [Português do Brasil](language-policy.pt-BR.md) | [Português de Portugal](language-policy.pt-PT.md)

## Purpose

ARA is intended for self-directed learners, researchers and institutions in Brazil, Portugal and other countries. The repository therefore separates the language of engineering, public communication, research work and jurisdiction-specific documentation.

## Engineering language

English is the canonical language for:

- commit messages;
- branch names;
- issue and pull request titles;
- source-code identifiers;
- APIs, schemas, database identifiers and event names;
- test, CI and log messages;
- developer reference documentation.

Commit messages follow Conventional Commits, use the imperative mood and do not end with a period.

Examples:

```text
docs: define multilingual documentation policy
research: add literature review protocol
feat: add pedagogical profile schema
fix: preserve course configuration on export
```

Branches use English and kebab-case, for example:

```text
docs/initial-governance
research/scoping-review
feat/pedagogical-profiles
```

## User interface

The user interface must support from the beginning:

- Brazilian Portuguese (`pt-BR`);
- European Portuguese (`pt-PT`);
- English (`en`).

Interface strings must not be scattered through source code. They must be stored in versioned locale catalogues. The interface language and course language are independent settings.

## Stable public documentation

Stable public documents must be maintained in English, Brazilian Portuguese and European Portuguese when they are relevant to users, adopters or contributors. This includes, progressively:

- project overview;
- installation and operation guides;
- learner and institutional guides;
- contribution guidance;
- licensing and trademark guidance;
- privacy, accessibility and security documentation;
- published release documentation.

The English version normally uses the base filename. Portuguese variants use `.pt-BR` and `.pt-PT` before the extension.

## Research work

Working research documents normally use Brazilian Portuguese as their canonical drafting language. This includes:

- preliminary protocols;
- evidence matrices;
- literature extraction records;
- design hypotheses;
- biographical and historical records;
- working notes for future academic writing.

A European Portuguese version is produced when required for formal work at the University of Lisbon. An English version is produced when needed for international collaboration or publication.

Translations must not silently change evidence, terminology, limitations or decisions. The canonical source and translation status must be identifiable.

## Legal and institutional documents

Legal documents follow their jurisdiction:

- Brazil: Brazilian Portuguese;
- Portugal: European Portuguese;
- European Union and international matters: the official source language, with clearly identified summaries or translations where useful.

A translation never replaces the authoritative legal text.

## Bibliographic records

Bibliographic metadata preserves the source language. Titles, journal names, identifiers and quoted terminology are not translated unless a separate translated field is explicitly recorded. Research summaries and extraction notes normally use Brazilian Portuguese.

## Review rule

A change to stable public documentation is incomplete when it creates material divergence among maintained language variants. Pull requests must state which variants were updated and whether a translation remains pending.
