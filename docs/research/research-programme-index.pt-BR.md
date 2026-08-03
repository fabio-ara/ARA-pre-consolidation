# Índice canônico do programa de pesquisa

**Estado:** canônico para planejamento de pesquisa  
**Idioma:** `pt-BR`  
**Última revisão:** 3 de agosto de 2026

## 1. Finalidade

Este índice organiza a pesquisa necessária para definir o ARA sem transferir ao proprietário o trabalho de interpretar corpus bruto.

Cada pacote deve entregar conclusão, recomendação, alternativas, riscos, incertezas, registros estruturados, perfis e handoffs. Pesquisa concluída não autoriza automaticamente requisitos, arquitetura, UX ou implementação.

## 2. Issue #4 — concluída

A Issue #4 produziu a primeira taxonomia aceita: `ara.configuration-taxonomy.v1`.

### Pacotes de origem

| Pacote | PR | Escopo | Parâmetros aceitos |
|---|---:|---|---:|
| P1 | #45 | prática, resposta, tentativas, reveal, feedback, consequências e acessibilidade | 21 |
| P2 | #47 | progressão, mastery, sequência, ritmo, spacing, revisão, exemplos, scaffolding e retomada | 36 |
| P3 | #48 | autonomia, autorregulação, adaptação, acessibilidade e IA | 50 |
| P4 | #49 | instrumentação, condições, analytics e governança | 31 |
| P5 | #51 | autoria, revisão, reparo, versões, publicação, licenciamento e governança | 67 |

Os artefatos P1–P5 em `research/data/`, `research/pt-BR/`, `research/searches/` e `research/library/` permanecem fontes primárias. A síntese final não reescreve seus resultados.

## 3. Síntese integrada final

A integração preserva:

- **205 parâmetros de origem e 205 parâmetros canônicos**;
- zero duplicatas exatas;
- 18 aliases de namespace;
- 38 perfis canônicos;
- 36 candidatos adiados;
- 41 princípios rejeitados ou não recomendados;
- 15 cenários de validação conceitual.

### Artefatos canônicos

- `research/data/issue4-final-parameter-registry-v1.json` — identidades, origem, aliases e camadas;
- `research/data/issue4-final-profile-registry-v1.json` — perfis e overlays;
- `research/data/issue4-final-precedence-model-v1.csv` — autoridade e resolução de conflitos;
- `research/data/issue4-final-deferred-candidates-v1.csv` — candidatos adiados;
- `research/data/issue4-final-rejected-principles-v1.csv` — caminhos rejeitados;
- `research/data/issue4-final-scenario-validation-v1.csv` — validação integrada;
- `research/data/issue4-final-decision-synthesis-v1.json` — decisão estruturada;
- `research/pt-BR/issue4-sintese-final-taxonomia-configuracao-v1.md` — síntese explicativa.

### Conclusão principal

A configuração do ARA não é um formulário ou JSON plano. O modelo aceito é:

```text
catálogo versionado
+ perfil-base
+ overlays
+ políticas e locks
+ overrides esparsos
+ conteúdo e composição versionados
+ capacidades disponíveis
→ resolução determinística
→ configuração efetiva e snapshot reproduzível
```

As camadas são:

1. runtime e configuração efetiva;
2. conteúdo e materialização;
3. composição e dependências;
4. lifecycle e governança;
5. condição de pesquisa;
6. direitos e acessibilidade, transversal.

Parâmetros que transformam conteúdo ou composição produzem novas revisões, derivações, variantes ou snapshots; não são switches de renderer.

## 4. Decisões normativas da taxonomia

- AraLearn permanece o primeiro perfil completo de referência: não punitivo, data-minimal, mobile/offline e controlado pelo usuário.
- Aceitar um parâmetro significa exigir representabilidade e rastreabilidade, não implementar todos os valores.
- `study_review.*` e `authoring_review.*` são namespaces distintos.
- Acessibilidade e direitos têm precedência e não podem ser desligados por perfil.
- Protocolo, instituição, autor, estudante, regras adaptativas, IA e capacidade técnica têm autoridades diferentes.
- Capacidade técnica ausente não autoriza fallback silencioso.
- GPT+MCP e ARA são canais complementares: o primeiro executa operações semânticas; o segundo torna artefatos e decisões visíveis e controláveis.
- IA não aprova, publica ou altera silenciosamente artefatos consequenciais.
- Evento, medida, constructo, interpretação e intervenção permanecem separados.
- Publicados e condições bloqueadas são snapshots; mudanças criam novas revisões, supersessão ou retirada.
- Reference, copy, fork, adaptation e translation são relações diferentes.
- Free-text tags não bastam como mecanismo único de dependência, provenance ou anotação.

## 5. Hipóteses preservadas para produto e arquitetura

Ainda não normativas:

```text
microssequência versionada
→ ocorrência/posição em composição de curso
→ composição versionada
→ snapshot local autossuficiente
→ estado contextual por curso/versão/posição/card
```

A Issue #6 deverá aceitar, revisar ou rejeitar explicitamente:

- microssequência como unidade reutilizável;
- placement/occurrence;
- curso composto por referências;
- reference, copy, fork e snapshot;
- transferência de estado entre cursos.

A Issue #7 decidirá persistência, materialização offline, IndexedDB ou alternativa, sincronização, deduplicação, revogação e exclusão.

## 6. Próxima fase — Issue #5

A próxima fase é **Issue #5 — protocolos de pesquisa, instrumentação e learning analytics**.

Ela deverá importar sem reabrir:

- `protocol.purpose` e `protocol.version_lock`;
- condição e assignment;
- participante, identidade, consentimento e retirada;
- autorização e semântica de eventos;
- instrumentos e administração;
- medida, constructo, interpretação, outcome e plano de análise;
- missing data e fidelity;
- provenance e diff de variantes;
- finalidade, retenção, acesso e exportação de dados;
- analytics pessoais e perguntas por papel;
- política de intervenção;
- equivalência entre implantações;
- separação entre telemetria operacional e analytics educacionais.

A Issue #5 deverá definir objetos, fórmulas, instrumentos, governança e inferências permitidas/proibidas. Não deve reabrir os defaults pedagógicos de P1–P3 nem a governança autoral de P5 sem nova evidência e decisão versionada.

## 7. Fases posteriores

- **Issue #6:** requisitos, atores, jornadas, entidades, estados, composição, versões, autoria, lifecycle e integração normativa da taxonomia.
- **Issue #7:** arquitetura, perfis de implantação, persistência, sincronização, segurança, custo e ADRs.
- **Issue #8:** formulários, perfis, progressive disclosure, rendering em tempo real, versões, diffs, comentários, review queues, analytics por papel, acessibilidade e offline.
- **Issue #9:** releases, quality gates, migração, rollback, evidence packages e backlog executável.

## 8. Regra de evolução

Qualquer revisão da taxonomia deverá:

1. criar nova versão;
2. identificar parâmetros e perfis afetados;
3. preservar aliases e origem;
4. registrar evidência e decisão;
5. avaliar efeitos em snapshots, estudos e cursos existentes;
6. não reescrever silenciosamente P1–P5.

## 9. Não autorizações

A conclusão da Issue #4 não autoriza:

- schema de produção;
- banco, Storage ou IndexedDB;
- MCP endpoints;
- arquitetura ou stack;
- UI;
- event store, dashboard ou coleta de participantes;
- scheduler, learner model ou adaptação automática;
- atualização ou reparo automático entre cursos;
- código ou migração.
