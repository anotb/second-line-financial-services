# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## cloud-iaas-regional-bank

### Example: Cloud IaaS contract for a regional U.S. bank

Public-source-derived. No named vendor. The shape mirrors a common matrix at a $50-100B regional bank reviewing a master cloud-services agreement (MSA) and its order form for a primary IaaS arrangement.

#### Input

- **Vendor**: a U.S.-incorporated hyperscale cloud provider; the contracting entity is a Delaware-incorporated subsidiary of the parent group. Two regions in scope; carrier-side data residency commitments.
- **Service**: IaaS plus selected PaaS (managed Kubernetes, managed PostgreSQL, object storage). Used to host the bank's deposit and consumer-loan core platforms.
- **Inputs already on file**: criticality-assessment record (criticality = critical; the deposit core sits on the IBS critical chain); the vendor's standard MSA (current edition); the order form; the financial-services addendum and the data-protection addendum; the bank's third-party-risk policy citing the U.S. interagency third-party guidance, the OCC Heightened Standards under 12 CFR Part 30 Appendix D, and Bank Service Company Act §1867(c).
- **Engagement scope supplied**: institution = state member bank; primary regulators = FRB, state DFI; persona = head of TPRM coordinating with general counsel and the CISO; source posture = public-plus-firm-policy-plus-system-of-record-evidence; sector overlay = banking; cross-cutting overlays = cyber, privacy.
- **AI vendor**: false. The IaaS arrangement does not include the vendor's foundation-model API service in this order form. If the bank later adds the foundation-model service to the order form, the matrix is re-opened with `ai_vendor = true` and the AI clause cluster is applied.
- **Digital-operational-resilience-act in scope**: false (U.S. bank, no EU subsidiary in scope of this contract). The mandatory-clause overlay does not load.

#### Output sketch

The skill produces a contract gap matrix. Headlines:

- **Arrangement and criticality** — critical-tier vendor; deposit and consumer-loan core platforms hosted; NPI in scope (account numbers, balances, dispute narratives, transaction history); two regions in scope; cross-border flows enabled by the order form's region selection (carrier-side region pin in the data-protection addendum is the operative restriction).

- **Applicable regimes and overlay set** — banking sector overlay loaded; cyber and privacy cross-cutting overlays loaded; mandatory-clause overlay not loaded.

