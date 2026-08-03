# Visão canônica atual do produto ARA

**Estado:** canônico para a fase de pesquisa e definição do produto  
**Idioma de trabalho:** `pt-BR`  
**Última consolidação:** 3 de agosto de 2026  
**Autoridade:** consolida a visão inicial, a memória do sucessor do AraLearn, as clarificações estratégicas do proprietário, a síntese integrada da Issue #30 e os Pacotes P1–P3 da Issue #4. Não substitui as fontes históricas; governa sua interpretação atual.

## 1. Definição do produto

ARA — Ambiente de Recursos de Aprendizagem / Learning Resources Environment — será o sucessor direto do AraLearn.

O produto preservará a experiência funcional que demonstrou valor no AraLearn, mas será reconstruído para oferecer:

- autoria, revisão, auditoria e reparo de cursos assistidos por GPT com MCP;
- visualização e intervenção direta do usuário durante a construção;
- parametrização pedagógica, operacional e experimental;
- pesquisa acadêmica reproduzível;
- estudo mobile-first e offline;
- resources estruturados e validação determinística onde adequada;
- versionamento, provenance e publicação explícita;
- extensibilidade governada;
- infraestrutura portável;
- adoção pessoal, acadêmica e institucional.

ARA não é apenas o AraLearn com mais opções. Também não é uma plataforma universal que implementará antecipadamente toda possibilidade educacional.

A direção vigente é:

```text
experiência funcional do AraLearn
+ pesquisa ampla, representativa e finita
+ parametrização explícita e versionada
+ autoria GPT+MCP com controle humano visível no ARA
+ kernel pequeno e capacidades separadas
+ infraestrutura por contratos e adapters
+ pesquisa → decisão → requisitos → arquitetura → UX → implementação
```

## 2. Continuidade com o AraLearn

### 2.1 Preservar como referência

- estrutura inicial `curso → módulo → lição → microssequência → card`;
- separação entre teoria e prática;
- progressão estrutural separada de acerto ou mastery;
- retomada rápida e estado de estudo não punitivo;
- estudo mobile-first e offline;
- resources estruturados;
- validação determinística onde metodologicamente adequada;
- autoria, auditoria e reparo por GPT com MCP;
- comentários e observações situados;
- publicação e aplicação explícitas;
- curadoria e autoridade humanas;
- aprendizagem acumulada dos defeitos e correções reais do AraLearn.

### 2.2 Não herdar automaticamente

- stack atual;
- JavaScript puro;
- organização interna do código;
- contrato monolítico `aralearn.resources.v4`;
- acoplamento com Supabase;
- frontend atual;
- limitações históricas de resposta e prática;
- preferências pessoais transformadas em regras universais;
- decisões provisórias dos experimentos de componentes.

AraLearn é a primeira configuração funcional de referência e uma fonte central de evidência. Não é o limite do espaço de possibilidades nem uma arquitetura obrigatória.

## 3. Transformação central: parametrização

ARA deve tornar explícitas, versionadas e pesquisáveis decisões que podem variar entre cursos, usuários, condições experimentais, protocolos, implantações e políticas institucionais.

P1–P3 demonstraram que parâmetros não devem ser agregados em modos monolíticos. A primeira taxonomia já separa, entre outras dimensões:

- prática, resposta, tentativas, reveal, feedback e consequência;
- progressão, evidência de mastery, sequência, ritmo, revisão e espaçamento;
- exemplos resolvidos, scaffolding, segmentação e retomada;
- autonomia, autorregulação e busca de ajuda;
- adaptação, transparência, override, rollback e fallback;
- acessibilidade, acomodação, equivalência e privacidade;
- funções, contexto, autoridade, validação, provenance e falha da IA.

### 3.1 Níveis de incidência

A síntese final da Issue #4 deverá classificar cada parâmetro também pelo que ele altera:

1. **runtime ou configuração efetiva** — modifica comportamento de estudo ou renderização sem reescrever o conteúdo;
2. **conteúdo ou materialização** — altera distribuição, concentração, granularidade, exemplos ou composição do artefato;
3. **estrutura e referências** — altera ordem, dependências, posições, relações entre unidades ou cursos;
4. **ciclo de vida e governança** — altera versões, visibilidade, compartilhamento, retirada, provenance ou retenção;
5. **condição experimental** — bloqueia invariantes e variações necessárias para comparação.

Um parâmetro que transforma conteúdo não é um simples switch de interface e pode produzir novas revisões ou uma nova composição de curso.

### 3.2 Perfis e overrides esparsos

O catálogo completo não deve ser repetido em cada JSON nem enviado integralmente ao GPT.

Direção candidata:

```text
catálogo versionado de parâmetros
→ perfil ou preset nomeado
→ overrides esparsos por escopo
→ resolução determinística da configuração efetiva
→ snapshot ou artefato materializado
```

O usuário escolhe em linguagem pedagógica e administrativa. O GPT declara somente perfis, diferenças e justificativas relevantes. A plataforma calcula, valida e torna inspecionável a configuração efetiva.

Cada parâmetro deverá registrar definição, evidência, relação com o perfil AraLearn, valores, escopo, autoridade, precedência, overrides, conflitos, implicações e maturidade.

A descoberta será ampla. A normatização será seletiva.

## 4. Modelo operacional: dois canais complementares

O usuário interage com o processo de autoria por dois canais que operam sobre o mesmo estado autorizado.

### 4.1 Chat com GPT e MCP

O chat serve a operações semânticas e de alto nível:

- formular objetivo, público e escopo;
- escolher ou discutir parâmetros;
- planejar partes do curso;
- construir microssequências e cards;
- recuperar contexto autorizado de unidades anteriores ou outros cursos;
- comparar versões ou variantes;
- solicitar auditoria;
- solicitar reparo localizado;
- discutir decisões e trade-offs.

O GPT deve consultar por MCP apenas os metadados, contratos, artefatos, dependências, comentários e fontes necessários à operação corrente.

### 4.2 ARA como superfície de visualização e controle

O ARA não será apenas o player final de cursos publicados. Ele será a superfície operacional na qual o usuário acompanha o que está sendo construído e intervém deterministicamente.

Operações candidatas incluem:

- visualizar em tempo real artefatos materializados;
- navegar por curso, parte, microssequência, card e resource;
- selecionar e comparar versões;
- inspecionar diffs, configuração e provenance;
- mover ou reorganizar unidades quando permitido;
- comentar card, microssequência, dependência ou conjunto;
- classificar observação como erro, dúvida, inadequação contextual ou solicitação;
- aceitar, rejeitar ou aplicar parcialmente mudanças;
- solicitar reparo pelo GPT;
- acompanhar auditoria e reauditoria;
- aprovar e publicar explicitamente.

O usuário comum não deverá administrar tabelas, objetos de Storage, chaves, stores do IndexedDB ou protocolos de sincronização.

### 4.3 Ciclo compartilhado de estado

```text
GPT/MCP planeja, grava ou propõe artefatos
↔ ARA renderiza e oferece operações determinísticas
↔ usuário registra decisões, comentários e observações
↔ GPT/MCP recupera o estado autorizado e executa auditoria ou reparo
```

Banco, Storage, artefatos e persistência local funcionarão como intermediários técnicos conforme os contratos aprovados nas Issues #6 e #7. Esta visão não seleciona a tecnologia.

## 5. Hipótese de composição por microssequências

A reflexão do proprietário definiu uma hipótese concreta que deve ser investigada antes das decisões de domínio e arquitetura:

```text
microssequências versionadas independentemente
→ manifesto ou composição versionada de curso
→ posições que referenciam revisões
→ materialização local autossuficiente para estudo offline
→ estado e observações vinculados ao contexto da ocorrência
```

A microssequência é a principal candidata à unidade granular de criação, versionamento, comentário, auditoria, reparo e reutilização. Ainda não está aprovada como átomo universal.

