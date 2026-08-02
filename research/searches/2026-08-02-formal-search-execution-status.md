# Formal PubMed and ERIC search execution status — round 01

**Date:** 2026-08-02  
**Issue:** #16  
**Status:** prepared, not executed to completion

## Work completed

- final pilot strings were prepared for PubMed and ERIC;
- official execution links were constructed and preserved in `2026-08-02-formal-search-links.md`;
- expected output fields and preservation rules were documented;
- the formal-search issue requires official counts, identifiers, exports and deduplication before closure.

## Execution limitation

The current execution environment could not submit the constructed arbitrary query URLs to the official PubMed ESearch endpoint or export the ERIC result set. The available web-access layer permits retrieval of indexed pages and search results but blocked direct execution of the newly constructed database URLs. The local code environment has no external network access.

Consequently:

- no official result count has been recorded;
- no PMID, ERIC, RIS, CSV or JSON export has been fabricated;
- no deduplication count has been claimed;
- Issue #16 remains open.

## Required completion evidence

The next valid execution must preserve:

1. the exact PubMed ESearch JSON response, including `count`, `querytranslation` and identifier list;
2. the ERIC official result count and exported record set;
3. file names, timestamps and cryptographic hashes of raw exports;
4. a deduplicated dataset derived from the raw files;
5. sensitivity checks and a sample review for false positives;
6. links from included records to Issues #17 and #18 or their successors.

## Acceptable completion routes

- execute the links in a normal browser and commit the official exports;
- run the PubMed query through the official NCBI E-utilities API from a network-enabled environment;
- use an institutionally available bibliographic manager or database interface and export the exact search results;
- retrieve ERIC results through an official interface or supported export endpoint.

General search-engine result counts, estimated counts, manually assembled result lists and reconstructed dates are not acceptable substitutes.

## Governance decision

This partial work may be merged because it preserves the exact protocol and the blocker. It must not close #16 or be cited as a completed formal search. Focused syntheses can continue with explicitly classified sources, but claims of completeness must wait for the official executions.
