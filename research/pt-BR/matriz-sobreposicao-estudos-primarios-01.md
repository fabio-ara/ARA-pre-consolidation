# Matriz de sobreposição de estudos primários — prioridade A, rodada 01

**Data:** 3 de agosto de 2026  
**Issue:** #28 (`[27] Map primary-study overlap across the priority A syntheses`)  
**Estado:** matriz bibliográfica inicial concluída; completude documentada por revisão

## 1. Finalidade e limite

Esta rodada constrói uma concordância entre as publicações primárias incluídas nas 12 sínteses formais do corpus de prioridade A. O resultado é uma **matriz de sobreposição bibliográfica**. Ele não é uma nova meta-análise, não estima eficácia e não converte publicações em experimentos independentes.

A fonte de verdade foi, em ordem:

1. tabelas de estudos incluídos;
2. apêndices e listas marcadas pelos próprios autores;
3. listas de referências vinculadas explicitamente ao corpus incluído;
4. metadados bibliográficos exatos para normalização.

Listas ausentes não foram reconstruídas a partir de revisões posteriores.

## 2. Completude das 12 sínteses

| Revisão | Escopo declarado | Registros recuperados | Estado da lista |
|---|---:|---:|---|
| Xu et al. 2024 | systematic review; number of included studies not available in accessible abstract | 0 | `unavailable-full-text` |
| Özdemir & Seçkin 2024 | 23.0 | 22 | `partial-internally-inconsistent` |
| Trumble et al. 2024 | 56.0 | 56 | `complete-author-year-list` |
| Van Hoof et al. 2023 | 25.0 | 0 | `unavailable-full-text` |
| Frappa et al. 2026 | 11.0 | 11 | `complete-exact-list` |
| Thompson & Hughes 2023 | 8.0 | 8 | `complete-table-list` |
| Maye & Hurley 2026 | 14.0 | 13 | `complete-meta-analysis-list-partial-review-list` |
| Pan & Rickard 2018 | 67.0 | 0 | `list-not-retrieved-current-execution` |
| Öcel & Su-Bergil 2025 | 25.0 | 25 | `complete-table-list` |
| Agarwal et al. 2021 | 37.0 | 0 | `list-not-retrieved-current-execution` |
| Murray et al. 2025 | 27 spacing studies and 7 retrieval studies | 0 | `supplement-not-retrieved-current-execution` |
| Cadavid et al. 2025 | 75.0 | 38 | `partial-complete-testing-and-spacing-subsets` |

Cinco revisões não puderam receber métrica definitiva porque a lista primária não foi recuperada: Xu et al., Van Hoof et al., Pan e Rickard, Agarwal et al. e Murray et al. A ausência permanece explícita.

A revisão de Özdemir e Seçkin declara 23 estudos, mas a convenção de asteriscos do próprio artigo permite identificar somente **22 referências**. A matriz conserva a discrepância em vez de criar um vigésimo terceiro registro.

A revisão de Cadavid et al. contém 75 artigos em sete famílias de técnicas. Foram extraídas integralmente as tabelas diretamente relacionadas a recuperação e espaçamento: **22 chaves de publicação no subconjunto de testagem** e **17 no subconjunto de espaçamento**. Há 38 publicações únicas porque Goossens et al. (2016) aparece nas duas famílias. As técnicas de enriquecimento de codificação permanecem fora desta rodada.

## 3. Corpus recuperado

A base estruturada contém:

- **167 publicações primárias ou chaves bibliográficas únicas recuperadas**;
- **174 relações revisão–publicação**;
- proveniência por tabela, lista marcada ou subconjunto meta-analisado;
- metadados exatos quando disponíveis e marcação `author-year-only` quando não foi possível completar a citação;
- famílias de publicação separadas de duplicatas exatas.

## 4. Sobreposição entre as revisões de Quizlet

A revisão de 2024 possui 22 referências identificáveis e a revisão de 2025 possui 25 publicações em sua tabela. Foram encontradas três publicações exatas nas duas:

- Chaikovska e Zbaravska (2020);
- Ho e Kawaguchi (2021);
- Nguyen e Le (2022).

O vigésimo terceiro registro não identificável da revisão de 2024 impede um Jaccard definitivo. O intervalo bibliograficamente possível é:

- mínimo: `3/45 = 0.0667`;
- máximo, caso o registro ausente também esteja na revisão de 2025: `4/44 = 0.0909`.

Foram ainda registrados dois vínculos prováveis, mas não confirmados, entre versões de uma mesma investigação:

- dissertação de Atalan (2022) e artigo de Atalan e Subaşı (2023);
- dissertação de Toy (2019) e artigo de Toy e Buyukkarci (2020).

Essas publicações permanecem separadas até confirmação pelo texto integral.

## 5. Subconjunto completo de profissões da saúde

Foi possível calcular sobreposição exata para três listas completas ou completas no subconjunto analisado:

- Frappa et al. — 11 publicações sobre Anki;
- Thompson e Hughes — 8 publicações em radiologia;
- Maye e Hurley — 13 publicações incluídas na meta-análise.

Resultados:

| Par | Interseção | União | Jaccard |
|---|---:|---:|---:|
| Frappa et al. 2026 × Thompson & Hughes 2023 | 0 | 19 | 0.0000 |
| Frappa et al. 2026 × Maye & Hurley 2026 | 3 | 21 | 0.1429 |
| Thompson & Hughes 2023 × Maye & Hurley 2026 | 0 | 21 | 0.0000 |

As três publicações compartilhadas por Anki e pela meta-análise médica são Durrani et al. (2024), Gilbert et al. (2023) e Lu et al. (2021). A lista de radiologia não compartilhou publicação exata com as outras duas.

Para esse subconjunto, a área coberta corrigida foi:

`CCA = (32 − 29) / (29 × 3 − 29) = 0.0517`

Esse valor representa **sobreposição leve**. Ele não autoriza combinar os efeitos, pois as revisões diferem em produto, mecanismo, população, comparador e resultado.

## 6. Outros resultados de concordância

- A lista de Trumble et al. foi recuperada em 56 chaves autor–ano. Ela permite auditoria nominal, mas não foi usada para CCA definitivo enquanto títulos e DOI não estiverem normalizados.
- Nenhuma correspondência nominal inequívoca foi encontrada entre a lista de Trumble e as listas exatas de Anki, radiologia ou a meta-análise médica. Isso não significa ausência de sobreposição conceitual: todas tratam recuperação ou distribuição em profissões da saúde.
- Cadavid et al. classificaram Goossens et al. (2016) simultaneamente como publicação de espaçamento e de testagem. Mecanismos, portanto, não são classes mutuamente exclusivas.
- Não foi calculada sobreposição definitiva de Murray et al. com o subconjunto infantil de espaçamento porque o suplemento de Murray não foi recuperado.
- Não foi calculada sobreposição entre Agarwal, Pan, Xu ou Van Hoof e as demais revisões sem suas listas de publicações.

## 7. Núcleo de síntese não redundante — proposta de trabalho

A matriz sustenta um núcleo por **função de evidência**, não por suposta superioridade:

1. **Pan e Rickard:** transferência e congruência entre prática e teste;
2. **Agarwal et al.:** aplicação em escolas e salas de aula;
3. **Trumble et al.:** implementação e relato nas profissões da saúde;
4. **Maye e Hurley:** estimativa quantitativa de repetição espaçada em medicina;
5. **Özdemir e Seçkin:** estimativa quantitativa de Quizlet e vocabulário;
6. **Murray et al.:** matemática como domínio com resultados menos uniformes;
7. **Cadavid et al.:** desenvolvimento infantil e condições de fronteira.

As revisões de Anki, radiologia, enfermagem e a atualização descritiva de Quizlet permanecem como suplementos de produto ou domínio. Xu et al. permanece suplemento potencial até obtenção do texto integral.

Essa seleção não descarta revisões: apenas evita usar sínteses sobrepostas como se fossem réplicas independentes.

## 8. Consequências para a taxonomia da ARA

A sobreposição reforça que a taxonomia não deve usar nomes de produtos como mecanismos. Os seguintes campos precisam permanecer separados:

- produto ou ambiente;
- recuperação, espaçamento, intercalação e feedback;
- domínio e nível educacional;
- autoria e qualidade do conteúdo;
- formato da prática e da avaliação;
- horizonte de retenção;
- resultado cognitivo, afetivo ou de uso;
- publicação, experimento e família de estudo.

## 9. Lacunas ainda abertas

A matriz deverá ser atualizada quando forem obtidos:

- a tabela integral de Xu et al.;
- a tabela de Van Hoof et al.;
- a lista de 67 relatórios de Pan e Rickard;
- a lista de 37 publicações de Agarwal et al.;
- o suplemento de Murray et al.;
- a identificação do vigésimo terceiro estudo declarado por Özdemir e Seçkin;
- a décima quarta publicação da revisão sistemática de Maye e Hurley, que não entrou na meta-análise.

Até essa atualização, métricas globais para as 12 revisões seriam enganosas e não serão calculadas.
