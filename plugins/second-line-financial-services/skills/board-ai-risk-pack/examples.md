# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## national-bank-quarterly

### Example: quarterly AI risk committee pack at a US national bank

Public-source-derived. No named institution. Framing patterns from SR 11-7, OCC Heightened Standards (12 CFR Part 30 Appendix D), the joint interagency third-party guidance (OCC Bulletin 2023-17), Reg B §1002.9 (adverse-action notification), and NYDFS October 2024 Industry Letter on AI cybersecurity. CFPB Circular 2022-03 informed earlier framing but was **withdrawn May 12, 2025; historical only**. No firm-specific facts asserted.

#### Input

- Institution: US national bank, OCC-supervised, mid-size to large by asset, OCC Heightened Standards covered. Standalone AI Risk Committee chartered alongside the board risk committee.
- Engagement scope supplied: institution.type = bank holding company; primary regulators OCC, FRB, CFPB; persona = AI Governance Lead, second line, reporting to the CRO; sector overlay = banking; cross-cutting overlays = cyber, conduct; source posture = public-plus-firm-policy-plus-system-of-record-evidence.
- Period: Q3; standing quarterly AI Risk Committee meeting.
- Upstream artifacts on file: AI inventory of record (47 in-production use cases, 12 in pre-prod gate, four retired in period); model performance feed for tier-1 and tier-2; AI incident log; vendor exposure data from `vendor-diligence` AI-vendor mode runs; open MRA on AI inventory completeness from the most recent OCC continuous-monitoring letter; AI policy refresh draft from the AI governance working group.
- AI Governance Lead has flagged: foundation-model concentration on a single provider crossed firm threshold; one tier-1 incident (vendor LLM version swap caused refusal-rate spike on relationship-manager assistant; resolved, no customer impact, near-miss logged); two newly tier-1 consumer-decisioning models in flight at pre-prod gate; AI policy refresh ready for committee approval.

#### Output sketch

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

#### Why this scenario matters

- Foundation-model concentration is the lead vendor item and is named, not buried. Top-three concentration ratio is the standing line; the firm threshold is named; the recommendation to diversify is a decision item.
- Near-misses are reported as a separate sub-section with three entries, not folded into incidents. The vendor-version near-miss converted to an incident; the prompt-injection signal event and the retrieval-source audit finding are pure near-misses; the section makes the seam visible.
- Top-risks trajectory is the four-value enum with one-line basis on each entry. "Stable" carries with a basis; "new" carries with logged date; "worsening" and "improving" carry with the underlying movement. No risk repeats from prior pack as "stable" without movement evidence.
- Decisions are first, not last. Committee chair reads three decisions before the executive summary; everything else supports those decisions.
- Data confidence label is medium because of BCBS 239 known limitations and partial inventory reconciliation. Schema validation enforces this; the label is medium.
- The OCC MRA on inventory completeness is the recurring exam topic and the section makes the remediation trajectory visible to the committee.

#### Anchors

- Joint interagency Revised Guidance on Model Risk Management (OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026; supersedes SR 11-7), with footnote 3 GenAI/agentic scope exclusion.
- NIST AI RMF 1.0 Govern function.
- NIST AI 600-1 Generative AI Profile.
- 12 CFR Part 30 Appendix D Section II and Section III.
- OCC Bulletin 2023-17 Risk Management Life Cycle.
- BCBS 239 Principles 3, 7-11.
- CFPB Circular 2022-03 [withdrawn May 12, 2025; historical only — anchor to Reg B §1002.9].
- NYDFS Industry Letter (October 2024) [verify section].

See `references/source-anchors.md` for full citations and verification flags.

## regional-life-insurer-annual

### Example: annual board AI program review at a regional life insurer

Public-source-derived. No named institution. Framing patterns from the NAIC Model Bulletin on the Use of AI Systems by Insurers (December 2023), NAIC Model #505 ORSA, NYDFS Insurance Circular Letter (January 2024), and the Colorado Division of Insurance regulation implementing SB 21-169. No firm-specific facts asserted.

