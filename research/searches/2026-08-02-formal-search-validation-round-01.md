# Formal PubMed and ERIC search validation — round 01

**Date:** 2026-08-02  
**Issue:** #16  
**Status:** official result exports received; within-database validation and ERIC deduplication completed; cross-database deduplication pending PubMed citation metadata

## Official search outputs received

### PubMed

- official ESearch count: **827**
- PMIDs returned: **827**
- unique PMIDs: **827**
- `retstart`: **0**
- `retmax`: **827**
- SHA-256: `67d69d01b9adf24d40ead5fedcae85343833ae3e327a6a1146e1715c23a346b2`
- official translated query preserved in the JSON
- warning preserved: the singular quoted phrase `digital flashcard` was not found as an exact phrase; PubMed retained `digital flashcards`

### ERIC

- official interface count reported by the researcher: **728**
- exported records received: **728**
- unique ERIC accession numbers before bibliographic deduplication: **728**
- batch sizes: **200 + 200 + 200 + 128**
- overlapping ERIC accession numbers between batches: **0**

| File | Records | First ERIC ID | Last ERIC ID | SHA-256 |
|---|---:|---|---|---|
| `eric-round-01-001-200.nbib` | 200 | `EJ1481349` | `EJ1492447` | `da27e8e9d6fd2c9c69f54de87b217396c03bd43281f71462e475cb91ac5265c5` |
| `eric-round-01-201-400.nbib` | 200 | `EJ1334252` | `EJ1368797` | `3b244287e2b08c18c4d41ecc7b52bdadb2459729b50fecd03fcf73acdc117c67` |
| `eric-round-01-401-600.nbib` | 200 | `EJ1142140` | `EJ597339` | `d76d36ab7154efc817bc696bb2652fb297e1e8cf10d2598abfd81ec714c7fdc3` |
| `eric-round-01-601-728.nbib` | 128 | `EJ794727` | `EJ711344` | `6e8ea2244eaf6e4c352fc4e0c9161dfe00fad2be6015fe541c74b5819b2efa08` |

The four batch counts sum to the official interface count. ERIC accession numbers are not sequential indicators of search rank, so completeness is established by the recorded range exports, expected batch counts, and absence of overlap rather than by numerical continuity of the accession identifiers.

## Within-database deduplication

### PubMed

- duplicate PMIDs: **0**
- unique identifier records retained: **827**

The ESearch JSON contains identifiers but not full citation metadata. DOI-, title- and author-based matching against ERIC cannot be completed from this file alone.

### ERIC

Two exact publication duplicates were found:

1. `ED602960` duplicates journal record `EJ1238295` — same title, authors, DOI `10.1891/1945-8959.18.2.160`, year and publication.
2. `ED645719` duplicates journal record `EJ1401499` — same title, author, DOI `10.1111/mbe.12375`, year and publication.

The journal records were retained as canonical. Therefore:

- raw ERIC records: **728**
- exact publication duplicates removed: **2**
- deduplicated ERIC bibliographic records: **726**

A third title match was not removed:

- `ED285546` (1987 conference/meeting paper)
- `EJ385854` (1988 journal article)

These are separate publications reporting the same study. They remain separate bibliographic records and are linked as one study family.

## Current combined counts

- raw database records: **1,555** (`827 PubMed + 728 ERIC`)
- records after within-database deduplication: **1,553** (`827 PubMed + 726 ERIC`)
- final cross-database unique-study count: **not yet established**

## Remaining requirement

To complete cross-database deduplication, PubMed citation metadata must be exported in NBIB/MEDLINE format for the same 827 records. This is required to compare DOI, normalized title, authors and publication year against ERIC.

No cross-database duplicate count has been estimated or inferred from identifiers alone.

## Raw-file preservation status

The files were received and validated. The repository connector used in this execution accepts UTF-8 content but not mounted-file uploads. Therefore, the raw files and generated machine-readable indexes remain pending direct repository upload. Their hashes and required paths are recorded so that the uploaded copies can be verified byte-for-byte.