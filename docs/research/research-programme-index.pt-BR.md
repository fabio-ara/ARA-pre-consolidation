# Índice canônico do programa de pesquisa

**Estado:** canônico para planejamento de pesquisa  
**Idioma:** `pt-BR`  
**Última revisão:** 3 de agosto de 2026

## 1. Issue #4 — concluída

A Issue #4 produziu `ara.configuration-taxonomy.v1`:

- 205 parâmetros canônicos;
- 38 perfis;
- camadas de runtime, conteúdo, composição, lifecycle, pesquisa e direitos;
- precedência, aliases, snapshots e combinações não suportadas;
- 36 candidatos adiados e 41 princípios rejeitados.

Artefatos principais:

- `research/data/issue4-final-decision-synthesis-v1.json`;
- `research/data/issue4-final-artifact-manifest-v1.json`;
- `research/pt-BR/issue4-sintese-final-taxonomia-configuracao-v1.md`.

P1–P5 permanecem fontes primárias das definições e evidências.

## 2. Issue #5 — concluída

A Issue #5 produziu `ara.research-framework.v1`.

### Decisão central

```text
pergunta/finalidade
→ protocolo
→ condição e assignment
→ evento autorizado ou instrumento
→ evidência
→ medida
→ constructo
→ interpretação
→ decisão/intervenção
```

Nenhuma camada é inferida automaticamente da anterior.

### Entregas

- `docs/research/research-protocols-analytics-v1.pt-BR.md`;
- `research/data/issue5-research-framework-v1.json`;
- `research/data/issue5-event-vocabulary-v1.csv`;
- `research/data/issue5-measure-registry-v1.csv`;
- `research/data/issue5-instrument-registry-v1.csv`;
- `research/data/issue5-governance-matrix-v1.csv`;
- `research/data/issue5-scenario-validation-v1.csv`;
- `research/data/issue5-decision-synthesis-v1.json`;
- `research/data/issue5-integration-audit-v1.json`;
- `research/data/issue5-artifact-manifest-v1.json`.

### Resultado

- 24 fontes centrais;
- 24 eventos mínimos e autorizáveis;
- 16 medidas candidatas com fórmula, unidade, janela, missingness e uso permitido;
- 14 famílias de instrumentos quantitativos, qualitativos e mistos;
- 15 regras de governança;
- 12 cenários aprovados.

Caliper, xAPI, QTI, DDI, PROV-O, RO-Crate e DPV são mapeamentos candidatos. Não substituem a semântica interna do ARA.

O perfil pessoal permanece data-minimal. Disponibilidade de evento nunca autoriza coleta. Analytics pessoais, pedagógicos, de pesquisa e operacionais possuem autoridade, visibilidade e retenção separadas.

## 3. Próxima fase — Issue #6

A próxima fase é **Issue #6 — requisitos do produto e modelo de domínio**.

Ela deverá integrar normativamente:

- `ara.configuration-taxonomy.v1`;
- `ara.research-framework.v1`;
- atores e jornadas;
- curso, módulo, lição, microssequência, card e placement;
- conteúdo, prática, resposta, validator e feedback;
- perfil, configuração efetiva e snapshot;
- protocolo, condição, participante, assignment, instrumento, evento, medida, constructo e evidência;
- autoria, observação, revisão, reparo, versão, publicação e retirada;
- biblioteca, pastas, referências, coleções, programas e catálogo;
- offline, sync, importação, exportação, confidencialidade, licença e exclusão;
- classificação de capacidades core, opcionais, conectadas, experimentais e fora de escopo.

A hipótese de composição por microssequências deverá ser aceita, revisada ou rejeitada explicitamente.

## 4. Fases seguintes

- **Issue #7:** arquitetura, perfis de implantação e ADRs;
- **Issue #8:** UX, acessibilidade, sistema visual e protótipos;
- **Issue #9:** releases, quality gates e backlog executável.

## 5. Não autorizações

As Issues #4 e #5 não autorizam:

- schema ou event store de produção;
- banco, Storage, IndexedDB ou sincronização;
- dashboard ou coleta de participantes;
- predição, early warning ou intervenção automática;
- arquitetura, stack, UI ou código.
