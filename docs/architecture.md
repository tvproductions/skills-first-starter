# Architecture and ownership

One bundle catalog composes three independently maintained plugins. Its two
native marketplace adapters refer to immutable upstream revisions; they do not
contain authored copies of those skill trees.

```text
Project AGENTS and domain authorities
  -> SP (feature work) + SP-BP (backlog/handoff) + gz-skills (engineering)
  -> project-owned operational skills
  -> project-owned deterministic code and adapters
  -> versioned operational records and generated products
```

The adoption helper is standard-library Python. It previews before writing,
checks all intended files before changing any, preserves unrelated TOML bytes
and existing AGENTS content, refuses conflicting managed files and discovery
copies, and never invokes a native install, remote model, or GitHub mutation.
Existing projects retain their app layout. Empty projects get the same minimal
configuration and entrypoint, rather than a speculative web or database stack.

`bundle.json` is desired composition. `.skills-first/bundle.lock.json` in an
adopter records selected sources. Neither is a runtime readiness receipt. Actual
loaded skills, native scope, trust, and conformance require a fresh host session.

FDAU supplies the primary precedent: portable disciplines, separate upstream
Superpowers, project adapters, domain rules, and independently inspectable
verification. Its older checkout/discovery surfaces are evidence, not instructions
to copy them over the native plugin installation contract.

Backplane's current skills companion and the proposed broader Python backplane
are different maturity targets. This starter supports the existing pinned package
without pretending the proposed requirements/traceability/release system has
shipped. gzkit remains a separate ecosystem; its ledger and lifecycle are not
imported here.

Project-specific constraints stay behind project seams. Public catalog and
starter changes must not carry real operational records, credentials, machine
paths, or sensitive source data. Examples and tests use invented fixtures only.
