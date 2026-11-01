# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## annual-bank-portfolio-review

### Example: annual operational-resilience-committee concentration review for a US regional bank

#### Input

A US regional bank, in the $50B-$250B asset band, runs the annual portfolio concentration cycle for its operational-resilience committee. Inputs supplied: the firm's TPRM register (310 active third-party arrangements), the criticality-assessment outputs for the 84 arrangements classified as critical or important, the firm's IBS map (12 important business services), the cloud-region map maintained by the cloud-platform team, the sub-contractor inventory where vendors have disclosed (rank-1 visibility on most arrangements; rank-2 disclosed on 28 of the 84 critical-or-important arrangements), and the prior-year concentration review for delta context. Source posture is public-plus-firm-policy-plus-system-of-record-evidence. Sector overlay: banking. Cross-cutting overlay: cyber.

#### Output sketch

The skill produces a structured record per `schemas/concentration-review.schema.json` and a committee narrative per `templates/default-output.md`. Highlights:

- **Scope and source posture**: 1 in-scope legal entity (the bank), `consolidation_level = individual`, register source TPRM as of the cycle date, criticality cutoff `critical-or-important` (84 arrangements), fourth-party visibility `rank-2-and-deeper` for 28 of 84 (33%) and `rank-1-only` for the rest. Data-quality caveats: 14 of the 84 arrangements carry `criticality = important` set on a placeholder basis without evidence backing, surfaced as a finding and routed back to `criticality-assessment`.
- **Hyperscaler dimension**: 62% of critical-or-important arrangements depend on a single hyperscaler for primary compute, with 71% of those concentrated in a single sub-region of one country. Multi-region promises documented in 18 arrangements; substitutability read names that the same hyperscaler's other regions share control plane, identity layer, and billing operation, so the multi-region claim does not equal multi-resilience for control-plane outages. Severity: `elevated`.
- **Shared-utility dimension**: KYC utility usage concentrates with one vendor across three critical-or-important arrangements (consumer onboarding, commercial onboarding, BSA periodic re-verification). The KYC vendor itself runs on the same hyperscaler the bank's own platform runs on; this is a hidden cross-dimension dependency surfaced in the technology-stack-shared-utility row. Severity: `watch` on its own; `elevated` when read against the hyperscaler dimension.
- **Fourth-party dimension**: a single SaaS-billing platform sits behind three nominally independent vendors (a workforce-scheduling vendor, an expense-management vendor, and a corporate-card programme vendor); none of the three first-line vendor relationships flagged the dependency in their respective `vendor-diligence` packs. The finding routes back as a re-ask. Severity: `watch`.
- **Sponsor-bank / BaaS dimension**: not applicable to this bank's own balance sheet; surfaced as `clear` for completeness.
- **AI-provider dimension**: the bank uses one foundation-model API across four AI use cases (call-summarisation, complaint-classification, internal knowledge retrieval, document-summarisation in commercial credit). All four sit on one foundation-model vendor's commercial API. The use cases are not customer-decisioning; severity `watch` rather than `elevated`. Re-test cadence: 6 months rather than the annual cycle for the rest of the portfolio.
- **Single-points-of-failure**: 4 critical-or-important functions identified where one failure removes the function entirely with no ready substitute under benign conditions; 9 functions added to the list when the substitutability read is run under stressed conditions (the substitute itself would be unavailable in a wider sector event).
- **Substitutability read**: the hyperscaler concentration read shows partial contractual portability (data export defined in 14 of the relevant arrangements, undefined in 18), weak operational substitutability (the bank has not exercised a substitute migration in the last 24 months), and absent stressed substitutability (sector-wide hyperscaler outage scenarios were not modelled in the last `resilience-testing-pack` cycle). Recommended actions chain to `resilience-testing-pack` for the substitute-migration scenario test and to `contract-gap-review` for the data-portability clause set.
- **Recommended actions**: 11 actions, named owner role per action, half chained to other skills, due dates clustered in the next two committee cycles.
- **Reviewer questions for the operational-resilience committee**: cluster on (a) whether the hyperscaler concentration sits within or above the firm's risk-appetite, (b) whether the fourth-party SaaS-billing dependency warrants a re-ask of the three first-line vendors and a refresh of their `vendor-diligence` packs, (c) whether the AI-provider concentration warrants a board-level briefing given the use-case spread is non-customer-decisioning today but trending upward.

