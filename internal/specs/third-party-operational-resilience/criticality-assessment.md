# criticality-assessment — Phase 1 spec sheet

Plugin: `third-party-operational-resilience`
Phase: 1 (per-skill scoping)
Plan: `docs/plans/2026-05-06-rationalized-plugin-map.md`

## Activation-tuned description

```
Drafts a criticality tier for a single third-party arrangement and ties it to the firm's important business service, recovery time and recovery point objectives, customer impact, regulatory impact, and concentration considerations. Produces the input that vendor-diligence, contract-gap-review, exit-plan, and dora-register-builder consume.

Best for:
- A new vendor arrangement is being proposed and the firm needs the criticality tier before kicking off diligence.
- An annual third-party portfolio review where criticality tiers are stale or inconsistently set.
- A DORA preparation cycle that requires a critical-or-important-function flag for every ICT arrangement.

Not the right tool when:
- The firm has not yet defined the important business service the arrangement supports (the criticality call is dependent on that).
- The portfolio question is concentration across vendors (use concentration-risk-review).
- The arrangement is a non-ICT third party with no information, technology, or business-process dependency.

Anchored to: Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FRB/FDIC, June 2023) §II risk-based approach and §III planning [verify section]; FFIEC IT Examination Handbook — Business Continuity Management booklet, business-impact-analysis section [verify section]; DORA Article 28 (general principles) and the EBA-defined notion of "critical or important function"; PRA SS2/21 (operational resilience) and SS1/21 (impact tolerances) for UK overlay reference.
```

## Source anchors

- Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FRB/FDIC, June 6, 2023). Risk-based approach and criticality framing [verify section]. The guidance does not prescribe a fixed tier scheme; it expects firms to apply criticality proportionate to risk.
- OCC Bulletin 2013-29 — predecessor framing for "critical activities" [verify section].
- FFIEC IT Examination Handbook — Business Continuity Management booklet. Business impact analysis (BIA) section, RTO/RPO definitions [verify section]. Use as the anchor for the RTO/RPO portion of the criticality output.
- FFIEC IT Examination Handbook — Outsourcing Technology Services booklet, risk-assessment section [verify section].
- DORA — Regulation (EU) 2022/2554, Article 28 general principles, and the concept of "critical or important function" referenced throughout DORA. Article 6 (ICT risk management framework) for the link from ICT risk to important functions [verify subarticle].
- EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02). Definition of "critical or important function" [verify section number]; assessment criteria for criticality.
- UK PRA SS1/21 (impact tolerances) and SS2/21 (operational resilience). Reference only for the UK overlay; the US-deep default uses the interagency-guidance frame.
- BCBS Principles for Operational Resilience (March 2021) for the cross-jurisdictional concept of important business services.

## Sector overlays needed

All four. Criticality is sector-shaped because the "important business service" definition is sector-shaped.

- `references/sector-overlays/banking.md` — payments, deposit-taking, lending, custody as candidate important business services; OCC heightened-standards expectations; community-bank vs large-bank proportionality.
- `references/sector-overlays/insurance.md` — claims handling, policy administration, underwriting, premium collection as candidate important business services; NAIC outsourcing model; state guaranty-fund and policyholder-protection considerations.
- `references/sector-overlays/capital-markets.md` — order management, execution, clearing, settlement, market-data distribution; Reg SCI critical-systems definitions; CFTC system-safeguards; FINRA business-continuity expectations.
- `references/sector-overlays/payments-fintech.md` — settlement-network access, BIN sponsorship, rails-connectivity (FedNow, RTP, ACH, card networks), KYC/AML utilities; payments-network rules.

## Cross-cutting overlays

- None mandatory at this skill level. Cyber, privacy, and conduct lenses inform the criticality tier (a vendor handling NPI on the customer-facing path may be "important" even at low transaction volume) but the overlays themselves live with `vendor-diligence` and `exit-plan`.

## Output template named sections

`templates/default-output.md`:

1. Service in scope
2. Business process supported (mapped to the firm's important business service if applicable)
3. Recovery time objective (RTO) — firm tolerance and vendor commitment
4. Recovery point objective (RPO) — firm tolerance and vendor commitment
5. Customer impact (financial, fairness, accessibility, complaint exposure)
6. Regulatory impact (reportable, supervisory, disclosure, market-conduct)
7. Operational impact (substitutability, time-to-restore, manual workaround viability)
8. Data scope (categories of data the arrangement touches; cross-border)
9. Concentration considerations (sector concentration, geographic concentration, fourth-party concentration; pointer to `concentration-risk-review`)
10. Tier (critical / important / not critical / unknown — with rationale and the named criteria that justify the tier)
11. DORA flag (critical-or-important-function: yes/no/not in scope; with rationale)
12. UK SS2/21 flag if applicable (important-business-service mapping)
13. Owner (role, not person)
14. Reviewer questions
15. Source trace and confidence label

## Structured output fields

Anchor: `schemas/vendor.schema.json` (criticality block; the schema in this plugin already carries `criticality` enum). The full criticality artifact is produced as a structured object that feeds `vendor-diligence` and `dora-register-builder`.

Fields (type, purpose):

- `arrangement_id` (string) — stable ID
- `service_in_scope` (string)
- `business_process_supported` (string)
- `important_business_service` (string, nullable) — the firm's named IBS this arrangement supports
- `rto_tolerance` (string) — firm tolerance, e.g., "4h"
- `rto_vendor_commitment` (string) — vendor commitment from contract or evidence
- `rpo_tolerance` (string)
- `rpo_vendor_commitment` (string)
- `customer_impact` (object: `severity` enum `low|medium|high|severe`, `populations`, `harm_modes`)
- `regulatory_impact` (object: `severity`, `regimes` array, `notification_triggers` array)
- `operational_impact` (object: `substitutability` enum `easy|moderate|hard|none`, `time_to_restore`, `manual_workaround_viable` boolean)
- `data_scope` (array of string)
- `concentration_considerations` (string) — pointer to `concentration-risk-review` output if available
- `tier` (enum: `critical | important | not-critical | unknown`)
- `tier_rationale` (string)
- `dora_critical_or_important_function` (enum: `yes | no | not-in-scope`)
- `uk_ss2_21_ibs_flag` (enum: `yes | no | not-in-scope`)
- `owner` (string) — role
- `reviewer_questions` (array of string)
- `confidence_label` (enum)
- `source_trace` (array of object)

## Example scenarios (two, public-source-derived)

1. **Core-banking SaaS for a community bank's deposit ledger.** Inputs: the firm's important-business-service register (deposits identified as IBS), the contracted RTO/RPO from the vendor (RTO 8h, RPO 1h), the firm's tolerance (RTO 4h, RPO 15 min). Anchored to: interagency guidance (June 2023); FFIEC BCM booklet BIA section [verify section]. The output sets the tier to "critical", flags the gap between vendor commitment and firm tolerance as a finding for `contract-gap-review`, and notes that DORA does not apply (US-only firm, no EU nexus).

2. **HRIS SaaS supporting payroll for an EU subsidiary of a US insurer.** Inputs: the firm's IBS register (payroll not an IBS but reputational and regulatory exposure exists), the vendor's certifications, and the EU nexus. Anchored to: DORA Article 28 [verify subarticle]; EBA outsourcing guidelines [verify section]; NAIC outsourcing model. The output sets the tier to "important", marks the DORA critical-or-important-function flag as "no" (because payroll for a small subsidiary does not meet the EBA criticality threshold; rationale recorded), and notes the arrangement is still in scope for the DORA register because it is an ICT service to a financial entity. Reviewer questions are surfaced for the chief operating officer and the EU subsidiary's risk officer.

## Common pitfalls

1. **Using a vendor-spend or vendor-headcount proxy for criticality.** Spend is not impact. A low-spend vendor on the customer-facing path can be critical.
2. **Setting RTO/RPO to the vendor's commitment rather than the firm's tolerance.** The firm's tolerance comes from the IBS impact analysis, not the contract.
3. **Treating "DORA critical or important function" and "interagency-guidance critical activity" as identical.** The criteria differ. Record both calls separately if both regimes apply.
4. **Skipping the manual-workaround question.** The criticality call depends on whether the firm can keep the IBS running without the vendor for the tolerance window.
5. **Letting the procurement category drive the tier.** "IT services" is not a tier. The tier is set by impact on the IBS, customer, and regulator, not by the contract category.
6. **Setting the tier and walking away.** Criticality must be revisited at re-contract, on material change to the service, on material change to the IBS, and on annual recertification. Note the next-review trigger in the output.
