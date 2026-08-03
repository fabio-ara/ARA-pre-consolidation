# Required `main` branch protection v1

**Implementation blocker:** apply before merging the first product-code PR.

Repository settings for `main`:

- require pull request before merging;
- block force pushes and deletion;
- require linear history;
- require conversation resolution;
- require branch up to date before merge;
- require status check `governance`;
- add code checks after R0 establishes them and they have run successfully: `lint`, `typecheck`, `unit`, `integration`, `build-budget`, `accessibility`, `security`, `package-conformance`;
- restrict workflow changes through CODEOWNERS review;
- do not allow bypass except emergency repository owner recovery, which requires an incident record;
- use squash merge and delete merged branches;
- require signed commits when operationally supported without blocking automated release provenance.

## Review rule

The repository currently has one human maintainer. Until a second eligible maintainer exists:

- owner-authored PRs require a documented independent review with findings resolved;
- self-approval is not represented as independent approval;
- high-risk security, data, migration and release PRs remain blocked for external/qualified review when required by their issue.

When a second maintainer exists, require at least one approval and approval of the most recent reviewable push.

## Verification record

After applying the settings, add the date, actor and settings screenshot/export to the Issue #9 completion comment and verify a test PR cannot merge with a failing required check.
