---
name: criticality-assessment
description: |
  Sets the criticality tier of a single third-party arrangement and ties it to the firm's important business service, recovery time and recovery point objectives, customer impact, regulatory impact, operational substitutability, and concentration considerations. Produces the upstream record that vendor-diligence, contract-gap-review, exit-plan, concentration-risk-review, and dora-register-builder consume. Audience: head of TPRM, head of operational resilience, business owner.

  Best for:
  - A new arrangement is being proposed and the firm needs the tier set before kicking off vendor-diligence.
  - An annual third-party portfolio review where tiers are stale or inconsistently applied.
  - A DORA preparation cycle that requires a critical-or-important-function flag for every ICT arrangement.
  - A material change to the service or to the firm's important-business-service map triggers a re-tier.

  Not the right tool when:
  - The firm has not yet defined the important business service the arrangement supports (the criticality call depends on the IBS read; do that first or default and flag).
  - The portfolio question is concentration across vendors (use concentration-risk-review).
  - The arrangement is a non-ICT third party with no information, technology, or business-process dependency the firm relies on.
  - Full diligence is needed (use vendor-diligence; this skill is the upstream input).
argument-hint: "[arrangement: vendor name, service, supported business process, IBS if known]"
---

# Criticality assessment

A criticality assessment is what second-line produces so the firm can set a defensible tier on a third-party arrangement and feed that tier into the rest of the lifecycle. The tier is the single field every downstream skill consumes. Get it wrong and vendor-diligence runs at the wrong depth, contract-gap-review reads against the wrong clauses, exit-plan never gets built, and the DORA register entry carries the wrong flag. The skill stops at the recommendation. The named approver, head of TPRM or operational-risk committee per firm policy, decides.

This skill produces the assessment as a markdown artifact (`templates/default-output.md` shape) and a structured record (`schemas/criticality-assessment.schema.json`) that downstream skills consume. The record is upstream of `vendor-diligence` (which reads the `criticality` field), and is read by `contract-gap-review`, `exit-plan`, `concentration-risk-review`, and `dora-register-builder` for the same reasons.

## Ask first

Before drafting, get plain answers to four things. Most engagements answer them quickly; if not, default and flag.

- **What business process does this arrangement support, and which important business service does that process sit on.** Sourced from the firm's IBS map. If the firm has no IBS map, work against the candidate IBS list in the loaded sector overlay and note the absence; do not block.
- **What is the firm's impact tolerance for that IBS.** Recovery time and recovery point come from the IBS impact analysis, not from the contract. The vendor commitment is the ceiling on what the vendor delivers; the firm tolerance is the test.
- **What is the firm's regulatory profile.** Institution type and primary regulators. The DORA flag and the UK SS2/21 flag are recorded only for entities in those perimeters; otherwise `not-in-scope`.
- **What is the engagement type.** Pre-onboarding, annual recertification, off-cycle trigger, material-change re-review, post-incident re-review, IBS-change re-review, contract-renewal re-review. Each carries a different decision-forum context.

When `engagement-scope` is supplied, the skill consumes it (institution type, sector overlay set, cross-cutting overlay set, persona, source posture). When it is not, ask the four questions and default to public posture if the practitioner declines. Note in the assessment that scope was not formalised; do not silently apply a default sector overlay.

## How the assessment gets built

The assessment has the same spine across arrangement types. A senior reviewer fills it in roughly in the order the engagement and the available evidence allow, not in a lockstep sequence. There is, however, a real dependency: the IBS read and the impact tolerance must land before the recovery-objective and operational-impact reads can be tested against firm tolerance. Do the IBS read first; everything else can be filled in any order the conversation surfaces.

The frame opens with the arrangement and the supported process. Vendor and contracting entity, concise service description, business process the arrangement supports, and the firm's named IBS where the arrangement sits on the IBS chain. Customer-facing position: on the IBS critical chain, supporting an IBS but off the critical chain, or non-IBS. The IBS read drives the rest of the assessment; an arrangement on the IBS critical chain is rarely below `important`, and many sit at `critical`.

Recovery time and recovery point objectives are read against firm tolerance, not vendor commitment. Firm tolerance comes from the IBS impact analysis and is the test the vendor must meet. The vendor commitment from the contract or evidence pack is the ceiling on what the vendor delivers. `recovery_meets_firm_tolerance` is `yes` only when the commitment meets the tolerance; a `no` or `partial` is itself a finding for `contract-gap-review` and a precondition for `vendor-diligence` to surface in operational-resilience evidence.

Customer impact, regulatory impact, and operational impact each get a severity read with a short narrative. Customer impact names the affected populations and the harm modes (financial loss, fairness, accessibility, complaint exposure, fraud exposure, privacy breach, fiduciary breach). Regulatory impact names the regimes intersected and the notification triggers a sustained outage could fire. Operational impact reads substitutability (`easy | moderate | hard | none`), the realistic time-to-restore under a forced cutover, and whether a manual workaround is viable for the full tolerance window. The manual-workaround test is load-bearing for the tier call: without it the substitutability read is incomplete and the tier is unreliable.

