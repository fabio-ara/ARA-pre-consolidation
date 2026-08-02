# Como contribuir para a ARA

[English](CONTRIBUTING.md) | [Português do Brasil](CONTRIBUTING.pt-BR.md) | [Português de Portugal](CONTRIBUTING.pt-PT.md)

A ARA está a ser desenvolvida como plataforma educativa, infraestrutura de investigação e artefacto técnico público. As contribuições deverão preservar a rastreabilidade entre evidências, decisões, requisitos, implementação e validação.

## Antes de começar

Leia:

- [Governação do repositório](docs/governance/repository-governance.pt-PT.md)
- [Política linguística](docs/governance/language-policy.pt-PT.md)
- [Limites de licenciamento](LICENSING.md)
- [Política de marca](TRADEMARKS.md)

Todo o trabalho substancial deverá possuir uma Issue aprovada. Não implemente requisitos que existam apenas numa conversa, mensagem ou anotação local.

## Issues

Utilize os formulários de issue do repositório. Uma issue executável deverá definir problema, âmbito, dependências, critérios de aceitação, validação, documentação e implicações pertinentes de investigação, pedagogia, dados, segurança, acessibilidade ou direito.

Quando surgir trabalho fora do âmbito, crie uma issue associada, em vez de ampliar silenciosamente a alteração atual.

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

Mantenha os commits coerentes e passíveis de revisão. Não combine trabalhos sem relação.

## Pull requests

Todo o pull request não trivial deverá:

- referenciar a respetiva issue orientadora;
- explicar o problema e a solução;
- permanecer dentro do âmbito;
- incluir validação e testes pertinentes;
- atualizar a documentação no mesmo ciclo;
- indicar variantes linguísticas atualizadas ou pendentes;
- identificar efeitos em dados, segurança, acessibilidade, licenciamento e direito;
- registar limitações e issues de acompanhamento;
- evitar fallbacks, caminhos de compatibilidade e comportamento legado não documentados.

## Evidências e investigação

Não apresente preferência pessoal, inferência ou comportamento da implementação como evidência educativa estabelecida. Distinga:

- evidência apoiada em fontes;
- inferência fundamentada;
- hipótese de desenho;
- preferência pessoal ou institucional;
- resultado empírico produzido pela ARA.

Não publique textos integrais restritos de artigos ou livros, dados de participantes, material institucional confidencial ou registos pessoais sensíveis. Preserve, quando lícito, metadados, citações, notas de extração e análises derivadas.

## Idiomas da documentação

O trabalho de engenharia utiliza inglês. A documentação pública estável será mantida em inglês, português do Brasil e português europeu quando aplicável. Os documentos de investigação em elaboração utilizarão normalmente o português do Brasil como idioma canónico.

## Licenciamento

Ao contribuir com código, concorda que este será disponibilizado sob `AGPL-3.0-or-later`, salvo quando um ficheiro declarar explicitamente outra licença compatível. A documentação do projeto será disponibilizada sob `CC BY 4.0`, salvo indicação em contrário.

O colaborador deverá possuir o direito de submeter o seu trabalho. Código, conteúdos multimédia, instrumentos, conjuntos de dados e materiais educativos de terceiros exigem proveniência explícita e termos compatíveis.

O nome ARA, o kanji, o logótipo e a identidade visual são regulados separadamente e não são licenciados pelas licenças do código ou da documentação.