- **Audit and reporting rights (clause-row 3, 4)** — MSA defaults the audit-right clause to "the audit reports the vendor publishes" (SOC 2 Type II summary plus the vendor's compliance-portal artefacts). No on-site posture; no third-party-auditor acceptability; cost-allocation silent. Marked `partial`. Recommended amendment posture: tighten to scope-frequency-cost-allocation language with a defined remedy when auditor findings dispute vendor representations. Severity: `high` for a critical vendor.

- **Regulator examination access (clause-row 4)** — the financial-services addendum includes a regulator-examination-access clause for U.S. federal banking regulators, but it is conditioned on prior notice and reasonable cooperation with the vendor's process. The Bank Service Company Act §1867(c) anchor requires unconditional examiner access. Marked `partial`. Recommended amendment posture: remove the prior-notice conditioning; preserve §1867(c) reach including continuity through wind-down. Severity: `high` (banking-only clause expectation; the §1867(c) row is mandatory-by-source).

- **Cybersecurity-event-notification clock (cyber cluster, C1)** — the data-protection addendum sets the vendor-to-firm notification window at "without undue delay, and in any case as required under applicable law". The bank is a NYDFS Covered Entity through its New York state branch network; the §500.17(a) 72-hour clock is operative. The contract clock does not close upstream because "applicable law" is the vendor's read of applicable law, not the bank's. Marked `partial`. Recommended amendment posture: tighten to vendor-to-firm notification within 48 hours of vendor confirmation, defined upstream of the §500.17(a) 72-hour clock; align with the SEC Item 1.05 four-business-day determination window for the bank-holding-company. Severity: `high`.

- **Sub-region change clause (privacy cluster, P5; subcontracting findings)** — the order form's region selection can be changed by the vendor with 30 days' notice without the bank's consent if the change is "to maintain service availability". The data-residency commitment is therefore conditional. Marked `partial`. Recommended amendment posture: require the bank's prior consent for any region change touching NPI, irrespective of availability rationale; preserve the bank's right to terminate without penalty if consent is withheld. Severity: `medium`, lifted to `high` by aggregation with the cross-border-flow row.

- **Sub-processor identification, change-notice, rejection (subcontracting findings)** — current sub-processor list is published on the vendor's compliance portal; change-notification by portal-update only, no push-notification, no rejection right. Marked `partial`. Recommended amendment posture: contractual push-notification 30 days before sub-processor change with rejection right and termination-for-convenience trigger if rejection is sustained. Severity: `medium`.

- **Termination for cause triggers (termination findings)** — the MSA includes SLA-failure, insolvency, and material-breach triggers. Missing: regulatory-action trigger (no termination right tied to a consent order, MRA, or supervisory recommendation); no licence-loss trigger (the vendor is not a licensed entity in any banking sense, but the bank's regulator-action posture should still trip a termination-for-convenience clause). Marked `partial`. Recommended amendment posture: add regulatory-action trigger; tighten termination-for-convenience to a defined notice window. Severity: `medium`.

- **Transitional-support obligation (termination findings)** — the MSA commits to "reasonable cooperation" for up to 90 days post-termination. Critical-tier vendors typically need 12 months of evidence-handover and exit-execution support, with cost-allocation defined upfront. Marked `partial`. Recommended amendment posture: extend to 12 months minimum with named scope (data-portability format, evidence handover, parallel-run support if needed); cost-allocation defined upfront. Severity: `high` (exit-plan workflow consumes this row; absence breaks the exit posture).

- **Limit of liability (liability findings)** — capped at 12 months of fees paid for the affected service. The bank's expected loss in a sustained-outage or major-data-incident scenario is multiples of that cap. Carve-outs: confidentiality breach (capped at 24 months fees), data breach (capped at 24 months fees), IP infringement (uncapped). Marked `partial`. Recommended amendment posture: surface to the bank's risk-acceptance forum; the cap below expected loss is a finding, not a deal-closer. Severity: `high` (cap-below-expected-loss flag is on; risk-acceptance documentation required).

- **Mandatory-clause overlay** — section omitted (`dora_in_scope = false`).

- **Summary severity** — `high`. Multiple `high`-severity findings on audit, regulator access, incident notification, transitional support, and liability cap. Recommended posture: `redline-and-defer-decision`. Conditions: §1867(c) clause inserted unconditional; cybersecurity-event-notification clock tightened; sub-region change consent required; transitional-support extended to 12 months; risk-acceptance documentation on the liability cap. Counsel-of-record: in-house banking counsel plus external counsel for the §1867(c) and limitation-of-liability redlines. Approver: head of TPRM and general counsel jointly per the firm's policy for critical-tier vendors.

The matrix stops at the recommended posture and the conditions. Counsel drafts language; the named approver decides.

#### Why this scenario matters

- **Boundary check on banking sector overlay**: §1867(c) is a banking-only clause expectation. Without the banking overlay, the matrix misses the row or treats the conditional examiner-access clause as sufficient. The banking overlay surfaces the unconditional reach as the source criterion.
- **Boundary check on the upstream cybersecurity-event-notification clock**: a "without undue delay" clause does not close upstream of the bank's NYDFS §500.17(a) 72-hour clock and SEC Item 1.05 four-business-day clock. The cyber overlay tightens the row.
- **Boundary check on sub-region change consent**: data-residency commitments that the vendor can modify unilaterally are conditional commitments. The privacy overlay surfaces the row.
- **Boundary check on liability cap**: a 12-months-fees cap below the bank's expected loss is a finding, not a deal-closer. The matrix surfaces the row to the risk-acceptance forum; it does not gate the contract.
- **Boundary check on the digital-operational-resilience-act in-scope flag**: a U.S.-only deposit-core IaaS arrangement is not in scope of the EU act. The mandatory-clause overlay is omitted; the matrix is built off the U.S. interagency frame plus the banking and cyber overlays.

#### Anchors

- Interagency Guidance on Third-Party Relationships: Risk Management (OCC / FRB / FDIC, June 2023).
- Bank Service Company Act, 12 USC §1867(c).
- 12 CFR Part 30 Appendix D (OCC Heightened Standards).
- 12 CFR Part 30 Appendix B (Interagency Guidelines on Safeguarding Customer Information).
- FFIEC IT Examination Handbook — Outsourcing Technology Services and Information Security booklets.
- FFIEC Joint Statement on Risk Management of Cloud Services (April 2020).
- NYDFS 23 NYCRR §§500.11, 500.17.
- SEC final rule on cybersecurity disclosure (Item 1.05 Form 8-K, Reg S-K Item 106).

See `references/source-anchors.md` for full citations and `references/sector-overlays.md#banking` and `references/cross-cutting.md#cyber` for the overlay-specific anchors.

## dora-saas-eu-collections

### Example: Digital-operational-resilience-act-in-scope SaaS contract for an EU subsidiary's collections platform

Public-source-derived. No named vendor. The shape mirrors a common matrix at the EU subsidiary of a multinational financial group reviewing a SaaS agreement for a collections-and-recoveries platform that supports the subsidiary's consumer-credit portfolio.

#### Input

- **Vendor**: an EU-incorporated SaaS provider (Ireland) offering a collections-and-recoveries workflow platform with hosted analytics, agent-workspace, and customer-communication tooling. Hosted on a hyperscaler's EU regions; sub-processor list includes the hyperscaler, an SMS gateway provider, and an email-deliverability provider.
- **Service**: collections workflow management; debtor segmentation analytics; agent telephony integration; customer-communication channel orchestration. Outputs feed the subsidiary's debt-recovery operations across consumer-credit and SME portfolios.
- **Inputs already on file**: criticality-assessment record (criticality = important under the firm's taxonomy; classified as critical-or-important-function ICT service under the EU digital-operational-resilience act because the platform supports a function whose disruption would materially impair the subsidiary's regulated activity); SOC 2 Type II report; ISO 27001 certificate; the proposed enterprise contract (master agreement, data-processing addendum, security addendum); the parent group's third-party-risk policy referencing the EU digital-operational-resilience act, the European banking authority outsourcing-arrangements guidelines, and the parent's internal contract paper standards.
- **Engagement scope supplied**: institution = EU subsidiary of a multinational banking group, with consumer-credit licence in member state of incorporation and passporting rights across selected EU member states; primary regulators = the local national competent authority and the European banking authority via consolidated supervision; persona = head of operational resilience coordinating with general counsel and the CISO; source posture = public-plus-firm-policy-plus-system-of-record-evidence; sector overlay = banking; cross-cutting overlays = cyber, privacy.
- **AI vendor**: false. The platform's analytics module uses statistical segmentation, not foundation-model AI. (If the subsidiary later enables the platform's optional AI-summarisation feature for agent-workspace narratives, the matrix is re-opened with `ai_vendor = true`.)
- **Digital-operational-resilience-act in scope**: true. Critical-or-important-function ICT service. The mandatory-clause overlay loads.

#### Output sketch

The skill produces a contract gap matrix with the mandatory-clause overlay populated. Headlines:

- **Arrangement and criticality** — important-tier vendor under the firm's taxonomy; critical-or-important-function ICT service under the EU digital-operational-resilience act; collections-platform supports a regulated activity (debt recovery on consumer-credit accounts under the firm's local consumer-credit licence); NPI in scope (debtor identifiers, account balances, communication records); EU-only data residency in the data-processing addendum.

