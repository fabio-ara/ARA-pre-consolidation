# Busca exploratória — ambientes estruturados e interativos de aprendizagem

**Data local:** 2 de agosto de 2026  
**Issues:** #33 e #34  
**Tipo:** busca exploratória de escopo; não é busca sistemática exaustiva nem execução formal em base bibliográfica

## 1. Finalidade

A primeira busca formal do programa foi deliberadamente centrada em flashcards, prática de recuperação, espaçamento, Anki e Quizlet. Esta rodada amplia o enquadramento para identificar:

- gêneros acadêmicos vizinhos da ARA;
- sínteses sobre ambientes tutoriais, representações externas, simulações, avaliação interativa e autoria;
- sistemas e repositórios que separam representação, resposta, validação, feedback e extensão;
- lacunas que exigirão buscas formais específicas por domínio.

Nenhuma contagem de resultados desta rodada deve ser usada como fluxo PRISMA. O mecanismo de busca web não fornece universo estável, exportação integral ou deduplicação reproduzível equivalente a ERIC, Scopus, Web of Science ou bases especializadas.

## 2. Consultas executadas

As consultas abaixo foram executadas em mecanismo de busca web, com prioridade posterior para páginas de editoras, ERIC, repositórios institucionais, artigos abertos e repositórios oficiais:

```text
systematic review intelligent tutoring systems learning outcomes meta-analysis educational technology primary source PDF
multiple external representations learning framework Ainsworth 2006 PDF
simulation-based learning meta-analysis education primary source 2020 PDF
Khan Academy interactive exercises research mastery learning official research
```

```text
site:eric.ed.gov Khan Academy mathematics study peer reviewed
site:pmc.ncbi.nlm.nih.gov Khan Academy education study
open educational platforms interactive exercises multiple representations systematic review learning environments
authoring tools intelligent tutoring systems review open educational technology primary source
```

```text
systematic review computer based assessment constructed response mathematics programming education
review virtual laboratories science education de Jong 2013 PDF
systematic review interactive learning environments multiple representations assessment authoring tools
Khan Academy Perseus exercise system widgets official
```

Consultas técnicas complementares foram executadas diretamente no GitHub para localizar repositórios oficiais, schemas, registries, modelos de pontuação, manifests, documentação de acessibilidade e licenças.

## 3. Critérios de seleção exploratória

Foram priorizados:

1. revisões sistemáticas, meta-análises e frameworks centrais;
2. fontes que distinguem representação, tarefa, resposta, avaliação ou autoria;
3. fontes com domínio ou constructo explicitamente delimitado;
4. repositórios oficiais com schema, contrato de extensão, runtime ou modelo de scoring inspecionável;
5. exemplos capazes de revelar limitações do enquadramento por flashcards.

Foram evitados como base de conclusão:

- rankings comerciais de plataformas;
- descrições promocionais sem método;
- inferência de eficácia a partir de recursos de software;
- uso de popularidade do repositório como proxy de qualidade pedagógica;
- transposição automática de achados de matemática ou programação para todos os domínios.

## 4. Corpus selecionado nesta rodada

A tabela estruturada está em `research/data/structured-learning-literature-01.csv`. Ela inclui, entre outros:

- DeFT e revisões recentes de múltiplas representações;
- meta-análises de sistemas tutoriais inteligentes;
- revisão de ferramentas de autoria para ITS;
- meta-análise de aprendizagem baseada em simulação;
- revisão de laboratórios físicos e virtuais;
- revisão de princípios de aprendizagem multimídia;
- síntese de componentes interativos em avaliação matemática;
- revisões de avaliação de pensamento computacional e feedback automático em programação;
- revisões de avaliação automática de respostas textuais;
- revisões de representações digitais em química e ambientes educacionais.

Khan Academy não foi incluída como categoria de evidência por possuir muitos usuários ou por publicar estudos próprios. Seu sistema Perseus foi auditado como precedente técnico oficial: recebe um problema em formato Perseus, renderiza widgets, recolhe interação e encaminha a pontuação por registries específicos. A presença de vídeo no ecossistema Khan Academy não implica vídeo no contrato-base da ARA.

## 5. Limites e próximos passos formais

Esta rodada é suficiente para rejeitar `flashcard platform` como gênero abrangente da ARA e para propor um benchmark transdomínio. Ela não é suficiente para afirmar completude bibliográfica.

Buscas formais posteriores deverão ser divididas por frente, com protocolo, bases, exportação e triagem próprios:

1. múltiplas representações e coordenação representacional;
2. avaliação digital por resposta construída;
3. ferramentas de autoria e ambientes tutoriais;
4. programação executável, avaliação automática e feedback;
5. matemática simbólica, geometria dinâmica e demonstração;
6. simulações e laboratórios virtuais;
7. química e física multirrepresentacionais;
8. argumentação, análise de fontes e respostas abertas;
9. linguística, aprendizagem de línguas e eventual TTS derivado;
10. acessibilidade de interações de construção e manipulação.

Cada frente deverá preservar diferença entre eficácia, affordance, requisito disciplinar, precedente técnico e hipótese de projeto.
