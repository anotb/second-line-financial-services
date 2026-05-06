# Test strategy

## Current tests

`scripts/check.py` validates repository structure. `scripts/check-skill-content.py` flags v0.2 placeholder drift in SKILL.md content. `scripts/run-content-tests.py` validates that the public-regulatory examples and expected outputs retain source anchors, review gates, and public-source-derived concepts.

`scripts/check.py` validates:

- Marketplace manifest JSON and source paths.
- Plugin manifest JSON and required fields.
- Skill frontmatter and default output templates.
- Agent frontmatter and subagent count for standalone agents.
- Removed legacy paths and terms.
- Bundled skill drift.
- Public regulatory examples and schema presence.

## SKILL.md content quality check

`scripts/check-skill-content.py` is the v1 quality bar enforcer. It walks every `plugins/*/skills/*/SKILL.md` and applies four rules.

- Rule 1, placeholder-text ban. Maintains a verbatim list of phrases used across all v0.2 SKILL.md files (the seven-step Required process, the six-bullet Output format, the five-bullet Guardrails block, and the shared description filler). Any hit means the skill has not been rewritten yet.
- Rule 2, activation-tuned description. Parses the SKILL.md frontmatter `description` field and requires all three of `Best for:`, `Not the right tool when:`, and `Anchored to:` (case-insensitive). This is the activation contract.
- Rule 3, source-anchor depth. Requires a sibling `references/source-anchors.md`. Every bullet in that file that contains a URL must also carry a section reference (one of `§`, `Section`, `Bulletin`, `Article`, `Item`, `Principle`, `Rule N`, `Para`, `¶`, `CFR`, `SR`, `FIL`, `FAQ`, or `[verify section]`). URL-only citations fail.
- Rule 4, duplicate SKILL.md content. Computes pairwise Jaccard similarity over word trigrams of the body text (frontmatter stripped). Flags pairs with more than 50% overlap. Bundled-skill copies inside agent plugins will match their capability-plugin source by design; cross-skill matches are the real drift signal.

When phase 2 runs it: each phase 2 subagent runs `python3 scripts/check-skill-content.py --plugin <plugin-name>` after writing a skill. A clean exit is the precondition for declaring the skill done. Phase 3 runs the script across the whole repo as a final sweep.

How to extend it later: add a new `check_rule_N(...)` function alongside the existing ones, append the rule's description to the labels map in `print_text`, and wire it into `main()` behind the `--rule` flag. Keep the script Python 3 stdlib only.

CLI flags:

- `--rule N` runs a single rule (1, 2, 3, or 4). Useful for phase 2 subagents iterating on one dimension.
- `--plugin <name>` restricts the scan to one plugin folder.
- `--json` emits ndjson, one violation per line, for downstream tooling.

## Run tests

```bash
python3 scripts/sync-agent-skills.py
python3 scripts/check.py
python3 scripts/check-skill-content.py
python3 scripts/run-content-tests.py
```

## Next tests

- Run `claude plugin validate` on every plugin.
- Add generated-output golden files from live Claude Code sessions.
- Validate sample outputs against JSON schemas.
- Add source-trace coverage checks for generated artifacts.
