# ARA

[English](README.md) | [Português do Brasil](README.pt-BR.md) | [Português de Portugal](README.pt-PT.md)

**Plataforma ARA — Ambiente de Recursos de Aprendizagem**

A ARA é uma plataforma educativa aberta, configurável, mobile-first e preparada para utilização offline, sucessora direta do [AraLearn](https://github.com/fabio-ara/AraLearn).

```text
versão de curso → módulo/lição → placement → revisão de microssequência → card
```

## Fase atual

O ARA encontra-se em investigação, definição do produto e exploração de design, antes do desenvolvimento. As Issues #4–#8 produziram baselines conceptuais; nenhuma issue de implementação está ativa ou autorizada.

O pré-backlog v3 reúne **207 itens candidatos em 18 áreas**:

- 171 itens iniciais;
- 26 itens de perfis modulares de agente, curadoria participativa e analytics;
- 10 itens de versionamento, retenção, armazenamento e economia operacional.

A Issue #77 investiga agentes modulares e analytics. O AraLearn é tratado como referência funcional e caso de contraste, não como implementação modular equivalente.

A Issue #79 investiga como sustentar o versionamento previsto: metadata relacional, artefactos imutáveis, deduplicação, retenção, workloads, Supabase Free/Pro, object storage, alternativas portáteis, backup e restauro. Não seleciona nem autoriza contratação de fornecedor.

## Caminho canónico

1. [Visão do produto](docs/vision/product-vision.pt-BR.md)
2. [Requisitos](docs/product/product-requirements-v1.md)
3. [Modelo de domínio](docs/product/domain-model-v1.md)
4. [Arquitetura](docs/architecture/reference-architecture-v1.md)
5. [UX](docs/ux/ux-specification-v1.md)
6. [Idealização do produto e pré-backlog](docs/ideation/README.md)
7. [Programa de investigação](docs/research/research-programme-index.pt-BR.md)
8. [Backlog e regras das fases](docs/roadmap/backlog-index.md)

O protótipo estrutural e os wireframes não são produto. A entrada em desenvolvimento exigirá uma decisão explícita posterior do proprietário, revisão das baselines e um novo programa de implementação revisto.

## Governação e licenciamento

- [Governação](docs/governance/repository-governance.pt-PT.md)
- [Política linguística](docs/governance/language-policy.pt-PT.md)
- [Como contribuir](CONTRIBUTING.pt-PT.md)
- Código: [AGPL-3.0-or-later](LICENSE)
- Documentação: [CC BY 4.0](LICENSE-DOCUMENTATION.md)
- Identidade: [TRADEMARKS.md](TRADEMARKS.md)
