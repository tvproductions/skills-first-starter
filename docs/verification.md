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