- **Applicable regimes and overlay set** — banking sector overlay loaded; cyber and privacy cross-cutting overlays loaded; mandatory-clause overlay loaded.

- **Mandatory-clause overlay (M1-M6)** — the matrix surfaces the enhanced clause set as `high`-severity-by-source rows:
  - **M1 termination rights tied to supervisory recommendation** — the master agreement includes termination for material breach and insolvency but does not include a right to terminate on the firm's competent authority's recommendation. Marked `absent`. Recommended amendment posture: add the supervisory-recommendation termination trigger; absence is mandatory-by-source. Severity: `high`.
  - **M2 full description of services** — the order form references "the platform" without a defined-services schedule. Marked `partial`. Recommended amendment posture: attach a defined-services schedule covering modules, sub-modules, integration points, and SLAs. Severity: `high`.
  - **M3 locations of data processing and storage** — the data-processing addendum names "EU regions" without specifying the cities or data centres. Marked `partial`. Recommended amendment posture: name the specific regions and data centres in the addendum; require firm consent for any change. Severity: `high`.
  - **M4 sub-outsourcing notification timing and rejection rights** — the addendum requires 60 days' notice for material sub-processor changes but no rejection right. Marked `partial`. Recommended amendment posture: tighten notification timing to align with the firm's competent authority's expectations; add rejection right with termination-for-convenience trip if rejection is sustained. Severity: `high`.
  - **M5 exit-strategy and transitional support** — the master agreement commits to "reasonable cooperation" for up to 6 months post-termination. The European banking authority guidelines and the EU act expect a tested exit strategy with transitional-period support sized to the criticality of the function. Marked `partial`. Recommended amendment posture: extend transitional support to 12 months minimum with named scope, defined cost-allocation, and parallel-run support during the transitional period; require the vendor to support the firm's documented exit-plan workflow. Severity: `high` (exit-plan workflow consumes this row; absence breaks the exit posture).
  - **M6 audit-and-access for the firm and the competent authority** — the security addendum includes audit rights for the firm but conditions competent-authority access on the vendor's process. Marked `partial`. Recommended amendment posture: unconditional access for the firm and the competent authority, with cost-allocation defined and on-site posture preserved. Severity: `high`.

