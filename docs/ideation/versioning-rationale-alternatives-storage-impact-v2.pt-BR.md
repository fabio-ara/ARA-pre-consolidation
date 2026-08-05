# Versionamento no ARA — razões, alternativas e impacto arquitetural

**Estado:** síntese v2 para discussão; não normativa  
**Data:** 5 de agosto de 2026  
**Issue principal:** #79  
**Relações:** #77, #81  
**Regra:** este documento não seleciona provider, banco, object storage, schema ou implementação.

## 1. Correção de prioridade

O versionamento não é apenas uma consequência técnica da fragmentação dos cursos nem um detalhe do sistema de acesso. Ele tornou-se um princípio central do produto durante a discussão posterior à PR #80.

A formulação correta é:

> O ARA deve permitir que a pessoa trabalhe depressa e com pouca burocracia porque o sistema preserva silenciosamente a trajetória, torna as ações reversíveis e permite compreender depois o que aconteceu.

O versionamento substitui, sempre que possível:

- confirmações a cada edição;
- medo de estragar o conteúdo;
- necessidade de planejar cada mudança antecipadamente;
- cópias manuais de segurança;
- processos longos de aprovação para alterações reversíveis;
- dependência da memória do chat ou do autor;
- perda do caminho que levou a uma correção.

Confirmações permanecem proporcionais ao impacto externo, como alteração de audiência privada, revogação ancestral, exclusão física, mudança de configuração ativa ou uso formal de uma versão em pesquisa. A edição comum não deve exigir cerimônia.

## 2. Por que o ARA precisa de versionamento

### 2.1 Autoria sem medo

O usuário pode editar diretamente, pedir alterações a uma LLM por API ou realizar reparos por GPT/MCP. Erros e mudanças de ideia não devem destruir o trabalho anterior.

```text
editar rapidamente
→ checkpoint automático
→ continuar
→ restaurar quando necessário
```

Restaurar uma revisão antiga cria uma nova revisão baseada nela. Não apaga caminhos posteriores.

### 2.2 Comportamento impulsivo não destrutivo

O sistema deve ser adequado a pessoas que experimentam antes de decidir. O versionamento delega ao produto a organização que não deve ser exigida do usuário em cada passo.

### 2.3 Conhecimento permanentemente provisório

Curso pronto, curso incompleto, curso reformulado e curso usado em pesquisa continuam sendo estados provisórios de uma linhagem. `Publicado` não é o ápice de um lifecycle. O que importa é:

- revisão atual;
- revisão disponível para determinada audiência;
- revisão fixada por um contexto;
- trajetória e derivações;
- referências que exigem retenção.

### 2.4 Investigação vertical

O GPT deve poder percorrer longitudinalmente a trajetória de um artefato:

```text
versões
→ operações
→ diffs
→ observações
→ reparos
→ restaurações
→ resultados posteriores
```

Isso permite investigar erros recorrentes, regressões, efeito de prompts, modelos, contracts e `resources`, e deduzir melhorias técnicas ou pedagógicas.

### 2.5 Investigação horizontal

O ARA deve reunir observações, versões e derivações de muitas pessoas para identificar convergências, conflitos, alternativas e padrões. A análise horizontal pode iniciar uma investigação vertical; a investigação vertical pode gerar um reparo acompanhado horizontalmente depois.

### 2.6 Pesquisa educacional reproduzível

Um estudo precisa conseguir fixar:

- versões de conteúdo;
- composição do curso;
- parâmetros;
- política de acesso;
- configuração do agente;
- instrumentos, datasets e análises.

Sem versionamento, a plataforma não consegue demonstrar o que os participantes realmente estudaram nem reproduzir uma condição experimental.

### 2.7 Colaboração e derivações

Versões pessoais, variantes experimentais e alterações de grupos diferentes precisam compartilhar o que não mudou e preservar suas origens. O grafo é parte do conteúdo investigável, não apenas estrutura técnica.

