# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## community-bank-core-deposit-ledger

### Example: core-banking SaaS for a community bank's deposit ledger

Public-source-derived. No named vendor. The shape mirrors a common criticality call at a community bank ($2-5B in assets) selecting a core-banking SaaS to host the deposit ledger.

#### Input

- **Arrangement**: a US-based core-banking SaaS that runs the bank's deposit subledger, posts daily settlement, and provides the system of record for retail and small-business deposits.
- **Business process supported**: deposit-account servicing across retail and small-business books.
- **Inputs already on file**: the bank's important-business-service map (deposits identified as IBS); the firm's impact tolerance for the deposit-servicing IBS (RTO 4 hours, RPO 15 minutes); vendor proposal with claimed RTO 8 hours and RPO 1 hour; SOC 2 Type II in process.
- **Engagement scope supplied**: institution = state-chartered community bank; primary regulators = FDIC, state DFI; persona = head of TPRM; source posture = public-plus-firm-policy; sector overlay = banking; cross-cutting overlays = cyber, privacy.
- **AI vendor**: false. The platform has an embedded summarisation feature for branch-staff workflows; the bank has not enabled it.

#### Output sketch

The skill produces a criticality assessment record. Headlines:

- **Service in scope and process supported** — core deposit-ledger and daily settlement; named IBS = deposit servicing.
- **RTO and RPO** — firm tolerance is 4h / 15 min; vendor commitment is 8h / 1h. `recovery_meets_firm_tolerance = no`. Surfaced as a finding for `contract-gap-review` and as a precondition for `vendor-diligence` to flag in operational-resilience evidence.
- **Customer impact** — `severity = severe`; populations = retail-deposit and small-business; harm modes = financial-loss, fairness on disputed transactions, complaint exposure on extended outage. The deposit-account holder cannot reach balances during outage; reputational damage compounds within hours.
- **Regulatory impact** — `severity = high`; regimes = bank-prudential and consumer-compliance; notification triggers = potential FDIC and state-DFI material-event reporting on sustained outage; Reg E and Reg DD customer-notice exposure if the outage induces a change-in-terms or fee-incidence event.
- **Operational impact** — `substitutability = hard`; time-to-restore on a forced cutover measured in months, not days; `manual_workaround_viable = false` (paper and IVR fallback exists for inquiry but not for transaction processing at scale beyond a short window).
- **Concentration considerations** — single core-platform vendor for the institution; raise the flag and pass portfolio analysis to `concentration-risk-review`.
- **Tier** — `critical`. Rationale names the IBS dependency, the customer-impact severity, the substitutability read, and the gap between firm tolerance and vendor commitment.
- **DORA flag** — `not-in-scope` (US-only firm, no EU nexus). Rationale recorded.
- **UK IBS flag** — `not-in-scope`.
- **Owner** — head of TPRM, with the deposit-product SVP as the business owner and the COO as the IBS owner per the firm's resilience policy. Approver per policy is the operational-risk committee for critical-tier arrangements.
- **Reviewer questions** — RTO/RPO gap closure path; manual-workaround testing cadence; exit-plan precondition before contract execution.
- **Next-review trigger** — contract-renewal, material-service-change, any IBS-impact-tolerance revision.

The record stops at the recommendation. The named approver decides.

#### Why this scenario matters

- **Tier set on impact, not spend.** A core-banking platform is critical because the IBS sits on it, not because of the contract value.
- **Vendor commitment is not the test.** The vendor's claimed RTO/RPO is a ceiling; the firm tolerance from the IBS analysis is the test. The gap is itself a finding.
- **Manual-workaround viability is load-bearing for the tier call.** Without it, "important" cannot survive contact with the firm's tolerance window.
- **Concentration is a flag here, not the analysis.** A single-arrangement assessment raises concentration; the portfolio call lives in `concentration-risk-review`.
- **DORA call is recorded explicitly even when negative.** US-only firm, no EU nexus, `not-in-scope`. The record carries the call and the rationale rather than leaving the field implied.

#### Anchors

- Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FRB/FDIC, June 2023).
- FFIEC IT Examination Handbook — Business Continuity Management booklet, business-impact analysis section.
- BCBS Principles for Operational Resilience (March 2021) on important business services.
- Reg DD (12 CFR Part 1030) and Reg E (12 CFR Part 1005) for the customer-notice clock context.

See `references/source-anchors.md` for full citations.

## eu-subsidiary-hris-payroll

### Example: HRIS SaaS supporting payroll for an EU subsidiary of a US insurer

Public-source-derived. No named vendor. The shape mirrors a common criticality call where a US-headquartered insurer's EU subsidiary procures an HRIS SaaS that runs payroll for the EU workforce. The arrangement falls inside DORA's perimeter as an ICT service to a financial entity but is not itself a high-criticality function.

#### Input

- **Arrangement**: a European HRIS SaaS providing core HR records, time-and-attendance, and monthly payroll calculation for the EU subsidiary's workforce. Payroll disbursement runs through the subsidiary's banking partner.
- **Business process supported**: workforce-payroll administration for the EU subsidiary.
- **Inputs already on file**: the insurer's IBS register (payroll is not on the IBS list; the regulated IBS list covers underwriting, claims, policy administration, and policyholder communications); the vendor's published certifications (ISO 27001, SOC 2 Type II); the subsidiary's regulatory profile.
- **Engagement scope supplied**: institution = EU subsidiary of US insurance group; primary regulators = the lead state insurance department (US) and the host EU competent authority; persona = head of TPRM with EU-subsidiary risk officer co-review; source posture = public-plus-firm-policy; sector overlay = insurance; cross-cutting overlays = privacy.
- **AI vendor**: false. The HRIS has no AI features in scope.

#### Output sketch

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

#### Why this scenario matters

