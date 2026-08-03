# ARA design system v1

## Foundations

- Semantic HTML first; ARIA only for established composite-widget behavior.
- System font stack; user text/zoom preferences respected.
- Four spacing increments: 4, 8, 16 and 24 CSS px; larger compositions use multiples.
- Content reading measure targets 45–80 characters where appropriate.
- Default touch controls target at least 44×44 CSS px; minimum never violates WCAG 2.2 AA.
- Focus indicator is persistent, high contrast and not obscured.
- Motion is functional, brief and disabled/reduced by user preference.

## Semantic tokens

Tokens are named by purpose, not fixed hue:

- surfaces: canvas, panel, elevated, selected, disabled;
- text: primary, secondary, muted, inverse, danger;
- borders: default, strong, focus, danger;
- actions: primary, secondary, quiet, destructive;
- states: draft, review, ready, published, offline, syncing, warning, error, success.

All themes meet contrast requirements. Status never relies on hue alone.

## Typography

- body: 1rem minimum user-scalable;
- small metadata: not below 0.875rem;
- headings use semantic levels, not visual-only size;
- code/IDs use monospace only in advanced views;
- labels remain visible; placeholders are examples, not labels.

## Core components

- Button, Link, IconButton with accessible name and optional text label;
- TextField/TextArea/Select/Combobox/Checkbox/Radio/Switch;
- Alert, ErrorSummary, InlineError, Toast for non-critical confirmations only;
- Card/ResourceFrame/PracticeFrame/FeedbackPanel;
- Tabs for small stable peer views; Disclosure for optional detail;
- Dialog only for short consequential confirmation; complex work uses pages/drawers;
- Breadcrumb/ContextHeader;
- StatusBadge with text;
- DataTable for static data; Grid/Treegrid only when keyboard interaction is implemented and tested;
- Tree/List alternative for course composition/dependency graphs;
- DiffViewer with unified, side-by-side and semantic-summary modes;
- SyncIndicator/OperationQueue/ConflictPanel;
- EmptyState/Skeleton/Progress; progress labels include current action.

## Layout

Breakpoints are content-driven. At narrow widths, side panes become ordered pages/bottom sheets and preserve a clear return path. Sticky elements never obscure keyboard focus. Two-dimensional views provide list/table alternatives and fit-to-content controls.

## Content design

- Commands use verbs and objects: “Publicar versão”, not “Confirmar”.
- Destructive labels state effect: “Remover download local”; “Solicitar exclusão”.
- Technical terms have plain-language label plus optional identifier.
- Dates/times include locale and timezone where consequential.
- No success claims such as “aprendido” from completion or events.

## Icons

Icons supplement visible labels in primary actions. Icon-only actions are restricted to established repeated controls, always with accessible name and tooltip available on focus/hover.

## Visual density

Default comfortable density. Compact density is opt-in for desktop tables/queues and cannot reduce target or focus accessibility. Study cards never inherit administrative density.
