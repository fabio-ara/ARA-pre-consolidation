# ARA external adapter audit — round 01

This package evaluates three external candidates behind the canonical ARA `0.2` boundary:

- a MathLive/MathJSON-oriented mathematical-input adapter;
- a Cytoscape.js relational adapter;
- a Recogito Text Annotator W3C-selector adapter.

## What was executed

The project-authored boundary adapters and replacement tests were executed locally. They demonstrate that:

- mathematical widget state can be reduced to original input and a canonical semantic expression;
- graph elements can be reduced to semantic nodes and edges while positions and renderer state remain derived;
- W3C-style quote and position selectors can be converted to ARA annotations without DOM ranges or library stores;
- replacing an adapter does not alter course-side canonical documents.

## What was not executed

External packages were not bundled or run in a browser because the execution environment could not resolve external package or CDN hosts and its package mirror did not provide the candidates. The official repositories and API/type surfaces were audited at pinned commits instead.

This is an environment limitation, not a finding against the libraries. Runtime bundle, interaction, accessibility and performance evaluation remains required in a network-enabled reproducible environment.

## Commands

```bash
npm test
```

The tests use library-shaped fixtures and do not claim runtime compatibility, educational effectiveness or accessibility conformance.
