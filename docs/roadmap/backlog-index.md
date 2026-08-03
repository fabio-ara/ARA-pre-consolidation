# Backlog e fluxo de trabalho do ARA

**Estado:** documento operacional vigente  
**Idioma:** `pt-BR`  
**Última revisão:** 3 de agosto de 2026  
**Público:** proprietário, Codex e outros agentes, colaboradores, avaliadores externos e pesquisa acadêmica.

## 1. Função e navegação principal

As Issues do GitHub são as unidades de trabalho autorizadas do ARA. Devem ser autossuficientes para pesquisa, síntese, decisão, especificação, protótipo exploratório, implementação, validação ou avaliação.

A navegação principal possui três documentos:

1. `docs/vision/product-vision.pt-BR.md` — produto pretendido;
2. `docs/research/research-programme-index.pt-BR.md` — pesquisa concluída, lacunas e pacotes;
3. este documento — fases, autoridade, rastreabilidade e regras das issues.

Relatórios, datasets, protocolos, ADRs, especificações e planos de release são entregas das issues correspondentes. Não devem repetir integralmente os três documentos principais.

## 2. Autoridade e fontes

### 2.1 Classes

- **Fonte histórica primária:** documentos iniciais, edição das issues, comentários, PRs, commits, código, exports, hashes, datasets e testes. Demonstra o que ocorreu, mas não é automaticamente requisito atual.
- **Evidência:** protocolo, busca, triagem, extração, revisão, benchmark, auditoria ou avaliação. Informa recomendações; não autoriza implementação.
- **Síntese decisória:** integra evidência, alternativas, recomendação, riscos e incertezas.
- **Especificação aprovada:** taxonomia, requisito, domínio, arquitetura, ADR, contrato, UX ou release aprovado.
- **Registro de implementação:** issue executável, código, teste, migração, release e documentação operacional.

### 2.2 Precedência

Para comportamento atual e engenharia:

1. especificação aprovada da fase relevante;
2. ADR ou decisão estratégica aprovada;
3. issue operacional vigente e este índice;
4. síntese decisória aceita;
5. evidência e datasets;
6. issue, PR ou protótipo histórico;
7. conversa ou memória não registrada.

Para afirmar o que ocorreu, prevalecem fontes primárias. Para afirmações bibliográficas, prevalecem fonte citada, extração e estado de acesso.

Ausência de classificação não torna um artefato normativo.

## 3. Caminho linear

```text
#3 pesquisa bibliográfica, comparativa e contextual
→ síntese crítica e recomendação
→ #4 taxonomia de parametrização
→ #5 protocolos, instrumentação e analytics
→ #6 requisitos e domínio
→ #7 arquitetura, stack, perfis e ADRs
→ #8 UX/UI e acessibilidade
→ #9 releases
→ issues de implementação autossuficientes
→ validação e avaliação
```

Possibilidade de pesquisa não se transforma automaticamente em requisito, contrato, protótipo, biblioteca ou implementação.

A Issue #2 prossegue em paralelo quando questões jurídicas, institucionais ou de identidade se tornam relevantes.

## 4. Issues principais

| Issue | Fase | Estado | Saída e autoridade |
|---|---:|---|---|
| #10 | 00 | aberta | Coordena fases, gates e regras. |
| #2 | 10 | paralela | Propriedade intelectual, licenciamento, marca e questões institucionais. |
| #3 | 20 | contínua | Protocolos, buscas, corpora, bibliografia e sínteses. |
| #4 | 30 | ativa | Parâmetros, perfis, maturidade, autoridade, precedência, conflitos e handoffs. |
| #5 | 40 | futura | Protocolos, condições, eventos, medidas, instrumentos, governança e inferências. |
| #6 | 50 | futura | Atores, jornadas, entidades, estados, capacidades e requisitos normativos. |
| #7 | 60 | futura | Arquitetura, stack, perfis de implantação e ADRs. |
| #8 | 70 | futura | Jornadas, telas, estados, acessibilidade e sistema visual. |
| #9 | 80 | futura | Releases funcionais e backlog executável pelo Codex. |

## 5. Pesquisa e sínteses concluídas

| Issue | PR(s) | Resultado | Autoridade atual |
|---|---:|---|---|
| #14 | #15 | primeira síntese de revisões | evidência |
| #16 | #21–#23 | busca formal e deduplicação | evidência/método |
| #17 | #19 | formatos de resposta e feedback | evidência P1 |
| #18 | #20 | programação móvel | evidência situada |
| #24 | #25 | triagem de 1.471 registros | evidência inicial |
| #26 | #27 | extração de prioridade A | evidência |
| #28 | #29 | sobreposição de estudos | evidência/método |
| #30 | #43 | síntese AraLearn + horizonte externo | síntese decisória |
| #31 | #32 | auditoria dos resources | baseline de referência |
| #33–#34 | #35 | benchmark de sistemas e gêneros | evidência comparativa |
| #4/P1 | #45 | prática, resposta, tentativas, feedback e consequências | síntese decisória P1 |
| #4/P2 | #47 | progressão, sequência, revisão e scaffolding | síntese decisória P2 |
| #4/P3 | branch P3 | autonomia, adaptação, acessibilidade e IA | síntese decisória P3 |

