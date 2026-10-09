# Skills-first development stack

This project adopts the independently versioned components recorded in
`.skills-first/bundle.lock.json`: Superpowers (feature design and delivery),
Superpowers Backplane (GitHub-backed backlog and handoff continuity), and
GovZero skills (portable engineering disciplines).

Project-owned `AGENTS.md`, domain rules, authorization, and verification commands
remain authoritative. App operational skills belong in the project's own skill
or plugin tree; runtime rules and persistence belong in its supporting code.

Start by checking actual skill discovery. Configuration is not proof of loading.
Use the installed Superpowers entry skill for development, Backplane's backlog
skill for issue continuity, and the gz-skills router for portable disciplines.
Preserve their independent sources; do not copy or edit installed upstream trees.
Read the current Backplane compatibility/setup instructions before backlog work.
Do not infer permission to mutate GitHub Issues or publish releases from adoption.

Choose a gz-skills profile explicitly when canonical upstream setup supports it.
The starter does not create or select a profile and never imports the gzkit lifecycle. Existing project rules override generic runtime,
framework, testing, and quality-tool examples from another adopting app.

For installation, status, updates, and rollback, use the reviewed version of
https://github.com/tvproductions/skills-first-starter and its `docs/adoption.md`.
A fresh-session discovery record is required before describing this stack as
loaded. Backplane's pre-release status must remain visible.
