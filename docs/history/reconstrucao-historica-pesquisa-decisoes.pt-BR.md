# Reconstrução histórica canônica da pesquisa e das decisões do ARA

**Estado:** narrativa histórica canônica e interpretativa  
**Idioma:** `pt-BR`  
**Data de consolidação:** 3 de agosto de 2026  
**Função:** permitir que Fabio, avaliadores, pesquisadores e agentes de desenvolvimento compreendam a evolução do projeto sem depender de conversas privadas ou de uma leitura desordenada de todas as issues.

## 1. Regra epistemológica deste documento

Este documento **reescreve a história como uma narrativa coerente**, mas não substitui as fontes primárias.

Fontes primárias preservadas:

- brainstorming e documentos de visão fornecidos pelo autor;
- código e documentação do AraLearn;
- issues e seus históricos de edição;
- pull requests, commits e diffs;
- protocolos, registros de busca, bibliografias e datasets;
- relatórios e sínteses versionados;
- resultados de testes e limitações registradas.

Quando esta narrativa divergir de uma fonte primária sobre o que foi efetivamente executado, a fonte primária prevalece. Quando fontes históricas expressarem direções posteriormente revistas, este documento explicará o estado atual da decisão.

## 2. Antecedentes: AraLearn

AraLearn surgiu para atender necessidades concretas de estudo, inicialmente ligadas à formação em Tecnologia em Análise e Desenvolvimento de Sistemas e a outros estudos técnicos e profissionais.

O artefato consolidou:

- cursos, módulos, lições, microssequências e cards;
- separação entre teoria e prática;
- resources estruturados;
- lacunas e escolhas;
- validação determinística;
- estudo mobile-first e offline;
- autoria e reparo por ChatGPT com MCP;
- publicação explícita;
- experiência de estudo adequada ao trabalhador-estudante.

Suas decisões foram situadas. Algumas são fortes candidatas à continuidade; outras refletem preferências pessoais, limitações de implementação ou demandas específicas dos cursos produzidos.

ARA nasce para preservar a experiência funcional e investigar o que deve tornar-se parametrizável, modular, extensível ou substituível.

## 3. Primeiro brainstorming

O primeiro brainstorming formulou uma ambição mais ampla que “melhorar flashcards”. Entre as preocupações estavam:

- parametrização pedagógica;
- muitos possíveis tipos de recurso;
- ferramentas e instrumentos específicos de domínio;
- autoria seletiva por MCP;
- crescimento do catálogo sem crescimento proporcional do contexto da LLM;
- pesquisa em diferentes áreas do conhecimento;
- uso pessoal, acadêmico e institucional;
- nova stack e nova arquitetura;
- separação entre núcleo e extensões;
- planejamento completo antes da implementação.

Essa fase continha possibilidades deliberadamente abertas. Não constituía um contrato de produto.

## 4. Consolidação da visão inicial

O documento de visão inicial e memória de evolução consolidou o AraLearn como esboço funcional e primeira configuração, enfatizando:

- investigação bibliográfica e normativa;
- parâmetros declarados e comparáveis;
- arquitetura portável;
- local/offline e mobile-first;
- autoria por MCP;
- UX integral antes da implementação;
- composição de resources simples;
- extensibilidade controlada;
- pesquisa, requisitos, arquitetura, UX, contratos e releases em fases sucessivas.

A visão permaneceu ampla sobre resources, instrumentos, ambientes e capacidades. Diversas definições de domínio e arquitetura continuavam abertas.

## 5. Fundação do repositório ARA

### PR #1 — governança inicial

Estabeleceu:

- Issues como backlog canônico;
- política de idiomas;
- licenças de código e documentação;
- proibição de requisitos ocultos;
- modelos de contribuição e revisão.

A governança foi correta, mas ainda não existia uma reconstrução histórica nem uma hierarquia clara entre fontes normativas e históricas.

