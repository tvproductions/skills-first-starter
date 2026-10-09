# Skills-first starter

For adoption into another project, start at
`skills/adopt-skills-stack/SKILL.md` and preserve that project's instructions.
For continuation of starter development, read
`docs/handoffs/2026-10-09-starter-continuation.md`; recheck live state before work.

This repository owns the bundle catalog, adoption helper, native marketplace
adapters, and guidance. Read README.md and docs/architecture.md before changes.
This is a public scaffold; use invented fixtures and preserve upstream ownership.

SP, SP-BP, and gz-skills are independent components. FDAU is the primary design
precedent. SP-BP is an expected addition to the target stack, currently deferred
until readiness and explicit adoption are established. Keep existing backlog
and handoff authority. Do not vendor upstream skills, introduce a gzkit lifecycle,
or infer app domain rules from another adopting project. App operational skills and
supporting domain code remain project-owned.

For Python work, read `skills/python-engineering/SKILL.md`. Non-gzkit projects
started from this starter require uv-managed, pinned Python 3.14, current clear
Python idioms and suitable stdlib APIs. Consult versioned official documentation
for behavior changes, deprecations and removals; configuration alone does not
supply engineering policy. Keep metadata and tool targets aligned and validate
on the actual pinned interpreter. The documented XPPython3 host exception pins
its supported version and explains the difference.

The routine standard is Ruff check/format, ty, unittest (never pytest), and
pre-commit running those checks. Favor strict, reviewed lint rules. On-demand
hygiene selects Ruff C901 (cyclomatic ceiling 20), complexipy (cognitive ceiling
15), Lizard (cyclomatic scores and aggregates), Interrogate, Vulture, Bandit, branch/statement
coverage through unittest, Cosmic Ray mutation testing, deptry, pip-audit and
Import Linter; none belongs in hooks or CI gates. Keep the approved routine
pre-commit set limited to Ruff check/format, ty and unittest. C901 is enabled only
in explicit hygiene commands, not routine Ruff selection. The new complexity
policy retires Xenon and Radon. The on-demand `skills/python-engineering/scripts/complexity_check.py` implements
function/module/overall ceilings of 20 under the reviewed `lizard-functions-v1`
contract. Read the skill reference; this is an explicit rebaseline, not exact
Radon equivalence. Syntax/discovery errors fail closed.
Record legacy baselines that may only shrink. Cosmic Ray is
selected but its Python 3.14 compatibility remains unverified. The exact expanded
Ruff rules, utility ownership and existing-project adoption mechanism remain
unsettled. Current starter tooling lacks ty and pre-commit; do not describe this
guidance as completed enforcement. Preserve existing project authorities while
reporting adoption gaps. No broad application refactoring is implied.

Validate pins and both catalogs after a bundle change. Use unittest, not pytest.
Test consequential adoption behavior at the public helper seam. Preserve existing
project files, explicit profile choices, and native manager state. A config file
or successful manifest validation cannot prove fresh-session skill discovery.
Report unverified host behavior and Backplane pre-release limitations explicitly.

Checks: `uv run --python 3.14 -m unittest discover -s tests -v`, `uv run --python 3.14 starter.py validate`,
`uvx --python 3.14 ruff==0.15.18 check .`, and `uvx --python 3.14 ruff==0.15.18 format --check .`.
No plugin installation, GitHub issue mutation, tag, or release publication is
implied by editing this repository. Follow the user's actual authorization.

Strong Python/tool preferences belong to this starter and its project binding.
Keep gz-skills and SP agnostic; SP-BP should remain agnostic as well. Do not
propagate these choices into upstream plugins. Review dependency freshness
periodically on demand (at adoption, tool upgrades, and quarterly maintenance),
including runtime/dev tools and pinned plugin releases; distinguish release age
from abandonment. See the Python skill. Do not add review hooks or automatic
schedules, or upgrade dependencies without a scoped request.

When designing features or reviewing dependencies, assess concrete Python 3.14
gains over 3.13 using the Python skill's versioned opportunity guide. Record
benefits, compatibility risks and adopt/defer decisions; do not treat a runtime
pin as sufficient guidance or add machinery without a project need.
