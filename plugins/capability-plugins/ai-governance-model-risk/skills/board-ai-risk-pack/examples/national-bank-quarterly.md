# Example: quarterly AI risk committee pack at a US national bank

Public-source-derived. No named institution. Framing patterns from SR 11-7, OCC Heightened Standards (12 CFR Part 30 Appendix D), the joint interagency third-party guidance (OCC Bulletin 2023-17), Reg B §1002.9 (adverse-action notification), and NYDFS October 2024 Industry Letter on AI cybersecurity. CFPB Circular 2022-03 informed earlier framing but was **withdrawn May 12, 2025; historical only**. No firm-specific facts asserted.

## Input

- Institution: US national bank, OCC-supervised, mid-size to large by asset, OCC Heightened Standards covered. Standalone AI Risk Committee chartered alongside the board risk committee.
- Engagement scope supplied: institution.type = bank holding company; primary regulators OCC, FRB, CFPB; persona = AI Governance Lead, second line, reporting to the CRO; sector overlay = banking; cross-cutting overlays = cyber, conduct; source posture = public-plus-firm-policy-plus-system-of-record-evidence.
- Period: Q3; standing quarterly AI Risk Committee meeting.
- Upstream artifacts on file: AI inventory of record (47 in-production use cases, 12 in pre-prod gate, four retired in period); model performance feed for tier-1 and tier-2; AI incident log; vendor exposure data from `vendor-diligence` AI-vendor mode runs; open MRA on AI inventory completeness from the most recent OCC continuous-monitoring letter; AI policy refresh draft from the AI governance working group.
- AI Governance Lead has flagged: foundation-model concentration on a single provider crossed firm threshold; one tier-1 incident (vendor LLM version swap caused refusal-rate spike on relationship-manager assistant; resolved, no customer impact, near-miss logged); two newly tier-1 consumer-decisioning models in flight at pre-prod gate; AI policy refresh ready for committee approval.

## Output sketch

The skill emits a markdown pack and a structured record. Headlines:

- **Cover and decisions requested** — meeting date, committee = AI Risk Committee, period, classification = board-confidential. Three decisions up front: (i) approval of the revised AI policy adding GenAI-specific control expectations and agentic autonomy escalation triggers; (ii) approval of two newly tier-1 consumer-decisioning model pre-prod gate exceptions with second-line conditions; (iii) acknowledgement of the foundation-model concentration above firm threshold and direction to second-line on the diversification roadmap.
- **Executive summary** — five bullets in AI Governance Lead voice. Headline: tier-1 count up by two; one tier-1 incident on vendor LLM version swap, resolved no customer impact; foundation-model concentration crossed firm threshold; AI policy refresh ready for approval; data confidence label medium because BCBS 239 known-limitations on the AI inventory aggregation are non-empty.
- **AI inventory state** — 47 in-production, 12 in pre-prod gate, four retired; tier-1 = 9 (was 7), tier-2 = 18, tier-3 = 14, tier-4 = 6; by architecture flag traditional ML = 22, foundation-model = 14, RAG = 8, agentic = 3; tier movements named (two tier-3 to tier-1 driven by expanded consumer-facing surface; one tier-2 to tier-1 driven by autonomy escalation in the relationship-manager assistant); inventory reconciliation status = partial (three use cases pending intake reconciliation per the open OCC MRA).
- **Top AI risks** — six named risks. Foundation-model concentration trajectory = worsening (basis: top-three concentration ratio rose from 0.62 to 0.81 this period). Consumer-decisioning fairness exposure trajectory = stable (basis: latest fair-lending test pass with disparity ratios within thresholds). Agentic autonomy posture trajectory = new (logged this period, basis: relationship-manager assistant escalated from human-in-the-loop to human-on-the-loop). Vendor cyber posture trajectory = stable. AI inventory completeness trajectory = improving (basis: OCC MRA remediation on track; reconciliation gap closed from 8 to 3 use cases). BSA/AML transaction-monitoring AI performance trajectory = stable.
- **In-flight reviews and decisions** — six items: the two tier-1 consumer-decisioning use cases at pre-prod gate (decision due this meeting); a foundation-model swap approval for the customer-service assistant (vendor deprecation notice, decision due next month); a RAG corpus governance update for the policy-Q&A assistant (committee acknowledgement requested); two tier-2 validations awaiting closure.
- **Incidents and near-misses** — incidents: one tier-1 incident (vendor LLM version swap caused refusal-rate spike on relationship-manager assistant; classification = foundation-model-version-event; severity = medium; regulator notification = no-notification-required-rationale-on-file; customer impact = none; owner = head of model risk; status = remediated). Near-misses section: three logged this period (the vendor-version near-miss converted to incident; one prompt-injection signal event on the customer-service assistant detected by monitoring; one RAG retrieval-source audit finding on the policy-Q&A assistant where retrieval scope was over-broad).
- **Regulator and exam interactions** — open OCC MRA on AI inventory completeness (in-remediation, head of AI governance, target close end of next quarter); two CFPB exam findings on adverse-action notice quality for AI-driven credit decisions (in-remediation, head of consumer compliance, target close end of next month); FRB SR 11-7 horizontal review information request on GenAI inventory (responded). One over-age item flagged with slippage commentary.
- **Foundation-model and AI vendor exposure** — top vendors named with use-case counts; foundation-model concentration table with three providers and one heavily concentrated; top-three concentration ratio = 0.81 (firm threshold = 0.70); version-change posture for the concentrated provider = floating (recommendation in the policy refresh to move to rolling-with-notice); watch list = the concentrated provider (concern = quality drift; the version swap incident this period is the basis).
- **Model performance trends** — 27 tier-1 and tier-2 in-production; three red breaches called out (PSI breach on the small-business credit decisioning model; refusal-rate breach on the relationship-manager assistant per the incident; complaint-rate drift on the customer-service assistant). Drift signals across the population, fairness drift on customer-facing summary, GenAI-specific drift summary all populated.
- **GenAI program status** — pipeline (intake = 8, in pre-prod gate = 12, in production = 14, retired = 1); pre-prod gate throughput (decisions = 6, exceptions = 1, items returned = 2; exception rationale summary on the one); RAG corpora under governance = 4; agentic deployments by autonomy level (human-in-the-loop = 5, human-on-the-loop = 3, supervised-autonomy = 0, agentic-with-tool-use = 0); GenAI incident posture summary covers the prompt-injection signal event, the retrieval-source audit finding, and the version swap incident.
- **AI governance maturity posture** — framework = nist-ai-rmf with the joint interagency Revised Guidance on Model Risk Management (OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026) governance overlay for traditional models in scope; the bulletin's GenAI/agentic scope exclusion (footnote 3) is noted. Narrative summary covers organisational governance, accountability, third-party considerations, and the GenAI overlay maturity.
- **Policy and framework changes** — three changes: AI policy refresh in the decisions list this meeting; agentic-AI controls update effective last month; vendor evaluation criteria revision for foundation-model providers effective this quarter.
- **Forward look** — five named items: NIST AI 600-1 update expected next quarter and firm review cadence; expected NYDFS Part 500 amendment effective Q1 next year and impact on cyber program; firm-policy mapping of GenAI use cases to the joint interagency Revised Guidance principles (the bulletin scope-excludes GenAI per footnote 3, so the work is firm-policy carry-forward); foundation-model swap for the customer-service assistant in the next two cycles; agentic deployment readiness review for the wealth advisor assistant in Q1 next year.
- **Decisions (full detail)** — three decisions with options, recommended motion, dissents (none recorded), requested vote.
- **Appendices** — data confidence label = medium (BCBS 239 known limitations on AI inventory aggregation are non-empty; inventory reconciliation status = partial); BCBS 239 known limitations enumerated; source trace per material claim; AI inventory completeness statement with the OCC MRA reference; sign-off block (AI Governance Lead, head of model risk, CRO acknowledgement).

The pack stops at draft. The AI Governance Lead and the head of model risk review before the committee secretary prepares for distribution.

## Why this scenario matters

- Foundation-model concentration is the lead vendor item and is named, not buried. Top-three concentration ratio is the standing line; the firm threshold is named; the recommendation to diversify is a decision item.
- Near-misses are reported as a separate sub-section with three entries, not folded into incidents. The vendor-version near-miss converted to an incident; the prompt-injection signal event and the retrieval-source audit finding are pure near-misses; the section makes the seam visible.
- Top-risks trajectory is the four-value enum with one-line basis on each entry. "Stable" carries with a basis; "new" carries with logged date; "worsening" and "improving" carry with the underlying movement. No risk repeats from prior pack as "stable" without movement evidence.
- Decisions are first, not last. Committee chair reads three decisions before the executive summary; everything else supports those decisions.
- Data confidence label is medium because of BCBS 239 known limitations and partial inventory reconciliation. Schema validation enforces this; the label is medium.
- The OCC MRA on inventory completeness is the recurring exam topic and the section makes the remediation trajectory visible to the committee.

## Anchors

- Joint interagency Revised Guidance on Model Risk Management (OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026; supersedes SR 11-7), with footnote 3 GenAI/agentic scope exclusion.
- NIST AI RMF 1.0 Govern function.
- NIST AI 600-1 Generative AI Profile.
- 12 CFR Part 30 Appendix D Section II and Section III.
- OCC Bulletin 2023-17 Risk Management Life Cycle.
- BCBS 239 Principles 3, 7-11.
- CFPB Circular 2022-03 [withdrawn May 12, 2025; historical only — anchor to Reg B §1002.9].
- NYDFS Industry Letter (October 2024) [verify section].

See `references/source-anchors.md` for full citations and verification flags.
