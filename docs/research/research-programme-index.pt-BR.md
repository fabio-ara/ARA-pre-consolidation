# Índice canônico do programa de pesquisa

**Estado:** canônico para planejamento de pesquisa  
**Idioma:** `pt-BR`  
**Última revisão:** 3 de agosto de 2026

## 1. Finalidade

Este índice organiza a pesquisa necessária para definir o ARA sem transferir ao proprietário o trabalho de interpretar um corpus bruto.

Cada frente deve resultar em:

- conclusão principal;
- caminho recomendado;
- alternativas relevantes;
- alternativas rejeitadas ou adiadas;
- justificativa;
- riscos;
- incertezas que possam alterar a recomendação;
- implicações para parametrização, produto, arquitetura, UX ou avaliação.

A pesquisa é ampla e finita. O objetivo é evidência suficiente para decidir, não exaustão universal.

## 2. Estados de cobertura

| Estado | Significado |
|---|---|
| `concluído` | Pacote decisório entregue e incorporado à fase corrente. |
| `baseline-concluído` | Existe síntese suficiente para iniciar modelagem, com limitações registradas. |
| `parcial` | Há evidência útil, mas falta síntese focada para decisão. |
| `exploratório` | Existem precedentes ou literatura inicial, insuficientes para decisão normativa. |
| `não-iniciado` | A frente precisa de protocolo e corpus próprios. |
| `contínuo` | A pesquisa permanece aberta e é atualizada quando decisões futuras exigirem. |

## 3. Evidência já produzida

### 3.1 Recuperação, resposta e feedback

**Estado:** P1 concluído para a primeira taxonomia.

Fontes principais:

- Issues #14, #16, #17, #24, #26 e #28;
- síntese da Issue #30;
- auditoria do AraLearn;
- Pacote P1 / PR #45.

Entregas P1:

- `research/searches/2026-08-03-p1-pratica-resposta-feedback-protocolo.md`;
- `research/data/p1-evidence-corpus-01.csv`;
- `research/data/p1-parameter-records-01.csv`;
- `research/data/p1-profile-comparison-01.csv`;
- `research/data/p1-decision-synthesis-01.json`;
- `research/pt-BR/p1-sintese-pratica-resposta-tentativas-feedback-consequencias-01.md`;
- `research/library/referencias-formatos-feedback.bib`.

Resultado:

- prática, resposta, validade, crédito, tentativas, reveal, feedback, consequência e acessibilidade são dimensões distintas;
- perfil AraLearn preservado como referência não punitiva;
- telemetry de tentativas e confiança adiadas;
- ranking público rejeitado na primeira taxonomia;
- nenhum schema, adapter, UX ou código autorizado.

### 3.2 Progressão, sequência, revisão e apoio

**Estado:** P2 concluído para a primeira taxonomia.

Entregas P2:

- `research/searches/2026-08-03-p2-progressao-sequenciamento-revisao-protocolo.md`;
- `research/data/p2-evidence-corpus-01.csv`;
- `research/data/p2-parameter-records-01.csv`;
- `research/data/p2-profile-comparison-01.csv`;
- `research/data/p2-decision-synthesis-01.json`;
- `research/pt-BR/p2-sintese-progressao-sequenciamento-revisao-scaffolding-01.md`;
- `research/library/referencias-progressao-sequenciamento.bib`.

Resultado:

- 36 dimensões aceitas;
- conclusão estrutural separada de mastery;
- mastery por critério exige evidência, escopo, remediação, override e rechecagem;
- autoridade de sequência separada de ritmo;
- spacing separado de interleaving;
- schedule, intervalo, horizonte, carga e adiamento separados;
- exemplos resolvidos e scaffolds modelados por disponibilidade, posição, tipo, acesso e fading;
- segmentação coerente e retomada não punitiva preservadas;
- scheduler, mastery estimator, branching, struggle detection e fading automático adiados;
- nenhum algoritmo, schema, UX ou código autorizado.

### 3.3 Programação móvel e feedback automatizado

**Estado:** `parcial`.

Fontes:

- Issue #18 / PR #20;
- benchmark de sistemas;
- experimentos históricos #36–#41.

Contribuições:

- distinguir ler, prever, completar, escrever, executar, depurar e projetar;
- separar testes, análise estática, diagnóstico, rubrica e revisão;
- não equiparar execução a aprendizagem.

Programação executável permanece candidata a extensão, não requisito do primeiro recorte.

### 3.4 Representações múltiplas e resources estruturados

**Estado:** `exploratório` com material comparativo forte.

Fontes:

- #31 / PR #32;
- #33/#34 / PR #35;
- #30 / PR #43;
- literatura de representações múltiplas.

Conclusões:

- quantidade de tipos não é qualidade;
- representação, atividade, resposta, validação e feedback precisam permanecer distinguíveis;
- gramáticas de domínio podem ser legítimas;
- coordenação, redundância e acessibilidade exigem pesquisa própria.

A decisão de domínio e arquitetura pertence a #6 e #7.

### 3.5 Sistemas, gêneros e extensibilidade

**Estado:** `exploratório` suficiente para excluir extremos, insuficiente para arquitetura.

Fontes:

- #33 e #34 / PR #35;
- 21 sistemas e 16 fontes acadêmicas;
- histórico #36–#42.

Conclusões:

- ARA não é apenas flashcards;
- não deve reivindicar ITS, LMS, simulação ou avaliação geral sem capacidades próprias;
- extensibilidade requer governança;
- plugins arbitrários ampliam segurança, operação e acessibilidade.

Faltam modelos de kernel, packages, descoberta, carregamento seletivo por MCP, migração e comparação de stacks após #6.

