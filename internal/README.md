# internal/

Research artifacts kept in the repo for future improvement of the public-facing skills under `plugins/`. Not part of the installable plugin set.

## What's here

- **`specs/`** — phase 1 spec sheets, one per skill, plus per-plugin `AUDIT.md` memos and per-sector `overlay-snippets.md`. The spec sheet is the contract a phase 2 skill build was held to. Use it to:
  - Understand why a skill is shaped the way it is (source anchors, sector overlays, cross-cutting overlays, common pitfalls).
  - Drive the next iteration of a skill (revisit the spec, refine, rebuild).
  - Onboard a contributor who needs the design rationale, not just the playbook.

- **`reviews/`** — phase 2 revision memos. Each memo compares a skill's draft against its spec sheet and proposes surgical edits. Use it to:
  - See where past iterations over-cut or under-cut substance.
  - Reproduce the review pattern when iterating again.
  - Avoid relitigating decisions already made.

- **`plans/`** — design plans, including the rationalized plugin map (the v1 design rationale) and the phase 2 build contract (the constraint set every phase-2 build was held to). Use it to:
  - Understand the v1 design decisions and the audience they were made for.
  - Apply the build contract to future phase-N waves.

## Why it stays in the repo (for now)

The research is too useful to throw away after one iteration. Spec sheets capture practitioner-grade source anchors that a future build can refresh. Reviews capture practitioner-grade critique. Plans capture the why.

If a future release wants the public surface even cleaner, this directory can be moved to a separate private repo without affecting the installable plugin set.