### 2.8 Evolução dos agentes

System instructions, perfis de domínio, templates, knowledge snapshots, policies, contracts e evals também evoluem. Cada operação relevante deve registrar a configuração efetiva que a produziu.

### 2.9 Offline e sincronização

A edição local precisa continuar sem conexão. O histórico ajuda a sincronizar operações, detectar bases antigas e preservar alterações concorrentes sem sobrescrita silenciosa.

### 2.10 Acesso derivacional

A audiência de um descendente depende dos ancestrais necessários. Revogações podem bloquear nós sem apagá-los. Logo, revisão, proveniência e acesso são partes do mesmo grafo, embora sejam responsabilidades distintas.

## 3. Três escalas de histórico

### 3.1 Diário local

No IndexedDB ou store local:

- autosave frequente;
- undo/redo;
- estado da interface;
- alterações ainda não sincronizadas;
- eventos de granularidade fina;
- retenção curta ou compactável.

Não é apresentado ao usuário como uma lista de commits.

### 3.2 Checkpoint automático

Criado por política, por exemplo:

- saída do objeto editado;
- inatividade;
- conclusão de operação da IA;
- mudança estrutural;
- sincronização;
- restauração;
- encerramento de sessão.

A política deve evitar tanto perda de trabalho quanto milhares de versões sem significado.

### 3.3 Revisão durável

É a unidade persistida e navegável no grafo. Registra:

- linhagem e pais;
- manifesto ou payload;
- autor/agente;
- operação e motivo;
- diff;
- data;
- audiência declarada e snapshot necessário;
- referências de pesquisa ou retenção.

## 4. Unidades e granularidade

### 4.1 Microssequência

Continua candidata principal a:

- unidade de coerência pedagógica;
- contexto integral da IA;
- revisão editorial visível;
- restauração;
- auditoria;
- composição em cursos.

### 4.2 Card e resource

Podem possuir identidade e artefato próprios para:

- edição localizada;
- deduplicação;
- diff;
- observações situadas;
- seleção de escopo para IA;
- compartilhamento entre revisões da mesma microssequência.

### 4.3 Manifesto hierárquico

```text
MicrosequenceRevision
└── manifest
    ├── CardRevision A
    ├── CardRevision B
    ├── CardRevision C
    ├── ordem
    ├── relações
    └── metadata pedagógica
```

Alterar um card pode criar um novo artefato de card e um novo manifesto de microssequência, reutilizando os objetos inalterados.

A granularidade definitiva depende de benchmark. Fragmentos excessivamente pequenos ampliam quantidade de objetos e consultas; fragmentos grandes ampliam duplicação e custo de diff.

## 5. Alternativas de versionamento

### A — Sobrescrever o estado atual e guardar somente logs

**Como funciona:** o conteúdo atual é atualizado; logs registram operações.

**Vantagens:** CRUD e leitura simples.  
**Problemas:** restauração exige reconstrução ou cópia separada; o log pode não conter estado suficiente; análise histórica fica frágil.  
**Adequação:** insuficiente como modelo principal do ARA.

### B — Snapshots completos no banco relacional

**Como funciona:** cada revisão grava uma nova linha com o JSON completo.

**Vantagens:** transações, consultas e RLS no mesmo sistema.  
**Problemas:** aumenta linhas, índices, WAL, backups, parsing e CPU; repete payloads; pode reproduzir o problema já observado no AraLearn.  
**Adequação:** útil apenas para objetos pequenos ou protótipo medido.

### C — Snapshots completos no object storage

**Como funciona:** cada revisão é um JSON completo imutável; o banco guarda ponteiros.

**Vantagens:** implementação simples, restauração independente e banco pequeno.  
**Problemas:** duplica conteúdo; quantidade de objetos e requests cresce; diffs exigem ler dois snapshots.  
**Adequação:** baseline simples e possível primeira etapa.

### D — Objetos endereçados por conteúdo + manifests

