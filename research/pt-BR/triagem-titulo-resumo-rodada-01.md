# Triagem por título e resumo — rodada formal 01

**Data:** 2 de agosto de 2026  
**Issue:** #24 (`[25] Screen the first formal search corpus by title and abstract`)  
**Estado:** primeira triagem concluída; revisão de avaliador único assistida por regras, não dupla triagem independente

## 1. Corpus

A rodada formal reuniu **1.471 publicações únicas** após a deduplicação entre PubMed e ERIC. Todos os registros mantêm identificadores de origem e, quando existente, o identificador alternativo da outra base.

## 2. Pergunta operacional

Quais publicações são suficientemente relacionadas a flashcards, prática de recuperação, testagem, espaçamento, intercalação, feedback, formatos de resposta, quizzes, aprendizagem móvel, plataformas educacionais, autorregulação ou mecanismos adjacentes para justificar recuperação de texto integral ou análise posterior?

A decisão de triagem indica **relevância temática**, não qualidade metodológica nem eficácia.

## 3. Método

A triagem utilizou quatro camadas:

1. exclusões inequívocas, como recuperação de informação, uso não educacional de termos de memória, estudos não humanos, materiais sem evidência substantiva e avaliação não relacionada à aprendizagem;
2. identificação de mecanismos centrais em títulos;
3. avaliação da centralidade dos mecanismos em resumos e do contexto educacional ou experimental humano;
4. classificação conservadora como `maybe` quando o resumo era insuficiente, o contexto era adjacente ou a transferência para a ARA não era segura.

Foram preservadas distinções entre:

- pesquisa aplicada em educação;
- experimentos cognitivos humanos;
- literatura de reabilitação clínica;
- relatos, revisões e documentos de base;
- satisfação, uso e aprendizagem;
- publicações diferentes pertencentes à mesma família de estudo.

## 4. Resultados

| Decisão | Publicações |
|---|---:|
| `include` | 732 |
| `maybe` | 504 |
| `exclude` | 235 |
| **Total** | **1.471** |

Por base:

| Base | Include | Maybe | Exclude | Total |
|---|---:|---:|---:|---:|
| PubMed | 410 | 293 | 124 | 827 |
| ERIC | 322 | 211 | 111 | 644 |

## 5. Prioridade para a próxima fase

| Nível | Finalidade | Publicações |
|---|---|---:|
| `A-synthesis` | revisões sistemáticas, meta-análises e sínteses diretamente relacionadas | 26 |
| `B-direct-applied` | estudos diretamente aplicados aos mecanismos e sistemas prioritários | 425 |
| `C-direct-mechanism` | estudos humanos diretamente relacionados aos mecanismos, mas menos aplicados | 281 |
| `D-borderline` | registros mantidos para reavaliação, busca complementar ou texto integral | 504 |
| `none` | excluídos nesta etapa | 235 |

A prioridade não substitui avaliação de qualidade. Ela define apenas a ordem de trabalho.

## 6. Ausência de resumo

Foram encontrados **18 registros** com resumo ausente ou insuficiente. Dezessete foram preservados como `maybe`; um registro sem conteúdo substantivo foi excluído por tipo de publicação.

## 7. Auditoria

Foi selecionada uma amostra estratificada de **90 registros**:

- 15 por base e por decisão inicial;
- 30 `include`;
- 30 `maybe`;
- 30 `exclude`.

Após leitura de título e trecho do resumo:

- **80 decisões** foram mantidas;
- **10 decisões** foram alteradas;
- duas classificações adicionais tiveram o motivo refinado sem mudança de estado;
- **14 intervenções manuais** foram registradas no corpus completo.

As mudanças foram preservadas no arquivo de auditoria. O nível de desacordo confirma que esta triagem deve ser descrita como **primeira passagem assistida**, não como resultado equivalente a dupla triagem cega.

## 8. Frentes temáticas mais frequentes entre `include` e `maybe`

| Frente | Registros |
|---|---:|
| `retrieval-testing` | 681 |
| `basic-cognitive-mechanisms` | 520 |
| `flashcards-srs` | 486 |
| `spacing-repetition` | 256 |
| `language-vocabulary` | 234 |
| `feedback` | 204 |
| `school-literacy-mathematics` | 196 |
| `self-regulation-learner-control` | 130 |
| `quizzes-formative-assessment` | 123 |
| `response-formats` | 119 |
| `medical-health-education` | 102 |
| `mobile-microlearning` | 57 |
| `interleaving` | 48 |
| `lms-mooc-online` | 44 |
| `gamification-games` | 33 |

As frentes são multilabel; um registro pode aparecer em mais de uma categoria.

## 9. Regras de interpretação

- `include`: relevância suficiente para extração, revisão focada ou recuperação de texto integral;
- `maybe`: relevância possível, resumo insuficiente ou domínio adjacente;
- `exclude`: ausência clara de relação com a pergunta operacional desta rodada;
- nenhum estado representa avaliação de risco de viés;
- nenhum estado prova eficácia;
- uma publicação não corresponde necessariamente a um experimento ou a uma amostra independente.

## 10. Arquivos

- `formal-search-round-01-title-abstract-screening.csv`: todas as decisões;
- `formal-search-round-01-screening-audit.csv`: amostra auditada;
- `formal-search-round-01-priority-a-b.csv`: subconjunto inicial para obtenção de texto integral;
- `formal-search-round-01-screening-reason-counts.csv`: contagens por código;
- `formal-search-round-01-screening-summary.json`: resumo legível por máquina.

Os arquivos completos foram entregues ao proprietário do projeto em um pacote versionado. O manifesto registra nomes, tamanhos e hashes SHA-256; o conector disponível nesta execução não aceita o envio direto de arquivos montados ao repositório.

## 11. Próxima etapa recomendada

A recuperação de texto integral deve começar pelos **26 registros `A-synthesis`**, seguida por subgrupos temáticos de `B-direct-applied`. O conjunto `D-borderline` não deve ser descartado: deve ser reavaliado após novas revisões, rastreamento de citações ou obtenção de resumos completos.