- **Tier and DORA flag are separate calls.** The firm's tier ("important") and the DORA critical-or-important-function flag ("no") are derived from different criteria and recorded separately, with rationale on each. Treating them as one call collapses the record.
- **In-scope-of-register is not the same as critical-or-important.** The arrangement still lands in the DORA register because it is an ICT service to a financial entity. The criticality flag inside the register is a different field.
- **Cross-border lens enters via the cross-cutting privacy overlay.** Privacy applies because the arrangement processes regulated personal data of EU residents. Sector overlay is insurance because the regulated firm is an insurer; the work touches both.
- **Substitutability and manual-workaround viability change the tier read.** A vendor processing the same data category at a higher-criticality function (e.g., policy administration) would land at `critical` under the same evidence pack. The IBS dependency drives the tier, not the vendor's category.

#### Anchors

- Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FRB/FDIC, June 2023) on risk-based criticality.
- DORA Regulation (EU) 2022/2554, Article 28 general principles and the EBA-defined notion of critical or important function.
- EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02) on the assessment criteria for criticality.
- BCBS Principles for Operational Resilience (March 2021) on important business services.
- NAIC Insurance Holding Company System Regulatory Act (Model #440) for the holding-company-act lens on intragroup arrangements where applicable.

See `references/source-anchors.md` for full citations.

## troubleshooting

### Troubleshooting: criticality-assessment

Recurring pitfalls. Read before producing the assessment and again before sign-off.

#### Tier-setting pitfalls

##### Using vendor spend or vendor headcount as a proxy for criticality

Spend is not impact. A low-spend vendor on the customer-facing path can be critical. A high-spend vendor that runs a non-IBS internal process can be not-critical. The IBS dependency, customer-impact severity, and substitutability read drive the tier.

##### Setting RTO and RPO to the vendor's commitment rather than the firm's tolerance

The vendor's commitment is the ceiling on what the vendor delivers. The firm's tolerance comes from the IBS impact analysis and is the test the vendor must meet. `recovery_meets_firm_tolerance = yes` only when the vendor's commitment meets the tolerance. A gap is itself a finding for `contract-gap-review` and a precondition for `vendor-diligence` to evidence operational-resilience posture.

##### Letting the procurement category drive the tier

"IT services" is not a tier. "Cloud" is not a tier. "Professional services" is not a tier. The tier is set by impact on the IBS, customer, and regulator. The procurement category may correlate with tier; it does not determine it.

##### Skipping the manual-workaround viability test

The criticality call depends on whether the firm can keep the supported process running without the vendor for the full tolerance window. Without this test the substitutability read is incomplete and the tier is unreliable. `manual_workaround_viable = true` is a high bar and uncommon for vendors on the IBS chain.

#### DORA and jurisdictional pitfalls

##### Treating "DORA critical or important function" and the firm's own tier as identical

The criteria differ. The firm's tier reflects the firm's IBS map, customer-impact framework, and substitutability read. The DORA critical-or-important-function call applies the EBA-defined criteria. Where DORA applies, record both calls separately with rationale on each. Collapsing them is a documentation defect that propagates to the DORA register.

##### Confusing "in scope of the DORA register" with "DORA critical or important function"

An ICT service to a financial entity in the DORA perimeter belongs in the register regardless of criticality. The critical-or-important-function flag is a separate field on the register entry. Many register entries are ICT services that are not critical or important functions; the flag is `no` and the rationale is recorded.

##### Defaulting the DORA call to "not-in-scope" without checking entity perimeter

Where the firm or its EU subsidiary is in DORA scope, every ICT arrangement gets the call (`yes`, `no`, or both calls separately if multiple entities are affected). `not-in-scope` is reserved for entities outside the DORA perimeter.

##### Missing the UK PRA SS2/21 overlay for UK-licensed firms

If the firm is UK-licensed, the IBS framing and impact-tolerance test are UK-overlay items. `uk_ibs_flag = yes | no` per the firm's UK IBS map; `not-in-scope` only for firms outside the UK perimeter.

#### Engagement-scope pitfalls

##### Running without scope

If the scope record is missing, ask the four questions (institution type, primary regulator(s), persona/audience, source posture) and default to public posture if the practitioner declines. Note in the artifact that scope was not formalised. Do not silently apply a default sector overlay.

##### Loading the wrong sector overlay

Institution type and primary regulator constellation determine the sector overlay set. Banking is not insurance is not capital markets is not payments-fintech. A dual-registrant or a fintech with a sponsor bank may need two overlays.

##### Setting the tier and walking away

The criticality call is revisited on contract renewal, on material change to the service, on material change to the IBS, and on annual recertification per the firm's policy. Record the next-review trigger explicitly. A criticality call without a next-review trigger is incomplete.

#### Output discipline

##### Citing without sections

Every regulator citation in the assessment carries a section reference or a `[verify section]` placeholder. URL alone fails the source-anchor depth check. Use `references/source-anchors.md` for the canonical citation set; do not restate excerpts in the assessment body.

##### Marking unsupported claims silently

Use `[evidence needed]` explicitly. An inferred claim presented as evidenced is the failure mode. Tier rationale that reads as authoritative without a cited source is the most common version of this defect.

##### Treating the assessment as the decision

The assessment stops at the recommendation. The named approver decides under the firm's third-party-risk policy for the proposed tier. The skill outputs a `tier` and `tier_rationale`; the formal sign-off lives downstream.

##### Closing with too much certainty

The confidence label is `high` only when the IBS map, the impact tolerance, and the customer-impact and regulatory-impact reads are all anchored in firm-of-record evidence. `medium` and `low` are normal for early-stage assessments and for arrangements where the firm has not yet formalised an IBS map. `unknown` is honest where the criteria are unresolved.
