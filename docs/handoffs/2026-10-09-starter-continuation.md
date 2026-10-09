# Starter continuation — October 9, 2026

## Purpose and authority

This public GitHub template provides a reusable skills-first adoption pattern
for work and personal projects. The active default is Superpowers + gz-skills;
SP-BP is the future third component and is not ready for normal adoption.
FDAU is the primary precedent. gzkit is a separate heavier process and must not
be imported. Project-owned operational skills and deterministic domain code
remain separate from independently versioned engineering plugins.

Read root AGENTS.md, README.md, docs/architecture.md and docs/adoption.md.
Recheck the repository HEAD, worktree changes, current upstream versions and
CI; this handoff is context, not a replacement for live evidence.

## Implemented

- Immutable three-component bundle and Codex/Claude native catalogs.
- Preview/apply/status helper preserving existing instructions, configuration,
  explicit profiles and independently installed sources; conflicts stop writes.
- SP and gz-skills enabled by default, SP-BP explicitly disabled.
- Read-only bounded top-level backport assessment and source-mapping guidance.
- Starter-owned bootstrap entry skill, with gz-skills selection routed to
  `gzs-router` and SP feature work routed to `using-superpowers`.
- Instructions to query latest released SP/gz-skills versions, resolve full SHAs,
  review updates and distinguish unreleased main from published releases.

The current baseline is SP v6.4.1 and gz-skills v0.5.0. SP v6.4.2 was the latest
published release checked today. Update SP independently of deferred Backplane
when requested and reviewed. Do not silently activate a lite/heavy profile.
Matt Pocock adaptations in gz-skills remain candidate design in the inspected
catalog, not delivered capabilities of the pinned v0.5.0 release.

## Verified and pending

Nineteen unittest cases, bundle validation, Ruff checks and skill validation
passed. Commit 0222e123fcdc8b8be6b3b8699c54311be7bf6cf5 passed GitHub CI on
Python 3.11, 3.13 and 3.14. Check later commits' actual CI results separately.
No adopting application has been migrated, and no plugins were installed by
this work. Codex recognized the local marketplace but did not list its available
entries in the earlier read-only probe. Fresh-session discovery and project-scope
installation remain unverified; see docs/verification.md. Claude end-to-end
adoption and OpenCode remain unverified/deferred.

## Next useful work

1. Independently test onboarding from the public README in an authorized,
   disposable project. Verify native installation, scope, exact loaded sources,
   and discovered entry skills. Record failures without claiming success from
   file generation or manifest validation alone.
2. Complete a concrete existing-project pilot: map current authorities, skills,
   code and records before structural moves. The assessment is not a code audit.
3. Propose broader routing in gz-skills upstream when authorized. The desired
   primary front door is `gzs-router`; currently the starter bootstrap explains
   the remaining cross-stack routes. No upstream router changes were made here.
4. Consider a minimal new-project skeleton: using GitHub's template currently
   copies starter maintenance tooling as well as adoption guidance, so product
   cleanup is needed. Do not describe this as a finished product generator.

Keep Backplane disabled until its readiness and explicit adoption are established.
Do not turn a fresh-chat test into permission to mutate production GitHub issues,
install global plugins or migrate an unspecified application.