O curso continuaria sendo um objeto pedagógico completo por sua composição, objetivos, ordem, dependências, parâmetros e publicação, ainda que não possua cópia exclusiva de cada unidade.

A pesquisa deverá comparar:

- propriedade integral pelo curso;
- referência a unidades imutáveis;
- fork e copy-on-write;
- deduplicação sem reutilização pedagógica;
- snapshots offline;
- versionamento e impacto de alterações;
- exclusão, retirada de compartilhamento e confidencialidade;
- progressão contextualizada por curso, versão, posição e card.

Reutilização de conteúdo não transfere automaticamente conclusão, mastery ou estado de revisão.

## 6. Kernel e categorias do produto

ARA deve possuir um kernel pequeno, coeso, versionado e de evolução controlada.

Responsabilidades transversais candidatas:

- carregar e validar artefatos;
- resolver versões, perfis e capacidades;
- executar o ciclo de cards;
- despachar resources, práticas e capacidades;
- resolver configuração efetiva;
- controlar estado, progressão, feedback e retomada;
- persistir e operar offline;
- registrar somente eventos autorizados;
- integrar contratos de infraestrutura;
- tratar capacidades ausentes explicitamente.

O kernel não deverá conter semântica específica de matemática, química, linguística, programação, grafos, mapas ou outro domínio.

Um `resource` representa conteúdo declarativo. Não deve absorver silenciosamente prática, resposta, validator, runtime, instrumento de pesquisa, integração com IA ou serviço externo.

A divisão normativa entre curso, microssequência, card, resource, prática, resposta, validator, feedback, perfil, snapshot, protocolo e evidência pertence às Issues #6 e #7.

## 7. Autoria assistida por IA

O catálogo de capacidades deve crescer sem crescimento proporcional do contexto da LLM.

Fluxo candidato:

1. planejar objetivo, conteúdo, parâmetros e dependências;
2. consultar metadados e contratos necessários por MCP;
3. buscar unidades ou contexto autorizados;
4. construir uma parte ou microssequência;
5. validar estrutura e referências;
6. renderizar no ARA;
7. auditar de forma independente;
8. receber comentários do usuário;
9. reparar localmente e reauditar;
10. aprovar e publicar explicitamente;
11. prosseguir para a parte seguinte.

O padrão human-in-the-loop é:

```text
planejador/construtor
→ auditor independente
→ reparo e reauditoria
→ revisão/aprovação humana
→ publicação
```

### 7.1 Estado da saída de IA

Toda saída começa sem autoridade normativa:

```text
suggestion
→ draft
→ validated-structure
→ audited
→ human-approved
→ published
```

Também pode ser `rejected` ou `superseded`.

A IA não promove a própria saída. Validação determinística não prova qualidade pedagógica. Auditoria por outra IA não substitui revisão humana ou especialista quando o risco ou consequência exigir.

### 7.2 Autoridade, contexto e falha

A IA deverá operar com:

- função delimitada;
- iniciação explícita;
- contexto mínimo e inspecionável;
- grounding e fontes;
- status visível;
- validação apropriada;
- editabilidade e aplicação parcial;
- contestação e rollback;
- provenance;
- fronteiras de dados;
- retenção mínima;
- política de provedor;
- fallback offline;
- falha explícita.

O estudo baseline e as operações determinísticas essenciais não dependerão de uma LLM conectada.

## 8. Autonomia, adaptação e acessibilidade

ARA adotará shared control, não liberdade total nem adaptação oculta.

- autores e protocolos definem estrutura, dependências e limites;
- estudantes controlam ritmo e escolhas permitidas;
- recomendações não se aplicam automaticamente;
- adaptações devem declarar alvo, gatilho, evidência, autoridade e estado efetivo;
- mudanças relevantes devem ser transparentes, contestáveis e reversíveis;
- acessibilidade e direitos têm precedência sobre preferências ordinárias;
- opções acessíveis devem ser oferecidas sem exigir diagnóstico sempre que possível;
- equivalência e preservação de constructo precisam ser registradas;
- dados de acessibilidade permanecem minimizados e protegidos.

