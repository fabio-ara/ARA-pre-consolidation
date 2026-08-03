# Visão canônica atual do produto ARA

**Estado:** canônico para pesquisa e definição do produto  
**Idioma de trabalho:** `pt-BR`  
**Última consolidação:** 3 de agosto de 2026  
**Autoridade:** consolida a visão inicial, a memória do sucessor do AraLearn, as clarificações estratégicas do proprietário, a síntese da Issue #30 e a taxonomia `ara.configuration-taxonomy.v1` concluída pela Issue #4. Fontes históricas permanecem preservadas, mas esta visão governa sua interpretação atual.

## 1. Definição

ARA — Ambiente de Recursos de Aprendizagem / Learning Resources Environment — é o sucessor direto do AraLearn.

O produto preservará a experiência funcional que demonstrou valor no AraLearn e a reconstruirá para oferecer:

- autoria, revisão, auditoria e reparo de cursos assistidos por GPT com MCP;
- visualização e intervenção direta do usuário durante a construção;
- parametrização pedagógica, operacional, autoral e experimental;
- pesquisa acadêmica reproduzível;
- estudo mobile-first e offline;
- resources estruturados e validação determinística onde adequada;
- versionamento, provenance e publicação explícita;
- extensibilidade governada;
- infraestrutura portável;
- adoção pessoal, acadêmica e institucional.

ARA não é apenas o AraLearn com mais opções e não é uma plataforma universal que implementa antecipadamente toda possibilidade educacional.

```text
experiência funcional do AraLearn
+ pesquisa ampla, representativa e finita
+ taxonomia explícita e versionada
+ autoria GPT+MCP com controle humano visível no ARA
+ pesquisa e analytics governados
+ requisitos → arquitetura → UX → implementação
```

## 2. Continuidade com o AraLearn

O primeiro perfil de referência preserva:

- estrutura inicial `curso → módulo → lição → microssequência → card`;
- separação entre teoria e prática;
- progressão estrutural não punitiva;
- ritmo controlado pelo estudante;
- reveal solicitado e feedback acionável;
- ausência de ranking, nota e card timer por padrão;
- estado funcional mínimo;
- estudo mobile-first e offline;
- resources estruturados;
- comentários situados;
- autoria em partes;
- fluxo `plan → build → audit → repair → re-audit`;
- revisões e publicação explícitas;
- GPT+MCP subordinado à autoridade humana;
- ARA como superfície de inspeção e intervenção.

Não são herdados automaticamente:

- stack, frontend ou organização interna atuais;
- JavaScript puro;
- contrato monolítico `aralearn.resources.v4`;
- acoplamento com Supabase;
- limitações históricas de resposta e prática;
- preferências pessoais convertidas em regras universais;
- contratos experimentais das Issues #36–#40.

AraLearn é referência funcional e evidência, não arquitetura obrigatória nem limite do espaço de possibilidades.

## 3. Primeira taxonomia de configuração

A Issue #4 concluiu a primeira taxonomia versionada: `ara.configuration-taxonomy.v1`.

Ela preserva **205 parâmetros canônicos**, **38 perfis**, autoridade e precedência, candidatos adiados, princípios rejeitados e validação por cenários. Os artefatos canônicos estão em:

- `research/data/issue4-final-parameter-registry-v1.json`;
- `research/data/issue4-final-profile-registry-v1.json`;
- `research/data/issue4-final-decision-synthesis-v1.json`;
- `research/pt-BR/issue4-sintese-final-taxonomia-configuracao-v1.md`.

A aceitação de uma dimensão significa que ela deve poder ser representada, explicada, versionada e reproduzida. Não exige que todos os valores sejam implementados ou expostos no primeiro release.

### 3.1 Camadas de incidência

A parametrização é organizada em:

1. **runtime e configuração efetiva** — comportamento de estudo, avaliação, feedback, progressão, autonomia, acessibilidade e assistência;
2. **conteúdo e materialização** — distribuição, concentração, granularidade, exemplos, scaffolds, geração, adaptação, tradução e reparo;
3. **composição e dependências** — ordem, pré-requisitos, ocorrências, reuse, reference, copy, fork e variantes;
4. **lifecycle e governança** — autoria, revisão, versão, publicação, licença, acesso, retenção, retirada e exclusão;
5. **condição de pesquisa** — protocolo, condição, assignment, eventos, instrumentos, medidas, constructos e interpretações;
6. **direitos e acessibilidade**, transversal.

Parâmetros que transformam conteúdo ou composição não são switches de renderer. Produzem novas revisões, derivações, variantes ou snapshots.

### 3.2 Perfis e overrides

A direção aceita é:

```text
catálogo versionado
+ perfil-base nomeado
+ overlays compatíveis
+ políticas e locks
+ overrides esparsos por escopo
+ capacidades disponíveis
→ resolução determinística
→ configuração efetiva e snapshot reproduzível
```

O catálogo completo não será repetido em cada JSON nem enviado integralmente ao GPT. O modelo e o usuário trabalham com perfis, diferenças e consequências relevantes; a plataforma resolve e torna inspecionável a configuração efetiva.

## 4. Dois canais complementares

### 4.1 Chat com GPT e MCP

O chat serve a operações semânticas:

- definir objetivo, público e escopo;
- escolher ou discutir parâmetros;
- planejar partes;
- construir microssequências e cards;
- consultar contexto autorizado;
- comparar versões e variantes;
- auditar, reparar e reauditar;
- discutir decisões e trade-offs.

O GPT consulta somente metadados, contratos, unidades, dependências, fontes, comentários e diffs necessários à operação corrente.

### 4.2 ARA como superfície operacional

ARA não será apenas o player final. Ele deverá permitir ao usuário:

- acompanhar artefatos em evolução;
- navegar por curso, parte, microssequência, card e resource;
- inspecionar versões, diffs, dependências, configuração e provenance;
- comentar alvos situados;
- selecionar, mover ou reorganizar unidades quando autorizado;
- aceitar, rejeitar ou aplicar parcialmente mudanças;
- solicitar reparos;
- acompanhar auditoria e reauditoria;
- aprovar e publicar explicitamente.

Professores, tutores, pesquisadores e autodidatas administrarão conceitos pedagógicos e operacionais, não tabelas, blobs, chaves, stores locais ou protocolos de sincronização.

```text
GPT/MCP planeja, cria ou propõe
↔ ARA renderiza e oferece operações determinísticas
↔ usuário observa, comenta e decide
↔ GPT/MCP lê o estado autorizado e repara
```

## 5. Autoria, revisão e autoridade

Planejamento, construção, validação, auditoria, reparo, reauditoria, aprovação e publicação são operações distintas.

O mesmo GPT poderá exercer papéis diferentes em rodadas separadas, contra versões persistidas, mas não herdará autoridade para aprovar ou publicar o próprio trabalho.

```text
suggestion → draft → validated-structure → audited
→ human-approved → published
```

Uma saída também pode ser `rejected` ou `superseded`.

Published não significa público. Responder a comentário não significa resolvê-lo. Validação estrutural não significa qualidade pedagógica nem efetividade educacional.

## 6. Hipótese de composição por microssequências

Permanece como hipótese obrigatória para decisão nas Issues #6 e #7:

```text
microssequência versionada
→ ocorrência/posição em composição de curso
→ composição versionada
→ snapshot local autossuficiente
→ estado contextual por curso/versão/posição/card
```

A hipótese favorece autoria e reparo granulares, contexto seletivo para GPT, reutilização com provenance, dependências explícitas, variantes de pesquisa e estudo offline.

Ainda precisam ser decididos:

- se microssequência é a unidade reutilizável adequada;
- identidade de ocorrência/placement;
- relação entre curso completo e unidades independentes;
- reference, copy, fork e snapshot;
- transferência de estado entre cursos;
- persistência, materialização, sincronização, deduplicação e revogação.

Reutilização de conteúdo não transfere automaticamente conclusão, mastery ou estado de revisão.

## 7. Pesquisa e analytics

ARA separará obrigatoriamente:

```text
finalidade → protocolo → condição → evento/instrumento
→ medida → constructo → interpretação → decisão/intervenção
```

Eventos não autorizam coleta; medidas não são constructos; constructos não autorizam automaticamente decisões.

O perfil pessoal permanece data-minimal. Analytics pessoais, pedagógicos, de pesquisa e operacionais terão autoridade, visibilidade, retenção e uso distintos.

A Issue #5 consolidará normativamente protocolos, participantes, instrumentos, medidas, governança, exportação e equivalência entre implantações sem reabrir os parâmetros pedagógicos e autorais já aceitos.

## 8. Kernel, resources e capacidades

ARA deverá possuir kernel pequeno, versionado e de evolução controlada, responsável apenas por funções transversais como:

- carregar e validar artefatos;
- resolver versões, perfis, políticas e capacidades;
- executar o ciclo de cards;
- despachar resources, práticas e outras capacidades;
- controlar estado, progressão, feedback e retomada;
- operar offline;
- registrar somente eventos autorizados;
- tratar capacidades ausentes explicitamente.

Um `resource` representa conteúdo declarativo. Não absorve silenciosamente prática, resposta, validator, runtime, instrumento de pesquisa, integração com IA ou serviço externo.

As entidades e fronteiras normativas serão decididas na Issue #6; a arquitetura e os adapters, na Issue #7.

## 9. Gate para engenharia

Sequência obrigatória:

```text
pesquisa
→ síntese crítica
→ recomendação e decisão
→ protocolos e analytics
→ requisitos e domínio
→ arquitetura e ADRs
→ UX/UI
→ releases
→ implementação
```

A taxonomia não autoriza:

- schema de produção;
- banco, Storage ou IndexedDB;
- MCP endpoints;
- arquitetura ou stack;
- UI;
- event store ou dashboard;
- coleta de participantes;
- scheduler, learner model ou adaptação automática;
- atualização ou reparo automático entre cursos;
- código ou migração.

## 10. Próxima etapa

A Issue #4 está concluída pela taxonomia `ara.configuration-taxonomy.v1`.

A próxima fase é a **Issue #5 — protocolos de pesquisa, instrumentação e learning analytics**. Ela deverá importar o handoff normativo da taxonomia, preservar o perfil pessoal data-minimal e produzir especificações de pesquisa e analytics antes de a Issue #6 consolidar produto e domínio.