- **Cybersecurity-event-notification clock (cyber cluster, C1)** — the security addendum sets vendor-to-firm notification at "without undue delay and in any event within 72 hours". The firm's incident-reporting timetable under the EU act is the operative upstream clock; the vendor's 72-hour window does not give the firm enough margin for triage and onward reporting. Marked `partial`. Recommended amendment posture: tighten to vendor-to-firm notification within 24 hours of vendor confirmation. Severity: `high`.

- **Sub-processor list and change-notice (privacy cluster, P2; subcontracting findings)** — current sub-processor list is referenced in the addendum and published on the vendor's portal; change-notification by portal-update plus email; rejection right is present but conditioned on the firm proposing an alternative sub-processor. Marked `partial`. Recommended amendment posture: remove the alternative-proposal condition on rejection; align change-notice timing with the M4 row. Severity: `medium`.

- **Cross-border-transfer mechanism (privacy cluster, P5)** — the data-processing addendum addresses cross-border-transfer through standard contractual clauses for any onward transfer outside the EEA, but does not include a transfer-impact-assessment cooperation commitment. Marked `partial`. Recommended amendment posture: add transfer-impact-assessment cooperation; define the firm's audit reach into onward-transfer chains. Severity: `medium`.

- **Termination findings** — termination-for-convenience present with 90-day notice; termination-for-cause triggers include SLA-failure, security-incident, insolvency, and material-breach; missing the supervisory-recommendation trigger (covered by M1) and the regulatory-action trigger more broadly. Recommended amendment posture: add the regulatory-action trigger; align with M1.

- **Liability findings** — limit of liability capped at one year of fees; carve-outs include confidentiality breach, data breach, IP infringement, gross negligence, and willful misconduct; insurance evidence sufficient. The cap is below the firm's expected loss in a sustained-outage scenario; risk-acceptance documentation required. Severity: `high` for the cap-below-expected-loss flag.

- **Audit findings** — audit rights present for the firm; competent-authority access conditional (covered by M6); performance reporting cadence defined (monthly); problem-reporting posture present.

- **Summary severity** — `high`. The mandatory-clause overlay raises six `high`-severity-by-source rows; the cyber and privacy clusters raise additional rows. Recommended posture: `redline-and-defer-decision`. Conditions: all six mandatory-clause rows redlined to satisfaction; cybersecurity-event-notification clock tightened to 24 hours; sub-processor rejection right unconditioned; cross-border transfer-impact-assessment cooperation added; risk-acceptance documentation on the liability cap. Counsel-of-record: the EU subsidiary's general counsel plus the parent group's external counsel on the digital-operational-resilience-act compliance read. Approver: head of operational resilience and general counsel jointly per the firm's policy for critical-or-important-function ICT services.

