# Banking sector overlay — contract-gap-review

When the engagement scope flags banking, load this overlay alongside `references/source-anchors.md`. It carries the banking-only clause expectations the generic capability skill does not own.

## Operative supervisory frame

- **Interagency Guidance on Third-Party Relationships: Risk Management** (OCC Bulletin 2023-17, FRB SR 23-4, FDIC FIL-29-2023, June 6, 2023). The contract-negotiation section is the spine of the banking gap matrix.
- **OCC Bulletin 2013-29** is still cited as the predecessor frame in supervisory practice. Where examiners reference it, treat as supplemental, not operative.
- **FFIEC IT Examination Handbook — Outsourcing Technology Services booklet** is the examiner-facing detail for technology-vendor contracts.
- **Comptroller's Handbook — Third-Party Relationships: Risk Management** [verify current edition] is the OCC examiner playbook for national banks and federal savings associations; the contract-issues section informs what an examiner expects to read in the matrix.
- **12 CFR Part 30 Appendix D (OCC Heightened Standards)** for $50B+ covered banks: contract gap matrix outputs feed the risk-governance framework and the board's third-party oversight. The matrix for an important or critical vendor should be visible to the independent risk-management function.

## Banking-only contract anchors

- **Bank Service Company Act, 12 USC §1867(c)** — statutory examiner-access right over bank service providers. The contract must preserve regulator examination access and audit rights into the vendor's records, systems, and personnel for the services performed for the bank. Banking-only clause expectation; flag any contract that lacks the clause as a `high`-severity finding regardless of vendor tier or other audit-rights language. The clause must include continuity through wind-down (the right survives termination for the records-retention period).

- **12 CFR Part 30 Appendix B (Interagency Guidelines Establishing Standards for Safeguarding Customer Information), III.D**. Service-provider arrangements: due diligence, contract requirements (information-security safeguards, monitoring), monitoring [verify subsection labels]. The contract clause cluster has a specific information-security floor here that pre-dates and is independent of the GLBA Safeguards Rule's FTC version.

## Reg O lens

- **Reg O, 12 CFR Part 215** — diligence on a vendor whose principals are insiders (directors, executive officers, principal shareholders) of the partner bank, or affiliates thereof, must include the Reg O screen, and the contract must be at arms-length on terms substantially the same as those for comparable transactions with non-insiders. The contract gap matrix surfaces a `high`-severity finding where the contract reads as a related-party arrangement without the substantive Reg O substantiation.

## BaaS and bank-fintech contract clauses

- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC, OCC, FRB, July 25, 2024) [verify exact title and date]: where the contract is a sponsor-bank program agreement or BaaS platform agreement, the clause set expands to: end-customer-reconciliation responsibilities and frequency; FBO subledger ownership, access, and reconciliation; deposit-insurance representation review (and customer-facing FDIC framing); program-operator operational-resilience commitments; the fourth-party register and the change-notice mechanism; BSA/AML responsibility allocation; customer-liability allocation under Reg E and Reg DD; complaint-handling chain; data-portability on termination. The standard generic clause set undercovers BaaS; the overlay adds the program-specific rows.

- **OCC Bulletin on Bank-Fintech Arrangements** [verify bulletin number]: where present in the firm's source list, treat as supplemental detail.

- **FFIEC inter-agency joint statement on community-bank fintech due diligence** (August 2023) [verify exact title]: for community banks engaging fintech partners; carries an explicit contract-checklist that runs alongside the interagency guidance.

## Reg E, Reg DD, and consumer-account close-out

- **Reg E (12 CFR Part 1005)** §1005.6, §1005.11, §1005.18 — error-resolution, customer-liability allocation, and prepaid-account rules. Contract must support the bank's ability to meet its Reg E obligations through the vendor's processes, including evidence handover for error-resolution determinations.
- **Reg DD (12 CFR Part 1030)** §1030.5 — change-in-terms and account-close-out customer-notification. Contract must support the bank's notification obligation on a vendor-driven account-close-out scenario.

## Cross-link inside the plugin

- **`exit-plan` banking overlay** carries the FBO-account wind-down sequence, the §1030.5 and §1005.8 customer-notification responsibilities, and §1867(c) examination-access continuity through wind-down. The contract gap matrix should evidence the contract clauses that enable each of those exit steps; the exit-plan workflow consumes the findings.
- **`vendor-diligence` banking overlay** carries the read-through on monitoring evidence; the contract gap matrix is the input on whether the contract gives the bank the rights to obtain that evidence.

## Common banking pitfalls

- Treating "audit rights subject to reasonable cooperation" as satisfying Bank Service Company Act §1867(c). It does not. The §1867(c) clause must explicitly preserve regulator examination access; bilateral audit-cooperation language is a separate row.
- Missing the FBO subledger and end-customer-reconciliation clause set in a sponsor-bank program contract. The standard generic clause set undercovers BaaS; the overlay adds the program-specific rows.
- Treating "industry-standard SLA" as sufficient for a critical vendor at a $50B+ covered bank. Heightened Standards Appendix D requires the board's third-party oversight to read against the firm's tolerance, not the vendor's default.
