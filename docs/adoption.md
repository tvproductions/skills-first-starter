# Adoption and native loading

## Establish the project boundary

Use a separate reviewed checkout of `tvproductions/skills-first-starter`. Record
its full published commit SHA and review `bundle.json`. The configure helper
uses that checkout's HEAD unless `--starter-ref <full-SHA>` is supplied. Supplying
a SHA records your selection; the helper does not prove it is published. Verify
it before applying:

```bash
git rev-parse HEAD
gh api repos/tvproductions/skills-first-starter/commits/FULL_STARTER_SHA --jq .sha
```

Review existing `AGENTS.md`, skill discovery surfaces, plugin configuration,
and gzkit ownership. Existing project authorities remain in place. A conflict
is a request for reconciliation, not permission to remove an existing install.
The starter does not select a gz-skills profile. At the pinned release,
`gzs-project-setup` is not available; reconsider setup only after reviewing and
updating the bundle to a version that actually supplies it.

## Codex

After configure preview/apply, `.codex/config.toml` registers the shared Git
marketplace at your reviewed starter SHA and enables SP and gz-skills for that
project. SP-BP remains pinned and
explicitly disabled. The starter-owned front-door skill is placed in
`.agents/skills/skills-first-start/`; confirm its discovery in a fresh session.
Commit this project configuration after review;
installation caches remain native-harness state.

Open the project in Codex and review its trust decision. Inventory the existing
plugins and marketplaces before installation:

```bash
codex plugin marketplace list --json
codex plugin list --json
```

The marketplace is named `skills-first-starter`. If the configured project
marketplace is absent, inspect project-config loading and trust; do not work
around it by silently changing global configuration. If the same components
already appear under another marketplace or through a checkout, reconcile the
sources before adding duplicates. The helper can catch repository-local copies
and configuration conflicts, but cannot inventory another host's session.

When the correct marketplace is loaded and duplicate discovery has been ruled
out, explicitly install its components through the native manager:

```bash
codex plugin add superpowers@skills-first-starter
codex plugin add gz-skills@skills-first-starter
codex plugin list --json
```

These are user-run native installation commands, not actions performed by the
helper. Native manager commands may alter user-level installation state; inspect
the resulting configuration and keep project enablement in the adopting repo.
Installing the bundle here does not authorize global enablement for unrelated
projects. If this host cannot maintain the intended project scope, stop and
record that limitation rather than claiming project-only activation.

Start a fresh session. Confirm the actual discovered identities:

- `superpowers:using-superpowers`
- `skills-first-start` (starter-owned project skill)
- `gz-skills:gzs-router`

Backplane installation and conformance checks below apply only to a future,
explicitly authorized adoption after readiness review. They are not part of
the default pair.

Read Backplane's pinned [installation/compatibility reference](https://github.com/tvproductions/superpowers-backplane/blob/d0eeee829c491da02351e793544aa16ad96461bf/skills/managing-superpowers-backlog/references/installing-superpowers.md).
Setup verifies GitHub CLI capabilities and actual native issue fields before
backlog operation. Use an authorized disposable issue for mutation scenarios.
Do not infer a right to modify production issues from installation.

Record starter and component revisions, host version, installed source identities,
fresh-session skill discovery, and Backplane compatibility/conformance results.
Report each result as PASS, FAIL, or UNKNOWN. The starter's tests do not replace
host verification. Five Backplane checks are skill structure, native issue
intake, language-neutral verification, lifecycle transitions, and Superpowers
installation. An `UNKNOWN` is not a passing combined-stack claim.

## Claude Code

The `.claude-plugin/marketplace.json` catalog references the same three immutable
sources. From the adopting project, inspect the current manager and existing
installations first. Then use Claude's project scope:

```text
/plugin marketplace add tvproductions/skills-first-starter
/plugin install superpowers@skills-first-starter --scope project
/plugin install gz-skills@skills-first-starter --scope project
```

The displayed catalog pins component source revisions. The command above obtains
the current starter marketplace; for repeatable adoption, use a reviewed checkout
at a recorded full SHA and `/plugin marketplace add /path/to/reviewed-starter`
instead. Check the manager's current syntax before executing. Restart and verify
actual SP and gz-skills discovery. Backplane remains deferred.
Marketplace syntax validation
alone is not a completed installation or lifecycle proof.

This starter does not automate Claude project settings or claim end-to-end
Claude verification. Backplane Claude lifecycle acceptance remains upstream work.

## OpenCode

Do not generate a guessed adapter or claim readiness. Backplane's OpenCode
implementation/acceptance is pending. The bundle can add an OpenCode adapter
when those upstream contracts and negative cases have been demonstrated.

## Updates and rollback

Components remain separately owned. Do not update upstream Superpowers as a
side effect of a Backplane update. Review candidate revisions and compatibility,
change `bundle.json` and both catalogs together, then run the repository checks
and affected host tests before publishing the starter change.

The configure helper intentionally refuses an existing different lock or
marketplace revision. For an adopter update, review a diff of the new lock,
marketplace ref and instructions fragment; commit the accepted configuration
change, then use the native manager's supported update/reinstall route. No
force-overwrite or automatic update command is shipped. Preserve the prior refs
and restore the prior reviewed configuration and plugin revisions if verification
fails. Recheck discovery after either update or rollback.

To remove the stack, first inspect whether other projects use the cached plugins.
Remove this project's enablement/configuration after review. Use native plugin
removal only for installations no longer needed; never delete shared caches by
hand. Preserve app skills, operational records, and unrelated configuration.
