# Example: first-cycle Register of Information build for an EU subsidiary of a US bank

## Input

EU subsidiary of a US bank, in DORA scope as a credit institution, building the Register of Information for the first reporting cycle. Inputs supplied: TPRM register export (78 active vendor arrangements), contract repository (the legal-team-curated set of executed contracts), ICT-asset inventory, criticality-assessment outputs for the 14 arrangements where criticality has been formally set, and the firm's existing EBA outsourcing register (EBA/GL/2019/02 §11 register, 22 outsourcing arrangements). Two material ICT third-party arrangements: (1) a hyperscaler IaaS arrangement supporting the core banking platform, and (2) a SWIFT-connectivity managed service for cross-border payments. Both flagged critical-or-important by the firm's own criticality work.

## Output sketch

The skill produces a register record conforming to `schemas/dora-register-entry.schema.json` and a markdown narrative per `templates/default-output.md`. Highlights:

- Scope: one in-scope legal entity (the EU subsidiary), `consolidation_level = individual`, NCA code for the host-state competent authority.
- 78 contractual-arrangement records in `b_01`. Of those: 14 with criticality determined and supported by a `criticality_assessment_record_id`; 64 with `criticality = unknown` and a data-quality finding flagging the gap.
- 71 ICT-third-party-service-provider records in `b_03`. 11 records flagged as a data-quality finding because LEI is missing (mostly long-tail SaaS vendors with no LEI in GLEIF).
- 132 ICT-service records in `b_05`. The hyperscaler arrangement breaks down into 6 ICT services across compute, storage, networking, identity, key management, and data analytics — each with its own ITS-service-type code (mapped from the firm's internal taxonomy; mapping decisions captured in `data_quality_findings.notes`).
- 19 sub-contractor records in `b_06`, all tied to ICT services supporting critical-or-important functions. Three of the 19 carry a `data_quality_findings` row: the hyperscaler's hardware sub-supplier sits as `rank_in_chain = 2` but the data-residency commitments at that rank are not visible in any documentation the firm holds.
- Reconciliation against the existing EBA outsourcing register: 22 entries reconcile to 22 contractual arrangements in `b_01`, but only 18 of the 22 carry the same data-residency value across both registers. Result: `exceptions-noted`.
- Headline data-quality findings: missing LEI on 11 providers; missing `location_of_data_processing` on the SWIFT-connectivity arrangement; sub-contractor visibility at rank 2 of the hyperscaler chain; one critical-or-important arrangement where the criticality flag is set but no `criticality_evidence_record_id` is supplied.
- Reviewer questions for the EU subsidiary's risk officer and the head of vendor management. Open questions for legal on the host-state NCA's expectations for first-cycle data-quality tolerance.

## Why this scenario matters

It exercises the full table chain (`b_01` through `b_07`), the LEI-gap and sub-contractor-chain visibility findings (the two predictable data-quality failure modes for first-cycle builds), and the reconciliation against the EBA outsourcing register that most EU banks will need to perform. It also tests the boundary with `criticality-assessment` (the register consumes criticality, it does not set it) and with `vendor-diligence` (the per-arrangement diligence input), and it surfaces the consolidation question (the EU subsidiary reports individually here; the US parent receives the data but is not the DORA filer).
