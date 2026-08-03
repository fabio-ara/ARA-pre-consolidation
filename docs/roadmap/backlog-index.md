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
5. evidência/dataset;
6. issue, PR ou protótipo histórico;
7. conversa não registrada.

Fontes primárias prevalecem para afirmar o que ocorreu. Ausência de classificação não torna um artefato normativo.

## 3. Caminho linear

```text
#3 evidência
→ síntese/recomendação
→ #4 taxonomia
→ #5 protocolos e analytics
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
| #4 | 30 | ativa | parâmetros, perfis, autoridade, precedência e handoffs |
| #5 | 40 | futura | protocolos, eventos, instrumentos, medidas e governança |
| #6 | 50 | futura | requisitos, atores, jornadas, entidades e estados |
| #7 | 60 | futura | arquitetura, stack, perfis e ADRs |
| #8 | 70 | futura | jornadas, telas, estados e acessibilidade |
| #9 | 80 | futura | releases e backlog executável |

## 5. Issue #4 — pacotes

### P1 — concluído — PR #45

21 dimensões: prática, resposta, tentativas, reveal, feedback, consequências e acessibilidade. Perfil AraLearn não punitivo preservado; ranking rejeitado; telemetry adiada.

### P2 — concluído — PR #47

36 dimensões: progressão, mastery, sequência, ritmo, spacing, revisão, exemplos, scaffolding, segmentação e retomada. Conclusão estrutural não equivale a mastery; scheduler e adaptação automática adiados.

### P3 — concluído — PR #48

50 dimensões e nove perfis: autonomia, autorregulação, adaptação, acessibilidade e IA. Shared control; baseline acessível; IA delimitada; `preview-only`/`recommend-and-confirm`; GPT+MCP e ARA como canais complementares.

### P4 — concluído — PR pendente

31 dimensões e nove perfis: protocolos, condições, participantes, consentimento, eventos, instrumentos, medidas, constructos, interpretações, provenance, variantes, governança, analytics e equivalência entre implantações.

Cadeia obrigatória:

```text
finalidade
→ protocolo
→ condição
→ evento/instrumento
→ medida
→ constructo
→ interpretação
→ decisão/intervenção
```

Decisões:

- AraLearn data-minimal permanece baseline pessoal;
- eventos exigem finalidade e autorização;
- eventos não são medidas; medidas não são constructos;
- consentimento, retirada, minimização, retenção, acesso e exportação são explícitos;
- analytics pessoais, pedagógicos, de pesquisa e operacionais são separados;
- painéis respondem perguntas por papel;
- variantes exigem snapshots e diffs;
- Caliper/xAPI são mapeamentos candidatos;
- telemetria operacional permanece separada;
- coleta, event store, dashboards, predição e early warning não foram autorizados.

Artefatos P4 em `research/data/p4-*`, `research/pt-BR/p4-*`, protocolo e bibliografia P4 prevalecem sobre resumos.

### P5 — próximo

Autoria, revisão, auditoria, reparo, publicação e políticas institucionais. Deve integrar o modelo de dois canais, composição por microssequências, perfis/overrides, provenance, permissões, forks, retirada e administração leiga.

Pacotes não geram novas issues automaticamente.

## 6. Hipóteses transversais obrigatórias

`discovered`, não normativas:

- parametrização em runtime, conteúdo/materialização, composição/dependências, lifecycle e condição;
- microssequências versionadas e ocorrências contextuais;
- curso como composição versionada;
- snapshot offline autossuficiente;
- estado por curso/versão/posição/card;
- chat/MCP para direção semântica e ARA para inspeção/controle determinístico;
- catálogo + perfil + overrides esparsos;
- cursos derivados com invariantes e diffs;
- interface administrativa em linguagem pedagógica.

#6 decidirá domínio; #7 arquitetura; #8 UX.

## 7. Experimentos históricos

#36/#37, #38/#39 e #40/#41 permanecem experimentos não normativos. #42 permanece adiado. Podem informar falhas, testes e segurança; não definem requisitos ou stack.

## 8. Classificação obrigatória

Cada issue declara:

- fase;
- tipo;
- autoridade;
- fontes governantes;
- dependências;
- saída verificável;
- não autorizações.

Autoridades: `governing`, `normative-pending`, `accepted-normative`, `decision-synthesis`, `evidence`, `historical-experiment`, `deferred`, `superseded`, `rejected`.

## 9. Estrutura mínima de issue

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

## 10. Regras por tipo

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

Deve apontar release, requisito, domínio, ADR, contrato, jornada/tela, escopo, dados, comportamento, falhas, impactos, aceite, testes, documentação e rollback. Lacunas voltam à fase correta.

## 11. Rastreabilidade

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

## 12. Conclusão e PRs

Uma PR substancial registra issues, documentos, evidência/decisão, validação, limitações, migração/rollback e follow-up autorizado.

Issue só conclui quando entregas e critérios estão verificados e limitações explícitas. Pesquisa parcial ou bloqueada não é concluída.

## 13. Próxima ação

Executar o **P5 da Issue #4**. Depois, produzir a síntese final da primeira taxonomia antes de avançar para #5.
