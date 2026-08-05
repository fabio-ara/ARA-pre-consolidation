# ARA

[English](README.md) | [Português do Brasil](README.pt-BR.md) | [Português de Portugal](README.pt-PT.md)

**ARA Platform — Learning Resources Environment**

ARA is an open, configurable, mobile-first and offline-capable educational platform and the direct successor to [AraLearn](https://github.com/fabio-ara/AraLearn).

```text
course version → module/lesson → placement → microsequence revision → card
```

## Current stage

ARA is in pre-development research, product definition and design exploration. No product implementation issue is active or authorized.

Draft backlog v4 contains **233 candidate items across 19 areas**:

- 171 initial items;
- 26 items for modular agents, participation and analytics;
- 10 items for versioning, storage and economics;
- 26 items for visible version graphs, derivative access and low-friction authorship.

Focused research:

- **#77:** modular agents, observations and analytics;
- **#79:** immutable artifacts, object storage, workloads, retention and cost;
- **#81:** visible version graphs, automatic checkpoints and public/private access inherited through derivation.

Issue #81 combines precedents from hierarchical visibility, permission guardrails, attenuated delegation, derived-data information flow and relationship-based ACLs. The candidate technical term is **derivative access control with monotonic attenuation**. The common interface still uses only Public, Private and Who can access.

## Canonical path

1. [Product vision](docs/vision/product-vision.pt-BR.md)
2. [Product requirements](docs/product/product-requirements-v1.md)
3. [Domain model](docs/product/domain-model-v1.md)
4. [Reference architecture](docs/architecture/reference-architecture-v1.md)
5. [UX specification](docs/ux/ux-specification-v1.md)
6. [Product ideation and draft backlog (pt-BR)](docs/ideation/README.md)
7. [Research programme](docs/research/research-programme-index.pt-BR.md)
8. [Backlog and phase rules](docs/roadmap/backlog-index.md)

The structural prototype and wireframes are not product. Entering implementation requires an explicit owner decision, baseline review and a newly reviewed implementation programme.

## Governance and licensing

- [Governance](docs/governance/repository-governance.md)
- [Language policy](docs/governance/language-policy.md)
- [Contributing](CONTRIBUTING.md)
- Source: [AGPL-3.0-or-later](LICENSE)
- Documentation: [CC BY 4.0](LICENSE-DOCUMENTATION.md)
- Identity: [TRADEMARKS.md](TRADEMARKS.md)