#### Input

- Institution: US regional life insurer, multistate writer with NY and CO footprint among others. Holding-company structure with an ORSA filing under Model #505. AI governance run as a section of the board risk committee (no standalone AI committee at this firm size).
- Engagement scope supplied: institution.type = insurer; primary regulators = state DOIs in operating states (NY DFS, CO DOI flagged); persona = AI Governance Lead, second line, reporting to the chief risk officer; sector overlay = insurance; cross-cutting overlay = conduct; source posture = public-plus-firm-policy-plus-system-of-record-evidence.
- Period: annual board education and program review session ahead of ORSA Summary Report drafting.
- Upstream artifacts on file: AI inventory (12 in-production use cases, four in pre-prod gate); AIS Program self-assessment results from the second-line annual cycle; state DOI inquiry inventory (one NY DFS information request on AI in life-underwriting acceleration in progress; one CO DOI information request on the SB 21-169 framework documentation responded last quarter); foundation-model vendor concentration in claims summarisation pilot; AI governance framework draft updated for NAIC Model Bulletin alignment.
- AI Governance Lead has flagged: claims summarisation pilot expected to seek production approval in two quarters; the AI governance framework update is the headline decision for the board; state insurance fairness exposure on accelerated underwriting is the top risk.

#### Output sketch

The skill emits a markdown pack and a structured record. Headlines:

