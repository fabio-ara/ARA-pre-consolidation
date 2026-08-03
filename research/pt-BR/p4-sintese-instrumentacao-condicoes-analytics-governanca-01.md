# Síntese P4 — instrumentação, condições experimentais, analytics e governança

## Conclusão principal

O ARA deve impedir a passagem silenciosa de rastros técnicos para afirmações educacionais. A cadeia normativa é:

```text
pergunta/finalidade
→ protocolo
→ condição
→ evento autorizado ou instrumento
→ medida
→ constructo
→ interpretação
→ decisão ou intervenção
```

Cada elo possui definição, versão, autoridade, limitações e rastreabilidade próprias.

## 1. Perfil AraLearn preservado

O perfil pessoal de referência mantém apenas estado funcional:

- cursor;
- conclusão estrutural;
- marca pessoal de revisão;
- observação situada;
- versão ou snapshot necessário para retomada.

Não coleta por padrão tempo, abertura, tentativas, acertos, erros, navegação detalhada ou histórico comportamental. Esses sinais não medem atenção, esforço, domínio ou qualidade.

## 2. Protocolos e condições

Um protocolo explicita pergunta, finalidade, população, direitos, designs, outcomes, instrumentos, eventos autorizados, análise, retenção e acesso.

Uma condição é um snapshot versionado de:

- conteúdo e composição;
- perfil e overrides;
- instrumentos;
- capacidades;
- assignment;
- materialização;
- regras de coleta;
- provenance.

Para cursos pareados, o ARA precisa distinguir diferenças intencionais de diferenças acidentais em conteúdo, configuração, composição, capacidades e instrumentos.

## 3. Eventos

Eventos devem ser seletivos e vinculados à finalidade. O núcleo deve ser pequeno, versionado e extensível. Caliper e xAPI são candidatos de mapeamento e intercâmbio, não ontologias de aprendizagem nem autorização para coleta.

Telemetria operacional deve permanecer separada de analytics educacionais. Erro, latência ou sincronização podem diagnosticar sistema; não caracterizam automaticamente o estudante.

## 4. Medidas, constructos e interpretações

Toda medida registra:

- fórmula;
- unidade;
- janela;
- entradas;
- denominador;
- missingness;
- versão;
- limitações;
- uso permitido.

Constructos exigem teoria e evidência de validade. Uma medida de cliques ou tempo não é “engajamento”; conclusão não é mastery; demora não é dificuldade.

A interpretação explicita se é descritiva, comparativa, preditiva candidata ou causal somente quando o desenho sustenta.

## 5. Instrumentos e métodos

O ARA deve representar testes, delayed tests, escalas, questionários, rubricas, entrevistas, diários, observações e análise de artefatos. Administração, idioma, acessibilidade, timing e versão são parte da condição.

O protocolo diferencia:

- outcomes primários, secundários, exploratórios, de processo e harms;
- análise exploratória e confirmatória;
- randomização, contrabalanceamento e quase-experimento;
- pesquisa quantitativa, qualitativa e mista;
- fidelidade técnica, pedagógica e de participação.

## 6. Direitos e governança

Finalidade, base legal, consentimento quando aplicável, retirada, minimização, retenção, acesso e exportação são parâmetros.

Consentimento não deve ser agrupado, coercivo ou irrevogável. Pseudonimização não equivale a anonimização. Retirada não pode ser punitiva.

Dados de acessibilidade e acomodação exigem escopo e acesso mais restritos.

## 7. Analytics por papel

O ARA não deve ter um dashboard universal.

### Estudante

- onde retomar;
- carga de revisão escolhida;
- metas e reflexões opt-in;
- explicação do que cada indicador significa.

### Professor ou tutor

- cobertura e dependências;
- observações e auditorias;
- agregados autorizados;
- fidelidade do curso;
- nunca ranking individual por padrão.

### Pesquisador

- diferenças entre condições;
- assignment;
- snapshots;
- qualidade e missingness;
- instrumentos e outcomes;
- exports autorizados.

### Administrador

- consentimento e retenção;
- integridade e provenance;
- conformance entre implantações;
- operação separada de aprendizagem.

## 8. Perfis

Foram registrados nove perfis:

- `aralearn-reference`;
- `personal-reflective`;
- `formal-formative-course`;
- `research-between-participant`;
- `research-within-participant`;
- `qualitative-development`;
- `institutional-quality-assurance`;
- `participant-rights-overlay`;
- `offline-research-overlay`.

## 9. Parâmetros aceitos

A primeira taxonomia aceita 31 dimensões organizadas em:

- protocolo e condição;
- participante, consentimento e retirada;
- eventos;
- medidas, constructos, interpretação e análise;
- instrumentos;
- provenance e variantes;
- governança de dados;
- analytics por papel;
- interoperabilidade e separação operacional.

Aceitar a dimensão não autoriza todos os valores nem implementação na primeira release.

## 10. Adiados

- event schema de produção;
- catálogo de métricas;
- early warning;
- predição individual;
- dashboard;
- event store;
- causal inference automatizada;
- coleta com participantes;
- transferência automática de mastery entre cursos.

## 11. Handoff

### P5

Autoria, revisão, reparo e publicação devem preservar provenance, audit trail, direitos, estados de aprovação e diferenças entre versões.

### Issue #5

Transformará a taxonomia em especificação metodológica e analítica, com fórmulas, instrumentos, governança e exportação.

### Issue #6

Definirá entidades normativas: protocolo, condição, participante, assignment, instrumento, dataset, snapshot e evidence.

### Issue #7

Comparará event transport, storage, offline buffering, pseudonymisation, conformance e adapters.

### Issue #8

Projetará painéis orientados por perguntas, consentimento, explicações, diffs e administração simples.

## 12. Decisão

O P4 recomenda incorporar as 31 dimensões à primeira taxonomia e preservar o perfil AraLearn data-minimal como padrão pessoal. A Issue #4 permanece aberta para P5 e síntese final.
