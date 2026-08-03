# ARA research and evidence programme

This directory preserves the reproducible evidence base used to define ARA's pedagogical parameters, research capabilities, product requirements, architecture, legal analysis and future empirical studies.

## Working language

Brazilian Portuguese (`pt-BR`) is the canonical working language for protocols, screening notes, extraction records and preliminary syntheses. Stable public summaries are translated according to the repository language policy.

## Principles

- The literature is investigated before product decisions are treated as general rules.
- Evidence, inference, design hypothesis, operational decision and personal preference remain distinct.
- Reviews, handbooks and institutional guidance are used to map a field; central claims are checked against primary studies when necessary.
- A source is never represented as read in full when only metadata, an abstract or a secondary citation was available.
- Restricted full texts are not committed to the public repository.
- Search strings, dates, databases, result counts, screening decisions and extraction records are versioned.
- Bibliographic work supports both self-directed customization and formal educational research.

## Current structure

### Protocol and framing

- `pt-BR/protocolo-mestre.md`: master protocol for the evidence programme.
- `pt-BR/inventario-ucs-metd.md`: initial mapping of the supplied University of Lisbon course-unit sheets.
- `pt-BR/mapa-inicial-evidencias.md`: seed evidence map and first candidate sources.
- `pt-BR/antecedentes-aplicativos.md`: situated account of formative applications, MOOCs and learning environments.

### Syntheses and structured data

- `pt-BR/sintese-revisoes-centrais-01.md`: first critical review-of-reviews synthesis.
- `data/review-of-reviews-01.csv`: structured comparison of the first eight central reviews.
- `pt-BR/sintese-formatos-resposta-feedback-01.md`: focused synthesis of response formats, scoring, feedback content, timing and retry cycles.
- `data/response-feedback-evidence-01.csv`: structured evidence table for the response and feedback review.
- `pt-BR/atualizacao-programacao-movel-2023-2026.md`: provisional post-2022 update of mobile and microlearning evidence in programming education.
- `data/mobile-programming-update-2023-2026.csv`: structured source table for the programming update.
- `data/system-activity-feedback-matrix.csv`: initial cross-system matrix of activities, feedback, progression, consequences and evidence status.
- `data/formal-search-round-01-file-manifest.csv`: counts, sizes and SHA-256 hashes for the first formal PubMed and ERIC exports.
- `data/eric-round-01-duplicate-decisions.csv`: explicit ERIC duplicate and study-family decisions.
- `data/formal-search-round-01-cross-database-duplicates.csv`: deterministic PubMed–ERIC duplicate mappings.
- `data/formal-search-round-01-related-publications.csv`: related publications retained as distinct records.
- `data/formal-search-round-01-summary.json`: final formal-search and deduplication counts.
- `pt-BR/triagem-titulo-resumo-rodada-01.md`: first single-reviewer title-and-abstract screening report.
- `data/formal-search-round-01-screening-summary.json`: screening decisions, source counts, priority tiers and audit totals.
- `data/formal-search-round-01-screening-reason-counts.csv`: counts by screening decision and reason code.
- `data/formal-search-round-01-screening-manual-overrides.csv`: documented manual changes and refined reasons.
- `data/formal-search-round-01-screening-file-manifest.csv`: hashes for the complete screening package handed to the project owner.
- `pt-BR/sintese-corpus-prioridade-a-01.md`: critical extraction and reclassification of the 26 priority-A publications.
- `data/priority-a-formal-syntheses-round-01.csv`: structured extraction of the 12 formal evidence syntheses.
- `data/priority-a-other-evidence-round-01.csv`: structured extraction of narrative reviews, empirical/product studies and the secondary appraisal.
- `data/priority-a-overlap-clusters-round-01.csv`: review-overlap and study-family risks.
- `data/priority-a-extraction-summary.json`: corrected evidence groups and access-depth counts.

### Search records

- `searches/2026-08-02-aplicativos-e-flashcards.md`: first exploratory mapping of applications and flashcards.
- `searches/2026-08-02-expansao-sistemas-relacionados.md`: planned search fronts for additional systems and experiences.
- `searches/2026-08-02-execucao-exploratoria-sistemas-ampliados.md`: verified exploratory execution for the expanded system map.
- `searches/2026-08-02-extracao-revisoes-centrais-01.md`: source verification and extraction record for the first review corpus.
- `searches/2026-08-02-formal-search-links.md`: exact PubMed and ERIC pilot strings and official execution links.
- `searches/2026-08-02-formal-search-execution-status.md`: initial execution blocker and completion requirements.
- `searches/2026-08-02-formal-search-validation-round-01.md`: validation of the received identifier and ERIC exports.
- `searches/2026-08-02-formal-search-completion-round-01.md`: completed PubMed–ERIC comparison and final publication count.

### Schemas, templates and libraries

- `schemas/registro-fonte.md`: source-status and bibliographic record schema.
- `schemas/extracao-estudo.md`: detailed extraction schema for included studies.
- `templates/registro-busca.csv`: reproducible search log template.
- `templates/triagem.csv`: screening template.
- `library/referencias-iniciais.bib`: verified seed and central review references.
- `library/referencias-sistemas-iniciais.bib`: official and academic references for related learning systems.
- `library/referencias-formatos-feedback.bib`: references for response formats, scoring and feedback.
- `library/referencias-programacao-movel-2023-2026.bib`: references for the post-2022 mobile programming update.
- `requests/textos-integrais.md`: general precise requests for inaccessible material.
- `requests/textos-integrais-prioridade-a.md`: three priority full-text requests required to deepen the priority-A extraction.

## Governance

This programme is governed by GitHub Issue #3 and the canonical roadmap. Focused reviews receive their own protocols and issues when the initial mapping demonstrates that a narrower synthesis is warranted. The first review-of-reviews corpus is governed by Issue #14; response formats and feedback are governed by Issue #17; the mobile programming update is governed by Issue #18; formal PubMed and ERIC execution is governed by Issue #16; first-pass title-and-abstract screening is governed by Issue #24; priority-A full-text retrieval and extraction is governed by Issue #26.

Unless a file states otherwise, original documentation in this directory is licensed under CC BY 4.0.