The matrix stops at the recommended posture and the conditions. Counsel drafts language; the named approver decides.

#### Why this scenario matters

- **Boundary check on the digital-operational-resilience-act in-scope flag**: any contract supporting a critical-or-important-function ICT service in scope of the act picks up the mandatory-clause overlay regardless of the firm's internal criticality taxonomy. The matrix surfaces the M1-M6 rows as `high`-severity-by-source.
- **Boundary check on the cybersecurity-event-notification clock**: the act's incident-reporting timetable is operative. A 72-hour vendor-to-firm window does not give the firm enough margin; the cyber overlay tightens.
- **Boundary check on the exit-strategy commitment**: the M5 row is mandatory-by-source. A 6-month "reasonable cooperation" clause is not enough for a critical-or-important-function service; the matrix surfaces the row to the exit-plan workflow.
- **Boundary check on competent-authority access**: the audit-rights row for the firm is distinct from the competent-authority access row. Both must be unconditional under M6.
- **Boundary check on transfer-impact-assessment cooperation**: cross-border-transfer mechanism is a privacy-overlay row; transfer-impact-assessment cooperation is a separate sub-row that the addendum often misses.

#### Anchors

- DORA — Regulation (EU) 2022/2554, Articles 28-30 key contractual provisions.
- EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02).
- GDPR (Regulation (EU) 2016/679) where the data-processing addendum reaches.
- The European banking authority's guidelines on ICT and security risk management.

See `references/source-anchors.md` for full citations and `references/cross-cutting.md#cyber` and `references/cross-cutting.md#privacy` for the overlay-specific anchors.

## troubleshooting

### Troubleshooting: contract-gap-review

Recurring pitfalls. Read before producing the gap matrix and again before sign-off.

#### Reading the contract

##### Treating "right to audit subject to reasonable cooperation" as audit rights

Reservation of vendor discretion. Audit rights need scope, frequency, cost-allocation, on-site posture, third-party-auditor acceptability, and a remedy when auditor findings dispute vendor representations. Mark `partial` and surface the missing components as a single row, not as five rows that all read "absent".

##### Treating "industry-standard SLA" as sufficient

Industry-standard often means below the firm's tolerance. Compare against the criticality output's RTO and RPO tolerance, not the vendor's default. Mark `partial` and recommend tightening to the firm's tolerance band.

##### Missing the cybersecurity-event-notification clock mismatch

The contract clock must close upstream of the tightest applicable regulatory clock: the firm's public-company materiality determination window where listed; the New York State 72-hour cybersecurity-event-notification clock where the firm is a covered entity; the EU digital-operational-resilience-act major-ICT-related-incident reporting timetable where in scope; the GLBA Safeguards 30-day customer-notice clock where amended 314 reaches; the HIPAA 60-day breach-notification clock where PHI is in scope. Always a finding for a vendor touching NPI, PHI, PCI, or IBS controls.

##### Treating sub-processor flow-down as visibility

Flow-down is a contractual mechanic. The contract must also require sub-processor identification (current list, not just "available on request"), change-notification with timing, and rejection rights. These are separate rows.

##### Skipping exit-and-transition clauses for a "non-critical" arrangement

Even non-critical arrangements need basic data-return and deletion clauses for privacy compliance. Do not gate exit clauses entirely on criticality; gate the depth.

##### Confusing limit-of-liability caps with risk transfer

A liability cap below the firm's expected loss is a finding, not a deal-closer. Surface the cap-below-expected-loss flag and require risk-acceptance documentation. The matrix does not gate the contract on this row alone.

##### Missing the regulator-examination-access continuity clause

For banking arrangements, the Bank Service Company Act §1867(c) reach must be unconditional and must survive termination through the records-retention period. A regulator-access clause conditioned on prior notice or on the vendor's process is a `partial` finding and a `high`-severity row.

#### Mandatory-clause overlay

##### Skipping the overlay because the firm taxonomy says "important", not "critical"

The EU digital-operational-resilience-act in-scope flag is a function classification (critical-or-important-function ICT service), not the firm's internal criticality tier. An "important"-tier vendor under the firm's taxonomy can be in scope of the act; the mandatory-clause overlay loads off the in-scope flag, not the firm tier.

