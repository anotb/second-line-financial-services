# dora-register-builder — Phase 1 spec sheet

Plugin: `third-party-operational-resilience`
Phase: 1 (per-skill scoping)
Plan: `docs/plans/2026-05-06-rationalized-plugin-map.md`

## Activation-tuned description

```
Drafts the firm's Register of Information for ICT third-party arrangements in the structure defined by the EBA-developed implementing technical standard under DORA. Produces register entries for one or many arrangements, with the relational fields the supervisory submission requires.

Best for:
- An EU-nexus firm preparing the DORA Register of Information for the first or annual submission cycle.
- An EU subsidiary of a US firm where the parent needs visibility into the EU register-of-information data quality before submission.
- A second-line review of an existing register where data-quality and consistency need a structured check against the ITS schema.

Not the right tool when:
- The firm has no DORA nexus (US-only with no in-scope entity). Use the firm's own TPRM register and skip this skill.
- The question is per-arrangement diligence (use vendor-diligence) or contract clause coverage (use contract-gap-review).
- The submission is governed by national-competent-authority technical filing rules that diverge from the ITS (call out for legal/compliance review; this skill drafts to the ITS schema).

Anchored to: DORA — Regulation (EU) 2022/2554, Articles 28(3) and 28(7) on the register of information [verify subarticle]; the Commission Implementing Regulation laying down the implementing technical standard for the register of information (developed by the EBA, EIOPA, and ESMA via the ESAs) and the related EBA preparation page [verify ITS reference]; EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02) §11 outsourcing register [verify section]; ECB and national-competent-authority technical reporting instructions where applicable.
```

## Source anchors

- DORA — Regulation (EU) 2022/2554. Article 28(3) requires the register of information; Article 28(7) governs annual reporting and competent-authority access. Article 6 (ICT risk management framework) for the link from the ICT register to the firm's ICT risk management framework [verify subarticle].
- ESAs joint work on the implementing technical standard (ITS) for the register of information under DORA. The Commission Implementing Regulation adopting the ITS sets the register schema. Use the EBA preparation page as the public anchor for the schema as adopted: https://www.eba.europa.eu/activities/direct-supervision-and-oversight/digital-operational-resilience-act/preparation-dora-application. [verify ITS Commission Implementing Regulation citation].
- EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02). Outsourcing-register guideline [verify section number]. Pre-existing-register data is the natural input to the DORA register for many EU banks.
- ECB and national-competent-authority technical instructions for register submission (vary by jurisdiction; cite the relevant instruction).
- Cross-references inside this plugin: criticality-assessment (the critical-or-important-function flag is sourced here), vendor-diligence (subcontractor and data-flow inputs), concentration-risk-review (consumes register output).

## Sector overlays needed

- `references/sector-overlays/banking.md` — banking-specific national-competent-authority instructions (ECB SSM banks; EBA-coordinated approach for less-significant institutions); EBA outsourcing-register transitional posture.
- `references/sector-overlays/insurance.md` — EIOPA-coordinated approach for insurers; NAIC outsourcing model for the US-parent dimension; Form B/Form F and US-parent reporting interplay.
- `references/sector-overlays/capital-markets.md` — ESMA-coordinated approach for investment firms, trading venues, CSDs, CCPs; AIFMD/UCITS depositary arrangements as ICT-third-party considerations.
- `references/sector-overlays/payments-fintech.md` — payment institutions and e-money institutions in scope where DORA applies; EBA register expectations for payments-specific service types.

## Cross-cutting overlays

- None mandatory at this skill level. The register is a structured filing; cyber, privacy, and concentration considerations show up via fields the schema already includes (data location, sub-outsourcing, function-supported), and the deeper treatment lives with `vendor-diligence`, `exit-plan`, and `concentration-risk-review`.

## Output template named sections

`templates/default-output.md`:

1. Scope and entities in scope (which legal entities of the financial-entity group are covered; consolidation posture)
2. As-of date and reporting reference period
3. Source-data posture (which firm registers and systems were used as input; data-quality caveats)
4. Register entries by ITS table:
   - Contractual arrangements (general information) [verify ITS table number]
   - Contractual arrangements (specific) [verify ITS table number]
   - ICT third-party service providers [verify ITS table number]
   - Functions identified as critical or important [verify ITS table number]
   - ICT services [verify ITS table number]
   - Sub-contractors and ICT services chain [verify ITS table number]
   - Identification of LEI / EUID / national-identifier values
