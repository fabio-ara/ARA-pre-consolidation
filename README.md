# ARA

[English](README.md) | [Português do Brasil](README.pt-BR.md) | [Português de Portugal](README.pt-PT.md)

**ARA Platform — Learning Resources Environment**

ARA is an open, configurable, mobile-first and offline-capable educational platform and the direct successor to [AraLearn](https://github.com/fabio-ara/AraLearn).

```text
course version → module/lesson → placement → microsequence revision → card
```

## Current stage

ARA is in pre-development research, product definition and design exploration. Issues #4–#8 produced configuration, research/analytics, product/domain, architecture and UX baselines. They support continued brainstorming and later review; no product implementation issue is active or authorized.

Draft backlog v2 now contains **197 candidate items across 17 areas**, preserving the original 171 items and adding a new area for modular agent profiles, participatory curation, diffs, evals and quantitative, qualitative and mixed-method analytics.

Issue #77 is the active focused research round. It investigates how to decompose AraLearn's monolithic GPT/MCP configuration into versioned instructions, domain profiles, templates, knowledge collections, context policies, tools/contracts and evals while preserving human control and a simple interface. The initial corpus contains 34 sources and authorizes neither product code nor participant collection.

## Canonical path

1. [Product vision](docs/vision/product-vision.pt-BR.md)
2. [Product requirements](docs/product/product-requirements-v1.md)
3. [Domain model](docs/product/domain-model-v1.md)
4. [Reference architecture](docs/architecture/reference-architecture-v1.md)
5. [UX specification](docs/ux/ux-specification-v1.md)
6. [Product ideation and draft backlog (pt-BR)](docs/ideation/README.md)
7. [Research programme](docs/research/research-programme-index.pt-BR.md)
8. [Backlog and phase rules](docs/roadmap/backlog-index.md)

The structural UX prototype in [`prototypes/ux-v1/`](prototypes/ux-v1/) and the ideation wireframes are non-production materials for discussion. Entering implementation requires a later explicit owner decision and a newly reviewed implementation programme.

## Governance and licensing

- [Governance](docs/governance/repository-governance.md)
- [Language policy](docs/governance/language-policy.md)
- [Contributing](CONTRIBUTING.md)
- Source: [AGPL-3.0-or-later](LICENSE)
- Documentation: [CC BY 4.0](LICENSE-DOCUMENTATION.md)
- Identity: [TRADEMARKS.md](TRADEMARKS.md)
