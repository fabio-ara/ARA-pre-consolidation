# Extensão do pré-backlog — versionamento, arquitetura de histórico e economia de armazenamento v2

**Estado:** candidato para discussão; não executável  
**Relação:** revisão integral da área R  
**Substitui para leitura corrente:** `draft-backlog-versioning-storage-v1.pt-BR.md`  
**Regra:** nenhum item seleciona provider, plano, banco, object storage ou schema.

## Correção

A versão anterior concentrou-se em Storage, provider e custo. Esta revisão registra que o versionamento é primeiro um requisito de produto e pesquisa:

- permite autoria rápida e pouco burocrática;
- torna comportamento impulsivo não destrutivo;
- preserva erro, reparo e mudança de ideia;
- sustenta investigação vertical e horizontal pelo GPT;
- fixa condições de pesquisa;
- viabiliza colaboração, derivações, offline e evolução de agentes;
- somente depois gera decisões de banco, Storage e economia operacional.

## Composição do pré-backlog v5

```text
A–P: 171 itens
Q: 26 itens
R v2: 20 itens
S: 26 itens
→ 243 itens candidatos em 19 áreas
```

Manifesto: `research/data/ara-draft-backlog-v5-manifest.json`.

---

## R. Versionamento, arquitetura de histórico e economia operacional

### R01 — Tese de versionamento como redutor de burocracia

**Resultado candidato:** política de produto segundo a qual edição comum é imediata e reversível; o sistema cria histórico sem exigir confirmação ou nomeação manual de cada revisão.  
**Decisão:** quais ações de impacto externo ainda exigem confirmação explícita.

### R02 — Diário local, checkpoint e revisão durável

Separar autosave/undo local, checkpoints automáticos e revisões duráveis sincronizadas. Definir gatilhos, compactação, retenção e transição entre as três escalas.

### R03 — Semântica do grafo de revisões

Pais, múltiplos pais, derivação, restauração não destrutiva, combinação, revisão atual, versão fixada e nós bloqueados. O grafo preserva caminhos abandonados.

### R04 — Inventário integral de objetos versionados

Microssequências, cards, resources, composições, parâmetros, perfis de agente, templates, knowledge artifacts, operations, diffs, observações, políticas de acesso, instrumentos, datasets e análises.

### R05 — Granularidade do artefato

Comparar JSON completo de microssequência, manifesto de microssequência com cards independentes e decomposição adicional por resource. Medir duplicação, objeto count, latência, diff e compreensão.

### R06 — Alternativa: snapshots completos no banco

Medir rows, JSON size, WAL, índices, RLS, backups, parsing, triggers e CPU. Registrar por que a solução simples pode repetir o problema observado no AraLearn.

### R07 — Alternativa: snapshots completos no object storage

Avaliar como baseline de menor complexidade: um objeto imutável por revisão e ponteiro no banco. Medir duplicação, requests, restore e diff.

### R08 — Alternativa: content addressing e manifests

Canonicalização, digest, deduplicação, compartilhamento de subobjetos, integridade, refs e distinção entre bytes iguais e contexto pedagógico diferente.

### R09 — Alternativa: deltas e patches

Avaliar economia, comprimento de cadeia, compaction, migrations, corrupção, acesso aleatório e snapshots periódicos. Não presumir adoção inicial.

### R10 — Alternativa: operação/event log híbrido

Revisões imutáveis como fonte editorial; operações append-only como intenção e proveniência. Comparar com event sourcing integral e documentar o limite de complexidade aceitável.

### R11 — Alternativa: versionamento temporal no banco

Avaliar uso para metadata temporal, memberships e políticas. Registrar limites para DAG, múltiplos pais, grandes JSONs e deduplicação.

### R12 — Alternativa: versionamento nativo de bucket

Comparar recuperação operacional e lifecycle. Registrar custo de versões completas, ausência de semântica de domínio e falta de S3 Object Versioning no Supabase Storage.

### R13 — Alternativa: Git real e camada Git-like

Comparar Git/bundles para exportação e artefatos técnicos com sistemas Git-like sobre object storage para zero-copy derivation. Avaliar incompatibilidades com sync mobile, acesso por nó e analytics.

### R14 — Fronteira banco / artifact repository / local store

Definir responsabilidades e invariantes:

- banco: graph metadata, refs, access, operations, indexes e retention;
- Storage: artifacts e manifests imutáveis;
- local: materialização, diário, drafts, outbox e cache.

### R15 — Impacto no banco de dados

Modelar crescimento de linhas, arestas, índices, RLS/autorização, effective-audience projections, invalidations, concorrência de refs, WAL, backup e CPU. Payload fora do banco não significa banco irrelevante.

### R16 — Impacto no object storage

Modelar GB, número de objetos, PUT/GET/LIST, signed URLs, latência, órfãos, lifecycle, cold storage, egress, backup, restore e integridade.

### R17 — Projeções e front-end do histórico

Criar read models para revisão atual, histórico paginado, grafo em janela, diff resumido, audiência e referências de pesquisa. O front-end não deve varrer blobs para montar cada tela.

### R18 — Recuperação de contexto vertical e horizontal

Definir índices e pacotes de contexto para análise longitudinal de uma linhagem, síntese transversal de observações/branches e ciclo combinado. Guardar tudo não significa enviar tudo à LLM.

### R19 — Retenção, garbage collection e research holds

Classes para diário, checkpoint, revisão atual, ancestral, nó bloqueado, rollback, versão fixada, research hold, derivado reconstruível e órfão. Exclusão física apenas após prova de ausência de referência e retenção.

### R20 — Workload, custo, BaaS e ADR

Simular 10 mil, 100 mil e 1 milhão de revisões; alternativas de snapshot e deduplicação; deployments públicos e institucionais; backup/restore; CPU e custo operacional. Selecionar provider e arquitetura somente por ADR posterior.

---

## Sequência de investigação

1. R01–R04: tese, escalas, grafo e inventário;
2. R05–R13: granularidade e alternativas;
3. R14–R18: divisão arquitetural e consultas;
4. R19: retenção e GC;
5. R20: workload, custo e ADR.

## Critério de promoção futura

Um item somente poderá virar implementação quando possuir:

- comportamento observável e interface sem burocracia;
- unidade, identidade, pais, refs e restauração definidos;
- impacto medido em banco, Storage, local store e front-end;
- workload, object count e request model;
- política de retenção, acesso, backup e restore;
- análise de alternativa mais simples;
- provider-neutral export;
- decisão registrada por ADR.
