# Protocolo inicial — versionamento, armazenamento e economia operacional

**Estado:** revisão técnica de escopo; não normativa  
**Data:** 4 de agosto de 2026  
**Relações:** Issues #7, #10, #77 e nova frente de versionamento/infraestrutura  
**Limite:** não seleciona fornecedor, plano, schema ou implantação.

## 1. Problema

O ARA pretende manter revisões imutáveis de microssequências, cursos, configurações de agente, knowledge collections, prompts/templates, operações, diffs, observações e análises. A escala prevista pode alcançar dezenas de milhares de microssequências e múltiplas revisões por objeto.

O AraLearn usa Supabase Free e já evidencia limites práticos de banco, Storage, computação e pausa por inatividade. O ARA não pode definir sua semântica de versionamento a partir da quota de um fornecedor, mas também não pode ignorar custo, retenção, disponibilidade, backup e restauração.

## 2. Hipótese arquitetural a examinar

```text
PostgreSQL ou metadata store
- identidades, relações, permissões, placements, revisões e índices

Object storage
- payloads JSON imutáveis, assets, snapshots, exports e evidência

Local store
- materialização offline, rascunhos, outbox e estado pessoal
```

Essa separação é hipótese, não decisão. Deve ser comparada com BaaS integrado, backend próprio portátil e perfil local-only.

## 3. Perguntas

1. Qual volume resulta de 10 mil, 100 mil e 1 milhão de revisões pequenas?
2. Quanto deve permanecer no banco relacional e quanto pode residir como artefato imutável?
3. Como deduplicação por digest, manifests e referências reduzem duplicação de variantes de curso?
4. Quais objetos exigem retenção permanente, temporária, protocolar ou configurável?
5. Como garbage collection pode remover artefatos não referenciados sem apagar publicações, pesquisas ou rollback?
6. Como planos gratuitos e pagos diferem em pausa, backup, restauração, storage, egress, operações e custo mínimo?
7. O primeiro deployment deve usar Supabase Pro, Supabase + object storage externo, outro BaaS ou componentes separados?
8. Como garantir exportação e restauração entre providers?
9. Que budgets e alertas devem ser visíveis ao proprietário em linguagem simples?
10. Como testar custo e desempenho antes de selecionar uma arquitetura?

## 4. Cenários de carga

### S1 — uso pessoal

- 20 cursos;
- 10 mil microssequências/revisões;
- poucos assets;
- uso intermitente;
- sem coleta de pesquisa contínua.

### S2 — pesquisa acadêmica pequena

- 50 versões/condições de curso;
- 100 participantes;
- conteúdo versionado, eventos autorizados, instrumentos e exports;
- retenção exigida pelo protocolo.

### S3 — comunidade de curadoria

- 100 mil microssequências/revisões;
- observações e diffs frequentes;
- múltiplos perfis de agente e knowledge snapshots;
- deduplicação obrigatória.

### S4 — implantação institucional

- dados confidenciais;
- disponibilidade, backup e restauração formais;
- servidor próprio ou serviço contratado;
- política de retenção e território.

## 5. Dimensões de comparação

- banco e storage incluídos;
- pausa ou scale-to-zero;
- disponibilidade esperada;
- backups e janela de restauração;
- object storage e compatibilidade S3;
- egress e custo por operação;
- custo mínimo e previsibilidade;
- autenticação e autorização;
- self-host/portabilidade;
- suporte a exportação integral;
- complexidade operacional;
- adequação a milhares de objetos pequenos;
- adequação a metadados relacionais e grafos;
- integração com PWA/local-first;
- proteção de dados e deployment institucional.

## 6. Fontes iniciais

A rodada usa documentação oficial atual de Supabase, Cloudflare R2/D1, Neon e Appwrite. Preços e quotas são fotografias de agosto de 2026 e devem ser reverificados no momento de decisão.

## 7. Saídas

- matriz oficial de planos e limites;
- modelos de carga e simulação;
- requisitos de retenção, GC, backup e exportação;
- alternativas de deployment;
- itens novos do pré-backlog;
- correção da Issue #77: AraLearn como contraste, não como fixture equivalente;
- decisão posterior por ADR, somente após medições.

## 8. Não autorizações

- contratação de plano;
- criação de nova conta;
- migração do AraLearn;
- seleção de Supabase, Cloudflare, Neon ou Appwrite;
- schema de produção;
- descarte automático de revisões;
- uso de branch de banco como versionamento pedagógico;
- implementação de analytics ou participantes.
