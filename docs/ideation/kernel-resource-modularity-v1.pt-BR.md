# Kernel e modularidade de resources/capabilities

**Estado:** opções de desenho para discussão  
**Objetivo:** permitir crescimento do repertório sem alterar continuamente o kernel nem repetir refatorações transversais.

## 1. Problema observado no AraLearn

O AraLearn já possui um registro canônico e separa conceitualmente schema, renderer e autoria. Entretanto:

- schemas e validadores convergem num registry grande;
- renderers convergem num runtime grande;
- o orquestrador principal da UI conhece muitos resources e fluxos;
- novos resources ampliam o bundle comum;
- cópias do runtime são sincronizadas para Edge Functions;
- testes de cobertura protegem consistência, mas a adição ainda toca superfícies centrais.

O ARA precisa preservar a semântica e mudar a fronteira física.

## 2. Referências externas

### H5P

H5P separa core, editor, integração de plataforma e libraries. Uma library possui nome/versão, dependências, dados semânticos, código e metadata. Content types podem ser publicados e atualizados independentemente. Isso demonstra o valor de packages versionados e discoverable, mas também alerta para riscos de código de terceiros, dependências e compatibilidade.

Fontes oficiais:

- [Technical overview](https://h5p.org/node/61447)
- [Content type development](https://h5p.org/library-development)
- [.h5p specification](https://h5p.org/documentation/developers/h5p-specification)
- [Content Type Hub](https://h5p.org/hub-docs/content-type-hub-overview)

### Open edX/XBlock

XBlocks são componentes independentes e composáveis que mantêm estado, renderizam views e processam ações por handlers. A independência permite compartilhamento; a composição permite construir unidades maiores. Para o ARA, o princípio útil é: um package deve funcionar sem conhecer os outros, mas deve respeitar runtime e contratos comuns.

Fonte oficial: [Introduction to XBlocks](https://docs.openedx.org/projects/xblock/en/latest/introduction.html).

### Moodle

Moodle distingue plugin types, question types, question behaviours, renderers, question bank e formatos de importação/exportação. Isso mostra que “o que é a questão”, “como a pessoa interage” e “como é renderizada” são responsabilidades diferentes. Também mostra o custo de uma plataforma com centenas de plugin types: o ARA deve escolher poucas extensões bem delimitadas.

Fontes oficiais:

- [Plugin types](https://moodledev.io/docs/5.1/apis/plugintypes)
- [Question subsystem](https://moodledev.io/docs/5.1/apis/subsystems/question)
- [Question type plugins](https://moodledev.io/docs/5.0/apis/plugintypes/qtype)
- [Component communication](https://moodledev.io/general/development/policies/component-communication)

## 3. Princípio do ARA

```text
kernel estável
+ contratos versionados
+ packages confiáveis
+ adapters de infraestrutura
+ perfis de implantação
```

O kernel não deve conter `if resource === ...` para cada resource. Ele pergunta ao registry de capabilities por um contrato compatível.

## 4. Responsabilidades do kernel

### 4.1 Identidade e versão

- IDs estáveis;
- lineages e revisions;
- provenance e relações de derivação;
- snapshots imutáveis;
- migrations de contratos do kernel.

### 4.2 Composição

- CourseVersion;
- Placement;
- ordem e relações tipadas;
- validação de referências;
- seleção de contexto;
- impacto de alterações.

### 4.3 Configuração

- catálogo de parâmetros;
- perfis, overlays e overrides;
- precedência e locks;
- snapshot efetivo;
- classificação runtime/conteúdo/composição/lifecycle/pesquisa/direitos.

### 4.4 Lifecycle

- draft/review/audit/repair/approval/publication;
- comentários/findings;
- audiences e visibility;
- retirada, supersessão, arquivo e exclusão.

### 4.5 Runtime de estudo

- navegação;
- estado contextual;
- comando de confirmar/limpar/revelar;
- coordenação de practice/validator/feedback;
- fallback e capability unavailable;
- acessibilidade comum.

### 4.6 Portas

- identity;
- authorization;
- artifact repository;
- metadata repository;
- local store;
- sync;
- asset delivery;
- MCP/agent gateway;
- provider LLM;
- research evidence;
- clock/ID/digest.

### 4.7 Segurança

- validação de packages;
- política de capabilities;
- sandbox ou proibição de código não confiável;
- limites de tamanho/profundidade;
- sanitização e CSP;
- controle de acesso e purpose binding.

## 5. O que não pertence ao kernel

- schema específico de grafo, fórmula ou reação;
- algoritmo de layout de um resource;
- formulário autoral específico;
- avaliação específica de uma practice;
- cliente de um provider de LLM;
- SQL de um BaaS;
- código de sincronização de uma implantação;
- analytics de um protocolo;
- regras de coleção/catálogo que possam ser capability opcional;
- lógica específica de Android.

## 6. Tipos candidatos de package

### 6.1 Resource package

Preserva e renderiza uma representação: `paragraph`, `table`, `graph`, `formula` etc.

### 6.2 Practice package

Define interação e response: choice, gap, ordering, matching, selection on structure etc.

### 6.3 Validator package

Compara response com definition de forma determinística. Pode ser compartilhado por practices/resources.

### 6.4 Feedback package

Resolve regras de feedback, reveal, hints e mensagens.

### 6.5 Instrument package

Questionários, escalas, rubricas, diário ou outro instrumento de pesquisa/ensino formal.

### 6.6 Provider package

Adapter para LLM ou serviço conectado. Nunca entra no curso publicado nem recebe autoridade própria.

### 6.7 Infrastructure adapter

Supabase, Appwrite, Nhost, local-only etc. Implementa ports, não muda domínio.

### 6.8 Integration package

LTI, LMS, exportadores, importadores ou formatos externos.

## 7. Manifesto candidato de resource

Exemplo ilustrativo, não schema aprovado:

```json
{
  "package": "ara.resource.graph",
  "version": "1.0.0",
  "kernelContract": ">=1 <2",
  "kind": "resource",
  "resourceIds": ["graph"],
  "contentSchema": "./content.schema.json",
  "authoringSchema": "./authoring.schema.json",
  "renderer": "./renderer.js",
  "accessibleRenderer": "./accessible.js",
  "validators": ["./validate.js"],
  "practiceAdapters": ["choice", "gap", "select-node", "select-edge"],
  "migrations": [],
  "examples": "./fixtures",
  "budgets": {
    "initialJsKb": 0,
    "lazyJsKb": 60,
    "maxItems": 80
  },
  "permissions": [],
  "offline": "full"
}
```

## 8. Contratos mínimos de um resource package

### 8.1 Definition

- id/version;
- labels e descrição;
- usos e contraindicações;
- schemas;
- compatibilidade de practice;
- limites;
- accessibility requirements;
- capability requirements;
- migration support.

### 8.2 Renderer

Entrada:

```text
validated content
+ effective configuration subset
+ practice state
+ locale/accessibility context
```

Saída:

```text
view model ou DOM seguro
+ accessible description/list/table
+ declared interactions
```

O renderer não lê banco, não sincroniza, não publica e não chama LLM.

### 8.3 Authoring adapter

- campos editáveis;
- seleção de alvos;
- preview;
- resumo para GPT;
- schema compacto e integral;
- diff semântico;
- validação local.

### 8.4 Test kit

- fixtures válidas/inválidas;
- round-trip;
- renderer snapshots;
- teclado/toque;
- acessibilidade;
- practices compatíveis;
- limites móveis;
- migrations;
- capability unavailable.

## 9. Registry

O registry do ARA deve ser pequeno e genérico. Pode:

- descobrir manifests no build;
- registrar packages internos;
- validar compatibilidade;
- expor catálogo ao autor/GPT;
- carregar package sob demanda;
- resolver fallback;
- apresentar versão/licença/origem;
- desativar package numa implantação.

Não deve:

- conter schemas copiados de todos os resources;
- conter switches por ID;
- importar todos os renderers no bundle inicial;
- conceder permissões;
- decidir pedagogia por nome do resource.

## 10. Estratégias de carregamento

### Opção A — packages compilados no produto

Cada implantação escolhe packages no build. Simples, seguro e adequado ao primeiro corte. Adicionar resource exige novo build, mas não mudança no kernel.

**Vantagens:** menor superfície de ataque, tree-shaking, testes previsíveis.  
**Limites:** não há instalação em runtime.

### Opção B — dynamic imports internos

Packages oficiais são publicados junto do app e carregados por demanda.

**Vantagens:** bundle inicial menor; uma base suporta muitos resources.  
**Limites:** gestão de cache/versão e disponibilidade offline.

### Opção C — packages instaláveis assinados

Registro confiável permite instalação posterior.

**Vantagens:** ecossistema extensível.  
**Limites:** supply chain, sandbox, atualização, licença, compatibilidade, auditoria e suporte.

### Opção D — packages declarativos sem código

Novos resources são descritos por primitivas do kernel.

**Vantagens:** segurança e portabilidade.  
**Limites:** expressividade limitada; pode fazer o kernel crescer para acomodar todas as primitivas.

### Recomendação para discussão

Começar conceitualmente com **A + B**: packages oficiais isolados, compilados e lazy-loaded. Projetar manifesto compatível com futura C, sem prometer marketplace ou código de terceiros.

## 11. Packages-base candidatos

### Kernel mínimo

- `resource-paragraph`;
- `resource-choice`;
- `resource-table`;
- `resource-code`;
- `resource-formula`;
- `resource-composite`;
- `practice-choice`;
- `practice-gap-choice`;
- feedback básico.

### Pacote estruturado inicial

- flow;
- tree;
- graph;
- matrix;
- plane;
- relation map.

### Pacotes disciplinares/avançados

- chart;
- sequence;
- annotated text;
- linguistic example;
- system map;
- reaction.

A divisão não é decisão de escopo; serve para comparar custo, alcance e dependências.

## 12. Compatibilidade entre packages

A compatibilidade deve ser explícita:

```text
ResourceDefinition
→ supported practices
→ supported response shapes
→ compatible validators
→ supported feedback modes
```

Não presumir que todo resource aceita toda prática. Um graph pode aceitar choice externo, seleção de vértice ou lacuna de label; uma fórmula pode aceitar lacunas em folhas; um paragraph pode aceitar texto ou choice. Essas capacidades pertencem ao package.

## 13. Estado e eventos

Packages não definem armazenamento. Eles devolvem eventos semânticos ao kernel:

- response changed;
- confirm requested;
- reveal requested;
- reset requested;
- annotation requested;
- resource action invoked.

O kernel aplica configuração, persiste estado e decide efeitos permitidos.

## 14. Acessibilidade

Todo package deve fornecer:

- nome e descrição acessível;
- ordem semântica;
- operação por teclado;
- alternativa não visual para estrutura espacial;
- status/feedback anunciado;
- reflow/zoom;
- limites de densidade;
- orientação de autoria para alt/accessibility text.

Um package sem fallback acessível não pode entrar no perfil-base.

## 15. MCP e packages

O GPT não recebe todos os schemas. Fluxo sugerido:

1. consulta catálogo compacto;
2. escolhe resources candidatos;
3. consulta contratos compactos dos escolhidos;
4. recebe contexto pedagógico;
5. produz somente dados;
6. kernel valida com packages;
7. ARA mostra preview e findings.

A ferramenta MCP é genérica por package capability, não uma ferramenta diferente por resource.

## 16. Atualização e migração

- conteúdo publicado referencia package ID e major/minor exigidos;
- snapshot offline registra versões instaladas;
- mudança compatível não reescreve conteúdo;
- mudança de schema exige migration pura e testável;
- package novo não altera snapshots antigos;
- retirada de package não apaga conteúdo; marca indisponibilidade e permite exportar;
- publicação deve recusar capability não suportada no destino.

## 17. Fronteira de confiança

### Packages internos oficiais

Podem executar código no app, após revisão e build.

### Packages externos

Não devem ser aceitos no primeiro modelo. Futuramente exigiriam assinatura, provenance, revisão, CSP, sandbox e revogação.

### Conteúdo de curso

Permanece data-only. Não importa package, não injeta script e não amplia permissões.

## 18. Estrutura de repositório candidata

```text
apps/
  web/
  android-wrapper/
packages/
  kernel-domain/
  kernel-config/
  kernel-runtime/
  kernel-authoring/
  kernel-ui/
  contracts/
  resource-paragraph/
  resource-table/
  resource-graph/
  practice-choice/
  adapter-local-indexeddb/
  adapter-supabase/
  adapter-mcp/
test-kits/
  resource-conformance/
  adapter-conformance/
  accessibility/
```

Essa árvore é ilustrativa. Monorepo, linguagem e tooling continuam alternativas a comparar.

## 19. Critérios para aceitar um novo resource

1. há tarefa educacional real não representada adequadamente;
2. a estrutura preservada é distinta de resources existentes;
3. conteúdo, prática e validator estão separados;
4. contrato autoral é produzível por humanos e LLM;
5. fallback acessível existe;
6. funciona ou falha explicitamente offline;
7. orçamento móvel é medido;
8. package não toca kernel;
9. fixtures e conformance existem;
10. custo de manutenção é aceito.

## 20. Questões abertas

- packages serão módulos TypeScript, Web Components ou view models sem framework?
- renderer retorna DOM, template, virtual tree ou custom element?
- como garantir isolamento de CSS?
- o package declara tokens semânticos próprios ou só usa tokens do kernel?
- as migrations de package operam dentro do pacote de curso ou no local store?
- como registrar packages instalados em snapshots de pesquisa?
- quais packages são obrigatórios em qualquer implantação ARA?
- instalação dinâmica é realmente necessária ou apenas uma possibilidade futura?
