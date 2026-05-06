# udaap-risk-review — Phase 1 spec sheet

Date: 2026-05-06
Plugin: consumer-compliance-fair-lending
Phase: 1 (per-skill scoping; no SKILL.md content)

## Activation-tuned description

Reviews a product, feature, fee, disclosure flow, servicing process, or marketing motion for UDAAP risk under Dodd-Frank §1031 / §1036 — deception, unfairness, abusiveness — using the CFPB UDAAP Examination Manual elements. Produces a second-line UDAAP review memo with element-by-element analysis, consumer-harm hypothesis, severity rating, and recommended remediation.

Best for:
- Pre-launch UDAAP review of a new product, feature, fee, or disclosure flow.
- Targeted review after a complaint theme, regulator inquiry, or consent order in the firm's footprint suggests UDAAP exposure (cross-reference complaint-theme-analysis).
- Annual UDAAP risk-assessment refresh by product line.
- Post-incident root-cause review where consumer harm has been alleged.

Not the right tool when:
- The question is fair-lending under ECOA / FHA (use fair-lending-test-plan; UDAAP and fair-lending overlap but are distinct frameworks).
- The question is the adverse action notice (use adverse-action-review).
- The question is marketing-claim substantiation at the asset level (use marketing-claim-review; this skill addresses UDAAP at the product / process level).
- A final UDAAP determination is required (this skill does not finalize; it surfaces risk).

Anchored to: Dodd-Frank §1031 (12 U.S.C. §5531) — unfair, deceptive, or abusive acts or practices; Dodd-Frank §1036 (12 U.S.C. §5536) — prohibited acts; CFPB UDAAP Examination Manual (current edition) — element tests for deception, unfairness, abusiveness; CFPB Policy Statement on Abusive Acts or Practices (April 3, 2023) [verify exact title and date]; FTC Act §5 (15 U.S.C. §45) — UDAP overlay where applicable; CFPB Circulars on UDAAP topics (current set; including circulars on overdraft, junk fees, deposit account fees, fee mismatches, and AI-related practices) [verify circulars in scope]; CFPB Supervisory Highlights (latest two issues at time of review).

## Source anchors

- Dodd-Frank §1031, 12 U.S.C. §5531 — definitions of unfair, deceptive, abusive (statutory standards for unfairness and abusiveness).
- Dodd-Frank §1036, 12 U.S.C. §5536 — prohibition on UDAAPs.
- CFPB UDAAP Examination Manual (current edition) [verify edition date] — element tests:
  - Deception: representation / omission / practice that is likely to mislead a reasonable consumer; consumer's interpretation is reasonable; representation / omission / practice is material.
  - Unfairness: substantial injury to consumers; not reasonably avoidable; not outweighed by countervailing benefits.
  - Abusiveness: materially interferes with ability to understand a term or condition; takes unreasonable advantage of lack of understanding, inability to protect interests, or reasonable reliance.
- CFPB Policy Statement on Abusive Acts or Practices [verify exact title and date — bureau issued an updated abusiveness policy in 2023].
- FTC Act §5 (15 U.S.C. §45) — UDAP framework where the firm is FTC-jurisdictional or the FTC overlay applies.
- CFPB Circulars relevant to UDAAP — including circulars on (non-exhaustive; phase 2 enumerates):
  - Overdraft and authorize-positive-settle-negative practices.
  - Surprise overdraft and surprise representment fees.
  - Pay-to-pay (convenience) fees.
  - Negative-option marketing.
  - Algorithmic discrimination touching UDAAP — Joint Statement (April 2023) overlay.
  - Adverse action and complex-algorithm circulars (2022-03, 2023-03) where UDAAP touches AI-driven decisioning.
- CFPB Supervisory Highlights (most recent two editions) [verify issue numbers and dates] — bureau-stated UDAAP focus areas.
- CFPB enforcement actions and consent orders (used as worked-example anchors; cite by name and date).
- DOJ joint actions where UDAAP overlaps with civil rights enforcement.
- Joint Statement on Enforcement of Civil Rights, Fair Lending, Fair Housing, and Consumer Financial Protection Laws (CFPB / DOJ / FTC / EEOC, April 25, 2023) — algorithmic discrimination tying into unfairness theories.

