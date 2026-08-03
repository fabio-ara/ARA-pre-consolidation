# Backlog e fluxo de trabalho do ARA

**Estado:** documento operacional vigente  
**Idioma:** `pt-BR`  
**Última revisão:** 3 de agosto de 2026  
**Público:** proprietário do projeto, Codex e outros agentes, colaboradores, avaliadores externos e investigação acadêmica.

## 1. Função e navegação principal

As Issues do GitHub são as unidades de trabalho autorizadas do ARA. Devem ser autossuficientes para sua finalidade: pesquisa, síntese, decisão, especificação, protótipo exploratório, implementação, validação ou avaliação.

A navegação principal possui somente três documentos:

1. `docs/vision/product-vision.pt-BR.md` — produto pretendido;
2. `docs/research/research-programme-index.pt-BR.md` — pesquisa concluída, lacunas e pacotes decisórios;
3. este documento — fases, autoridade, rastreabilidade, issues e regras operacionais.

Relatórios, datasets, protocolos, ADRs, especificações e planos de release são entregas das issues correspondentes. Não devem repetir integralmente os três documentos principais.

## 2. Modelo de registro e autoridade

### 2.1 Classes de fonte

- **Fonte histórica primária:** documentos iniciais, histórico de edição das issues, comentários, PRs, diffs, commits, código, exports, hashes, datasets, testes e registros oficiais. Demonstra o que efetivamente ocorreu, mas não constitui automaticamente requisito atual.
- **Evidência:** protocolo, busca, triagem, extração, revisão, benchmark, auditoria ou avaliação. Informa recomendações; não autoriza implementação diretamente.
- **Síntese decisória:** integra evidência, alternativas, recomendação, riscos e incertezas. Orienta a fase normativa seguinte.
- **Especificação aprovada:** taxonomia, requisito, modelo de domínio, arquitetura, ADR, contrato, UX ou plano de release aprovado. Governa o trabalho posterior no respectivo escopo.
- **Registro de implementação:** issue de implementação, código, teste, migração, evidência de release e documentação operacional.

### 2.2 Precedência

Para comportamento atual e engenharia, use esta ordem:

1. especificação aprovada da fase relevante;
2. ADR ou decisão estratégica aprovada;
3. issue operacional vigente e este índice;
4. síntese decisória aceita;
5. evidência e datasets;
6. issue, PR ou protótipo histórico;
7. conversa ou memória não registrada.

Para afirmar o que ocorreu historicamente, prevalecem as fontes históricas primárias. Para afirmações bibliográficas, prevalecem a fonte citada, o registro de extração e o estado de acesso.

A ausência de classificação não torna um artefato normativo.

## 3. Caminho linear do projeto

```text
#3 pesquisa bibliográfica, comparativa e contextual
→ síntese crítica e recomendação
→ #4 taxonomia de parametrização
→ #5 protocolos, instrumentação e analytics
→ #6 requisitos e modelo de domínio
→ #7 arquitetura, stack, perfis e ADRs
→ #8 UX/UI e acessibilidade
→ #9 releases funcionais
→ issues de implementação autossuficientes para o Codex
→ validação e avaliação
```

Uma possibilidade encontrada na pesquisa não se transforma automaticamente em requisito, contrato, protótipo, biblioteca ou implementação.

A Issue #2 prossegue em paralelo quando questões jurídicas, institucionais ou de identidade se tornam relevantes à decisão.

## 4. Issues principais

| Issue | Fase | Tipo | Estado | Autoridade e saída esperada |
|---|---:|---|---|---|
| #10 | 00 | governança e roadmap | aberta | Coordena fases, gates e regras. Deve apontar para os três documentos principais. |
| #2 | 10 | pesquisa jurídica e identidade | aberta/paralela | Produzirá a base de propriedade intelectual, licenciamento, marca e questões institucionais. |
| #3 | 20 | programa de evidência | aberta/contínua | Governa protocolos, buscas, corpora, bibliografia e sínteses. Não precisa ser “encerrada para sempre”. |
| #4 | 30 | taxonomia de parametrização | aberta/ativa | Produzirá parâmetros, perfis, maturidade, autoridade, precedência, conflitos e handoff para #5 e #6. |
| #5 | 40 | protocolos e analytics | futura | Produzirá condições, instrumentos, eventos, medidas, governança e inferências permitidas. |
| #6 | 50 | produto e domínio | futura | Aceitará ou rejeitará conceitos e definirá atores, jornadas, entidades, estados e capacidades normativas. |
| #7 | 60 | arquitetura e stack | futura | Separará requisitos duráveis, primeiro recorte, perfis e hipóteses; registrará decisões por ADR. |
| #8 | 70 | UX, acessibilidade e sistema visual | futura | Definirá jornadas, telas, estados, transições e avaliação antes da implementação user-facing. |
| #9 | 80 | releases e implementação | futura | Produzirá releases funcionais e issues executáveis pelo Codex. |

