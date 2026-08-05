# Idealização do ARA — índice do rascunho para discussão

**Estado:** rascunho não normativo, pré-desenvolvimento  
**Data de corte inicial:** 3 de agosto de 2026  
**Extensão atual:** 4 de agosto de 2026  
**Finalidade:** materializar uma proposta ampla para leitura, crítica e discussão com o proprietário antes de qualquer backlog definitivo.

## O que este conjunto representa

Este diretório descreve uma possível evolução do AraLearn para o ARA. Ele reúne:

- auditoria do produto e do código atual do AraLearn;
- funções a preservar, reformular, separar ou reconsiderar;
- idealização do funcionamento do ARA;
- alternativas de kernel, packages de resource, persistência, sincronização, BaaS e empacotamento móvel;
- rascunho amplo de backlog, ainda sem autoridade de execução;
- catálogo de telas, controles, estados e wireframes SVG deliberadamente simples;
- investigação de perfis modulares de agente, knowledge, prompts/templates, MCP, evals e contexto;
- curadoria participativa, diffs e analytics de autoria/sistema;
- analytics quantitativos, qualitativos e mistos assistidos por IA para pesquisa educacional;
- investigação de versionamento, retenção, deduplicação, armazenamento e custo operacional.

## O que este conjunto não representa

Não é:

- backlog definitivo;
- issue executável para Codex;
- arquitetura selecionada;
- autorização para desenvolvimento;
- promessa de cronograma;
- alegação de efetividade educacional;
- obrigação de reproduzir toda a complexidade atual do AraLearn;
- alegação de que o AraLearn possua uma arquitetura modular equivalente ao ARA;
- autorização para o GPT alterar prompts, knowledge, resources ou publicações autonomamente;
- representação do GPT como autoridade científica;
- seleção ou contratação de BaaS, banco ou object storage.

## Artefatos

1. [`aralearn-integral-audit-v1.pt-BR.md`](aralearn-integral-audit-v1.pt-BR.md) — leitura funcional e estrutural do predecessor.
2. [`ara-product-idealization-v1.pt-BR.md`](ara-product-idealization-v1.pt-BR.md) — experiência pretendida e ciclos do produto.
3. [`kernel-resource-modularity-v1.pt-BR.md`](kernel-resource-modularity-v1.pt-BR.md) — opções para kernel estável e resources independentes.
4. [`technology-and-baas-options-v1.pt-BR.md`](technology-and-baas-options-v1.pt-BR.md) — alternativas técnicas e trade-offs.
5. [`versioning-storage-economics-v1.pt-BR.md`](versioning-storage-economics-v1.pt-BR.md) — versionamento, retenção, storage e comparação inicial de deployments.
6. [`draft-backlog-v1.pt-BR.md`](draft-backlog-v1.pt-BR.md) — áreas A–P do backlog candidato amplo.
7. [`draft-backlog-agent-profiles-analytics-v1.pt-BR.md`](draft-backlog-agent-profiles-analytics-v1.pt-BR.md) — área Q original.
8. [`draft-backlog-agent-profiles-analytics-v2.pt-BR.md`](draft-backlog-agent-profiles-analytics-v2.pt-BR.md) — correção versionada de Q01, Q10 e Q26.
9. [`draft-backlog-versioning-storage-v1.pt-BR.md`](draft-backlog-versioning-storage-v1.pt-BR.md) — área R: versionamento e armazenamento sustentável.
10. [`screens-and-states-v1.pt-BR.md`](screens-and-states-v1.pt-BR.md) — telas, controles, estados e ligações para wireframes.
11. [`agent-profiles-participatory-analytics-v1.pt-BR.md`](agent-profiles-participatory-analytics-v1.pt-BR.md) — síntese integrada da frente de agentes e analytics.
12. [`agent-profile-administration-ux-notes-v1.pt-BR.md`](agent-profile-administration-ux-notes-v1.pt-BR.md) — notas para administração sem aparência técnica.
13. [`wireframes/`](wireframes/) — esquemas SVG minimalistas, não protótipos aprovados.

## Pré-backlog versionado

O pré-backlog v3 é a união explícita de:

- **A–P:** 171 itens preservados do rascunho inicial;
- **Q:** 26 itens sobre agentes, participação e analytics, com correção v2;
- **R:** 10 itens sobre versionamento, retenção, storage e economia operacional.

Total: **207 itens candidatos em 18 áreas**.

