# Proveniência operacional, materialização de revisões e retenção sustentável

**Estado:** síntese para discussão; não normativa  
**Data:** 5 de agosto de 2026  
**Relação:** detalha itens já existentes das áreas Q e R do pré-backlog, sem alterar sua contagem.  
**Issues relacionadas:** #77 e #79

## 1. Problema

O ARA pretende preservar o fluxo já demonstrado no AraLearn:

```text
planejamento
→ aprovação humana
→ construção de uma parte
→ auditoria
→ proposta de reparos
→ inspeção e observações situadas no ARA
→ discussão e delimitação do escopo
→ reparo
→ reauditoria
→ aprovação da parte
→ construção da parte seguinte
```

Também deve permitir reparos posteriores a partir de observações de estudantes, professores, tutores ou pesquisadores, além de novas derivações produzidas por edição manual ou LLM por API.

Cada alteração efetivamente aplicada ao curso persistido deve produzir uma nova revisão do curso. Isso cria valor para reversibilidade, autoria, colaboração e pesquisa, mas pode gerar custos excessivos se o GPT também tiver de redocumentar cada operação ou se todo dado transitório for retido indefinidamente.

## 2. Decisão candidata

Separar três responsabilidades:

```text
GPT ou agente com MCP
- planeja, constrói, audita, repara e reaudita

MCP/backend
- registra automaticamente fatos operacionais, versões e relações

processo analítico posterior
- interpreta trajetórias quando houver finalidade e protocolo
```

O GPT não deve receber uma segunda tarefa de produzir, em linguagem natural, toda a contabilidade histórica da própria operação.

## 3. Materialização por alteração confirmada

Toda operação autoral confirmada que altere o artefato persistido cria uma revisão imutável.

Exemplos:

- criação de parte do curso;
- inserção, remoção ou reorganização de módulo, lição ou microssequência;
- alteração de card ou resource;
- reparo;
- restauração;
- aplicação de parâmetro transformador;
- consolidação de contribuições;
- adaptação ou tradução.

Não criam revisão do curso por si só:

- planejamento não aplicado;
- auditoria;
- finding;
- observação;
- comentário;
- proposta de reparo;
- discussão;
- aprovação ainda não executada.

Esses objetos permanecem ligados à revisão examinada e à operação que eventualmente os utilizou.

## 4. Materialização lógica não exige cópia física integral

Uma revisão do curso pode ser um manifesto completo que reutiliza revisões inalteradas de seus componentes.

```text
CourseRevision V42
├── ModuleRevision A7
├── ModuleRevision B4
└── ModuleRevision C9

alteração em um card do módulo B

CourseRevision V43
├── ModuleRevision A7   reutilizada
├── ModuleRevision B5   nova
└── ModuleRevision C9   reutilizada
```

O mesmo princípio pode ser aplicado em módulo, lição, microssequência, card e resource conforme a granularidade aprovada posteriormente.

## 5. Registro operacional mínimo e automático

O gateway e o backend já conhecem deterministicamente:

- pessoa autenticada;
- agente e configuração efetiva;
- ferramenta MCP chamada;
- versão-base;
- alvo e escopo de escrita;
- request ID;
- horário;
- objetos alterados;
- validação;
- nova revisão resultante;
- diff estrutural;
- autorização humana recebida.

Esses fatos devem ser registrados automaticamente, sem nova chamada ao modelo.

Registro candidato:

```text
OperationReceipt
- operation_id
- actor_id
- software_agent_configuration_ref
- base_revision_ref
- target_refs
- write_scope
- request_id
- validation_result
- result_revision_ref
- changed_object_refs
- created_at
```

## 6. Proveniência contributiva sem resolver autoria automaticamente

É relevante distinguir:

```text
proposta aceita sem alteração expressa
≠
proposta selecionada, contestada, ampliada ou reformulada pelo usuário
```

Contudo, o ARA não deve produzir automaticamente um “percentual de autoria humana” ou declarar autoria exclusiva.

O sistema deve preservar fatos observáveis:

- proposta inicial;
- itens aceitos;
- itens rejeitados;
- itens modificados;
- novos alvos ou requisitos acrescentados;
- observações utilizadas;
- número de rodadas deliberativas;
- proposta final executada;
- diff materializado.

Classificações analíticas mais sofisticadas sobre agência, autoria ou qualidade pertencem a pesquisas posteriores.

## 7. Pacotes seletivos de contexto para o agente

O mesmo GPT pode assumir papéis diferentes em rodadas sucessivas, mas não deve reler todo o curso e todo o histórico em cada chamada.

### Construção

```text
plano aprovado
+ especificação da parte atual
+ partes vizinhas relevantes
+ contratos necessários
```

### Auditoria

```text
revisão congelada
+ escopo
+ rubrica
+ contexto pedagógico necessário
```

### Reparo

```text
revisão auditada
+ findings autorizados
+ observações incluídas
+ escopo de escrita
```

### Reauditoria

```text
revisão anterior
+ revisão reparada
+ findings originais
+ diff
```

Guardar todo o histórico não significa enviá-lo integralmente ao modelo.

## 8. Classes de retenção

