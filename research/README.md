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
- `pt-BR/enquadramento-genero-ara-01.md`: provisional scholarly and product-genre framing beyond flashcards.
- `pt-BR/briefing-redesenho-resources-primeiros-principios-01.md`: first-principles brief for representations, activities, responses, validators and runtimes.
- `pt-BR/prototipos-contratos-componentes-primeiros-principios-01.md`: schema-level prototype synthesis across four response families.
- `pt-BR/registro-decisoes-legado-aralearn-prototipos-01.md`: provisional retain, split, replace, merge and retire decisions for AraLearn concepts.
- `pt-BR/relatorio-adapters-descartaveis-01.md`: executable adapter findings, rejected production assumptions and proposed contract amendments.

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
- `pt-BR/matriz-sobreposicao-estudos-primarios-01.md`: primary-publication overlap map for the 12 priority-A formal syntheses.
- `data/priority-a-review-completeness-01.csv`: included-study-list completeness and metric eligibility by synthesis.
- `data/priority-a-primary-publications-01.csv`: normalized recovered primary-publication keys.
- `data/priority-a-review-publication-incidence-01.csv`: review-by-primary-publication incidence data.
- `data/priority-a-pairwise-overlap-01.csv`: pairwise exact, bounded and ineligible overlap comparisons.
- `data/priority-a-study-families-01.csv`: confirmed and probable cross-publication study-family links.
- `data/priority-a-nonredundant-core-01.csv`: working non-redundant synthesis-core proposal.
- `data/priority-a-overlap-summary-01.json`: overlap-map counts and bounded metrics.
- `data/priority-a-overlap-file-manifest-01.csv`: hashes for the overlap-map package.
- `pt-BR/auditoria-resources-aralearn-01.md`: canonical audit of the implemented AraLearn v4 resource contracts.
- `data/aralearn-resource-inventory-01.csv`: resource structure, exercise modes, limits, provisional decisions and known constraints.
- `data/aralearn-resource-gap-targets-01.csv`: formal gap and structured-practice targets by resource.
- `data/aralearn-domain-scenario-coverage-01.csv`: disciplinary coverage and current response limitations.
- `data/aralearn-resource-audit-summary-01.json`: source commit, canonical resource list and audit-level conclusions.
- `data/aralearn-resource-audit-source-manifest-01.csv`: audited source paths, roles and authority status.
- `pt-BR/benchmark-sistemas-estruturados-transdominio-01.md`: critical comparison of 21 structured, interactive and domain-specific systems.
- `data/cross-domain-repository-manifest-01.csv`: repositories, pinned revisions, paths, families and license status.
- `data/cross-domain-system-benchmark-01.csv`: representation, response, validation, feedback, authoring and runtime comparison.
- `data/cross-domain-capability-map-01.csv`: capabilities and first-principles directions derived from the benchmark.
- `data/cross-domain-knowledge-domain-coverage-01.csv`: coverage of knowledge domains absent or weak in the AraLearn-origin corpus.
- `data/structured-learning-literature-01.csv`: exploratory scholarly map for structured interactive learning environments.
- `data/cross-domain-benchmark-summary-01.json`: machine-readable benchmark and genre conclusions.
- `data/component-contract-comparison-01.csv`: cross-track comparison of representation, activity, response, validity, authority and domain grammar.
- `data/component-contract-accessibility-security-01.csv`: accessibility, offline and security requirements by prototype family.
- `data/aralearn-legacy-concept-decisions-02.csv`: prototype-informed decisions for AraLearn legacy concepts.
- `data/component-contract-validation-report-01.json`: reproducible JSON Schema validation result and limitations.
- `data/component-contract-prototype-summary-01.json`: machine-readable conclusions and next work.
- `data/component-contract-file-manifest-01.csv`: sizes and SHA-256 hashes for the prototype artifacts.
- `data/disposable-adapter-comparison-01.csv`: representation, validity, authority, offline result and production blockers by adapter family.
- `data/disposable-adapter-accessibility-walkthrough-01.csv`: keyboard, focus, live-region, reflow, visual and accessibility-tree observations.
- `data/disposable-adapter-security-threat-model-01.csv`: executed and inferred security scenarios with production implications.
- `data/disposable-adapter-license-risk-01.csv`: licenses and follow-up risks for the reference environment and candidate libraries.
- `data/disposable-adapter-contract-amendments-01.csv`: ten implementation-informed amendments proposed for contract version `0.2`.
- `data/disposable-adapter-measurements-01.csv`: source size and lifecycle measurements for the dependency-free reference adapters.
- `data/disposable-adapter-test-summary-01.json`: Node, browser and environment validation counts.
- `data/disposable-adapter-summary-01.json`: machine-readable round conclusions and next work.
- `data/disposable-adapter-file-manifest-01.csv`: hashes for stable source, test and structured artifacts.

