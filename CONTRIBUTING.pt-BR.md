# Como contribuir com a ARA

[English](CONTRIBUTING.md) | [Português do Brasil](CONTRIBUTING.pt-BR.md) | [Português de Portugal](CONTRIBUTING.pt-PT.md)

A ARA está sendo desenvolvida como plataforma educacional, infraestrutura de pesquisa e artefato técnico público. As contribuições deverão preservar a rastreabilidade entre evidências, decisões, requisitos, implementação e validação.

## Antes de começar

Leia:

- [Governança do repositório](docs/governance/repository-governance.pt-BR.md)
- [Política linguística](docs/governance/language-policy.pt-BR.md)
- [Limites de licenciamento](LICENSING.md)
- [Política de marca](TRADEMARKS.md)

Todo trabalho substancial deverá possuir uma Issue aprovada. Não implemente requisitos que existam apenas numa conversa, mensagem ou anotação local.

## Issues

Use os formulários de issue do repositório. Uma issue executável deverá definir problema, escopo, dependências, critérios de aceitação, validação, documentação e implicações pertinentes de pesquisa, pedagogia, dados, segurança, acessibilidade ou direito.

Quando surgir trabalho fora do escopo, crie uma issue vinculada, em vez de ampliar silenciosamente a alteração atual.

## Branches

Use inglês, letras minúsculas e `kebab-case`:

```text
docs/initial-governance
research/scoping-review
feat/pedagogical-profiles
fix/course-versioning
```

## Commits

Use Conventional Commits em inglês, no imperativo e sem ponto final:

```text
docs: define multilingual documentation policy
research: add literature review protocol
feat: add pedagogical profile schema
fix: preserve course configuration on export
```

Mantenha os commits coerentes e revisáveis. Não misture trabalhos sem relação.

## Pull requests

Todo pull request não trivial deverá:

- referenciar sua issue orientadora;
- explicar o problema e a solução;
- permanecer dentro do escopo;
- incluir validação e testes pertinentes;
- atualizar a documentação no mesmo ciclo;
- informar variantes linguísticas atualizadas ou pendentes;
- identificar efeitos em dados, segurança, acessibilidade, licenciamento e direito;
- registrar limitações e issues de acompanhamento;
- evitar fallbacks, caminhos de compatibilidade e comportamento legado não documentados.

## Evidências e pesquisa

Não apresente preferência pessoal, inferência ou comportamento da implementação como evidência educacional estabelecida. Distinga:

- evidência apoiada em fontes;
- inferência fundamentada;
- hipótese de desenho;
- preferência pessoal ou institucional;
- resultado empírico produzido pela ARA.

Não publique textos integrais restritos de artigos ou livros, dados de participantes, material institucional confidencial ou registros pessoais sensíveis. Preserve, quando lícito, metadados, citações, notas de extração e análises derivadas.

## Idiomas da documentação

O trabalho de engenharia usa inglês. A documentação pública estável será mantida em inglês, português brasileiro e português europeu quando aplicável. Documentos de pesquisa em elaboração usarão normalmente o português brasileiro como idioma canônico.

## Licenciamento

Ao contribuir com código, você concorda que ele será disponibilizado sob `AGPL-3.0-or-later`, salvo quando um arquivo declarar explicitamente outra licença compatível. A documentação do projeto será disponibilizada sob `CC BY 4.0`, salvo indicação em contrário.

O colaborador deverá possuir direito de submeter seu trabalho. Código, mídia, instrumentos, conjuntos de dados e materiais educacionais de terceiros exigem proveniência explícita e termos compatíveis.

O nome ARA, o kanji, o logotipo e a identidade visual são regidos separadamente e não são licenciados pelas licenças do código ou da documentação.