**Como funciona:** cards/resources/blobs imutáveis recebem digest; manifests referenciam os objetos e pais.

**Vantagens:** deduplicação, derivações econômicas e compartilhamento de partes inalteradas. É próximo do modelo de objetos do Git e de sistemas Git-like sobre object storage.  
**Problemas:** canonicalização, integridade, GC e depuração ficam mais complexos; igualdade de bytes não significa igualdade de contexto pedagógico.  
**Adequação:** hipótese principal do ARA, dependente de benchmark.

### E — Cadeias de deltas ou patches

**Como funciona:** uma versão armazena apenas alterações em relação à anterior.

**Vantagens:** pode economizar espaço quando os objetos são grandes e as mudanças pequenas.  
**Problemas:** reconstrução exige cadeia; perda/corrupção afeta descendentes; compaction e migrations são difíceis; acesso aleatório a versões antigas fica caro.  
**Adequação:** possível otimização posterior, não fonte editorial inicial.

### F — Event sourcing integral

**Como funciona:** eventos append-only são a fonte de verdade; estado é reconstruído e projetado.

**Vantagens:** intenção, auditoria e análise longitudinal ricas.  
**Problemas:** evolução de eventos, replay, snapshots, projeções, consistência eventual e migração tornam o padrão caro e restritivo.  
**Adequação:** não recomendado para o produto inteiro. O ARA pode manter operações append-only como proveniência, enquanto revisões imutáveis são a fonte editorial.

### G — Versionamento nativo do bucket

**Como funciona:** o provider preserva versões quando a mesma chave é sobrescrita.

**Vantagens:** recuperação operacional simples contra sobrescrita ou exclusão acidental.  
**Problemas:** cada versão pode ser um objeto completo; IDs não expressam semântica pedagógica; lifecycle do bucket não entende pesquisa, derivações ou audiência. Supabase Storage não oferece S3 Object Versioning.  
**Adequação:** proteção adicional em providers compatíveis, não modelo de domínio.

### H — Versionamento temporal no banco

**Como funciona:** linhas com períodos ou tabelas de histórico representam estados no tempo.

**Vantagens:** consultas temporais e integridade relacional.  
**Problemas:** não representa naturalmente DAGs, múltiplos pais, manifests, blobs grandes ou deduplicação; mantém custo no banco.  
**Adequação:** possível para políticas, memberships ou metadata temporal, não substituto do grafo de artefatos.

### I — Repositório Git verdadeiro

**Como funciona:** artefatos são arquivos num repositório Git servido por filesystem/serviço Git.

**Vantagens:** modelo maduro de DAG, diffs, refs, packfiles e ferramentas.  
**Problemas:** permissões por nó, consultas de produto, pequenas operações online, progresso, analytics e sync mobile não correspondem diretamente ao Git; exige serviço computacional, não apenas bucket.  
**Adequação:** exportação, backup, contratos e artefatos técnicos; não necessariamente backend cotidiano.

### J — Camada Git-like sobre object storage

**Como funciona:** commits/refs são metadata; objetos alterados são gravados no storage; branches podem ser zero-copy.

**Vantagens:** demonstra que histórico e derivações econômicas podem existir sobre object storage sem cópia integral.  
**Problemas:** ferramentas como lakeFS são orientadas a data lakes, não ao domínio pedagógico, ao offline nem ao acesso derivacional do ARA.  
**Adequação:** referência arquitetural e alternativa a prototipar, não dependência escolhida.

## 6. Combinação candidata para o ARA

```text
revisões editoriais imutáveis
+ artifacts content-addressed quando vantajoso
+ manifests hierárquicos
+ operation log append-only para intenção/proveniência
+ projeções materializadas para o front-end
+ IndexedDB para diário local e offline
```

A combinação evita dois extremos:

- reconstruir tudo exclusivamente por eventos;
- duplicar sempre o curso inteiro.

