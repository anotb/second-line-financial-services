---
name: dora-register-builder
description: |
  Drafts a financial entity's Register of Information for ICT third-party arrangements in the structure set by the Commission Implementing Regulation under DORA Article 28(9). Produces the per-arrangement records the firm submits, with the relational links across contractual arrangement, ICT third-party, ICT service, function, sub-contractor chain, and the entities of the group signing or making use. Heaviest structured-output skill in the plugin: the structured record is the artifact, the markdown narrative is the build pack the named approver reads.

  Best for:
  - An EU-nexus financial entity preparing the Register of Information for the first reporting cycle, or for the annual refresh.
  - An EU subsidiary of a non-EU group where the parent needs visibility into EU register data quality before submission, and the subsidiary files individually to its national competent authority.
  - A second-line review of an existing register where data quality, relational integrity, and ICT-service-type taxonomy mapping need a structured check against the ITS schema before the accountable executive signs off.
  - An off-cycle update following a material onboarding, termination, restructuring, or criticality re-classification.

  Not the right tool when:
  - The firm has no DORA nexus. Use the firm's own TPRM register and skip this skill.
  - The criticality flag has not been set (run `criticality-assessment` first; the register consumes the determination).
  - The job is per-arrangement diligence (use `vendor-diligence`), contract clause coverage (use `contract-gap-review`), portfolio-level concentration (use `concentration-risk-review`), or exit posture for a specific arrangement (use `exit-plan`).
  - The submission is governed by an NCA-specific technical filing rule that diverges from the ITS templates. The skill drafts to the ITS schema; the firm's regulatory-reporting pipeline applies the NCA-specific channel and validation overlay.
argument-hint: "[arrangement set, prior-year register, criticality outputs, vendor-diligence pack, TPRM register export, contract repository pointers, scope statement]"
---

# DORA Register of Information builder

A Register of Information is the relational, identifier-driven file the financial entity maintains under DORA Article 28(3) and reports annually under Article 28(7). Supervisors read it for sub-contractor-chain visibility, cross-border data-flow posture, and ICT-third-party concentration. The Critical ICT Third-Party Service Provider designation pipeline under Article 31 reads it. The firm's own concentration analysis and exit-readiness review read it. So the register is not a procurement export. It is the firm's structured supervisory artifact for ICT third-party risk.

This skill drafts that artifact. It produces a structured record (`schemas/dora-register-entry.schema.json`) that mirrors the ITS B-table structure, plus a markdown build pack (`templates/default-output.md` shape) the named approver reads before signing off. The submission itself is filed by the firm's regulatory-reporting pipeline through the NCA-specified channel; this skill stops at the build, before sign-off.

## Ask first

Before drafting, settle six things. The build is identifier-driven and relational, so getting these wrong upstream costs more than asking once.

- **Which legal entities are in scope, and at what consolidation level.** Individual, sub-consolidated, or consolidated. An EU subsidiary of a non-EU group typically files individually to its host-state NCA; the parent's consolidated register is a separate filing where the parent has its own DORA scope through other EU entities. Resolve at scope, not in the table records.
- **Reporting reference date and reporting reference period.** The ITS sets the reference-date convention; pin it from the adopted Commission Implementing Regulation and the NCA's filing-cycle instructions for the cycle in flight.
- **National competent authority and submission channel.** ECB SSM for direct-supervised significant institutions. Host-state NCA for less-significant institutions, payment and e-money institutions, insurers and reinsurers, investment firms, fund managers, trading venues, CSDs, and CCPs (with ESMA, EIOPA, EBA coordination as applicable). The technical channel and validation rules vary; pin per filing.
- **Build review type.** First-cycle build, annual refresh, off-cycle update, quality-review-only, post-onboarding update, post-termination update. Each has a different evidence ask, a different reviewer-question cluster, and a different decision-forum context. A first-cycle build for a complex group runs long and carries heavy data-quality and reconciliation sections; a quality-review-only run skips the substantive table records and concentrates on findings and reconciliations.
- **Source-data posture.** Which firm systems are inputs: TPRM register, contract repository, ICT-asset inventory, prior-year register, EBA outsourcing register (EBA/GL/2019/02 §11), criticality-assessment outputs, vendor-diligence packs. Each carries a quality caveat. Name them.
- **Criticality-assessment availability.** The register's `b_04_functions.criticality` field is sourced from `criticality-assessment` and backed by a `criticality_evidence_record_id`. If criticality has not been formally set for in-scope arrangements, route there first and consume the output here. Setting the flag in this skill without backing evidence is a defect, not a shortcut.

