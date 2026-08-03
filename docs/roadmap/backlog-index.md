# Backlog e fluxo de trabalho do ARA

**Estado:** documento operacional vigente  
**Idioma:** `pt-BR`  
**Última revisão:** 3 de agosto de 2026

## 1. Navegação principal

1. `docs/vision/product-vision.pt-BR.md` — produto pretendido;
2. `docs/research/research-programme-index.pt-BR.md` — pesquisa concluída e próxima;
3. este documento — fases, autoridade, rastreabilidade e regras das issues.

Issues são unidades autorizadas e autossuficientes. Pesquisa, decisão, produto, arquitetura, UX e implementação permanecem separados.

## 2. Autoridade

Para comportamento atual e engenharia:

1. especificação aprovada da fase;
2. ADR ou decisão estratégica aceita;
3. issue operacional vigente e este índice;
4. síntese decisória;
5. evidência e dataset;
6. issue, PR ou protótipo histórico;
7. conversa não registrada.

Fontes primárias prevalecem para afirmar o que ocorreu. Ausência de classificação não torna um artefato normativo.

## 3. Caminho linear

```text
#3 evidência
→ síntese/recomendação
→ #4 taxonomia — concluída
→ #5 protocolos e analytics — atual
→ #6 produto e domínio
→ #7 arquitetura e ADRs
→ #8 UX/UI
→ #9 releases e implementação
→ avaliação
```

A Issue #2 corre em paralelo quando questões jurídicas e institucionais forem relevantes.

## 4. Issues principais

| Issue | Fase | Estado | Saída |
|---|---:|---|---|
| #10 | 00 | aberta | roadmap, gates e regras |
| #2 | 10 | paralela | propriedade intelectual, licenciamento e identidade |
| #3 | 20 | contínua | protocolos, corpora, bibliografia e sínteses |
| #4 | 30 | concluída | `ara.configuration-taxonomy.v1`, perfis, precedência e handoffs |
| #5 | 40 | ativa | protocolos, eventos, instrumentos, medidas e governança |
| #6 | 50 | futura | requisitos, atores, jornadas, entidades e estados |
| #7 | 60 | futura | arquitetura, stack, perfis e ADRs |
| #8 | 70 | futura | jornadas, telas, estados e acessibilidade |
| #9 | 80 | futura | releases e backlog executável |

## 5. Issue #4 — conclusão

### Pacotes

| Pacote | PR | Parâmetros |
|---|---:|---:|
| P1 | #45 | 21 |
| P2 | #47 | 36 |
| P3 | #48 | 50 |
| P4 | #49 | 31 |
| P5 | #51 | 67 |

### Síntese final

A taxonomia final preserva:

- 205 parâmetros canônicos;
- 18 aliases de namespace;
- 38 perfis;
- seis camadas de incidência;
- autoridade e precedência explícitas;
- 36 candidatos adiados;
- 41 princípios rejeitados;
- 15 cenários validados conceitualmente.

Artefatos:

- `research/data/issue4-final-parameter-registry-v1.json`;
- `research/data/issue4-final-profile-registry-v1.json`;
- `research/data/issue4-final-precedence-model-v1.csv`;
- `research/data/issue4-final-deferred-candidates-v1.csv`;
- `research/data/issue4-final-rejected-principles-v1.csv`;
- `research/data/issue4-final-scenario-validation-v1.csv`;
- `research/data/issue4-final-decision-synthesis-v1.json`;
- `research/pt-BR/issue4-sintese-final-taxonomia-configuracao-v1.md`.

Os artefatos P1–P5 continuam prevalecendo para as definições e evidências de cada parâmetro. A integração acrescenta aliases, camadas, perfis, precedência e handoffs; não apaga resultados anteriores.

## 6. Hipóteses transversais preservadas

Continuam `discovered`, não normativas:

- microssequência versionada como candidata a unidade autoral e reutilizável;
- curso como composição versionada de ocorrências;
- snapshot offline autossuficiente;
- estado por curso, versão, posição e card;
- catálogo + perfil + overlays + overrides esparsos;
- cursos derivados com invariantes e diffs;
- GPT+MCP e ARA como canais complementares;
- administração em linguagem pedagógica.

#6 decidirá domínio; #7 arquitetura; #8 UX.