### Issues #2–#10 — roadmap estrutural

Foram abertas as fases principais:

- #2: propriedade intelectual e identidade;
- #3: programa bibliográfico e de evidências;
- #4: taxonomia de parametrização;
- #5: pesquisa, instrumentação e analytics;
- #6: requisitos e modelo de domínio;
- #7: arquitetura e perfis de implantação;
- #8: UX, acessibilidade e sistema visual;
- #9: releases e implementação;
- #10: roadmap e regras de execução.

Essa estrutura permanece válida em essência.

## 6. Primeira rodada do programa de evidências

### PR #11 — protocolo-mestre

Criou:

- protocolo de busca e evidência;
- inventário das unidades curriculares do METD;
- schemas de fonte e extração;
- templates de busca e triagem;
- bibliografia inicial;
- registro de pedidos de texto integral.

### PRs #12 e #13 — antecedentes e plataformas formativas

Documentaram experiências e fontes sobre:

- Anki;
- Duolingo;
- SoloLearn;
- LingoDeer;
- Encode;
- Enki;
- IFRS MOOCs;
- UNIVESP;
- Moodle e experiências negativas não identificadas.

Separaram experiência pessoal, descrição do fornecedor, evidência independente e requisito do produto.

### Issue #14 / PR #15 — revisão de revisões

Comparou sínteses sobre:

- flashcards;
- Anki;
- recuperação;
- espaçamento;
- quizzes de baixo risco;
- avaliação formativa;
- programação móvel.

Conclusão metodológica central: rótulos como “flashcard”, “quiz”, “feedback” e “spaced repetition” não descrevem condições homogêneas. A configuração efetiva deve ser explicitada.

### Issues #16, #24, #26 e #28

Construíram uma cadeia bibliográfica reproduzível:

- buscas formais PubMed e ERIC;
- 1.555 registros brutos;
- 1.471 publicações únicas após deduplicação;
- triagem de título e resumo;
- extração de 26 registros prioritários;
- identificação de 12 sínteses formais;
- mapa de sobreposição de 167 publicações primárias recuperadas.

Essa cadeia é importante para a dissertação porque preserva:

- strings;
- datas;
- contagens;
- hashes;
- critérios;
- estados de acesso;
- limitações;
- risco de dupla contagem.

### Issues #17 e #18

Produziram sínteses focadas sobre:

- formatos de resposta e feedback;
- programação móvel após 2022.

Revelaram dimensões candidatas de configuração e diferenças entre reconhecimento, produção, execução, feedback, timing, retry e avaliação.

## 7. Ampliação além de flashcards

### Issue #31 / PR #32 — auditoria canônica do AraLearn

Auditou os 18 resources do AraLearn contra código, documentação, registries, validators, renderers e testes.

Conclusões principais:

- AraLearn já é mais rico que um sistema de frente e verso;
- a riqueza representacional é maior que a riqueza das respostas;
- 13 funções representacionais foram provisoriamente preservadas;
- `flow`, `graph`, `plane`, `chart` e `system_map` exigiam revisão;
- execução, simulação e respostas construtivas não existiam como baseline;
- schemas fechados, geometria derivada, segurança e offline eram pontos fortes.

A classificação era provisória, não uma decisão de migração.

### Issues #33 e #34 / PR #35 — benchmark transdisciplinar e gêneros

Compararam 21 sistemas ou famílias, incluindo:

- Perseus;
- H5P;
- Numbas;
- STACK;
- XBlock;
- MathLive;
- JSXGraph;
- Cytoscape.js;
- Pyodide;
- Papyros;
- Blockly;
- Mermaid;
- Jupyter Widgets;
- OpenDSA;
- Mol*;
- Leaflet;
- OpenSheetMusicDisplay;
- CircuitVerse;
- Recogito;
- LanguageTool;
- PhET.

Também mapearam literatura sobre representações múltiplas, ITS, autoria, simulação, assessment, programação e respostas abertas.

