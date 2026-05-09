---
name: board-ai-risk-pack
description: |
  Drafts the AI risk committee pack the AI Governance Lead carries into the meeting: AI inventory state with heat map by tier, top AI risks with trajectory, recent AI incidents and near-misses, foundation-model vendor concentration, model performance trends, GenAI program status, AI governance maturity posture, and the decisions the committee owes this cycle. The pack is the firm's standing instrument for AI-specific board oversight, alongside (not inside) the enterprise risk committee pack.

  Best for:
  - Standing AI risk committee meeting (often quarterly) where the AI Governance Lead, CRO, and head of model risk need a curated view of AI posture rather than the full inventory dump.
  - The AI section of a board risk committee at firms without a standalone AI committee, when the board wants AI-specific framing rather than a heat-map row inside the enterprise pack.
  - Board education session on AI governance: tier mix, top risks, foundation-model exposure, GenAI program status, and the decisions in flight.
  - Regulator pre-meet pack for an AI-themed exam request, supervisory letter response, or NYDFS / NAIC information request; the committee pack travels as the firm's documented oversight posture.
  - Annual AI program review at an insurer aligning to the NAIC Model Bulletin AIS Program elements; same pack, deeper.

  Not the right tool when:
  - The audience is the enterprise risk committee at large (use `risk-reporting/skills/risk-committee-pack`; that pack pulls a brief from this one for the AI heat-map cell rather than re-anchoring the AI sources).
  - The artifact required is the full AI inventory list (this skill curates and summarises; it does not enumerate the catalogue).
  - The artifact required is a single use-case model card (use `model-card-builder`; this pack consumes its sign-off questions).
  - The work is a single AI vendor diligence file (use `third-party-operational-resilience/skills/vendor-diligence` in AI-vendor mode; this pack consumes its outputs as concentration evidence).
  - The work is the EU AI Act Annex IV technical documentation file (provider-side; use `ai-act-triage` to scope deltas).
argument-hint: "[committee name and meeting date, AI inventory pointer, incident log pointer, vendor exposure pointer, prior pack, or scope statement]"
---

# Board AI risk pack

The pack is what the AI risk committee (or the AI section of the board risk committee) reaches for to discharge AI oversight under the firm's AI governance framework. It is the AI Governance Lead's instrument, drafted with second-line AI risk, distributed by the committee secretary, challenged by the chair. The named sections (executive summary, inventory state, top AI risks, in-flight reviews and decisions, incidents and near-misses, regulator interactions, foundation-model and AI vendor exposure, policy and framework changes, forward look, decisions requested) are the spine the AI committee charter expects. Depth and tone flex with firm posture, regulator constellation, and audience.

This is an AI-governance artifact, not an enterprise risk artifact. The vocabulary is tier mix, AIS Program (insurance), foundation-model dependence, RAG corpus, agentic autonomy, prompt-injection signal, model risk MRA, model drift, AI governance maturity. Enterprise risk reporting (credit, market, liquidity, conduct, financial crime, operational loss) lands here only where an AI use case materially drives an enterprise-risk movement; the broader enterprise pack is somewhere else in the firm and consumes a brief from this pack for the AI cell.

The pack is a draft until the AI Governance Lead and the head of model risk attest. The skill stops at the draft.

## Ask first

Most of the spine is set by the engagement, the prior-period pack, and the AI inventory of record. A few things settle before drafting:

- Who is the audience and what is the cadence. A standalone AI risk committee pack runs quarterly and is challenge-shaped on tier-1 and tier-2 movements, GenAI program status, and decisions. A board-level AI section is condensed and decision-loaded. A regulator-attended meeting tightens the source trace and the inventory-completeness narrative. An annual program review is the deepest cut and usually carries the NAIC AIS Program self-assessment for insurers or the ISO/IEC 42001 management review for certified firms.
- What is in scope on the heat map. Tier drives the AI heat map (not enterprise risk type); the firm's AI risk-rating taxonomy decides whether tiers are 1-4, low/moderate/high/critical, or NIST RMF-aligned categorical. Use what the firm uses; do not re-tier silently.
- What did the inventory move. Period-over-period change in tier mix is the single most useful number a committee member reads. New tier-1 use cases, tier movements, retirements, and use cases newly classified as agentic land here. If the inventory is not reconciled to the system of record, the data confidence label drops and the absence is itself a sign-off question.
- What decisions does the committee owe this cycle. Decisions usually include AI policy refresh approval, GenAI pre-prod gate exceptions, foundation-model swap approvals, agentic deployment go/no-go, AI incident response posture, and resourcing requests. A pack with no decisions is a status update; surface that absence as a sign-off question rather than ship the status pack as a committee instrument.
- What is the GenAI program status. GenAI is the highest-velocity bucket and the section the committee will spend the most time on. Foundation-model vendor concentration, RAG corpus governance, agentic autonomy levels in production, prompt-injection signal trend, and the GenAI pre-prod gate throughput are the standing items.

