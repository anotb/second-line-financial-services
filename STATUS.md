# Status

Last updated: 2026-05-09, post agentic eval + fix bundle (capability skill fixes, AI-ethics overlay, DORA privacy overlay, agent-plugin deferral).

## Build state

68 source skills across 8 capability plugins and 4 sector overlay plugins ship in v1. The 6 standalone agent plugins are deferred to v1.x (held under `internal/agent-plugins-deferred/`).

| Stage | Status |
|---|---|
| v1 plugin map locked | done |
| 68 source skills built | done (batch 2D-2 closed the build queue) |
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
| Pre-launch agentic eval (8-case maker / checker run) | done (`internal/eval-2026-05-09/synthesis/findings.md`) |
| AI-ethics cross-cutting overlay (5 of 11 AI / model-risk skills) | done (this cycle) |
| DORA privacy cross-cutting overlay | done (this cycle) |
| Capability skill fixes from eval (scoping enum, sample-roll-up template, fair-lending template thicken, DORA capital-markets overlay enrichment, conduct B2B trigger) | done (this cycle) |
| Agent plugins (6) | deferred to v1.x; held under `internal/agent-plugins-deferred/` |
| Live `claude plugin validate` from this environment | not run |
| `dora-register-builder` full schema rebuild against EU 2024/2956 | deferred to v1.1 |
| Modular install Stage 1 (README paths) + Stage 2 (manifest deps) | deferred to v1.1 |
| Schema dedup quick-win (replaces Phase 3 schema relocation) | deferred to v1.1 |
| AI-ethics overlay rollout to remaining 6 AI / model-risk skills | deferred to v1.1 |
| Conduct overlay B2B-flow-through trigger rollout to other 8 conduct overlays | deferred to v1.1 |
| `bsa-aml-ra-methodology` skill (new) | deferred to v1.1 |

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
- 8 capability plugins + 4 sector overlay plugins ship in v1; 6 standalone agent plugins deferred to v1.x (see ROADMAP).
- Strict sector overlay rule: sector plugins ship sector-unique skills only; sector flavor on capability skills lives as a `references/sector-overlays/<sector>.md` reference inside the capability skill.
- Scoping primitive in `risk-compliance-core` produces a structured scope record every other skill consumes.
- References-first SKILL.md design: SKILL.md body uses generic regulator language; named regulators, sections, and dates live in `references/source-anchors.md`; sector and cross-cutting overlays load conditionally from the scope.
- Description shape: summary + `Best for:` + `Not the right tool when:`. No `Anchored to:` line.
- Workflow narrative bakes invariants and adaptation guidance inline. No "What's load-bearing and what flexes" meta-section.
- Schemas optional, only when the artifact has a structure that genuinely helps downstream automation. No shared `_defs.json`. No cross-skill enum forcing.
- Deliverables are practitioner-natural formats (Word, Excel, PowerPoint) rendered via Anthropic's `document-skills` plugin (`docx`, `xlsx`, `pptx`). Markdown is the content spec, not the deliverable.

## Repository organization

Public-facing root is Anthropic-shaped:

- `plugins/` — deliverables (capability + sector plugins). Agent plugins deferred to v1.x and held under `internal/agent-plugins-deferred/`.
- `docs/` — public documentation (architecture, source-map, test-strategy, conventions review, public examples).
- `scripts/` — build and validation tooling (`check.py`, `check-skill-content.py`, `sync-agent-skills.py`).
- Plus README, LICENSE (MIT), CHANGELOG, CONTRIBUTING, SECURITY, STATUS, ROADMAP, CLAUDE.md, and `.claude-plugin/marketplace.json`.

Internal research kept under `internal/` (gitignored):

- `internal/specs/` — phase 1 spec sheets per skill plus per-plugin `AUDIT.md` memos.
- `internal/reviews/` — phase 2 revision and cleanup memos.
- `internal/plans/` — rationalized plugin map and phase 2 build contract.
- `internal/templates/` — the `skill-skeleton.md` v1 SKILL.md shape.
- `internal/eval-2026-05-09/` — pre-launch agentic eval (8 cases, maker / checker pattern, synthesis findings, fix worklogs).
- `internal/agent-plugins-deferred/` — the 6 agent plugins held for v1.x revival.
- `internal/v0.2-archive/` — the v0.2 root layers preserved for reference.
- `internal/RESUME-NOTES.md` — orchestrator notes for picking the build back up.

## Limitations and open work

### Limitations

- Public-source-derived examples and references only. Not a substitute for legal review or firm policy overlays.
- Some regulatory anchors evolve quickly. Refresh `docs/source-map.md` and per-skill `references/source-anchors.md` before production use.
- Agent plugins deferred to v1.x. The deferred copies under `internal/agent-plugins-deferred/` are not part of v1 distribution; the v1.x rebuild changes the orchestration shape (primary plus critic with genuine forked subagent context isolation, plus plugin dependencies in place of bundled-skill copies). See ROADMAP.
- No production MCP connectors. Only `.mcp.example.json` placeholders.
- No firm-specific policy, risk taxonomy, issue-rating, control library, committee template, or legal interpretation. Skills consume firm overlays via `references/firm-overlay.md` when a firm installs one.
- Live `claude plugin validate` has not been run in Claude Code from this environment.

### Open work

- v1.x agent revival per ROADMAP (primary + critic shape, forked subagent context isolation, plugin dependencies, engagement-level scoping prompts, golden conversation regression tests).
- AI-ethics cross-cutting overlay rollout to the remaining 6 AI / model-risk skills.
- Conduct overlay B2B-flow-through trigger propagation to other 8 conduct overlays in `ai-governance-model-risk`.
- New `bsa-aml-ra-methodology` skill in `financial-crime-governance`.
- Per-skill quality lift: independent reviewer pass per skill, drafting edits against spec sheets.
- EU overlay expansion across sector skills.
- Final README polish and validation pass before public GitHub publish.
