# DORA Register of Information — preparation build pack

This pack is preparation-grade. It supports the firm's data-quality posture and the named approver's sign-off on that posture. It is not the official Register of Information template under Commission Implementing Regulation (EU) 2024/2956; the firm's regulatory-reporting pipeline maps the prepared records into the official template before submission.

**Register ID**: [firm-defined, e.g., `<group-LEI>-<reporting-year>`]
**Reporting reference date**: [YYYY-MM-DD]
**Reporting reference period**: [start] to [end]
**Consolidation level**: [individual | sub-consolidated | consolidated]
**National competent authority**: [code]
**Reporting currency**: [ISO 4217]
**Build review type**: [first-cycle-build | annual-refresh | off-cycle-update | quality-review-only | post-onboarding-update | post-termination-update]
**Owner (role)**: [head of TPRM | ICT risk manager | DORA programme lead]
**Approver (role)**: [accountable executive named in the firm's DORA governance for register submission]
**Confidence label**: [high | medium | low | unknown]

## Scope and entities in scope

Legal entities of the financial-entity group covered by this register, with LEI, country, and consolidation role. The register is reported at the consolidation level set above; sub-consolidated and consolidated registers carry additional scope notes.

| Legal entity name | LEI | Country | Consolidation role | Competent authority |
|---|---|---|---|---|
| | | | | |

## Source-data posture

Which firm systems and registers were used as input to the build, and the data-quality caveats that follow.

- TPRM register used: [yes / no — system name].
- Contract repository used: [yes / no — system name].
- ICT asset inventory used: [yes / no — system name].
- Criticality-assessment records used: [yes / no — pointer to the records].
- Vendor-diligence records used: [yes / no — pointer to the records].
- EBA outsourcing register (EBA/GL/2019/02) used as input: [yes / no — pointer; mapping note].
- Data-quality caveats: [bulleted; e.g., contract repository missing 2 amendments executed in Q4; criticality outputs not yet refreshed for 6 arrangements].

## Register entries by table (preparation-grade)

Table identifiers below follow a local B-table convention adapted from the EBA preparation materials. They are preparation-grade — not aligned column-for-column to the official ITS taxonomy under Commission Implementing Regulation (EU) 2024/2956. Confirm the exact table and column codes from the adopted Implementing Regulation against `references/source-anchors.md` at firm onboarding, and rely on the firm's regulatory-reporting pipeline to format the official template before submission.

### B.01 — Contractual arrangements (general information)

One record per contractual arrangement. Carries the arrangement reference number, type, dates, notice period, governing law, jurisdiction of dispute resolution, contract value for the reporting period.

[record table or per-record narrative; the structured output carries the per-field detail]

### B.02 — Contractual arrangements (specific information)

Links each arrangement to the ICT third-party service provider, the ICT services covered, and the function references supported. Carries the intra-group flag.

### B.03 — ICT third-party service providers

One record per provider. LEI preferred; EUID or national identifier where LEI unavailable (and a corresponding data-quality finding). Country of head office, country of registration, ultimate parent, provider type, EU-presence flag, designation under DORA Article 31 oversight where known.

### B.04 — Functions of the financial entity

Function references and descriptions, criticality classification (`critical-or-important` / `not-critical-or-important`), and the criticality evidence pointer. Recovery objectives where defined for the function.

### B.05 — ICT services

ICT services supplied under the arrangements, with the ICT-service-type code from the ITS-defined taxonomy (map firm-internal taxonomy to ITS codes; record mapping decisions). Locations of data at rest and data processing, sensitivity of data, EEA-boundary indicators.

### B.06 — Sub-contractors and ICT-services chain

Sub-contractor records for ICT services supporting critical or important functions. Rank in chain, role (provides service / intermediary / infrastructure), country of head office, data locations. Sub-contractor visibility is required for critical-or-important services; gaps are findings, not absences.

### B.07 — Entities of the financial-entity group signing or making use

Per-entity records linking the in-scope legal entities to the contractual arrangements they sign or use.

## Data-quality findings

The firm's own quality view of the register. Supervisors expect the firm to know its own gaps before they look.

| Table | Column | Record reference | Finding | Severity | Owner | Remediation due |
|---|---|---|---|---|---|---|
| | | | | blocking / high / medium / low | | |

## Reconciliations

Reconciliations against the firm's existing TPRM register, the ICT-asset inventory, the contract repository, and (for refresh cycles) the prior-year register.

| Source system | Scope note | Records in source | Records in register | Records matched | Result | Exceptions |
|---|---|---|---|---|---|---|
| | | | | | clean / exceptions-noted / material-gaps | |

## Open questions for legal and compliance

Open interpretation, scoping, and submission questions. Each item names the function the question goes to (legal, compliance, regulatory affairs, the host-state NCA dialogue).

## Reviewer questions

Questions for the named approver and for the human review-gate forums. Each question names the decision it supports (sign-off on submission readiness, sign-off on data-quality posture, sign-off on the consolidation choice).

## Source trace

| Claim | Source | Section | Date | URL or file ref |
|---|---|---|---|---|
| | | | | |

Cite `references/source-anchors.md` for the canonical citations. Use `[verify ITS table code]`, `[verify ITS column code]`, or `[verify section]` where the exact reference is uncertain; do not invent. The DORA ITS column codes and table codes resolve at firm onboarding.

## Review-gate posture

- Review gates this build must clear: [scope, evidence, authority, impact, decision].
- The build does not file and is not the official template. The named accountable executive signs off on the firm's data-quality posture. The firm's regulatory-reporting pipeline maps the prepared records into the official Register of Information template under Commission Implementing Regulation (EU) 2024/2956 and submits via the NCA-specified channel.
- Next review trigger: [next reporting reference date | scope-change trigger | criticality re-classification | ICT-third-party restructure].

---

*Build depth scales to scope and review type.* A first-cycle build for a complex group reads long and carries heavy data-quality and reconciliation sections; an annual refresh for a stable register reads shorter, with the year-on-year delta as the headline. A quality-review-only run skips the substantive register tables and concentrates on the data-quality and reconciliation sections.

*The pack adapts to audience.* A pack for the DORA programme lead reads operational. A pack for the accountable executive leads with the residual data-quality posture and the sign-off question. A pack for the host-state NCA dialogue reads as a justification of the firm's own quality posture before the supervisor asks.