When the scope record is supplied, the skill consumes it for institution type, sector overlay set, cross-cutting overlay set, persona, and source posture. When it is not supplied, ask the questions above and default to public posture if the practitioner declines. Do not silently apply a sector overlay default.

## How the build gets done

The build has the same spine across firm types. A senior practitioner walks it in roughly the order the inputs land, not in lockstep. The structured record sorts itself; the build pack reads in the order below.

### Scope, source posture, identifiers

Open by naming the in-scope legal entities with LEI, country, and consolidation role. Pin the reporting reference date and period, the NCA code, and the consolidation level. Record the source systems used as input and their quality caveats. Identifier integrity is load-bearing: LEI is preferred for `b_03_ict_third_party_service_providers.provider_identifier`, EUID or national identifier where LEI is unavailable, with `identifier_type` set. Long-tail SaaS vendors and small specialist providers without a GLEIF-issued LEI are common; record the best available identifier and raise a `data_quality_findings` entry. Do not invent identifiers. Do not leave the field blank to "fix in submission".

### B.01 to B.07: the table chain

The table identifiers below follow the EBA preparation-materials convention. Confirm the exact column codes and table labels against the adopted Commission Implementing Regulation each cycle (the ITS Annexes set the column codes; the joint ESA Final Report on the draft ITS is the explanatory record). Where ITS column codes are uncertain, mark them in the structured output per the verification posture in `references/source-anchors.md`; the build-pack body does not carry verification markers.

**B.01 Contractual arrangements (general information).** One record per contractual arrangement. Reference number, type (single, complex, master and addenda, framework agreement), date of last update, start date, end date or perpetual indicator, notice period, governing law country, jurisdiction of dispute resolution, contract value for the reporting period and currency. Where a master agreement and a chain of addenda sit together, the relational chain goes in `linked_arrangement_references`. The arrangement reference number is firm-internal and stable across cycles; preserve the history when restructurings happen.

**B.02 Contractual arrangements (specific information).** Links each arrangement reference to the ICT third-party identifier and to the ICT-service identifiers it covers, and to the function references it supports. The intra-group flag lives here. Intra-group arrangements remain reportable but are flagged differently. Treating them as full third-party arrangements without the flag, or omitting them as "not third party", both fail the schema.

**B.03 ICT third-party service providers.** One record per provider. Name, identifier (LEI preferred), country of head office, country of registration, ultimate parent identifier and name, person type, provider type, EU-presence flag, designation under Article 31 oversight where known. The CTPP designation field is supervisor-set, not firm-set; record where known, follow the verification posture in `references/source-anchors.md` for any ITS column whose code is uncertain, and surface ambiguity as an open question rather than guessing.

**B.04 Functions of the financial entity.** Function reference, description, criticality (`critical-or-important`, `not-critical-or-important`, `unknown`), licensed activity reference where applicable, recovery time objective and recovery point objective for the function, impact-of-discontinuation indicator, supports-critical-business-function flag. Criticality is sourced from `criticality-assessment` and pointed at by `criticality_evidence_record_id`. A flag without an evidence pointer is a finding even when the flag is correct.

**B.05 ICT services.** Service identifier, ICT-service-type code from the ITS-defined taxonomy in the Annex, description, link to function reference, link to ICT-third-party identifier, link to contractual-arrangement reference, supports-critical-or-important-function flag, locations of data at rest and data processing (ISO 3166-1 alpha-2 country codes), sensitivity of data, EEA-boundary indicators for storage and processing. The ITS-defined service-type taxonomy is prescriptive; the firm's internal procurement or TPRM service-type taxonomy will not align one-for-one. Build the mapping once, document the mapping decisions (especially the lossy ones), and reuse. Mapping decisions are part of the source trace, not metadata to be discarded. Cross-border data flows are a supervisory focus: a record with a single country code where the actual hyperscaler footprint spans multiple regions is wrong, not minimal.

**B.06 Sub-contractor and ICT-services chain.** Sub-contractor identifier, name, parent ICT third-party identifier, linked ICT-service identifier, role in chain (provides service, intermediary, infrastructure provider), country of head office, locations of data at rest and data processing, supports-critical-or-important-function flag, rank in chain (1 for direct sub-contractor of the contracted ICT third party, 2 for the next tier, and so on). Sub-contractor visibility is required for ICT services supporting critical or important functions: stopping at rank 1 and treating rank 2+ as out of scope is a frequent gap. The Commission Delegated Regulation on the RTS on sub-contracting under Article 30(5) sets the elements the firm must assess before allowing sub-contracting in the chain that supports a critical or important function; the register's B.06 record is the structured artifact the RTS reads back into. Where the chain is genuinely opaque past rank 1 because the vendor will not disclose, that is itself a finding and a contract gap (route to `contract-gap-review`), not an absence to be silently accepted.