## 5. Pesquisa e sínteses concluídas

| Issue | PR(s) | Resultado | Uso atual |
|---|---:|---|---|
| #14 | #15 | primeira síntese de revisões centrais | evidência inicial sobre recuperação, quizzes, espaçamento e feedback |
| #16 | #21–#23 | busca formal PubMed/ERIC e deduplicação | corpus formal de 1.471 publicações |
| #17 | #19 | formatos de resposta e feedback | evidência-base do P1 |
| #18 | #20 | programação móvel 2023–2026 | evidência parcial e situada |
| #24 | #25 | triagem de título e resumo | relevância inicial, não avaliação de qualidade |
| #26 | #27 | extração do corpus prioridade A | classificação e extração com estados de acesso explícitos |
| #28 | #29 | sobreposição de estudos primários | prevenção de dupla contagem e núcleo não redundante |
| #30 | #43 | síntese AraLearn + horizonte externo | direção: referência AraLearn, descoberta ampla, normatização seletiva e extensibilidade governada |
| #31 | #32 | auditoria dos resources do AraLearn | referência implementada, não decisão automática de migração |
| #33–#34 | #35 | benchmark de sistemas e gêneros | precedentes, contrastes e riscos; não requisitos automáticos |

## 6. Issue #4 — estado dos pacotes

### P1 — concluído

**Escopo:** prática, resposta, tentativas, revelação, feedback, consequências e precedência de acessibilidade.  
**PR:** #45  
**Commit incorporado em `main`:** `eb3c6bdc16685a4d8e3b912e96b662d4735e4cdb`  
**Estado:** pacote concluído, pendente apenas da síntese final da Issue #4 com P2–P5.

Artefatos preservados integralmente:

- `research/searches/2026-08-03-p1-pratica-resposta-feedback-protocolo.md`;
- `research/data/p1-evidence-corpus-01.csv`;
- `research/data/p1-parameter-records-01.csv`;
- `research/data/p1-profile-comparison-01.csv`;
- `research/data/p1-decision-synthesis-01.json`;
- `research/pt-BR/p1-sintese-pratica-resposta-tentativas-feedback-consequencias-01.md`;
- `research/library/referencias-formatos-feedback.bib`;
- atualização de `docs/research/research-programme-index.pt-BR.md`.

Resultados vigentes do P1:

- 21 dimensões aceitas para a primeira taxonomia;
- perfil `aralearn-reference` preservado como configuração não punitiva, não como default universal;
- perfis/overlays contrastantes: `self-directed-mastery`, `formal-formative-course`, `summative-institutional`, `research-condition` e `accessibility-overlay`;
- prática para aprender separada de medição e avaliação consequencial;
- formato de resposta separado de demanda cognitiva;
- validade, autoridade, crédito, tentativas, pistas, reveal, feedback e consequências modelados como dimensões combináveis;
- acessibilidade com precedência superior a preferências ordinárias;
- coleta de tentativas desligada por padrão e adiada para P4/#5;
- confiança e avaliação automática autoritativa de respostas abertas adiadas;
- ranking público rejeitado na primeira taxonomia ativa;
- nenhum schema, adapter, stack, UX, telemetry ou código autorizado.

O P1 não deve ser reduzido, reinterpretado ou substituído por resumos posteriores. Em caso de dúvida, prevalecem os artefatos listados e a síntese decisória estruturada.

### P2 — próximo pacote

