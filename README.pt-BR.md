# ARA

[English](README.md) | [Português do Brasil](README.pt-BR.md) | [Português de Portugal](README.pt-PT.md)

**Plataforma ARA — Ambiente de Recursos de Aprendizagem**

A ARA é uma plataforma educacional aberta, configurável, mobile-first e preparada para uso offline, sucessora direta do [AraLearn](https://github.com/fabio-ara/AraLearn).

```text
versão de curso → módulo/lição → placement → revisão de microssequência → card
```

## Estágio atual

O ARA está em pesquisa, definição do produto e exploração de design, antes do desenvolvimento. As Issues #4–#8 produziram baselines de configuração, pesquisa/analytics, produto/domínio, arquitetura e UX. Elas servem ao brainstorming e à revisão posterior; nenhuma issue de implementação está ativa ou autorizada.

O pré-backlog v2 reúne agora **197 itens candidatos em 17 áreas**, preservando os 171 itens iniciais e acrescentando uma área dedicada a perfis modulares de agente, curadoria participativa, diffs, evals e analytics quantitativos, qualitativos e mistos.

A Issue #77 é a frente focal ativa. Ela investiga como decompor a configuração monolítica de GPT/MCP do AraLearn em instruções, perfis de domínio, templates, coleções de conhecimento, contexto, tools/contracts e evals versionados, mantendo controle humano e interface simples. O corpus inicial contém 34 fontes e não autoriza código ou coleta de participantes.

## Caminho canônico

1. [Visão do produto](docs/vision/product-vision.pt-BR.md)
2. [Requisitos](docs/product/product-requirements-v1.md)
3. [Modelo de domínio](docs/product/domain-model-v1.md)
4. [Arquitetura](docs/architecture/reference-architecture-v1.md)
5. [UX](docs/ux/ux-specification-v1.md)
6. [Idealização do produto e pré-backlog](docs/ideation/README.md)
7. [Programa de pesquisa](docs/research/research-programme-index.pt-BR.md)
8. [Backlog e regras das fases](docs/roadmap/backlog-index.md)

O protótipo estrutural em [`prototypes/ux-v1/`](prototypes/ux-v1/) e os wireframes de idealização não são produto e servem apenas à discussão. A entrada em desenvolvimento exigirá decisão explícita posterior do proprietário e novo programa de implementação revisado.

## Governança e licenciamento

- [Governança](docs/governance/repository-governance.pt-BR.md)
- [Política linguística](docs/governance/language-policy.pt-BR.md)
- [Como contribuir](CONTRIBUTING.pt-BR.md)
- Código: [AGPL-3.0-or-later](LICENSE)
- Documentação: [CC BY 4.0](LICENSE-DOCUMENTATION.md)
- Identidade: [TRADEMARKS.md](TRADEMARKS.md)