## 6. Issue #4 — estado dos pacotes

### P1 — concluído

- 21 dimensões aceitas;
- perfil AraLearn não punitivo preservado;
- prática separada de medição e consequência;
- resposta, validade, crédito, tentativa, reveal e feedback combináveis;
- acessibilidade com precedência;
- telemetry de tentativas adiada;
- ranking público rejeitado;
- nenhum schema, UX ou código autorizado.

Artefatos originais em `research/data/p1-*`, `research/pt-BR/p1-*` e bibliografia P1 prevalecem sobre resumos.

### P2 — concluído

- 36 dimensões aceitas;
- conclusão estrutural separada de mastery;
- evidência, critério, remediação, override e rechecagem explícitos;
- sequência separada de ritmo;
- spacing separado de interleaving;
- agenda, carga, adiamento e item relation separados;
- exemplos, scaffolding, segmentação e retomada representados;
- estimadores, scheduler e detecção automática adiados;
- nenhum algoritmo, UX ou código autorizado.

Artefatos originais em `research/data/p2-*`, `research/pt-BR/p2-*` e bibliografia P2 prevalecem sobre resumos.

### P3 — concluído

- corpus de 34 fontes;
- 50 dimensões aceitas;
- nove perfis e overlays;
- autonomia separada de liberdade total;
- autorregulação representada por suportes explícitos;
- adaptação separada de acomodação e aplicação automática;
- acessibilidade tratada como baseline e precedência;
- IA separada por função, iniciação, contexto, grounding, status, autoridade, revisão, validação, incerteza, provenance, editabilidade, contestação, dados, retenção, provedor, fallback e falha;
- `preview-only` e `recommend-and-confirm` recomendados;
- ciclo de saída `suggestion → draft → validated-structure → audited → human-approved → published`;
- chat/MCP e ARA definidos como canais complementares;
- perfis e overrides esparsos recomendados;
- estudo baseline independente de LLM conectada;
- nenhuma tecnologia, schema, UI, coleta ou código autorizado.

Artefatos:

- `research/searches/2026-08-03-p3-autonomia-adaptacao-acessibilidade-IA-protocolo.md`;
- `research/data/p3-evidence-corpus-01.csv`;
- `research/data/p3-parameter-records-autonomy-adaptation-01.csv`;
- `research/data/p3-parameter-records-accessibility-ai-01.csv`;
- `research/data/p3-profile-comparison-01.csv`;
- `research/data/p3-decision-synthesis-01.json`;
- `research/pt-BR/p3-sintese-autonomia-adaptacao-acessibilidade-IA-01.md`;
- `research/library/referencias-autonomia-adaptacao-acessibilidade-IA.bib`.

### P4 — próximo

Instrumentação, condições experimentais, analytics e governança.

Deverá integrar P1–P3 e as hipóteses de variantes, composição por microssequências, materialização offline e dois canais de autoria. Não autoriza coleta ou dashboard.

### P5 — futuro

Autoria, revisão, reparo, publicação e políticas institucionais.

Deverá investigar GPT+MCP, ARA em tempo real, busca/reuso de microssequências, contexto autorizado, auditoria, comentários, forks, versões, provenance, publicação e papéis.

Pacotes não geram novas issues automaticamente.

## 7. Hipóteses transversais obrigatórias

Foram registradas como `discovered`, não normativas:

### 7.1 Níveis de parametrização

- runtime/configuração efetiva;
- conteúdo/materialização;
- composição e dependências;
- ciclo de vida e governança;
- condição experimental.

### 7.2 Composição por microssequências

Candidato concreto:

```text
microssequência versionada
→ posição em manifesto de curso versionado
→ snapshot local autossuficiente
→ estado contextual por curso/versão/posição/card
```

A Issue #6 decidirá o domínio; a #7 decidirá persistência e materialização.

### 7.3 Dois canais de autoria

- chat/MCP: intenção semântica, planejamento, construção, auditoria e reparo;
- ARA: renderização, versões, diffs, comentários, operações determinísticas, aprovação e publicação.

### 7.4 Perfis e overrides

Catálogo versionado + perfil nomeado + overrides esparsos + configuração efetiva. O usuário e o GPT não devem declarar o catálogo inteiro em cada artefato.

### 7.5 Administração leiga