**Escopo:** progressão, sequenciamento, espaçamento, revisão, exemplos resolvidos e scaffolding.

Deve pesquisar e recomendar, sem implementar:

- mastery e critérios de progressão;
- learner pacing e autoridade sobre a sequência;
- spacing e interleaving;
- agenda, carga, adiamento e retomada de revisão;
- exemplos resolvidos, fading, hints e scaffolding;
- carga cognitiva, segmentação e estudo fragmentado;
- item equivalente e evidência de domínio.

### P3–P5

- **P3:** autonomia, autorregulação, adaptação, acessibilidade e assistência por IA;
- **P4:** instrumentação, condições experimentais, analytics e governança;
- **P5:** autoria, revisão, reparo, publicação e políticas institucionais.

Pacotes são subdivisões operacionais da Issue #4; não geram novas issues automaticamente.

## 7. Experimentos históricos

| Issue | PR | Classificação | Interpretação vigente |
|---|---:|---|---|
| #36 | #37 | `historical-experiment` | contratos 0.1 de quatro famílias; não normativos |
| #38 | #39 | `historical-experiment` | adapters descartáveis e achados negativos; não produção |
| #40 | #41 | `historical-experiment` concluído | contratos 0.2, migrações e auditorias; não é o contrato do ARA |
| #42 | — | `deferred` | protocolo de bake-off preservado, sem resultado de runtime |

Esses trabalhos podem informar falhas, testes, segurança e padrões. Não selecionam stack, não definem requisitos e só podem retornar mediante necessidade aceita em #6 e pergunta arquitetural em #7.

## 8. Classificação obrigatória das issues

Cada issue deve declarar:

- **fase:** `00`, `10`, `20`, `25`, `30`, `40`, `50`, `60`, `70`, `80` ou `90`;
- **tipo:** governança, pesquisa jurídica, protocolo, extração, análise comparativa, síntese decisória, taxonomia, especificação de produto, arquitetura/ADR, UX, protótipo exploratório, implementação, validação ou avaliação;
- **autoridade:** `governing`, `normative-pending`, `accepted-normative`, `decision-synthesis`, `evidence`, `historical-experiment`, `deferred`, `superseded` ou `rejected`;
- **fontes governantes**;
- **dependências**;
- **saída canônica ou verificável**;
- **não autorizações**.

Uma issue pode conter mais de uma atividade somente quando a dependência é direta e as saídas permanecem separáveis.

## 9. Estrutura mínima de toda issue

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

Efeitos transversais relevantes devem cobrir, conforme o caso: pedagogia, validade de pesquisa, privacidade e ética, acessibilidade, segurança, mobile/offline, desempenho e custo, licenciamento e autoria por MCP.

## 10. Regras por tipo de trabalho

### 10.1 Pesquisa

Uma issue de pesquisa deve registrar:

- pergunta e decisão que pretende informar;
- protocolo ou método;
- bases, fontes, idiomas, datas e queries exatas quando aplicável;
- amostragem de plataformas, domínios, stakeholders e implantações;
- inclusão, exclusão, suficiência ou saturação;
- estado de acesso: texto integral, manuscrito, resumo, metadados, citação secundária, documentação oficial, experiência pessoal, código/schema primário ou fonte inacessível;
- extração, limitações, síntese e recomendação.

Não se deve declarar pesquisa sistemática, exaustiva, causal ou duplamente revisada sem método correspondente.

A entrega final deve incluir conclusão, caminho recomendado, alternativas adiadas/rejeitadas, justificativa, riscos, incertezas decisivas e classificação das implicações. O proprietário não deve receber um corpus bruto como produto final.

### 10.2 Síntese e decisão

A síntese deve comparar alternativas limitadas e inteligíveis, incluindo benefícios, custos, evidência, riscos e reversibilidade. O estado final deve ser `recommended`, `accepted`, `deferred`, `rejected` ou `owner-decision-required`.

A escolha do proprietário somente é solicitada quando persiste conflito estratégico, ético, pedagógico ou valorativo que a evidência não resolve. A recomendação deve ser explícita.

### 10.3 Protótipo exploratório

Exige:

