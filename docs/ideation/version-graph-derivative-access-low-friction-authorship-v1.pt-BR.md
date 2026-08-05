# Grafo de versões, acesso derivacional e autoria sem burocracia

**Estado:** síntese inicial para discussão; não normativa  
**Data:** 5 de agosto de 2026  
**Issue:** #81  
**Relação:** consolida a discussão posterior à PR #80 e estende as Issues #77 e #79.

## 1. Tese

O ARA deve permitir que a pessoa trabalhe rapidamente, de forma exploratória e até impulsiva, sem tornar o erro destrutivo e sem exigir confirmações para cada detalhe.

O sistema assume silenciosamente o trabalho de:

- salvar localmente;
- criar checkpoints;
- preservar revisões;
- registrar derivações;
- calcular acesso;
- sincronizar;
- recuperar contexto;
- permitir comparação e restauração.

A pessoa vê ações simples:

```text
Editar
Histórico
Comparar
Restaurar
Público
Privado
Quem pode acessar
```

Ela não precisa administrar tabelas, branches, hashes, ACLs, policies ou buckets.

## 2. Resultado da pesquisa comparativa

Não foi identificado um sistema consolidado que reúna exatamente todas as regras propostas para o ARA. A solução é uma composição de padrões já adotados em contextos diferentes.

### 2.1 Visibilidade hierárquica

GitLab aplica um teto de visibilidade: projetos e subgrupos não podem ser mais públicos do que o grupo pai.

**Correspondência com o ARA:** uma derivação não pode tornar público aquilo que depende de um ancestral privado.

### 2.2 Guardrails herdados por interseção

AWS Organizations usa políticas de controle que não concedem acesso; elas definem o máximo permitido. As permissões efetivas dependem da interseção das políticas aplicáveis e dos limites herdados dos ancestrais organizacionais.

**Correspondência com o ARA:** a audiência efetiva de um nó é limitada por todos os ancestrais necessários.

### 2.3 Delegação atenuada

OAuth e credenciais do tipo macaroon admitem delegação com escopo igual ou menor ao recebido. Restrições adicionais podem reduzir a autoridade, mas não ampliá-la.

**Correspondência com o ARA:** uma derivação pode restringir quem acessa, mas não incluir pessoas que não receberam acesso à origem.

### 2.4 Controle de fluxo e dados derivados

Modelos de informação rotulada, como o Decentralized Label Model, e trabalhos sobre derived-data control tratam políticas dos proprietários como restrições que acompanham transformações e combinações de dados. A composição de políticas tende a manter ou aumentar a restrição, salvo autoridade explícita de desclassificação.

**Correspondência com o ARA:** a versão derivada continua subordinada aos limites de acesso das versões das quais depende.

### 2.5 ACLs baseadas em relações

Zanzibar e sistemas inspirados nele armazenam relações entre usuários, grupos e objetos e avaliam autorização em grande escala. OpenFGA documenta padrões para acesso público, relações pai-filho e múltiplas restrições.

**Correspondência com o ARA:** pessoas e grupos autorizados podem ser representados sem uma hierarquia global fixa de contas.

### 2.6 Proveniência e grafos de versão

W3C PROV representa entidades, atividades, agentes e relações de derivação. Git mantém commits imutáveis em um DAG e liga cada revisão a seus pais e ao snapshot correspondente.

**Correspondência com o ARA:** cards, microssequências, configurações e cursos podem possuir linhagens navegáveis, autoria, operações e relações de derivação.

### 2.7 Versionamento sobre object storage

lakeFS demonstra que semântica semelhante à do Git pode ser construída sobre armazenamento de objetos, com commits, rollback e branches sem cópia integral: uma nova branch é inicialmente metadata-only e novos objetos surgem quando há alterações.

**Correspondência com o ARA:** versões e derivações não precisam duplicar cursos completos.

## 3. Nome técnico candidato

A formulação mais precisa encontrada para o modelo é:

> **controle de acesso derivacional com atenuação monotônica**

O nome reúne:

- controle por nó;
- dependência de proveniência;
- autoridade que só pode permanecer igual ou diminuir ao derivar;
- ausência de ampliação silenciosa de audiência.

Não é necessário apresentar esse termo ao usuário. A interface usa apenas **Público**, **Privado** e **Quem pode acessar**.

## 4. Modelo candidato

### 4.1 Nó versionado

```text
ArtifactRevision
- id
- lineage_id
- artifact_type
- author_id
- required_parent_ids[]
- container_revision_id?
- declared_visibility: public | private
- direct_subjects[]: user | group
- manifest_hash
- operation_id
- created_at
```

### 4.2 Audiência declarada

```text
declaredAudience(n) =
  everyone                              se n é público
  {author(n)} ∪ directSubjects(n)        se n é privado
```

### 4.3 Teto herdado

Para cada derivação, o sistema calcula o conjunto máximo herdado:

```text
inheritedCeiling(n) =
  interseção das audiências efetivas
  de todos os pais e contêineres necessários
```

A audiência declarada do descendente precisa ser subconjunto desse teto:

