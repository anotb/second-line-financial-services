# Troubleshooting: concentration-risk-review

Recurring pitfalls. Read before producing the artifact and again before sign-off.

## Counting at the legal-entity level only

A vendor's brand name does not equal its underlying infrastructure or its parent group. Multiple "different vendors" run on the same hyperscaler, share the same identity-provider, or sit under the same ultimate-parent entity. Concentration must be assessed at the fourth-party and infrastructure level, and at the group-level where a parent entity carries multiple vendor relationships into the firm. Surface the group-level read explicitly when the legal-entity-only read would miss it.

## Treating spend as the concentration metric

Spend correlates poorly with operational dependency. A high-spend vendor running a non-critical function is less concentration than a low-spend vendor sitting on the critical path of an important business service. Use criticality-weighted count, transaction or operational-volume share where available, function-dependency count, and time-to-substitute as the metrics. Spend can sit in the metadata as a tertiary cross-check, never as the primary metric.

## Treating multi-region as multi-resilience

Two regions of the same hyperscaler share a control plane, an identity layer, and a billing operation. Diversification gain depends on what fails. The substitutability read names the failure modes the multi-region claim does and does not cover; it does not accept the claim at face value.

## Ignoring shared-utility concentration

KYC utilities, sanctions-screening vendors, market-data feeds, identity verifiers, transaction-monitoring utilities, and post-trade processors create concentration the firm shares with its peers. Sector-wide concentration shows up as the firm's idiosyncratic risk under stress (every peer is shopping for the same alternative). The technology-stack-shared-utility dimension reads this explicitly; do not let it collapse into the single-vendor row.

## Skipping the AI-provider dimension

A single foundation-model vendor sitting behind multiple AI use cases is concentration the firm typically did not have eighteen months ago. Add the dimension explicitly, even when the use cases are non-customer-decisioning today. The trajectory matters as much as the current state. Re-test cadence is shorter than the rest of the portfolio.

## Stopping at rank 1 of the sub-contractor chain

Concentration that lives at rank 2 or rank 3 of a sub-contractor chain is the concentration the firm does not see in a vendor-by-vendor read. Visibility limits are findings, not absences. Where rank-2 disclosure is partial and rank-3 is unknown, surface the limit and route a re-ask to the relevant `vendor-diligence` packs.

## Producing a list without a substitutability read

Concentration findings without a substitutability read are descriptive, not actionable. Each watch, elevated, or breach finding carries: alternative vendors known, time-to-substitute estimate, contractual portability (chain to `contract-gap-review`), operational substitutability, stressed-substitutability under a wider sector-event scenario where the substitute itself may be in demand. The stressed-substitutability read is the operative test for committee, not the benign-conditions read.

## Producing a list without single-points-of-failure

The function-level dimension and the cross-dimension read should surface the functions where one failure removes the function entirely with no ready substitute. A concentration view without an SPOF section does not give the committee what it needs to decide.

## Treating the artifact as the legal record

In EU pre-contract preliminary-assessment cycles under DORA Article 29, the firm's signed assessment is the legal artifact and requires legal and compliance sign-off. This skill produces the draft input. Do not let the draft become the signed assessment by quiet substitution; the sign-off step is part of the workflow.

## Filling register gaps with inferred entries

Where the source register is incomplete, the analysis is scoped to the usable subset and the limitation is a data-quality caveat. Filling gaps with inferred entries (a vendor "must have" a particular sub-contractor because the market pattern suggests it) is a defect. Inference is fine in the substitutability read, where it is named as inference; it is not fine in the dimension distributions where it gets read as fact.

## Setting criticality in this skill

Criticality is consumed from `criticality-assessment`, not set here. A register where most arrangements carry `criticality = unknown` is not yet usable for concentration; route back to `criticality-assessment` or scope the analysis to the classified subset and name the scoping decision as a caveat.

## Loading the wrong sector overlay

Institution type and primary regulator constellation determine the sector overlay set. A dual-registrant or a fintech with a sponsor-bank arrangement may load two. Do not collapse to one. Do not load all four "to be safe"; gold-plating the overlay set adds noise without supervisory value.

## Reading the cyber-overlay rows as a duplicate of vendor-diligence

The cyber-overlay treatment in this skill is the portfolio-level read of how cyber incidents propagate through the concentration map. It is not a duplicate of the per-arrangement cyber-evidence read in `vendor-diligence`. Where the cyber overlay surfaces a concentration finding (identity-provider, EDR, email-security-gateway, CA/PKI, SIEM), the recommended action may chain to a `vendor-diligence` re-run, but the portfolio-level finding lives here.

## Missing the stressed-substitutability lens

Substitutability under benign conditions and substitutability under sector stress (where the substitute itself is in demand) are not the same test. Many concentration findings have apparent substitutability under benign conditions and weak or absent substitutability under stress. The committee read needs both; the stressed read is usually what drives the recommended actions.

## Scope creep into per-arrangement work

Where a finding warrants per-arrangement attention (a specific contract gap, a specific exit-plan refresh, a specific re-diligence), the recommended action chains to the relevant skill (`contract-gap-review`, `exit-plan`, `vendor-diligence`). The concentration review does not produce the per-arrangement artifact itself; doing so blurs the boundary and produces overlapping work. Chain, do not duplicate.

## Confidence-label inflation

The confidence label is `high` only when the source register is complete and recent, the criticality classification is set with evidence backing, fourth-party visibility is at rank 2 or deeper for material arrangements, and the substitutability read is grounded in tested or recently-rehearsed substitution scenarios. `medium` and `low` are normal for first-cycle reviews and for portfolios with thin fourth-party visibility; `unknown` is honest where the firm has not yet resourced the evidence ask.