Não se deve inferir motivação, esforço, expertise, deficiência, struggle ou engagement de tempo, tentativas, pausas, comentários ou uso de ajuda sem modelo metodológico e autorização.

## 9. Pesquisa e decisão

A pesquisa considerará literatura, plataformas, áreas do conhecimento, currículos, usuários, acessibilidade, instituições, requisitos jurídicos e alternativas técnicas.

Toda frente deverá declarar amostragem, limitações e suficiência decisória.

O assistente deverá integrar evidência, comparar alternativas e recomendar uma direção. O proprietário receberá decisões compreensíveis, não um corpus bruto para arquitetar sozinho.

Sequência obrigatória:

```text
pesquisa
→ síntese crítica
→ alternativas e trade-offs
→ recomendação
→ decisão estratégica
→ requisitos e domínio
→ arquitetura e stack
→ UX/UI
→ releases
→ implementação
```

Uma possibilidade descoberta não se converte automaticamente em requisito, schema, adapter, biblioteca, protótipo ou código.

## 10. Arquitetura e infraestrutura

A stack será investigada depois dos requisitos.

Critérios obrigatórios:

- web e experiência móvel;
- tipagem, contratos e schemas;
- modularidade;
- acessibilidade;
- offline e sincronização;
- desempenho em smartphones modestos;
- MCP e carregamento seletivo;
- implantação gerenciada e autogerenciada;
- segurança, privacidade e provenance;
- observabilidade, backup, restauração e rollback;
- custo, manutenção e exit strategy.

Supabase, IndexedDB, PWA, bancos, Storage, grafos, content addressing, runtimes e provedores de IA permanecem hipóteses até ADR.

O domínio não dependerá de Supabase. Implantações gerenciadas e autogerenciadas deverão preservar os mesmos contratos funcionais, pedagógicos e analíticos relevantes.

## 11. Administração, analytics e UX

O produto deverá oferecer superfícies compreensíveis para estudantes, professores, tutores, autores, pesquisadores e instituições.

A experiência comum deverá usar linguagem pedagógica e administrativa, com:

- entrada por contexto e papel;
- perfis recomendados;
- progressive disclosure;
- resumo das consequências;
- preview de fluxo e configuração;
- comparação entre versões e condições;
- alertas de conflitos e capacidades ausentes;
- mudanças reversíveis;
- publicação confirmada;
- analytics orientados a perguntas;
- detalhes técnicos e auditáveis em camada avançada.

Analytics serão definidos por pergunta, constructo, evento autorizado, fórmula, unidade de análise, retenção, acesso e inferência permitida. Disponibilidade técnica não autoriza coleta.

Antes de implementação user-facing, a Issue #8 deverá especificar e avaliar jornadas, telas, estados, transições, formulários, mensagens, offline, permissões, acessibilidade e protótipos.

## 12. Perfis de implantação

Perfis iniciais de investigação:

- pessoal mobile/offline;
- acadêmico ou pesquisa gerenciada;
- ensino formal e turmas;
- institucional autogerenciado;
- publicação pública ou aberta;
- conteúdo confidencial.

São configurações do mesmo produto e domínio, embora capacidades e obrigações operacionais possam variar.

## 13. Condição para implementação

Antes do backlog de implementação, deverão existir documentos aprovados para:

- visão do produto;
- sínteses de pesquisa;
- taxonomia de parametrização;
- protocolos e analytics;
- requisitos e domínio;
- arquitetura, stack e ADRs;
- contratos;
- UX/UI;
- plano de releases.

Issues de implementação deverão apontar para release, requisito, decisão, contrato, jornada ou tela, critérios de aceite e testes.

## 14. Próxima etapa

P1, P2 e P3 da Issue #4 estão concluídos. A próxima etapa é o Pacote P4: instrumentação, condições experimentais, analytics e governança.

P4 deverá receber os estados, snapshots, parâmetros, perfis, funções de IA, limites de inferência e hipóteses de variantes/composição definidos até aqui, sem iniciar arquitetura ou implementação.
