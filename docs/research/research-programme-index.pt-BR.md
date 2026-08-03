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

### 3.1 Recuperação, flashcards, quizzes e espaçamento

**Estado:** `baseline-concluído` para parâmetros; `parcial` para algoritmos e progressão.

Fontes principais:

- Issue #14 / PR #15;
- Issues #16, #24, #26 e #28;
- Pacote P1;
- sínteses e datasets em `research/`.

Já é possível:

- separar produto, mecanismo, formato, agenda, feedback e consequência;
- distinguir recuperação, repetição, nota e progressão;
- representar objetivo temporal, resposta exigida e autoridade.

Faltam para P2:

- algoritmos e controle da revisão;
- mastery e progressão;
- adultos trabalhadores;
- transferência e retenção tardia;
- carga, adiamento, interrupção e abandono.

### 3.2 Resposta, tentativas, reveal, feedback e consequências

**Estado:** `concluído` pelo Pacote P1 para a primeira taxonomia.

Entregas:

- `research/searches/2026-08-03-p1-pratica-resposta-feedback-protocolo.md`;
- `research/data/p1-evidence-corpus-01.csv`;
- `research/data/p1-parameter-records-01.csv`;
- `research/data/p1-profile-comparison-01.csv`;
- `research/data/p1-decision-synthesis-01.json`;
- `research/pt-BR/p1-sintese-pratica-resposta-tentativas-feedback-consequencias-01.md`;
- bibliografia atualizada em `research/library/referencias-formatos-feedback.bib`.

Resultado:

- 21 dimensões aceitas para a primeira taxonomia;
- perfil AraLearn formalizado como referência não punitiva;
- perfis contrastantes para mastery pessoal, curso formativo, avaliação somativa, pesquisa e acessibilidade;
- precedência entre direitos, consentimento, protocolo, instituição, autor, estudante, default e disponibilidade técnica;
- telemetry de tentativas e confiança adiadas;
- ranking rejeitado como capacidade ativa da primeira versão;
- nenhum schema, adapter, UX ou código autorizado.

Lacunas preservadas:

- sequências ótimas entre pista, retry, reveal e item equivalente;
- respostas abertas e IA;
- acessibilidade de respostas estruturadas complexas;
- múltiplas tentativas e agregação em cursos formais;
- contextos brasileiros, portugueses e não WEIRD.

### 3.3 Programação móvel e feedback automatizado

**Estado:** `parcial`.

Fontes:

- Issue #18 / PR #20;
- benchmark de sistemas;
- experimentos históricos #36–#41.

Contribuições:

- distinguir ler, prever, completar, escrever, executar, depurar e projetar;
- separar tests, análise estática, diagnóstico, rubrica e revisão;
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

### P1 — prática, resposta, tentativas, revelação, feedback e consequências

**Estado:** `concluído`.

**Conclusão:** essas dimensões são combináveis e semanticamente independentes. O perfil AraLearn é preservado, mas não universalizado.

**Handoff para P2:**

- `practice.purpose`;
- `attempts.retry_target`;
- `hints.access`;
- `consequence.level`;
- perfil `self-directed-mastery`;
- incertezas sobre mastery, equivalência de itens e revisão posterior.

### P2 — progressão, sequenciamento, espaçamento, revisão, exemplos e scaffolding

**Estado:** próximo pacote.

**Pergunta:** quem controla a sequência, quando o estudante avança e como apoio e revisão são distribuídos?

Pesquisa focada:

- mastery e progressão;
- learner pacing e autonomia de sequência;
- spacing e interleaving;
- agenda, carga, adiamento e recuperação de revisão;
- worked examples, fading, hints e scaffolding;
- carga cognitiva e segmentação;
- interrupção, retomada e estudo fragmentado;
- item equivalente e evidência de domínio.

Entrega:

- parâmetros de progressão, sequenciamento, revisão e apoio;
- valores AraLearn e alternativas externas;
- autoridade e precedência;
- perfis contrastantes;
- recomendação para primeira taxonomia;
- aceitos, adiados e rejeitados;
- handoff para P3, #5 e #6.

Não autoriza algoritmo de produção, UX, banco, scheduler ou código.

### P3 — autonomia, autorregulação, adaptação, acessibilidade e assistência por IA

**Estado:** `parcial`.

Pesquisa necessária:

- self-regulated learning;
- learner control;
- adaptive learning;
- neurodiversidade e acomodações;
- IA em pistas, explicação, autoria e revisão;
- transparência, override, erro e autoridade.

Entrega:

- parâmetros e precedência;
- limites de adaptação;
- políticas de transparência;
- recomendações de IA por função.

### P4 — instrumentação, condições experimentais, analytics e governança

**Estado:** `parcial`.

Pesquisa necessária:

- learning analytics;
- vocabulários de eventos;
- protocolos e condições;
- consentimento, pseudonimização, retirada e retenção;
- métricas, constructos e inferências;
- personal analytics;
- interoperabilidade e exportação;
- ética e legislação.

Receberá do P1, entre outros, `telemetry.attempt_capture` e as inferências proibidas.

### P5 — autoria, revisão, reparo, publicação e políticas institucionais

**Estado:** `parcial`.

Pesquisa necessária:

- autoria humano–IA;
- quality assurance;
- proveniência e source anchoring;
- revisão por pares e especialistas;
- permissões e workspaces;
- publicação, versionamento e retirada;
- contextos institucionais.

Entrega:

- parâmetros de autoria e governança;
- perfis pessoais e institucionais;
- limites de autoridade do agente;
- requisitos candidatos para #6.

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

A próxima entrega é o **Pacote P2 da Issue #4**.

A Issue #4 permanece aberta até P2–P5 e a síntese final da taxonomia. Nenhum código, schema de produção, adapter ou UX é autorizado durante esses pacotes.
