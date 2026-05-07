# Status

Last updated: 2026-05-06, end of batch 2D-1, batch 2D-2 in flight. Detailed orchestrator notes at `internal/RESUME-NOTES.md`.

## Phase 2 build state

- **Skills built clean** (against four content quality rules): ~57 of 68
- **In flight**: batch 2D-2, 11 sector skills (banking 3, capital-markets 4, insurance 2, payments-fintech 2). When 2D-2 lands, the build queue is closed.
- **Quality progression** across batches:

| Metric | Pre wave-1 | Post wave-1 | Post 2A | Post 2B | Post 2C | Post 2D-1 | Cumulative |
|---|---:|---:|---:|---:|---:|---:|---:|
| Rule 1 (placeholder text) | 2,691 | 1,978 | 1,472 | 1,104 | 644 | **253** | -91% |
| Rule 2 (description shape) | 117 | 86 | 64 | 48 | 28 | **11** | -91% |
| Rule 3 (source-anchor depth) | 117 | 88 | 65 | 48 | 28 | **11** | -91% |
| Rule 4 (duplicate-content pairs) | 6,786 | 3,685 | 2,057 | 1,175 | 435 | **118** | -98% |

## v1 design locked

- Companion repo to `anthropics/financial-services` (second-line layer over their first-line workflows).
- US-deep, EU as overlays, UK as see-also.
- 8 capability plugins + 4 sector overlay plugins + 6 standalone agent plugins.
- Strict sector overlay rule: sector plugins ship sector-unique skills only; sector flavor on capability skills lives as a `references/sector-overlays/<sector>.md` reference inside the capability skill.
- Engagement-scoping primitive in `risk-compliance-core` produces a structured engagement-scope record every other skill consumes.
- References-first design: SKILL.md body uses generic regulator language; specific regulator names and section refs live only in `references/source-anchors.md`; sector and cross-cutting nuance load conditionally based on the engagement scope.
- Description shape: summary + `Best for:` + `Not the right tool when:`. No `Anchored to:` line.
- Workflow narrative bakes non-negotiables and adaptation guidance inline. No "What's load-bearing and what flexes" meta-section.
- Schemas optional, only when the artifact has a structure that genuinely helps downstream automation. No shared `_defs.json`. No cross-skill enum forcing.
- Deliverables are practitioner-natural formats (Word, Excel, PowerPoint) rendered via Anthropic's `document-skills` plugin (`docx`, `xlsx`, `pptx`). Markdown is the content spec, not the deliverable.
- Agent plugins keep their primary `agent.md` plus reader / critic / writer subagent pattern.

## Repository organization

Public-facing root is now Anthropic-shaped:

- `plugins/` — deliverables (capability + sector + agent plugins).
- `docs/` — public-facing documentation (architecture, source-map, test-strategy, conventions review, public examples).
- `scripts/` — build and validation tooling (`sync-agent-skills.py`, `check.py`, `check-skill-content.py`).
- Plus README, LICENSE, CHANGELOG, CONTRIBUTING, SECURITY, STATUS, ROADMAP, CLAUDE.md, and `.claude-plugin/marketplace.json`.

Internal research kept under `internal/`:

- `internal/specs/` — phase 1 spec sheets per skill plus per-plugin `AUDIT.md` memos.
- `internal/reviews/` — phase 2 revision and cleanup memos.
- `internal/plans/` — rationalized plugin map and phase 2 build contract.
- `internal/templates/` — the `skill-skeleton.md` v1 SKILL.md shape.
- `internal/v0.2-archive/` — the v0.2 root layers (common, examples, tests, run-content-tests.py) preserved for reference.
- `internal/RESUME-NOTES.md` — orchestrator notes for picking the build back up.

## Known limitations and open work

### Limitations

- Public-source-derived examples and references only. Not a substitute for legal review or firm policy overlays.
- Some regulatory obligations evolve quickly. Refresh `docs/source-map.md` and per-skill `references/source-anchors.md` before production use.
- Agent subagents are Claude Code subagents (Markdown files in `agents/`), not Managed Agent API callable-agent YAML manifests. v1.1 may add a `managed-agent-cookbooks/` subtree for upstream PR candidates.
- No production MCP connectors. Only `.mcp.example.json` placeholders.
- No firm-specific policy, risk taxonomy, issue-rating, control library, committee template, or legal interpretation. Skills consume firm overlays via `references/firm-overlay.md` when a firm installs one.
- Live `claude plugin validate` has not been run in Claude Code from this environment.

### Retroactive cleanup queued (not blocking)

The sharpened v1 rules were tightened multiple times during the build. Older skills carry tells from earlier rule iterations.

- Strip `Anchored to:` from description across ~49 built SKILL.md files (mechanical fix).
- Drop "What's load-bearing and what flexes" sections from older built skills; fold inline into workflow narrative.
- Convert markdown deliverables to Word / Excel / PowerPoint via `document-skills` rendering across older built skills.
- Strip rigid schema enums to descriptive strings.
- Audit `examples/` folders; cut where the artifact is mechanical and the template tells the reader everything.

### Forward work

- v1.1 cookbook layer for upstream PR candidates (`ai-governance-reviewer`, `regulatory-change-analyst`).
- Per-skill quality lift: independent reviewer pass per skill, drafting edits against spec sheets.
- EU overlays expansion across sector skills.
- Final README polish before public GitHub publish.