Contribuições válidas:

- não reduzir ARA a flashcards;
- separar representação, atividade, resposta, validação, feedback e runtime;
- reconhecer gramáticas disciplinares;
- distinguir validade e correção;
- compreender riscos de plugins e runtimes;
- tratar gênero como hipótese, não eficácia.

Problema posterior identificado: conclusões comparativas começaram a adquirir força de requisito antes da síntese de produto.

## 8. Deriva experimental

### Issue #36 / PR #37

Criou contratos experimentais para:

- matemática semântica;
- construção relacional;
- programação executável;
- anotação de fontes e argumentação.

### Issue #38 / PR #39

Criou adapters descartáveis e testes para as quatro famílias.

### Issue #40 / PR #41

Revisou os contratos para versão `0.2`, criou migrações e auditou fronteiras com candidatos externos.

### Issue #42

Planejou um bake-off de runtime que não chegou a ser executado.

### Avaliação histórica

Esses trabalhos produziram evidência técnica válida:

- não persistir objetos de biblioteca e geometria transitória como estado portável;
- separar input de autoridade de correção;
- distinguir validação pública de validação protegida;
- não tratar Worker ou `vm` como sandbox de produção;
- tornar indisponibilidade de capacidades explícita;
- evitar código arbitrário fornecido pelo curso.

Contudo, a sequência antecipou contratos e protótipos antes de uma síntese decisória sobre o produto e o recorte. A cadeia foi encerrada para evitar que cada possibilidade técnica gerasse automaticamente nova engenharia.

Os artefatos permanecem não normativos, recuperáveis e potencialmente úteis.

## 9. Correção da rota

A correção passou por três movimentos:

1. restaurar ARA como sucessor direto do AraLearn;
2. impedir que AraLearn limitasse o espaço de possibilidades;
3. inserir síntese, recomendação e decisão entre pesquisa e engenharia.

As Issues #10, #30, #4, #6 e #7 foram ajustadas para:

- pesquisa ampla, representativa e finita;
- AraLearn como primeira referência, não limite;
- parâmetros ausentes no AraLearn;
- maturidade de candidatos;
- autoridade normativa da #6;
- arquitetura e stack decididas na #7;
- distinção entre requisito durável, primeiro recorte, perfil e hipótese técnica;
- protótipos subordinados a perguntas de decisão.

## 10. Issue #30 / PR #43 — síntese integrada

A Issue #30 revisada analisou dois eixos com igual importância:

- configuração funcional do AraLearn;
- horizonte externo de possibilidades.

A síntese recomendou:

- preservar AraLearn como primeiro perfil;
- descobrir parâmetros em literatura, plataformas, domínios, stakeholders e instituições;
- manter descoberta ampla e normatização seletiva;
- separar configurações, representações, práticas, instrumentos e capacidades;
- usar extensibilidade governada;
- não promover automaticamente os contratos experimentais.

Foram produzidos:

- relatório integrado;
- mapa do perfil AraLearn;
- mapa de oportunidades externas;
- registro de amostragem e saturação;
- síntese decisória em JSON;
- índice de pesquisa atualizado.

## 11. Estado atual da decisão

### Canônico e vigente

- ARA é sucessor direto do AraLearn;
- preserva experiência essencial, estrutura de estudo, mobile/offline e MCP;
- investiga configurações ausentes do predecessor;
- utiliza parametrização explícita e versionada;
- pretende kernel pequeno e extensibilidade governada;
- separa resources, práticas, respostas, validators, instrumentos e capacidades no nível analítico;
- domínio permanece independente de Supabase;
- stack será escolhida por investigação;
- UX antecede implementação;
- analytics depende de pergunta, autorização e governança;
- decisões fundamentais exigem síntese e recomendação.

### Ainda em pesquisa ou decisão futura

