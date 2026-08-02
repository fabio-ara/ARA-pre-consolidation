# Política linguística

[English](language-policy.md) | [Português do Brasil](language-policy.pt-BR.md) | [Português de Portugal](language-policy.pt-PT.md)

## Finalidade

A ARA destina-se a estudantes autodidatas, pesquisadores e instituições no Brasil, em Portugal e em outros países. O repositório, portanto, distingue o idioma da engenharia, da comunicação pública, da pesquisa em elaboração e da documentação específica de cada jurisdição.

## Idioma da engenharia

O inglês é o idioma canônico para:

- mensagens de commit;
- nomes de branches;
- títulos de issues e pull requests;
- identificadores do código-fonte;
- APIs, schemas, identificadores do banco de dados e nomes de eventos;
- mensagens de testes, integração contínua e logs;
- documentação técnica de referência para desenvolvedores.

As mensagens de commit seguem Conventional Commits, usam o imperativo e não terminam com ponto final.

Exemplos:

```text
docs: define multilingual documentation policy
research: add literature review protocol
feat: add pedagogical profile schema
fix: preserve course configuration on export
```

As branches usam inglês e `kebab-case`, por exemplo:

```text
docs/initial-governance
research/scoping-review
feat/pedagogical-profiles
```

## Interface

A interface deverá oferecer desde o início:

- português brasileiro (`pt-BR`);
- português europeu (`pt-PT`);
- inglês (`en`).

Os textos da interface não podem ficar espalhados pelo código-fonte. Devem residir em catálogos de localização versionados. O idioma da interface e o idioma do curso são configurações independentes.

## Documentação pública estável

Documentos públicos estáveis deverão ser mantidos em inglês, português brasileiro e português europeu quando forem relevantes para usuários, instituições adotantes ou colaboradores. Isso inclui progressivamente:

- apresentação do projeto;
- guias de instalação e operação;
- guias do estudante e da instituição;
- orientações de contribuição;
- orientações de licenciamento e marca;
- documentação de privacidade, acessibilidade e segurança;
- documentação de versões publicadas.

A versão inglesa usa normalmente o nome-base do arquivo. As variantes em português usam `.pt-BR` e `.pt-PT` antes da extensão.

## Pesquisa em elaboração

Documentos de pesquisa em elaboração usarão normalmente o português brasileiro como idioma canônico. Isso inclui:

- protocolos preliminares;
- matrizes de evidência;
- registros de extração bibliográfica;
- hipóteses de desenho;
- registros biográficos e históricos;
- notas de trabalho para futura escrita acadêmica.

Uma versão em português europeu será produzida quando necessária para trabalhos formais na Universidade de Lisboa. Uma versão inglesa será produzida quando necessária para colaboração ou publicação internacional.

Traduções não podem alterar silenciosamente evidências, terminologia, limitações ou decisões. A fonte canônica e o estado da tradução deverão ser identificáveis.

## Documentos jurídicos e institucionais

Documentos jurídicos seguem a jurisdição:

- Brasil: português brasileiro;
- Portugal: português europeu;
- União Europeia e matérias internacionais: idioma oficial da fonte, com sínteses ou traduções claramente identificadas quando úteis.

Uma tradução nunca substitui o texto jurídico oficial.

## Registros bibliográficos

Os metadados bibliográficos preservam o idioma original. Títulos, nomes de periódicos, identificadores e terminologia citada não são traduzidos, salvo quando houver um campo de tradução explicitamente registrado. Sínteses e fichas de extração serão normalmente redigidas em português brasileiro.

## Regra de revisão

Uma mudança em documentação pública estável estará incompleta quando criar divergência material entre as variantes mantidas. Pull requests deverão informar quais variantes foram atualizadas e se alguma tradução permanece pendente.
