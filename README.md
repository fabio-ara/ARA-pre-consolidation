# ARA

[English](README.md) | [Português do Brasil](README.pt-BR.md) | [Português de Portugal](README.pt-PT.md)

**ARA Platform — Learning Resources Environment**

ARA is an open, configurable, mobile-first and offline-capable educational platform and the direct successor to [AraLearn](https://github.com/fabio-ara/AraLearn).

```text
course version → module/lesson → placement → microsequence revision → card
```

## Current stage

ARA is in pre-development research, product definition and design exploration. Issues #4–#8 produced conceptual baselines; no product implementation issue is active or authorized.

Draft backlog v3 contains **207 candidate items across 18 areas**:

- 171 original items;
- 26 items for modular agent profiles, participatory curation and analytics;
- 10 items for versioning, retention, storage and deployment economics.

Issue #77 studies modular agents and analytics. AraLearn is treated as the main functional reference and a contrast case, not as an equivalent modular implementation.

Issue #79 studies how to sustain the intended versioning model: relational metadata, immutable artifacts, deduplication, retention, workloads, Supabase Free/Pro, object storage, portable alternatives, backup and restore. It neither selects nor authorizes purchase of a provider.

## Canonical path

1. [Product vision](docs/vision/product-vision.pt-BR.md)
2. [Product requirements](docs/product/product-requirements-v1.md)
3. [Domain model](docs/product/domain-model-v1.md)
4. [Reference architecture](docs/architecture/reference-architecture-v1.md)
5. [UX specification](docs/ux/ux-specification-v1.md)
6. [Product ideation and draft backlog (pt-BR)](docs/ideation/README.md)
7. [Research programme](docs/research/research-programme-index.pt-BR.md)
8. [Backlog and phase rules](docs/roadmap/backlog-index.md)

The structural prototype and wireframes are not product. Entering implementation requires a later explicit owner decision, baseline review and a newly reviewed implementation programme.

## Governance and licensing

- [Governance](docs/governance/repository-governance.md)
- [Language policy](docs/governance/language-policy.md)
- [Contributing](CONTRIBUTING.md)
- Source: [AGPL-3.0-or-later](LICENSE)
- Documentation: [CC BY 4.0](LICENSE-DOCUMENTATION.md)
- Identity: [TRADEMARKS.md](TRADEMARKS.md)
