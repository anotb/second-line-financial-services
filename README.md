# Second Line Financial Services

Open Claude Code plugin scaffolding for financial-services governance, risk, compliance, controls, reporting, AI governance, model risk, third-party risk, operational resilience, financial crime governance, and consumer compliance.

This repo is designed to complement Anthropic's public financial-services plugin work. Anthropic's financial-services repo packages self-contained agent plugins and source plugin bundles for workflows such as financial analysis, investment banking, equity research, private equity, wealth management, fund admin, and operations. This repo focuses on the missing second-line layer: the artifacts that make regulated deployment safer, more traceable, and easier to review.

## What changed in v0.2

- Removed all managed-agent cookbook scaffolding.
- Replaced `plugins/vertical-plugins` with `plugins/capability-plugins` and `plugins/sector-plugins`. The term vertical is overloaded. This repo uses capability bundles for horizontal GRC workflows and sector overlays for institution-specific context.
- Kept `plugins/agent-plugins` for standalone, self-contained agents.
- Added focused subagents inside every standalone agent plugin. Each agent plugin now has a primary workflow agent plus reader, critic, and writer-style subagents under `agents/`.
- Replaced demo examples with public-source-derived regulatory examples. No named institutions, no confidential client facts, no private firm policies.
- Added public-source-informed policy, risk, and control libraries, schemas, test fixtures, expected outputs, and validation scripts.
- Moved away from legacy `commands/` for new plugins. Current Claude Code skills create slash invocations and support richer metadata and supporting files.

## Repository layout

```text
.claude-plugin/marketplace.json
plugins/
  capability-plugins/       # Horizontal GRC, AI, TPRM, testing, reporting, financial crime, consumer compliance
  sector-plugins/           # Banking, insurance, capital markets and asset management, payments and fintech overlays
  agent-plugins/            # Self-contained workflow agents with bundled skills and focused subagents
docs/                       # Architecture, source map, test strategy, public examples, conventions review
scripts/                    # sync-agent-skills.py, check.py, check-skill-content.py
internal/                   # Research artifacts kept for future improvement (specs, reviews, plans, v0.2 archive)
```

Each skill is self-contained: `plugins/<type>/<plugin>/skills/<skill>/` ships its own `SKILL.md`, `references/source-anchors.md`, `references/sector-overlays/`, `references/cross-cutting/`, `templates/default-output.md`, `schemas/*.schema.json`, `examples/`, and (where useful) `TROUBLESHOOTING.md` and `scripts/`.

## Plugin catalog

### Capability plugins

| Plugin | Purpose |
|---|---|
| `risk-compliance-core` | Core obligation, control, evidence, issue, policy-gap, and human-review workflows |
| `regulatory-change-management` | Rule impact, obligation extraction, policy diffing, implementation plans, exam briefs |
| `ai-governance-model-risk` | AI intake, risk tiering, model cards, validation plans, agentic controls, EU AI Act triage, AI vendor review |
| `third-party-operational-resilience` | Vendor diligence, criticality, DORA-style registers, contracts, exit plans, resilience testing, concentration |
| `compliance-testing` | Test plans, sampling, evidence requests, workpapers, exceptions, issue write-ups, QA |
| `risk-reporting` | Risk committee packs, BCBS 239 gap assessment, KRI commentary, SEC cyber readiness, attestations |
| `financial-crime-governance` | CDD, EDD, SAR decision QA, sanctions screening QA, AML monitoring governance |
| `consumer-compliance-fair-lending` | Fair lending, adverse action, UDAAP, Section 1071 readiness, complaints, marketing claims |

### Sector overlay plugins

| Plugin | Purpose |
|---|---|
| `banking-risk-compliance` | Banking supervision, credit risk governance, deposit ops controls, bank-fintech partnerships |
| `insurance-risk-compliance` | Insurance AI triage, life and health pricing governance, claims AI controls, outsourcing |
| `capital-markets-asset-management-compliance` | Adviser exam readiness, marketing evidence, best execution, fund board reporting |
| `payments-fintech-compliance` | Payments risk, fintech partner controls, payment incidents, open-banking data controls |

### Standalone agent plugins

| Agent plugin | Subagent pattern |
|---|---|
| `ai-governance-reviewer` | evidence reader, control critic, pack writer |
| `regulatory-change-analyst` | source reader, policy mapper, challenge reviewer |
| `third-party-risk-reviewer` | document reader, resilience critic, register writer |
| `controls-testing-analyst` | population reader, testing critic, workpaper writer |
| `risk-reporting-analyst` | metric reader, reporting critic, committee writer |
| `financial-crime-governance-reviewer` | case reader, financial-crime critic, escalation writer |

## Install locally in Claude Code

```bash
claude plugin marketplace add /path/to/second-line-financial-services
claude plugin install ai-governance-model-risk@second-line-financial-services
claude plugin install ai-governance-reviewer@second-line-financial-services
```

For rapid local testing without marketplace installation, use Claude Code's plugin directory support with a plugin folder under `plugins/`.

## Development workflow

```bash
python3 scripts/sync-agent-skills.py
python3 scripts/check.py
python3 scripts/check-skill-content.py
```

`sync-agent-skills.py` copies source skills from capability and sector plugins into self-contained agent plugins. `check.py` validates plugin manifests, skill frontmatter, agent frontmatter, marketplace paths, and bundled-skill drift. `check-skill-content.py` flags v0.2 placeholder drift in SKILL.md content (placeholder phrases, missing description shape, thin source anchors, duplicate bodies); see `docs/test-strategy.md` for the four rules and CLI flags.

## Source posture

The repo uses public sources only. See `docs/source-map.md` for source anchors and `internal/specs/<plugin>/<skill>.md` for per-skill source citations. Examples are regulatory scenarios derived from public material, not named-institution case studies.

## Disclaimer

Nothing in this repository is legal, compliance, investment, tax, accounting, regulatory, audit, or supervisory advice. These plugins draft work product for qualified professional review. They do not approve AI use cases, approve vendors, make customer decisions, file regulatory reports, submit SARs, determine legal obligations, issue final ratings, or close remediation.
