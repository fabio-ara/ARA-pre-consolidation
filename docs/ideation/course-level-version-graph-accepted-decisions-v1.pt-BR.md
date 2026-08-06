# Decisões aceitas — versionamento por curso, derivações e proveniência operacional

**Estado:** decisões aceitas pelo proprietário para orientar a continuação da idealização  
**Data:** 5 de agosto de 2026  
**Relação:** complementa `operational-provenance-retention-v1.pt-BR.md` e refina as áreas Q, R e S do pré-backlog sem alterar sua contagem.  
**Issues relacionadas:** #77, #79 e #81

## 1. Decisão principal

Cada alteração efetivamente aplicada ao curso persistido produz uma nova revisão imutável do curso.

A revisão é uma materialização lógica completa do curso, ainda que reutilize fisicamente revisões inalteradas de módulos, lições, microssequências, cards e resources por meio de manifests e referências.

```text
revisão anterior do curso
+ operação autoral confirmada
→ nova revisão do curso
```

Planejamento, auditoria, findings, observações, comentários, discussão e propostas ainda não executadas permanecem ligados à revisão examinada, mas não criam por si só uma nova revisão do curso.

## 2. Continuidade com o fluxo do AraLearn

O ARA deve preservar e tornar persistente o fluxo já demonstrado no AraLearn:

```text
planejamento
→ aprovação humana
→ construção de uma parte
→ materialização de nova revisão
→ auditoria
→ proposta de reparos
→ inspeção e observações situadas no ARA
→ discussão e delimitação do escopo
→ reparo
→ materialização de nova revisão
→ reauditoria
→ novas rodadas quando necessárias
→ aprovação da parte
→ construção da parte seguinte
```

O mesmo modelo se aplica a reparos posteriores motivados por observações de estudantes, professores, tutores ou pesquisadores e a alterações livres realizadas por usuários autorizados com LLM por API.

## 3. Usuários e agentes podem criar derivações

Um usuário autorizado pode:

- editar manualmente;
- usar LLM por API no ARA;
- usar GPT com MCP;
- criar conteúdo novo;
- reparar conteúdo;
- adaptar conteúdo para outro público ou finalidade;
- consolidar contribuições ou versões;
- continuar uma linhagem própria ou compartilhada.

Quando a alteração é confirmada e materializada, nasce uma nova revisão derivada da revisão-base.

Não existem categorias fixas de branch como `main`, `experimental` ou `repair`. A interface deve representar fatos reais:

- revisão de origem;
- autor humano;
- agente e configuração utilizados;
- finalidade declarada quando houver;
- contexto de uso;
- visibilidade e audiência;
- relações de derivação e consolidação.

## 4. Grafo somente no nível do curso

A visualização principal de versões e derivações será renderizada somente no nível do curso.

Cada nó do grafo representa uma revisão completa e utilizável do curso. Cada aresta representa derivação, restauração, consolidação ou outra relação versionada entre revisões do curso.

Módulos, lições, microssequências, cards e resources não terão grafos principais próprios na interface de navegação aceita nesta fase.

Esses objetos permanecem:

- versionados internamente quando alterados;
- referenciados pelo manifesto da revisão do curso;
- disponíveis na estrutura hierárquica do curso;
- identificáveis em diffs;
- alvos de observações, findings, auditorias e reparos;
- recuperáveis para análise de proveniência.

A decisão evita grafos recursivos ou grafos dentro de grafos, que se mostraram confusos nos mocks da sessão.

## 5. Estrutura de navegação aceita

A interface desktop deve usar, como direção de idealização:

```text
painel esquerdo
- pastas e cursos visíveis ao usuário

área central
- grafo da linhagem do curso selecionado

painel contextual
- revisão selecionada, autoria, origem, acesso, composição e ações
```

O painel esquerdo lista todos os cursos que o usuário pode ver, e não uma categoria chamada “Meus cursos”.

Cursos podem ser:

- públicos;
- privados com pessoas e grupos explicitamente autorizados;
- limitados adicionalmente pela atenuação de acesso herdada de suas origens.

Ao selecionar uma revisão do curso, a interface pode abrir:

- composição hierárquica;
- módulos, lições, microssequências e cards;
- preview ou runtime herdado do AraLearn;
- diff contra outra revisão;
- observações e findings;
- auditorias, reparos e reauditorias;
- configuração e proveniência;
- relações com turmas, protocolos e condições de pesquisa.

## 6. Escala do grafo e projeções de interface

O grafo canônico pode conter muitas revisões e derivações. A interface não deve presumir que todos os nós serão renderizados simultaneamente.

O sistema deve preservar o DAG completo e oferecer projeções orientadas à tarefa, como:

- ancestrais e descendentes próximos da revisão selecionada;
- linhagem de uma pessoa ou grupo;
- versões compartilhadas com o usuário;
- consolidações;
- revisões fixadas em uma turma ou protocolo;
- derivações que alteraram determinado módulo, lição, microssequência ou card;
- caminho entre duas revisões;
- agrupamentos expansíveis de grandes conjuntos de derivações.

A projeção visual não altera nem simplifica o grafo canônico armazenado.

## 7. Consolidações concorrentes

Não existe necessariamente uma única consolidação correta.

Partindo do mesmo conjunto de revisões, observações ou contribuições, Fabio, outro pesquisador, um grupo ou um agente podem produzir consolidações distintas.

Cada consolidação deve registrar:

- revisão-base principal;
- revisões e observações examinadas;
- critérios e rubrica;
- agente e configuração;
- decisões humanas;
- itens incorporados, modificados e rejeitados;
- nova revisão resultante.

As consolidações permanecem comparáveis e podem constituir objetos legítimos de pesquisa educacional.

## 8. Proveniência sem sobrecarregar o GPT

O GPT ou agente executa o trabalho cognitivo de planejamento, construção, auditoria, reparo e reauditoria.

O MCP e o backend registram automaticamente os fatos já conhecidos pelo sistema:

- pessoa autenticada;
- agente e configuração;
- ferramenta ou operação;
- revisão-base;
- alvo e escopo;
- request ID;
- autorização humana;
- objetos alterados;
- validação;
- diff;
- revisão resultante.

O agente não deve receber uma segunda tarefa de redigir toda a contabilidade histórica.

Análises sofisticadas de autoria, agência, participação humana e qualidade são processos posteriores, executados somente quando houver finalidade definida.

## 9. Participação humana observável

O sistema deve conseguir distinguir, sem atribuir percentuais automáticos de autoria:

```text
proposta aceita como apresentada
≠
proposta parcialmente aceita
≠
proposta contestada ou reformulada
≠
novo escopo ou conteúdo acrescentado pelo usuário
```

Devem ser preservados, quando disponíveis:

- proposta inicial;
- decisão humana;
- itens aceitos, rejeitados ou modificados;
- novos requisitos e alvos;
- observações utilizadas;
- proposta final executada;
- diff materializado.

A interpretação científica dessas diferenças não integra o registro operacional obrigatório.

## 10. Retenção sustentável

São duráveis por padrão:

- revisões materializadas do curso;
- manifests e referências necessárias à reconstrução;
- relações do grafo;
- operação geradora;
- atores humanos e agentes;
- configuração efetiva do agente;
- diff;
- decisões, findings e observações diretamente ligados à transformação;
- acesso, proveniência e referências de pesquisa.

São configuráveis por implantação, workspace ou protocolo:

- prompts completos;
- respostas brutas da LLM;
- mensagens intermediárias;
- contexto recuperado;
- propostas rejeitadas;
- outputs detalhados;
- anexos.

São transitórios ou locais:

- digitação;
- undo/redo;
- estado da interface;
- caches;
- respostas inválidas;
- operações ainda não sincronizadas.

A plataforma não exige armazenamento indiscriminado de toda conversa, todo contexto ou telemetria comportamental.

## 11. Valor potencial para pesquisa

A preservação fina das revisões pode permitir pesquisas sobre:

- evolução longitudinal de materiais;
- divergência e convergência entre autores;
- efeitos de diferentes configurações de agente;
- aceitação, rejeição e reformulação de propostas de IA;
- auditorias, reparos, regressões e estabilização;
- processos de consolidação concorrentes;
- relação entre trajetórias autorais e resultados educacionais sob protocolo apropriado.

Essas possibilidades não constituem alegação de efetividade nem definem a futura dissertação. Elas caracterizam capacidades de investigação que o ARA pretende tornar possíveis.

## 12. Efeito no pré-backlog

Estas decisões refinam, sem criar novos itens:

### Área Q

- Q08, Q09, Q13, Q16, Q18, Q23 e Q25.

### Área R

- R01, R02, R03, R04, R05, R10, R14, R17, R18, R19 e R20.

### Área S

- S04, S05, S06, S07, S08, S10, S11, S12, S13, S20, S21, S22, S25 e S26.

## 13. Decisões que não permanecem abertas

Para a continuação dos mocks e da idealização, não devem ser reabertas silenciosamente:

- cada alteração efetivamente materializada cria nova revisão do curso;
- o grafo principal é renderizado somente no nível do curso;
- níveis internos aparecem como composição, navegação e diff, não como grafos principais recursivos;
- usuários autorizados podem criar derivações com edição manual, LLM por API ou GPT com MCP;
- branches técnicas fixas não organizam a interface;
- o backend registra proveniência operacional automaticamente;
- o grafo completo é preservado, mas a UI usa projeções e agrupamentos para escala;
- retenção rica é possível, porém não indiscriminada.
