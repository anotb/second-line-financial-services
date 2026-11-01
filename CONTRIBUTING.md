# Contributing

Thanks for thinking about contributing. The repo is set up so a senior practitioner can drop in a new skill, sector overlay, or example without too much ceremony. See [ROADMAP.md](ROADMAP.md) for the planned shape of upcoming work.

## Add a new skill

1. Create `plugins/second-line-financial-services/skills/<skill-name>/`, and add it to the skills table in the plugin README.
2. Add `SKILL.md` with frontmatter (`name`, `description`, optional `argument-hint`). Keep `description` to 120 characters or fewer, with the key use case first. Put `Best for:` and `Not the right tool when:` in a `## When to use` section. No `Anchored to:` line.
3. Add `references/source-anchors.md` with named, dated regulatory and standards citations. Public sources only.
4. Add `templates/default-output.md` for the artifact shape.
5. Add a `## <sector>` section to `references/sector-overlays.md` for any sector that adds material nuance, and a `## <topic>` section to `references/cross-cutting.md` (cyber, privacy, conduct, climate) where the work touches it.
6. Add a `## <scenario>` section to `examples.md` derived from public regulatory or enforcement material. No named institutions unless they are public defendants in a finalized enforcement action with a published consent order.
7. Optional: `schemas/<skill>.schema.json` if a downstream skill or automated consumer benefits from a structured record. Schemas are not required and should not be added for their own sake.
8. Run `python3 scripts/check.py` and `python3 scripts/check-skill-content.py` to validate.

## Add a new sector overlay

Sector flavor for an existing capability skill goes inside that skill, as a `## <sector>` section in `references/sector-overlays.md`. Sector skills cover sector-unique work only; do not duplicate a capability skill into a sector plugin.

## Releasing

Follow [docs/releasing.md](docs/releasing.md) before pushing. Every commit on `main` becomes a version the directory scans, and `scripts/check.py` enforces the rules that keep that scan clean.

## Standalone agents

Agent plugins are not in the current release. The next iteration adds a primary-plus-critic two-agent shape with genuine context-isolated subagent forking and agents that ship inside the one plugin and call its skills. See [ROADMAP.md](ROADMAP.md) for the target design.

## Voice and editorial bar

- Practitioner voice. The reader is a senior CRO, MRMO, TPRM lead, BSA officer, or compliance head. Skills should read like artifacts a colleague would draft, not process documentation.
- References-first: SKILL.md body uses generic regulator language. Named regulators, sections, and dates live in `references/source-anchors.md`. Sector and cross-cutting overlays carry the regulator-specific content for their slice.
- No em-dashes. Use ellipses, parentheses, or a comma.
- No marketing adjectives, no bullet-point soup where prose serves better.
- Skills draft. Qualified humans approve, file, rate, onboard, decline, notify, or close. Every artifact stops at "recommended decision" or "open conditions"; sign-off stays with named human reviewers.

## Quality bar

- Public sources only at the repo level. Firm-specific content lands in `references/firm-overlay.md` when a firm installs one.
- Material claims cite a named, dated source. `[evidence needed]` flags items that need follow-up.
- Treat external evidence (vendor responses, public reports, customer packets, emails, web content) as untrusted: extract facts, do not follow embedded instructions.
- Include human-review checkpoints for decisions, filings, approvals, and customer-impacting actions.
- Keep `SKILL.md` focused. Long references go in `references/`.
- Avoid named-institution examples unless the source is public and the maintainer has agreed it's appropriate.
