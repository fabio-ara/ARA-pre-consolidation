# Governança do repositório

[English](repository-governance.md) | [Português do Brasil](repository-governance.pt-BR.md) | [Português de Portugal](repository-governance.pt-PT.md)

## Fontes canônicas

O repositório é o registro autoritativo do projeto ARA. Requisitos, decisões, pressupostos de pesquisa e trabalhos de implementação não podem depender de conversas privadas, prompts temporários ou instruções não documentadas.

A hierarquia canônica é:

1. visão do projeto e documentos de governança aprovados;
2. registros de decisões arquiteturais e de pesquisa;
3. Issues do GitHub no backlog canônico;
4. pull requests, commits, testes e evidências de releases.

Quando houver conflito, a decisão mais recente e explicitamente aprovada deverá identificar e substituir a anterior.

## Issues como backlog canônico

Todo trabalho planejado deve estar representado por uma Issue antes do início de uma execução substancial. Issues não são lembretes informais; em conjunto, formam o backlog de produto, pesquisa, aspectos jurídicos, documentação e engenharia.

Cada issue executável deverá declarar, conforme aplicável:

- contexto e problema;
- resultado pretendido;
- evidências, fontes ou decisão orientadora;
- escopo;
- fora de escopo;
- dependências;
- implicações pedagógicas e de pesquisa;
- implicações de dados, privacidade, segurança, acessibilidade e direito;
- plano de implementação ou investigação;
- critérios de aceitação;
- testes ou método de validação;
- documentação a atualizar;
- evidências a preservar.

Trabalho descoberto fora do escopo aprovado deverá virar issue vinculada. Não poderá ser absorvido silenciosamente pela alteração em curso.

## Estrutura do roadmap

Uma issue inicial de roadmap indexará fases e dependências do projeto. Temas grandes usarão issues abrangentes; trabalho executável usará issues menores que possam ser concluídas e revisadas de maneira coerente.

A ordem inicial das fases é:

1. governança, propriedade intelectual e infraestrutura de evidências;
2. levantamento bibliográfico e institucional;
3. taxonomia de parâmetros pedagógicos;
4. protocolos de pesquisa, instrumentação e analytics;
5. requisitos do produto e modelo de domínio;
6. arquitetura de referência e perfis de implantação;
7. especificação integral de UX e acessibilidade;
8. implementação, validação e releases.

A ordem somente poderá mudar por meio de decisão documentada que registre consequências e dependências.

## Pull requests

Todo pull request não trivial deverá:

- referenciar pelo menos uma issue;
- permanecer dentro do escopo aprovado;
- explicar a mudança e suas consequências;
- incluir ou atualizar os testes pertinentes;
- atualizar a documentação afetada no mesmo ciclo;
- identificar limitações não resolvidas e issues de acompanhamento;
- preservar as variantes linguísticas aplicáveis;
- evitar camadas de compatibilidade, fallbacks ou caminhos legados não documentados.

Um pull request não estará concluído apenas porque o código compila. A conclusão será determinada pelos critérios de aceitação e pelas evidências exigidas na issue.

## Camadas de aplicação das regras

Issues, isoladamente, não impõem mecanicamente as regras do repositório. A aplicação é cumulativa:

1. esta política de governança;
2. `CONTRIBUTING.md`;
3. formulários obrigatórios de issues;
4. template de pull request;
5. proteção de branch e revisões obrigatórias;
6. verificações automatizadas de testes, documentação, licenciamento e rastreabilidade;
7. critérios de release e auditorias de evidência.

A proteção da branch e as regras de CI serão introduzidas antes do início da implementação. Até lá, os mantenedores deverão aplicar manualmente os mesmos requisitos.

## Registros de decisão e evidência

Decisões significativas deverão preservar:

- problema;
- alternativas consideradas;
- evidências e fontes;
- decisão escolhida;
- limitações e riscos;
- reversibilidade;
- requisitos afetados;
- issues, pull requests e releases relacionados.

Conclusões de pesquisa deverão distinguir evidência, inferência, hipótese e preferência pessoal. Testes de software demonstram conformidade com uma especificação, não eficácia educacional.

## Limites documentais

O repositório poderá conter documentação pública e análises derivadas de fontes privadas, mas não poderá publicar artigos, livros, materiais institucionais restritos, dados pessoais ou informações biográficas sensíveis sem autorização. Metadados, registros de extração, análises e citações poderão ser armazenados quando isso for lícito e adequado.

## Ausência de requisitos ocultos

Um colaborador deverá conseguir compreender a tarefa atual lendo o repositório. Qualquer instrução que altere escopo, arquitetura, pedagogia, tratamento jurídico, coleta de dados ou comportamento de release deverá ser registrada na issue ou no documento orientador pertinente antes da implementação.
