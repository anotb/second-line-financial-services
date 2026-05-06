# Example: Cloud IaaS contract for a regional U.S. bank

Public-source-derived. No named vendor. The shape mirrors a common matrix at a $50-100B regional bank reviewing a master cloud-services agreement (MSA) and its order form for a primary IaaS arrangement.

## Input

- **Vendor**: a U.S.-incorporated hyperscale cloud provider; the contracting entity is a Delaware-incorporated subsidiary of the parent group. Two regions in scope; carrier-side data residency commitments.
- **Service**: IaaS plus selected PaaS (managed Kubernetes, managed PostgreSQL, object storage). Used to host the bank's deposit and consumer-loan core platforms.
- **Inputs already on file**: criticality-assessment record (criticality = critical; the deposit core sits on the IBS critical chain); the vendor's standard MSA (current edition); the order form; the financial-services addendum and the data-protection addendum; the bank's third-party-risk policy citing the U.S. interagency third-party guidance, the OCC Heightened Standards under 12 CFR Part 30 Appendix D, and Bank Service Company Act §1867(c).
- **Engagement scope supplied**: institution = state member bank; primary regulators = FRB, state DFI; persona = head of TPRM coordinating with general counsel and the CISO; source posture = public-plus-firm-policy-plus-system-of-record-evidence; sector overlay = banking; cross-cutting overlays = cyber, privacy.
- **AI vendor**: false. The IaaS arrangement does not include the vendor's foundation-model API service in this order form. If the bank later adds the foundation-model service to the order form, the matrix is re-opened with `ai_vendor = true` and the AI clause cluster is applied.
- **Digital-operational-resilience-act in scope**: false (U.S. bank, no EU subsidiary in scope of this contract). The mandatory-clause overlay does not load.

## Output sketch

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

## Why this scenario matters

- **Boundary check on banking sector overlay**: §1867(c) is a banking-only clause expectation. Without the banking overlay, the matrix misses the row or treats the conditional examiner-access clause as sufficient. The banking overlay surfaces the unconditional reach as the source criterion.
- **Boundary check on the upstream cybersecurity-event-notification clock**: a "without undue delay" clause does not close upstream of the bank's NYDFS §500.17(a) 72-hour clock and SEC Item 1.05 four-business-day clock. The cyber overlay tightens the row.
- **Boundary check on sub-region change consent**: data-residency commitments that the vendor can modify unilaterally are conditional commitments. The privacy overlay surfaces the row.
- **Boundary check on liability cap**: a 12-months-fees cap below the bank's expected loss is a finding, not a deal-closer. The matrix surfaces the row to the risk-acceptance forum; it does not gate the contract.
- **Boundary check on the digital-operational-resilience-act in-scope flag**: a U.S.-only deposit-core IaaS arrangement is not in scope of the EU act. The mandatory-clause overlay is omitted; the matrix is built off the U.S. interagency frame plus the banking and cyber overlays.

## Anchors

- Interagency Guidance on Third-Party Relationships: Risk Management (OCC / FRB / FDIC, June 2023).
- Bank Service Company Act, 12 USC §1867(c).
- 12 CFR Part 30 Appendix D (OCC Heightened Standards).
- 12 CFR Part 30 Appendix B (Interagency Guidelines on Safeguarding Customer Information).
- FFIEC IT Examination Handbook — Outsourcing Technology Services and Information Security booklets.
- FFIEC Joint Statement on Risk Management of Cloud Services (April 2020).
- NYDFS 23 NYCRR §§500.11, 500.17.
- SEC final rule on cybersecurity disclosure (Item 1.05 Form 8-K, Reg S-K Item 106).

See `references/source-anchors.md` for full citations and `references/sector-overlays/banking.md` and `references/cross-cutting/cyber.md` for the overlay-specific anchors.
