# Initial scaffold verification — October 9, 2026

The initial source passed these local checks on Python 3.13.15:

- Thirteen unittest cases covering preview/no-write, idempotence, preservation
  of existing instructions/configuration, disabled/foreign plugin conflicts,
  gzkit separation, symlink destinations, legacy skill copies, profile preservation,
  malformed settings, immutable pins, and matching catalogs.
- Ruff 0.15.18 lint and formatting checks.
- Bundle validation against independently resolved published upstream revisions.
- Skill Creator frontmatter/name validation for `adopt-skills-stack`.
- Claude Code strict marketplace validation: no errors or warnings.

Codex CLI 0.160.0 recognized the local marketplace through command-scoped
configuration. Its read-only plugin listing did not return this bundle's
available entries, including with network access. No plugin add or global
configuration mutation was performed. This is a native-loading verification
gap, not a passing installation receipt. Complete the fresh-session Codex
installation proof before claiming the bundle is loaded or project-scoped
native operation is verified.

No application projects were migrated or operational records accessed. Backplane
remains a pre-release published commit. End-to-end Claude operation, OpenCode,
combined-stack runtime conformance, update/rollback automation, and the FDAU pilot
are not established by these local tests. CI provides the separate Python-version
matrix; report its actual result rather than assuming these local checks prove it.

## Backport and front-door update — October 9, 2026

Nineteen unittest cases passed on Python 3.13.15, including deferred Backplane
configuration, preservation of existing enabled Backplane state, front-door
preservation/duplicate discovery, and bounded read-only structural assessment.
Both starter skills passed Skill Creator validation; Ruff lint/format and bundle
validation passed. The three upstream revisions and native catalogs are unchanged.

No target application was restructured or plugin installed. The new front door
is authored and staged by the helper; fresh-session native discovery is still
unverified. The backport assessment is a starting inventory, not evidence that
an application's structure or behavior has been audited.
