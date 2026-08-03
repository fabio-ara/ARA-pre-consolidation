# ARA disposable adapters — round 01

This directory contains four non-production reference adapters used to test the schema-level contracts from Issue #36/PR #37.

## Purpose

The round tests whether one narrow lifecycle can support four materially different response families without introducing renderer geometry, third-party fields, protected tests or executable component code into canonical course and response documents.

The adapters are disposable research instruments. They are not production components and do not select the final stack.

## Families

- `semantic-mathematics`: infix input, semantic interpretation preview, validity and property-level outcomes;
- `relational-construction`: semantic node/edge state, operation history, derived SVG layout and linear non-drag editing;
- `executable-programming`: JavaScript response, Node worker host tests and browser public-test worker;
- `source-argument`: text selection, stable source digest, selector re-resolution, evidence links and human-review handoff.

## Shared lifecycle

Every Node adapter implements:

```text
load(instance)
start()
importResponse(response)
exportResponse()
validate(options)
produceFeedback(validation)
dispose()
```

`exportResponse()` is the canonical boundary. Renderer state, layout, worker internals and protected tests are excluded.

## Reproduction

Requirements used in this round:

- Node.js `22.16.0`;
- Python `3.13.5` with Playwright;
- Chromium `144.0.7559.96`.

Commands:

```bash
npm test
node scripts/build-standalone.mjs
python tests/browser_walkthrough.py
npm run measure
```

`standalone.html` is a generated offline demonstration with no external network requests or runtime dependencies.

## Security limits

The JavaScript worker and Node `vm` reference runtimes demonstrate lifecycle, timeouts, output limits and host-only protected tests. Neither is accepted as a production security sandbox. The programming adapter is intentionally classified as contract-compatible but runtime-rejected for production.

## Accessibility limits

Keyboard order, non-drag controls, live regions and 320 CSS-pixel reflow were exercised in Chromium. This is not a conformance claim and did not include an assistive-technology user study. Dense graphs, code editing and text-range selection require later specialist evaluation.

## Licensing

Prototype code is licensed under AGPL-3.0-or-later. Original research documentation and structured reports are licensed under CC BY 4.0 unless a file states otherwise. No third-party runtime library is bundled in this round.
