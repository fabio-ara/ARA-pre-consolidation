# Backlog e fluxo de trabalho do ARA

**Estado:** pré-desenvolvimento; brainstorming e revisão  
**Idioma:** `pt-BR`  
**Última revisão:** 3 de agosto de 2026

## 1. Estado das fases

```text
#3 evidência contínua
→ #4 taxonomia — concluída
→ #5 pesquisa/analytics — concluída
→ #6 produto/domínio — baseline conceitual
→ #7 arquitetura — baseline conceitual
→ #8 UX/UI — baseline conceitual e protótipo não produtivo
→ #9 planejamento de implementação — futuro, não iniciado
```

A conclusão de uma baseline significa que existe material suficiente para discussão e revisão. Não significa que o projeto entrou em desenvolvimento.

## 2. Trabalho atual

O trabalho atual permanece aberto a brainstorming, investigação bibliográfica, análise de repositórios, revisão de hipóteses e clarificações do proprietário.

Não existe bloqueio administrativo, branch protegida obrigatória, release ativa ou issue de código autorizada.

## 3. Rascunho amplo para discussão

O índice [`docs/ideation/README.md`](../ideation/README.md) reúne a primeira idealização integrada do produto depois da análise do AraLearn atual.

O conjunto contém:

- auditoria funcional e estrutural do predecessor;
- mapa preservar/reformular/separar/adiar;
- proposta de kernel estável e packages independentes de resource/practice;
- alternativas de BaaS, store local, sync, hosting, framework e app Android;
- backlog candidato com 169 itens em 16 áreas;
- catálogo de 37 telas e estados;
- 12 wireframes SVG simples;
- registries CSV para filtragem e discussão;
- manifesto e auditoria do próprio rascunho.

O arquivo `docs/ideation/draft-backlog-v1.pt-BR.md` e seu CSV não são backlog executável. Não possuem prioridade, release, sprint, bloqueio ou autorização para Codex. Sua função é permitir discussão item a item e futura seleção.

## 4. Baselines de consulta

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

Esses documentos são propostas consolidadas, sujeitas a revisão versionada antes da implementação.

## 5. Entrada futura em desenvolvimento

A Issue #9 somente deverá ser executada após decisão explícita do proprietário de iniciar a fase de desenvolvimento.

Nesse momento, e não antes, será necessário:

- revisar o rascunho amplo e registrar decisões;
- revisar novamente requisitos, domínio, arquitetura e UX;
- decidir o primeiro escopo implementável;
- criar releases e issues executáveis novas;
- escolher quality gates proporcionais ao estágio;
- decidir se qualquer proteção de branch realmente agrega valor;
- definir migração, rollback e evidência de release.

Nenhuma dessas escolhas é pré-condição para continuar pesquisando ou refinando o produto.

## 6. Regras permanentes

- possibilidade descoberta não se converte automaticamente em requisito;
- baseline conceitual ou item do rascunho não autoriza código;
- implementação futura não poderá inventar silenciosamente domínio ou UX;
- AraLearn permanece fonte de evidência e predecessor, não legado obrigatório;
- nenhum fallback, compatibilidade ou bloqueio será criado sem decisão explícita;
- pesquisa, decisão, produto, arquitetura, UX e implementação permanecem distinguíveis;
- um item só será promovido depois de discussão, decisão registrada e definição de resultado observável.

## 7. Registros históricos

#36–#40 permanecem experimentos não normativos; #42 permanece adiado. #50 e #53 são placeholders acidentais `not_planned`.

As Issues #59–#74 foram criadas prematuramente durante uma interpretação incorreta da fase do projeto e permanecem encerradas como `not_planned`. Não constituem backlog atual nem autorização futura.

## 8. Próxima ação

Discutir a auditoria, os wireframes e o backlog candidato com o proprietário, corrigindo, removendo, aprofundando e agrupando itens. Não iniciar desenvolvimento até nova decisão explícita.
