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
- analytics quantitativos, qualitativos e mistos assistidos por IA para pesquisa educacional.

## O que este conjunto não representa

Não é:

- backlog definitivo;
- issue executável para Codex;
- arquitetura selecionada;
- autorização para desenvolvimento;
- promessa de cronograma;
- alegação de efetividade educacional;
- obrigação de reproduzir toda a complexidade atual do AraLearn;
- autorização para o GPT alterar prompts, knowledge, resources ou publicações autonomamente;
- representação do GPT como autoridade científica.

## Artefatos

1. [`aralearn-integral-audit-v1.pt-BR.md`](aralearn-integral-audit-v1.pt-BR.md) — leitura funcional e estrutural do predecessor.
2. [`ara-product-idealization-v1.pt-BR.md`](ara-product-idealization-v1.pt-BR.md) — experiência pretendida e ciclos do produto.
3. [`kernel-resource-modularity-v1.pt-BR.md`](kernel-resource-modularity-v1.pt-BR.md) — opções para kernel estável e resources independentes.
4. [`technology-and-baas-options-v1.pt-BR.md`](technology-and-baas-options-v1.pt-BR.md) — alternativas técnicas e trade-offs.
5. [`draft-backlog-v1.pt-BR.md`](draft-backlog-v1.pt-BR.md) — áreas A–P do backlog candidato amplo.
6. [`draft-backlog-agent-profiles-analytics-v1.pt-BR.md`](draft-backlog-agent-profiles-analytics-v1.pt-BR.md) — área Q: perfis modulares de agente, curadoria participativa e analytics.
7. [`screens-and-states-v1.pt-BR.md`](screens-and-states-v1.pt-BR.md) — telas, controles, estados e ligações para wireframes.
8. [`agent-profiles-participatory-analytics-v1.pt-BR.md`](agent-profiles-participatory-analytics-v1.pt-BR.md) — síntese integrada da nova frente de pesquisa e produto.
9. [`agent-profile-administration-ux-notes-v1.pt-BR.md`](agent-profile-administration-ux-notes-v1.pt-BR.md) — notas para administração sem aparência técnica.
10. [`wireframes/`](wireframes/) — esquemas SVG minimalistas, não protótipos aprovados.

## Pré-backlog versionado

O pré-backlog v2 é a união explícita de:

- **A–P:** 171 itens preservados do rascunho inicial;
- **Q:** 26 itens sobre agentes, participação e analytics.

Total: **197 itens candidatos em 17 áreas**.

Manifesto: `research/data/ara-draft-backlog-v2-manifest.json`.

Registros estruturados:

- `research/data/aralearn-capability-preservation-matrix-v1.csv`;
- `research/data/ara-draft-backlog-v1.csv`;
- `research/data/ara-draft-backlog-agent-profiles-analytics-v1.csv`;
- `research/data/ara-screen-catalog-v1.csv`;
- `research/data/ara-technology-options-v1.csv`;
- `research/data/agent-profile-object-candidates-v1.csv`;
- `research/data/agent-profile-role-candidates-v1.csv`;
- `research/data/agent-profile-scope-examples-v1.csv`;
- `research/data/agent-analytics-question-map-v1.csv`.

## Nova frente de pesquisa

A Issue #77 investiga:

- decomposição da configuração monolítica do agente do AraLearn;
- perfis de domínio e coleções de conhecimento versionadas;
- prompts/templates, MCP resources/tools e contratos;
- contexto de leitura e escopo de escrita;
- evals, reprodutibilidade e regressões;
- observações participativas e síntese argumentativa;
- analytics de autoria, sistema e pesquisa;
- GPT como pesquisador-assistente sob autoridade humana.

Corpus inicial: 34 fontes, com protocolo, CSV, BibTeX, síntese de decisão e manifesto próprios.

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

A auditoria usa como fontes primárias o código e a documentação atuais de `fabio-ara/AraLearn`, especialmente contrato v4, arquitetura, persistência, MCP, resources, UI e testes. Comparações externas usam documentação oficial, literatura acadêmica, standards e orientações institucionais, mantendo capacidade técnica, evidência educacional e decisão de produto separadas.

As baselines das Issues #4–#8 continuam separadas. Este rascunho e a Issue #77 podem motivar revisões versionadas futuras; não as substituem silenciosamente.

## Perguntas para a revisão com o proprietário

1. Qual é o menor kernel que ainda preserva a identidade do AraLearn?
2. A microssequência deve ser o primeiro objeto reutilizável ou apenas a unidade inicial de composição?
3. Quais resources entram no pacote-base e quais podem ser instalados depois?
4. Quanto do painel administrativo deve existir no primeiro produto utilizável?
5. O usuário sem conta deve poder estudar e criar localmente?
6. O Supabase continua como primeira implantação ou apenas como adapter de referência?
7. O ARA precisa de sincronização genérica desde o primeiro corte?
8. Quais telas e parâmetros realmente precisam ser visíveis para cada perfil?
9. Como comparar variantes de curso sem introduzir diferenças acidentais?
10. Como decompor a configuração funcional do GPT/MCP do AraLearn sem perder qualidade?
11. Quando um perfil de domínio é justificado?
12. Que contexto o agente lê integralmente ou por índice em cada escopo?
13. Como observações divergentes devem ser sintetizadas e decididas?
14. Quais análises quantitativas, qualitativas e mistas entram primeiro no ARA?
15. Quais capacidades devem ser descartadas, simplificadas ou adiadas para evitar reconstruir um LMS ou framework genérico de agentes?