- **Cover and decisions requested** — board risk committee, annual session, classification = board-confidential. Two decisions up front: (i) board endorsement of the AI governance framework as updated for NAIC Model Bulletin AIS Program alignment; (ii) acknowledgement of the claims summarisation pilot trajectory toward production approval and direction to second-line on production-readiness criteria.
- **Executive summary** — five bullets in AI Governance Lead voice. Headline: 12 in-production AI use cases mostly pricing and underwriting decisioning; top risks are state insurance fairness exposure on accelerated underwriting and foundation-model vendor concentration in claims pilot; one state DOI information request closed in period and one in progress; AI governance framework ready for board endorsement; AIS Program self-assessment shows alignment in seven of nine elements with two flagged for build-out.
- **AI inventory state** — 12 in-production, four in pre-prod gate, no retirements; tier-1 = 4 (life underwriting acceleration, P&C pricing, accelerated underwriting fraud screening, agent productivity recommendation), tier-2 = 5, tier-3 = 3; by architecture flag traditional ML = 9, foundation-model = 2, RAG = 1, agentic = 0; tier movements = one (accelerated underwriting fraud screening moved tier-3 to tier-2 driven by expanded use across more products); by business line breakdown (life = 6, P&C = 3, claims = 2, distribution = 1); inventory reconciliation status = reconciled.
- **Top AI risks** — five named risks. State insurance fairness exposure on accelerated underwriting trajectory = stable (basis: latest unfair-discrimination testing pass under the NAIC Bulletin fairness element with disparity assessment within thresholds for in-scope dimensions). Foundation-model vendor concentration in claims summarisation pilot trajectory = new (logged this quarter as the pilot reaches scale). NAIC Model Bulletin alignment trajectory = improving (basis: AIS Program self-assessment moved from five aligned to seven aligned out of nine). Third-party AI accountability posture trajectory = stable (basis: vendor evidence pack reviews complete for the two foundation-model vendors). Customer recourse posture for AI-driven decisions trajectory = improving (basis: enhanced disclosure language and recourse mechanism rolled out per CO SB 21-169 framework).
- **In-flight reviews and decisions** — four items: claims summarisation pilot production-readiness review (decision due in two cycles); AI governance framework endorsement (this meeting); two pre-prod gate items on tier-2 underwriting AI (decisions due over next two cycles).
- **Incidents and near-misses** — incidents: no incidents in the annual period rising to committee notification threshold. Near-misses section: two logged (one fairness-metric drift signal on a tier-2 underwriting model, detected and remediated through model retune; one vendor evidence-pack staleness flagged in the third-party review and refreshed).
- **Regulator and exam interactions** — one NY DFS information request on AI in life-underwriting acceleration (in-progress, head of underwriting governance, target close end of quarter); one CO DOI information request on SB 21-169 framework documentation (responded, no follow-up); NAIC AI Working Group participation update (not an interaction in the regulator-action sense; noted for board context).
- **Foundation-model and AI vendor exposure** — top vendors named with use-case counts; foundation-model concentration table with two providers, one in claims summarisation pilot and one in agent productivity recommendation; top-three concentration ratio = 0.95 (driven by very small GenAI footprint; firm threshold is not yet codified for an insurer of this profile and that absence is itself a decision item carried forward); version-change posture = pinned for both; watch list = empty.
- **Model performance trends** — nine tier-1 and tier-2 in-production; one yellow drift signal on the tier-2 underwriting model converted to a near-miss (above); fairness-metric drift summary covers underwriting and pricing models; GenAI-specific drift not yet meaningful at this scale.
- **GenAI program status** — pipeline (intake = 1, in pre-prod gate = 2, in production = 2, retired = 0); pre-prod gate throughput (decisions = 1, exceptions = 0, items returned = 1; exception rationale summary on the returned item); RAG corpora under governance = 1 (the claims-summarisation pilot retrieval corpus); agentic deployments by autonomy level = none; GenAI incident posture summary indicates no GenAI incidents in period.
- **AI governance maturity posture** — framework = naic-ais-program; narrative summary covers each of the nine AIS Program elements (governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness) with the seven aligned elements and the two flagged for build-out (third-party AI accountability and monitoring at the population level). Evidence appendix pointer to the AIS Program self-assessment artifact.
- **Policy and framework changes** — two changes: the AI governance framework update for NAIC Model Bulletin alignment (in the decisions list this meeting); enhanced consumer disclosure language for AI-driven decisions per CO SB 21-169 framework (effective last quarter).
- **Forward look** — five named items: NAIC AI Working Group state-adoption tracker movement expected on the Model Bulletin (named states with tracker status); claims summarisation pilot production-readiness review in two cycles; expected NY DFS publication update on the January 2024 Circular Letter implementation guidance; CO DOI implementation guidance evolution on SB 21-169; firm AIS Program self-assessment cycle for next year (build-out completion targeted for the two flagged elements).
- **Decisions (full detail)** — two decisions with options, recommended motion, dissents (none recorded), requested vote on (i) and acknowledgement on (ii).
- **Appendices** — data confidence label = high (inventory reconciled, no BCBS 239 limitations applicable; insurer is not a G-SIB or D-SIB so the BCBS 239 framing is not the constraining one but the data quality discipline is followed); source trace per material claim; AI inventory completeness statement with the AIS Program documentation element reference; sign-off block (AI Governance Lead, head of model risk, CRO, chief actuary, head of consumer compliance).

The pack stops at draft. The AI Governance Lead and the head of model risk review before the board committee secretary prepares for distribution.

#### Why this scenario matters

- The pack is the annual board education session, deeper than the standing quarterly cycle. The AI governance maturity posture section carries the AIS Program element-by-element narrative; this is the deeper cut a quarterly pack would compress.
- The decisions list carries an endorsement of the AI governance framework update for NAIC Model Bulletin alignment. This is the standing committee decision insurers face as state DOIs adopt the Bulletin and the firm's framework needs board-level endorsement to support the AIS Program governance element.
- The state DOI inquiry inventory is its own line under regulator interactions; for insurers the state-DOI surface is the dominant exam interaction and the committee oversight visibility is required.
- Top-risks trajectory is the four-value enum with one-line basis. "Improving" on NAIC alignment carries with the AIS Program self-assessment movement; "new" on foundation-model concentration carries with the pilot reaching scale.
- Foundation-model concentration is named even at low scale because the pilot is approaching production. Firm threshold absence (the firm has not yet codified a threshold for an insurer of this size) is itself surfaced as a decision item; this is the right kind of "decision the committee owes" that a pack can surface.
- Sign-off block names the chief actuary and the head of consumer compliance because actuarial AI is in scope and customer-facing claims and underwriting AI is in scope. The persona constellation is broader than the bank case.