Armazenar tudo indiscriminadamente não é requisito da plataforma de pesquisa.

### Retenção durável essencial

- revisões materializadas;
- manifests;
- relações entre revisões;
- operações que as geraram;
- atores humanos e agentes;
- configuração efetiva do agente;
- diffs;
- findings e observações ligados à decisão;
- decisões de aprovação, modificação ou rejeição;
- versões fixadas em publicação, turma ou protocolo;
- acesso e proveniência.

### Retenção configurável

- prompts completos;
- respostas brutas da LLM;
- contexto recuperado;
- mensagens intermediárias;
- propostas rejeitadas;
- checkpoints automáticos;
- outputs detalhados de validação;
- anexos.

### Retenção curta ou local

- digitação;
- undo/redo;
- estado transitório da interface;
- respostas inválidas;
- caches;
- contexto reconstruível;
- operações ainda não sincronizadas.

### Normalmente não registrar

- movimentos de mouse;
- cada foco de campo;
- cada abertura de tela;
- telemetria comportamental sem finalidade;
- raciocínio privado do modelo;
- cópias redundantes de contexto já referenciado.

## 9. Referências em vez de duplicação

A operação pode guardar referências aos objetos utilizados:

```text
base_revision_ref
plan_revision_ref
audit_run_ref
included_observation_refs
agent_configuration_snapshot_ref
prompt_template_ref
tool_contract_ref
```

Prompts, knowledge, rubricas e contratos compartilhados não devem ser copiados integralmente para cada operação quando puderem ser recuperados por uma referência imutável.

## 10. Revisões materializadas + log de operações

A direção candidata é:

```text
revisões imutáveis materializadas
+ operation log append-only para intenção e proveniência
+ projeções prontas para leitura
```

O curso não deve depender da reprodução de todo o histórico para ser aberto. O log explica como uma revisão surgiu; o manifesto permite materializá-la diretamente.

## 11. Escala institucional

A pesquisa de arquitetura deve medir:

- número de revisões e arestas;
- quantidade de objetos pequenos;
- índices e consultas de grafo;
- prompts e respostas retidos;
- configurações de agente;
- observações e findings;
- backups e restore;
- research holds;
- assets e anexos;
- request rate de Storage;
- CPU de projeções e autorização.

O conteúdo textual pode ser pequeno, mas milhões de objetos e operações ainda criam custos de metadata, requests, índices, backup e restauração.

## 12. Políticas por perfil e finalidade

A retenção deve poder variar por implantação, workspace e protocolo.

Exemplos candidatos:

```text
perfil pessoal
- revisões duráveis
- prompts completos por período limitado
- checkpoints locais com retenção curta

perfil institucional
- revisões conforme política
- prompts omitidos, criptografados ou retidos por prazo definido
- logs técnicos com retenção operacional

protocolo de pesquisa
- conjunto explicitamente congelado
- finalidade, acesso e retenção definidos
- proibição de coleta ou reutilização fora do protocolo
```

## 13. Relação com o pré-backlog

Esta síntese detalha, sem criar novos itens:

### Área Q

- Q08 — políticas de contexto e escopo de escrita;
- Q09 — snapshot efetivo da configuração do agente;
- Q13 — proveniência e diff da operação;
- Q16 — ciclo observação → finding → reparo → reauditoria;
- Q18 — analytics de autoria, agente e sistema;
- Q23 — execução analítica reproduzível;
- Q25 — direitos, privacidade e governança analítica.

### Área R

- R01 — versionamento como redutor de burocracia;
- R02 — diário, checkpoint e revisão durável;
- R04 — inventário de objetos versionados;
- R05 — granularidade do artefato;
- R10 — log de operações híbrido;
- R14 — fronteira banco/Storage/local;
- R17 — projeções e front-end;
- R18 — contexto vertical e horizontal;
- R19 — retenção, GC e research holds;
- R20 — workload, custo, BaaS e ADR.

## 14. Questões abertas

1. Qual alteração confirmada cria revisão imediata e qual apenas checkpoint?
2. Quais mensagens e respostas brutas são necessárias para reprodução em cada tipo de pesquisa?
3. Qual granularidade física minimiza duplicação sem multiplicar excessivamente objetos?
4. Como representar deterministicamente seleção, rejeição e modificação de propostas em linguagem natural?
5. Que partes da configuração do modelo são realmente recuperáveis e estáveis entre providers?
6. Como aplicar retenção diferenciada sem quebrar proveniência, auditoria ou restauração?
7. Quais workloads institucionais devem controlar a ADR inicial?
8. Como exportar uma trajetória de pesquisa sem exportar dados fora de sua finalidade autorizada?

## 15. Limites

Esta síntese não autoriza:

- armazenar toda conversa ou todo contexto por padrão;
- classificar automaticamente autoria, agência ou qualidade;
- usar logs operacionais como dados de pesquisa sem protocolo;
- adotar event sourcing integral;
- escolher banco, Storage, provider ou modelo;
- coletar telemetria comportamental ampla;
- eliminar revisões por custo sem verificar referências e retenção;
- exigir que o GPT produza novamente metadata que o backend já conhece.
