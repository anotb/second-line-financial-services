# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## critical-cloud-bank

### Example: first-cycle Register of Information build for an EU subsidiary of a US bank

#### Input

EU subsidiary of a US bank, in DORA scope as a credit institution, building the Register of Information for the first reporting cycle. Inputs supplied: TPRM register export (78 active vendor arrangements), contract repository (the legal-team-curated set of executed contracts), ICT-asset inventory, criticality-assessment outputs for the 14 arrangements where criticality has been formally set, and the firm's existing EBA outsourcing register (EBA/GL/2019/02 §11 register, 22 outsourcing arrangements). Two material ICT third-party arrangements: (1) a hyperscaler IaaS arrangement supporting the core banking platform, and (2) a SWIFT-connectivity managed service for cross-border payments. Both flagged critical-or-important by the firm's own criticality work.

#### Output sketch

The skill produces a register record conforming to `schemas/dora-register-entry.schema.json` and a markdown narrative per `templates/default-output.md`. Highlights:

- Scope: one in-scope legal entity (the EU subsidiary), `consolidation_level = individual`, NCA code for the host-state competent authority.
- 78 contractual-arrangement records in `b_01`. Of those: 14 with criticality determined and supported by a `criticality_assessment_record_id`; 64 with `criticality = unknown` and a data-quality finding flagging the gap.
- 71 ICT-third-party-service-provider records in `b_03`. 11 records flagged as a data-quality finding because LEI is missing (mostly long-tail SaaS vendors with no LEI in GLEIF).
- 132 ICT-service records in `b_05`. The hyperscaler arrangement breaks down into 6 ICT services across compute, storage, networking, identity, key management, and data analytics — each with its own ITS-service-type code (mapped from the firm's internal taxonomy; mapping decisions captured in `data_quality_findings.notes`).
- 19 sub-contractor records in `b_06`, all tied to ICT services supporting critical-or-important functions. Three of the 19 carry a `data_quality_findings` row: the hyperscaler's hardware sub-supplier sits as `rank_in_chain = 2` but the data-residency commitments at that rank are not visible in any documentation the firm holds.
- Reconciliation against the existing EBA outsourcing register: 22 entries reconcile to 22 contractual arrangements in `b_01`, but only 18 of the 22 carry the same data-residency value across both registers. Result: `exceptions-noted`.
- Headline data-quality findings: missing LEI on 11 providers; missing `location_of_data_processing` on the SWIFT-connectivity arrangement; sub-contractor visibility at rank 2 of the hyperscaler chain; one critical-or-important arrangement where the criticality flag is set but no `criticality_evidence_record_id` is supplied.
- Reviewer questions for the EU subsidiary's risk officer and the head of vendor management. Open questions for legal on the host-state NCA's expectations for first-cycle data-quality tolerance.

#### Why this scenario matters

It exercises the full table chain (`b_01` through `b_07`), the LEI-gap and sub-contractor-chain visibility findings (the two predictable data-quality failure modes for first-cycle builds), and the reconciliation against the EBA outsourcing register that most EU banks will need to perform. It also tests the boundary with `criticality-assessment` (the register consumes criticality, it does not set it) and with `vendor-diligence` (the per-arrangement diligence input), and it surfaces the consolidation question (the EU subsidiary reports individually here; the US parent receives the data but is not the DORA filer).

## data-vendor-asset-manager

### Example: annual refresh review for an EU asset manager's existing register

#### Input

EU UCITS management company, in DORA scope as an asset manager, completing the annual refresh of the Register of Information after the first cycle landed last year. Inputs supplied: prior-year register submission (extracted from the firm's submission archive), the year's vendor-onboarding log, contract amendments executed during the year, the criticality re-assessment outputs for the year, and the consolidated ICT third-party register from the parent group (the firm is part of a wider asset-management group). Two specific scenarios in focus: (1) a market-data vendor used for portfolio valuation across 12 funds, where the vendor restructured during the year and a new contracting entity is in place; (2) an alternative-data vendor newly onboarded during the year, supplying sustainability-screening data that influences fund construction.

#### Output sketch

The skill produces an updated register record and a refresh narrative. Highlights:

- Year-on-year movement: 9 new contractual arrangements added, 4 discontinued, 2 re-classified upward in criticality (one moved from `not-critical-or-important` to `critical-or-important`). The re-classifications and additions are surfaced as their own narrative section because the supervisory dialogue is interested in movement, not just stock.
- Market-data-vendor change: the prior-year `b_03` record carried the legacy contracting entity LEI. The refresh produces a new `b_03` record with the post-restructure LEI, and a `b_01` record with the new contractual-arrangement reference number. The relational update propagates through `b_02` (links updated), `b_05` (12 ICT-service records re-pointed), and `b_07` (the 12 funds making use of the service stay the same but the arrangement reference changes). The contractual-arrangement reference number history is captured in `linked_arrangement_references` so the year-on-year audit trail holds.
- Alternative-data-vendor onboarding: new records across `b_01`, `b_02`, `b_03`, `b_04` (the sustainability-screening function reference), `b_05`, and `b_07`. Sub-contractor visibility (`b_06`) is `partial` because the vendor's data-collection sub-processors are disclosed at sector level only, not entity level. Recorded as a data-quality finding.
- Re-classified arrangement: the prior-year register had a custodian-feed integration as `not-critical-or-important`. This year's criticality re-assessment moves it to `critical-or-important` because of the operational-tolerance reset for fund net-asset-value publication. The skill flags that the re-classification is not supported by a dated `criticality_assessment_record_id` for the new tier and surfaces the gap as the headline finding (use `criticality-assessment` to remediate before submission).
- Reconciliation against the parent group's consolidated register: the firm reports `consolidation_level = individual` to its NCA but the parent maintains a consolidated view; differences in counterpart taxonomy and ICT-service-type mapping surfaced as exceptions. Decision-flagged for the parent group's DORA programme lead.

#### Why this scenario matters

The refresh case is structurally different from the first-cycle build. It tests the year-on-year delta logic, the relational-integrity preservation across vendor-entity changes (the LEI moves but the substantive arrangement persists), the criticality re-classification trail (every up-classification needs an evidence pointer), and the parent-group consolidation interplay that EU subsidiaries of larger groups must reconcile each year. It also tests the boundary with sector overlay (asset manager vs bank: ESMA-coordinated approach for investment firms; UCITS depositary considerations show up via the depositary as an in-scope counterparty).

## troubleshooting

### Troubleshooting: dora-register-builder

Recurring pitfalls in DORA Register of Information builds, with the corrective posture for each. Sources are in `references/source-anchors.md`.

#### EBA outsourcing register treated as drop-in DORA register data

The EBA outsourcing register (EBA/GL/2019/02 §11 [verify section]) is a different schema from the DORA Register of Information. Different columns, different relational structure (the DORA register is identifier-driven and links across tables; the outsourcing register is a flatter list), different scope (DORA covers all ICT third-party arrangements; the outsourcing register covers outsourcing as defined by EBA/GL/2019/02).

Map, do not copy. The mapping decisions and any conflicts (data-residency value differs across the two registers; sub-contractor list shorter on one side) are findings, not silent overwrites. Capture them in `data_quality_findings` and `reconciliations`.

#### Missing LEI or other identifier values

The register schema is identifier-driven; missing identifiers break relational integrity and the supervisory pipeline. Long-tail SaaS vendors and small specialist providers often lack a GLEIF-issued LEI. Record `provider_identifier` as the best available (EUID, national identifier) with `identifier_type` set, and raise a `data_quality_findings` entry. Do not invent identifiers. Do not leave the field blank to "fix in submission".

#### Firm-internal service-type taxonomy used instead of the ITS ICT-service-type codes

The ITS prescribes the ICT-service-type taxonomy for `b_05.ict_service_type_code` [verify ITS taxonomy reference in source-anchors.md]. The firm's internal procurement or TPRM service-type taxonomy will not align one-for-one. Build the mapping once, document the mapping decisions (especially the lossy ones), and reuse. Mapping decisions are part of the source trace, not metadata to be discarded.

#### "Critical or important function" set without dated criticality evidence

The criticality flag drives downstream supervisory consequences (sub-contractor-chain visibility expectations, NCA scrutiny on exit posture, oversight-framework relevance for designated CTPPs). Setting the flag without a `criticality_evidence_record_id` pointing to a dated `criticality-assessment` output is a finding even when the flag is correct. Run `criticality-assessment` first; consume the output here.

#### Stopping at first-tier ICT third party

For ICT services supporting critical or important functions, sub-contractor-chain visibility is required. Stopping at the contracted ICT third party (rank 1) and treating sub-contractors at rank 2+ as out of scope is a frequent gap. The EBA RTS on sub-contracting (where in force) and DORA Article 30 sub-outsourcing provisions [verify article number] set the expectation.

When the chain is genuinely opaque past rank 1 because the vendor will not disclose, that is itself a finding and a contract-gap (route to `contract-gap-review`), not an absence to be silently accepted.

#### Data-processing-location field treated as nice-to-have

Cross-border data flows are a supervisory focus, especially data leaving the EEA. The `location_of_data_at_rest` and `location_of_data_processing` fields are mandatory for many records [verify ITS column codes] and material for the concentration view (consumed by `concentration-risk-review`). A record with a single country code where the actual hyperscaler footprint spans multiple regions is wrong, not minimal.

#### Intra-group arrangements confused with third-party arrangements

Intra-group arrangements remain reportable under DORA but are flagged differently via `intra_group_flag` in `b_02`. Treating them as full third-party arrangements without the flag, or omitting them as "not third party", both fail the schema. The intra-group flag is the supervisory expectation; use it.

#### Producing the register without a data-quality findings section

A submission-quality register includes the firm's own quality view. Supervisors expect the firm to know its own gaps; a clean-looking register with no `data_quality_findings` reads as either complete (rare for first-cycle builds) or unaware (more common). The findings section is an asset in supervisory dialogue, not an admission of failure.

#### Treating the skill output as the submission

This skill drafts. The submission is a regulated filing requiring legal, compliance, and accountable-executive sign-off, and goes through the firm's regulatory-reporting pipeline (with NCA-specific technical instructions on file format, channel, and validation). The skill produces the structured record and the build pack; the firm files.

#### Confusing the consolidation level

`individual`, `sub-consolidated`, and `consolidated` are not interchangeable. An EU subsidiary of a non-EU group reports individually to its NCA; the parent group's consolidated register (where the parent has its own DORA scope through other EU entities) is a separate filing. A record marked `consolidation_level = consolidated` for an entity that files individually is wrong. Resolve at the scope step, not in the table records.

#### Annual refresh: silent up-classification of criticality

When a function moves from `not-critical-or-important` to `critical-or-important` between cycles, the change has supervisory weight. Silent up-classification (the flag flips but no `criticality_evidence_record_id` is updated) reads as the firm not noticing. Surface the change in the build pack's year-on-year delta section; require fresh criticality evidence for the upward move.

#### Annual refresh: vendor restructuring breaks relational integrity

When an ICT third party restructures and the contracting entity changes (new LEI, new legal entity, same operational service), preserve the arrangement reference history via `linked_arrangement_references`. A new `b_03` record for the post-restructure entity, a new `b_01` record for the new contractual arrangement, and an audit trail linking the two. Otherwise the year-on-year register reads as termination plus new onboarding rather than continuation.
