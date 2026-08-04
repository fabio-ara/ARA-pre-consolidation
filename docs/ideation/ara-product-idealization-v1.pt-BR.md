# Idealização do produto ARA

**Estado:** proposta ampla e revisável  
**Relação com o AraLearn:** sucessor funcional, não simples continuação de código  
**Fase:** pré-desenvolvimento

## 1. Tese do produto

O ARA deve permitir que uma pessoa sem conhecimento de banco de dados, arquitetura ou contratos JSON:

- estude cursos estruturados em microssequências;
- crie e adapte cursos com apoio de LLM;
- veja o que está sendo criado enquanto o processo acontece;
- intervenha em cards, resources, microssequências, dependências, versões e parâmetros;
- audite e repare conteúdo de modo localizado;
- compare versões ou condições de pesquisa;
- trabalhe offline e sincronize depois;
- compreenda onde o conteúdo está, de onde veio, quem pode vê-lo e o que será afetado por uma alteração.

O produto deve ser reconhecível como sucessor do AraLearn:

```text
estudo por microssequências
+ resources declarativos
+ prática e feedback determinísticos
+ offline
+ autoria por GPT/MCP
+ observações situadas
+ publicação versionada
```

O salto do ARA é:

```text
parametrização explícita
+ composição reutilizável
+ versões visíveis
+ dependências tipadas
+ controle humano superior
+ kernel extensível
+ infraestrutura substituível
```

## 2. Princípios de experiência

### 2.1 O conteúdo continua sendo o centro

O estudante não entra num dashboard administrativo. Abre sua biblioteca, retoma um curso e vê o card. Recursos avançados aparecem quando têm relação com a tarefa atual.

### 2.2 Complexidade progressiva

A mesma plataforma atende autodidata, autor, professor, tutor, pesquisador e instituição, mas não mostra tudo a todos.

Camadas sugeridas:

1. **ação comum:** estudar, continuar, observar, rever;
2. **detalhe:** estrutura, versão, fontes e dependências;
3. **autoria:** editar, pedir ao GPT, comparar e reparar;
4. **configuração:** perfil, consequências e overrides;
5. **pesquisa/administração:** condição, governança, armazenamento e diagnósticos.

### 2.3 A pessoa decide; o GPT propõe e executa operações autorizadas

O GPT pode planejar, construir, auditar e reparar. O ARA deve tornar visíveis:

- o alvo;
- o papel do agente;
- o contexto autorizado;
- o que foi lido;
- a alteração proposta;
- o diff;
- validações;
- findings;
- decisões da pessoa;
- a revisão resultante.

### 2.4 Offline não é modo degradado

O baseline deve permitir leitura, prática determinística, retomada, comentários locais, edição manual compatível e inspeção dos artefatos materializados. Capacidades conectadas ficam marcadas como indisponíveis, não simuladas silenciosamente.

### 2.5 Nenhuma decisão técnica aparece como obrigação cognitiva do usuário

A interface não pede para administrar tabelas, buckets, foreign keys, hashes ou outbox. Ela traduz isso para perguntas como:

- “Esta alteração vale só neste curso ou em todos que usam a unidade?”
- “Deseja manter a versão baixada ou atualizar?”
- “Este curso será privado, compartilhado ou público?”
- “A revisão será aplicada agora ou apenas comparada?”
- “O estudo continuará disponível offline?”

## 3. Canais de interação

O ARA possui dois canais complementares.

### 3.1 Chat com GPT e MCP

Adequado para:

- expressar objetivos em linguagem natural;
- planejar curso, parte ou microssequência;
- pedir pesquisa e fontes;
- construir conteúdo em lotes delimitados;
- auditar segundo rubrica;
- reparar findings selecionados;
- derivar variante parametrizada;
- consultar unidades de outros cursos autorizados;
- discutir decisões e alternativas.

### 3.2 Interface ARA

Adequada para:

- navegar e estudar;
- ver a construção em tempo real;
- escolher alvo e versão;
- executar operações determinísticas;
- selecionar cards/resources;
- mover placements;
- criar comentários e findings;
- aceitar, rejeitar ou aplicar parcialmente;
- comparar configurações e versões;
- publicar, retirar, exportar e remover;
- compreender armazenamento e sync.

### 3.3 Ciclo integrado

```text
pessoa conversa com GPT
→ GPT/MCP registra operação delimitada
→ ARA mostra estado e artefatos em evolução
→ pessoa inspeciona/comenta/decide
→ GPT/MCP relê o alvo persistido
→ reparo gera nova revisão
→ ARA mostra diff e resultado
```

O chat não é fonte de verdade. O estado persistido e versionado é a base da rodada seguinte.

## 4. Unidade autoral e composição

### 4.1 Hipótese principal

```text
MicrosequenceLineage
└── MicrosequenceRevision
    ├── metadata pedagógica
    ├── cards/resources
    ├── fontes
    └── relações conceituais

CourseVersion
└── Placements ordenados
    ├── referência à revisão
    ├── papel no curso
    ├── dependências contextuais
    └── overrides de configuração
```

A microssequência é a primeira candidata a unidade reutilizável porque coincide com o nível em que o AraLearn já materializa, audita e repara conteúdo. Ela não é declarada átomo universal: certos resources, bundles de prática ou conjuntos maiores podem exigir outro recorte.

### 4.2 O curso continua completo

Um curso não é uma lista arbitrária de fragmentos. Sua versão declara:

- objetivos;
- público e pré-requisitos;
- módulos/lições ou outra organização de apresentação;
- placements;
- relações de ordem e dependência;
- configuração efetiva;
- fontes e licenças;
- capability requirements;
- estado de auditoria e publicação.

### 4.3 Relações que precisam ser distintas

- `reference`: usa uma revisão sem criar linhagem nova;
- `copy`: cria conteúdo independente sem ligação operacional futura;
- `fork`: cria linhagem derivada com provenance;
- `adaptation`: deriva para público, contexto ou parâmetro diferente;
- `translation`: deriva preservando relação linguística;
- `snapshot`: incorpora uma revisão num pacote imutável;
- `supersedes`: marca substituição editorial;
- `reuses`: registra reutilização sem equivalência pedagógica automática.

## 5. Dependências e conhecimento acumulado

Tags livres não devem sustentar progressão. O ARA deve explorar um grafo tipado com IDs estáveis.

Relações candidatas:

- `requires`;
- `introduces`;
- `explains`;
- `exemplifies`;
- `practises`;
- `assesses`;
- `revisits`;
- `contrasts-with`;
- `misconception-of`;
- `derived-from`;
- `supersedes`;
- `reuses`.

Esse grafo pode apoiar:

- contexto para o GPT;
- verificação de lacunas;
- distratores ligados a erros/conceitos já apresentados;
- impacto de alterações;
- reaproveitamento entre cursos;
- retomada e revisão;
- comparação de variantes.

Exposição não implica domínio. O uso de uma dependência em outro curso não transfere automaticamente progresso ou mastery.

## 6. Parametrização

### 6.1 Níveis de incidência

1. **runtime:** tentativas, feedback, reveal, ritmo, revisão;
2. **materialização de conteúdo:** concentração, segmentação, distribuição teoria–prática, exemplos;
3. **composição:** ordem, dependências, placements, reutilização;
4. **autoria e lifecycle:** revisão, aprovação, publicação, acesso;
5. **pesquisa:** condição, instrumentos, eventos e medidas;
6. **direitos:** acessibilidade, consentimento, retirada e privacidade.

### 6.2 Perfil + overlays + overrides

O usuário não preenche centenas de parâmetros. Escolhe um contexto/perfil e vê consequências em linguagem comum.

