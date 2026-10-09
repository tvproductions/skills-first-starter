---
name: python-engineering
description: Apply the skills-first starter's Python 3.14 engineering standards when developing, reviewing, or modernizing its non-gzkit projects; run deeper hygiene or mutation analysis only when requested.
---

# Python engineering

This skill binds the starter's Python standards to project engineering work.
These standards are required for projects started from this starter, not an
optional profile. gzkit is a separate ecosystem. Read the project's AGENTS.md,
configuration and current evidence; preserve unrelated work and operational
contracts. In an existing project, report gaps before proposing a bounded
adoption change. This skill does not authorize a broad application refactor.

## Runtime and version-aware decisions

Use uv-managed, pinned Python 3.14. Confirm the actual interpreter through
`uv run --managed-python --python 3.14 python --version`. Keep `requires-python`,
`.python-version`, Ruff's `py314` target, ty's Python target, hooks and CI aligned.
The documented exception is an X-Plane tool whose XPPython3 host requires another
Python version: pin the supported version, explain why and align tool targets.

Prefer clear current Python idioms and suitable standard-library APIs. Runtime
metadata constrains tools; it does not establish which APIs or idioms are
appropriate. Check the official [Python 3.14 release notes](https://docs.python.org/3.14/whatsnew/3.14.html)
and versioned [library documentation](https://docs.python.org/3.14/library/)
when behavior, syntax, deprecations or removals matter. In migrations, read the
intervening release notes and porting sections as well. Deferred annotation
evaluation and annotation introspection are examples that warrant inspection.
Do not mechanically remove `from __future__ import annotations` or substitute
new syntax without checking its effect on consumers and dependencies. Validate
changed behavior on the pinned runtime; keep modernization within task scope.

For design and dependency review, read the [3.14 opportunity guide](references/python314-opportunities.md)
and assess concrete gains over 3.13: annotation introspection, bounded executor
submission, appropriate stdlib file/compression APIs and structured templates.
Choose adopt/defer/not-applicable with evidence; a successful migration is not
proof that new capabilities were evaluated. Keep this binding starter-owned.

## Routine engineering

Use project-locked Ruff check, Ruff format, ty and unittest through uv; never
pytest. Pre-commit runs the routine checks. Inspect available configuration
before giving executable commands; report missing tooling rather than claiming
it is installed. Favor strict linting with a pinned Ruff release and reasoned
exceptions. The exact expanded rule set remains to be agreed; do not silently
select ALL, suppress findings or loosen thresholds to pass.

Combine TDD, BDD and DDD for consequential behavior: first demonstrate a failure
at a public seam, describe observable outcomes and model domain meanings. Favor
hexagonal architecture: the domain core performs no I/O, defines ports, and
adapters own external effects. Skills orchestrate commands and hold no domain
logic. Use the available SP and gz-skills workflows for their portable design
and engineering disciplines; this skill supplies the Python-specific binding.

Prefer the standard library, including `sqlite3` for SQLite. Pydantic is allowed.
Record any other dependency's purpose and resource cost, and keep it at an
adapter boundary outside the domain core. A skill-local script serves only its
own skill and imports no other skill's scripts. Shared code or a system of
record belongs in a package behind one CLI.

## On-demand hygiene and mutation testing

Run deeper tools when requested, never as hooks, manual hooks, CI gates or an
automatic consequence of routine changes. Resolve and pin development tools
through uv after their Python 3.14 compatibility is established. Use explicit
source/test scopes and invented fixtures; exclude operational data and records.

| Tool | Required interpretation |
| --- | --- |
| Ruff C901 | On-demand cyclomatic ceiling 20 per function; never raise the threshold to pass |
| complexipy | On-demand cognitive ceiling 15 per function/module-level script; exposes nesting/readability costs |
| Lizard | Per-function cyclomatic measurements and module/project aggregates for a reviewed C/C/C approximation; do not claim Radon-equivalent scores |
| Interrogate | Measure docstring presence; review usefulness and correctness separately |
| Vulture | Investigate dead-code candidates and external consumers before deletion |
| Bandit | Review severity, confidence and code context; no blanket suppressions |
| Coverage.py | Measure branch and statement coverage through unittest; report consequential gaps |
| Cosmic Ray | Selected mutation tester; use a unittest test command and bounded mutation scope |
| deptry | Check missing, unused and directly used transitive dependencies; review dynamic imports before changing declarations |
| pip-audit | Audit exact resolved dependencies for known vulnerabilities; record scope, skipped packages and advisory results |
| Import Linter | Verify project-specific forbidden imports and layers, including indirect violations of domain/adapter boundaries |

These three additions are selected on-demand tools, not extra pre-commit checks.
Use [deptry's rules](https://deptry.com/rules-violations/) against the actual
project metadata; distinguish runtime dependencies, development tools and
plugin-discovered imports. Findings do not authorize package removal.
Define [Import Linter contracts](https://import-linter.readthedocs.io/en/stable/contract_types/)
from the project's real domain, ports and adapters. Keep reviewed contracts in
project configuration; do not invent a package layout or blanket-ignore debt.

[pip-audit](https://github.com/pypa/pip-audit) works with uv-managed environments
and pinned requirements exports. Keep uv as the resolver: export the existing
lock with `uv export --locked --format requirements.txt --no-emit-project`
to a task-specific temporary file, choosing the intended dependency groups.
Check the export contains exact versions and the full selected transitive set.
Run the project-pinned auditor through uv against that file with `--no-deps`
and `--disable-pip` to avoid a second resolver. Retain exported hashes. Do not
claim direct `uv.lock` support from `pip-audit --locked`; the documented native
lockfile format is `pylock.*.toml`. Record what was audited and what was skipped;
no known advisories is not proof of absence of vulnerabilities. Do not run
`--fix` or upgrade packages as part of a check-only request.

### Complexity policy: Ruff, complexipy and Lizard

Ruff 0.15.18 and complexipy 8.0.1 passed the starter's focused Python 3.14.8
syntax, threshold-boundary and invalid-syntax checks. The selected toolchain now adds Lizard 1.24.1 and retires both Xenon and
Radon. The saved two-tool receipt is historical; use the new three-tool receipt
for Lizard evidence. Ruff measures cyclomatic branching;
complexipy adds cognitive costs such as nesting. Use cyclomatic 20 and cognitive
15 as ceilings, not targets to write up to. Cyclomatic 20 retains the numeric
upper boundary of Radon's former C rank, but Ruff and Radon counting differs.
Cognitive 15 is a separate metric, not a translation of C/C/C. Use Lizard's
per-function measurements to recover the three-part approach: maximum function
score, each module's mean, and the overall function-weighted mean. Starting
cyclomatic ceilings are 20/20/20, under the reviewed function-based contract for classes, nested functions,
assertions, exclusions and empty modules. These ceilings are implemented by the explicit Lizard checker; see the
[counting contract](references/ccc-contract.md) before running or adopting it.
When all three use the same population and ceiling, the maximum already bounds
the averages; retain averages for visibility and future stricter policies.
Lizard's counting differs from Radon and Ruff. Compare changed scores and
verdicts explicitly; complexipy's script score is not a module average. This changes only the starter's policy;
do not rewrite other projects' complexity contracts without authorization.

The starter pins all three tools in the explicit `hygiene` dependency group. Their
purpose is static development analysis. Ruff/complexipy add native wheels;
Lizard adds a Python analyzer. All use uv storage/download resources, with no
application runtime dependencies or service calls. Run from the reviewed starter root, replacing REPORT_DIR with an unused
task-specific temporary directory created first:

```bash
uv run --managed-python --python 3.14 --group hygiene ruff check --select C901 --ignore-noqa starter.py tests skills/python-engineering/scripts
uv run --managed-python --python 3.14 --group hygiene complexipy starter.py tests skills/python-engineering/scripts --cache-dir REPORT_DIR/cache --output-format json --output REPORT_DIR/cognitive.json
```

Run all three even when one reports findings. Use the evaluation probe for
Lizard compatibility scores. Run `scripts/complexity_check.py` explicitly for
the C/C/C gate using the contract command and source scope. In an adopting project, select
its explicit source and invented-test paths and use its reviewed tool pins.
Do not add C901 to routine Ruff selection, complexipy to hooks, or complexity
checks to CI. No routine pre-commit selection changes are implied.

The [historical two-tool baseline](../../docs/evidence/2026-10-09-complexity-evaluation.json)
contains source hashes and scores: `configure` is cyclomatic 21/cognitive 57;
`project_config` is cyclomatic 10/cognitive 28. These remain failures against the
ceilings, not waived passes. New code meets both ceilings; existing over-limit
functions may only improve, with no new over-limit functions. Compare stable
file/function identities and scores, not only failure counts. Do not regenerate
a snapshot to hide regressions, suppress findings or raise limits. Refactoring
is separately scoped and verified. Routine checks passing does not establish
that the on-demand complexity checks are clean.

The [three-tool receipt](../../docs/evidence/2026-10-09-three-tool-complexity-evaluation.json)
records current source hashes, Lizard measurements and aggregates.

See [the evaluation procedure](references/complexity-evaluation.md) to reproduce
the compatibility checks and interpret the evidence. Full Python grammar support
is not established by the synthetic cases.

Record comparable legacy measurements and findings as a baseline that may only
shrink. Do not transplant another project's Interrogate, coverage or mutation
percentage thresholds. Write useful docstrings; do not add filler or redundant
tests to improve a score.

For Cosmic Ray, first prove a clean unmodified test baseline, then use an
isolated disposable code checkout, a bounded time budget and per-test-run
timeouts. Keep session databases and reports outside source and operational
records. Classify surviving mutants, equivalent mutants, timeouts and tool
errors separately; inspect survivors before adding meaningful tests. A failed
baseline or broken tool execution is not a successful mutation assessment.
Its [official tutorial](https://cosmic-ray.readthedocs.io/en/latest/tutorials/intro/index.html)
documents a configurable unittest command. Selection does not prove Python 3.14
compatibility: verify a pinned release with a small synthetic unittest fixture
before adopting it. No Cosmic Ray compatibility or installation proof exists in
this starter yet.

## Periodic dependency freshness review

During adoption, reviewed tool upgrades and quarterly maintenance, explicitly
review runtime dependencies, development/hygiene tools and pinned SP/gz-skills/
SP-BP releases. This is an on-demand maintenance workflow, not a scheduled job,
hook, CI gate or automatic consequence of ordinary code changes. Keep deferred
SP-BP disabled.

Inspect declarations and the current uv lock. Where supported, use
`uv tree --outdated` to identify newer package releases without changing the
lock. Check official release history, meaningful source/test activity, supported
Python versions, unresolved compatibility issues and vulnerability advisories.
Treat a year without releases as a review signal, not proof of abandonment;
recent cosmetic commits are not proof of analyzer maintenance. Record the
checked date, pinned/latest versions, evidence links, risks and recommendation.
Separate freshness, compatibility and vulnerability findings. Propose bounded
upgrades or replacements; do not refresh every pin or change upstream plugin
policy merely to make the list current. Verify changed tools on pinned Python
3.14 before adoption and retain comparable complexity evidence.

Strong tool preferences belong to this starter binding. gz-skills and SP remain
agnostic, and SP-BP should be agnostic too; no upstream edits are authorized by
this skill. Readiness and explicit adoption still govern SP-BP participation.

## Ownership and evidence

Keep code in a Git development checkout and data in a separate location. Live
databases remain local outside synced storage. For persistence, use immutable
applied migration entries, refuse to silently initialize a missing live record,
and create and verify a recovery copy with the data after every write; a failed
recovery copy fails the run. Resolve paths from one configuration module with
environment overrides. Commands are read-only or dry-run unless explicitly
asked to write; output names, counts and status only. New program-input filenames
contain no spaces; do not rename existing inputs without a reviewed migration.

Report actual checks, unresolved failures and unverified capabilities. Current
SP and gz-skills remain independently owned. SP-BP is an expected addition to
the target stack, deferred until readiness and explicit adoption are established;
existing backlog and handoff authority remains in place. Never infer plugin
installation, a profile choice or publication permission from this skill.