- taxonomia inicial de parâmetros;
- modelo de protocolos, eventos e analytics;
- entidades normativas do domínio;
- limites exatos do kernel;
- contrato comum de resources e capacidades;
- stack;
- persistência e sincronização;
- adapters de infraestrutura;
- arquitetura MCP detalhada;
- UX/UI;
- primeiro recorte e releases.

### Histórico não normativo

- classificação dos resources como `legacy-seed`;
- contratos de componentes `0.1` e `0.2`;
- adapters das quatro famílias;
- candidatos MathLive, Cytoscape.js, Recogito e Pyodide;
- decisões provisórias de retain/split/replace dos protótipos.

## 12. Próxima etapa

A próxima etapa é a Issue #4: taxonomia de parametrização.

Ela deverá ser executada por pacotes coerentes de evidência e síntese, começando pelas dimensões transversais necessárias para descrever condições educacionais:

1. prática, resposta, tentativas, revelação, feedback e consequências;
2. progressão, sequenciamento, revisão, espaçamento, exemplos e scaffolding;
3. autonomia, adaptação, acessibilidade e assistência por IA;
4. instrumentação, condições de pesquisa, analytics e governança;
5. autoria, publicação e políticas de configuração.

Nenhum pacote deve transferir pesquisa bruta para Fabio. Cada um deverá produzir conclusão, recomendação, alternativas, riscos e incertezas decisivas.

## 13. Relação com mestrado e doutorado

A documentação produzida tem três funções distintas:

- **engenharia:** rastrear requisitos, decisões, arquitetura, UX, releases e código;
- **mestrado:** fornecer corpus para justificar o artefato, a revisão, as decisões de design, o método de desenvolvimento e a avaliação;
- **doutorado futuro em Sistemas de Informação:** preservar questões de arquitetura, extensibilidade, autoria por agentes, portabilidade, governança, adoção institucional e evolução do sistema.

Nenhum documento atual constitui, por si só, dissertação ou tese. Ele preserva material verificável e rastreável para formulação acadêmica posterior.

## 14. Mapa resumido de marcos

| Marco | Issue(s) | PR(s) | Estado atual |
|---|---:|---:|---|
| Governança inicial | #10 e regras do repositório | #1 | vigente, complementada por documentos canônicos |
| Protocolo de evidência | #3 | #11–#13 | programa contínuo |
| Revisão de revisões | #14 | #15 | evidência concluída |
| Buscas formais | #16 | #21–#23 | rodada concluída |
| Resposta e feedback | #17 | #19 | síntese inicial concluída |
| Programação móvel | #18 | #20 | síntese provisória concluída |
| Triagem e extração | #24, #26, #28 | #25, #27, #29 | rodada concluída |
| Auditoria AraLearn | #31 | #32 | baseline concluído |
| Benchmark externo | #33, #34 | #35 | evidência comparativa concluída |
| Contratos experimentais | #36, #38, #40 | #37, #39, #41 | histórico não normativo |
| Bake-off de runtime | #42 | — | adiado, não executado |
| Síntese integrada | #30 | #43 | concluída e vigente como recomendação |
| Parametrização | #4 | — | próxima etapa |
| Pesquisa e analytics | #5 | — | futura, depende de #4 |
| Produto e domínio | #6 | — | futura, depende de #4 e #5 |
| Arquitetura e stack | #7 | — | futura, depende de #6 |
| UX/UI | #8 | — | futura, depende do produto e arquitetura |
| Releases | #9 | — | futura, após UX e arquitetura |

## 15. Como atualizar esta história

Esta narrativa será atualizada apenas quando houver:

- síntese decisória relevante;
- mudança de fase;
- decisão normativa;
- revisão fundamental por inviabilidade, contradição ou risco;
- avaliação empírica que altere o entendimento do artefato.

Não deverá ser reescrita a cada commit ou issue operacional. Detalhes permanecem nas fontes primárias e no índice do backlog.