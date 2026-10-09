---
name: skills-first-start
description: Orient an agent in a skills-first project, choose among project workflows, Superpowers and gz-skills, or guide adoption and structural backporting of the starter.
---

# Start a skills-first task

Read the project's AGENTS.md and referenced authorities first. Identify the user's
actual task and available skills; recommend the smallest useful workflow and then
continue the authorized task. This skill is orientation, not another lifecycle.
Do not invoke every audit or reinterpret a small task as an architecture project.

| Need | Route after confirming discovery |
| --- | --- |
| Run an application operation | Project-owned operational skill and supporting code |
| Design or implement a feature | Installed Superpowers `using-superpowers` entry and its task workflow |
| Select an engineering discipline | Installed gz-skills `gzs-router` |
| Adopt the bundle or translate existing structure | Starter `adopt-skills-stack` and `docs/backport.md` |
| Backlog or handoff continuity | Existing project practice; SP-BP is deferred |

Check actual skill discovery before claiming an entry is available. A pinned
catalog or configuration is not an installed skill. If the target skill is
missing, identify the gap and use its reviewed source instructions when useful;
do not silently install it. The starter's own adoption skill can be read from a
reviewed checkout when it is not exposed through native discovery.

The maintained guidance lives at https://github.com/tvproductions/skills-first-starter.
Use the revision recorded in `.skills-first/bundle.lock.json` when present.
From that reviewed checkout, `python3 starter.py backport --project <root>` gives
a read-only starting assessment. Build a source-to-target mapping before changes;
retain project authorities, domain rules, records, and working verification.

SP and gz-skills are the current default pair. SP-BP stays cataloged but disabled
until readiness and explicit adoption are established. Do not invent its missing
issue automation or replace project backlog authority with local starter code.
No gz-skills lite/heavy profile is inferred here. Upstream main proposals are
not capabilities in the pinned release. Keep upstream sources independently
versioned, and never install their skills through duplicate discovery paths.

For current SP/gz-skills releases or development snapshots, follow the reviewed
starter's `docs/adoption.md` update procedure. Query upstream before saying
“latest”; preserve exact source pins and verify actual loading after an update.
