# Skills-first starter

This repository owns the bundle catalog, adoption helper, native marketplace
adapters, and guidance. Read README.md and docs/architecture.md before changes.
This is a public scaffold; use invented fixtures and preserve upstream ownership.

SP, SP-BP, and gz-skills are independent components. FDAU is the primary design
precedent. Do not vendor their skills, introduce a gzkit lifecycle, or infer app
rules and runtimes from another adopting project. App operational skills and
supporting domain code remain project-owned.

Validate pins and both catalogs after a bundle change. Use unittest, not pytest.
Test consequential adoption behavior at the public helper seam. Preserve existing
project files, explicit profile choices, and native manager state. A config file
or successful manifest validation cannot prove fresh-session skill discovery.
Report unverified host behavior and Backplane pre-release limitations explicitly.

Checks: `python3 -m unittest discover -s tests -v`, `python3 starter.py validate`,
`uvx ruff check .`, and `uvx ruff format --check .`.
No plugin installation, GitHub issue mutation, tag, or release publication is
implied by editing this repository. Follow the user's actual authorization.