##### Treating the M1-M6 rows as recommendations

The mandatory-clause rows are mandatory-by-source for an in-scope arrangement. Absence is `high`-severity-by-source regardless of the firm's bilateral position. Do not soften the severity on the strength of a strong commercial relationship.

##### Conflating "EU regions" with named locations of data processing

The M3 row requires named locations (cities, data centres), not regions. A "EU regions" clause is `partial`, not `present`.

##### Reading audit rights for the firm as audit rights for the firm and the competent authority

The M6 row covers both the firm and the competent authority. The clauses are distinct; coverage must be assessed separately.

#### Sector overlays

##### Applying the bank-flavoured interagency-guidance frame to a non-bank registrant

The non-bank registrant's contract clause set comes through 206(4)-7, 38a-1, FINRA 3110, and the rule-specific contract reach (Custody Rule, books-and-records, Reg S-P, Reg SCI). The matrix must build off the right frame; do not paste the bank checklist onto an adviser, fund, or BD contract.

##### Missing the §4.F clause set on a TPA or MGA contract

The federal interagency-guidance frame does not cover NAIC Insurance Data Security Model Law §4.F third-party-service-provider contract terms. Where adopted, the §4.F clauses are mandatory-by-source.

##### Missing the BaaS clause expansions

The standard generic clause set undercovers BaaS. The payments-fintech overlay adds the FBO subledger, end-customer reconciliation, deposit-insurance representation, customer-liability allocation, complaint-handling, and data-portability rows.

##### Loading one sector overlay where the arrangement spans two

A dual-registrant contract or a sponsor-bank-program contract may need two sector overlays. Flag the choice in the scope record; do not collapse to one.

#### AI-vendor mode

##### Treating an "embedded AI feature" as automatically AI-vendor mode

If the AI feature is off and the firm has no plan to turn it on, the matrix is not in AI-vendor mode. Mark `ai_vendor = false` and add a re-review trigger if the feature is enabled. Do not pull the AI clause cluster in by reflex.

##### Missing the model-version pin and deprecation-notice clock

For foundation-model arrangements, the deployed checkpoint is a moving target. The contract must address model-version pinning and deprecation-notice timing; absence is a finding regardless of the firm's read on the vendor's stability.

##### Reading "we do not retain training data" without reading the abuse-monitoring exception

The enterprise default is rarely the consumer default; the contract addendum and the trust-and-safety pages set the operative posture. The matrix cites the contractual data-handling commitment and the abuse-monitoring exception, not the marketing default.

#### Engagement-scope handling

##### Running without scope

If the scope record is missing, ask the four questions (criticality tier, AI-vendor flag, regulatory profile, review type) and default to public posture if the practitioner declines. Note in the matrix that scope was not formalised. Do not silently apply a default sector overlay.

##### Skipping cyber or privacy because "the contract is not a cyber or privacy contract"

Cyber applies whenever the contract touches NPI, PHI, PCI, customer prompts, or any control on the firm's important-business-service path. Privacy applies whenever the contract reaches regulated personal data, including customer prompts. Both default-on for AI vendors.

#### Output discipline

##### Citing without sections

Every regulator citation in the matrix carries a section reference or a `[verify section]` placeholder. URL alone fails the source-anchor depth check. Use `references/source-anchors.md` for the canonical citation set; do not restate excerpts in the matrix body.

##### Marking unsupported findings silently

Use `[evidence needed]` explicitly. An inferred finding presented as evidenced is the failure mode.

##### Closing with too much certainty

The confidence label is `high` only when the source posture, the evidence set, and the severity rollup line up. `medium` and `low` are normal for early-stage matrices; `unknown` is honest where the firm has not yet resourced the evidence ask.

##### Drafting language instead of posture

The matrix records the recommended-amendment posture (a posture, not legal language). Counsel drafts language; the matrix names what the language must do. A posture that reads like a contract clause is over-stepping the skill's role.

##### Approving the contract

The matrix stops at the recommended posture and the conditions. Counsel drafts language; the named approver decides. The skill outputs `recommended_posture`, not `decision`.
