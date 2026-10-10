# Starter continuation — October 9, 2026

## Authority and final stack

Read root AGENTS.md, README.md, docs/architecture.md and docs/adoption.md.
This handoff describes the final changes prepared for publication; verify live
HEAD, worktree, remote and CI before continuing. Historical measurements and
verification notes are in docs/verification.md and docs/evidence/.

The active default is Superpowers + gz-skills. SP-BP is an expected third
component, pinned but deferred and explicitly disabled until readiness and
explicit adoption are established. Existing backlog/handoff authority remains.
The baseline pins are SP v6.4.1 and gz-skills v0.5.0; this change does not update
upstream pins, choose a lite/heavy profile, or certify combined native loading.
FDAU is the primary precedent. gzkit is a separate heavier ecosystem and its
lifecycle is not imported. App operational skills and deterministic domain code
remain project-owned.

Strong Python/tool preferences belong to starter and its project binding.
SP and gz-skills remain agnostic; SP-BP should be agnostic too. No upstream
plugin implementation changed. Review released upstream updates independently;
the bundled baseline is not a latest-version claim.

## Implemented starter behavior

- Immutable bundle and native marketplace catalogs; SP-BP disabled by default.
- Preview/apply/status helper preserving existing instructions, configurations,
  profiles and installed sources; conflicts stop writes.
- Read-only bounded structural backport assessment and incremental mapping guide.
- Bootstrap front door that prefers gzs-router for engineering catalog selection
  and SP using-superpowers for feature work.
- Python engineering skill with runtime/idiom, stdlib/adapter, persistence,
  version-aware design and on-demand hygiene guidance.

The helper still copies only the front-door skill. Read the Python engineering
skill from a reviewed starter checkout until its native discovery/adoption is
established. Configuration generation is not plugin installation or discovery
proof. Native project installation, fresh-session conformance, Claude end-to-end
adoption and OpenCode remain unverified/deferred.

## Final Python and hygiene choices

Starter targets Python >=3.14,<3.15, Ruff py314, and a uv runtime pin. Verification
used uv-managed Python 3.14.8. CI now uses uv and Python 3.14 only; earlier
3.11/3.13/3.14 results do not prove this new workflow. Check its live run.

The required routine standard is Ruff check/format, ty and unittest through
pre-commit. Existing routine Ruff selection is preserved. ty/pre-commit
configuration and agreed stricter Ruff rules remain pending in starter; policy
is not a claim that those tools are enforced here.

The selected complexity tools are **Ruff 0.15.18 + complexipy 8.0.1 + Lizard
1.24.1**, pinned in the explicit hygiene group. Xenon and Radon are retired from
starter's selected toolchain. Ruff C901 20 and complexipy cognitive 15 are
independent checks, not interchangeable measurements. Deeper hygiene remains
explicitly on demand: no complexity hooks, manual hooks, CI gates or scheduler.

Other on-demand selections are Interrogate, Vulture, Bandit, Coverage.py through
unittest, Cosmic Ray, deptry, pip-audit and Import Linter. Their installation and
full Python 3.14 proofs remain pending; Cosmic Ray is selected, not verified.
pip-audit inspects pinned uv exports without a second resolution. Review package
and pinned-plugin freshness at adoption, reviewed upgrades and quarterly
maintenance on demand; release age alone does not establish abandonment.

Consult the skill's Python 3.14 opportunity guide during design/dependency
review. Assess concrete benefits over 3.13 and porting risks; a version pin
alone supplies no API/idiom guidance or permission for broad modernization.

## Settled C/C/C contract

Read skills/python-engineering/references/ccc-contract.md. The explicit checker
is skills/python-engineering/scripts/complexity_check.py, contract
**lizard-functions-v1**:

- Original source and native Lizard 1.24.1 scores; no Radon emulation or syntax
  normalization. Count functions, async functions, methods and nested functions
  once each. Omit synthetic class blocks, lambdas and module-level statements.
- Ceiling 20 for each function, each module's arithmetic function mean, and the
  overall function-weighted mean. Compare unrounded scores; 20 passes.
- Native assertion semantics: assert itself adds no decision; Boolean decisions
  in its expression count. Empty module means are undefined and excluded from
  denominators; empty scopes without Python files are errors.
- Compile/parse and AST function discovery must agree. Lizard's skipped inline
  suites are unsupported measurements, not hidden passes. Do not rewrite app
  code solely to satisfy Lizard. Missing tools, wrong versions, discovery errors
  and invalid scopes return exit 2; violations return 1; clean checks return 0.
- Explicit relative source scopes, path deduplication, symlink refusal and
  excluded plugin/archive/environment/output trees. No application execution.

This is a reviewed function-based rebaseline, not universal Xenon/Radon parity.
The equal ceilings make averages mathematically bounded by the maximum, but
all three remain explicitly reported and enforced. Preserve failures and compare
stable identities/scores; do not waive them by regenerating snapshots.

## Verification and evidence

Nineteen adoption tests, ten on-demand checker CLI tests, bundle validation,
routine Ruff lint/format and engineering-skill validation passed on Python 3.14.8.
Run checker tests explicitly with the hygiene group; they are not routine CI
complexity gates. Unsupported inline-suite and generated-code suppression tests
verify visible measurement errors rather than fabricated scores.

Final receipts: docs/evidence/2026-10-09-starter-ccc-v1.json and
2026-10-09-cob-reports-ccc-v1.json. Both retain absolute complexity failures with
zero tool errors. Starter has one function violation (maximum 31). Source-only
cob_reports verification measured 88 files and 649 functions: maximum 100,
overall mean 7.14946, 42 function violations and 12 module violations.
No cob_reports dependencies, hooks or app code changed; no protected data was
accessed. Its workboard records the external checker assessment.

The earlier comparison receipt records 585/621 matching legacy function scores.
Combined exploratory Ruff/Lizard/complexipy checks caught all 43 legacy failing
functions and added 31 failures. Class/nested populations differ. These are
specific corpus observations, not a universal compatibility guarantee.

Gzkit issue #1183 records Xenon/Radon retirement and the final findings:
https://github.com/tvproductions/gzkit/issues/1183
Gzkit issue #1184 requests its separate Python 3.14 opportunity/support review:
https://github.com/tvproductions/gzkit/issues/1184
Neither issue implies gzkit implemented starter's checker or changed support.

## Next useful work

1. Check the published revision's CI and independently test authorized native
   onboarding/discovery in a disposable project; record exact loaded sources.
2. Establish Python skill adoption and routine ty/pre-commit enforcement without
   expanding the approved hook set or copying upstream plugin skills.
3. Scope existing complexity remediation separately; retain honest failures.
4. Verify the other selected hygiene tools on invented Python 3.14 fixtures.
5. Review broader gz-skills routing and new-project skeleton improvements only
   when authorized. Keep upstream preferences portable and SP-BP deferred.


## Repository rename — October 10, 2026

The operator renamed the public GitHub template to tvproductions/gz-skills-first-starter. Canonical URL: https://github.com/tvproductions/gz-skills-first-starter. Existing local development checkout remains /Users/jbabb/Documents/Devel/skills-first-starter; the Git origin is updated to the new URL. The skills-first-starter marketplace identifier, Python project name and adoption identities remain unchanged for compatibility. SP-BP remains expected and deferred; no upstream pins or installation behavior changed.
