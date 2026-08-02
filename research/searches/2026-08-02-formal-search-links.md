# Official search execution links — round 01

**Date:** 2026-08-02  
**Issue:** #16  
**Status:** execution links prepared for official database/API retrieval

## PubMed ESearch

Exact query:

```text
((flashcard*[Title/Abstract] OR "digital flashcard"[Title/Abstract] OR "digital flashcards"[Title/Abstract] OR "electronic flashcard"[Title/Abstract] OR "electronic flashcards"[Title/Abstract] OR "spaced repetition"[Title/Abstract] OR "retrieval practice"[Title/Abstract] OR Anki[Title/Abstract] OR Quizlet[Title/Abstract]) AND (learn*[Title/Abstract] OR education[Title/Abstract] OR student*[Title/Abstract] OR instruction[Title/Abstract] OR assessment[Title/Abstract]))
```

Official API URL:

https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=100000&sort=pub+date&term=%28%28flashcard%2A%5BTitle%2FAbstract%5D+OR+%22digital+flashcard%22%5BTitle%2FAbstract%5D+OR+%22digital+flashcards%22%5BTitle%2FAbstract%5D+OR+%22electronic+flashcard%22%5BTitle%2FAbstract%5D+OR+%22electronic+flashcards%22%5BTitle%2FAbstract%5D+OR+%22spaced+repetition%22%5BTitle%2FAbstract%5D+OR+%22retrieval+practice%22%5BTitle%2FAbstract%5D+OR+Anki%5BTitle%2FAbstract%5D+OR+Quizlet%5BTitle%2FAbstract%5D%29+AND+%28learn%2A%5BTitle%2FAbstract%5D+OR+education%5BTitle%2FAbstract%5D+OR+student%2A%5BTitle%2FAbstract%5D+OR+instruction%5BTitle%2FAbstract%5D+OR+assessment%5BTitle%2FAbstract%5D%29%29

Expected output: JSON containing the official result count, translated query and all PMIDs up to the API limit.

## ERIC

Exact query:

```text
(flashcard* OR "digital flashcard*" OR "electronic flashcard*" OR "spaced repetition" OR "retrieval practice" OR Anki OR Quizlet) AND (learn* OR education OR student* OR instruction OR assessment)
```

Official interface URL:

https://eric.ed.gov/?q=%28flashcard%2A+OR+%22digital+flashcard%2A%22+OR+%22electronic+flashcard%2A%22+OR+%22spaced+repetition%22+OR+%22retrieval+practice%22+OR+Anki+OR+Quizlet%29+AND+%28learn%2A+OR+education+OR+student%2A+OR+instruction+OR+assessment%29

Expected output: official result count and record set from the ERIC interface. Any export method exposed by the interface must be preserved without inferring missing records from a web search engine.

## Rules

- Counts must be copied from official outputs only.
- Raw results must be preserved separately from screened or deduplicated records.
- Query revisions require a new execution identifier.
- General web-search results do not substitute for either execution.
