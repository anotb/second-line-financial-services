# Status

Last updated: 2026-05-09, post Phase 5 audit + currency sweep + sector-flagship gap fills.

## Build state

68 source skills across 8 capability plugins and 4 sector overlay plugins, plus 6 standalone agent plugins that bundle subsets of those skills.

| Stage | Status |
|---|---|
| v1 plugin map locked | done |
| 68 source skills built | done (batch 2D-2 closed the build queue) |
| Sync to agent-plugin bundles | done |
| Phase 1 cross-cutting cleanup (6 sweeps) | done (commit 22dc202) |
| Phase 2 editorial review (B1-B6) | done (commit 5fd4cf6) |
| `engagement-scoping` to `scoping` rename | done (commit aa4500c) |
| License switch to MIT | done (commit aa4500c) |
| Phase 5 audit + fix-applier | done (commit deae432) |
| `dora-register-builder` light relabel | done (commit d11e3b5) |
| Cross-cutting overlay obvious wins (B7) | done (commit d11e3b5) |
| TROUBLESHOOTING + examples relevance audit (B9) | done (commit d11e3b5) |
| CFPB / BNPL / FDIC / SAR-FAQ / FinCEN / NIST / SEC currency sweep | done (commit 12e8020) |
| Sector-flagship skill build candidates (B10a-c) | done |
| Pack-schema field canonicalisation + small-items bundle (B11) | done |
| Modular install analysis | done (deferred to v1.1) |
| Live `claude plugin validate` from this environment | not run |
| `dora-register-builder` full schema rebuild against EU 2024/2956 | deferred to v1.1 |
| Modular install Stage 1 (README paths) + Stage 2 (manifest deps) | deferred to v1.1 |
| Schema dedup quick-win (replaces Phase 3 schema relocation) | deferred to v1.1 |

## Quality progression across batches

| Metric | Pre wave-1 | Post wave-1 | Post 2A | Post 2B | Post 2C | Post 2D-1 |
|---|---:|---:|---:|---:|---:|---:|
| Rule 1 (placeholder text) | 2,691 | 1,978 | 1,472 | 1,104 | 644 | 253 |
| Rule 2 (description shape) | 117 | 86 | 64 | 48 | 28 | 11 |
| Rule 3 (source-anchor depth) | 117 | 88 | 65 | 48 | 28 | 11 |
| Rule 4 (duplicate-content pairs) | 6,786 | 3,685 | 2,057 | 1,175 | 435 | 118 |

Batch 2D-2 closed the build queue; Phase 1 and Phase 2 layered cross-cutting cleanup and editorial review over that base.

## v1 design (locked)

- Companion repo to `anthropics/financial-services` (second-line layer over their first-line workflows).
- US-deep, EU as overlay, UK as see-also.
- 8 capability plugins + 4 sector overlay plugins + 6 standalone agent plugins.
- Strict sector overlay rule: sector plugins ship sector-unique skills only; sector flavor on capability skills lives as a `references/sector-overlays/<sector>.md` reference inside the capability skill.
- Scoping primitive in `risk-compliance-core` produces a structured scope record every other skill consumes.
- References-first SKILL.md design: SKILL.md body uses generic regulator language; named regulators, sections, and dates live in `references/source-anchors.md`; sector and cross-cutting overlays load conditionally from the scope.
- Description shape: summary + `Best for:` + `Not the right tool when:`. No `Anchored to:` line.
- Workflow narrative bakes invariants and adaptation guidance inline. No "What's load-bearing and what flexes" meta-section.
- Schemas optional, only when the artifact has a structure that genuinely helps downstream automation. No shared `_defs.json`. No cross-skill enum forcing.
- Deliverables are practitioner-natural formats (Word, Excel, PowerPoint) rendered via Anthropic's `document-skills` plugin (`docx`, `xlsx`, `pptx`). Markdown is the content spec, not the deliverable.
- Agent plugins keep their primary `agent.md` plus reader / critic / writer subagent pattern.

## Repository organization

Public-facing root is Anthropic-shaped:

- `plugins/` — deliverables (capability + sector + agent plugins).
- `docs/` — public documentation (architecture, source-map, test-strategy, conventions review, public examples).
- `scripts/` — build and validation tooling (`sync-agent-skills.py`, `check.py`, `check-skill-content.py`).
- Plus README, LICENSE (MIT), CHANGELOG, CONTRIBUTING, SECURITY, STATUS, ROADMAP, CLAUDE.md, and `.claude-plugin/marketplace.json`.

Internal research kept under `internal/`:

- `internal/specs/` — phase 1 spec sheets per skill plus per-plugin `AUDIT.md` memos.
- `internal/reviews/` — phase 2 revision and cleanup memos.
- `internal/plans/` — rationalized plugin map and phase 2 build contract.
- `internal/templates/` — the `skill-skeleton.md` v1 SKILL.md shape.
- `internal/v0.2-archive/` — the v0.2 root layers preserved for reference.
- `internal/RESUME-NOTES.md` — orchestrator notes for picking the build back up.

## Limitations and open work

### Limitations

- Public-source-derived examples and references only. Not a substitute for legal review or firm policy overlays.
- Some regulatory anchors evolve quickly. Refresh `docs/source-map.md` and per-skill `references/source-anchors.md` before production use.
- Agent subagents are Claude Code subagents (Markdown files in `agents/`), not Managed Agent API callable-agent YAML manifests. v1.1 may add a `managed-agent-cookbooks/` subtree for upstream PR candidates.
- No production MCP connectors. Only `.mcp.example.json` placeholders.
- No firm-specific policy, risk taxonomy, issue-rating, control library, committee template, or legal interpretation. Skills consume firm overlays via `references/firm-overlay.md` when a firm installs one.
- Live `claude plugin validate` has not been run in Claude Code from this environment.

### Open work

- `dora-register-builder` relabel (operational-resilience plugin).
- Phase 5 audit findings, currently open in `internal/reviews/`.
- Phase 3 schema relocation: schemas borrowed across plugins for v1 move to their owning plugins.
- Per-skill quality lift: independent reviewer pass per skill, drafting edits against spec sheets.
- EU overlay expansion across sector skills.
- v1.1 cookbook layer for upstream PR candidates (`ai-governance-reviewer`, `regulatory-change-analyst`).
- Final README polish and validation pass before public GitHub publish.