```text
perfil-base
+ overlays de acessibilidade/offline/pesquisa
+ políticas institucionais autorizadas
+ overrides esparsos por curso/unidade/placement
→ configuração efetiva
```

### 6.3 Parâmetro transformador

Alterar “máximo de tentativas” pode mudar somente runtime. Alterar “conteúdo mais concentrado” exige novas revisões ou nova composição. A interface deve informar a diferença antes da ação.

### 6.4 Variantes de pesquisa

Uma variante deve registrar:

- escopo de conteúdo comum;
- invariantes;
- parâmetros alterados;
- revisões derivadas;
- diferenças acidentais detectadas;
- condição e público;
- provenance.

## 7. Recursos e práticas

### 7.1 Resource

Resource é uma representação declarativa da estrutura com que a pessoa raciocina: texto, tabela, grafo, fórmula, sequência, reação etc.

### 7.2 Practice

Practice define o que a pessoa faz e como a resposta é capturada. Não deve ser confundida com o resource visual.

### 7.3 Validator

Validator determinístico recebe response e definition e devolve resultado estruturado. Um validator por LLM, quando um dia existir, será capability conectada explícita, não fallback do baseline.

### 7.4 Feedback

Feedback é conteúdo/configuração separado da validação. Pode variar por opção, erro, etapa ou política de reveal.

### 7.5 Pacotes

Cada resource package candidato deve possuir:

- manifesto e versão;
- schema de conteúdo;
- schema de autoria;
- renderer;
- representação acessível;
- adapters de prática compatíveis;
- validadores semânticos próprios;
- exemplos e fixtures;
- limites de mobile/performance;
- migrations próprias;
- política de fallback;
- testes isolados e de conformance.

## 8. Perfis de usuário

### 8.1 Autodidata

- biblioteca pessoal;
- estudo offline;
- criação/adaptação local opcional;
- controle de dados;
- parâmetros simplificados;
- sem analytics compartilhados por padrão.

### 8.2 Autor/professor

- workspace;
- composição e dependências;
- comentários e findings;
- GPT/MCP;
- versões, preview e publicação;
- visão de impacto de unidades reutilizadas.

### 8.3 Tutor/revisor

- fila orientada a questões reais;
- acesso somente ao contexto autorizado;
- resposta e triagem;
- auditoria por rubrica;
- ausência de ranking comportamental.

### 8.4 Pesquisador

- variantes, condições e snapshots;
- instrumentos e eventos autorizados;
- diffs e fidelity;
- exportação governada;
- separação entre dado, medida, constructo e interpretação.

### 8.5 Instituição

- identidade e políticas locais;
- conteúdo confidencial;
- papéis e aprovações;
- implantação própria ou gerenciada;
- retenção, backup e auditoria;
- sem contaminar workspaces pessoais com locks institucionais.

## 9. Superfícies do produto

Navegação candidata:

```text
Biblioteca
├── Continuar
├── Cursos e coleções
├── Trilhas/pastas
└── Offline neste dispositivo

Criar
├── Workspaces
├── Cursos em construção
├── Unidades reutilizáveis
├── Operações GPT/MCP
└── Configurações e versões

Revisar
├── Minhas observações
├── Findings
├── Auditorias
├── Reparos
└── Aprovações/publicações

Pesquisar
├── Protocolos
├── Condições/variantes
├── Instrumentos
├── Evidência/exports
└── Analytics por pergunta

Administrar
├── Pessoas e papéis
├── Capabilities/resources
├── Armazenamento e sync
├── Licenças/provenance
└── Diagnóstico
```

Essas áreas são capacidades, não cinco abas obrigatórias. O perfil pessoal pode mostrar somente Biblioteca e Criar.

## 10. Funcionamento offline e sincronização

### 10.1 Materialização local

O dispositivo recebe:

- manifesto da versão do curso;
- revisões de microssequência referenciadas;
- resources/capabilities necessários;
- assets;
- configuração efetiva;
- provenance mínimo;
- estado pessoal.

