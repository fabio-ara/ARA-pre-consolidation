# Backlog e fluxo de trabalho do ARA

**Estado:** pré-desenvolvimento; brainstorming, pesquisa e revisão  
**Idioma:** `pt-BR`  
**Última revisão:** 4 de agosto de 2026

## 1. Estado das fases

```text
#3 evidência contínua
→ #4 taxonomia — concluída
→ #5 pesquisa/analytics — baseline v1
→ #6 produto/domínio — baseline conceitual
→ #7 arquitetura — baseline conceitual
→ #8 UX/UI — baseline conceitual e protótipo não produtivo
→ #77 agentes, participação e analytics — pesquisa focal
→ #79 versionamento, storage e economia — pesquisa focal
→ #9 planejamento de implementação — futuro, não iniciado
```

A conclusão de uma baseline significa que existe material suficiente para discussão e revisão. Não significa desenvolvimento. As Issues #77 e #79 investigam extensões e possíveis revisões versionadas; não são issues de código.

## 2. Trabalho atual

### Issue #77

Investiga:

- configuração modular e versionada do agente;
- perfis de domínio e knowledge collections;
- prompts/templates, MCP resources/tools e contratos;
- contexto de leitura e escopo de escrita;
- observações participativas, diffs e reparos;
- analytics de autoria/sistema e pesquisa educacional;
- análise quantitativa, qualitativa e mista assistida por GPT;
- papéis, autoridade, reprodutibilidade, privacidade e UX administrativa.

O AraLearn é referência funcional e caso de contraste. Não possui uma arquitetura modular equivalente a ser reproduzida. Evals devem partir de tarefas-alvo do ARA, casos controlados, invariantes e exemplos sintéticos, podendo usar jornadas ou falhas do predecessor como contraste.

### Issue #79

Investiga:

- objetos versionados e retenção;
- metadata relacional versus artifact repository e local store;
- content addressing e deduplicação;
- manifests, materialização e cache;
- garbage collection por referências e políticas;
- workloads e custo para grandes quantidades de revisões;
- Supabase Free/Pro, Supabase + object storage, stack portátil, BaaS alternativo e local-only;
- disponibilidade, pausa, backup, exportação e restauração;
- budgets compreensíveis ao proprietário.

Não existe bloqueio administrativo, branch protegida obrigatória, release ativa ou issue de implementação autorizada.

## 3. Pré-backlog v3 para discussão

O índice [`docs/ideation/README.md`](../ideation/README.md) reúne a idealização integrada.

O pré-backlog v3 é composto por:

- áreas A–P: 171 itens;
- área Q: 26 itens, com correção versionada v2;
- área R: 10 itens de versionamento, retenção, storage e economia operacional.

Total: **207 itens candidatos em 18 áreas**.

Manifesto: `research/data/ara-draft-backlog-v3-manifest.json`.

Documentos:

- `docs/ideation/draft-backlog-v1.pt-BR.md`;
- `docs/ideation/draft-backlog-agent-profiles-analytics-v2.pt-BR.md`;
- `docs/ideation/draft-backlog-versioning-storage-v1.pt-BR.md`.

Registries:

- `research/data/ara-draft-backlog-v1.csv`;
- `research/data/ara-draft-backlog-agent-profiles-analytics-v2.csv`;
- `research/data/ara-draft-backlog-versioning-storage-v1.csv`.

Esses arquivos não possuem prioridade, release, sprint, bloqueio ou autorização para Codex.

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

Extensões em pesquisa:

- `docs/ideation/agent-profiles-participatory-analytics-v1.pt-BR.md`;
- `docs/ideation/draft-backlog-agent-profiles-analytics-v2.pt-BR.md`;
- `docs/ideation/versioning-storage-economics-v1.pt-BR.md`;
- `research/searches/2026-08-04-agent-profiles-participatory-analytics-protocol.md`;
- `research/searches/2026-08-04-versioning-storage-economics-protocol.md`;
- `research/data/versioning-storage-provider-evidence-v1.csv`;
- `research/data/ara-draft-backlog-v3-manifest.json`.

Esses documentos são propostas e evidências, sujeitas a revisão versionada antes da implementação.

## 5. Dependências conceituais

### Área Q

1. inventário contrastivo do AraLearn;
2. objetos e resolução de configuração;
3. tarefas-alvo e casos controlados de evals;
4. primeiro perfil de domínio;
5. contexto de leitura e escopo de escrita;
6. observações, síntese, diffs e reparos;
7. analytics operacionais, educacionais e de pesquisa;
8. workbenches quantitativo, qualitativo e misto.

### Área R

1. inventário de objetos versionados;
2. fronteiras metadata/artifact/local;
3. deduplicação, manifests e retenção;
4. workload sintético e amostras do AraLearn;
5. comparação de deployments e custos;
6. backup, exportação e restore;
7. budgets e UX administrativa;
8. decisão por ADR somente após medições.

Nenhuma dependência conceitual é bloqueio administrativo de GitHub.

## 6. Entrada futura em desenvolvimento

A Issue #9 somente deverá ser executada após decisão explícita do proprietário.

Nesse momento será necessário:

- revisar o pré-backlog v3 e registrar decisões;
- revisar requisitos, domínio, arquitetura e UX;
- escolher o primeiro escopo implementável;
- selecionar infraestrutura por ADR com workload medido;
- criar releases e issues executáveis novas;
- definir qualidade, migração, rollback e evidência de release.

Nenhuma dessas escolhas é pré-condição para continuar a pesquisa.

## 7. Regras permanentes

- possibilidade descoberta não se converte automaticamente em requisito;
- baseline ou item do pré-backlog não autoriza código;
- implementação futura não poderá inventar silenciosamente domínio ou UX;
- AraLearn permanece principal referência funcional e fonte de contraste, não arquitetura equivalente nem limite de escala;
- contexto legível não concede permissão de escrita ao agente;
- output do GPT não equivale a aprovação ou autoridade científica;
- observações participativas não são votação;
- analytics técnicos, educacionais e de pesquisa permanecem distinguíveis;
- nenhum prompt, knowledge, resource, perfil ou publicação é alterado automaticamente;
- free tier não define durabilidade, retenção ou arquitetura;
- provider, plano, banco e object storage exigem decisão medida e plano de saída;
- nenhum fallback, compatibilidade ou bloqueio será criado sem decisão explícita;
- pesquisa, decisão, produto, arquitetura, UX e implementação permanecem distinguíveis.

## 8. Registros históricos

#36–#40 permanecem experimentos não normativos; #42 permanece adiado. #50 e #53 são placeholders acidentais `not_planned`.

As Issues #59–#74 foram criadas prematuramente e permanecem encerradas como `not_planned`. Não constituem backlog atual nem autorização futura.

## 9. Próxima ação

Executar em paralelo:

1. inventário contrastivo e tarefas-alvo da Issue #77;
2. inventário de objetos versionados e workloads da Issue #79;
3. simulação de storage/custo e requisitos de retenção;
4. discussão do pré-backlog v3 com o proprietário.

Não iniciar desenvolvimento nem contratar infraestrutura até nova decisão explícita.