Data scope names the categories the arrangement touches (NPI, PHI, PCI, model prompts, model outputs, training data, books-and-records, logs-only) and whether cross-border flows apply. Concentration considerations raise the flag here (hyperscaler region, sponsor-bank, BIN sponsor, foundation-model vendor, transfer agent, custodian, claims TPA, fund accountant); the portfolio analysis lives downstream in `concentration-risk-review`.

The tier call follows from the reads above. The four values are `critical | important | not-critical | unknown`. The rationale must name the criteria that drove the call; tier without rationale is a documentation defect that propagates. Cite sources by file path (`references/source-anchors.md` and the loaded sector overlay) rather than restating excerpts in the body.

The DORA critical-or-important-function flag is a separate call from the firm's own tier. Where DORA applies to the entity, record `yes`, `no`, or both calls separately if multiple entities are affected, with rationale. The criteria differ from the firm's own tier; the EBA-defined notion of critical or important function applies its own tests. `not-in-scope` is reserved for entities outside the DORA perimeter; `no` means DORA applies but the arrangement does not meet the EBA criticality threshold (the arrangement may still belong in the DORA register as an in-scope ICT service, with the flag set to `no`). The UK SS2/21 IBS flag follows the same pattern for UK-licensed firms.

The owner is named by role, not person. For a `critical` arrangement the owner is usually the IBS owner with the head of TPRM as second-line co-owner; the approver is the operational-risk committee or equivalent per firm policy. For `important`, owner is typically the business owner SVP and approver the TPRM forum or business-unit risk forum. For `not-critical`, line management owns and approves under the firm's policy.

The assessment closes with reviewer questions clustered for the forum that decides, the next-review trigger (annual cycle date, contract-renewal trigger, IBS-change trigger, material-service-change trigger, incident-driven re-review condition, and for AI vendors the model-version-change trigger), and the source trace. The assessment does not approve the tier; the named approver decides.

## Quality bar

Holds across every assessment regardless of arrangement type, audience, or render format. Every material claim cites a source from `references/source-anchors.md` (or a loaded overlay) by path. Unsupported claims are marked `[evidence needed]`. Section references that cannot be confirmed get `[verify section]` rather than fabricated. Source evidence, vendor commitment, public-source obligation, generated inference, and open legal or compliance question stay distinguishable in the assessment. No named institutions in narrative unless they are public defendants in a finalised enforcement action with a published consent order. The assessment stops at the recommendation. The vendor's claimed RTO/RPO is not the test, anywhere; firm tolerance from the IBS impact analysis is the test.

## Adaptation

Flexes by engagement. Assessment depth and length scale to the proposed tier and to whether the engagement is in DORA or UK SS2/21 scope. A `not-critical` arrangement collapses several sections to a paragraph; a `critical` or DORA-in-scope arrangement runs full depth with reviewer questions clustered for the operational-risk committee (or AI risk committee for AI vendors, fund board for registered funds). The sector overlay set drives which `references/sector-overlays/<sector>.md` is loaded; a dual-registrant or BaaS arrangement may load two. Source posture (public-only, public-plus-firm-policy, public-plus-firm-policy-plus-system-of-record-evidence, connector-aware) drives the evidence ask, particularly for the IBS map and the impact-tolerance read. Render format (Word, Excel, PowerPoint, Markdown) follows the workflow.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays/banking.md`, `insurance.md`, `capital-markets.md`, `payments-fintech.md` — sector-specific criticality criteria loaded per engagement-scope.
- `references/firm-overlay.md` — firm-installed IBS map, impact-tolerance taxonomy, criticality-policy thresholds, and decision forums beyond the regulatory baseline; consumed when present.
- `templates/default-output.md` — assessment template.
- `schemas/criticality-assessment.schema.json` — structured-output contract for downstream consumption.
- `examples/` — core-banking SaaS at a community bank (criticality = critical); HRIS payroll at an EU subsidiary of a US insurer (criticality = important, DORA flag = no, in-scope-of-register).
- `TROUBLESHOOTING.md` — recurring pitfalls (spend-as-criticality, vendor-commitment-as-tolerance, procurement-category-as-tier, manual-workaround skip, DORA-flag-collapsed-with-firm-tier).

The plugin-level shared references (`references/source-map.md`, `references/policy-control-library.md`, `references/review-gates.md`) sit at the plugin root and are consulted alongside the skill-level files.

## Output

The deliverable is the criticality assessment. Default to drafting against `templates/default-output.md`. Render as Word, Excel, PowerPoint, or Markdown when the audience or workflow asks for it (a TPRM-cycle batch may want a workbook; an operational-risk-committee read may want a deck or memo). Produce the structured record at `schemas/criticality-assessment.schema.json` when downstream automation or a registered consumer needs it.

Downstream consumers: `vendor-diligence` reads the `criticality` field to set diligence depth; `contract-gap-review` reads the recovery-objective gap and the regulatory-impact regimes to set the clause-coverage test; `exit-plan` reads `tier`, `important_business_service`, `data_scope`, and `operational_impact` to set transition mechanics; `concentration-risk-review` reads the `concentration_considerations` flag to drive portfolio analysis; `dora-register-builder` reads the structured fields, including the `dora_critical_or_important_function` flag, for ICT-third-party register entries where DORA applies.

When the structured record is produced, treat the schema as a downstream contract: additive changes only. Add fields, do not rename or repurpose them. A breaking change is a versioned migration with the downstream skills told in advance.
