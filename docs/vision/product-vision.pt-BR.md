# Visão canônica atual do produto ARA

**Estado:** canônico para a fase de pesquisa e definição do produto  
**Idioma de trabalho:** `pt-BR`  
**Última consolidação:** 3 de agosto de 2026  
**Autoridade:** consolida a visão inicial, a memória do sucessor do AraLearn, a clarificação estratégica posterior e a síntese integrada da Issue #30. Não substitui as fontes históricas; governa a interpretação atual delas.

## 1. Definição do produto

ARA — Ambiente de Recursos de Aprendizagem / Learning Resources Environment — será o sucessor direto do AraLearn.

O produto preservará a experiência funcional que já demonstrou valor no AraLearn, mas será reconstruído sobre uma arquitetura deliberadamente escolhida para:

- parametrização pedagógica e experimental;
- pesquisa acadêmica reproduzível;
- autoria, revisão e reparo por ChatGPT com MCP;
- estudo mobile-first e offline;
- extensibilidade governada;
- portabilidade de infraestrutura;
- adoção pessoal, acadêmica e institucional.

ARA não é apenas o AraLearn com mais opções. Também não é uma plataforma universal que deve implementar antecipadamente toda interação educacional possível.

A direção recomendada é:

```text
experiência validada do AraLearn
+ investigação externa ampla, representativa e finita
+ parametrização explícita e versionada
+ kernel pequeno e controlado
+ resources e capacidades independentes
+ infraestrutura por contratos e adapters
+ pesquisa, decisão, arquitetura e UX antes da implementação
```

## 2. Continuidade com o AraLearn

### 2.1 Preservar como referência comportamental

- estrutura `curso → módulo → lição → microssequência → card`;
- separação entre teoria e prática;
- progressão simples e retomada rápida;
- estudo mobile-first e offline;
- resources estruturados;
- validação determinística onde metodologicamente adequada;
- autoria, auditoria e reparo por ChatGPT com MCP;
- comentários e observações situados;
- publicação e aplicação explícitas;
- curadoria e autoridade humanas;
- aprendizagem derivada dos casos reais, defeitos e correções do AraLearn.

### 2.2 Não herdar automaticamente

- stack atual;
- JavaScript puro;
- organização interna do código;
- contrato monolítico `aralearn.resources.v4`;
- acoplamento com Supabase;
- frontend atual;
- limitações históricas de resposta e prática;
- preferências pessoais convertidas em regras universais;
- decisões provisórias dos experimentos de componentes.

AraLearn é a primeira configuração funcional de referência, uma fonte central de evidência e uma possível origem de lógica auditável. Não é o limite do espaço de possibilidades nem uma arquitetura obrigatória.

## 3. Transformação central: parametrização

ARA deve tornar explícitas, versionadas e pesquisáveis decisões que podem variar entre cursos, usuários, condições experimentais, protocolos, implantações e políticas institucionais.

As famílias candidatas incluem, sem se limitar a:

- tentativas e novas tentativas;
- progressão e bloqueios;
- feedback: conteúdo, momento, persistência e autoridade;
- revelação de respostas;
- avaliação, pontuação, notas e consequências;
- resposta selecionada, construída, explicativa ou executável;
- repetição, revisão, espaçamento e intercalação;
- sequenciamento;
- extensão, segmentação e granularidade;
- exemplos resolvidos, pistas e scaffolding;
- adaptação;
- autonomia e learner control;
- acessibilidade e acomodações;
- assistência por IA;
- comentários, revisão, reparo e publicação;
- eventos, analytics e retenção;
- condições experimentais e bloqueio de configuração.

Cada parâmetro deverá registrar:

- definição;
- origem e estado da evidência;
- relação com o perfil AraLearn, inclusive `ausente` ou `não aplicável`;
- valores possíveis;
- escopo;
- autoridade;
- precedência e possibilidade de override;
- conflitos e dependências;
- implicações pedagógicas;
- implicações para pesquisa e analytics;
- acessibilidade, privacidade, offline, desempenho, MCP e UX;
- maturidade: descoberto, candidato, recomendado, aceito, adiado ou rejeitado.

A descoberta será ampla. A normatização será seletiva.

## 4. Kernel

ARA deve possuir um kernel pequeno, coeso, versionado e de evolução controlada.

Responsabilidades transversais candidatas do kernel:

- carregar e validar cursos;
- resolver versões e capacidades;
- executar o ciclo de cards;
- despachar resources, práticas e outras capacidades para implementações registradas;
- aplicar configuração e políticas;
- controlar estado, progressão, feedback e retomada;
- persistir e operar offline;
- registrar somente eventos autorizados;
- integrar-se a contratos de infraestrutura;
- tratar capacidades ausentes de modo previsível.

O kernel não deverá conter semântica específica de matemática, química, linguística, programação, grafos, diagramas, mapas, música ou outro domínio.

Adicionar rotineiramente um resource, renderer, prática, validator, instrumento ou adapter não deverá exigir refatoração do kernel. Alterações do núcleo exigirão decisão arquitetural e versionamento de contrato.

A divisão exata de responsabilidades permanece sujeita à Issue #6 e à Issue #7.

## 5. Resources e categorias relacionadas

Um `resource` representa e renderiza conteúdo declarativo armazenado no documento do curso. Exemplos: texto, fórmula, tabela, código formatado, citação e diagrama estruturado.

`Resource` não deve absorver silenciosamente:

- prática;
- resposta do estudante;
- validator;
- runtime;
- editor executável;
- instrumento de pesquisa;
- avaliação discursiva;
- integração com LLM;
- serviço externo.

A pesquisa e o modelo de domínio poderão recomendar categorias adicionais.

Cada tipo de resource deverá possuir contrato independente, incluindo conforme a necessidade:

- identidade e versão;
- descrição resumida e finalidade;
- schema e validação;
- renderer;
- alternativa acessível;
- capacidades e limitações;
- eventos possíveis, sem implicar coleta automática;
- compatibilidade e migrações;
- requisitos de pacote;
- exemplos;
- testes e critérios de auditoria.

O kernel conhecerá somente a interface comum necessária para descobrir, carregar, validar e despachar resources.

## 6. Autoria por ChatGPT com MCP

O modelo não deverá receber um schema monolítico com todo o catálogo.

Fluxo pretendido:

1. analisar a finalidade pedagógica, o conteúdo e a operação cognitiva;
2. consultar por MCP a lista resumida de resources e capacidades disponíveis;
3. selecionar candidatos por metadados;
4. solicitar somente os contratos completos necessários;
5. construir ou atualizar cards e cursos;
6. validar deterministicamente;
7. reparar erros localizados;
8. produzir prévia;
9. persistir, aplicar ou publicar somente segundo autoridade explícita.

Operações conceituais futuras do MCP:

- listar resources e capacidades;
- consultar metadados;
- obter contrato específico;
- validar uma instância;
- produzir prévia;
- criar ou atualizar cards e cursos;
- informar capacidades instaladas;
- auditar e reparar conteúdo;
- aplicar ou publicar alterações autorizadas.

O catálogo deve poder crescer sem crescimento proporcional do contexto enviado ao modelo.

## 7. Pesquisa e decisão

A pesquisa deve considerar amostras representativas de:

- literatura educacional;
- plataformas e sistemas;
- áreas do conhecimento e práticas disciplinares;
- currículos;
- estudantes, autores, revisores e pesquisadores;
- acessibilidade;
- instituições;
- contextos pessoais, acadêmicos, organizacionais e públicos;
- requisitos jurídicos e de governança;
- alternativas técnicas.

A pesquisa é ampla, mas finita. Toda frente deve declarar amostragem, limitações e critérios de suficiência ou saturação decisória.

O assistente deve:

- integrar a evidência;
- organizar alternativas e controvérsias;
- eliminar caminhos claramente inadequados;
- recomendar a melhor direção;
- distinguir núcleo, parâmetro, extensão, capacidade conectada, experimento, documentação, adiamento e rejeição.

Fabio não deve receber pesquisa bruta para arquitetar o produto sozinho. Sua escolha será solicitada somente quando persistir conflito estratégico, ético, pedagógico ou valorativo não resolvido pela evidência. Nesses casos, deverão ser apresentadas poucas opções compreensíveis e uma recomendação explícita.

## 8. Gate entre pesquisa e engenharia

Sequência obrigatória:

```text
pesquisa
→ organização das possibilidades
→ síntese crítica
→ alternativas e trade-offs
→ recomendação fundamentada
→ decisão estratégica
→ requisitos e modelo de domínio
→ arquitetura e stack
→ UX/UI
→ planejamento de releases
→ implementação
```