```text
declaredAudience(n) ⊆ inheritedCeiling(n)
```

Consequências:

- origem pública → derivação pública ou privada;
- origem privada → derivação obrigatoriamente privada;
- a lista do descendente só mostra pessoas ou grupos já autorizados;
- múltiplos pais → vale a interseção entre todos;
- o autor do descendente não possui bypass sobre ancestral revogado.

### 4.4 Audiência efetiva

```text
effectiveAudience(n) =
  declaredAudience(n)
  ∩ effectiveAudience(parent 1)
  ∩ ...
  ∩ effectiveAudience(parent k)
  ∩ effectiveAudience(container)
```

Uma implementação não deve percorrer todo o grafo em cada leitura. A pesquisa de arquitetura deve avaliar:

- política efetiva materializada;
- digests de política;
- invalidação por mudança em ancestral;
- índices de descendentes afetados;
- cache com revisão e causalidade explícitas.

## 5. Revogação

Quando o autor de um ancestral remove uma pessoa ou grupo:

- o ancestral permanece no grafo;
- a nova política é versionada;
- descendentes dependentes não são apagados;
- pessoas excluídas perdem acesso efetivo aos descendentes;
- isso pode atingir o próprio autor de uma derivação;
- a interface mostra o nó bloqueado somente na medida permitida;
- restaurar o acesso pode reativar automaticamente os descendentes.

Exemplo:

```text
B — privado: Fabio, Ana
└── C — autora: Ana; privado: Ana

Fabio remove Ana de B
→ Ana perde acesso efetivo a B
→ Ana perde acesso efetivo a C
→ C continua no grafo como revisão bloqueada
```

A regra expressa a autoridade do autor do componente anterior sobre a disponibilidade do conteúdo do qual os descendentes dependem.

Esse comportamento é uma decisão específica do ARA. Os sistemas examinados fornecem precedentes para visibilidade herdada, guardrails e atenuação, mas não estabelecem universalmente que o autor derivado deva perder acesso ao próprio descendente.

## 6. Versionamento sem cerimônia

### 6.1 Diário local

IndexedDB mantém:

- digitação;
- mudanças ainda não consolidadas;
- undo/redo;
- estado da interface;
- operações não sincronizadas.

Esses registros não aparecem como versões editoriais permanentes.

### 6.2 Checkpoints automáticos

Uma revisão pode ser criada por regras como:

- saída do editor;
- inatividade;
- fim de uma operação da IA;
- alteração estrutural;
- sincronização;
- restauração;
- fechamento de sessão;
- checkpoint manual opcional.

Não se exige nome, mensagem ou aprovação para cada checkpoint.

### 6.3 Revisões duráveis

Revisões sincronizadas são imutáveis. Alterar novamente cria outra revisão.

Restaurar uma versão anterior não apaga versões posteriores. A restauração cria uma nova revisão e registra a origem restaurada. O histórico permanece investigável.

## 7. Grafo visível

O grafo não precisa ser ocultado. Para autores, pesquisadores e curadores, ele pode ser a forma mais clara de navegar no histórico.

Cada nó pode abrir:

- conteúdo daquela revisão;
- autor ou agente;
- data;
- tipo de operação;
- diff;
- observações relacionadas;
- configuração do agente;
- disponibilidade e audiência;
- pesquisas ou condições que fixaram a revisão;
- motivo de bloqueio ou restauração.

Camadas ativáveis:

1. **versões e derivações**;
2. **operações**: manual, LLM por API, GPT/MCP, reparo, restauração;
3. **observações e findings**;
4. **acesso**: público, privado, bloqueado;
5. **pesquisa**: condições, snapshots e análises.

## 8. Unidade de armazenamento

A hipótese integrada é:

```text
MicrosequenceRevision
└── manifest
    ├── CardRevision
    │   └── ResourceRevision[]
    ├── CardRevision
    └── ordem/relações
```

- microssequência: unidade principal de coerência, contexto e histórico editorial;
- card: unidade de edição localizada, observação e deduplicação;
- resource: objeto próprio quando seu tamanho, reutilização ou semântica justificarem;
- curso: composição de revisões de microssequência por placements.

A escolha final da granularidade exige workload e medição sob #79.

## 9. Investigação vertical e horizontal

### 9.1 Vertical

Análise longitudinal da trajetória de um artefato:

```text
revisões
→ operações
→ observações
→ reparos
→ reversões
→ configurações do agente
→ efeitos posteriores
```

### 9.2 Horizontal

Análise transversal de muitos usuários, branches, observações ou artefatos:

```text
muitos nós e participantes
→ convergências
→ divergências
→ evidências
→ padrões de alteração
→ recomendação
```

### 9.3 Ciclo conjunto

```text
padrão horizontal
→ investigação vertical das linhagens afetadas
→ hipótese
→ reparo
→ acompanhamento horizontal posterior
```

A recuperação para o GPT deve selecionar contexto relevante. Guardar todo o histórico não significa enviá-lo integralmente ao modelo.

## 10. Publicação deixa de ser o centro

