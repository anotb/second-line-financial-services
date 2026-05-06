# Troubleshooting — dora-register-builder

Recurring pitfalls in DORA Register of Information builds, with the corrective posture for each. Sources are in `references/source-anchors.md`.

## EBA outsourcing register treated as drop-in DORA register data

The EBA outsourcing register (EBA/GL/2019/02 §11 [verify section]) is a different schema from the DORA Register of Information. Different columns, different relational structure (the DORA register is identifier-driven and links across tables; the outsourcing register is a flatter list), different scope (DORA covers all ICT third-party arrangements; the outsourcing register covers outsourcing as defined by EBA/GL/2019/02).

Map, do not copy. The mapping decisions and any conflicts (data-residency value differs across the two registers; sub-contractor list shorter on one side) are findings, not silent overwrites. Capture them in `data_quality_findings` and `reconciliations`.

## Missing LEI or other identifier values

The register schema is identifier-driven; missing identifiers break relational integrity and the supervisory pipeline. Long-tail SaaS vendors and small specialist providers often lack a GLEIF-issued LEI. Record `provider_identifier` as the best available (EUID, national identifier) with `identifier_type` set, and raise a `data_quality_findings` entry. Do not invent identifiers. Do not leave the field blank to "fix in submission".

## Firm-internal service-type taxonomy used instead of the ITS ICT-service-type codes

The ITS prescribes the ICT-service-type taxonomy for `b_05.ict_service_type_code` [verify ITS taxonomy reference in source-anchors.md]. The firm's internal procurement or TPRM service-type taxonomy will not align one-for-one. Build the mapping once, document the mapping decisions (especially the lossy ones), and reuse. Mapping decisions are part of the source trace, not metadata to be discarded.

## "Critical or important function" set without dated criticality evidence

The criticality flag drives downstream supervisory consequences (sub-contractor-chain visibility expectations, NCA scrutiny on exit posture, oversight-framework relevance for designated CTPPs). Setting the flag without a `criticality_evidence_record_id` pointing to a dated `criticality-assessment` output is a finding even when the flag is correct. Run `criticality-assessment` first; consume the output here.

## Stopping at first-tier ICT third party

For ICT services supporting critical or important functions, sub-contractor-chain visibility is required. Stopping at the contracted ICT third party (rank 1) and treating sub-contractors at rank 2+ as out of scope is a frequent gap. The EBA RTS on sub-contracting (where in force) and DORA Article 30 sub-outsourcing provisions [verify article number] set the expectation.

When the chain is genuinely opaque past rank 1 because the vendor will not disclose, that is itself a finding and a contract-gap (route to `contract-gap-review`), not an absence to be silently accepted.

## Data-processing-location field treated as nice-to-have

Cross-border data flows are a supervisory focus, especially data leaving the EEA. The `location_of_data_at_rest` and `location_of_data_processing` fields are mandatory for many records [verify ITS column codes] and material for the concentration view (consumed by `concentration-risk-review`). A record with a single country code where the actual hyperscaler footprint spans multiple regions is wrong, not minimal.

## Intra-group arrangements confused with third-party arrangements

Intra-group arrangements remain reportable under DORA but are flagged differently via `intra_group_flag` in `b_02`. Treating them as full third-party arrangements without the flag, or omitting them as "not third party", both fail the schema. The intra-group flag is the supervisory expectation; use it.

## Producing the register without a data-quality findings section

A submission-quality register includes the firm's own quality view. Supervisors expect the firm to know its own gaps; a clean-looking register with no `data_quality_findings` reads as either complete (rare for first-cycle builds) or unaware (more common). The findings section is an asset in supervisory dialogue, not an admission of failure.

## Treating the skill output as the submission

This skill drafts. The submission is a regulated filing requiring legal, compliance, and accountable-executive sign-off, and goes through the firm's regulatory-reporting pipeline (with NCA-specific technical instructions on file format, channel, and validation). The skill produces the structured record and the build pack; the firm files.

## Confusing the consolidation level

`individual`, `sub-consolidated`, and `consolidated` are not interchangeable. An EU subsidiary of a non-EU group reports individually to its NCA; the parent group's consolidated register (where the parent has its own DORA scope through other EU entities) is a separate filing. A record marked `consolidation_level = consolidated` for an entity that files individually is wrong. Resolve at the scope step, not in the table records.

## Annual refresh: silent up-classification of criticality

When a function moves from `not-critical-or-important` to `critical-or-important` between cycles, the change has supervisory weight. Silent up-classification (the flag flips but no `criticality_evidence_record_id` is updated) reads as the firm not noticing. Surface the change in the build pack's year-on-year delta section; require fresh criticality evidence for the upward move.

## Annual refresh: vendor restructuring breaks relational integrity

When an ICT third party restructures and the contracting entity changes (new LEI, new legal entity, same operational service), preserve the arrangement reference history via `linked_arrangement_references`. A new `b_03` record for the post-restructure entity, a new `b_01` record for the new contractual arrangement, and an audit trail linking the two. Otherwise the year-on-year register reads as termination plus new onboarding rather than continuation.
