# Síntese P5 — autoria, revisão, auditoria, reparo, publicação e governança institucional

**Issue governante:** #4  
**Pacote:** P5  
**Data:** 3 de agosto de 2026  
**Estado:** pacote concluído; pendente da síntese final integrada da Issue #4.

## 1. Conclusão principal

O ARA deve tratar autoria como uma sequência governada de contribuições, estados e decisões, distribuída por dois canais complementares:

```text
chat + GPT/MCP
→ intenção semântica, contexto autorizado, planejamento, construção,
  auditoria, reparo e reauditoria

ARA
→ renderização em tempo real, seleção de alvo, comentários situados,
  versões, diffs, operações determinísticas, aprovação e publicação
```

Banco, Storage, persistência local e sincronização serão intermediários técnicos. O usuário administra artefatos e decisões pedagógicas; não tabelas, blobs ou filas.

A taxonomia P5 aceita **67 dimensões**. Aceitar significa tornar a distinção representável, versionada e rastreável; não implementar todos os valores na primeira release.

## 2. Fluxo de referência herdado do AraLearn

O AraLearn estabeleceu o fluxo:

```text
planejar
→ construir parte
→ auditar
→ reparar problemas aprovados
→ reauditar
→ marcar pronto
→ publicar explicitamente
```

A microssequência é a unidade técnica de gravação; a parte é a unidade conversacional. O alvo persistido é relido antes de mutações. `revision` controla concorrência, mas não aprovação. `generated`, `needs_review`, `ready` e estados de publicação permanecem distintos.

O ARA deve preservar esse perfil e formalizá-lo:

- etapas não dependem apenas de convenção de prompt;
- papéis não são apenas personalidades do GPT;
- estados pertencem aos artefatos;
- autoridade pertence a pessoas, protocolos, políticas e capacidades;
- cada ação aponta para versão persistida;
- comentários e findings possuem alvos recuperáveis;
- publicação nunca decorre implicitamente de outra etapa.

## 3. Papéis, identidade e contribuição

Papéis candidatos:

- planner;
- builder;
- auditor;
- repairer;
- reauditor;
- reviewer;
- approver;
- publisher;
- administrator;
- observer.

Uma pessoa ou agente pode exercer mais de um papel em momentos diferentes. Isso não transfere automaticamente autoridade. O mesmo GPT pode planejar, construir, auditar e reparar em rodadas separadas, mas não aprovar ou publicar implicitamente o próprio trabalho.

A taxonomia separa:

```text
agente/identidade
× papel
× atividade
× alvo e versão
× contexto
× autoridade
× estado produzido
```

O rótulo único “autor” é insuficiente. O produto deve registrar contribuições como conceptualização, planejamento instrucional, redação, curadoria de fontes, revisão de conteúdo, revisão pedagógica, acessibilidade, edição, reparo, aprovação e publicação. CRediT é referência para transparência de papéis, não regra automática de autoria jurídica.

## 4. Dois canais coerentes

### Chat e MCP

Adequados para:

- formular objetivos e público;
- definir parâmetros;
- planejar partes;
- consultar contexto autorizado;
- construir microssequências e cards;
- pedir auditoria e reparo;
- comparar alternativas e variantes.

O chat não é a fonte exclusiva do estado nem concede permissão por memória.

### ARA

Deve:

- mostrar o curso sendo construído;
- renderizar como o estudante verá;
- navegar por estrutura e dependências;
- comparar revisões e variantes;
- mostrar configuração efetiva, fontes e provenance;
- receber comentários e findings;
- oferecer ações determinísticas;
- exigir aprovação e publicação explícitas.

Cada operação registra canal, requester, alvo, versão esperada, papel, intenção, resultado, nova versão e status.

## 5. Contexto autorizado e snapshots

O agente pode receber:

- alvo;
- vizinhança local;
- dependências aprovadas;
- partes anteriores;
- unidades selecionadas de outros cursos;
- fontes e brief;
- configuração/condição;
- observações abertas.