Cursos e demais artefatos permanecem provisórios. O produto deve distinguir:

- **visibilidade:** público ou privado;
- **audiência:** pessoas e grupos de um privado;
- **versão atual:** revisão aberta por padrão;
- **versão fixada:** revisão usada por curso, turma, experimento ou análise;
- **disponibilidade:** se a cadeia necessária continua acessível;
- **trajetória:** grafo completo de evolução.

Não se presume um estágio final de publicação.

## 11. Fontes externas

O ARA não é, por padrão, um repositório das obras usadas como ancoragem para estudo. Ele armazena os artefatos gerados e suas relações internas.

Podem existir referências bibliográficas ou metadados dentro do conteúdo, mas a gestão e o armazenamento das fontes externas não integram automaticamente o núcleo proposto.

Knowledge collections administrativas do agente são uma preocupação distinta da biblioteca de fontes do estudante e permanecem sob #77.

## 12. Separação Storage/banco/local

```text
Object/artifact storage
- manifests e JSONs imutáveis
- cards/resources versionados
- configurações e prompts versionados
- diffs materializados
- exports e snapshots

Banco de metadata
- IDs e lineages
- edges do grafo
- refs atuais/fixadas
- autores
- políticas declaradas
- audiência efetiva materializada
- índices e invalidações
- operações e observações

IndexedDB/local
- diário de trabalho
- autosave
- materialização offline
- fila de sync
- undo/redo
```

A compatibilidade do backend precisa ser avaliada pelo comportamento do conjunto, não apenas por quotas de Storage.

## 13. Requisitos para BaaS ou backend portátil

A frente #79 deve avaliar se a opção suporta:

- object storage com chaves imutáveis e API estável;
- escrita condicional ou proteção contra sobrescrita;
- banco transacional para metadata e refs;
- consultas eficientes de ancestrais/descendentes;
- invalidação e recomputação de acesso efetivo;
- autenticação de pessoas e grupos;
- URLs assinadas ou gateway para artefatos privados;
- operações idempotentes;
- fila/outbox ou mecanismo equivalente;
- exportação e restauração integral;
- backup verificável;
- retenção e garbage collection conscientes das referências;
- implantação gerenciada e institucional;
- ausência de dependência da versão nativa do bucket.

## 14. Grafo no front-end

### Mermaid

Adequado a trajetórias pequenas, documentação, protótipos e grafos predominantemente de leitura. Suporta callbacks e links em nós, mas a interatividade depende de configuração de segurança menos restritiva e não oferece, por si só, uma superfície completa para grandes grafos.

### Cytoscape.js

Adequado a grafos reais, seleção, travessia, filtros, pan/zoom, múltiplos layouts e grafos compostos. É candidato forte para visualização investigativa.

### React Flow

Adequado a nós altamente customizados, controles dentro dos nós e superfícies de autoria. Layout automático costuma exigir Dagre ou ELK.

### ELK.js

É motor de layout, não renderer. Pode complementar Cytoscape.js, React Flow ou outra camada em DAGs grandes e direcionados.

Nenhuma opção é selecionada nesta fase.

## 15. Contextos de adoção dos padrões

A solução composta possui precedentes em:

- plataformas de código e projetos hierárquicos;
- organizações de cloud com guardrails herdados;
- credenciais delegadas e tokens de escopo reduzido;
- sistemas de informação rotulada;
- compartilhamento e transformação de dados sensíveis;
- serviços globais de ACLs relacionais;
- provenance e pesquisa reproduzível;
- data lakes versionados;
- ferramentas de autoria local-first.

## 16. Limites

A regra simples de acesso não substitui:

- proteção de dados pessoais;
- obrigação legal;
- segurança da implantação;
- isolamento de datasets de pesquisa;
- resposta a incidentes;
- regras institucionais externas.

Esses temas não devem, contudo, reintroduzir uma matriz cotidiana de papéis e confirmações no fluxo comum de autoria.

## 17. Decisões já incorporadas

- versionamento é requisito central;
- grafo de versões pode ser apresentado;
- restauração não apaga história;
- edição comum não exige rito de aprovação;
- publicação não é endpoint de maturidade;
- somente público e privado aparecem como visibilidades comuns;
- privados podem autorizar pessoas e grupos;
- descendentes não ampliam acesso;
- revogação ancestral pode bloquear descendentes;
- fontes externas não são armazenadas por padrão;
- conteúdo versionado reside prioritariamente em artifact storage;
- metadata e projeções residem no banco;
- local-first e IndexedDB permanecem parte do desenho;
- a pesquisa deve usar o histórico vertical e horizontalmente.

## 18. Questões abertas

- frequência e compactação dos checkpoints;
- granularidade final entre microssequência, card e resource;
- semântica de merges com múltiplos pais;
- metadata visível num nó bloqueado;
- tratamento de mudança de membros de grupos em pesquisas;
- custo da recomputação de acesso;
- retenção de branches bloqueadas;
- stack de visualização;
- BaaS e deployment;
- política excepcional para obrigações jurídicas ou incidentes.
