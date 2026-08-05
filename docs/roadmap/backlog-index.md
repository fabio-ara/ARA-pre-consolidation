# Backlog e fluxo de trabalho do ARA

**Estado:** pré-desenvolvimento; brainstorming, pesquisa e revisão  
**Idioma:** `pt-BR`  
**Última revisão:** 4 de agosto de 2026

## 1. Estado das fases

```text
#3 evidência contínua
→ #4 taxonomia — concluída
→ #5 pesquisa/analytics — concluída como baseline v1
→ #6 produto/domínio — baseline conceitual
→ #7 arquitetura — baseline conceitual
→ #8 UX/UI — baseline conceitual e protótipo não produtivo
→ #77 perfis de agente, participação e analytics — pesquisa focal ativa
→ #9 planejamento de implementação — futuro, não iniciado
```

A conclusão de uma baseline significa que existe material suficiente para discussão e revisão. Não significa que o projeto entrou em desenvolvimento. A Issue #77 investiga uma extensão e possível revisão versionada das baselines; não é issue de código.

## 2. Trabalho atual

O trabalho atual permanece aberto a brainstorming, investigação bibliográfica, análise do AraLearn, análise de repositórios, revisão de hipóteses e clarificações do proprietário.

A frente focal ativa é a Issue #77, que investiga:

- configuração modular e versionada do agente;
- perfis de domínio e knowledge collections;
- prompts/templates, MCP resources/tools e contratos;
- contexto de leitura e escopo de escrita;
- observações participativas, diffs e reparos;
- analytics de autoria/sistema e pesquisa educacional;
- análise quantitativa, qualitativa e mista assistida por GPT;
- papéis, autoridade, evals, reprodutibilidade, privacidade e UX administrativa.

Não existe bloqueio administrativo, branch protegida obrigatória, release ativa ou issue de código autorizada.

## 3. Pré-backlog v2 para discussão

O índice [`docs/ideation/README.md`](../ideation/README.md) reúne a idealização integrada do produto depois da análise do AraLearn atual.

O pré-backlog v2 é composto por:

- áreas A–P: 171 itens preservados de `docs/ideation/draft-backlog-v1.pt-BR.md`;
- área Q: 26 itens de `docs/ideation/draft-backlog-agent-profiles-analytics-v1.pt-BR.md`.

Total: **197 itens candidatos em 17 áreas**.

Manifesto: `research/data/ara-draft-backlog-v2-manifest.json`.

O conjunto também contém:

- auditoria funcional e estrutural do predecessor;
- mapa preservar/reformular/separar/adiar;
- proposta de kernel estável e packages independentes de resource/practice;
- alternativas de BaaS, store local, sync, hosting, framework e app Android;
- catálogo de 37 telas e estados;
- 12 wireframes SVG simples;
- corpus inicial de 34 fontes para a Issue #77;
- registries de objetos, papéis, escopos, analytics, evals e questões abertas.

Os arquivos do pré-backlog não possuem prioridade, release, sprint, bloqueio ou autorização para Codex. Sua função é permitir discussão item a item, investigação e futura seleção.

## 4. Baselines e extensões de consulta

Baselines:

- `research/data/issue4-final-artifact-manifest-v1.json`;
- `research/data/issue5-artifact-manifest-v1.json`;
- `research/data/issue6-artifact-manifest-v1.json`;
- `research/data/issue7-artifact-manifest-v1.json`;
- `research/data/issue8-artifact-manifest-v1.json`;
- `research/data/ara-ideation-draft-manifest-v1.json`;
- `docs/product/product-requirements-v1.md`;
- `docs/product/domain-model-v1.md`;
- `docs/architecture/reference-architecture-v1.md`;
- `docs/ux/ux-specification-v1.md`.

Extensão em pesquisa:

- `docs/ideation/agent-profiles-participatory-analytics-v1.pt-BR.md`;
- `research/searches/2026-08-04-agent-profiles-participatory-analytics-protocol.md`;
- `research/data/agent-profiles-participatory-analytics-manifest-v1.json`;
- `research/data/ara-draft-backlog-v2-manifest.json`.

Esses documentos são propostas e evidências, sujeitas a revisão versionada antes da implementação.

## 5. Dependências conceituais da nova área Q

A sequência candidata é:

1. inventariar a configuração monolítica do AraLearn;
2. definir objetos e resolução de configuração;
3. criar fixtures e evals de continuidade;
4. validar um primeiro perfil de domínio;
5. validar contexto de leitura e escopo de escrita;
6. modelar observações, síntese, diffs e reparos;
7. separar analytics operacionais, educacionais e de pesquisa;
8. aprofundar workbenches quantitativo, qualitativo e misto;
9. revisar requisitos, domínio, arquitetura e UX;
10. somente depois selecionar um primeiro escopo implementável.

Nenhuma dependência conceitual é bloqueio administrativo de GitHub.

## 6. Entrada futura em desenvolvimento

A Issue #9 somente deverá ser executada após decisão explícita do proprietário de iniciar a fase de desenvolvimento.

Nesse momento, e não antes, será necessário:

- revisar o pré-backlog v2 e registrar decisões;
- revisar novamente requisitos, domínio, arquitetura e UX;
- decidir o primeiro escopo implementável;
- criar releases e issues executáveis novas;
- escolher quality gates proporcionais ao estágio;
- decidir se qualquer proteção de branch realmente agrega valor;
- definir migração, rollback e evidência de release.

Nenhuma dessas escolhas é pré-condição para continuar pesquisando ou refinando o produto.

## 7. Regras permanentes

- possibilidade descoberta não se converte automaticamente em requisito;
- baseline conceitual ou item do rascunho não autoriza código;
- implementação futura não poderá inventar silenciosamente domínio ou UX;
- AraLearn permanece principal fonte de evidência funcional e predecessor;
- contexto legível não concede permissão de escrita ao agente;
- output do GPT não equivale a aprovação, evidência conclusiva ou autoridade científica;
- observações participativas não são votação;
- analytics técnicos, educacionais e de pesquisa permanecem distinguíveis;
- nenhum prompt, knowledge, resource, perfil ou publicação é alterado automaticamente por analytics;
- nenhum fallback, compatibilidade ou bloqueio será criado sem decisão explícita;
- pesquisa, decisão, produto, arquitetura, UX e implementação permanecem distinguíveis;
- um item só será promovido depois de discussão, decisão registrada e definição de resultado observável.

## 8. Registros históricos

#36–#40 permanecem experimentos não normativos; #42 permanece adiado. #50 e #53 são placeholders acidentais `not_planned`.

As Issues #59–#74 foram criadas prematuramente durante uma interpretação incorreta da fase do projeto e permanecem encerradas como `not_planned`. Não constituem backlog atual nem autorização futura.

## 9. Próxima ação

Executar e revisar a pesquisa da Issue #77, começando pelo inventário do AraLearn e pelos evals de continuidade. Em paralelo, continuar a discussão das telas e do pré-backlog com o proprietário. Não iniciar desenvolvimento até nova decisão explícita.
