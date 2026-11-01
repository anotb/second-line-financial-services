# AI Governance and Model Risk

Second-line workflows for AI and model risk management. Eleven skills covering the AI artifact set a model risk lead, AI governance lead, validation team, or AI risk committee secretary actually produces: intake, risk tiering, EU AI Act triage, model cards, validation planning, agentic-AI controls, board pack, and a four-skill GenAI deep-dive.

Flagship plugin in this repo. Carries the heaviest source-anchor depth. The bank model-risk anchor is the joint interagency Revised Guidance on Model Risk Management (OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17 2026; supersedes SR 11-7 and SR 21-8) for traditional statistical and quantitative models; the bulletin expressly excludes generative AI and agentic AI from its scope (footnote 3). For GenAI and agentic use cases the substantive anchors are NIST AI RMF 1.0, NIST AI 600-1 (Generative AI Profile), ISO/IEC 42001:2023, EU AI Act, OWASP Top 10 for LLM Applications, MITRE ATLAS, NCSC/CISA secure-AI guidelines, NYDFS October 2024 letter on AI cyber, and the NAIC AI Bulletin for insurers.

## GenAI expansion

Four new skills make this the most regulator-active part of the repo for 2025-26 supervisory activity:

- `prompt-injection-risk` — second-line review of the prompt-injection threat surface for a GenAI deployment. Carriers, tested attack classes, mitigations, residual, monitoring. Substantive anchors: NIST AI 600-1, OWASP Top 10 for LLM Applications, MITRE ATLAS, NCSC/CISA secure-AI guidance, NYDFS October 2024 letter, SEC cyber-disclosure rules, the 36-hour banking computer-security incident notification rule. The bank model-risk bulletin (OCC 2026-13 et al.) excludes generative AI from scope.
- `rag-evaluation-review` — second-line review of retrieval and grounding evaluation for RAG. Corpus fitness, retrieval quality, grounding metrics (faithfulness, citation precision, refusal), failure modes, monitoring. Substantive anchors: NIST AI 600-1 Measure 2.9 and Measure 1.1, ISO/IEC 42001 §8.1 / §9.1, EU AI Act Article 10 where applicable. The bank model-risk bulletin (OCC 2026-13 et al.) excludes generative AI from scope.
- `genai-pre-prod-review` — pre-production gate review for a GenAI use case. Roll-up of upstream artifacts, conditions, residual risk, monitoring readiness, sign-off block. Substantive anchors: NIST AI RMF, NIST AI 600-1, ISO/IEC 42001, EU AI Act Articles 9, 13, 14, 26 where applicable. The bank model-risk bulletin (OCC 2026-13 et al.) excludes generative AI from scope.
- `llm-vendor-evidence-review` — review of foundation-model vendor evidence packs (system cards, model cards, evaluation reports, red-team results, responsible-use policies) against firm criteria. Sufficiency view, gaps, residual reliance. Substantive anchors: NIST AI 600-1 Govern 6.x and Manage 3.x, ISO/IEC 42001:2023 §7.4 / §8.x, the joint interagency third-party guidance (June 2023), EU AI Act Articles 51 to 55 for GPAI where applicable. Public system cards from frontier labs (Anthropic, OpenAI, Google) referenced as the form-factor pattern under review.

## Skill inventory

Foundational AI governance:

- `ai-use-case-intake` — structured intake record (purpose, users, data, vendors, autonomy, decision impact, review gates).
- `ai-risk-tiering` — multi-factor tier rubric (tier 1 to 4), with triggered gates and validation depth.
- `ai-act-triage` — EU AI Act classification (prohibited / high-risk / limited / minimal / GPAI), operator role, obligations.

Model risk artifacts:

- `model-card-builder` — model card with intended use, data, performance, limitations, monitoring, controls, sign-off questions.
- `validation-plan` — validation scope (conceptual soundness, outcomes analysis, ongoing monitoring) sized to tier.
- `agentic-ai-controls` — controls for agentic systems (scope, authority, tool inventory, oversight, kill switch, residual risk).

Committee artifact:

- `board-ai-risk-pack` — AI risk committee pre-read (inventory, top risks, in-flight reviews, incidents, decisions).

GenAI deep-dive:

- `prompt-injection-risk`
- `rag-evaluation-review`
- `genai-pre-prod-review`
- `llm-vendor-evidence-review`

## Components

- `skills/` — user-invocable and model-invocable Claude Code skills. This repo does not use legacy `commands/` for new plugins because current Claude Code skills create slash invocations and support supporting files.
- `references/` — public-source map, policy and control library, and review gates copied into this plugin so it is self-contained after installation.
- `schemas/` — JSON schemas for AI use cases, controls, issues, obligations, vendors, test plans, and risk-report items.

## Operating posture

The plugin drafts second-line work product for qualified review. It does not approve, file, rate, onboard, decline, notify, or close items. Every artifact stops at "recommended decision" or "open conditions"; sign-off remains with named human reviewers.

## Sector overlays

Sector flavor lives inside the relevant skill rather than in separate sector plugins. Two specifically called out:

- `ai-act-triage` carries banking, insurance, capital-markets, and payments-fintech overlays. The earlier `insurance-ai-act-triage` is absorbed here.
- `agentic-ai-controls` carries the insurance overlay for claims-handling agentic AI. The earlier `claims-ai-controls` is absorbed here.

## Cross-cutting overlays

Cyber, privacy, and conduct land as embedded reference content inside the skills they touch (most skills here pick up cyber and privacy; conduct lands where customer impact is in scope). NYDFS October 2024 letter on AI cyber is the primary cross-cutting cyber anchor for this plugin.

## Companion to anthropics/financial-services

This is an independent second-line companion project, not affiliated with or endorsed by Anthropic. The Anthropic financial-services repo handles first-line workflows (analysis, banking, equity research, PE). This plugin sits over those workflows when an AI or model component is in scope and second-line review is needed.
