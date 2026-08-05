# Correção v2 — papel do AraLearn, evals e dependência de versionamento

**Estado:** correção normativa apenas sobre a leitura do rascunho; produto continua não normativo  
**Base:** `agent-profiles-participatory-analytics-v1.pt-BR.md`  
**Issues:** #77 e #79

## 1. O que esta correção substitui

No caminho de implantação do documento v1, expressões como “fixtures reais do AraLearn”, “composição equivalente” e “garantir continuidade” podem sugerir que o AraLearn já possua uma implementação comparável da arquitetura modular do ARA.

Essa interpretação está incorreta.

## 2. Papel correto do AraLearn

O AraLearn fornece:

- experiência funcional amadurecida;
- jornadas de estudo, curadoria, auditoria e reparo;
- operações reais executadas por GPT/MCP;
- limitações do system prompt, knowledge e MCP monolíticos;
- exemplos de acoplamento a Supabase;
- amostras de payload e padrões de uso;
- problemas que motivam a reconstrução.

Ele não fornece:

- `AgentProfileVersion` equivalente;
- `KnowledgeCollectionSnapshot` administrável;
- prompts/templates modulares;
- eval suites do ARA;
- diffs da configuração efetiva;
- escala prevista de versões, analytics e pesquisa;
- especificação física obrigatória.

## 3. Evals corrigidos

Os evals do ARA devem partir de:

1. tarefas que o ARA deverá executar;
2. invariantes estruturais e de autorização;
3. casos controlados e sintéticos;
4. rubricas pedagógicas e técnicas;
5. casos negativos e limítrofes;
6. repetições para estimar estabilidade;
7. operações reais do ARA quando existirem.

Jornadas e falhas do AraLearn podem compor casos de contraste, sem alegação de equivalência interna.

## 4. Continuidade corrigida

Continuidade significa:

- preservar jornadas e princípios explicitamente aceitos pelo proprietário;
- não piorar silenciosamente a simplicidade da interface;
- manter conteúdo declarativo e operações delimitadas;
- demonstrar que problemas identificados foram resolvidos;
- registrar diferenças deliberadas.

Não significa reproduzir monolitismo, schemas, tools, storage, sync ou organização física.

## 5. Dependência de versionamento

A decomposição do agente gera novos objetos e snapshots que precisam de retenção sustentável. Essa questão pertence à Issue #79 e à área R do pré-backlog.

Nenhuma configuração modular é considerada viável até que existam:

- inventário de objetos versionados;
- workload e custo estimados;
- política de retenção e garbage collection;
- exportação e restore;
- opção de storage provider-neutral;
- decisão posterior por ADR.

## 6. Caminho corrigido

1. inventariar o AraLearn como contraste;
2. definir os objetos-alvo do ARA;
3. criar casos controlados e sintéticos;
4. formular workloads de versionamento;
5. comparar deployments e retenção;
6. testar um perfil de domínio apenas depois das fronteiras conceituais;
7. coletar evidência operacional real somente quando houver ARA executável;
8. revisar baselines antes de implementação.
