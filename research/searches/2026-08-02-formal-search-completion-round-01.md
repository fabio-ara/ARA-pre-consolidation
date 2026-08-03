# Formal PubMed and ERIC search completion — round 01

**Date:** 2026-08-02  
**Issue:** #16  
**Status:** official exports received; within- and cross-database publication deduplication completed

## 1. Inputs validated

### PubMed

- ESearch official count: **827**
- PMIDs in ESearch JSON: **827**
- PubMed Citation Manager records: **827**
- unique PMIDs in Citation Manager export: **827**
- Citation Manager PMID set exactly matches the ESearch PMID set: **yes**
- PubMed publication duplicates removed: **0**

### ERIC

- official interface count reported: **728**
- exported records: **728**
- batch sizes: **200 + 200 + 200 + 128**
- overlapping ERIC accession numbers between batches: **0**
- exact ERIC publication duplicates removed: **2**
- ERIC records retained after internal deduplication: **726**

## 2. Cross-database deduplication

Matching was performed in this order:

1. exact normalized DOI;
2. exact normalized title with the same publication year when no shared DOI was available;
3. manual review of high-similarity title candidates to avoid merging related but distinct publications.

Results:

- exact DOI matches: **81**
- exact title/year match without shared DOI: **1**
- total PubMed–ERIC publication duplicates: **82**
- canonical record for cross-database duplicates: **PubMed**
- ERIC accession numbers are preserved as alternate identifiers

No additional high-similarity candidate was removed without exact bibliographic support.

## 3. Final counts

| Stage | Records |
|---|---:|
| Raw PubMed + ERIC | 1,555 |
| After within-database deduplication | 1,553 |
| After cross-database deduplication | **1,471** |

Composition of the final publication set:

- PubMed canonical records: **827**
- ERIC-only records: **644**

## 4. Related publications retained

The deduplication operates at publication level. Separate reports of one study are linked, not automatically deleted.

Retained examples include:

- a 1987 ERIC meeting paper and its 1988 journal article;
- a PubMed preprint and the later journal article with the same title but different DOI;
- a primary study and a WWC evidence review of that study;
- an original article and its correction notice.

## 5. Derived files

- `formal-search-round-01-file-manifest.csv`
- `eric-round-01-duplicate-decisions.csv`
- `formal-search-round-01-cross-database-duplicates.csv`
- `formal-search-round-01-related-publications.csv`
- `formal-search-round-01-summary.json`

A screening-ready dataset with the retained metadata and abstracts was also generated in the complete research package handed off to the project owner.

## 6. Integrity

Every raw file was checked by byte size and SHA-256 hash. The PubMed Citation Manager file and ESearch JSON were compared by exact PMID set rather than assumed to represent the same result set.

## 7. Interpretation boundary

The final count of **1,471** represents unique publications after deterministic bibliographic deduplication. It is not a count of unique experiments or independent participant samples. Multiple publications may belong to the same study family and will be linked during extraction.