## 7. Issue #5 — trabalho atual

A Issue #5 deverá consolidar normativamente:

- protocolo, condição e assignment;
- participante, identidade, consentimento e retirada;
- eventos autorizados e vocabulário semântico;
- instrumentos quantitativos e qualitativos;
- medidas, constructos, interpretações e outcomes;
- missing data, fidelity e análise;
- finalidade, minimização, retenção, acesso e exportação;
- analytics pessoais, pedagógicos e de pesquisa;
- intervenções e inferências proibidas;
- equivalência entre implantações;
- separação de telemetria operacional.

### Entradas obrigatórias

- `research/data/issue4-final-decision-synthesis-v1.json`;
- `research/pt-BR/issue4-sintese-final-taxonomia-configuracao-v1.md`;
- parâmetros P4 e handoffs de P1–P5;
- perfil AraLearn data-minimal;
- precedência de direitos, consentimento e acessibilidade.

### Não autorizações

Issue #5 não autoriza automaticamente:

- coleta com participantes;
- event store de produção;
- dashboard;
- modelo preditivo ou early warning;
- arquitetura ou stack;
- UX;
- código.

## 8. Experimentos históricos

#36/#37, #38/#39 e #40/#41 permanecem experimentos não normativos. #42 permanece adiado. Podem informar falhas, testes e segurança; não definem requisitos ou stack.

A Issue #50 é um placeholder acidental encerrado como `not_planned`; não autoriza trabalho.

## 9. Classificação obrigatória

Cada issue declara:

- fase;
- tipo;
- autoridade;
- fontes governantes;
- dependências;
- saída verificável;
- não autorizações.

Autoridades: `governing`, `normative-pending`, `accepted-normative`, `decision-synthesis`, `evidence`, `historical-experiment`, `deferred`, `superseded`, `rejected`.

## 10. Estrutura mínima de issue

```markdown
## Classification
- Phase:
- Type:
- Authority:
- Governing sources:
- Expected output:

## Context and decision problem
## Intended outcome
## Evidence and prior decisions
## Scope
## Out of scope and non-authorizations
## Dependencies
## Method or proposed approach
## Risks and cross-cutting effects
## Deliverables
## Acceptance criteria
## Validation
## Documentation and traceability
```

## 11. Regras por tipo

### Pesquisa

Registra pergunta, decisão informada, método, fontes, datas, queries, amostragem, inclusão/exclusão, acesso, suficiência, extração, limitações, síntese e recomendação. Não entrega corpus bruto ao proprietário.

### Síntese

Compara alternativas, benefícios, custos, evidência, riscos e reversibilidade. Estados: `recommended`, `accepted`, `deferred`, `rejected`, `owner-decision-required`.

### Protótipo

Exige incerteza, hipótese, falsificação, menor escopo adequado, estado não normativo e fase responsável. Não seleciona stack implicitamente.

### Produto/domínio

Define atores, jornadas, entidades, estados, invariantes e lifecycle; separa núcleo, extensão, conectado, experimental e fora de escopo.

### Arquitetura

Liga decisão a requisito e perfil; compara workloads, segurança, privacidade, acessibilidade, offline, desempenho, operação, custo e migração; registra ADR.

### UX

Liga ator, jornada, estado, requisito, parâmetro, permissão, falha, mobile/offline e acessibilidade. Implementação não inventa comportamento.

### Implementação para Codex

Aponta release, requisito, domínio, ADR, contrato, jornada/tela, escopo, dados, comportamento, falhas, impactos, aceite, testes, documentação e rollback. Lacunas voltam à fase correta.

## 12. Rastreabilidade

```text
problema
→ evidência
→ síntese
→ requisito
→ domínio
→ ADR
→ UX
→ release
→ issue
→ código/testes
→ avaliação
```

Omissões exigem justificativa.

## 13. Conclusão e PRs

Uma PR substancial registra issues, documentos, evidência ou decisão, validação, limitações e follow-up autorizado.

Uma issue só conclui quando entregas e critérios estão verificados e limitações explícitas. Pesquisa parcial ou bloqueada não é concluída.

## 14. Próxima ação

Executar a **Issue #5** com a taxonomia final da Issue #4 como entrada normativa. Não avançar para #6 antes de concluir protocolos, instrumentação e analytics.
