# Esquema de registro de fonte

Cada registro bibliográfico ou documental deve preservar os campos aplicáveis abaixo. O formato operacional poderá ser CSV, JSONL, BibTeX ou banco relacional, desde que não perca estas distinções.

## Identificação

- `record_id`: identificador interno estável.
- `source_type`: artigo, livro, capítulo, tese, dissertação, revisão, norma, lei, documentação técnica, página institucional ou outro.
- `title_original`.
- `authors_or_organization`.
- `year`.
- `publication`.
- `volume`, `issue`, `pages`.
- `doi` normalizado.
- `isbn`, `issn`, `pmid`, `arxiv_id` ou identificador equivalente.
- `canonical_url`.
- `language`.

## Descoberta

- `discovery_source`: base, lista de referências, ementa, busca web ou indicação.
- `search_id`.
- `date_discovered`.
- `query_or_path`.
- `import_batch`.

## Acesso e verificação

- `access_status`:
  - `full_text_verified`;
  - `full_text_partial`;
  - `abstract_verified`;
  - `metadata_only`;
  - `secondary_report`;
  - `requested`;
  - `unavailable`;
  - `superseded_or_retracted`.
- `access_date`.
- `access_notes`.
- `verified_by`.
- `source_file_private_reference`, quando houver, sem publicar o arquivo restrito.

## Triagem

- `screening_title_abstract`: include, exclude, uncertain.
- `screening_full_text`: include, exclude, uncertain, not_applicable.
- `exclusion_reason`.
- `screening_date`.
- `screening_notes`.

## Classificação temática

- `research_fronts`.
- `population`.
- `concepts`.
- `context`.
- `parameter_families`.
- `constructs`.
- `methods`.
- `platform_implications`.

## Integridade e qualidade

- `peer_review_status`.
- `correction_or_retraction_status`.
- `quality_appraisal_tool`.
- `quality_appraisal_result`.
- `limitations`.
- `conflicts_of_interest`.

## Proveniência da síntese

- `claims_supported`.
- `pages_or_locations`.
- `evidence_status`: evidence, inference, hypothesis, contextual_source.
- `notes`.
- `related_decisions`.
- `related_issues`.

## Regras

1. DOI e outros identificadores devem ser normalizados, sem parâmetros de rastreamento.
2. O título original não deve ser traduzido no campo canônico.
3. Uma fonte conhecida apenas por outra fonte recebe `secondary_report`.
4. A ausência de texto completo não pode ser ocultada por uma síntese convincente.
5. Razões de exclusão em texto completo devem usar vocabulário controlado e nota livre apenas quando necessário.
6. PDFs restritos não são anexados ao repositório público.