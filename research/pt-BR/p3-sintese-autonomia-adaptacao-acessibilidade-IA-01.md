# Síntese P3 — autonomia, autorregulação, adaptação, acessibilidade e assistência por IA

**Issue governante:** #4  
**Pacote:** P3  
**Data:** 3 de agosto de 2026  
**Estado:** concluído para a primeira taxonomia; pendente da síntese final de P1–P5.

## 1. Conclusão principal

O ARA deve representar autonomia, apoio à autorregulação, adaptação, acessibilidade e assistência por IA como famílias distintas e combináveis.

Não são equivalentes:

- autonomia e ausência de estrutura;
- learner control e controle irrestrito;
- preferência e evidência de aprendizagem;
- adaptação e acomodação;
- recomendação e aplicação;
- explicação e correção;
- revisão humana e garantia de qualidade;
- saída fluente e conteúdo validado;
- auditoria por outra IA e evidência independente;
- acessibilidade e personalização opcional.

A direção recomendada é **shared control com autoridade explícita**:

```text
leis, direitos e acessibilidade
→ consentimento e direitos do participante
→ protocolo de pesquisa aprovado
→ política institucional
→ autor, revisor ou tutor
→ escolha do estudante dentro do espaço permitido
→ regra determinística validada
→ recomendação de IA
→ disponibilidade técnica
```

A IA permanece assistente. Ela pode planejar, sugerir, redigir, comparar, criticar, auditar e reparar, mas não se torna professora automática, editora final, publicadora ou avaliadora consequencial por padrão.

## 2. Autonomia apoiada

A literatura de aprendizagem autorregulada descreve processos de planejamento, execução, monitoramento, controle e reflexão, com componentes cognitivos, metacognitivos, motivacionais, comportamentais e afetivos. Isso não justifica um campo único `selfRegulation` nem uma inferência automática de que o estudante possui ou não autorregulação.

A primeira taxonomia separa:

- objetivo;
- planejamento;
- monitoramento;
- reflexão;
- apoio a estratégias;
- busca de ajuda;
- autoavaliação.

Esses elementos são suportes ou condições. A ausência de uma nota, meta declarada, comentário ou planejamento no sistema não deve ser interpretada como déficit do estudante.

A evidência sobre learner control é heterogênea. A meta-análise de Karich, Burns e Maki encontrou efeito acadêmico geral próximo de zero, o que desaconselha liberdade total como regra universal. Estudos de autonomia apoiada e shared control mostram uma direção mais defensável: a estrutura mantém coerência, dependências e limites; o estudante controla ritmo e escolhas relevantes.

No ARA, portanto, devem permanecer separados:

- escopo do controle;
- forma de escolha;
- política de recomendação;
- bloqueio, override e contestação.

## 3. Adaptação não é um mecanismo único

A literatura sobre intelligent tutoring systems e adaptive learning mostra efeitos potencialmente positivos, mas dependentes do comparador, domínio, população, duração, desenho e mecanismo. “Adaptativo” não é uma intervenção homogênea.

A primeira taxonomia aceita dimensões para:

- modo de adaptação;
- alvo;
- gatilho;
- base de evidência;
- autoridade;
- modo de aplicação;
- transparência;
- override;
- rollback;
- snapshot;
- fallback.

Uma adaptação somente é inteligível quando o sistema consegue responder:

1. o que mudou;
2. por que mudou;
3. com base em qual evidência;
4. quem propôs;
5. quem aprovou;
6. quando entrou em vigor;
7. como desfazer;
8. qual estado efetivo foi usado;
9. o que ocorre sem rede, modelo ou capacidade.

Para recomendações produzidas por IA, o padrão recomendado é:

```text
preview-only
ou
recommend-and-confirm
```

Aplicação automática permanece adiada, salvo regras determinísticas, validadas, reversíveis e explicitamente autorizadas.

Não se deve inferir dificuldade, esforço, expertise, motivação ou struggle de tempo, tentativas, pausas, interrupções, comentários ou pedidos de ajuda sem constructo, método e autorização definidos em P4 e na Issue #5.

## 4. Acessibilidade como precedência

Acessibilidade não deve ser um preset que pode ser desligado. O ARA precisa combinar:

- baseline acessível;
- opções inspiradas por UDL;
- preferências controladas pelo usuário;
- acomodações protegidas;
- compatibilidade com tecnologias assistivas;
- revisão de equivalência e preservação do constructo;
- persistência mínima;
- privacidade.

WCAG 2.2 fornece critérios técnicos verificáveis para interfaces perceptíveis, operáveis, compreensíveis e robustas. As UDL Guidelines 3.0 ampliam a análise para barreiras, agência, representação e ação/expressão. Nenhum desses referenciais, isoladamente, demonstra efetividade pedagógica de uma configuração específica.

A taxonomia separa:

- desenho inclusivo geral;
- escopo da acomodação;
- necessidade de declaração;
- controle de preferências;
- modalidades;
- equivalência;
- preservação do constructo;
- tecnologias assistivas;
- persistência;
- privacidade.