## Sector overlays needed

- `references/sector-overlays/banking.md` — overdraft and NSF practices; deposit account fee structures; mortgage servicing (loss mitigation, force-placed insurance, fee assessments); credit-card specific UDAAP themes (deferred-interest promotions, rewards-program changes, balance transfer mechanics); auto loan add-ons (GAP, VSC).
- `references/sector-overlays/payments-fintech.md` — sponsor bank attribution; BNPL UDAAP themes [verify current bureau position]; P2P and Reg E error-resolution; subscription / negative-option mechanics; tip and "instant funding" fee mechanics; junk-fee themes.
- `references/sector-overlays/capital-markets.md` — retail brokerage UDAP overlay where Reg BI / FINRA Rule 2010 overlap (non-CFPB-jurisdictional but the same fact patterns); securities-based lending and margin-call mechanics.
- `references/sector-overlays/insurance.md` — bank-affiliated insurance and credit-life add-ons; flag scope boundary for state-DOI unfair trade practices.

## Cross-cutting overlays

- `references/cross-cutting/conduct.md` — UDAAP findings as the dominant conduct-risk signal; mapping to firm conduct-risk taxonomy (incentives, product design, communication, sales practices); FCA conduct-risk framework parallel for global firms; conduct-committee escalation path; complaint-theme intersection with conduct.
- (AI-related cross-cutting is implicit where the product or process is AI-driven. SKILL.md must reference the April 2023 Joint Statement and the CFPB AI / complex-model circulars where AI personalization, AI underwriting, or AI-generated communication is in scope. The bureau has explicitly used existing UDAAP authority against algorithmic harms.)

Privacy not applicable as a primary overlay (handled at marketing-claim-review and adverse-action-review). Climate not applicable.

## Output template named sections

1. Scope (product / feature / fee / disclosure / process; period; channel; population)
2. Reviewer and review posture (legal-privilege posture, second-line independence, evidence base)
3. Element-by-element analysis:
   a. Deception — representation / omission / practice; reasonable consumer; materiality
   b. Unfairness — substantial injury; not reasonably avoidable; countervailing benefits
   c. Abusiveness — material interference; unreasonable advantage
4. Consumer-harm hypothesis (population affected, magnitude, frequency, redress posture)
5. Evidence supporting / refuting each element (with named source: complaints, transaction data, call recordings, marketing assets, policy text, training records, system-output logs)
6. AI / algorithmic discrimination tie-in (where applicable)
7. Severity rating (with rubric)
8. Conduct-risk implications (cross-cutting/conduct.md)
9. Recommended remediation (consumer redress, control change, policy change, training, kill-switch candidates, named owner, due date)
10. Open legal questions
11. Cross-references (complaint-theme-analysis, marketing-claim-review, adverse-action-review, fair-lending-test-plan)
12. Source trace and confidence label

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| `review_id` | string | Unique reference. |
| `scope` | object | Product, feature, fee, disclosure, process, period, channel, population. |
| `legal_privilege_posture` | string | Privilege flag. |
| `evidence_base[]` | array of objects | Source, type, date, completeness flag. |
| `deception` | object | Element findings. |
| `deception.representation_or_omission` | string | What is represented or omitted. |
| `deception.likely_to_mislead` | enum | `yes`, `no`, `indeterminate`. |
| `deception.reasonable_consumer_basis` | string | Reasoning. |
| `deception.materiality` | enum | `material`, `not_material`, `indeterminate`. |
| `unfairness` | object | Element findings. |
| `unfairness.substantial_injury` | object | Injury type, magnitude, population. |
| `unfairness.reasonably_avoidable` | enum | `yes`, `no`, `indeterminate`. |
| `unfairness.countervailing_benefits` | object | Benefits asserted by first line; reviewer assessment. |
| `abusiveness` | object | Element findings. |
| `abusiveness.material_interference` | object | Description, evidence. |
| `abusiveness.unreasonable_advantage` | object | Type (lack of understanding, inability to protect interests, reasonable reliance), evidence. |
| `consumer_harm` | object | Population, magnitude, frequency, redress posture. |
| `ai_algorithmic_findings` | object | Where AI is involved; cite-back to circulars and Joint Statement. |
| `severity` | enum | `low`, `medium`, `high`, `critical`. |
| `severity_rationale` | string | Per-element reasoning. |
| `conduct_risk_implications[]` | array of strings | Conduct-risk taxonomy tie-back. |
| `recommended_remediation[]` | array of objects | Action, type (redress / control / policy / training / kill-switch), owner, due date. |
| `open_questions[]` | array of strings | For counsel. |
| `cross_references[]` | array of strings | Other skills called for follow-up. |
| `source_trace[]` | array of objects | Claim, source, evidence, confidence. |

