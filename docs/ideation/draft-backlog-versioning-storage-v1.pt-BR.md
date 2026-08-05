# Extensão do pré-backlog — versionamento e armazenamento sustentável

**Estado:** candidato para discussão; não executável  
**Relação:** nova área R do pré-backlog do ARA  
**Regra:** nenhum item seleciona fornecedor, plano ou schema.

## Integração

```text
Áreas A–P: 171 itens
+ Área Q: 26 itens
+ Área R: 10 itens
→ pré-backlog v3: 207 itens candidatos em 18 áreas
```

Manifesto: `research/data/ara-draft-backlog-v3-manifest.json`.

---

## R. Versionamento, retenção, armazenamento e economia operacional

### R01 — Inventário de objetos versionados

Mapear microssequências, cards, composições, configurações, perfis de agente, knowledge, operações, diffs, observações, instrumentos, datasets e análises. Definir o que é revisionável, imutável, derivado ou descartável.

### R02 — Separação metadata/artifact/local

Comparar banco relacional pequeno, object storage imutável e materialização local. Definir consultas e transações que exigem metadata e payloads que podem residir como artefato.

### R03 — Content addressing e deduplicação

Canonicalização, digest, identificação de artefato já existente, referências compartilhadas e distinção entre igualdade de payload e contexto pedagógico.

### R04 — Manifests e materialização

Curso e condição como manifestos de referências; pacotes completos somente para publicação, exportação ou uso offline. Medir custo de reconstrução e cache.

### R05 — Retenção e garbage collection

Classes ativa, publicada, research-locked, rollback, superseded e órfã; GC por referências, janelas, direitos e protocolos, nunca apenas por idade.

### R06 — Workload e simulação de custo

Gerar cenários com 10 mil, 100 mil e 1 milhão de revisões. Medir banco, storage, objetos, operações, egress, functions, backup, restore e custo operacional.

### R07 — Comparação de deployment

Comparar Supabase Free/Pro, Supabase + object storage externo, PostgreSQL + S3/OIDC/API, BaaS alternativo e perfil local-only.

### R08 — Disponibilidade e pausa

Definir requisitos de always-on, scale-to-zero, retomada, provider degraded e funcionamento offline. Free tier não pode ser confundido com garantia de durabilidade.

### R09 — Backup, exportação e restauração

Formato completo e provider-neutral para metadata, artifacts, assets, versões, relações e retenções; restore testado em deployment alternativo.

### R10 — Budgets e administração compreensível

Exibir espaço, crescimento, retenção, custo estimado, objetos órfãos e consequência de limpeza em linguagem comum, sem buckets, WAL ou classes de operação na superfície principal.

---

## Sequência de investigação

1. R01–R02: objetos e fronteiras;
2. R03–R05: deduplicação e retenção;
3. R06: workload sintético e amostras do AraLearn;
4. R07–R09: provider, export e restore;
5. R10: interface e alertas;
6. ADR somente após medições.

## Critério de promoção

Um item somente poderá virar implementação quando possuir:

- workload medido;
- requisitos de durabilidade e disponibilidade;
- custo mensal e operacional estimado;
- política de retenção e rollback;
- export/restore verificável;
- alternativa provider-neutral;
- efeitos offline, segurança e privacidade;
- decisão por ADR e plano de saída.
