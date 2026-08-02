# Política linguística

[English](language-policy.md) | [Português do Brasil](language-policy.pt-BR.md) | [Português de Portugal](language-policy.pt-PT.md)

## Finalidade

A ARA destina-se a estudantes autodidatas, investigadores e instituições no Brasil, em Portugal e noutros países. O repositório distingue, por isso, o idioma da engenharia, da comunicação pública, da investigação em curso e da documentação específica de cada jurisdição.

## Idioma da engenharia

O inglês é o idioma canónico para:

- mensagens de commit;
- nomes de branches;
- títulos de issues e pull requests;
- identificadores do código-fonte;
- APIs, schemas, identificadores da base de dados e nomes de eventos;
- mensagens de testes, integração contínua e logs;
- documentação técnica de referência para programadores.

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

A interface deverá disponibilizar desde o início:

- português do Brasil (`pt-BR`);
- português europeu (`pt-PT`);
- inglês (`en`).

Os textos da interface não podem ficar dispersos pelo código-fonte. Devem residir em catálogos de localização versionados. O idioma da interface e o idioma do curso são configurações independentes.

## Documentação pública estável

Os documentos públicos estáveis deverão ser mantidos em inglês, português do Brasil e português europeu quando forem relevantes para utilizadores, instituições adotantes ou colaboradores. Isto inclui progressivamente:

- apresentação do projeto;
- guias de instalação e operação;
- guias do estudante e da instituição;
- orientações de contribuição;
- orientações de licenciamento e marca;
- documentação de privacidade, acessibilidade e segurança;
- documentação das versões publicadas.

A versão inglesa usa normalmente o nome-base do ficheiro. As variantes em português usam `.pt-BR` e `.pt-PT` antes da extensão.

## Investigação em curso

Os documentos de investigação em elaboração utilizarão normalmente o português do Brasil como idioma canónico. Isto inclui:

- protocolos preliminares;
- matrizes de evidência;
- registos de extração bibliográfica;
- hipóteses de desenho;
- registos biográficos e históricos;
- notas de trabalho para futura escrita académica.

Será produzida uma versão em português europeu quando necessária para trabalhos formais na Universidade de Lisboa. Será produzida uma versão inglesa quando necessária para colaboração ou publicação internacional.

As traduções não podem alterar silenciosamente evidências, terminologia, limitações ou decisões. A fonte canónica e o estado da tradução deverão ser identificáveis.

## Documentos jurídicos e institucionais

Os documentos jurídicos seguem a jurisdição:

- Brasil: português do Brasil;
- Portugal: português europeu;
- União Europeia e matérias internacionais: idioma oficial da fonte, com sínteses ou traduções claramente identificadas quando úteis.

Uma tradução nunca substitui o texto jurídico oficial.

## Registos bibliográficos

Os metadados bibliográficos preservam o idioma original. Títulos, nomes de publicações, identificadores e terminologia citada não são traduzidos, salvo quando exista um campo de tradução explicitamente registado. As sínteses e fichas de extração serão normalmente redigidas em português do Brasil.

## Regra de revisão

Uma alteração à documentação pública estável estará incompleta quando criar divergência material entre as variantes mantidas. Os pull requests deverão indicar quais as variantes atualizadas e se alguma tradução permanece pendente.