Busca global silenciosa é rejeitada. A precedência é:

1. lei, direitos, acessibilidade e confidencialidade;
2. consentimento e protocolo;
3. política institucional;
4. permissões locais;
5. escolha do usuário;
6. disponibilidade técnica.

Para trabalho reproduzível ou consequencial, registrar IDs, revisões, hashes/manifests quando necessários, fontes, versão das instruções, agente/modelo, ferramentas e configuração efetiva. Isso não exige reter chats ou raciocínios integrais.

## 6. Grounding e ancoragem

Grounding pode ser:

- dispensado em notas pessoais;
- baseado em fontes do autor;
- oficial;
- acadêmico;
- misto validado;
- fixado por protocolo;
- marcado como indisponível.

Anchors podem existir no curso, parte, microssequência, card, claim, resource ou prática. Bibliografia geral sem relação recuperável é insuficiente para auditoria granular.

Uma citação não garante correção, atualidade, acesso integral ou interpretação adequada. Auditoria precisa avaliar correspondência entre claim e fonte.

## 7. Provenance

A provenance deve responder:

- o que foi criado;
- por qual atividade e agente;
- com quais fontes, versões e contexto;
- derivado, revisado, adaptado ou forked de quê;
- aprovado e publicado por quem;
- sob qual licença;
- qual versão está ativa.

W3C PROV oferece Entity, Activity, Agent e relações de geração/derivação/revisão. C2PA oferece precedentes para assertions verificáveis. São candidatos de mapeamento, não schema interno obrigatório.

Provenance não prova verdade, qualidade pedagógica, ausência de viés, acessibilidade, validade de licença ou eficácia.

## 8. Estados editoriais

Estados candidatos:

```text
planned
suggestion
draft
generated
validated-structure
needs_review
audited
ready
approved
rejected
superseded
```

Validação confirma contratos e invariantes; não qualidade pedagógica. Auditoria examina critérios sem modificar. Aprovação é decisão sobre versão. Publicação disponibiliza para audiência definida.

## 9. Revisão e quality assurance

Tipos:

- self-review;
- AI audit;
- peer review;
- SME review;
- instructional-design review;
- accessibility review;
- legal/licensing review;
- institutional QA;
- composite review.

Rubricas podem cobrir alinhamento, cobertura, precisão, pré-requisitos, sequência, teoria/prática, carga cognitiva, representações, feedback, acessibilidade, fontes, provenance, licença, privacidade, fidelidade experimental, offline e linguagem.

Quality Matters e OSCQR são referências de rubricas e ciclos de revisão, não rubrica universal.

Níveis de independência:

- self-review;
- mesmo GPT em rodada separada e snapshot congelado;
- outro agente/modelo;
- peer humano;
- SME;
- equipe multidisciplinar;
- revisor externo.

LLMs podem apoiar critérios, triagem e feedback, mas falham em factualidade, nuance, entradas longas e domínios críticos. Não substituem especialista quando a decisão exige competência específica.

Um finding registra localização, critério, gravidade, impacto, recomendação, escopo e estado. `no-blocker`, `findings`, `changes-requested`, `conditionally-acceptable`, `approved-for-next-gate`, `rejected` e `inconclusive` permanecem distintos.

## 10. Reparo e reauditoria

Reparo exige autoridade explícita e alvo persistido. Deve alterar apenas findings aprovados. Não pode:

- corrigir outros problemas silenciosamente;
- ampliar escopo;
- reestruturar sem autorização;
- trocar fontes ou parâmetros inadvertidamente;
- atualizar todos os consumidores.

Mudança semântica cria nova revisão. Publicações e condições experimentais não são alteradas in place.

Após reparo, verificar finding original, regressões, dependências, consistência, acessibilidade, licenciamento e condições afetadas. Reauditoria pode ser opcional no uso pessoal e obrigatória por gravidade, para `ready`, publicação ou protocolo.

## 11. Observações situadas

Alvos:

- curso, módulo, lição;
- microssequência ou ocorrência;
- card, resource ou prática;
- relação/dependência;
- parâmetro;
- trecho ou diff.

Motivações:

- pergunta;
- possível erro;
- confusão;
- sugestão;
- avaliação;
- classificação;
- pedido de reparo;
- nota de aprovação.

Lifecycle:

```text
open
→ triaged
→ accepted / rejected / needs-information
→ repair-planned
→ resolved / superseded / withdrawn
```

Responder não resolve automaticamente. Resolução deve apontar para decisão, alteração ou revisão. O Web Annotation Data Model oferece conceitos úteis de body, target, selector, motivation e provenance, sem obrigar JSON-LD interno.

## 12. Identidade, revisão e derivação

Distinções obrigatórias:

```text
linhagem
≠ revisão
≠ ocorrência no curso
≠ snapshot publicado
≠ cópia do estudante
```

Relações candidatas incluem `revision-of`, `derived-from`, `fork-of`, `adaptation-of`, `translation-of`, `variant-of`, `supersedes`, `reuses` e `imports`. O vocabulário normativo pertence a #6.

Diffs devem separar estrutura, conteúdo, configuração, composição, capabilities, instrumentos e resumo semântico. Diff textual isolado não representa toda mudança pedagógica.

Rollback deve repontar explicitamente, criar revisão de reversão ou retirar versão atual; nunca apagar a história.

## 13. Reutilização

Modos:

- referência;
- cópia;
- fork;
- adaptação;
- tradução;
- snapshot incorporado;
- link.

Escopos de busca incluem curso atual, biblioteca pessoal, workspace, cursos aprovados, biblioteca institucional, catálogo público e conjunto de fontes.

Context fit verifica pré-requisitos, terminologia, dificuldade, público, sequência, avaliação, licença, acessibilidade, confidencialidade e contexto cultural.

Atualização recomendada:

```text
origem atualizada
→ consumidor notificado
→ diff/impacto mostrado
→ autor aceita, adapta ou mantém snapshot
```

Propagação global silenciosa é rejeitada. Open edX Content Libraries e H5P demonstram reuse e versionamento, mas também riscos de cópia sem lineage e atualização sem ajuste contextual.

## 14. Publicação, retirada e exclusão

Estados:

- draft;
- private preview;
- private partial;
- ready;
- approved;
- published private/shared/institutional/public;
- withdrawn;
- superseded;
- archived.

`published` deve declarar audiência.

Gates possíveis:

- validação estrutural;
- targets prontos;
- auditoria;
- aprovação humana;
- licença;
- acessibilidade;
- confidencialidade;
- protocolo;
- aprovação institucional.

Prévia privada parcial pode usar gate menor. Autoridades incluem owner, publisher, institutional approver, catalogue editor e protocol owner. GPT não publica por conclusão implícita.

Distinguir remoção de composição, unlisting, revogação de novos acessos, withdrawal, supersession, archive, tombstone e hard delete permitido. Retirada de distribuição não revoga necessariamente licença aberta já concedida; obrigações acadêmicas, legais ou de pesquisa podem exigir retenção.

## 15. Licenciamento

Licenças podem existir em curso, microssequência, card, resource, asset ou source. Licença geral não deve ocultar materiais de terceiros.

Creative Commons distingue BY, SA, NC e ND. NoDerivatives pode impedir distribuição de adaptação; ShareAlike pode exigir licença compatível. Regras podem auxiliar, mas casos ambíguos exigem revisão humana/jurídica.

Atribuição pode registrar título, criador, fonte, licença, mudanças, papéis e cadeia de derivação.

Uso de IA não resolve titularidade, originalidade, direitos de terceiros, reprodução protegida ou responsabilidade. Decisões jurídicas finais dependem de #2 e #6.

## 16. Confidencialidade, workspaces e papéis

Classes:

- public;
- open-licensed;
- internal;
- private;
- confidential;
- restricted research;
- participant-sensitive;
- legal hold.

