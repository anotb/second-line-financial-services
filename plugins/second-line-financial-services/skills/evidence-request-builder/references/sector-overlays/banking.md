# Banking sector overlay — evidence-request-builder

Loaded when `scope.sector_overlay_set` includes `banking` or when the test addresses a banking regulator's rule. Does not replace `references/source-anchors.md`; supplements it with bank-specific evidence-request conventions.

## Request-list conventions banking testing programs apply

A bank consumer-compliance or operational-risk testing PBC list carries a few conventions beyond the methodology baseline:

- **System of record is named, not generic.** Loan origination system (LOS), customer-relationship-management system, deposit operations system, complaint-management system, BSA case-management system, IAM, AUS — name the system, not "internal database". The workpaper later relies on the same naming.
- **CSV asks name expected columns.** A LAR extract request, a transaction extract request, and a complaints extract request all carry the expected columns in the artifact description (FFIEC HMDA field labels, ACH transaction fields, complaints-data dictionary fields). "Send the LAR" without a column list is the request-shaping failure that triggers re-asks.
- **Reg-specific evidence has format conventions.** HMDA LAR extracts are CSV by FFIEC field labels; Reg E case files are PDF bundles per case ID; CIP / CDD evidence is per-customer packets; SAR-decision evidence carries the access-control posture without restating SAR content.
- **Reliance classification distinguishes vendor and management-prepared evidence.** AUS configuration extracts are vendor-supplied; quarterly LAR data-quality reconciliation logs are management-prepared. Both classifications drive workpaper reliance test notes.
- **Population reference ties the request to the sampling memo.** A request for "the LAR for sample IDs 1-60" or "the recertification packets for the privileged subset (full population) plus the 30-record stratified standard subset" is testable; a request for "the LAR" without a population reference is not.

## Bank-supervisory anchors (load by reference; do not restate)

- **CFPB Compliance Management Review** examination procedures inside the **CFPB Supervision and Examination Manual** (current edition) [verify section labels for the testing-program component]. https://www.consumerfinance.gov/compliance/supervision-examinations/ .
- **OCC Comptroller's Handbook — Compliance Management Systems** [verify current edition and section labels]. https://www.occ.gov/publications-and-resources/publications/comptrollers-handbook/index-comptrollers-handbook.html .
- **SR 08-8 — Compliance Risk Management Programs and Oversight at Large Banking Organizations with Complex Compliance Profiles** (Federal Reserve, October 16, 2008) [verify section labels for testing-program documentation]. https://www.federalreserve.gov/boarddocs/srletters/2008/sr0808.htm .
- **OCC PPM 5310-3 — Bank Supervision Process** [verify exact PPM number and current effective date].
- **12 CFR Part 30 Appendix D (OCC Heightened Standards)** for $50B+ covered banks [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-I/part-30 .
- **Bank Service Company Act, 12 USC §1867(c)** — examiner-access posture for bank service providers; cite when a request asks a bank service provider for evidence.

## Bank-control-area request notes

### HMDA / Reg C testing

- Reg C — 12 CFR Part 1003. §1003.4 data points, §1003.5 disclosure and reporting [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1003 .
- FFIEC HMDA Filing Instructions Guide (current edition) [verify edition year]. https://www.ffiec.gov/hmda/guide.htm .
- Request conventions: LAR record extracts are CSV with named columns matching FFIEC field labels; underlying loan files are per-sample PDF bundles (URLA, AUS findings, rate-lock confirmation, settlement statement, lien-position evidence); demographic-firewall evidence carries an IAM-extract scope (production, by role) plus the demographic-information form per sample. AUS configuration extracts are a separate request flagged vendor-supplied. Quarterly LAR data-quality reconciliation log is management-prepared and triggers the workpaper's completeness-and-accuracy check.

### CRA testing

- CRA — 12 CFR Part 25 (OCC), Part 228 (FRB Reg BB), Part 345 (FDIC) [verify current effective state given the 2023 final-rule litigation history]. https://www.federalreserve.gov/supervisionreg/regbbcg.htm .
- Request conventions: lending-test evidence requests draw geographic distribution extracts, borrower-profile distribution extracts, and product-mix distribution extracts; service-test and investment-test requests draw the qualified-investment register and branch-distribution evidence. Performance-context narrative is set out in the test plan rather than requested as evidence.

### Reg B / ECOA testing

- Reg B — 12 CFR Part 1002. §1002.4, §1002.5(b), §1002.6, §1002.9, §1002.13 [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1002 .
- Request conventions: adverse-action notice testing requests the underlying application file and the notice-issuance log per sample; spousal-signature testing requests the underwriting file (not just the front-end application) per sample; demographic-firewall testing requests the production-environment role-based access entitlement extract for any role with access to demographic information at underwriting (not the test environment).

### Reg DD, Reg E, Reg Z testing

- Reg DD — 12 CFR Part 1030 [verify subsection labels].
- Reg E — 12 CFR Part 1005 [verify subsection labels including §1005.11 procedures and §1005.18 prepaid].
- Reg Z — 12 CFR Part 1026 [verify subsection labels].
- Request conventions: error-resolution case files are PDF bundles per case ID with the dispute-management-system case extract attached; disclosure-content testing requests the production disclosure (PDF) plus the regulatory model for redline; periodic-statement testing requests sample statements per account ID with the statement-generation log.

### BSA/AML testing

- FFIEC BSA/AML Examination Manual (current edition) [verify last-revision date]. https://bsaaml.ffiec.gov/manual .
- 31 CFR Part 1010, 1020, 1022, 1023, 1024, 1025, 1026 (FinCEN AML rules by industry) [verify part references].
- 31 CFR §1010.230 (beneficial ownership for legal-entity customers) [verify subsection].
- Request conventions: CIP testing requests the new-account opening packet plus the documented identification-and-verification step per sample; CDD/EDD testing requests the customer-due-diligence questionnaire and the EDD enrichment evidence per sample; SAR-decision testing requests the case-management file from alert to disposition with timing checks against 31 CFR §1020.320 — SAR content access is restricted; the request notes the access-control posture rather than restating SAR content. Beneficial-ownership recertification testing requests the recertification form, certifier-attestation record, and any change-of-ownership trigger evidence per legal-entity sample.

### Sponsor-bank arrangements

- When the test addresses a bank-fintech partnership or a sponsor-bank deposit program, the request list draws against the **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date]: end-customer reconciliation evidence (FBO subledger versus fintech program ledger), deposit-insurance representation evidence (account-opening, T&Cs, marketing), and the fourth-party register evidence.
- Bank Service Company Act, 12 USC §1867(c) examiner-access posture is cited where the firm relies on the BSCA-covered contract to field a request to a bank service provider.

## Audience and tone

A request list drafted ahead of an upcoming OCC, FRB, FDIC, or CFPB exam reads heavier on the regulator-acknowledgement evidence (resubmission logs, prior-cycle remediation evidence) and on the named system-of-record discipline. A request list drafted for in-cycle internal testing reads operationally with the same evidence base; the methodology bar is the same, only the rendering audience changes.