Professores, tutores, pesquisadores e autodidatas devem administrar conceitos pedagógicos e operacionais, não detalhes de banco, Storage ou sincronização.

Essas hipóteses são entradas obrigatórias para P4, P5 e Issues #5–#8. Não autorizam arquitetura ou implementação.

## 8. Experimentos históricos

| Issue | PR | Estado | Interpretação |
|---|---:|---|---|
| #36 | #37 | fechado | contratos 0.1 não normativos |
| #38 | #39 | fechado | adapters descartáveis e achados negativos |
| #40 | #41 | concluído | contratos 0.2 e auditorias; não é o contrato do ARA |
| #42 | — | adiado | protocolo de bake-off sem resultado |

Podem informar falhas, testes e segurança. Não definem requisitos ou stack.

## 9. Classificação obrigatória das issues

Cada issue deve declarar:

- fase;
- tipo;
- autoridade;
- fontes governantes;
- dependências;
- saída verificável;
- não autorizações.

Vocabulário de autoridade:

- `governing`;
- `normative-pending`;
- `accepted-normative`;
- `decision-synthesis`;
- `evidence`;
- `historical-experiment`;
- `deferred`;
- `superseded`;
- `rejected`.

Uma issue pode conter mais de uma atividade somente quando a dependência é direta e as saídas permanecem separáveis.

## 10. Estrutura mínima

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

Deve registrar pergunta, decisão informada, método, fontes, datas, queries, amostragem, inclusão/exclusão, acesso, suficiência, extração, limitações, síntese e recomendação.

Não declarar pesquisa sistemática, exaustiva, causal ou duplamente revisada sem método correspondente. O proprietário não recebe corpus bruto como entrega final.

### Síntese e decisão

Deve comparar alternativas limitadas e inteligíveis, com benefícios, custos, evidência, riscos e reversibilidade. Estados: `recommended`, `accepted`, `deferred`, `rejected` ou `owner-decision-required`.

### Protótipo exploratório

Exige incerteza específica, hipótese, critério de falsificação, menor protótipo adequado, estado não normativo, regra de descarte/adoção e fase responsável pela decisão.

Não seleciona stack implicitamente nem vira dependência automática.

### Produto e domínio

Importa decisões aceitas e define atores, jornadas, entidades, estados, invariantes e lifecycle. Separa núcleo, extensão, conectado, experimental e fora de escopo.

### Arquitetura e ADR

Informa requisito, perfil, horizonte, workload, alternativas, segurança, privacidade, acessibilidade, offline, desempenho, operação, custo, migração, recomendação e decisão.

### UX

Referencia ator, jornada, estado, requisito, parâmetro, permissão, falha, mobile/desktop/offline, acessibilidade e avaliação. Implementação não inventa comportamento user-facing.

### Implementação para o Codex

Deve ser autossuficiente e identificar objetivo, release, requisito, domínio, ADR, contrato, jornada/tela, escopo, módulos, dados, comportamento, falhas, impactos, aceite, testes, documentação e rollback.

Quando requisito, ADR, contrato ou UX estiver ausente, a lacuna retorna à fase apropriada.

## 12. Rastreabilidade

```text
problema ou pergunta
→ evidência
→ extração/análise
→ síntese decisória
→ requisito aceito
→ domínio/política
→ ADR/arquitetura
→ jornada e tela
→ release
→ issue de implementação
→ código e testes
→ avaliação
```

Nem toda função exige todos os elos; omissões devem ser justificadas.

## 13. Pull requests e conclusão

Uma PR substancial registra issues, documentos atualizados, evidência ou decisão, validação, limitações, migração/rollback, encerramento e follow-up autorizado.

Uma issue só conclui quando entregas e critérios estão verificados, limitações são explícitas e nenhum item inacabado é transferido silenciosamente.

Bloqueio ou pesquisa parcial é `parcial`, `adiado` ou `inconclusivo`, não concluído.

## 14. Avaliação externa e reutilização acadêmica

O registro deve permitir distinguir intenção, método, evidência, mudanças, alternativas, decisões, incertezas, implementação e avaliação.

Dissertação, tese ou artigo deverá formular pergunta própria, selecionar corpus, citar fontes originais, distinguir desenvolvimento de efetividade educacional, declarar assistência por IA, respeitar privacidade/licenciamento e não apresentar planos como resultados.

## 15. Atualização documental

O conjunto principal permanece limitado a visão, programa de pesquisa e backlog.

Ao mudar decisão:

1. atualizar síntese;
2. registrar mudança de evidência ou trade-off;
3. aprovar decisão;
4. atualizar especificação;
5. atualizar este índice;
6. implementar somente depois;
7. preservar estado anterior no GitHub.

Não reescrever silenciosamente o passado para sugerir que a decisão final sempre existiu.