#### Why this scenario matters

Exercises the full dimension set on a portfolio big enough that the cross-dimension reads matter (hyperscaler-on-hyperscaler-on-shared-utility). Tests the load-bearing rules: spend is not the metric; multi-region is not multi-resilience; fourth-party visibility limits are findings, not absences; the substitutability read names the difference between benign and stressed conditions. Surfaces the firm-policy-vs-supervisory-threshold layering through the threshold-reference column. Demonstrates the chain to `vendor-diligence`, `contract-gap-review`, and `resilience-testing-pack` without duplicating their work.

## dora-preliminary-assessment-eu-insurer

### Example: DORA Article 29 preliminary concentration assessment for an EU subsidiary of a US insurer

#### Input

EU subsidiary of a US insurance group, in DORA scope as an insurance undertaking, running a pre-contract preliminary assessment of ICT concentration risk for a proposed critical-or-important ICT service: a managed claims-analytics platform that would replace the firm's current in-house analytics for property-and-casualty large-loss claims. Inputs supplied: the firm's DORA register of information output (the `dora-register-builder` artifact from the most recent reporting cycle, 31 ICT third-party arrangements), the criticality-assessment determination on the proposed service (critical-or-important; the analytics output feeds the firm's IBS for large-loss claims handling), the proposed vendor's `vendor-diligence` pack draft (in flight, sub-contractor chain disclosed to rank 2), and the firm's existing analytics-vendor footprint. Source posture is public-plus-firm-policy. Sector overlays: insurance and capital-markets (the holding-company-level filing dimension). Cross-cutting overlay: cyber.

#### Output sketch

The skill produces a structured record per `schemas/concentration-review.schema.json` and a narrative per `templates/default-output.md`. The artifact is the draft input for the firm's signed preliminary assessment under the EU regime; legal and compliance sign-off make it the legal record. Highlights:

- **Scope and source posture**: 1 in-scope legal entity (the EU subsidiary), `consolidation_level = individual`, register source DORA register of information from the most recent reporting cycle, criticality cutoff `critical-or-important` (the proposed service is in scope; the existing portfolio is read for context). Cycle type `pre-contract-preliminary-assessment`. Data-quality caveats: the proposed vendor's sub-contractor disclosure stops at rank 2; the analytics output's downstream consumers in the firm's IBS map are listed but the IBS map itself is one cycle out of date and is being refreshed in parallel.
- **Single-vendor dimension**: the proposed vendor would be the firm's first arrangement with this counterparty; the dimension is `clear` on a stand-alone basis. The vendor's parent company is, however, the same parent as the firm's existing market-data vendor, surfacing a group-level concentration the legal-entity-only read would miss. Severity: `watch` on the group-level read.
- **Sub-contractor dimension**: the proposed vendor's rank-1 sub-contractor for compute is the same hyperscaler that hosts the firm's three other critical-or-important ICT services. Adding the proposed service would move the hyperscaler share from 60% (3 of 5 of the firm's critical-or-important ICT services) to 67% (4 of 6). The proposed vendor's rank-2 sub-contractor for identity is the same identity provider that sits behind the firm's customer-facing portal; this is a cross-arrangement dependency not previously surfaced in the register. Severity: `elevated`.
- **Sub-region dimension**: the proposed vendor would deploy in a single EU sub-region of the named hyperscaler. Two of the firm's three existing critical-or-important ICT services run in the same sub-region. The proposed addition would concentrate three of the firm's now-four critical-or-important ICT services in one sub-region, with the third service in a different sub-region of the same hyperscaler. Severity: `elevated`. Substitutability read names that the proposed vendor's contractual region commitment is documented but the firm has no operational evidence of a sub-region migration test.
- **Jurisdictional dimension**: the proposed contract's governing law is the same as the existing arrangements; dispute-resolution forum concentration is unchanged. Severity: `clear`.
- **Single-points-of-failure**: the proposed service would create a new single-point-of-failure for large-loss claims handling under the firm's IBS map (no in-house substitute remains operational once the migration completes). Severity: `elevated`.
- **Substitutability read**: alternative analytics vendors known (3 named in the market scan), time-to-substitute estimate 9-14 months under benign conditions, contractual portability `partial` (data export defined; analytics-model portability undefined), operational substitutability `weak` (firm has not run a vendor-switch test on an analytics platform), stressed substitutability `weak-to-absent` (the alternative vendors run on a small set of the same hyperscalers; sector stress affecting one hyperscaler removes most of the substitution set).
- **Recommended actions**: 7 actions. Conditions on contract (chain to `contract-gap-review` for clauses on data portability, analytics-model portability, sub-contractor change consent, sub-region pinning), an `exit-plan` requirement before contract signature, a `resilience-testing-pack` scenario test for sub-region failure, a re-ask of the proposed vendor's rank-3 sub-contractor disclosure.
- **Reviewer questions** for the EU subsidiary's risk officer and the accountable executive who signs the preliminary assessment: whether the elevated sub-region and sub-contractor concentrations are within the firm's risk-appetite for the proposed service; whether the group-level concentration with the existing market-data vendor's parent company warrants a separate parent-level briefing; whether the contract conditions adequately address the substitutability gap.

#### Why this scenario matters

Exercises the pre-contract preliminary-assessment cycle (the EU regime's per-arrangement concentration test before contracting or recontracting a critical-or-important function). Tests the chain from `dora-register-builder` to this skill (the register feeds; the concentration view consumes), the chain to `vendor-diligence` (the in-flight pack feeds the sub-contractor chain), the chain to `contract-gap-review` and `exit-plan` for the recommended actions, and the legal-record boundary (the artifact is the draft input; the firm's signed preliminary assessment with legal and compliance sign-off is the legal record). Surfaces the group-level concentration that the legal-entity-only read misses. Names the stressed-substitutability read as the operative test, not the benign-conditions read.

## troubleshooting

### Troubleshooting: concentration-risk-review

Recurring pitfalls. Read before producing the artifact and again before sign-off.

#### Counting at the legal-entity level only

A vendor's brand name does not equal its underlying infrastructure or its parent group. Multiple "different vendors" run on the same hyperscaler, share the same identity-provider, or sit under the same ultimate-parent entity. Concentration must be assessed at the fourth-party and infrastructure level, and at the group-level where a parent entity carries multiple vendor relationships into the firm. Surface the group-level read explicitly when the legal-entity-only read would miss it.

#### Treating spend as the concentration metric

Spend correlates poorly with operational dependency. A high-spend vendor running a non-critical function is less concentration than a low-spend vendor sitting on the critical path of an important business service. Use criticality-weighted count, transaction or operational-volume share where available, function-dependency count, and time-to-substitute as the metrics. Spend can sit in the metadata as a tertiary cross-check, never as the primary metric.

#### Treating multi-region as multi-resilience

Two regions of the same hyperscaler share a control plane, an identity layer, and a billing operation. Diversification gain depends on what fails. The substitutability read names the failure modes the multi-region claim does and does not cover; it does not accept the claim at face value.

#### Ignoring shared-utility concentration

KYC utilities, sanctions-screening vendors, market-data feeds, identity verifiers, transaction-monitoring utilities, and post-trade processors create concentration the firm shares with its peers. Sector-wide concentration shows up as the firm's idiosyncratic risk under stress (every peer is shopping for the same alternative). The technology-stack-shared-utility dimension reads this explicitly; do not let it collapse into the single-vendor row.

#### Skipping the AI-provider dimension

A single foundation-model vendor sitting behind multiple AI use cases is concentration the firm typically did not have eighteen months ago. Add the dimension explicitly, even when the use cases are non-customer-decisioning today. The trajectory matters as much as the current state. Re-test cadence is shorter than the rest of the portfolio.

#### Stopping at rank 1 of the sub-contractor chain

Concentration that lives at rank 2 or rank 3 of a sub-contractor chain is the concentration the firm does not see in a vendor-by-vendor read. Visibility limits are findings, not absences. Where rank-2 disclosure is partial and rank-3 is unknown, surface the limit and route a re-ask to the relevant `vendor-diligence` packs.

#### Producing a list without a substitutability read

Concentration findings without a substitutability read are descriptive, not actionable. Each watch, elevated, or breach finding carries: alternative vendors known, time-to-substitute estimate, contractual portability (chain to `contract-gap-review`), operational substitutability, stressed-substitutability under a wider sector-event scenario where the substitute itself may be in demand. The stressed-substitutability read is the operative test for committee, not the benign-conditions read.

#### Producing a list without single-points-of-failure

The function-level dimension and the cross-dimension read should surface the functions where one failure removes the function entirely with no ready substitute. A concentration view without an SPOF section does not give the committee what it needs to decide.

#### Treating the artifact as the legal record

In EU pre-contract preliminary-assessment cycles under DORA Article 29, the firm's signed assessment is the legal artifact and requires legal and compliance sign-off. This skill produces the draft input. Do not let the draft become the signed assessment by quiet substitution; the sign-off step is part of the workflow.

#### Filling register gaps with inferred entries

Where the source register is incomplete, the analysis is scoped to the usable subset and the limitation is a data-quality caveat. Filling gaps with inferred entries (a vendor "must have" a particular sub-contractor because the market pattern suggests it) is a defect. Inference is fine in the substitutability read, where it is named as inference; it is not fine in the dimension distributions where it gets read as fact.

#### Setting criticality in this skill

Criticality is consumed from `criticality-assessment`, not set here. A register where most arrangements carry `criticality = unknown` is not yet usable for concentration; route back to `criticality-assessment` or scope the analysis to the classified subset and name the scoping decision as a caveat.

#### Loading the wrong sector overlay

Institution type and primary regulator constellation determine the sector overlay set. A dual-registrant or a fintech with a sponsor-bank arrangement may load two. Do not collapse to one. Do not load all four "to be safe"; gold-plating the overlay set adds noise without supervisory value.

#### Reading the cyber-overlay rows as a duplicate of vendor-diligence

The cyber-overlay treatment in this skill is the portfolio-level read of how cyber incidents propagate through the concentration map. It is not a duplicate of the per-arrangement cyber-evidence read in `vendor-diligence`. Where the cyber overlay surfaces a concentration finding (identity-provider, EDR, email-security-gateway, CA/PKI, SIEM), the recommended action may chain to a `vendor-diligence` re-run, but the portfolio-level finding lives here.

#### Missing the stressed-substitutability lens

Substitutability under benign conditions and substitutability under sector stress (where the substitute itself is in demand) are not the same test. Many concentration findings have apparent substitutability under benign conditions and weak or absent substitutability under stress. The committee read needs both; the stressed read is usually what drives the recommended actions.

#### Scope creep into per-arrangement work

Where a finding warrants per-arrangement attention (a specific contract gap, a specific exit-plan refresh, a specific re-diligence), the recommended action chains to the relevant skill (`contract-gap-review`, `exit-plan`, `vendor-diligence`). The concentration review does not produce the per-arrangement artifact itself; doing so blurs the boundary and produces overlapping work. Chain, do not duplicate.

#### Confidence-label inflation

The confidence label is `high` only when the source register is complete and recent, the criticality classification is set with evidence backing, fourth-party visibility is at rank 2 or deeper for material arrangements, and the substitutability read is grounded in tested or recently-rehearsed substitution scenarios. `medium` and `low` are normal for first-cycle reviews and for portfolios with thin fourth-party visibility; `unknown` is honest where the firm has not yet resourced the evidence ask.