Manifesto: `research/data/ara-draft-backlog-v3-manifest.json`.

Registros estruturados principais:

- `research/data/ara-draft-backlog-v1.csv`;
- `research/data/ara-draft-backlog-agent-profiles-analytics-v2.csv`;
- `research/data/ara-draft-backlog-versioning-storage-v1.csv`;
- `research/data/versioning-storage-provider-evidence-v1.csv`;
- `research/data/versioning-storage-decision-synthesis-v1.json`;
- `research/data/agent-profile-object-candidates-v1.csv`;
- `research/data/agent-profile-role-candidates-v1.csv`;
- `research/data/agent-profile-scope-examples-v1.csv`;
- `research/data/agent-analytics-question-map-v1.csv`.

## Frentes focais

### Issue #77 — agentes e analytics

Investiga:

- decomposição da configuração monolítica do agente do AraLearn;
- perfis de domínio e coleções de conhecimento versionadas;
- prompts/templates, MCP resources/tools e contratos;
- contexto de leitura e escopo de escrita;
- evals orientados às tarefas-alvo do ARA;
- observações participativas e síntese argumentativa;
- analytics de autoria, sistema e pesquisa;
- GPT como pesquisador-assistente sob autoridade humana.

O AraLearn fornece jornadas, limitações e casos de contraste; não fornece fixtures equivalentes da arquitetura modular pretendida.

### Issue #79 — versionamento e armazenamento

Investiga:

- objetos versionados e imutáveis;
- metadata relacional versus artifact repository;
- content addressing e deduplicação;
- retenção e garbage collection;
- workloads de 10 mil, 100 mil e 1 milhão de revisões;
- Supabase Free/Pro, object storage externo, stacks portáteis e alternativas;
- disponibilidade, backup, exportação e restore;
- budgets compreensíveis ao proprietário.

Nenhuma das frentes autoriza implementação ou seleção de fornecedor.

## Linguagem de decisão

Cada item usa uma das classificações:

- **preservar:** valor demonstrado no AraLearn e compatível com o propósito do ARA;
- **reformular:** finalidade preservada, solução atual não tomada como definitiva;
- **separar:** responsabilidade atualmente acoplada que deve receber contrato/fronteira própria;
- **alternativa a comparar:** opção plausível ainda sem escolha;
- **adiar:** possibilidade legítima, mas não necessária para definir o produto-base;
- **rejeitar como padrão:** comportamento que contradiz o propósito ou cria custo/risco desnecessário;
- **questão aberta:** decisão que precisa de discussão, protótipo ou evidência adicional.

## Fontes e rastreabilidade

A auditoria usa como fontes primárias o código e a documentação atuais de `fabio-ara/AraLearn`. O predecessor é referência funcional e fonte de contraste, não implementação equivalente da arquitetura proposta.

Comparações externas usam documentação oficial, literatura acadêmica, standards e orientações institucionais, mantendo capacidade técnica, evidência educacional, custo e decisão de produto separados. Preços e quotas são fotografias temporais e devem ser reverificados.

As baselines das Issues #4–#8 continuam separadas. Os rascunhos e as Issues #77/#79 podem motivar revisões versionadas futuras; não as substituem silenciosamente.

## Perguntas para a revisão com o proprietário

1. Qual é o menor kernel que ainda preserva a identidade do AraLearn?
2. A microssequência deve ser o primeiro objeto reutilizável ou apenas a unidade inicial de composição?
3. Quais resources entram no pacote-base e quais podem ser instalados depois?
4. Quanto do painel administrativo deve existir no primeiro produto utilizável?
5. O usuário sem conta deve poder estudar e criar localmente?
6. O Supabase continua como primeira implantação, em plano gratuito ou pago, ou apenas como adapter de referência?
7. Metadata e artefatos devem usar o mesmo provider?
8. Que retenção é necessária para publicação, pesquisa e rollback?
9. Como comparar variantes sem duplicar conteúdo e sem introduzir diferenças acidentais?
10. Como decompor a configuração funcional do GPT/MCP do AraLearn sem inventar equivalência?
11. Quando um perfil de domínio é justificado?
12. Que contexto o agente lê integralmente ou por índice em cada escopo?
13. Como observações divergentes devem ser sintetizadas e decididas?
14. Quais análises quantitativas, qualitativas e mistas entram primeiro no ARA?
15. Qual workload deve governar a primeira decisão de infraestrutura?