Uma possibilidade descoberta não se converte automaticamente em requisito, schema, contrato, adapter, biblioteca, protótipo ou issue de implementação.

Protótipos exploratórios são permitidos para responder a incertezas materiais. Permanecem não normativos até síntese e decisão explícitas.

## 9. Stack e arquitetura

A stack será investigada, comparada e recomendada depois dos requisitos.

Critérios obrigatórios:

- aplicação web e experiência móvel;
- tipagem forte;
- contratos e schemas;
- modularidade e fronteiras claras;
- testes;
- acessibilidade;
- offline;
- persistência local e sincronização;
- desempenho em smartphones modestos;
- carregamento seletivo de resources;
- MCP;
- implantação gerenciada e autogerenciada;
- segurança e privacidade;
- manutenção assistida por IA;
- evolução de longo prazo;
- custos e capacidade operacional.

JavaScript puro, Supabase, IndexedDB, PWA, frameworks, bancos, runtimes e modelos de extensão permanecem candidatos ou hipóteses até decisão registrada em ADR.

## 10. Infraestrutura portável

O domínio não dependerá de Supabase nem de uma solução local específica.

Contratos de infraestrutura deverão cobrir, conforme o modelo aprovado:

- repositório de cursos;
- armazenamento de artefatos;
- identidade e autorização;
- estado de estudo;
- analytics;
- sincronização;
- workspaces;
- publicação;
- backup, restauração e diagnóstico.

Uma implantação gerenciada pode usar Supabase como adapter de referência. Uma implantação autogerenciada deverá preservar os mesmos contratos funcionais, pedagógicos e analíticos relevantes.

## 11. Administração, pesquisa e analytics

O produto deverá oferecer uma superfície administrativa e de pesquisa coerente para organizar:

- cursos e estrutura curricular;
- versões e publicações;
- configurações;
- turmas e participantes;
- condições experimentais;
- capacidades e permissões;
- fontes e proveniência;
- observações, reparos e auditorias;
- eventos e analytics;
- instrumentos e exportações;
- retenção;
- implantação e operações.

Analytics serão orientados por perguntas, constructos, eventos autorizados, fórmulas, unidades de análise, retenção, acesso e inferências permitidas. Disponibilidade técnica não autoriza coleta.

## 12. UX/UI

A arquitetura não autoriza o Codex a inventar a interface.

Antes de implementação user-facing, deverão ser especificados e avaliados:

- jornadas;
- arquitetura de informação;
- telas e estados;
- transições;
- controles, botões e ícones;
- formulários;
- mensagens e erros;
- offline e sincronização;
- permissões;
- acessibilidade;
- protótipos visuais.

O formulário de parametrização deverá ser compreensível, progressivo, retomável e capaz de explicar consequências e comparar configurações.

## 13. Perfis de implantação

Perfis iniciais de investigação:

- pessoal mobile/offline;
- acadêmico ou pesquisa gerenciada;
- ensino formal e turmas;
- institucional autogerenciado;
- publicação pública ou aberta;
- conteúdo confidencial, inclusive contexto público-organizacional.

São perfis do mesmo produto e dos mesmos conceitos de domínio, embora capacidades e obrigações operacionais possam variar.

## 14. Estado do trabalho exploratório

Experimentos sobre matemática semântica, estruturas relacionais, programação executável e anotação de fontes permanecem:

- recuperáveis;
- documentados;
- não normativos;
- não bloqueadores;
- não aprovados para produção;
- não rejeitados permanentemente.

Sua retomada exige necessidade, caso concreto, classificação no produto e decisão arquitetural.

## 15. Condição para iniciar implementação

Antes do backlog de implementação, deverão existir documentos canônicos aprovados para:

- visão do produto;
- sínteses de pesquisa e decisões;
- taxonomia de parametrização;
- protocolos e analytics;
- requisitos;
- modelo de domínio;
- arquitetura e stack;
- contratos;
- UX/UI;
- plano de releases.

Issues de implementação deverão apontar para release, requisito, decisão, contrato, jornada ou tela, critérios de aceite e testes.

## 16. Próxima etapa

A etapa corrente é a Issue #4: produzir a primeira taxonomia de parametrização por pacotes de evidência e síntese, sem iniciar arquitetura ou implementação.

A taxonomia deverá entregar parâmetros candidatos e aceitos, perfis de referência e um handoff explícito para protocolos de pesquisa e modelo de domínio.