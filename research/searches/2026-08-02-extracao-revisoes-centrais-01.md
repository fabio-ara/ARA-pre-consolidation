# Execução de descoberta e extração — revisões centrais 01

**Data:** 2 de agosto de 2026  
**Issue:** #14  
**Tipo:** descoberta dirigida, verificação bibliográfica e extração de revisões  
**Estado:** concluída para a primeira síntese; não equivale às futuras buscas formais completas em bases

## 1. Objetivos

- verificar metadados e acesso das revisões centrais;
- extrair resultados, métodos e limitações necessários à primeira síntese crítica;
- localizar versões abertas ou aceitas;
- identificar revisões adicionais sobre quizzes de baixo risco e programação móvel;
- preparar a próxima etapa de buscas formais com contagem e exportação.

## 2. Consultas de descoberta

As consultas foram executadas em busca web acadêmica e direcionadas a páginas oficiais, periódicos, PubMed, ERIC e repositórios institucionais:

```text
site:pubmed.ncbi.nlm.nih.gov electronic flashcards health professions education scoping review 2025 Barrison
site:pmc.ncbi.nlm.nih.gov Anki Use and Academic Performance in Medical Education systematic review 2026
site:onlinelibrary.wiley.com Effectiveness of Spaced Repetition in Medical Education systematic review meta-analysis 2026
site:eric.ed.gov mobile learning tools teaching programming logic systematic literature review 2023
Retrieval Practice Consistently Benefits Student Learning full text systematic review 2021
site:link.springer.com/article/10.1007/s10648-021-09595-9
site:eric.ed.gov Retrieval Practice Consistently Benefits Student Learning
site:pubmed.ncbi.nlm.nih.gov distributed practice verbal recall tasks quantitative synthesis 2006 Cepeda
formative assessment feedback learning higher education systematic review 2021 Morris Perry Wardle
frequent low stakes quizzes meta-analysis real classes 52 samples 7864 Sotola Crede 2021
site:eric.ed.gov frequent low stakes quizzes meta analysis academic performance real classes
2023 2024 2025 systematic review mobile programming education app learning programming smartphone
site:eric.ed.gov programming learning app mobile education 2024 2025
```

## 3. Fontes prioritárias verificadas

### PubMed e PMC

- Barrison et al. (2025), PMID 39774058.
- Frappa et al. (2026), PMID 42183420, PMCID PMC13197492.
- Maye e Hurley (2026), PMID 41601436.
- Cepeda et al. (2006), PMID 16719566.

### ERIC

- Agarwal, Nunes e Blunt (2021), ERIC EJ1319572.
- Sotola e Crede (2021), ERIC EJ1296076.
- Coelho, Marques e Oliveira (2023), ERIC EJ1410469.

### Periódicos e repositórios

- Springer Nature: Agarwal et al. (2021).
- Berklee Research Media and Information Exchange: versão aceita de Agarwal et al. (2021).
- Wiley / Review of Education: Morris et al. (2021).
- Wiley / The Clinical Teacher: Maye e Hurley (2026).
- ERIC full text: PDF integral de Coelho et al. (2023).

## 4. Procedimento de extração

Para cada revisão foram registrados:

- tipo de revisão;
- domínio e população;
- período e bases pesquisadas, quando disponíveis;
- quantidade de estudos, experimentos, amostras ou efeitos;
- intervenção e comparação;
- medidas e resultados centrais;
- heterogeneidade e riscos de generalização;
- acesso disponível nesta rodada;
- implicações como variáveis de pesquisa, sem adoção automática no produto.

A extração foi consolidada em:

- `research/pt-BR/sintese-revisoes-centrais-01.md`;
- `research/data/review-of-reviews-01.csv`.

## 5. Verificações numéricas

Foram conferidos diretamente nas fontes acessadas:

- Barrison et al.: 64 estudos; utilização 51/64; resultados associados 38/64; desenvolvimento 12/64; entrega 16/64.
- Frappa et al.: 11 estudos; três estudos com associação consistente para Step 1; diferenças relatadas de 4–13 pontos em alguns estudos.
- Maye e Hurley: 542 registros; 14 estudos na revisão; 13 na meta-análise; 21.415 participantes; SMD 0,78; IC95% 0,56–0,99.
- Agarwal et al.: aproximadamente 2.000 resumos triados; 50 experimentos; 49 efeitos; n=5.374; 57% dos efeitos médios ou grandes; 6% fora de países WEIRD.
- Cepeda et al.: 839 avaliações; 317 experimentos; 184 artigos.
- Sotola e Crede: 52 amostras; n=7.864; d=0,42; d=0,51 quando quizzes contribuíam para nota; r=0,57 entre desempenho em quizzes e desempenho acadêmico; OR=2,566 para aprovação.
- Morris et al.: 12.599 registros após deduplicação inicial; 3.290 após triagem de títulos; 188 textos elegíveis e avaliados; 27 estudos com classificação 3 estrelas e um com 4 estrelas mantidos na síntese principal.
- Coelho et al.: três bases; período 2011–2022; 12 ferramentas; ausência de amostra e duração em vários estudos.

## 6. Limites desta execução

- Acesso ao texto integral não foi uniforme.
- Alguns periódicos forneceram apenas resumo ou prévia.
- Nenhuma contagem de busca própria em PubMed, ERIC, Scopus, Web of Science, ACM ou IEEE foi registrada nesta rodada.
- Consultas web foram usadas para descoberta e acesso, não como substitutas de buscas formais.
- A síntese não realizou nova meta-análise nem reanálise estatística.
- Resultados publicados em 2026 são recentes e deverão ser confrontados com atualizações, críticas e estudos posteriores.

## 7. Próximas execuções formais

### 7.1 PubMed — flashcards, recuperação e espaçamento

Estratégia piloto a adaptar e executar diretamente na interface:

```text
(
  flashcard*[Title/Abstract]
  OR "electronic flashcard*"[Title/Abstract]
  OR "digital flashcard*"[Title/Abstract]
  OR "spaced repetition"[Title/Abstract]
  OR "retrieval practice"[Title/Abstract]
  OR Anki[Title/Abstract]
  OR Quizlet[Title/Abstract]
)
AND
(
  education[Title/Abstract]
  OR learning[Title/Abstract]
  OR student*[Title/Abstract]
  OR teaching[Title/Abstract]
  OR assessment[Title/Abstract]
)
```

### 7.2 ERIC — recuperação, quizzes e feedback

Estratégia piloto:

```text
(
  "retrieval practice"
  OR flashcard*
  OR "spaced repetition"
  OR "low-stakes quiz*"
  OR "frequent quiz*"
)
AND
(
  learning
  OR achievement
  OR retention
  OR transfer
  OR feedback
)
```

### 7.3 Programação móvel — atualização 2023–2026

```text
(
  "mobile programming education"
  OR "programming learning app*"
  OR "coding learning app*"
  OR "mobile learning" AND programming
  OR SoloLearn
  OR Mimo
  OR "Programming Hub"
  OR Encode
  OR Enki
)
AND
(
  learning
  OR feedback
  OR transfer
  OR usability
  OR self-directed
  OR engagement
)
```

Cada execução formal deverá registrar string final, base, campos, filtros, data, contagem, exportação, deduplicação e alterações de sensibilidade. Nenhum desses dados será reconstruído posteriormente por estimativa.