## Example scenarios (public-source-derived, anonymous)

1. Pre-launch UDAAP review of a new "instant funding" feature on a personal-loan product, where instant funding is offered for a tip or fee disclosed at funding selection but not at the application page. Element analysis: deception — the application page presents an APR that does not include the funding fee, and the funding-fee election is presented at a moment of high consumer commitment; reasonable consumer would interpret the APR as inclusive of the cost of funds; materiality clear. Unfairness — the disclosed structure may meet the unfairness elements depending on the avoidability analysis (slow-funding alternative is functionally available but de-emphasized in UI). Severity assigned `high`. Recommended remediation: re-design the disclosure to surface fee at application; add fee in the cost-of-credit math for marketing; restructure UI so slow-funding default is symmetric. Cross-reference to marketing-claim-review for asset-level review. (Pattern derived from public CFPB enforcement themes on instant-funding tips and fees.)

2. Annual UDAAP risk-assessment refresh on a deposit-account overdraft program for a regional bank. Findings: authorize-positive-settle-negative pattern present in 11% of overdraft fees in the period (CFPB has named this practice as unfair). Surprise overdraft fee on debit-card transactions where intervening transactions cleared first. Element analysis ties findings to unfairness elements: substantial injury (per-fee dollar value times population); not reasonably avoidable (consumer cannot anticipate authorization-vs-settlement timing); countervailing benefits weak. Severity assigned `critical`. Conduct-risk implications: incentive design for branch overdraft education, complaint volume linkage. Recommended remediation: pause the APSN pattern; consumer-redress program for affected fees in the lookback period; control change to detect and prevent APSN at posting; training; quarterly reporting to the conduct committee. Cross-reference to complaint-theme-analysis. (Pattern derived from public CFPB enforcement and supervisory observations on APSN overdraft practices.)

## Common pitfalls

1. Reviewing only deception, ignoring unfairness and abusiveness. UDAAP is three elements; firms over-index on deception because it is the easiest to evidence with marketing artifacts. Mitigation: every review covers all three element tests; abusiveness can be `not_applicable` but only with rationale.
2. Treating "the disclosure was technically correct" as a defense. Materially-correct technical disclosure can still mislead a reasonable consumer in context; CFPB has consistently pursued context-driven deception. Mitigation: deception analysis includes the consumer journey, not the disclosure document alone.
3. Substantial-injury analysis without a population estimate. "Some customers were charged" is not a UDAAP finding. Mitigation: consumer_harm.population and magnitude fields are mandatory with sourcing.
4. Countervailing-benefits analysis written as the first line's marketing pitch. The countervailing-benefits prong is not a sales argument. Mitigation: reviewer must independently assess; the first-line assertion is recorded but not sufficient.
5. Algorithmic / AI fact patterns reviewed as if UDAAP does not reach the model. The bureau has explicitly said UDAAP does. Mitigation: ai_algorithmic_findings block is mandatory where AI is in the production path; cite-backs to CFPB circulars and Joint Statement.
6. Severity rating set without a rubric. Severity drift is the single most common audit finding on UDAAP processes. Mitigation: severity rubric named and applied per element, with rationale field.
7. Skill produces a UDAAP determination or executes remediation. It does not. The skill produces a UDAAP review memo with element-by-element analysis and recommended remediation for human decision.

## Guardrail (mandatory in SKILL.md)

This skill does not finalize UDAAP determinations, approve products for launch, take down live products, execute consumer redress, or take any customer-facing action. It produces a UDAAP review memo and surfaces red flags for human decision by qualified compliance, conduct, fair-lending, legal, and product reviewers.
