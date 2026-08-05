# ARA

[English](README.md) | [Português do Brasil](README.pt-BR.md) | [Português de Portugal](README.pt-PT.md)

**Plataforma ARA — Ambiente de Recursos de Aprendizagem**

A ARA é uma plataforma educacional aberta, configurável, mobile-first e preparada para uso offline, sucessora direta do [AraLearn](https://github.com/fabio-ara/AraLearn).

```text
versão de curso → módulo/lição → placement → revisão de microssequência → card
```

## Estágio atual

O ARA está em pesquisa, definição do produto e exploração de design, antes do desenvolvimento. Nenhuma issue de implementação está ativa ou autorizada.

O pré-backlog v4 reúne **233 itens candidatos em 19 áreas**:

- 171 itens iniciais;
- 26 itens de agentes, participação e analytics;
- 10 itens de versionamento, Storage e economia;
- 26 itens de grafo, acesso derivacional e autoria sem burocracia.

Frentes focais:

- **#77:** agentes modulares, observações e analytics;
- **#79:** artefatos imutáveis, Storage, workloads, retenção e custo;
- **#81:** grafo visível de versões, checkpoints automáticos e público/privado com acesso herdado.

A direção da #81 combina precedentes de visibilidade hierárquica, guardrails, delegação atenuada, controle de informação derivada e ACLs relacionais. O nome técnico candidato é **controle de acesso derivacional com atenuação monotônica**. A interface comum continua usando apenas Público, Privado e Quem pode acessar.

## Caminho canônico

1. [Visão do produto](docs/vision/product-vision.pt-BR.md)
2. [Requisitos](docs/product/product-requirements-v1.md)
3. [Modelo de domínio](docs/product/domain-model-v1.md)
4. [Arquitetura](docs/architecture/reference-architecture-v1.md)
5. [UX](docs/ux/ux-specification-v1.md)
6. [Idealização do produto e pré-backlog](docs/ideation/README.md)
7. [Programa de pesquisa](docs/research/research-programme-index.pt-BR.md)
8. [Backlog e regras das fases](docs/roadmap/backlog-index.md)

O protótipo estrutural e os wireframes não são produto. A entrada em desenvolvimento exigirá decisão explícita do proprietário, revisão das baselines e novo programa de implementação.

## Governança e licenciamento

- [Governança](docs/governance/repository-governance.pt-BR.md)
- [Política linguística](docs/governance/language-policy.pt-BR.md)
- [Como contribuir](CONTRIBUTING.pt-BR.md)
- Código: [AGPL-3.0-or-later](LICENSE)
- Documentação: [CC BY 4.0](LICENSE-DOCUMENTATION.md)
- Identidade: [TRADEMARKS.md](TRADEMARKS.md)