## 7. Impacto no banco de dados

O banco não deixa de participar do versionamento. Ele deixa de carregar os payloads grandes como responsabilidade principal.

### 7.1 O que deve residir no banco

- IDs de linhagem e revisão;
- pais e arestas do DAG;
- ponteiro da revisão atual;
- placements e composição;
- hashes, tamanhos e media types;
- autoria e operações;
- diffs resumidos ou ponteiros;
- audiência declarada e projeção efetiva;
- referências de retenção;
- índices de busca;
- estado de sync;
- snapshots de pesquisa e configuração.

### 7.2 Custos deslocados para o banco

Mesmo sem JSON grande, o banco pode sofrer com:

- crescimento de linhas e índices;
- travessia de grafos;
- invalidação de audiência efetiva após revogação ancestral;
- concorrência sobre refs atuais;
- RLS ou autorização por nó;
- filas de operações e sync;
- projeções para histórico, biblioteca e pesquisa;
- backups de metadata.

### 7.3 Como limitar CPU e armazenamento relacional

- não atualizar JSON monolítico repetidamente;
- manter operações pequenas e append-only quando apropriado;
- materializar audiência e consultas recorrentes;
- paginar histórico e grafo;
- não calcular diffs pesados em cada leitura;
- separar analytics brutos do banco transacional;
- medir quantidade de arestas, índices e invalidations;
- evitar triggers complexos sem benchmark;
- usar ponteiros e digests em vez de copiar payloads.

## 8. Impacto no object storage

### 8.1 O que deve residir no Storage

- JSONs imutáveis de microssequências, cards e resources;
- manifests;
- prompts, perfis e configurações versionadas quando forem artefatos;
- knowledge artifacts administrados pelo ARA, não fontes externas de estudo por padrão;
- diffs grandes, exports e bundles;
- assets e pacotes offline;
- datasets e outputs de pesquisa autorizados.

### 8.2 Custos e riscos

- número muito alto de objetos pequenos;
- custo por PUT/GET/LIST, não apenas por GB;
- latência de muitas leituras pequenas;
- consistência entre metadata e artifact;
- objetos órfãos após falha;
- signed URLs e autorização;
- inventário e verificação de digest;
- backup e restore de milhões de chaves;
- lifecycle e armazenamento frio;
- egress em alguns providers.

### 8.3 Estratégias de redução

- content addressing e deduplicação;
- checkpoints significativos, não um objeto por tecla;
- manifests pequenos;
- cache e materialização local;
- bundles/packfiles para exportação ou storage frio, se medidos;
- compactação de JSON;
- índices de objetos no banco, evitando listagens globais frequentes;
- GC por referência e retenção;
- separação entre fonte canônica e artefatos reconstruíveis.

## 9. Impacto no IndexedDB e sincronização

O IndexedDB deve manter:

- estado materializado atual;
- diário local curto;
- rascunhos;
- outbox;
- objetos necessários offline;
- cache do grafo e dos diffs recentes.

A sincronização deve:

- declarar a revisão-base;
- agrupar autosaves em checkpoints;
- criar revisão durável atomically;
- enviar apenas objetos novos;
- detectar base obsoleta;
- preservar derivações concorrentes;
- atualizar refs somente após validação;
- permitir retry idempotente.

## 10. Impacto no front-end e no GPT

### Front-end

A UI não consulta todos os blobs para mostrar histórico. Usa projeções:

- revisão atual;
- lista paginada de revisões;
- resumo do diff;
- grafo em janela relevante;
- estados de acesso;
- nós usados em pesquisa.

O conteúdo completo é carregado ao selecionar um nó.

### GPT

O GPT não recebe o histórico inteiro por padrão. O ARA monta pacotes de contexto:

- vertical: revisões materiais, operações, diffs, reparos e resultados;
- horizontal: corpus de observações, branches, conflitos e amostras;
- combinado: padrão horizontal seguido de investigação vertical e acompanhamento posterior.

