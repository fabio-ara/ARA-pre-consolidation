# Versionamento, armazenamento sustentável e economia operacional

**Estado:** síntese técnica inicial para discussão; não normativa  
**Data:** 4 de agosto de 2026  
**Relação com o AraLearn:** usa suas limitações como contraste; não presume migração nem equivalência técnica.  
**Regra:** preços e quotas devem ser reverificados antes de qualquer decisão.

## 1. Correção de premissa sobre o AraLearn

O AraLearn não possui uma versão monolítica equivalente da arquitetura modular pretendida pelo ARA. Portanto, não é correto exigir que fixtures “reproduzam” a configuração atual como se os dois produtos tivessem o mesmo objeto ou comportamento interno.

O predecessor serve para:

- mostrar jornadas que funcionam e não devem regredir silenciosamente;
- registrar problemas observados com configuração monolítica;
- identificar acoplamentos entre instruções, knowledge, contracts e tools;
- fornecer exemplos de operações reais de planejamento, construção, auditoria e reparo;
- evidenciar limitações de banco, Storage, sync e interface;
- oferecer casos de contraste, não uma especificação completa do ARA.

Os evals futuros devem ser construídos principalmente a partir de **tarefas-alvo do ARA, casos controlados e falhas representativas**, podendo incorporar jornadas observadas no AraLearn quando forem pertinentes. Não devem alegar paridade de uma arquitetura que ainda não existe.

## 2. Por que o versionamento amplia o problema de armazenamento

O ARA pretende versionar:

- microssequências e cards;
- composição de cursos;
- configurações e condições experimentais;
- perfis de agente;
- instruções, templates e knowledge snapshots;
- operações do GPT/MCP;
- diffs, findings, observações e reparos;
- datasets, instrumentos e execuções de análise.

Se cada revisão duplicar árvores inteiras, o custo crescerá rapidamente. O modelo precisa favorecer referências, imutabilidade, deduplicação e materialização somente quando necessária.

## 3. Separação candidata

```text
Metadata repository
- IDs, lineages, revision pointers, relações, placements, permissões e índices

Artifact repository
- JSON imutável, assets, snapshots, exports, evidence packages e payloads grandes

Local store
- curso materializado, estado pessoal, drafts, outbox e cache
```

Essa separação permite que o banco relacional mantenha entidades pequenas e consultáveis enquanto o object storage recebe dezenas ou centenas de milhares de objetos imutáveis.

Ela não é decisão final. Deve ser comparada com BaaS integrado e perfil local-only.

## 4. Modelo de fragmentos e referências

Um curso variante não precisa duplicar todas as microssequências.

```text
CourseVersion A
├── MS01-r3
├── MS02-r1
├── MS03-r4
└── MS04-r2

CourseVersion B
├── MS01-r3   compartilhada
├── MS02-r1   compartilhada
├── MS03B-r1  derivada
└── MS04-r2   compartilhada
```

O manifesto da versão contém referências e configuração efetiva. Uma revisão alterada cria novo artefato; as demais permanecem compartilhadas.

## 5. Content addressing e deduplicação

Hipótese candidata:

1. canonicalizar o payload;
2. calcular digest;
3. verificar se o artefato já existe;
4. armazenar somente quando novo;
5. registrar referência e proveniência;
6. materializar pacote de estudo/publicação quando necessário.

Isso pode reduzir duplicação, mas não substitui versionamento semântico. Dois artefatos idênticos podem participar de contextos pedagógicos diferentes; o estado pessoal e o placement permanecem contextuais.

## 6. Retenção e garbage collection

Nem toda revisão pode ser apagada pelo mesmo critério.

Classes candidatas:

- **ativa:** referenciada por workspace ou curso corrente;
- **publicada:** imutável e retida enquanto a publicação existir;
- **research-locked:** retida pelo protocolo;
- **rollback:** retida por janela configurada;
- **superseded:** sem novos acessos, mas ainda referenciada;
- **orphan candidate:** sem referência e fora das janelas;
- **exported-only:** removível do deployment após exportação validada, se autorizado.

Garbage collection deve operar por referência, retenção e decisão, nunca por idade isolada.

## 7. Fotografia atual das alternativas

### Supabase Free

- 500 MB de banco;
- 1 GB de file storage;
- projetos sujeitos a pausa por baixa atividade;
- restauração possível por período limitado;
- dois projetos ativos gratuitos.

É útil para desenvolvimento e uso pequeno, mas não garante disponibilidade permanente nem espaço confortável para histórico crescente.

### Supabase Pro

- a partir de USD 25/mês;
- 8 GB de disco de banco incluído;
- 100 GB de file storage;
- sem pausa automática por inatividade;
- backups diários por sete dias.