- incerteza específica;
- evidência ou hipótese;
- motivo pelo qual análise não basta;
- critério de falsificação;
- menor protótipo adequado;
- estado não normativo;
- regra de descarte, retenção ou adoção;
- fase posterior com autoridade para aceitar o resultado.

Não pode selecionar stack implicitamente, criar contrato permanente por conveniência, tornar-se dependência automática, ocultar riscos ou alegar efetividade educacional.

### 10.4 Produto e domínio

Deve importar parâmetros e decisões aceitos, definir atores, jornadas, entidades, estados, invariantes e lifecycle, classificar núcleo/extensão/conectado/experimental/fora de escopo e registrar questões que pertencem à arquitetura ou UX.

### 10.5 Arquitetura e ADR

Deve informar requisito servido, perfil de implantação, caráter durável ou de primeiro recorte, workloads, alternativas, segurança, privacidade, acessibilidade, offline, desempenho, operação, custo, saída/migração, protótipo usado, recomendação e decisão aceita.

Popularidade, uso atual no AraLearn ou existência de protótipo não bastam como justificativa.

### 10.6 UX

Deve referenciar ator, jornada, estado/transição, requisito, parâmetro, permissão, falha, mobile/desktop/offline, acessibilidade, protótipo e método de avaliação.

A implementação não pode inventar comportamento user-facing ausente de especificação aprovada.

### 10.7 Implementação para o Codex

A issue deve ser autossuficiente e identificar:

- objetivo e valor para o usuário;
- release e requisito de origem;
- conceito de domínio;
- ADR ou arquitetura aceita;
- versão de contrato;
- jornada e tela, quando aplicável;
- escopo e exclusões;
- módulos e dados afetados;
- comportamento esperado e falhas;
- impacto de migração, segurança, privacidade, acessibilidade, offline e desempenho;
- critérios de aceite;
- plano de testes;
- documentação;
- rollback ou recuperação.

Quando requisito, ADR, contrato ou UX necessário estiver ausente, o Codex não deve inventá-lo: a lacuna retorna à fase apropriada.

## 11. Cadeia de rastreabilidade

Uma função normativa deve ser recuperável por:

```text
problema ou pergunta
→ evidência
→ extração/análise
→ síntese decisória
→ requisito aceito
→ conceito de domínio/política
→ ADR/arquitetura
→ jornada e tela
→ release
→ issue de implementação
→ código e testes
→ avaliação
```

Nem toda função exige todos os elos; qualquer omissão deve ser justificada.

## 12. Pull requests e conclusão

Uma PR substancial deve registrar:

- issues atendidas;
- especificações ou índices atualizados;
- evidência produzida ou decisão implementada;
- validação executada;
- limitações;
- efeitos de migração e rollback;
- se encerra a issue;
- follow-up sem abertura automática, salvo autorização.

Uma issue só é concluída quando entregas e critérios de aceite estão verificados, limitações são explícitas, o índice foi atualizado quando necessário e nenhum critério inacabado foi transferido silenciosamente.

Bloqueio ambiental ou pesquisa parcial deve ser classificado como parcial, adiado ou inconclusivo, não como concluído.

## 13. Avaliação externa e reutilização acadêmica

O registro deve permitir distinguir:

- intenção inicial;
- método e evidência;
- mudanças e justificativas;
- alternativas consideradas;
- decisões vigentes;
- incertezas;
- implementação e avaliação realizadas.

Dissertação, tese ou artigo futuro deverá formular pergunta própria, selecionar o corpus relevante, citar literatura original, distinguir desenvolvimento de efetividade educacional, declarar assistência por IA, respeitar privacidade/licenciamento e não apresentar planos como resultados.

## 14. Política documental e atualização

O conjunto principal permanece limitado a visão, programa de pesquisa e backlog. Um novo documento transversal exige função exclusiva, responsável de manutenção e ausência demonstrável de duplicação.

Ao mudar uma decisão:

1. atualizar ou produzir síntese decisória;
2. registrar por que evidência ou trade-off mudou;
3. aprovar a decisão revisada;
4. atualizar a especificação pertinente;
5. atualizar este índice;
6. criar migração ou implementação somente depois;
7. preservar o estado anterior no histórico do GitHub.

Não se deve reescrever silenciosamente o passado para sugerir que a decisão final sempre existiu.
