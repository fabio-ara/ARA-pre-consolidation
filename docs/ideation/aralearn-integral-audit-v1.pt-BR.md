# Auditoria integral do AraLearn como predecessor do ARA

**Estado:** rascunho analítico para discussão  
**Objeto examinado:** `fabio-ara/AraLearn`, branch `main`, versão declarada `0.0.14`  
**Commit de corte:** `9bff37eee3ba80263084328dc5897d26c7ca3d5a`  
**Data:** 3 de agosto de 2026

## 1. Pergunta da auditoria

O AraLearn atual deve ser tratado como:

1. produto descartável a ser substituído;
2. código a ser simplesmente renomeado e ampliado; ou
3. predecessor funcional cuja experiência, contratos, regras e testes orientam uma reconstrução modular?

A conclusão preliminar é a terceira. O AraLearn já resolve problemas centrais do futuro ARA, mas sua organização física cresceu por sucessivas ampliações e não deve ser reproduzida sem revisão.

## 2. Método

Foram examinados:

- README, guias por público e estado atual;
- contrato público v4 e catálogo de resources;
- arquitetura, persistência relacional, sincronização e implantação;
- gateway MCP, Action e fluxos de autoria;
- registro de resources, renderer e orquestrador principal da UI;
- scripts e dependências declarados em `package.json`;
- auditoria do front-end, refatoração dos resources e referências à suíte de testes;
- commits recentes do ramo principal.

A documentação foi confrontada com arquivos centrais do código. Quando uma capacidade aparece somente na documentação, ela não é tomada automaticamente como implementação comprovada; quando há código, contrato e teste associados, a confiança é maior.

## 3. Síntese do produto atual

O AraLearn é uma aplicação JavaScript única distribuída na web e em APK Android. Seu caminho pedagógico é:

```text
projeto → curso → módulo → lição → microssequência → card
```

O produto oferece atualmente:

- autenticação por conta;
- catálogo oficial e coleções;
- biblioteca pessoal organizada em Trilhas;
- download e estudo offline;
- retomada, conclusão estrutural, marca **Rever** e observações situadas;
- sincronização de estado pessoal;
- importação e exportação JSON v4;
- leitura e edição contextual no mesmo card;
- assistência atômica por API para cards e resources;
- autoria extensa por GPT externo via MCP ou Action;
- workspaces educacionais, papéis locais e fluxo editorial;
- publicações imutáveis no Storage;
- dezoito resources declarativos;
- publicação web estática e empacotamento Android.

Fontes primárias:

- [README](https://github.com/fabio-ara/AraLearn/blob/main/README.md)
- [Estado atual e roadmap](https://github.com/fabio-ara/AraLearn/blob/main/docs/estado-atual-e-roadmap.md)
- [Uso do app](https://github.com/fabio-ara/AraLearn/blob/main/docs/uso-do-app.md)

## 4. Experiência funcional que forma o esqueleto do ARA

### 4.1 Estudo em microssequências

O card permanece a superfície de leitura e prática. As microssequências oferecem contexto menor que uma lição inteira e maior que um card isolado. A navegação ordenada, a retomada e a possibilidade de revisão localizada são coerentes com o público trabalhador-estudante e com uso móvel interrompível.

**Decisão candidata:** preservar a experiência, mas não presumir que toda microssequência pertença fisicamente a um único curso.

### 4.2 Conteúdo declarativo e estudo determinístico

A LLM produz dados semânticos. O aplicativo valida, calcula geometria, renderiza, recebe resposta, avalia e apresenta feedback. Conteúdo de curso não fornece JavaScript, HTML arbitrário ou validator executável.

Esse limite é uma das decisões mais importantes do predecessor. Ele reduz risco, permite funcionamento offline, mantém comportamento testável e diminui dependência da disponibilidade de uma LLM.

**Decisão candidata:** preservar como regra do kernel.

### 4.3 Estado de estudo não punitivo

O estado pessoal deliberadamente não registra abertura, tempo, número de tentativas ou resultado. Mantém cursor, conclusão estrutural, marca de revisão e observação. Essa opção reduz vigilância, armazenamento e interpretações indevidas.

**Decisão candidata:** preservar como perfil de referência, sem impedir protocolos de pesquisa explicitamente autorizados.

### 4.4 Local-first pragmático

A mudança ocorre primeiro no dispositivo e sincroniza depois. O curso publicado é baixado, validado e projetado no IndexedDB. Falhas de rede não impedem o estudo; atualizações inválidas não substituem a revisão funcional anterior.

**Decisão candidata:** preservar o princípio e reavaliar a tecnologia/protocolo.

### 4.5 Autoria humano–IA em rodadas

O gateway MCP sustenta planejamento, construção, auditoria, reparo e reauditoria como papéis/rodadas distintos. O mesmo backend atende Plugin e Action. O modelo não recebe acesso direto a tabelas ou credenciais administrativas.

**Decisão candidata:** preservar a fronteira de aplicação e tornar o estado das operações muito mais visível no ARA.

### 4.6 Revisões imutáveis e publicação explícita

O workspace é mutável; a publicação é composta, validada, canonicalizada, identificada por hash e gravada como artefato imutável. Atualizar troca um ponteiro, em vez de editar o artefato publicado.

**Decisão candidata:** preservar, estendendo a lógica a unidades reutilizáveis e snapshots de composição.

### 4.7 Observação situada

A observação pertence ao card exato e pode ser triada por pessoas autorizadas no workspace. Responder, corrigir e encerrar são operações distintas.

**Decisão candidata:** preservar e generalizar o alvo para card, resource, microssequência, placement, dependência, configuração e versão.

## 5. Arquitetura atual

A documentação descreve três planos principais:

```text
PostgreSQL/Supabase
- autenticação, autorização e metadados
- estado pessoal e feeds de sincronização
- workspace mutável composto por entidades

Supabase Storage
- revisões JSON publicadas e imutáveis
- assets e artefatos

IndexedDB
- projeção relacional por conta/dispositivo
- curso materializado para estudo
- estado pessoal, outbox e rascunho local
```

A publicação integral do curso não é duplicada como segunda árvore relacional remota. O workspace, por sua vez, mantém linhas correntes para os níveis da hierarquia. O dispositivo projeta o documento para navegação e estudo.

Fonte: [Arquitetura](https://github.com/fabio-ara/AraLearn/blob/main/docs/arquitetura.md) e [Persistência relacional](https://github.com/fabio-ara/AraLearn/blob/main/docs/persistencia-relacional.md).

### 5.1 Pontos fortes

- separação entre autoria mutável e publicação imutável;
- download por hash e troca atômica;
- idempotência por `requestId`;
- concorrência otimista por `expectedRevision`;
- separação entre conteúdo e estado pessoal;
- réplica local por UUID de conta;
- falhas classificadas e trabalho offline preservado;
- ausência de chave administrativa no cliente;
- uso de RLS e funções transacionais.

### 5.2 Limites para o ARA

- o contrato operacional depende diretamente de Auth, RLS, PostgREST, RPCs, Edge Functions e Storage do Supabase;
- não existe adapter de conformidade para outro BaaS;
- a autoria remota é relacional por entidade, enquanto a unidade reutilizável proposta ainda não é um objeto de domínio próprio;
- a publicação é principalmente centrada no curso completo;
- o protocolo de sync foi construído especificamente para o conjunto atual de tabelas e ações;
- a conta é requisito para abrir a aplicação, embora um futuro perfil pessoal local possa dispensá-la;
- o painel do usuário não revela de modo simples os artefatos, referências, versões, placements e efeitos no armazenamento.

## 6. Contrato de conteúdo

O `aralearn.contract` v4 é uma contribuição relevante. Ele inclui:

- fronteiras de módulo e lição por `guide`;
- tópicos estruturados com tipos, checks e erros plausíveis;
- microssequências com objetivo, papel, estado, dependências, cobertura e checks;
- cards com identidade, posição, resource, tipo pedagógico e mecânica de exercício;
- fontes e tags;
- campos fechados e rejeição de desconhecidos;
- round-trip e publicação canônica.

Fonte: [Contrato público](https://github.com/fabio-ara/AraLearn/blob/main/docs/aralearn-contract.md).

### 6.1 O que preservar

- IDs estáveis;
- schemas fechados e versionados;
- conteúdo sem geometria de apresentação;
- separação entre resource e mecânica de resposta;
- fronteiras pedagógicas locais;
- fontes e proveniência;
- rejeição explícita de campos desconhecidos.

### 6.2 O que reformular

- `dependsOn` limita-se a microssequências da mesma lição;
- `card.topics` ainda admite tags livres sem referência estruturada;
- a árvore pública faz o card pertencer diretamente à microssequência e a microssequência pertencer ao curso, sem placement reutilizável;
- o documento integral carrega conteúdo e composição juntos;
- parâmetros de runtime, autoria, composição e pesquisa não estão separados em snapshots próprios;
- reuse, fork, adaptation, translation e supersession não são relações de primeira classe no contrato público.

## 7. Sistema de resources

O AraLearn possui 18 resources:

`paragraph`, `choice`, `composite`, `code`, `table`, `flow`, `tree`, `graph`, `relation_map`, `matrix`, `plane`, `formula`, `chart`, `sequence`, `annotated_text`, `linguistic_example`, `system_map` e `reaction`.

O registro canônico contém IDs, labels, schemas, capacidades, limites, exemplos, contratos de autoria e validadores. O domínio deriva sua lista desse registro. O renderer fica conceitualmente separado e há testes de cobertura entre contrato, runtime, autoria e Edge.

Fontes:

- [Recursos de card](https://github.com/fabio-ara/AraLearn/blob/main/docs/recursos-de-card.md)
- [Refatoração do sistema](https://github.com/fabio-ara/AraLearn/blob/main/docs/resource-system-refactor.md)
- [`src/resources/registry/index.js`](https://github.com/fabio-ara/AraLearn/blob/main/src/resources/registry/index.js)
- [`src/render/renderCardRuntime.js`](https://github.com/fabio-ara/AraLearn/blob/main/src/render/renderCardRuntime.js)

### 7.1 Contribuições a preservar

- resource representa estrutura cognitiva, não apenas aparência;
- gap e choice são mecânicas, não uma taxonomia paralela de resources;
- LLM envia semântica e IDs; layout pertence ao renderer;
- cada resource declara alvos permitidos de autoria e prática;
- schema integral permanece canônico mesmo quando o MCP transporta uma visão compacta;
- alternativas podem variar entre 2 e 7 conforme distratores funcionais;
- `composite` exige IDs estáveis nos blocos;
- accessibility text e representações alternativas fazem parte do contrato.

### 7.2 Problema físico atual

Embora exista um registro central, grande parte do catálogo, schemas e validadores converge em `src/resources/registry/index.js`. O renderer de todos os resources converge em `src/render/renderCardRuntime.js`. Alterar um resource pode exigir tocar em arquivos centrais compartilhados e ampliar bundles comuns.

Isso é diferente de uma arquitetura realmente extensível. No ARA, adicionar um resource deve ocorrer principalmente dentro de um package isolado, com testes e manifesto próprios, sem modificar o kernel nem um switch/registry monolítico.

## 8. UI e controle do usuário

O AraLearn passou por grande evolução visual. A Central, os modos Ler/Editar, os overlays e os tokens reduziram resíduos e melhoraram a coerência. A auditoria corrente registra ampla cobertura automatizada.

Fonte: [Auditoria do front-end](https://github.com/fabio-ara/AraLearn/blob/main/docs/auditoria-front-end.md).

### 8.1 Valor preservável

- card como superfície principal;
- uma ação primária por vez no mobile;
- Central orientada a “onde está cada coisa?”;
- nomes amigáveis como Coleções, Trilhas e Rever;
- edição contextual e prévia antes de aplicar;
- indicação de trabalho local e atualização remota;
- estados de falha sem apagar trabalho;
- tema claro/escuro e ícones SVG.

### 8.2 Concentração a evitar

`src/ui/lessonEditorApp.js` orquestra navegação, renderização, overlays, edição manual, assistência por IA, providers, anexos, importação, progresso, comentários, estrutura e persistência. Mesmo dividido em auxiliares, funciona como um coordenador excessivamente amplo.

`public/styles.css`, embora auditado e sem resíduos detectados, ainda é um arquivo muito grande. O tamanho não é defeito isolado; o risco é a dificuldade de atribuir estilos e estados a packages independentes.

### 8.3 Lacuna principal para o ARA

O usuário precisa enxergar e controlar:

- versão do curso e das microssequências;
- origem e relation (`reference`, `copy`, `fork`, `adaptation`);
- placements e dependências;
- parâmetros herdados e overrides;
- operações do GPT/MCP em andamento;
- findings, comentários e reparos;
- efeitos de publicar, retirar, atualizar e excluir;
- armazenamento local/remoto e sincronização;
- diferenças entre variantes.

Essas informações devem aparecer em linguagem pedagógica e operacional, não como tabelas, hashes e nomes internos.

## 9. Autoria local, MCP e providers

O AraLearn distingue assistência atômica no card e autoria estrutural extensa pelo MCP. Essa distinção é útil, mas a implementação local combina muitas responsabilidades na mesma aplicação.

O MCP atual é um gateway delimitado com OAuth 2.1, ferramentas fechadas, contexto paginado, consultas compactas de resources, expected revision, request ID e publicação explícita.

Fonte: [Gateway MCP](https://github.com/fabio-ara/AraLearn/blob/main/docs/autoria-mcp.md).

### 9.1 Preservar

- gateway de aplicação, nunca acesso direto a banco/Storage;
- ferramentas pequenas e semanticamente nomeadas;
- consulta de contratos sob demanda;
- leitura menor antes de conteúdo integral;
- idempotência e concorrência otimista;
- separação de audit e repair;
- saída persistida e visível no app;
- mesma autoridade para Plugin e Action;
- provenance de fontes, agente e operação.

### 9.2 Reformular

- tornar a microssequência/revisão/placement um alvo explícito de primeira classe;
- registrar operações como objetos visíveis, retomáveis e auditáveis;
- separar packages de provider da aplicação principal;
- impedir que a lista de ferramentas cresça por duplicação de cada resource;
- usar capability discovery e contratos versionados;
- permitir que a pessoa escolha, no ARA, alvo, versão, escopo e decisão final;
- separar claramente pedido de conteúdo, parâmetro transformador e alteração apenas de runtime.

## 10. Testes e confiabilidade observável

O repositório possui scripts e testes para:

- contrato e round-trip;
- resources e cenários disciplinares;
- assistência atômica e providers;
- persistência, IndexedDB e sync;
- Supabase local, RLS, Auth, PostgREST e Edge Functions;
- MCP local/hosted/OAuth;
- E2E e capturas de galeria;
- auditoria de CSS, documentos e implantação;
- build de Pages e Android.

O estado documentado menciona 1.007 testes de código e 60 jornadas E2E no recorte corrente. Esses números são fotografia de uma versão, não garantia permanente.

**Decisão candidata:** preservar fixtures e invariantes como patrimônio migrável, sem transportar obrigatoriamente a estrutura de testes ou o stack.

## 11. Acoplamentos e dívidas relevantes

### 11.1 Acoplamento de implantação

Supabase não é apenas banco; fornece autenticação, RLS, API, funções e Storage. Trocar de BaaS hoje significaria reconstruir contratos operacionais.

### 11.2 Acoplamento físico dos resources

Registro e renderer são conceitualmente corretos, mas fisicamente centralizados. Um package por resource ainda não existe.

### 11.3 Orquestradores grandes

Startup, sincronização e UI reúnem muitos fluxos numa superfície central. Isso aumenta a chance de uma nova capacidade tocar caminhos antigos.

### 11.4 Conteúdo e composição unidos

O JSON publicado descreve toda a árvore. Não há manifesto separado que componha revisões reutilizáveis de microssequências.

### 11.5 Dependências insuficientes

Há IDs e DAG local, mas não um grafo tipado entre unidades, conceitos e cursos. Tags livres não podem sustentar orquestração, impacto ou reutilização confiável.

### 11.6 Visibilidade abaixo da complexidade do backend

O backend já distingue vários objetos e estados. A interface os resume ou oculta. O ARA nasce justamente para reduzir essa assimetria.

### 11.7 Crescimento por incorporação ao produto principal

Cada novo resource, provider, overlay ou fluxo pode aumentar o bundle e arquivos centrais. O ARA precisa de instalação/registro de capability sem crescimento silencioso do kernel.

## 12. Matriz de decisão preliminar

| Área | Tratamento proposto |
|---|---|
| hierarquia pedagógica | preservar como visão inicial |
| microssequência | preservar e promover a unidade versionada candidata |
| card | preservar como unidade de apresentação/interação |
| contrato JSON fechado | preservar e decompor em contratos menores |
| 18 resources | preservar como corpus de referência, não todos obrigatórios no kernel |
| resource semantic data | preservar |
| registry monolítico | separar em manifests/packages |
| renderer monolítico | separar por resource package |
| estudo offline | preservar |
| IndexedDB atual | alternativa a comparar |
| sync específico | reformular atrás de port |
| Supabase | manter como adapter candidato, não como domínio |
| conta obrigatória | questão aberta; considerar perfil local sem conta |
| estado não punitivo | preservar como perfil de referência |
| autoria local atômica | preservar finalidade e simplificar |
| MCP/OAuth | preservar fronteira; reavaliar stack e ferramentas |
| workspace | preservar finalidade |
| publicação imutável | preservar |
| curso integral no Storage | reformular com composição e snapshots |
| comentários situados | preservar e ampliar alvos |
| Coleções/Trilhas | preservar linguagem, revisar domínio |
| Central | preservar princípio, redesenhar para versões/parâmetros/artefatos |
| catálogo editorial | adiar ao escopo adequado, sem descartá-lo |
| analytics comportamental | rejeitar como padrão |

O registro detalhado está em `research/data/aralearn-capability-preservation-matrix-v1.csv`.

## 13. Riscos de simplesmente copiar o AraLearn

1. carregar para o ARA arquivos centrais já muito amplos;
2. manter a extensão de resources dependente de edições no kernel;
3. vincular o domínio a Supabase e a quotas de um fornecedor;
4. manter conteúdo reutilizável preso ao curso integral;
5. perpetuar tags livres como substituto de dependências;
6. transportar funções avançadas antes de definir o produto-base;
7. manter dois fluxos de autoria difíceis de compreender;
8. confundir cobertura automatizada existente com validação da nova arquitetura;
9. reconstruir um LMS amplo em vez de uma ferramenta focada;
10. ocultar novamente do usuário a complexidade criada no backend.

## 14. Riscos de ignorar o AraLearn

1. perder contratos e invariantes já testados;
2. reabrir decisões pedagógicas resolvidas;
3. reconstruir incorretamente offline, sync e publicação;
4. repetir erros de fields desconhecidos, IDs instáveis e mutações laterais;
5. perder o fluxo de autoria humano–IA já observado em uso;
6. desconsiderar recursos visuais especializados;
7. remover a continuidade perceptível que define o ARA como sucessor.

## 15. Conclusão

O AraLearn deve fornecer ao ARA:

- experiência de estudo e autoria;
- linguagem do produto;
- contratos semânticos;
- fixtures e invariantes;
- casos de falha;
- operações de MCP;
- decisões de privacidade e estado;
- corpus dos resources;
- evidência de limites de UI, Supabase e crescimento do código.

O ARA, por sua vez, deve reconstruir:

- fronteiras físicas dos módulos;
- kernel mínimo;
- packages de resource/capability;
- composição e reutilização de microssequências;
- resolução de parâmetros;
- visibilidade de versões, artefatos e operações;
- ports para persistência, sync, identidade, assets e LLM;
- experiência progressiva por perfil.

A relação proposta é:

```text
AraLearn funcional e testado
→ extração de semântica, contratos, fixtures e jornadas
→ kernel menor e estável
→ packages independentes
→ adapters substituíveis
→ ARA configurável e observável
```