A instalação só é ativada depois de validação integral. A versão anterior continua disponível se houver falha.

### 10.2 Estado pessoal contextual

Chave conceitual:

```text
pessoa/atribuição
+ versão do curso
+ placement
+ card/practice
```

Não usar apenas `pessoa + microssequência`, porque a mesma revisão pode aparecer em contextos diferentes.

### 10.3 Alterações de autoria

Autoria sem sync remoto deve continuar localmente. Quando existir conexão, operações são enviadas com request ID e base revision. Conflito semântico resulta em releitura, reapply, fork ou escolha humana.

### 10.4 Capacidade indisponível

Estados possíveis:

- disponível localmente;
- disponível após download;
- conectada e disponível;
- temporariamente indisponível;
- não suportada nesta implantação;
- bloqueada por política.

## 11. Visibilidade do armazenamento

O usuário não precisa saber o nome do serviço, mas deve compreender:

- o que está apenas neste dispositivo;
- o que está sincronizado;
- o que está compartilhado;
- o que é snapshot publicado;
- quais cursos referenciam uma unidade;
- quanto espaço o curso e seus assets ocupam;
- o que será removido numa operação;
- se uma exclusão é local, lógica, retirada ou hard delete;
- se uma publicação ou protocolo exige retenção.

## 12. Lifecycle de autoria

Estados candidatos:

```text
planned
→ suggestion
→ draft
→ validated-structure
→ needs-review
→ audited
→ ready
→ approved
→ published
```

Saídas laterais:

- rejected;
- superseded;
- withdrawn;
- archived.

`revision` é concorrência/versão; não significa qualidade nem aprovação.

## 13. Analytics

O ARA não inicia por gráficos. Cada painel responde perguntas.

Estudante:
- onde retomar;
- o que marcou para rever;
- que dados estão sendo guardados.

Autor/professor:
- o que está incompleto;
- quais dependências faltam;
- onde há findings;
- que cursos são afetados por uma alteração.

Pesquisador:
- o que difere entre condições;
- quais versões foram estudadas;
- que evidência está autorizada;
- que dados faltam.

Administrador:
- armazenamento;
- sync;
- capabilities;
- acesso, retenção e integridade.

## 14. Critério de simplicidade

Uma função entra no produto-base somente se:

1. resolve uma jornada recorrente;
2. pode ser explicada sem jargão técnico;
3. possui estado offline/falha claro;
4. não amplia o kernel desnecessariamente;
5. pode ser testada deterministicamente ou classificada como conectada;
6. preserva acessibilidade;
7. possui custo de armazenamento e manutenção compreendido.

## 15. Continuidade e mudança

### ARA deve parecer AraLearn em:

- biblioteca e percurso de estudo;
- card limpo;
- microssequência;
- resources;
- observação;
- offline;
- autoria GPT/MCP;
- preview e publicação.

### ARA deve superar AraLearn em:

- modularidade física;
- gestão de resources;
- composição reutilizável;
- dependências;
- parametrização;
- versões e diffs;
- transparência de operações;
- portabilidade do backend;
- administração simples;
- capacidade de pesquisa comparativa.

## 16. Questões em aberto

- perfil pessoal sem conta entra no produto-base?
- o curso usa obrigatoriamente módulo e lição ou essas são views de composição?
- microssequência é unidade mínima de reutilização ou um bundle versionado?
- packages de resource são carregados estaticamente, dinamicamente ou por build profile?
- a instalação pode aceitar packages de terceiros ou apenas registro confiável?
- qual parte do conteúdo publicado deve ser content-addressed?
- como atualizar unidade reutilizada sem criar coupling invisível?
- quais dos 18 resources entram no baseline?
- qual nível de analytics é útil ao professor sem vigilância?
- qual primeira implantação deve ser demonstrada: Supabase, outro BaaS ou local-only?