A classe limita contexto do GPT, provider, reuse, publicação, exportação, retenção e analytics. Conteúdo restrito não vai a provider externo não autorizado.

Tipos de workspace:

- personal;
- private team;
- course team;
- research;
- institutional;
- confidential;
- catalogue editorial;
- public community.

Papéis locais incluem owner, author, contributor, viewer, reviewer, auditor, repairer, approver, publisher, admin, participant e catalogue editor. Evita-se superadmin universal.

Separação de deveres pode ocorrer por rodada, agente, pessoa, two-person rule, SME + instructional designer ou board institucional. O rigor varia por risco.

Exceções registram autoridade, justificativa, prazo, escopo, risco e revisão posterior. Acomodação não é falha disciplinar.

## 17. Administração compreensível

O usuário deve ver:

- o que está sendo construído;
- quem contribuiu;
- o que mudou;
- pendências e observações;
- cursos afetados;
- audiência;
- fontes e licenças;
- consequência de cada ação.

Detalhes como foreign keys, blobs, hashes, object stores e event streams ficam em camada avançada.

Perfis iniciais podem ser: pessoal, equipe, pesquisa, instituição, OER e confidencial. Depois o ARA mostra overrides relevantes.

Filas respondem perguntas:

- O que precisa de revisão?
- O que mudou?
- O que aguarda aprovação?
- Quais comentários continuam abertos?
- O que será publicado?
- Quais cursos serão afetados?
- Há conflito de licença?
- Funciona offline?
- Há barreira de acessibilidade?

## 18. Perfis P5

1. `aralearn-reference`;
2. `personal-manual-author`;
3. `personal-ai-assisted-author`;
4. `collaborative-course-team`;
5. `research-locked-authoring`;
6. `institutional-controlled-publication`;
7. `open-oer-publication`;
8. `confidential-institutional`;
9. `external-expert-review-overlay`;
10. `accessibility-quality-overlay`;
11. `offline-authoring-overlay`.

## 19. Adiados e rejeitados

Adiados:

- schema de microssequência/manifesto;
- banco, Storage e content addressing;
- sincronização e merge;
- adoção interna de PROV-O/C2PA;
- verificação automática de fontes e licenças;
- repair/update automático entre cursos;
- marketplace, endpoints MCP e UI.

Rejeitados como padrão:

- GPT único como autor, auditor, aprovador e publisher;
- contexto concedido por memória do chat;
- audit que altera o alvo;
- promoção automática a `ready`/`published`;
- mutação silenciosa de publicado;
- propagação global automática;
- comentários sem alvo;
- tags textuais como única dependency/provenance;
- licença geral ocultando assets;
- retenção integral de chats;
- quality score universal;
- hard delete sem impacto;
- superadmin universal.

## 20. Handoffs

### Issue #5

Recebe provenance editorial, estados e review events autorizáveis, rubricas/findings, separação de logs editoriais e learning analytics, authoring bloqueado por protocolo e snapshots.

### Issue #6

Decidirá entidades de autoria, curso/microssequência/placement, identidade/revisão/derivação, annotation/finding/change set, workspace/role/capability, publicação/retirada/exclusão, licença/confidencialidade e reuse modes.

### Issue #7

Comparará storage, concorrência, sync/conflitos, manifests, hashes/content addressing, provenance mappings, providers, access control, offline authoring, backup, migração e rollback.

### Issue #8

Especificará dois canais, rendering em tempo real, comments/findings, versões/diffs, perfis/formulários, review queues, approval/publish, reuse/fork/update, licença/confidencialidade e administração acessível.

## 21. Decisão final do P5

A primeira taxonomia aceita 67 dimensões agrupadas em:

- authoring;
- review;
- repair;
- annotation;
- versioning;
- reuse;
- publication;
- licensing;
- governance.

O perfil AraLearn permanece referência funcional. O ARA deve tornar explícitos estados, autoridades, versões, provenance e políticas que antes dependiam de instruções ou implementação.

Nenhum schema, arquitetura, UI ou código foi autorizado.