Guardar histórico e enviar contexto são decisões diferentes.

## 11. Retenção e garbage collection

Classes candidatas:

- diário local temporário;
- checkpoint não referenciado;
- revisão atual;
- revisão ancestral de descendente acessível ou bloqueado;
- versão fixada por curso ou audiência;
- versão protegida por pesquisa;
- versão necessária para rollback;
- artefato derivado reconstruível;
- órfão confirmado.

A exclusão física exige provar ausência de referência e de retenção. Revogação e restauração não apagam história.

## 12. Matriz resumida de impacto

| Alternativa | Banco | Storage | Leitura histórica | Escrita | Ajuste ao ARA |
|---|---|---|---|---|---|
| Snapshot completo no banco | alto | baixo | simples | CPU/WAL altos | limitado |
| Snapshot completo no Storage | baixo/médio | alto | simples | simples | bom baseline |
| Content-addressed + manifest | médio | eficiente | média | média | principal hipótese |
| Patches/deltas | baixo | eficiente | cara | complexa | otimização futura |
| Event sourcing integral | eventos/projeções altos | variável | replay | append-only | excessivo como padrão |
| Bucket versioning | metadata externa | cópia completa | provider-specific | simples | apenas proteção |
| Git verdadeiro | fora do DB de produto | packfiles | madura | serviço Git | export/técnico |
| Git-like sobre objects | metadata média | eficiente | média | média/alta | referência forte |

## 13. Requisitos para o BaaS ou backend

A escolha deve suportar ou permitir implementar:

- banco transacional para metadata e refs;
- object storage imutável ou S3-compatible;
- uploads idempotentes;
- verificação de integridade;
- autorização sobre metadata e acesso seguro aos blobs;
- processamento assíncrono de diffs, projeções e GC;
- exportação completa;
- backup e restore testados;
- observabilidade de CPU, requests, storage e filas;
- implantação pública gerenciada e institucional/self-hostable;
- adaptação sem alterar o domínio.

O provider não precisa oferecer versionamento semântico nativo. Precisa permitir que o ARA o implemente com segurança e custo previsível.

## 14. Direção candidata

A direção mais coerente com as decisões até agora é:

```text
IndexedDB
→ diário local, autosave, undo/redo e offline

PostgreSQL ou metadata store transacional
→ lineages, revisions, DAG, refs, operações, acesso e índices

Object storage
→ artifacts e manifests imutáveis

Workers/serviços
→ diffs, projeções, bundles, integridade e GC
```

Ela ainda precisa ser comparada, por workload, com snapshots completos simples e outras alternativas. Não é arquitetura aprovada.

## 15. Critérios para decisão futura

A ADR de infraestrutura e versão somente deve ocorrer depois de medir:

- tamanho e frequência de revisões;
- taxa de deduplicação;
- quantidade e tamanho de objetos;
- reads/writes/list operations;
- custo de travessia e audiência efetiva;
- CPU e WAL do metadata store;
- latência de reconstrução e diff;
- duração de backup e restore;
- comportamento offline e sync;
- custo mensal e operacional em deployment público e institucional;
- portabilidade demonstrada por export/restore.

## 16. Fontes técnicas principais

- Git data model: `https://git-scm.com/docs/gitdatamodel.html`;
- lakeFS model and zero-copy branches: `https://docs.lakefs.io/v1.81/understand/model/`;
- Azure Event Sourcing pattern: `https://learn.microsoft.com/azure/architecture/patterns/event-sourcing`;
- Azure Materialized View pattern: `https://learn.microsoft.com/azure/architecture/patterns/materialized-view`;
- S3 Versioning: `https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html`;
- Supabase S3 compatibility and absence of bucket versioning: `https://supabase.com/docs/guides/storage/s3/compatibility`;
- PostgreSQL temporal tables: `https://www.postgresql.org/docs/19/ddl-temporal-tables.html`.
