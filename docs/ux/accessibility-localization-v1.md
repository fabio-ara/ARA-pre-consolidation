# ARA accessibility and localization specification v1

## Accessibility baseline

Target WCAG 2.2 AA for complete approved journeys, with additional focus visibility and 44px preferred targets where feasible.

Required:

- keyboard access and logical focus order;
- skip links/landmarks/headings;
- no focus obscured by sticky regions;
- accessible authentication without cognitive-test-only barriers;
- reflow at 320 CSS px and 400% zoom;
- pointer alternatives for drag, resize and spatial editing;
- persistent labels and descriptive errors;
- live announcements for operation/sync state without excessive interruption;
- screen-reader alternatives for graph, tree, flow, matrix and visual diff;
- captions/transcripts/alt descriptions according to content contract;
- reduced motion, high contrast and user font/zoom support;
- no forced disclosure for ordinary accessible choices;
- accommodation details restricted by purpose and role.

Composite patterns follow tested WAI-ARIA APG keyboard models. Native HTML is preferred. A treegrid/grid is used only when its interaction cost is justified; otherwise use semantic lists/tables.

## Course resources

Every ResourceType contract declares:

- reading/interaction order;
- accessible name/description;
- non-visual equivalent;
- keyboard behavior;
- zoom/reflow constraints;
- contrast/non-color semantics;
- fallback for unsupported capability;
- authoring validation and preview checks.

## Locales and language

Interface locales: `en`, `pt-BR`, `pt-PT`. Course content language is independent and can vary within a course/resource.

Rules:

- all user-visible strings use stable message keys;
- no concatenated translated fragments;
- plural/date/number/list formatting use locale APIs;
- critical dates include timezone/absolute form;
- IDs and technical values remain language-neutral;
- search supports diacritics without erasing meaningful distinctions;
- translated course revisions retain derivation and review status;
- machine translation is draft status until approved;
- layout tests include 30–50% string expansion;
- legal/consent text is jurisdiction-specific and separately reviewed.

## Error and status terms

Canonical concepts have plain-language locale terms plus stable English identifiers in advanced/audit views. Status vocabulary is consistent across study, authoring and research; identical words are not reused for incompatible states.

## Testing

- automated axe-like checks as a floor;
- keyboard and screen reader tests on representative browsers/platforms;
- zoom/reflow and touch-target checks;
- assistive-tech review of study, authoring, conflict, protocol and publication flows;
- locale visual regressions and truncation checks;
- user evaluation including people with relevant access needs.
