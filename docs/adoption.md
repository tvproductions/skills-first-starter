# Adoption and native loading

## Establish the project boundary

Use a separate reviewed checkout of `tvproductions/gz-skills-first-starter`. Record
its full published commit SHA and review `bundle.json`. The configure helper
uses that checkout's HEAD unless `--starter-ref <full-SHA>` is supplied. Supplying
a SHA records your selection; the helper does not prove it is published. Verify
it before applying:

```bash
git rev-parse HEAD
gh api repos/tvproductions/gz-skills-first-starter/commits/FULL_STARTER_SHA --jq .sha
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
/plugin marketplace add tvproductions/gz-skills-first-starter
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

## Getting current SP and gz-skills

Check upstream at adoption time rather than assuming this template's baseline
is newest. As checked October 9, 2026, the latest published releases are SP
**v6.4.2** and gz-skills **v0.5.0**; the starter currently pins SP v6.4.1 and
gz-skills v0.5.0. These observations expire as upstream releases change.

From a shell with authenticated GitHub CLI, obtain each latest published release
and resolve its tag to a full commit SHA:

```bash
sp_tag=$(gh api repos/obra/superpowers/releases/latest --jq .tag_name)
sp_revision=$(gh api "repos/obra/superpowers/commits/$sp_tag" --jq .sha)
gzs_tag=$(gh api repos/tvproductions/gz-skills/releases/latest --jq .tag_name)
gzs_revision=$(gh api "repos/tvproductions/gz-skills/commits/$gzs_tag" --jq .sha)
printf 'SP: %s %s\nGZS: %s %s\n' "$sp_tag" "$sp_revision" "$gzs_tag" "$gzs_revision"
```

Review the release notes and installation guidance at each exact revision:
[SP releases](https://github.com/obra/superpowers/releases) and
[gz-skills releases](https://github.com/tvproductions/gz-skills/releases).
A failed query is not proof that a release is absent. Resolve network or access
errors before choosing a version. Do not run upstream bootstrap scripts blindly.

Latest published release and latest development commit are different choices.
For an explicitly requested development version, resolve `commits/HEAD` through
the same repository API, review its changes, and record its full SHA with release
set to null and status identifying an unreleased development snapshot. Never put
`main`, `HEAD`, or a moving tag in the catalog's revision field. gz-skills main
may contain setup behavior absent from v0.5.0; inspect that version's profile
contract and retain an explicit user profile choice. Proposals are not shipped
capabilities just because they appear on main.

To adopt newer versions in the shared starter:

1. Change each selected component's release, revision and accurate status in
   `bundle.json`. Keep SP-BP disabled. Updating SP or gz-skills does not depend on
   Backplane's old compatibility baseline while Backplane is deferred.
2. Change the corresponding full SHA in both native catalogs:
   `.agents/plugins/marketplace.json` and `.claude-plugin/marketplace.json`.
   Keep upstream ownership and plugin names intact.
3. Run the repository's tests, bundle validation and lint/format checks. Publish
   the reviewed starter revision and record host verification separately.
4. For a new adopter, configure from that reviewed starter checkout, then follow
   the active host's native installation steps above. For an existing adopter,
   review the configuration/lock/entry-skill diff as described below; the helper
   deliberately refuses to overwrite older managed files.
5. Use the installed host manager's supported update/reinstall operation after
   reviewing its current help. Verify the selected marketplace source, actual
   loaded revision and fresh-session skill discovery; a manager saying “updated”
   or a changed lock alone does not prove that the newest selected source loaded.
   Retain the prior pins for rollback.

Do not edit cached upstream skills, duplicate their installation under a second
marketplace, or silently update unrelated projects. To use a project-specific
version ahead of the shared baseline, record it in a separately reviewed catalog
and reconcile the existing discovery source explicitly. Do not leave the shared
bundle lock claiming one revision while another is installed.

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