## 4. Pacotes da primeira taxonomia — Issue #4

A Issue #4 é executada por pacotes sucessivos e uma síntese integrada final. Pacotes não geram novas issues automaticamente.

### P1 — concluído

**Escopo:** prática, resposta, tentativas, revelação, feedback e consequências.

**Handoff preservado:**

- `practice.purpose`;
- `attempts.retry_target`;
- `hints.access`;
- `consequence.level`;
- perfil `self-directed-mastery`;
- incertezas sobre mastery, equivalência de itens e revisão posterior.

### P2 — concluído

**Escopo:** progressão, sequenciamento, espaçamento, revisão, exemplos resolvidos, scaffolding, segmentação e retomada.

**Handoff para P3:**

- autoridade e shared control;
- learner pacing versus sequence control;
- expertise e adaptação;
- acesso e fading de scaffolds;
- perfis `novice-support-overlay`, `expert-efficiency-overlay` e `interruptible-mobile-overlay`;
- candidatos `adaptive.mastery_estimator`, `adaptive.branching`, `automatic.struggle_detection`, `automatic.scaffold_fading` e `generative.resumption_summary`;
- proibição de inferir expertise, struggle ou disengagement de sinais brutos.

### P3 — próximo pacote

**Escopo:** autonomia, autorregulação, adaptação, acessibilidade e assistência por IA.

**Pergunta:** como separar escolha do estudante, acomodação, política institucional, condição experimental, adaptação algorítmica e assistência por IA sem retirar autoridade humana ou criar inferências opacas?

Pesquisa focada:

- self-regulated learning;
- learner control e shared control;
- adaptive learning;
- expertise, diagnóstico e transparência;
- neurodiversidade e acomodações;
- Universal Design for Learning e acessibilidade;
- IA em pistas, explicação, autoria e revisão;
- riscos de dependência, erro, viés, privacidade e autoridade;
- override, contestação e fallback offline;
- perfis pessoais, formais e experimentais.

Entrega:

- parâmetros de autonomia, adaptação, acessibilidade e IA;
- valores AraLearn e alternativas externas;
- autoridade, consentimento, precedência e transparência;
- perfis contrastantes;
- aceitos, adiados e rejeitados;
- handoff para P4, #5, #6, #7 e #8.

Não autoriza modelo adaptativo, integração de LLM, coleta de dados, UX, schema ou código.

### P4 — futuro

**Escopo:** instrumentação, condições experimentais, analytics e governança.

Receberá:

- `telemetry.attempt_capture` e inferências proibidas do P1;
- snapshots, claims, schedules, deferral e constructos de struggle/expertise do P2;
- transparência, consentimento e adaptação do P3.

### P5 — futuro

**Escopo:** autoria, revisão, reparo, publicação e políticas institucionais.

Pesquisa necessária:

- autoria humano–IA;
- quality assurance;
- proveniência e source anchoring;
- revisão por pares e especialistas;
- permissões e workspaces;
- publicação, versionamento e retirada;
- contextos institucionais.

## 5. Frentes posteriores

### Issue #5 — pesquisa, instrumentos e analytics

Exigirá literatura metodológica sobre:

- modelos de investigação;
- participantes e consentimento;
- condições e assignment;
- instrumentos quantitativos e qualitativos;
- eventos, medidas e constructos;
- interpretação e inferências proibidas;
- exportação e equivalência entre implantações.

### Issue #6 — produto e domínio

Exigirá pesquisa e síntese sobre:

- modelagem de domínio;
- lifecycle de conteúdo;
- versionamento e proveniência;
- biblioteca e organização;
- colaboração e capacidades;
- portabilidade e interoperabilidade;
- requisitos institucionais.

Não será apenas uma sessão de modelagem técnica.

### Issue #7 — arquitetura e stack

Exigirá comparação de:

- arquiteturas modulares e sistemas de packages;
- web, mobile e offline;
- persistência e sincronização;
- schemas e contratos;
- carregamento dinâmico e MCP;
- segurança de extensões e runtimes;
- managed e self-hosted;
- observabilidade, backup e atualização;
- stacks candidatas, custos e exit strategy.

Saída: recomendações e ADRs, não catálogo bruto.

### Issue #8 — UX/UI

Exigirá pesquisa sobre mobile learning UX, progressive disclosure, configuração complexa, acessibilidade, interrupção, autoria, pesquisa/admin, multilinguismo e métodos de avaliação.

### Issue #9 — releases e implementação

Exigirá boas práticas de release slicing, CI/CD, quality gates, segurança, acessibilidade, migração, rollback, evidence packages e colaboração aberta.

## 6. Critérios gerais de suficiência

Uma frente pode avançar quando:

1. possui síntese confiável ou conjunto justificado de fontes primárias;
2. contém casos contrastantes e limitações;
3. cobre stakeholders e contextos decisivos;
4. duas adições sucessivas não criam categoria decisiva nem alteram a recomendação;
5. incertezas remanescentes estão explícitas;
6. a decisão pode evoluir sem perder rastreabilidade;
7. nenhuma fonte indispensável é substituída por suposição.

## 7. Papel de Fabio

Fabio receberá síntese, recomendação, justificativa, alternativas, riscos e incertezas decisivas.

Não receberá como produto final lista extensa de artigos, catálogo sem recomendação ou pergunta genérica para arquitetar sozinho.

Sua decisão será solicitada somente diante de conflito estratégico ou valorativo não resolvido pela evidência.

## 8. Próxima entrega verificável

A próxima entrega é o **Pacote P3 da Issue #4**.

A Issue #4 permanece aberta até P3–P5 e a síntese final da taxonomia. Nenhum código, schema de produção, adapter ou UX é autorizado durante esses pacotes.