**B.07 Entities of the financial-entity group signing or making use.** Per-entity records linking the in-scope legal entities to the contractual arrangements they sign, use, or both. The role enum carries `signing-entity`, `using-entity`, `signing-and-using`. For sub-consolidated and consolidated registers this table grows; for an individual filing it tracks the one in-scope entity against the arrangements it touches.

### Data quality, reconciliations, open questions, reviewer questions

A submission-quality register includes the firm's own quality view. Supervisors expect the firm to know its own gaps before they look. A clean-looking register with no `data_quality_findings` reads as either complete (rare for first-cycle builds) or unaware (more common). Record findings with table, column, record reference, finding, severity (`blocking`, `high`, `medium`, `low`), owner, and remediation due date. The findings section is an asset in supervisory dialogue, not an admission of failure.

Reconciliations sit alongside findings: against the firm's existing TPRM register, the ICT-asset inventory, the contract repository, the EBA outsourcing register where the firm has one (most EU credit institutions, investment firms, payment institutions, e-money institutions do), and the prior-year register for refresh cycles. Each reconciliation carries a record-count match, an exception list, and a result label (`clean`, `exceptions-noted`, `material-gaps`). The EBA outsourcing register is a different schema from the DORA register: different columns, different relational structure (DORA is identifier-driven and links across tables; the outsourcing register is a flatter list), different scope. Map, do not copy. Mapping conflicts (data-residency value differs across the two registers; sub-contractor list shorter on one side) are findings, not silent overwrites.

Open questions name the function the question goes to: legal, compliance, regulatory affairs, the host-state NCA dialogue. Reviewer questions tie to the decision and cluster for the forum that decides: TPRM forum for an operational question on a single arrangement, ICT risk committee for the register-wide quality posture, the named accountable executive for sign-off, the host-state NCA dialogue where the firm has chosen to surface the build pack pre-submission.

### Annual-refresh delta logic

A refresh build is structurally different from a first-cycle build. The supervisory dialogue is interested in movement, not just stock: new arrangements added during the year, arrangements discontinued, arrangements re-classified upward in criticality (from `not-critical-or-important` to `critical-or-important`), arrangements re-classified downward, vendor-entity restructurings where the LEI moves but the substantive arrangement persists, fresh sub-contractor-chain entries for newly-disclosed rank 2+ tiers. Surface each of these in a year-on-year delta narrative section. Up-classifications need fresh dated criticality evidence for the new tier; silent up-classification (the flag flips but no `criticality_evidence_record_id` is updated) reads as the firm not noticing. Vendor restructurings need `linked_arrangement_references` to preserve the audit trail; otherwise the register reads as a termination plus a new onboarding rather than a continuation.

### Sector and cross-cutting overlay loading

When the scope names a sector, load the matching `references/sector-overlays/<sector>.md`: `banking.md` for ECB SSM and EBA-coordinated banking matters; `insurance.md` for EIOPA-coordinated insurer matters and the US-parent dimension where Form B and Form F interplay; `capital-markets.md` for ESMA-coordinated investment firm, fund manager, trading venue, CSD, and CCP matters; `payments-fintech.md` for payment institution and e-money institution matters. A dual-registrant or a fintech with a sponsor-bank arrangement may load two.

The cyber cross-cutting overlay (`references/cross-cutting/cyber.md`) loads when ICT services in scope materially expose the firm to cyber risk that the register's data-residency, sub-contractor-chain, or service-type fields surface for supervisory attention. Privacy and concentration considerations show up via fields the schema already includes (data location, sub-outsourcing chain, function-supported); the deeper treatment lives with `vendor-diligence`, `exit-plan`, and `concentration-risk-review`. Load only the overlays the scope names. Gold-plating a build with overlays the engagement does not implicate adds noise without supervisory value.

## Quality bar

Holds across every build regardless of firm type, audience, or render format.

