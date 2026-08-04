# Idealização do ARA — índice do rascunho para discussão

**Estado:** rascunho não normativo, pré-desenvolvimento  
**Data de corte:** 3 de agosto de 2026  
**Finalidade:** materializar uma proposta ampla para leitura, crítica e discussão com o proprietário antes de qualquer backlog definitivo.

## O que este conjunto representa

Este diretório descreve uma possível evolução do AraLearn para o ARA. Ele reúne:

- auditoria do produto e do código atual do AraLearn;
- funções a preservar, reformular, separar ou reconsiderar;
- idealização do funcionamento do ARA;
- alternativas de kernel, packages de resource, persistência, sincronização, BaaS e empacotamento móvel;
- rascunho amplo de backlog, ainda sem autoridade de execução;
- catálogo de telas, controles, estados e wireframes SVG deliberadamente simples.

## O que este conjunto não representa

Não é:

- backlog definitivo;
- issue executável para Codex;
- arquitetura selecionada;
- autorização para desenvolvimento;
- promessa de cronograma;
- alegação de efetividade educacional;
- obrigação de reproduzir toda a complexidade atual do AraLearn.

## Artefatos

1. [`aralearn-integral-audit-v1.pt-BR.md`](aralearn-integral-audit-v1.pt-BR.md) — leitura funcional e estrutural do predecessor.
2. [`ara-product-idealization-v1.pt-BR.md`](ara-product-idealization-v1.pt-BR.md) — experiência pretendida e ciclos do produto.
3. [`kernel-resource-modularity-v1.pt-BR.md`](kernel-resource-modularity-v1.pt-BR.md) — opções para kernel estável e resources independentes.
4. [`technology-and-baas-options-v1.pt-BR.md`](technology-and-baas-options-v1.pt-BR.md) — alternativas técnicas e trade-offs.
5. [`draft-backlog-v1.pt-BR.md`](draft-backlog-v1.pt-BR.md) — backlog candidato amplo para discussão.
6. [`screens-and-states-v1.pt-BR.md`](screens-and-states-v1.pt-BR.md) — telas, controles, estados e ligações para wireframes.
7. [`wireframes/`](wireframes/) — esquemas SVG minimalistas, não protótipos aprovados.

Registros estruturados:

- `research/data/aralearn-capability-preservation-matrix-v1.csv`;
- `research/data/ara-draft-backlog-v1.csv`;
- `research/data/ara-screen-catalog-v1.csv`;
- `research/data/ara-technology-options-v1.csv`.

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

A auditoria usa como fontes primárias o código e a documentação atuais de `fabio-ara/AraLearn`, especialmente contrato v4, arquitetura, persistência, MCP, resources, UI e testes. Comparações externas usam documentação oficial de H5P, Open edX/XBlock, Moodle, Supabase, Firebase, Appwrite, Nhost, PocketBase, PowerSync, RxDB, PWA/Android e Capacitor.

As baselines das Issues #4–#8 do ARA continuam separadas. Este rascunho as interpreta à luz do produto predecessor; não as substitui silenciosamente.

## Perguntas para a revisão com o proprietário

1. Qual é o menor kernel que ainda preserva a identidade do AraLearn?
2. A microssequência deve ser o primeiro objeto reutilizável ou apenas a unidade inicial de composição?
3. Quais resources entram no pacote-base e quais podem ser instalados depois?
4. Quanto do painel administrativo deve existir no primeiro produto utilizável?
5. O usuário sem conta deve poder estudar e criar localmente?
6. O Supabase continua como primeira implantação ou apenas como um adapter de referência?
7. O ARA precisa de sincronização genérica desde o primeiro corte ou pode preservar temporariamente o protocolo específico do AraLearn?
8. Quais telas e parâmetros realmente precisam ser visíveis para cada perfil?
9. Como comparar variantes de curso sem introduzir diferenças acidentais de conteúdo?
10. Quais capacidades devem ser descartadas, simplificadas ou adiadas para evitar reconstruir um LMS genérico?
