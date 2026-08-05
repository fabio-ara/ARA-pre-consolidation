# ARA

[English](README.md) | [Português do Brasil](README.pt-BR.md) | [Português de Portugal](README.pt-PT.md)

**Plataforma ARA — Ambiente de Recursos de Aprendizagem**

A ARA é uma plataforma educativa aberta, configurável, mobile-first e preparada para utilização offline, sucessora direta do [AraLearn](https://github.com/fabio-ara/AraLearn).

```text
versão de curso → módulo/lição → placement → revisão de microssequência → card
```

## Fase atual

O ARA encontra-se em investigação, definição do produto e exploração de design, antes do desenvolvimento. Nenhuma issue de implementação está ativa ou autorizada.

O pré-backlog v4 reúne **233 itens candidatos em 19 áreas**:

- 171 itens iniciais;
- 26 itens de agentes, participação e analytics;
- 10 itens de versionamento, Storage e economia;
- 26 itens de grafo, acesso derivacional e autoria sem burocracia.

Frentes focais:

- **#77:** agentes modulares, observações e analytics;
- **#79:** artefactos imutáveis, Storage, workloads, retenção e custo;
- **#81:** grafo visível de versões, checkpoints automáticos e público/privado com acesso herdado.

A direção da #81 combina precedentes de visibilidade hierárquica, guardrails, delegação atenuada, controlo de informação derivada e ACLs relacionais. O nome técnico candidato é **controlo de acesso derivacional com atenuação monotónica**. A interface comum continua a usar apenas Público, Privado e Quem pode aceder.

## Caminho canónico

1. [Visão do produto](docs/vision/product-vision.pt-BR.md)
2. [Requisitos](docs/product/product-requirements-v1.md)
3. [Modelo de domínio](docs/product/domain-model-v1.md)
4. [Arquitetura](docs/architecture/reference-architecture-v1.md)
5. [UX](docs/ux/ux-specification-v1.md)
6. [Idealização do produto e pré-backlog](docs/ideation/README.md)
7. [Programa de investigação](docs/research/research-programme-index.pt-BR.md)
8. [Backlog e regras das fases](docs/roadmap/backlog-index.md)

O protótipo estrutural e os wireframes não são produto. A entrada em desenvolvimento exigirá uma decisão explícita do proprietário, revisão das baselines e um novo programa de implementação revisto.

## Governação e licenciamento

- [Governação](docs/governance/repository-governance.pt-PT.md)
- [Política linguística](docs/governance/language-policy.pt-PT.md)
- [Como contribuir](CONTRIBUTING.pt-PT.md)
- Código: [AGPL-3.0-or-later](LICENSE)
- Documentação: [CC BY 4.0](LICENSE-DOCUMENTATION.md)
- Identidade: [TRADEMARKS.md](TRADEMARKS.md)