- **Identifier integrity.** The register is identifier-driven. Missing LEI or other identifiers break relational integrity and the supervisory pipeline. Best available identifier with `identifier_type` set, plus a finding. Never invented.
- **Relational integrity across the table chain.** B.01 references resolve to B.02 which resolves to B.03, B.05, and B.04. B.06 chains hang off B.05 and B.03. B.07 links group entities to B.01. A record that does not resolve is a defect.
- **ITS taxonomy compliance for `b_05.ict_service_type_code`.** The ITS Annex sets the taxonomy. The firm's internal taxonomy is mapped to it; the mapping decisions sit in the source trace.
- **Criticality evidence backing.** `b_04_functions.criticality = critical-or-important` requires `criticality_evidence_record_id`. No exceptions.
- **Sub-contractor visibility for critical-or-important services.** B.06 entries to the depth the chain reveals; opacity is a finding, not an absence.
- **Data-quality findings section is part of the build, not a separate document.** A register without findings reads wrong.
- **Source trace.** Every material claim cites `references/source-anchors.md` (or a loaded overlay) by path. Uncertain ITS column codes are marked in the structured record only, per the verification posture in `references/source-anchors.md`; the build-pack body does not carry verification markers. Unsupported items go to the engagement issue log, not silently into the build.
- **The skill does not file.** The build pack carries reviewer questions and named decision checkpoints. The named accountable executive signs off via the attestation block. Submission goes through the firm's regulatory-reporting pipeline.

## Adaptation

Flexes by engagement.

- **Build depth scales to scope and review type.** First-cycle builds run long. Annual refreshes lead with the year-on-year delta. Quality-review-only runs skip the table records and concentrate on findings and reconciliations. Off-cycle updates concentrate on the changed records and the relational impact.
- **Audience drives shape.** A pack for the DORA programme lead reads operational. A pack for the accountable executive leads with the residual data-quality posture and the sign-off question. A pack for the host-state NCA dialogue reads as a justification of the firm's own quality posture before the supervisor asks.
- **Sector overlay loading follows the scope.** Dual-registrant or BaaS arrangements load two.
- **Source posture (public-only, public-plus-firm-policy, public-plus-firm-policy-plus-system-of-record-evidence, connector-aware) drives the evidence ask** and the confidence label on the build.
- **Firm-specific policy, taxonomy, named owners, internal-to-ITS service-type mapping table** sit in `references/firm-overlay.md`, consumed when present, never in the build directly.

## Output

Two artifacts: the structured record per `schemas/dora-register-entry.schema.json`, and the build pack per `templates/default-output.md`. The structured record is the cross-skill contract; the build pack is what the named approver reads before sign-off.

Downstream consumers: `concentration-risk-review` reads the B.03 ICT third-party records and the B.06 sub-contractor chain for the portfolio analysis. `exit-plan` reads the B.04 critical-or-important function records and confirms each carries a current exit plan; the absence is itself a finding routed back here. The firm's regulatory-reporting pipeline consumes the per-table records for the NCA submission. Where a record sits inside an Article 31 oversight perimeter, the joint ESA data-collection cycle for CTPP designation reads the relevant records.

The schema is additive only. Add fields, do not rename or repurpose them. A breaking change is a versioned migration with the downstream skills told in advance. Fields whose ITS column codes resolve at firm onboarding follow the verification posture in `references/source-anchors.md` until pinned; the firm-overlay file is where the pin lives once known.

## Pointers

- `references/source-anchors.md` ... citations, verification posture for ITS table and column codes, EU OJ references for the Commission Implementing Regulation, the joint ESA Final Report, and the RTS on sub-contracting under Article 30(5).
- `references/sector-overlays/banking.md`, `insurance.md`, `capital-markets.md`, `payments-fintech.md` ... sector-specific submission-channel and supervisory-frame detail loaded per scope.
- `references/cross-cutting/cyber.md` ... cyber cross-cutting frame loaded where the register's data-residency, sub-contractor-chain, and service-type fields surface cyber-risk material to the supervisory read.
- `references/firm-overlay.md` ... firm policy, named owners, ITS-to-firm taxonomy mapping table, NCA-specific channel and validation overlay (consumed when present).
- `templates/default-output.md` ... build-pack template.
- `schemas/dora-register-entry.schema.json` ... structured-output contract for downstream consumption.
- `examples/critical-cloud-bank.md`, `examples/data-vendor-asset-manager.md` ... anonymised public-source-derived scenarios: first-cycle build for an EU subsidiary of a US bank with a hyperscaler IaaS arrangement; annual refresh for an EU UCITS management company with a market-data-vendor restructuring and an alternative-data-vendor onboarding.
- `TROUBLESHOOTING.md` ... recurring defects: outsourcing-register copy-paste, missing identifiers, firm taxonomy used in place of ITS taxonomy, criticality flag without evidence, stopping at rank 1, data-processing-location treated as nice-to-have, intra-group confusion, missing data-quality section, treating the build as the submission, consolidation-level errors, silent up-classification, vendor-restructuring relational-integrity loss.

Plugin-level shared references (`references/source-map.md`, `references/policy-control-library.md`, `references/review-gates.md`) sit at the plugin root and are consulted alongside the skill-level files.
