# Governação do repositório

[English](repository-governance.md) | [Português do Brasil](repository-governance.pt-BR.md) | [Português de Portugal](repository-governance.pt-PT.md)

## Fontes canónicas

O repositório é o registo autoritativo do projeto ARA. Requisitos, decisões, pressupostos de investigação e trabalhos de implementação não podem depender de conversas privadas, prompts temporários ou instruções não documentadas.

A hierarquia canónica é:

1. visão do projeto e documentos de governação aprovados;
2. registos de decisões arquiteturais e de investigação;
3. Issues do GitHub no backlog canónico;
4. pull requests, commits, testes e evidências de releases.

Quando existir conflito, a decisão mais recente e explicitamente aprovada deverá identificar e substituir a anterior.

## Issues como backlog canónico

Todo o trabalho planeado deve estar representado por uma Issue antes do início de uma execução substancial. As Issues não são lembretes informais; em conjunto, formam o backlog de produto, investigação, matérias jurídicas, documentação e engenharia.

Cada issue executável deverá declarar, conforme aplicável:

- contexto e problema;
- resultado pretendido;
- evidências, fontes ou decisão orientadora;
- âmbito;
- fora de âmbito;
- dependências;
- implicações pedagógicas e de investigação;
- implicações de dados, privacidade, segurança, acessibilidade e direito;
- plano de implementação ou investigação;
- critérios de aceitação;
- testes ou método de validação;
- documentação a atualizar;
- evidências a preservar.

O trabalho descoberto fora do âmbito aprovado deverá originar uma issue associada. Não poderá ser absorvido silenciosamente pela alteração em curso.

## Estrutura do roadmap

Uma issue inicial de roadmap indexará as fases e dependências do projeto. Temas extensos utilizarão issues abrangentes; trabalho executável utilizará issues menores que possam ser concluídas e revistas de forma coerente.

A ordem inicial das fases é:

1. governação, propriedade intelectual e infraestrutura de evidências;
2. levantamento bibliográfico e institucional;
3. taxonomia de parâmetros pedagógicos;
4. protocolos de investigação, instrumentação e analytics;
5. requisitos do produto e modelo de domínio;
6. arquitetura de referência e perfis de implantação;
7. especificação integral de UX e acessibilidade;
8. implementação, validação e releases.

A ordem só poderá mudar através de uma decisão documentada que registe consequências e dependências.

## Pull requests

Todo o pull request não trivial deverá:

- referenciar pelo menos uma issue;
- permanecer dentro do âmbito aprovado;
- explicar a alteração e as suas consequências;
- incluir ou atualizar os testes pertinentes;
- atualizar a documentação afetada no mesmo ciclo;
- identificar limitações não resolvidas e issues de acompanhamento;
- preservar as variantes linguísticas aplicáveis;
- evitar camadas de compatibilidade, fallbacks ou caminhos legados não documentados.

Um pull request não estará concluído apenas porque o código compila. A conclusão será determinada pelos critérios de aceitação e pelas evidências exigidas na issue.

## Camadas de aplicação das regras

As Issues, isoladamente, não impõem mecanicamente as regras do repositório. A aplicação é cumulativa:

1. esta política de governação;
2. `CONTRIBUTING.md`;
3. formulários obrigatórios de issues;
4. template de pull request;
5. proteção da branch e revisões obrigatórias;
6. verificações automatizadas de testes, documentação, licenciamento e rastreabilidade;
7. critérios de release e auditorias de evidência.

A proteção da branch e as regras de CI serão introduzidas antes do início da implementação. Até lá, os responsáveis pela manutenção deverão aplicar manualmente os mesmos requisitos.

## Registos de decisão e evidência

As decisões significativas deverão preservar:

- problema;
- alternativas consideradas;
- evidências e fontes;
- decisão escolhida;
- limitações e riscos;
- reversibilidade;
- requisitos afetados;
- issues, pull requests e releases relacionados.

As conclusões de investigação deverão distinguir evidência, inferência, hipótese e preferência pessoal. Os testes de software demonstram conformidade com uma especificação, não eficácia educativa.

## Limites documentais

O repositório poderá conter documentação pública e análises derivadas de fontes privadas, mas não poderá publicar artigos, livros, materiais institucionais restritos, dados pessoais ou informação biográfica sensível sem autorização. Metadados, registos de extração, análises e citações poderão ser armazenados quando tal seja lícito e adequado.

## Ausência de requisitos ocultos

Um colaborador deverá conseguir compreender a tarefa atual através da leitura do repositório. Qualquer instrução que altere âmbito, arquitetura, pedagogia, tratamento jurídico, recolha de dados ou comportamento de release deverá ser registada na issue ou no documento orientador pertinente antes da implementação.
