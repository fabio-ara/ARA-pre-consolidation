# Alternativas de stack, arquitetura, BaaS e implantação

**Estado:** comparação não normativa  
**Data:** 3 de agosto de 2026  
**Regra:** limites e preços mudam; confirmar novamente antes de decidir ou implantar.

## 1. Critérios derivados do produto

Qualquer alternativa deve ser avaliada contra:

- estudo offline real;
- smartphone modesto;
- GitHub Pages ou outro host estático;
- app Android com a mesma experiência;
- conteúdo e composição versionados;
- autoria granular por GPT/MCP;
- resources extensíveis sem tocar no kernel;
- dados pessoais, conteúdo e pesquisa separados;
- armazenamento sustentável;
- implantação pessoal de baixo custo;
- caminho institucional e self-hosted possível;
- exportação e saída do fornecedor;
- acessibilidade e localização;
- baixa carga operacional para o proprietário.

## 2. Três topologias candidatas

### Topologia A — local-first com BaaS gerenciado

```text
PWA/app
├── banco local
├── packages/resources
└── sync/adapters
       ↓
BaaS gerenciado
├── auth
├── metadata/database
├── functions/API
└── object storage
```

**Vantagens:** menor operação, continuidade com AraLearn, autenticação e segurança prontas.  
**Riscos:** quotas, custos, lock-in operacional, funções específicas do fornecedor.

### Topologia B — local-first com backend próprio portátil

```text
PWA/app → API ARA → PostgreSQL + S3-compatible + OIDC
```

**Vantagens:** domínio e políticas controlados, múltiplos provedores, self-host.  
**Riscos:** maior implementação e operação; autenticação, email, backup e observabilidade deixam de ser terceirizados.

### Topologia C — personal/local-only primeiro

```text
PWA/app
├── local database
├── packages de curso
├── autoria local
└── export/import

sync e conta entram depois como capability
```

**Vantagens:** custo remoto mínimo, privacidade, uso imediato offline, kernel menor.  
**Riscos:** colaboração, recuperação e múltiplos dispositivos adiados; futura migração do estado local exige desenho antecipado.

### Leitura preliminar

O ARA pode combinar C no perfil pessoal e A/B nos perfis conectados. Não é necessário obrigar toda pessoa a usar o backend mais complexo.

## 3. Supabase

### Situação atual do AraLearn

O predecessor usa Supabase para Auth, PostgreSQL, RLS/PostgREST, RPCs, Edge Functions, Realtime/feeds e Storage. O funcionamento não é substituível hoje apenas trocando uma URL.

### Limites atuais do plano Free

A página oficial informa, entre outros:

- 500 MB de banco;
- 1 GB de file storage;
- 5 GB de egress e 5 GB de cached egress;
- 50.000 MAU;
- 500.000 invocações de Edge Functions;
- 2 milhões de mensagens Realtime;
- 200 conexões Realtime de pico;
- dois projetos ativos;
- pausa após uma semana de inatividade.

Fontes:

- [Supabase pricing](https://supabase.com/pricing)
- [Billing quotas](https://supabase.com/docs/guides/platform/billing-on-supabase)
- [Storage pricing](https://supabase.com/docs/guides/storage/pricing)

### Adequação ao ARA

**Pontos favoráveis**

- continuidade operacional;
- PostgreSQL e RLS adequados a relações e políticas;
- bom suporte a Auth, Storage e funções;
- ambiente local e migrations;
- fácil integração com host estático;
- caminho Pro previsível para projeto pequeno.

**Pontos críticos**

- 500 MB de banco exige não duplicar árvores e históricos sem limite;
- 1 GB de Storage exige deduplicação/assets controlados;
- pausa do Free afeta demonstrações esporádicas;
- Edge Functions e OAuth/MCP podem ampliar superfície de manutenção;
- domínio não pode depender de `auth.users`, RLS, RPC ou bucket;
- self-hosted Supabase completo tem carga operacional considerável.

### Tratamento candidato

Supabase pode ser o **primeiro adapter conectado**, porque o AraLearn oferece fixtures, migrations e conhecimento operacional. Não deve ser o contrato do kernel.

## 4. Firebase

O Firebase oferece Auth, Firestore, Storage, Functions e hosting integrados. O Spark possui quotas gratuitas para Firestore e outros serviços; ao exceder certas quotas gratuitas, operações podem ser recusadas até a renovação do ciclo, dependendo do produto.

Fontes oficiais:

- [Firebase pricing](https://firebase.google.com/pricing)
- [Firestore pricing](https://firebase.google.com/docs/firestore/pricing)

### Pontos favoráveis

- ecossistema móvel maduro;
- SDKs e offline do Firestore;
- autenticação e hosting integrados;
- baixa operação inicial.

### Pontos críticos

- modelo documental e cobrança por operações podem ser ruins para grafos/entidades finas e consultas administrativas;
- relações e policies complexas diferem do modelo PostgreSQL;
- exportação/portabilidade e self-hosting são mais fracos;
- Edge/Cloud Functions e rules constituem outra forma de lock-in;
- não resolve por si só a separação entre artefatos imutáveis e composição.

### Leitura candidata

É opção tecnicamente possível, mas a migração do domínio relacional atual seria profunda. Não parece a primeira alternativa a Supabase sem um benefício móvel específico demonstrado.

## 5. Appwrite

O Appwrite oferece Databases, Authentication, Storage, Functions, Messaging e Sites em cloud ou self-hosted. O plano Free atual informa 5 GB de bandwidth, 2 GB de storage, 75 mil MAU, uma database, um bucket e duas functions por projeto, com pausa após uma semana de inatividade.

Fontes:

- [Appwrite pricing](https://appwrite.io/pricing)
- [Free function limit](https://appwrite.io/changelog/entry/2026-01-08)

### Pontos favoráveis

- conjunto integrado semelhante a BaaS;
- storage gratuito maior que Supabase;
- opção self-hosted;
- sites e messaging no ecossistema;
- SDKs multiplataforma.

### Pontos críticos

- somente uma database, um bucket e duas functions no Free podem restringir separações desejadas;
- modelo de banco e queries precisa ser confrontado com relações/versões;
- migrar RLS/RPCs/SQL exige nova política;
- self-host transfere operação ao projeto;
- quotas e mudanças recentes mostram que free tier não deve governar domínio.

### Leitura candidata

Merece spike comparativo quando a arquitetura for discutida, especialmente se storage e self-host forem prioritários. Não deve ser escolhido apenas por quota maior.

## 6. Nhost

Nhost combina PostgreSQL, Hasura GraphQL, Authentication, Storage/MinIO, Functions e email. A CLI executa stack local por Docker com migrations e metadata.

Fontes:

- [Local development](https://docs.nhost.io/platform/cli/local-development)
- [Networking and services](https://docs.nhost.io/products/run/networking)

### Pontos favoráveis

- PostgreSQL preserva proximidade com o domínio atual;
- GraphQL/Hasura pode reduzir API repetitiva;
- Auth, Storage e Functions integrados;
- desenvolvimento local e self-host possível;
- metadata e migrations versionáveis.

### Pontos críticos

- operação de Hasura/Auth/Storage é relevante;
- permissions do Hasura não são RLS idêntico;
- GraphQL pode expor estrutura de persistência se não houver application layer;
- documentação/preços cloud precisam ser reverificados no momento da decisão;
- ecossistema menor que Firebase/Supabase.

### Leitura candidata

Alternativa próxima ao stack relacional do AraLearn. Adequada para uma prova de portabilidade de adapter, não para alterar o domínio.

## 7. PocketBase

PocketBase é um backend open-source em um único executável, com banco embutido, auth, files, realtime e API. Sua documentação posiciona-o para aplicações pequenas/médias em um servidor e enfatiza scale-up vertical.

Fontes oficiais:

- [PocketBase FAQ](https://pocketbase.io/faq/)
- [Production guide](https://pocketbase.io/docs/going-to-production/)

### Pontos favoráveis

- operação muito simples;
- baixo custo para uso pessoal/demonstração;
- portátil e self-hosted;
- bom para protótipo ou implantação pequena.

### Pontos críticos

- não é BaaS cloud gerenciado completo por padrão;
- single-node/SQLite não atende todos os cenários institucionais;
- functions, email, backups e HA exigem operação própria;
- migração do PostgreSQL/RLS não é direta;
- não deve virar teto arquitetural do produto.

### Leitura candidata

Pode ser adapter pessoal/self-host leve ou ambiente de demonstração. Não deve definir o perfil institucional.

## 8. Backend próprio: PostgreSQL + S3 + OIDC

Componentes possíveis:

- PostgreSQL gerenciado por qualquer provedor;
- object storage S3-compatible;
- OIDC externo;
- API própria;
- jobs/queues mínimos;
- host estático para PWA.

### Pontos favoráveis

- maior independência;
- ports claros;
- escolha separada de cada serviço;
- self-host e managed usam mesma semântica;
- facilita testes de conformidade.

### Pontos críticos

- maior volume de código e operação;
- email/transações/auth/backup/logs precisam de solução;
- risco de construir um BaaS próprio;
- custo pode superar o benefício para o primeiro corte.

### Leitura candidata

É uma arquitetura de referência importante, mas talvez não o primeiro deployment real. O kernel deve permitir essa saída mesmo que Supabase seja usado primeiro.

## 9. Local store

### IndexedDB direto

**Continuidade:** AraLearn já demonstra viabilidade.  
**Vantagens:** nativo no browser, zero dependência.  
**Limites:** API complexa, migrations e transações exigem disciplina, queries reativas precisam de camada própria.

### Dexie

Wrapper popular para IndexedDB com schema, transactions e observability.

**Questão:** dependência pequena pode reduzir código sem definir sync.

### RxDB

Banco local-first JavaScript que usa IndexedDB/OPFS e oferece replicação com backends diversos. A documentação enfatiza leitura/escrita local, multi-tab e protocolo de replication compatível com backends customizados.

Fontes:

- [Offline first](https://rxdb.info/offline-first.html)
- [Replication](https://rxdb.info/replication.html)

**Vantagens:** reatividade e sync genérico.  
**Riscos:** bundle, licença de plugins/performance, complexidade e modelo documental.

### SQLite/OPFS

Possível no browser moderno ou wrapper nativo.

**Vantagens:** SQL, consistência e portabilidade com app.  
**Riscos:** WASM/OPFS, bundle, compatibilidade, worker e custo no smartphone.

### PGlite

PostgreSQL/WASM no browser pode alinhar semântica relacional.

**Riscos:** peso, memória, startup e maturidade para device modesto precisam de medição.

### Decisão candidata

Não escolher por elegância. Comparar IndexedDB/Dexie com SQLite/OPFS em fixtures reais de curso, autoria, busca e sync no Galaxy A07-class.

## 10. Sync

### Protocolo específico ARA

Evolução do AraLearn: cursor/feed/outbox/request ID/expected revision.

**Vantagens:** sem dependência, semântica sob controle.  
**Riscos:** conflito, partial sync e manutenção são difíceis.

### PowerSync

Mantém SQLite local sincronizado com backend e separa leitura replicada de upload via API do aplicativo. Oferece checkpoints e consistency model.

Fontes:

- [Overview](https://docs.powersync.com/intro/powersync-overview)
- [Client architecture](https://docs.powersync.com/architecture/client-architecture)
- [Consistency](https://docs.powersync.com/architecture/consistency)

**Vantagens:** local-first pronto, partial sync, retry.  
**Riscos:** serviço adicional, SQLite obrigatório, custo/licença/hosting e adequação a artefatos precisam ser avaliados.

### RxDB replication

Cliente implementa pull/push/checkpoint e pode usar backend diverso.

**Vantagens:** flexibilidade.  
**Riscos:** conflito e modelo documental; parte complexa migra para biblioteca cliente.

### Sem sync genérico no primeiro perfil

Conteúdo por package download; estado export/import; sync entra depois.

**Vantagens:** reduz enorme risco inicial.  
**Riscos:** múltiplos dispositivos e recuperação ficam limitados.

### Regra de produto

Qualquer engine deve respeitar operações semânticas de autoria. CRDT/LWW não pode mesclar silenciosamente conteúdo pedagógico ou configuração de pesquisa.

## 11. Hosting web

### GitHub Pages

**Vantagens:** gratuito, já usado, simples, transparente.  
**Limites:** somente estático; runtime config e callbacks; cache/service worker; repositório público; domínio e deploy separados do backend.

### Cloudflare Pages, Netlify ou Vercel

Podem oferecer previews e functions, mas adicionam fornecedores e limites próprios.

### Servidor estático institucional

Mantém artefato igual e exige HTTPS, MIME, cache, CSP e callbacks corretos.

### Direção candidata

Preservar build estático provider-neutral. GitHub Pages permanece implantação de demonstração, não requisito do domínio.

## 12. Web e Android

### PWA instalável

Web App Manifest, Service Worker e Cache Storage oferecem instalação e offline. É o baseline mais simples e mantém uma aplicação.

Fonte: [web.dev — Learn PWA](https://web.dev/learn/pwa/welcome).

### Trusted Web Activity

O Android executa a PWA em tela cheia pelo navegador e verifica relação com o site por Digital Asset Links. Reduz tamanho do app, mas o wrapper não controla diretamente estado web.

Fonte: [Android — Trusted Web Activities](https://developer.android.com/develop/ui/views/layout/webapps/trusted-web-activities?hl=pt-BR).

### Capacitor

Runtime nativo web-first que permite plugins e acesso a SDKs Android/iOS.

Fonte: [Capacitor documentation](https://capacitorjs.com/docs).

**Vantagens:** filesystem, notifications e SQLite nativo.  
**Riscos:** projeto nativo, plugins, builds e divergência de comportamento.

### Alternativa candidata

- PWA como produto canônico;
- TWA/PWABuilder para wrapper mínimo quando suficiente;
- Capacitor somente se uma necessidade nativa demonstrada justificar.

## 13. Framework de UI

### Vanilla ESM/Web Components

**Continuidade:** AraLearn atual.  
**Vantagens:** baixo overhead e controle.  
**Riscos:** orquestração manual, arquivos centrais grandes, forms/state complexos.

### React + TypeScript

**Vantagens:** ecossistema, componentes, testabilidade, dynamic imports.  
**Riscos:** bundle e tendência a concentrar state em componentes; framework churn.

### Vue/Svelte

Podem reduzir boilerplate e bundle, mas trazem outro ecossistema.

### Web Components + framework shell

Packages de resource podem expor custom elements; shell usa framework.

**Riscos:** forms/context/state e SSR não são triviais; shadow DOM/accessibility/CSS exigem cuidado.

### Direção candidata

Escolher depois de um spike com três telas e dois resources, medindo:

- bundle/startup;
- ergonomia de package;
- forms e state machines;
- accessibility;
- testes;
- integração com IndexedDB;
- aprendizado/manutenção pelo proprietário.

## 14. Estratégias de armazenamento econômico

- conteúdo imutável por hash;
- assets deduplicados por digest;
- metadata pequena no banco;
- curso como manifesto de referências;
- snapshots materializados somente para publicação/offline;
- garbage collection por referências e retenção;
- previews parciais com prazo/limite;
- histórico de operações resumido, não cópia integral;
- comentários sem cópia do card;
- analytics opt-in e agregação limitada;
- compressão de JSON e imagens;
- budgets por package/course;
- export e remoção claros.

## 15. Matriz resumida

| Alternativa | Operação inicial | Portabilidade | Relações | Offline | Self-host | Principal risco |
|---|---|---|---|---|---|---|
| Supabase | baixa | média | forte/Postgres | exige camada local | possível/complexo | lock-in operacional e quotas |
| Firebase | baixa | baixa–média | documental | SDK forte | não equivalente | cobrança por operação e remodelagem |
| Appwrite | baixa–média | média | banco próprio | exige camada local | sim | limites Free e modelo a validar |
| Nhost | média | média–alta | Postgres/GraphQL | exige camada local | sim | operação Hasura/stack |
| PocketBase | média | alta no pequeno | SQLite | exige camada local | sim | escala/HA/operação |
| Backend próprio | alta | alta | escolhida | escolhida | sim | construir/operação excessiva |
| Local-only | muito baixa remota | alta | local | máxima | n/a | sem colaboração/recuperação |

Registro estruturado: `research/data/ara-technology-options-v1.csv`.

## 16. Sequência de decisão futura

Quando o projeto entrar em fase técnica, comparar nesta ordem:

1. perfil pessoal local-only versus conta obrigatória;
2. store local em fixture real;
3. package/artifact format;
4. sync necessário para o primeiro produto;
5. adapter Supabase mínimo;
6. adapter alternativo de prova de portabilidade;
7. wrapper Android;
8. framework de UI e package loading.

## 17. Hipótese de primeira implantação, sem decisão

Uma combinação de baixo risco para prototipagem futura seria:

```text
PWA estática
+ kernel/data-only packages
+ IndexedDB ou wrapper pequeno
+ artifacts imutáveis
+ adapter Supabase aproveitando conhecimento atual
+ modo pessoal local sem depender de LLM
```

A hipótese deve ser comparada com:

```text
PWA + SQLite/PowerSync + PostgreSQL/S3/OIDC
```

e com:

```text
PWA local-only + export/import, conexão adiada
```

Nenhuma é escolhida neste rascunho.
