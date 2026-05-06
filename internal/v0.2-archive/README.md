# v0.2 archive

Snapshot of the v0.2 root-level shared layers, archived after the per-skill content build (phase 2) made them redundant. Kept for reference.

- `common/references/` — repo-level shared reference docs (source map, policy-control library, review gates, output templates, public-regulatory scenarios). Each plugin still has its own copy under `plugins/<type>/<plugin>/references/` (synced from these originals during v0.2). Per-skill `references/source-anchors.md` files are now the operative source-of-truth.
- `common/schemas/` — base JSON schemas (obligation, control, issue, ai-use-case, vendor, test-plan, risk-report). Not currently consumed by any phase 2 skill schema; preserved here in case a future iteration wants to re-introduce shared-base schemas.
- `examples/public-regulatory/` — original 14 public-source-derived sample outputs grouped by topic. Replaced by per-skill `examples/` (62 files and growing) under each built skill.
- `tests/` — v0.2 content-test fixtures and expected outputs. Replaced by `scripts/check-skill-content.py` (per-skill content validation).
- `run-content-tests.py` — v0.2 content test harness. Replaced by `scripts/check-skill-content.py`.

These were valid v0.2 patterns when there was no per-skill content yet. After phase 2, the per-skill anatomy (matching `anthropics/financial-services`) is the active pattern. Nothing under `plugins/` references these archived files.
