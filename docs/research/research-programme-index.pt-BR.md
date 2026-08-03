# Índice canônico do programa de pesquisa

**Estado:** evidência e decisões consolidadas para arquitetura  
**Idioma:** `pt-BR`  
**Última revisão:** 3 de agosto de 2026

## 1. Baselines concluídas

### Issue #4 — configuração

`ara.configuration-taxonomy.v1` define 205 parâmetros, 38 perfis, camadas, precedência, effective configuration e snapshots.

Manifesto: `research/data/issue4-final-artifact-manifest-v1.json`.

### Issue #5 — pesquisa e analytics

`ara.research-framework.v1` separa pergunta, protocolo, condição, evento/instrumento, evidência, medida, constructo, interpretação e intervenção.

Manifesto: `research/data/issue5-artifact-manifest-v1.json`.

### Issue #6 — produto e domínio

A baseline aceita:

```text
CourseVersion
→ ModuleNode / LessonNode
→ Placement
→ MicrosequenceRevision
→ Card
→ Resource / Practice / Response / Validator / Feedback
```

Decisões:

- `MicrosequenceRevision` é a unidade autoral reutilizável inicial, sem pretensão universal;
- `Placement` fornece contexto de curso, dependências, posição, overrides e progressão;
- `CourseVersion` é uma composição pedagógica completa e imutável;
- estado do estudante é contextual por assignment, course version, placement e card;
- relações tipadas substituem tags livres como núcleo de dependências;
- conteúdo, prática, resposta, validator e feedback permanecem separados;
- draft/workspace é mutável; revisões, snapshots e publicações são imutáveis;
- pastas, coleções, programas e catálogo organizam referências;
- research objects de #5 são entidades opcionais do mesmo domínio;
- capacidades são core, opcionais locais, conectadas, experimentais, adiadas, fora de escopo ou proibidas.

Artefatos:

- `docs/product/product-requirements-v1.md`;
- `docs/product/domain-model-v1.md`;
- `research/data/issue6-domain-entities-v1.csv`;
- `research/data/issue6-invariants-v1.csv`;
- `research/data/issue6-capability-classification-v1.csv`;
- `research/data/issue6-journey-registry-v1.csv`;
- `research/data/issue6-state-machines-v1.json`;
- `research/data/issue6-scenario-validation-v1.csv`;
- `research/data/issue6-decision-synthesis-v1.json`;
- `research/data/issue6-artifact-manifest-v1.json`.

## 2. Pesquisa contínua

A Issue #3 permanece aberta para revisões futuras quando:

- uma decisão arquitetural revelar incerteza material;
- uma capacidade opcional adquirir caso de uso concreto;
- uma avaliação produzir evidência nova;
- legislação, acessibilidade ou padrões relevantes mudarem.

Novas fontes não reabrem automaticamente baselines aprovadas; alterações exigem versão e decisão.

## 3. Próxima fase — Issue #7

A arquitetura deverá:

- preservar os conceitos e invariantes aprovados;
- separar requisitos duráveis, primeiro escopo, perfis de implantação e hipóteses técnicas;
- comparar cliente, persistência local, metadata store, immutable artifacts, sync, identity, MCP, analytics e deployment;
- definir ports/adapters provider-independent;
- dimensionar personal, research, formal, self-hosted e public/open profiles;
- especificar offline, conflito, revogação, backup, restore, migração e rollback;
- registrar decisões por ADR;
- validar o baseline na classe Galaxy A07;
- manter estudo pessoal sem event store ou LLM obrigatórios.

## 4. Fases seguintes

- **Issue #8:** jornadas, telas, estados, acessibilidade, idiomas, protótipos e sistema visual;
- **Issue #9:** releases, CI, quality gates e backlog executável;
- **Implementação:** somente depois dos três gates.

## 5. Não autorizações atuais

A conclusão das Issues #4–#6 não autoriza código de produto, schema físico, stack, UI, sync, event store, participant collection ou adoção automática de protótipos históricos.
