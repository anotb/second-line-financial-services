# Test strategy

## Current tests

`scripts/check.py` validates repository structure. `scripts/check-skill-content.py` checks SKILL.md content quality.

`scripts/check.py` validates:

- Marketplace manifest JSON and source paths.
- Plugin manifest JSON and required fields.
- Skill frontmatter and default output templates.
- Agent frontmatter and subagent count for standalone agents.
- Removed legacy paths and terms.

## SKILL.md content quality check

`scripts/check-skill-content.py` walks every `plugins/*/skills/*/SKILL.md` and applies four rules.

- Rule 1, placeholder-text ban. Maintains a verbatim list of filler phrases (seven-step Required process, six-bullet Output format, five-bullet Guardrails block, generic description filler). Any hit means the skill has not been rewritten yet.
- Rule 2, short listing description. Requires `description` to be 120 characters or fewer, and requires `Best for:` and `Not the right tool when:` (case-insensitive) in the skill body's `When to use` section.
- Rule 3, source-anchor depth. Requires a sibling `references/source-anchors.md`. Every bullet in that file that contains a URL must also carry a section reference (one of `§`, `Section`, `Bulletin`, `Article`, `Item`, `Principle`, `Rule N`, `Para`, `¶`, `CFR`, `SR`, `FIL`, `FAQ`, or `[verify section]`). URL-only citations fail.
- Rule 4, duplicate SKILL.md content. Computes pairwise Jaccard similarity over word trigrams of the body text (frontmatter stripped). Flags pairs with more than 50% overlap.

Run after writing or editing a skill. A clean exit is the precondition for declaring the skill done.

How to extend it: add a new `check_rule_N(...)` function alongside the existing ones, append the rule's description to the labels map in `print_text`, and wire it into `main()` behind the `--rule` flag. Keep the script Python 3 stdlib only.

CLI flags:

- `--rule N` runs a single rule (1, 2, 3, or 4).
- `--plugin <name>` restricts the scan to one plugin folder.
- `--json` emits ndjson, one violation per line, for downstream tooling.

## Run tests

```bash
python3 scripts/check.py
python3 scripts/check-skill-content.py
```

## Next tests

- Run `claude plugin validate` on every plugin.
- Add generated-output golden files from live Claude Code sessions.
- Validate sample outputs against JSON schemas.
- Add source-trace coverage checks for generated artifacts.