Pode ser suficiente para a primeira implantação conectada, especialmente porque o AraLearn já oferece experiência operacional. Isso não elimina a necessidade de adapter, exportação e simulação de carga.

### Cloudflare R2

- 10 GB-mês gratuitos;
- preço de storage menor que banco relacional;
- compatibilidade S3;
- sem cobrança de egress direto do R2;
- cobrança por classes de operação.

É forte candidato para artefatos imutáveis, mas não substitui banco, autenticação, autorização ou transações.

### Cloudflare D1

Pode oferecer metadata store com SQLite e scale-to-zero, mas a semântica e cobrança por linhas precisam ser comparadas com PostgreSQL, relações, políticas e sync do ARA.

### Neon

Oferece PostgreSQL serverless e scale-to-zero. É alternativa de banco gerenciado separado, não BaaS completo. O free tier ainda tem pouco storage por projeto; o pago cobra compute e database storage por uso.

### Appwrite

É alternativa integrada e self-hostable. O Free também pausa por inatividade; o Pro inclui bastante storage, mas a migração do domínio relacional e das políticas atuais seria substancial.

## 8. Nenhum plano resolve sozinho

Pagar o Supabase Pro resolve dois problemas imediatos:

- pausa automática;
- quotas muito pequenas de banco e Storage.

Não resolve automaticamente:

- crescimento sem política de retenção;
- duplicação entre versões;
- acoplamento do domínio;
- portabilidade institucional;
- exportação completa;
- recuperação entre providers;
- custo de eventos e analytics de pesquisa;
- separação entre metadata, artefatos e dados de participantes.

Da mesma forma, usar R2 resolve custo de objetos, mas cria uma arquitetura composta que exige gateway, autorização e operação adicionais.

## 9. Alternativas a comparar

### A — Supabase Pro integrado

PostgreSQL + Auth + RLS + Functions + Storage.

**Vantagem:** menor risco operacional inicial.  
**Risco:** acoplamento e custo por projeto/organização.

### B — Supabase para metadata/Auth + object storage S3/R2

**Vantagem:** preserva conhecimento atual e amplia storage barato.  
**Risco:** autorização distribuída, signed URLs, inventário e consistência entre serviços.

### C — PostgreSQL gerenciado + S3-compatible + OIDC/API própria

**Vantagem:** portabilidade e separação claras.  
**Risco:** maior volume de código e operação.

### D — BaaS alternativo integrado

Appwrite, Nhost ou outro.

**Vantagem:** possível storage/self-host superior.  
**Risco:** remodelagem, novo lock-in e maturidade operacional.

### E — local-only no perfil pessoal

IndexedDB/SQLite + export/import; backend conectado opcional.

**Vantagem:** custo remoto mínimo.  
**Risco:** colaboração, recuperação e múltiplos dispositivos limitados.

## 10. Workloads que devem ser simulados

- 10 mil, 100 mil e 1 milhão de revisões JSON;
- tamanhos médios e máximos de microssequência;
- quantidade de relações e placements;
- frequência de novas versões;
- leituras durante estudo e autoria;
- geração de pacote offline;
- observações, diffs e findings;
- datasets de pesquisa e retenção;
- backups e restauração completa;
- GC de objetos órfãos.

A simulação deve calcular:

- GB de banco;
- GB de object storage;
- número de objetos;
- writes e reads;
- egress;
- funções/API;
- custo mensal;
- tempo de restore;
- custo operacional humano.

## 11. Requisitos de durabilidade

O ARA deve prever, independentemente do provider:

- exportação integral e documentada;
- inventário por digest;
- backup de metadata e artifacts;
- restore testado;
- cópia local de versões baixadas;
- verificação de integridade;
- retenção protocolar;
- migração para outro adapter;
- indicação clara do que está local, sincronizado, publicado ou retido.

## 12. Direção preliminar

A direção de menor risco para investigação é:

```text
metadata relacional pequena
+ artifact repository imutável
+ local materialization
+ adapters substituíveis
+ simulação de custo antes da seleção
```

O primeiro deployment pode continuar usando Supabase, inclusive pago, se as medições demonstrarem adequação. A arquitetura do domínio, entretanto, não deve depender da permanência dessa escolha.

## 13. Próximas decisões

1. medir o tamanho real de microssequências e revisões do AraLearn como amostra, não como limite do ARA;
2. construir gerador de workload sintético sem código de produto;
3. comparar Supabase Free/Pro, Supabase+R2 e uma alternativa portátil;
4. definir política de retenção e GC;
5. definir export/restore de referência;
6. somente então selecionar deployment inicial por ADR.