5. Data-quality findings (missing, inconsistent, or stale fields)
6. Reconciliations (against the firm's existing TPRM register, the ICT-asset inventory, and the contract repository)
7. Open questions for legal and compliance
8. Reviewer questions
9. Source trace and confidence label

## Structured output fields

The structured output mirrors the EBA DORA Register of Information ITS schema as adopted by the Commission Implementing Regulation [verify ITS reference]. The skill produces records aligned to the ITS tables; field names follow the ITS column names where stable, and `[verify ITS column]` is used where exact column code is uncertain.

Indicative table-field mapping (illustrative, not exhaustive; phase 2 must verify against the adopted ITS):

- `register_metadata` — financial entity LEI, reporting reference date, national competent authority code, consolidation level, currency [verify ITS column codes].
- `b_01_contractual_arrangement_general` — contractual arrangement reference number, type (single, complex, or master and addenda), date of last update, start date, end date, notice period, governing law country, jurisdiction of dispute resolution, value of contract reporting period, currency [verify ITS column codes].
- `b_02_contractual_arrangement_specific` — link from contractual-arrangement reference to ICT-service identifier and to ICT-third-party-service-provider identifier; identification of intra-group arrangements [verify ITS column codes].
- `b_03_ict_third_party_service_providers` — name, identifier (LEI), country of head office, country of registration, ultimate parent identifier, type (cloud, software, etc.), criticality designation by competent authority where known, EU-presence flag [verify ITS column codes].
- `b_04_functions` — financial-entity function reference, function description, criticality (critical, important, not critical), licensed activity reference, recovery time objective, recovery point objective, impact-of-discontinuation indicator [verify ITS column codes].
- `b_05_ict_services` — service identifier, ICT-service-type code (per the ITS taxonomy), description, link to function reference, link to ICT-third-party identifier, link to contractual-arrangement reference, location of data at rest, location of data processing, sensitivity-of-data indicator [verify ITS column codes and the ICT-service-type taxonomy].
- `b_06_sub_contractors_chain` — sub-contractor identifier, role-in-chain, location of data at rest, location of data processing, criticality of sub-contractor, identification of sub-contractor providing the actual service vs intermediary [verify ITS column codes].
- `b_07_identification_codes` — LEI, EUID, national-identifier-type, national-identifier-value [verify ITS column codes].

Top-level rollup:

- `register_id` (string)
- `as_of_date` (string, ISO 8601)
- `entities_in_scope` (array of object: `legal_entity_name`, `lei`, `consolidation_role`)
- `tables` (object keyed by ITS table identifier, each containing the array of records described above)
- `data_quality_findings` (array of object: `table`, `column`, `finding`, `severity`)
- `reconciliations` (array of object)
- `open_questions` (array of string)
- `reviewer_questions` (array of string)
- `confidence_label` (enum)
- `source_trace` (array of object)

## Example scenarios (two, public-source-derived)

1. **First-cycle Register of Information build for an EU subsidiary of a US bank.** Inputs: the firm's TPRM register export, the firm's contract repository, the ICT-asset inventory, the criticality output per arrangement. Anchored to: DORA Article 28(3) [verify subarticle]; the ITS adopted by the Commission Implementing Regulation [verify ITS reference]; EBA outsourcing register guideline [verify section]. The output produces register entries across the ITS tables, identifies that LEI is missing for two ICT third parties, that one critical-or-important-function arrangement is missing the data-processing-location field, and that two sub-contractor entries reconcile poorly against the contract repository's flow-down clauses. Reviewer questions are surfaced for the EU subsidiary's risk officer and the head of vendor management.

2. **Annual refresh review for an EU-nexus insurer's existing register.** Inputs: prior-year register, the year's vendor changes, the criticality re-assessment outputs. Anchored to: DORA Article 28(7); EIOPA-coordinated guidance for insurers; NAIC outsourcing model for the US-parent dimension. The output reconciles year-on-year movement, identifies five new critical-or-important-function arrangements added during the year, four discontinued, and one re-classified up from "not critical" to "important". Flags that the criticality re-classification was not supported by a dated criticality output (use `criticality-assessment` to remediate before submission). Surfaces the criticality-classification-evidence gap as the headline finding.

## Common pitfalls

1. **Treating the existing EBA outsourcing register as drop-in DORA register data.** The DORA ITS is a different schema with different columns and stricter relational links. Mapping is required, not copy-paste.
2. **Missing LEI or EUID values.** The register schema is identifier-driven; missing identifiers break relational integrity and the supervisory pipeline. Treat missing identifiers as data-quality findings.
3. **Using the firm's internal service-type taxonomy instead of the ITS ICT-service-type codes.** The ITS prescribes the taxonomy. Map firm-internal types to ITS codes; record the mapping decisions.
4. **Setting "critical or important function" without a dated `criticality-assessment` output to back it.** The flag is a regulatory determination with downstream consequences; document the evidence.
5. **Stopping at first-tier ICT third party.** The schema requires sub-contractor-chain visibility for critical-or-important-function services. Missing sub-contractor entries are a finding, not an absence.
6. **Treating the data-processing-location field as a nice-to-have.** Cross-border data flows are a supervisory focus; the field is mandatory for many records and material for the concentration view.
7. **Confusing intra-group arrangements with third-party arrangements without the appropriate flag.** Intra-group arrangements are reportable but flagged differently. Use the ITS flag.
8. **Producing the register without a data-quality findings section.** A submission-quality register includes the firm's own quality view; supervisors expect the firm to know its own gaps.
9. **Treating this skill's output as the submission.** This skill drafts. The submission is a regulated filing requiring legal, compliance, and accountable-executive sign-off.
