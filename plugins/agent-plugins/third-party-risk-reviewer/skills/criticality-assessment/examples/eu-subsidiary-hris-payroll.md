# Example: HRIS SaaS supporting payroll for an EU subsidiary of a US insurer

Public-source-derived. No named vendor. The shape mirrors a common criticality call where a US-headquartered insurer's EU subsidiary procures an HRIS SaaS that runs payroll for the EU workforce. The arrangement falls inside DORA's perimeter as an ICT service to a financial entity but is not itself a high-criticality function.

## Input

- **Arrangement**: a European HRIS SaaS providing core HR records, time-and-attendance, and monthly payroll calculation for the EU subsidiary's workforce. Payroll disbursement runs through the subsidiary's banking partner.
- **Business process supported**: workforce-payroll administration for the EU subsidiary.
- **Inputs already on file**: the insurer's IBS register (payroll is not on the IBS list; the regulated IBS list covers underwriting, claims, policy administration, and policyholder communications); the vendor's published certifications (ISO 27001, SOC 2 Type II); the subsidiary's regulatory profile.
- **Engagement scope supplied**: institution = EU subsidiary of US insurance group; primary regulators = the lead state insurance department (US) and the host EU competent authority; persona = head of TPRM with EU-subsidiary risk officer co-review; source posture = public-plus-firm-policy; sector overlay = insurance; cross-cutting overlays = privacy.
- **AI vendor**: false. The HRIS has no AI features in scope.

## Output sketch

The skill produces a criticality assessment record. Headlines:

- **Service in scope and process supported** — payroll administration; not on the firm's IBS list.
- **RTO and RPO** — firm tolerance for payroll is "monthly cycle plus 5 days"; vendor RTO is 24h, RPO is 4h. `recovery_meets_firm_tolerance = yes` for the cycle test.
- **Customer impact** — `severity = low`; populations = workforce (employees), not policyholders; harm modes = workforce financial impact and reputational on a missed payroll cycle.
- **Regulatory impact** — `severity = medium`; regimes = privacy, employment law, and the firm's prudential reporting where workforce-cost data feeds capital reporting; notification triggers = data-breach posture under GDPR and applicable state insurance department obligations on material vendor incidents.
- **Operational impact** — `substitutability = moderate` (payroll vendors are substitutable on a multi-month cycle); time-to-restore measured in days for a forced cutover under a backup vendor; `manual_workaround_viable = true` for a single cycle (manual payroll calculation under spreadsheet for the cycle window).
- **Concentration considerations** — minimal at the group level; flag if the same HRIS vendor serves multiple subsidiaries.
- **Tier** — `important` rather than `critical`. Rationale: not on the IBS list; substitutability is moderate; manual workaround viable for one cycle; regulatory exposure is privacy-driven, not solvency-driven.
- **DORA flag** — `no` (the arrangement is in scope of the DORA register because it is an ICT service to a financial entity, but the EBA criticality threshold for a critical or important function is not met for payroll at this subsidiary's scale and IBS map). Rationale recorded explicitly because the firm's own tier and the DORA call use different criteria; both belong on the record.
- **UK IBS flag** — `not-in-scope`.
- **Owner** — head of TPRM at the US group with the EU-subsidiary chief operating officer as the business owner. Approver per policy is the EU-subsidiary risk committee for important-tier arrangements with cross-border data flows.
- **Reviewer questions** — payroll-vendor portability rehearsal cadence; data-residency posture for EU-resident workforce data; the explicit DORA register entry with the not-critical-or-important-function flag.
- **Next-review trigger** — annual recertification, material-service-change at the vendor, expansion of the workforce population beyond the subsidiary.

The record stops at the recommendation. The named approver decides.

## Why this scenario matters

- **Tier and DORA flag are separate calls.** The firm's tier ("important") and the DORA critical-or-important-function flag ("no") are derived from different criteria and recorded separately, with rationale on each. Treating them as one call collapses the record.
- **In-scope-of-register is not the same as critical-or-important.** The arrangement still lands in the DORA register because it is an ICT service to a financial entity. The criticality flag inside the register is a different field.
- **Cross-border lens enters via the cross-cutting privacy overlay.** Privacy applies because the arrangement processes regulated personal data of EU residents. Sector overlay is insurance because the regulated firm is an insurer; the work touches both.
- **Substitutability and manual-workaround viability change the tier read.** A vendor processing the same data category at a higher-criticality function (e.g., policy administration) would land at `critical` under the same evidence pack. The IBS dependency drives the tier, not the vendor's category.

## Anchors

- Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FRB/FDIC, June 2023) on risk-based criticality.
- DORA Regulation (EU) 2022/2554, Article 28 general principles and the EBA-defined notion of critical or important function.
- EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02) on the assessment criteria for criticality.
- BCBS Principles for Operational Resilience (March 2021) on important business services.
- NAIC Insurance Holding Company System Regulatory Act (Model #440) for the holding-company-act lens on intragroup arrangements where applicable.

See `references/source-anchors.md` for full citations.