### Prototype contracts

- `prototypes/component-contracts-01/README.md`: package scope, files, reproduction command and normative limits.
- `prototypes/component-contracts-01/schemas/`: shared manifest, lifecycle and four domain-family schemas.
- `prototypes/component-contracts-01/examples/`: manifests, complete instances, validation scenarios and microsequences.
- `prototypes/component-contracts-01/validate_examples.py`: local Draft 2020-12 validation script.
- `prototypes/disposable-adapters-01/README.md`: scope, shared lifecycle, reproduction commands and explicit non-production limits.
- `prototypes/disposable-adapters-01/src/`: four adapters, browser harness and worker references.
- `prototypes/disposable-adapters-01/tests/`: Node contract tests and Chromium interaction walkthrough.
- `prototypes/disposable-adapters-01/reports/`: raw test, measurement and accessibility-tree outputs.

### Search records

- `searches/2026-08-02-aplicativos-e-flashcards.md`: first exploratory mapping of applications and flashcards.
- `searches/2026-08-02-expansao-sistemas-relacionados.md`: planned search fronts for additional systems and experiences.
- `searches/2026-08-02-execucao-exploratoria-sistemas-ampliados.md`: verified exploratory execution for the expanded system map.
- `searches/2026-08-02-extracao-revisoes-centrais-01.md`: source verification and extraction record for the first review corpus.
- `searches/2026-08-02-formal-search-links.md`: exact PubMed and ERIC pilot strings and official execution links.
- `searches/2026-08-02-formal-search-execution-status.md`: initial execution blocker and completion requirements.
- `searches/2026-08-02-formal-search-validation-round-01.md`: validation of the received identifier and ERIC exports.
- `searches/2026-08-02-formal-search-completion-round-01.md`: completed PubMed–ERIC comparison and final publication count.
- `searches/2026-08-02-structured-interactive-environments-scoping.md`: exploratory search beyond flashcards and formal follow-up fronts.

### Schemas, templates and libraries

- `schemas/registro-fonte.md`: source-status and bibliographic record schema.
- `schemas/extracao-estudo.md`: detailed extraction schema for included studies.
- `templates/registro-busca.csv`: reproducible search log template.
- `templates/triagem.csv`: screening template.
- `library/referencias-iniciais.bib`: verified seed and central review references.
- `library/referencias-sistemas-iniciais.bib`: official and academic references for related learning systems.
- `library/referencias-formatos-feedback.bib`: references for response formats, scoring and feedback.
- `library/referencias-programacao-movel-2023-2026.bib`: references for the post-2022 mobile programming update.
- `library/referencias-ambientes-interativos-01.bib`: open bibliography for interactive environments, representations, simulations and assessment.
- `requests/textos-integrais.md`: general precise requests for inaccessible material.
- `requests/textos-integrais-prioridade-a.md`: three priority full-text requests required to deepen the priority-A extraction.

## Governance

This programme is governed by GitHub Issue #3 and the canonical roadmap. Focused reviews receive their own protocols and issues when the initial mapping demonstrates that a narrower synthesis is warranted. The first review-of-reviews corpus is governed by Issue #14; response formats and feedback are governed by Issue #17; the mobile programming update is governed by Issue #18; formal PubMed and ERIC execution is governed by Issue #16; first-pass title-and-abstract screening is governed by Issue #24; priority-A full-text retrieval and extraction is governed by Issue #26; primary-study overlap mapping is governed by Issue #28; canonical AraLearn resource auditing is governed by Issue #31; cross-domain system benchmarking is governed by Issue #33; scholarly genre mapping is governed by Issue #34; first-principles component-contract prototyping is governed by Issue #36; disposable adapter implementation and testing is governed by Issue #38.

Unless a file states otherwise, original documentation in this directory is licensed under CC BY 4.0.