#### Anchors

- NAIC Model Bulletin on AI by Insurers (December 2023) Sections 1-4 and AIS Program elements.
- NAIC Model #505 ORSA Section 1 (governance) and Section 3 (risk capital).
- NYDFS Insurance Circular Letter (January 2024) [verify section].
- Colorado Division of Insurance regulation implementing SB 21-169 [verify regulation number].
- NIST AI RMF 1.0 Govern function.
- ISO/IEC 42001:2023 §5.1 and §9.3 (where firm posture references the standard).

See `references/source-anchors.md` for full citations and verification flags.

## troubleshooting

### Troubleshooting: board-ai-risk-pack

Recurring defects observed when this skill is used in practice. Each defect names the failure mode and the corrective pattern.

#### The pack reads as a catalogue dump

The committee opens to page nine and reads the inventory list instead of the executive summary. The decision items go missed. The chair leaves the meeting frustrated.

Corrective: the executive summary is up-to-five bullets at most and the rest of the pack is curated, not exhaustive. The inventory list is in `ai-use-case-intake` outputs; this pack carries summary counts and movement, not the catalogue. If the pack runs longer than a quarterly committee can read in a thirty-minute pre-read, the pack has inverted what belongs in the body and what belongs in the appendix.

#### Top risks repeats across packs without movement

The same five risks appear pack after pack with "stable" trajectory and no underlying movement. The committee stops engaging with the section because nothing changes. New risks land late because no one wants to retire an existing one to make room.

Corrective: trajectory is a four-value enum (improving, stable, worsening, new) with a required one-line basis on each entry. "Stable" without basis is the wallpaper failure mode. New risks land with `new` flag and `logged_date`. Risks that have been stable for four cycles with no underlying movement are candidates for retirement to the watch list rather than the top-risks section.

#### Incidents reported with no near-misses section

The pack lists incidents as resolved. The committee gets a false sense of security. Two cycles later, a near-miss that was not surfaced becomes an incident, and the chair asks why the committee did not see it earlier.

Corrective: near-misses are a separate sub-section under incidents, required every cycle. If the period had no near-misses, state that explicitly with one line on what was checked. An empty near-miss section without statement triggers the standing reviewer question on detection coverage.

#### Foundation-model vendor concentration is buried

The committee does not see that the firm has 80% of GenAI use cases on a single foundation-model provider until the provider issues a deprecation notice or has a security incident. The concentration risk lands as a fire drill, not an oversight finding.

Corrective: foundation-model concentration is a required section with a top-three concentration ratio. The firm threshold is named (or the absence of a threshold is itself flagged as a sign-off question). Watch list entries for concentrated providers carry the named concern. The version-change posture is reported by vendor.

#### Decisions requested are vague or missing

The decisions section says "note the report" or is empty. The committee meeting closes with no decisions taken. The pack functions as a status update masquerading as a committee instrument.

Corrective: decisions requested entries have options and a recommended motion. "Note the report" is not a decision. If nothing requires committee action this cycle, surface that explicitly so the chair can decide whether to call the meeting; the pack does not pretend a status update is a committee instrument.

#### Sector overlay loaded but not reflected in the pack body

The scope flags insurance, the insurance overlay loads, and the pack body is generic. The NAIC AIS Program elements are not addressed. The state DOI inquiry inventory is missing. The reviewer flags the gap on first read.

Corrective: overlays are content that lands in the pack body, not background reading. Insurance overlay implies AIS Program element narrative in the maturity section, state DOI inquiry inventory in the regulator interactions section, NAIC #880 / NYDFS Circular Letter / CO SB 21-169 framing in the top risks section as applicable. Same pattern for banking, capital-markets, payments-fintech.

#### Cyber overlay loaded but only AI-enabled threats called out