A direção recomendada é permitir opções úteis sem exigir diagnóstico. Quando uma instituição precisa verificar uma acomodação, a justificativa sensível deve permanecer separada da configuração aplicada.

Uma alternativa de resposta ou apresentação não deve ser declarada equivalente automaticamente. Ela pode ser:

- equivalente;
- funcionalmente equivalente;
- qualificada quanto ao constructo;
- evidência alternativa;
- não comparável.

## 5. IA para aprendizagem: potencial e risco

A evidência atual contém resultados positivos e negativos.

Ensaios recentes com tutores desenhados para contextos específicos encontraram ganhos relevantes. Esses resultados apoiam a pesquisa de funções delimitadas de tutoria, não uma autorização para um tutor universal autônomo.

Em sentido contrário, o experimento de Bastani e colaboradores mostrou que uma interface generativa sem guardrails pode melhorar o desempenho durante a prática e prejudicar o desempenho posterior sem assistência. A implicação não é rejeitar IA, mas preservar a operação cognitiva que o estudante deveria executar.

Assim, o perfil de estudo assistido por IA deve favorecer funções sob demanda, como:

- pista;
- explicação;
- pergunta;
- crítica;
- comparação;
- solicitação de autoexplicação;
- planejamento;
- resumo contextual.

Não deve assumir resposta pronta como default. Dependendo do objetivo, o sistema pode solicitar previsão, tentativa, justificativa ou reflexão antes de revelar a assistência.

Disclaimers podem ajudar, mas não resolvem overreliance sozinhos. Explicações e confiança aparente também não garantem confiança calibrada. Estudos de cognitive forcing sugerem que revisão ativa pode reduzir aceitação automática, mas cria custo e não deve virar fricção universal.

## 6. IA para autoria: GPT+MCP e ARA

A visão de produto foi refinada para dois canais complementares de intervenção.

### 6.1 Chat com GPT+MCP

O chat serve para operações semânticas e de alto nível:

- formular objetivos;
- escolher ou discutir parâmetros;
- planejar partes;
- construir microssequências;
- recuperar contexto autorizado;
- comparar unidades e cursos;
- solicitar auditoria;
- solicitar reparo;
- discutir decisões e trade-offs.

O GPT deve receber contexto limitado ao alvo, às dependências, aos contratos e às fontes necessários. Acesso entre cursos ou workspaces exige autorização explícita e provenance.

### 6.2 ARA como superfície operacional

O ARA serve para o usuário acompanhar os artefatos em construção e realizar ações determinísticas:

- visualizar em tempo real o que foi materializado;
- navegar por curso, parte, microssequência, card e resource;
- selecionar versões;
- comparar diffs;
- mover ou reorganizar unidades quando autorizado;
- comentar card, microssequência, dependência ou conjunto;
- registrar erro, dúvida, inadequação contextual ou solicitação;
- aceitar, rejeitar ou aplicar parcialmente mudanças;
- solicitar reparo pelo GPT;
- acompanhar auditoria e reauditoria;
- aprovar e publicar explicitamente.

O usuário não deve precisar compreender banco de dados, Storage, IndexedDB, chaves ou sincronização para executar essas operações.

### 6.3 Intermediação de estado

Persistência e sincronização intermedeiam:

```text
GPT/MCP grava ou propõe artefatos
↔ ARA renderiza e permite operações determinísticas
↔ usuário grava decisões e observações
↔ GPT/MCP recupera o estado autorizado e repara
```

A escolha entre banco, Storage, artefatos imutáveis, IndexedDB e outros mecanismos pertence às Issues #6 e #7.

## 7. Ciclo de autoridade da saída de IA

Toda saída de IA começa em estado não normativo:

```text
suggestion
→ draft
→ validated-structure
→ audited
→ human-approved
→ published
```

Também pode tornar-se:

```text
rejected
ou
superseded
```

A IA não promove a própria saída. Validação por schema ou testes determinísticos não estabelece qualidade pedagógica. Auditoria por outra chamada de modelo não substitui revisão humana ou especialista quando a decisão é consequencial, normativa ou sensível.

O fluxo construtor → auditor → reparo/re-auditoria foi preservado como perfil de autoria, com publicação humana explícita.

## 8. Controle e contestação

A pesquisa em interação humano–IA mostra dois riscos complementares:

- automação e overreliance quando a saída é fácil de aceitar;
- aversão ou abandono quando a pessoa não pode modificar um sistema imperfeito.

Por isso, a primeira taxonomia aceita:

- editabilidade;
- aplicação parcial;
- comentários situados;
- solicitação de explicação;
- contraprova;
- revisão humana;
- escalonamento;
- restauração de versão;
- rollback;
- provenance.

“Human-in-the-loop” não é garantia suficiente: pessoas podem concordar com recomendações erradas ou discriminatórias. O produto precisa de estado visível, orientação, papéis claros e validação sistêmica.

## 9. Perfis e overrides esparsos

Foram registrados nove perfis:

- `aralearn-reference`;
- `self-directed-reflective`;
- `teacher-guided-shared-control`;
- `research-locked-condition`;
- `accessibility-first-overlay`;
- `AI-assisted-authoring`;
- `AI-assisted-study`;
- `deterministic-offline`;
- `institutional-governed-AI`.