When the scope record is supplied, the skill reads `institution.type`, `institution.primary_regulators`, `persona.role`, `sector_overlay_set`, and `cross_cutting_overlay_set` from it, plus `source_posture` for the evidence asks. Otherwise the skill works with what the practitioner names and flags the rest.

## How the pack gets built

The pack has the same spine across firms, with depth and overlay flex. The order below is roughly how a senior AI risk lead walks it; in practice sections fill out as the inventory feed, incident log, and vendor exposure data arrive.

Start with the executive summary and the decisions requested list. Five bullets at most, in AI Governance Lead voice: headline tier-mix movement, the top AI risk, a material incident or near-miss, foundation-model exposure posture, the decision pointer. The decisions list is what the chair reads first; everything else supports those decisions.

The AI inventory state section reports total in-scope use cases, count by tier, count by sector or business line, count by lifecycle stage (pre-prod, production, retirement), count by architecture flag (traditional ML, foundation-model, RAG, agentic), and period-over-period change on each axis. Tier movement is the load-bearing line: a use case moving from tier-3 to tier-1 because of expanded autonomy or expanded customer surface is the kind of movement the committee challenges. Reconciliation status against the inventory of record is reported in the data confidence label, not buried in an appendix footnote.

Top AI risks names the small number of risks driving committee attention. Each carries trajectory (improving, stable, worsening, new), owner role (not named individual), quantified exposure where one exists, key drivers, and the linked use cases or program areas. Trajectory is required and uses the four-value enum; "stable" carries with a one-line basis, not as the default for any risk no one wants to retire. New risks (a foundation-model provider's deprecation notice for the model in production; an agentic deployment that just crossed an autonomy threshold; a regulator letter that opens a new exposure) carry the `new` flag with the date the risk was logged. Top risks repeats across packs without trajectory movement is the failure mode this section is built to prevent.

In-flight reviews and decisions covers what is in front of the committee this session: pre-prod gate decisions, tier escalations, validation findings awaiting closure, GenAI exceptions, foundation-model swap approvals. Each entry has use case or program, stage (intake, tiered, validated, gated, in-prod, retired), the decision due date, and the second-line recommendation. The committee may carry items rather than decide them; the absence of a decision is recorded with the reason.

Incidents and near-misses is curated, not the catalogue. Each entry has classification (functional failure, performance breach, fairness exposure, data leakage, prompt-injection signal, foundation-model version event, RAG retrieval failure, agentic tool-misuse, vendor outage), severity (informational, low, medium, high, critical), regulator-notification status (not applicable, evaluating, notified, no notification required with rationale), customer impact, owner role, and current status. Near-misses are required as a separate sub-section; if the period had none, state that explicitly. A pack that reports incidents as resolved with no near-miss section gives the committee a false sense of security and is the standing trap.

Regulator and exam interactions covers open MRAs and MRIAs touching AI scope, supervisory letters received, exam findings on AI inventory completeness, AI governance, model documentation, fairness testing, vendor oversight, or cyber posture as it touches AI. State insurance department interactions sit here for insurers; NYDFS interactions for NY footprint; CFPB, FRB, OCC, FDIC for federal banking; SEC for advisers. Each item has regulator, type (MRA, MRIA, letter, exam finding, information request), status, owner role, and target close date. The supervisory expectation for federally regulated banks is that the committee manages, not just counts, the open population; over-age items get the slippage commentary.

Foundation-model and AI vendor exposure is the section a committee will increasingly spend time on. Top vendors named with use-case count, foundation-model concentration (vendor and named model with use-case count) including the top-three concentration ratio, key dependencies (foundation-model providers, evaluation vendors, RAG infrastructure, agent platforms), version-change posture (pinned, floating, rolling-with-notice) by vendor, and a watch list of vendors under elevated concern (deprecation notice, security incident, regulatory action, quality drift). Concentration risk that is not surfaced explicitly is the standing trap; the committee does not see that 80% of GenAI use cases depend on one foundation-model provider until something happens.

Model performance trends covers in-production tier-1 and tier-2 performance and monitoring, with red breaches called out by use case, owner role, and status. Drift signals across the population, fairness-metric drift on customer-facing use cases, and refusal-rate or faithfulness drift on GenAI use cases sit here. Use case-level depth lives in the model cards; the pack carries the population view and the called-out breaches.

GenAI program status is its own section because of velocity and committee attention. Pipeline (intake count, in pre-prod gate, in production, retired this period), pre-prod gate throughput (decisions made, exceptions granted with rationale, items returned), foundation-model vendor inventory, RAG corpora under governance, agentic deployments by autonomy level, and the GenAI-specific incident posture (prompt-injection signal, retrieval-source audit findings, agentic tool-boundary events). The framing references (NIST GenAI Profile, ISO/IEC 42001 management-review evidence for certified firms) live in `references/source-anchors.md`.

AI governance maturity posture is the once-a-year deeper section and the standing one-paragraph summary in quarterly cycles. The frame depends on which the firm uses for AI governance: NIST AI RMF Govern function alignment for NIST-anchored firms, NAIC AIS Program elements self-assessment for insurers, ISO/IEC 42001 management review for firms pursuing certification, EU AI Act risk-management-system posture for EU-deployer exposure. The maturity narrative sits in the body; the structured evidence sits in the appendix.

Policy and framework changes since last meeting carries effective dates and owner roles. AI policy refresh, GenAI standard, agentic-AI controls update, AI incident response runbook, vendor evaluation criteria revision, intake form change. The committee's standing question is whether anything material changed under the framework without committee visibility; this section is the answer.

Forward look is named, dated, and regulator-anchored. Two cycles ahead is the standard horizon. Items that belong here: regulator developments expected (NIST AI 600-1 update, NYDFS Part 500 amendment, NAIC adoption tracker movement, EU AI Act phasing dates approaching, OCC bulletin refresh), use cases on the runway for tier escalation or pre-prod gate, GenAI deployments on the runway for production, foundation-model vendor changes expected, validation cycles due, training and capability program milestones. "Continuing to monitor the landscape" fails the section; named items only.

Decisions requested in full detail close the body: background, options considered, recommended motion with rationale, dissents from named roles where any, requested vote or acknowledgement, and owner role. "Note the report" is not a decision; if nothing requires committee action, surface that explicitly so the chair can decide whether to call the meeting.

The appendices carry the data confidence label (with the BCBS 239 posture for firms aggregating AI inventory data through enterprise data infrastructure), the source trace for every material claim, the AI inventory completeness statement, and the sign-off block. The reviewer questions for the secretary to surface in the meeting are the last item; tag them to specific sections (the tier-mix movement, the foundation-model concentration, the over-age MRA, the GenAI gate exception, the agentic deployment).

### Sector and cross-cutting overlays

When the scope names a sector, load the matching `references/sector-overlays/<sector>.md`. The overlay's named fields and committee-specific framing land in the pack; treating the overlay as background reading is the failure mode the troubleshooting file calls out.

- Banking covered-bank packs carry the OCC Heightened Standards framing on board AI oversight, the joint interagency model-risk guidance for traditional models (with the explicit GenAI/agentic scope exclusion noted), BCBS 239 data-confidence framing on the AI-inventory aggregation, and the CCAR governance-reporting cadence linkage.
- Insurance packs carry the NAIC Model Bulletin AIS Program elements as the spine of the governance maturity section, ORSA cadence linkage, NYDFS January 2024 Insurance Circular Letter framing for NY life-insurance writers, Colorado SB 21-169 framing for CO writers, and the state-DOI inquiry inventory.
- Capital-markets packs (broker-dealer or investment adviser) carry the SEC Rule 206(4)-7 annual review linkage, the Marketing Rule scope statement on AI-generated client communications, surveillance and execution AI framing, and FINRA AI guidance cross-references.
- Payments-fintech packs carry sponsor-bank governance reporting alignment, BaaS partner AI exposure, and program-management committee linkage.

Cross-cutting overlays load on the same pattern. Cyber covers the NYDFS October 2024 Industry Letter framing on AI-related cyber risk, AI-enabled threats (deepfake, social engineering), and prompt-injection exposure as a 23 NYCRR Part 500 covered-entity matter. Conduct covers customer-facing AI exposure, complaint trend by AI-touched product, fairness call-outs on consumer-credit and life-insurance underwriting decisioning, and CFPB Circular 2022-03 / 2023-03 adverse action posture for credit. Privacy lands in the cyber overlay where it touches; climate is not applicable to this pack.

Load only the overlays the scope names. Gold-plating with overlays the engagement does not implicate adds noise without challenge value.

## Quality bar

The pack is only credible when these hold:

- Every material claim cites a source. Unsupported items carry `[evidence needed]` and route to the engagement issue log, not silently into the pack.
- Evidence is separated from inference. The source-trace appendix shows the seam.
- Top-risks trajectory is a four-value enum with a one-line basis on each entry. "Stable" without basis turns the top-risks list into wallpaper across packs.
- Near-misses are reported as a separate sub-section. Empty period is stated explicitly.
- Foundation-model and vendor concentration is named, not buried. Top-three concentration ratio is the standing line.
- Decisions requested entries have options and a recommended motion. "Note the report" is not a decision.
- Inventory-state count by tier and period-over-period change are reconciled to the inventory of record. Reconciliation status is reported in the data confidence label.
- No named institutions outside finalised public enforcement actions; examples are anonymised and public-source-derived.
- The pack is a draft until the AI Governance Lead and the head of model risk attest. The skill does not distribute, file, or post to the committee folder.

## Adaptation

Audience drives tone (committee chair is challenge-shaped; board-level AI section is condensed and decision-loaded; regulator-attended meeting tightens the source trace; annual program review goes deepest on maturity). Depth flexes with firm posture (Heightened Standards bank deeper on governance section; insurer deeper on AIS Program elements; adviser deeper on Rule 206(4)-7 linkage). Sector and cross-cutting overlays load from the scope. Where firm-specific policy, taxonomy, named owners, or threshold values apply, they live in `references/firm-overlay.md` (consumed when present) and never in the pack directly.

## Output

Default to drafting the pack against `templates/default-output.md`. Render as PowerPoint for the committee meeting (the standard distribution format for a committee pre-read), or Word where the audience expects a memo, or another format the audience asks for. Produce the structured record at `schemas/board-ai-risk-pack.schema.json` when downstream consumers (the enterprise risk committee pack, the regulator response file, the firm's committee-minutes system) need it. The reviewer attestation block is filled by the AI Governance Lead and the head of model risk; the pack is distributed only after.

Downstream consumers: the structured object feeds the firm's committee minutes system and the regulator response file when supervisors ask for the pack as part of an AI-themed examination or supervisory letter response. The enterprise risk committee pack (`risk-reporting/skills/risk-committee-pack`) consumes a brief for the AI heat-map cell and any AI-driven top-risks entry rather than re-anchoring the AI sources. `model-card-builder` outputs feed the in-flight reviews and the model performance trends sections. `ai-risk-tiering` outputs feed the inventory-state counts. `agentic-ai-controls` outputs feed the GenAI program status and the agentic deployments line. Vendor exposure consumes outputs from `third-party-operational-resilience/skills/vendor-diligence` in AI-vendor mode. The schema is the cross-skill contract; additive changes only, never silent renames. Breaking changes ship as a versioned migration with the consumers told in advance.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays/{banking,insurance,capital-markets,payments-fintech}.md` — sector overlays loaded from scope.
- `references/cross-cutting/{cyber,conduct}.md` — cross-cutting overlays loaded from scope.
- `references/firm-overlay.md` — firm-installed AI policy, taxonomy, named owners, threshold values (consumed when present).
- `templates/default-output.md` — pack template with the named sections.
- `schemas/board-ai-risk-pack.schema.json` — structured-output contract.
- `examples/` — anonymised public-source-derived scenarios.
- `TROUBLESHOOTING.md` — recurring defects.
