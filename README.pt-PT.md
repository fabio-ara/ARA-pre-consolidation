# ARA

[English](README.md) | [Português do Brasil](README.pt-BR.md) | [Português de Portugal](README.pt-PT.md)

**Plataforma ARA — Ambiente de Recursos de Aprendizagem**

A ARA é uma plataforma educativa aberta, configurável, mobile-first e preparada para utilização offline, sucessora direta do [AraLearn](https://github.com/fabio-ara/AraLearn).

```text
versão de curso → módulo/lição → placement → revisão de microssequência → card
```

## Fase atual

O ARA encontra-se em investigação, definição do produto e exploração de design, antes do desenvolvimento. Nenhuma issue de implementação está ativa ou autorizada.

O pré-backlog v5 reúne **243 itens candidatos em 19 áreas**:

- 171 itens iniciais;
- 26 itens de agentes, participação e analytics;
- 20 itens de versionamento, arquitetura de histórico e economia operacional;
- 26 itens de grafo, acesso derivacional e autoria sem burocracia.

Frentes focais:

- **#77:** agentes modulares, observações e analytics;
- **#79:** razões do versionamento, alternativas técnicas e impactos na base de dados, Storage, IndexedDB, front-end e custo;
- **#81:** grafo visível de versões e público/privado com acesso herdado.

O versionamento é adotado para reduzir burocracia: a edição comum é local e imediata; autosaves tornam-se checkpoints automáticos; revisões duráveis preservam erros, reparações, restauros e derivações. A investigação compara snapshots na base de dados ou Storage, content addressing, patches, event sourcing, tabelas temporais, bucket versioning, Git e camadas Git-like antes de qualquer escolha.

A direção de acesso da #81 usa **controlo de acesso derivacional com atenuação monotónica** como nome técnico candidato. A interface comum continua a usar apenas Público, Privado e Quem pode aceder.

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