A direção de produto é usar:

```text
catálogo versionado
→ perfil nomeado
→ overrides esparsos por escopo
→ resolução determinística da configuração efetiva
```

Assim, o GPT e o usuário não precisam declarar todos os parâmetros em cada JSON. O formulário deverá apresentar linguagem pedagógica e administrativa, explicar consequências e ocultar detalhes de persistência na experiência comum.

## 10. Composição por microssequências e parametrização transformadora

As reflexões registradas após P2 foram preservadas como hipótese concreta:

- microssequências potencialmente versionadas de forma independente;
- curso como composição versionada de posições;
- materialização local autossuficiente para uso offline;
- comentários, auditoria e reparo em granularidade de card, microssequência, conjunto ou composição;
- retomada de microssequências em partes diferentes e entre cursos;
- variantes de curso sob parametrizações diferentes;
- dependências explícitas e referenciadas;
- GPT usando blocos anteriores ou outros cursos como contexto autorizado.

P3 não aceita essa arquitetura. Apenas determina requisitos de autoridade, transparência, contexto, provenance, editabilidade, contestação e fallback que qualquer solução futura deverá satisfazer.

A síntese final da Issue #4 deverá classificar parâmetros pelo nível de incidência:

- runtime/configuração efetiva;
- conteúdo ou materialização;
- composição e dependências;
- lifecycle e governança;
- condição experimental.

## 11. Analytics e dados

P3 não define eventos ou métricas. Preserva, porém, regras para P4:

- monitoramento pessoal é diferente de analytics de pesquisa ou instituição;
- assistência de IA não autoriza coleta;
- comentário pode conter informação sensível;
- uso de ajuda não é déficit;
- aceitação de recomendação não é domínio;
- atraso, tempo e interrupção não são motivação;
- configuração aplicada deve poder ser reconstruída;
- modelo, contexto, perfil, diff e cadeia de revisão podem ser necessários à reproducibilidade;
- conversa completa não deve ser retida por padrão.

## 12. Aceitos, adiados e rejeitados

P3 aceita 50 dimensões paramétricas distribuídas por autonomia, autorregulação, adaptação, acessibilidade e IA.

Foram adiados:

- learner model;
- inferência automática de struggle ou expertise;
- adaptação integralmente autônoma;
- personalização generativa em runtime;
- avaliação autoritativa de respostas abertas;
- inferência de emoção ou neurotipo;
- geração automática de acomodações;
- fine-tuning com conteúdo ou comportamento do usuário;
- reutilização e reparo cross-course automáticos.

Foram rejeitados como defaults:

- controle irrestrito;
- adaptação invisível;
- acessibilidade opcional;
- declaração pública obrigatória de deficiência;
- IA como autoridade final;
- aceite tudo-ou-nada;
- contexto MCP ilimitado;
- retenção integral de chat;
- substituição silenciosa de provedor;
- dependência de IA no estudo baseline;
- fornecimento automático da resposta;
- coleta por conveniência.

## 13. Limitações e incertezas

As principais incertezas são:

- efeitos para adultos trabalhadores em estudo fragmentado;
- quantidade produtiva de controle por domínio e expertise;
- evidência válida para gatilhos adaptativos;
- compreensão de perfis e overrides por usuários não técnicos;
- custo e acessibilidade de avisos e cognitive forcing;
- transferência de tutores generativos para outros domínios;
- desempenho sem assistência e transferência tardia;
- equivalência de variantes de curso;
- privacidade de acomodações;
- modelos locais e conectados;
- mudança de provedor/modelo;
- impacto da composição por microssequências;
- contextos brasileiros, portugueses e não WEIRD.

## 14. Handoff

### Para P4 e Issue #5

- eventos e medidas autorizados;
- snapshots e condições;
- comportamento de IA;
- constructos e inferências proibidas;
- consentimento, retenção e comparabilidade.

### Para P5

- autoria humano–IA;
- contexto e grounding;
- revisão e auditoria;
- comentários e reparo;
- provenance;
- publicação;
- reutilização entre cursos;
- políticas institucionais.

### Para Issue #6

- atores e autoridades;
- estados da saída de IA;
- perfis e configuração efetiva;
- composição e versões;
- observações situadas;
- aprovação/publicação;
- acessibilidade e dados sensíveis.

### Para Issue #7

- fronteiras de dados;
- provedores;
- offline e fallback;
- snapshots;
- rastreabilidade;
- materialização e sincronização;
- segurança e isolamento.

### Para Issue #8

- formulários em linguagem comum;
- progressive disclosure;
- preview e diff;
- estados de IA;
- contestação e rollback;
- dois canais de intervenção;
- administração por professores, tutores, pesquisadores e autodidatas.

## 15. Não autorizações

P3 não autoriza modelo adaptativo, LLM, provedor, MCP, schema, banco, Storage, IndexedDB, interface, dashboard, coleta de dados, inferência de estudante, runtime generativo, avaliação por IA, código ou migração.
