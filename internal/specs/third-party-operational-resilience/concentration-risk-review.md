# concentration-risk-review — Phase 1 spec sheet

Plugin: `third-party-operational-resilience`
Phase: 1 (per-skill scoping)
Plan: `docs/plans/2026-05-06-rationalized-plugin-map.md`

## Activation-tuned description

```
Drafts a concentration-risk view across the firm's third-party portfolio: which vendors and fourth parties cluster on a single provider, geography, jurisdiction, or technology stack, and what that concentration implies for resilience, exit, and supervisory posture.

Best for:
- An annual third-party portfolio review where leadership wants the concentration picture across vendors and fourth parties.
- A DORA preparation cycle where Article 29 preliminary assessment of ICT concentration risk is required.
- A specific arrangement is going through diligence and the diligence pack flags concentration as a residual concern (vendor-diligence triggers this skill).
- A regulator information request on cloud, market-data, or shared-utility concentration.

Not the right tool when:
- The firm's third-party register is not populated to a useful level (use dora-register-builder first if DORA is in scope, or rely on the firm's TPRM register).
- The question is a single arrangement's diligence (use vendor-diligence).
- The question is a single arrangement's exit posture (use exit-plan).

Anchored to: Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FRB/FDIC, June 2023) §V ongoing monitoring (concentration considerations) [verify section]; DORA Article 29 preliminary assessment of ICT concentration risk and Article 28(2) proportionality; EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02) §10 risk assessment of outsourcing arrangements (concentration limb) [verify section]; FFIEC IT Handbook — Outsourcing Technology Services concentration considerations [verify section]; BCBS Principles for Operational Resilience (March 2021) interconnections and interdependencies.
```

## Source anchors

- Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FRB/FDIC, June 6, 2023). Concentration is addressed in the planning and ongoing-monitoring sections; firms are expected to consider concentration risk in third-party relationships [verify section].
- OCC Bulletin 2013-29 — concentration framing (predecessor) [verify section].
- FFIEC IT Examination Handbook — Outsourcing Technology Services. Concentration considerations [verify section].
- DORA — Regulation (EU) 2022/2554, Article 29 preliminary assessment of ICT concentration risk at the level of ICT third-party service providers and at sub-contracting level [verify subarticle]. Article 28(2) proportionality. Recital language on critical ICT third-party service providers and the EU-level oversight regime.
- EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02). Risk-assessment guideline addressing concentration risk including with the same provider, group, geographical area [verify section number].
- BCBS Principles for Operational Resilience (March 2021) — interconnections and interdependencies (third-party-dependencies principle).
- FSB papers on third-party dependencies in financial services and on cloud-services concentration (use as background; cite where the question is sector-wide).
- FFIEC inter-agency joint statement on cloud (April 2020) — concentration considerations for cloud usage.

## Sector overlays needed

- `references/sector-overlays/banking.md` — interagency guidance concentration framing; OCC SR-letter approach to large-bank cloud concentration; community-bank fintech-partner concentration via the August 2023 inter-agency joint statement.
- `references/sector-overlays/insurance.md` — NAIC outsourcing model concentration considerations; state department of insurance examination questions on third-party concentration; reinsurance and policy-administration system concentration.
- `references/sector-overlays/capital-markets.md` — Reg SCI concentration on critical SCI systems; market-data provider concentration; central-counterparty / clearing-member concentration; consolidated-tape and exchange-feed concentration.
- `references/sector-overlays/payments-fintech.md` — settlement-network access concentration; rails concentration (FedNow/RTP/ACH/card-networks); BIN-sponsor concentration; banking-as-a-service partner-bank concentration.

## Cross-cutting overlays

- None mandatory at this skill level. Concentration is itself a cross-cutting frame (cyber, privacy, AI all show up as concentration dimensions). Concrete cyber and privacy treatment lives with `vendor-diligence` and `exit-plan`. Concentration of AI providers is treated as a dimension within this skill rather than a separate overlay file.

## Output template named sections

`templates/default-output.md`:

1. Scope and source posture (which vendors, which arrangements, which fourth parties were in scope; data-quality caveats)
2. Concentration dimensions assessed (provider, geography, jurisdiction, technology stack, fourth party, AI provider)
3. Per-dimension findings (each: dimension, distribution, threshold reference, observed posture, severity)
4. Single-points-of-failure identified
5. Cloud concentration view
6. AI-provider concentration view (where applicable)
7. Geographic and jurisdictional concentration view (cross-border data, sub-region concentration)
8. Substitutability read across concentrated dimensions
9. Recommended actions (with the qualifier that this skill drafts; second-line and the operational-resilience committee decide)
10. Reviewer questions
11. Source trace and confidence label

## Structured output fields

Top-level:

- `assessment_id` (string)
- `as_of_date` (string, ISO 8601)
- `scope` (object: `entities`, `arrangements_in_scope_count`, `data_quality_caveats`)
- `dimensions` (array of object: `dimension`, `metric`, `threshold_reference`, `distribution_summary`, `top_concentrations`, `severity` enum)
- `single_points_of_failure` (array of object: `function`, `arrangement_ids`, `rationale`, `severity`)
- `cloud_concentration_view` (object)
- `ai_provider_concentration_view` (object, nullable)
- `geographic_concentration_view` (object)
- `substitutability_read` (string)
- `recommended_actions` (array of object: `action`, `owner_role`, `rationale`)
- `reviewer_questions` (array of string)
- `confidence_label` (enum)
- `source_trace` (array of object)

## Example scenarios (two, public-source-derived)

1. **Annual operational-resilience-committee concentration review for a mid-size US bank.** Inputs: the firm's third-party register, the criticality output for each arrangement, the cloud-region map, and the fourth-party inventory where available. Anchored to: interagency guidance (June 2023) [verify section]; FFIEC inter-agency cloud joint statement (April 2020); FFIEC IT Handbook Outsourcing booklet [verify section]. The output identifies that 60-plus percent of critical and important arrangements depend on a single hyperscaler region for primary compute, that three critical arrangements share the same SaaS-billing platform as a hidden fourth-party dependency, and that the firm's KYC utility usage concentrates with a single vendor whose own infrastructure sits on the same hyperscaler. Surfaces single-points-of-failure for committee review.

2. **DORA Article 29 preliminary assessment for an EU subsidiary of a US insurer.** Inputs: the firm's DORA register of information output, the criticality flags, and the sub-outsourcing chain. Anchored to: DORA Article 29 [verify subarticle]; EBA outsourcing guidelines [verify section]; NAIC outsourcing model for the parent's other obligations. The output identifies that all three critical-or-important-function ICT services concentrate on the same ICT third-party service provider's same EU sub-region, that two of the three are sub-outsourced to the same downstream processor, and that the EU oversight-framework lens (DORA critical ICT third-party service provider designation) may apply. Surfaces this as a finding for the EU subsidiary's risk officer and the US-parent chief risk officer; recommends a follow-up cycle with `exit-plan` and `resilience-testing-pack` to test substitutability assumptions.

## Common pitfalls

1. **Counting at the legal-entity level only.** A vendor's brand-name does not equal its underlying infrastructure. Many "different vendors" run on the same hyperscaler and the same sub-region. Concentration must be assessed at the fourth-party and infrastructure level too.
2. **Ignoring shared-utility concentration.** KYC utilities, sanctions screening, market-data feeds, and identity verifiers create concentration the firm shares with its peers. Sector-wide concentration shows up as the firm's idiosyncratic risk.
3. **Treating multi-region as multi-resilience.** Two regions of the same hyperscaler share a control plane, an identity layer, and a billing operation. Diversification gain depends on what fails.
4. **Using vendor-spend as the concentration metric.** Spend correlates poorly with operational dependency. Use criticality, transaction volume, and time-to-substitute as the metrics.
5. **Skipping the AI-provider dimension.** A single foundation-model vendor across many AI use cases is a concentration the firm did not have a year ago. Add this dimension explicitly.
6. **Producing a list without a recommended-actions or single-points-of-failure section.** Concentration findings without a substitutability read are descriptive, not useful.
7. **Treating the output as a final regulatory determination.** This is a draft view for the operational-resilience committee. The DORA Article 29 assessment is the legal artifact and requires legal and compliance sign-off.
