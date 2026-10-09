# Skills-first starter

A reusable, project-scoped starting point for **Superpowers + Superpowers
Backplane + gz-skills**, with room for each application's own operational skills
and supporting code. Built for work and personal projects under `tvproductions`.

This repository is the bundle catalog, adoption tool, and guidance home. It is
not another development lifecycle or an application framework. Existing projects
can adopt it without replacing their architecture. **xplane-fdau is the primary
reference implementation**, not a template whose domain rules should be copied.

## Quick start: an existing or empty project

Requires Python 3.11+, Git, Codex with plugin support, and GitHub CLI for
Backplane's GitHub workflows. No Python dependencies are needed for this tool.

```bash
gh repo clone tvproductions/skills-first-starter
cd skills-first-starter
python3 starter.py validate
python3 starter.py configure --project /path/to/your-project
python3 starter.py configure --project /path/to/your-project --apply
```

The first configure command previews paths without writing. The second writes
project Codex settings, a pinned bundle record, and an instructions fragment.
Existing `AGENTS.md` is preserved; new projects get an entry pointing to the
fragment. Existing configuration is extended only when it is compatible.
Conflicts, legacy duplicate skill discovery, symlinked destinations, and gzkit
projects stop before any writes. Repeating adoption with the same inputs is a
no-op. Review the configuration before trusting it in Codex.

Then follow [native installation and verification](docs/adoption.md). Configuring
files does **not** install plugins, authenticate GitHub, or prove skill discovery.
The native managers own their caches; upstream skills are never copied here.

```bash
python3 starter.py status --project /path/to/your-project
```

For agent-guided adoption, read [the adoption skill](skills/adopt-skills-stack/SKILL.md).
You can also [use this repository as a GitHub template](https://github.com/tvproductions/skills-first-starter/generate),
then configure your new checkout from a separate, reviewed starter checkout.
A generated repository inherits the starter files; simplify it for your product
rather than turning this scaffolding into runtime dependencies. Running the copied
helper inside an adopting repo requires an explicit published `--starter-ref`;
the default refuses to mistake an adopting repo commit for a starter revision.

## The initial bundle

The canonical pins are in [bundle.json](bundle.json). Both native catalogs use
those exact full commit SHAs, not moving branches.

| Component | Initial baseline | Owns |
|---|---|---|
| [Superpowers](https://github.com/obra/superpowers) | v6.4.1 | Feature design, plans, implementation, review |
| [Superpowers Backplane](https://github.com/tvproductions/superpowers-backplane) | Published pre-release commit | GitHub-backed backlog and handoff continuity |
| [gz-skills](https://github.com/tvproductions/gz-skills) | v0.5.0 | Portable engineering disciplines |
| Your app | Project-owned | Operational workflows, domain rules, code, evidence |

Superpowers v6.4.2 exists, but this starter initially selects v6.4.1 because
Backplane's recorded compatibility proof uses that version. This is a reviewed
starting set, **not a blanket compatibility certification**. Backplane has no
published release; its remaining host acceptance and external pilot are tracked
upstream. The pinned gz-skills release contains sixteen skills and predates the
newer project-setup skill on upstream main. We do not silently adopt unreleased
setup behavior or select its lite/heavy profile.

## Current scope

- Implemented: immutable bundle catalogs, Codex project configuration, preview,
  idempotent adoption, conflict preservation, status, and automated tests.
- Claude Code: native bundle marketplace supplied; project install guidance
  documented. End-to-end installation is not verified by this starter yet.
- OpenCode: deferred until Backplane's adapter and variant verification exist.
- Fresh-session skill discovery and Backplane conformance remain operator-run
  checks; configuration or a manifest version is never treated as proof.
- No GitHub issue mutation, app migration, global installation, scheduling,
  autonomous jobs, or release publication occurs through `starter.py`.

See [architecture](docs/architecture.md), [adoption](docs/adoption.md), and
[roadmap](ROADMAP.md) for the boundary and remaining work.

## Checks

```bash
python3 -m unittest discover -s tests -v
python3 starter.py validate
uvx ruff check .
uvx ruff format --check .
```

The tool uses Python's standard library. A consuming application chooses its own
runtime, quality tools, constraints, and public contracts. This starter does not
impose FDAU's Python version or any numeric quality gate on other projects.

## Attribution and license

Original starter code and documentation are MIT licensed. Referenced projects
retain their own licenses and owners. The catalogs point to upstream sources;
this repository does not redistribute upstream skills. See [NOTICE](NOTICE).