The cyber overlay treats deepfakes and AI-aided phishing as the cyber-AI section and ignores the firm's own use of AI as cyber surface. Prompt-injection signal is not surfaced. The vendor cyber posture is not reported. The NYDFS October 2024 Industry Letter framing is not reflected.

Corrective: cyber-AI risk is two buckets: AI-enabled threats targeting the firm, and the firm's own use of AI as cyber surface (prompt injection, data exposure through GenAI outputs, vendor concentration on AI providers). Both are reflected in top risks and incidents where elevated. The GenAI program status section carries the prompt-injection signal trend as a standing line.

#### Conduct overlay reduces to "fairness testing happened"

The pack reports that fairness testing ran for the quarter and the disparity ratios were within thresholds. The complaint-rate drift is not reported. The adverse-action notice quality posture is not surfaced. The customer-facing GenAI accuracy and harm posture is not addressed.

Corrective: conduct-AI risk is broader than fairness testing. Adverse-action notice posture for credit decisioning AI, complaint-rate drift on AI-touched products, claims-handling AI fairness and accuracy, customer-facing GenAI accuracy and harm are all in scope where the firm has the relevant exposure. The conduct overlay sets which of these surface.

#### Inventory state count not reconciled to the inventory of record

The pack reports 47 in-production use cases. The system of record reports 51. The discrepancy is not surfaced. Three months later, an OCC continuous-monitoring letter cites the discrepancy as an inventory completeness finding.

Corrective: inventory reconciliation status is a required field on the inventory state section (reconciled, partial, not-reconciled). If partial or not-reconciled, the data confidence label cannot be high; the gap is named in the AI inventory completeness statement appendix; and the gap routes to the engagement issue log if not already an open MRA.

#### "Continuing to monitor the regulatory landscape"

The forward-look section recycles generic regulatory-horizon language pack after pack. The committee learns nothing actionable. The named items the committee can act on are missing.

Corrective: forward look is named, dated, regulator-anchored. Two cycles ahead is the standard horizon. Items: regulator developments expected (rule, date, implication), use cases on the runway for tier escalation or pre-prod gate, GenAI deployments on the runway for production, foundation-model vendor changes expected, validation cycles due, training and capability program milestones. "Continuing to monitor the landscape" fails the section.

#### AI governance maturity posture is one paragraph of marketing copy

The maturity section reads like a vendor pitch: "robust governance framework", "comprehensive AI program", "aligned to leading practice". Nothing the committee can challenge. Nothing that names the gaps.

Corrective: maturity narrative is calibrated to the named framework (NIST AI RMF, NAIC AIS Program, ISO/IEC 42001, EU AI Act deployer, firm-bespoke, blended). Each named framework dimension is addressed with current posture and named gaps. For insurers the AIS Program element-by-element narrative is the standing pattern; for federally regulated banks the NIST Govern function plus SR 11-7 §III posture is the standing pattern; for ISO/IEC 42001 firms the §5.1 / §6.2 / §9.3 posture is the standing pattern.

#### Pack overlaps with the enterprise risk committee pack

The board AI risk pack and the enterprise risk committee pack both anchor the AI sources, both report the AI inventory state, both list AI top risks. Two committees see two versions of the same content with the same depth. Neither committee gets the right pack for its audience.

Corrective: the board AI risk pack is the AI committee instrument, anchored to AI sources at AI committee depth. The enterprise risk committee pack consumes a brief from this pack for the AI heat-map cell and any AI-driven top-risks entry rather than re-anchoring the AI sources. The AI committee pack does not re-anchor enterprise risk sources (BCBS 239 framing on AI inventory aggregation is the one cross-cutting anchor that lives in both for a different reason).

#### Sign-off block names individuals instead of roles

The pack lists named individuals in the sign-off block. The pack ages and the named individuals leave or change roles. The audit trail is degraded.

Corrective: sign-off block names roles, not individuals. The system of record carries the named individual against the role at the time of sign-off. This is the same standing rule as the model card and the enterprise risk committee pack.
