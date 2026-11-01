# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — evidence-binder

Loads when the scope `sector_overlay_set` includes `banking`. Binds evidence-binder content to bank-supervisory expectations.

#### Supervisory frame

US bank examiners (OCC, FRB, FDIC) work from request lists (RFIs) typically issued at exam open and supplemented during fieldwork. The binder's `request_list` is the canonical reconciliation surface for these RFIs. State DFIs follow a similar pattern; for state-member banks, the FRB and the state share supervision and the binder may carry items from both.

The FFIEC IT Examination Handbook (Audit booklet, April 2012) frames evidence sufficiency for IT and third-party audit programs. Audit evidence is read against the program's design and the institution's risk profile; the binder cites the booklet section by reference, not by excerpt.

For OCC large-bank populations, 12 CFR Part 30 Appendix D (Heightened Standards) sets framework-level expectations that bear on what the binder must support: independent risk management evidence, board-level oversight evidence, risk-appetite-statement evidence, and chief-risk-executive evidence.

#### Recordkeeping and retention

- Bank Service Company Act, 12 USC §1867(c): examiner-access expectations for third-party-provided services. Vendor-evidence rows in the binder reference the contract clause that gives the examiner access; if the clause is missing, the binder surfaces a gap.
- 12 CFR §1010 (FinCEN BSA recordkeeping): five-year retention floor for BSA records. Binder rows for BSA evidence carry a period_start that respects the five-year window even when the examination period is shorter, because the underlying records must be available.
- FFIEC IT Audit booklet: retention expectations for audit workpapers vary by program; a typical floor is the longer of the firm's internal policy or the supervisory cycle (commonly seven years for federally regulated institutions).

#### Common request-list shapes

Federal exam RFIs typically cluster around: governance and oversight (board minutes, committee minutes, charter, policy versions), risk management (risk-appetite statement, KRI dashboards, KRI breach log), controls (control inventory, testing results, exception register), audit (internal-audit plan, prior-period workpapers, follow-up status), data and reporting (BCBS 239 conformance evidence for the relevant institutions, data-quality metrics, lineage documentation), and third-party (TPRM inventory, criticality determinations, vendor diligence packs, SOC reports, exit plans).

The binder reconciles each cluster against the evidence index. Cluster-level gaps appear in the gaps section even when individual requests within the cluster are met.

#### BCBS 239 traceability

For G-SIBs and D-SIBs, BCBS 239 Principles 3 (accuracy and integrity), 4 (completeness), and 7 (accuracy of risk reporting) bear on the binder when risk-data evidence is in scope. Binder rows for risk-data extracts cite the BCBS 239 principle they support and the firm's data-lineage record where one exists.

#### Sign-off and review-gate norms

A bank-exam binder is signed by the chief compliance officer or chief risk officer (depending on the exam type) before it is presented to the examiner-in-charge. Internal-audit fieldwork binders are signed by the audit director and the in-charge auditor. The binder's `sign_off` field carries the role.

#### Anchors used by this overlay

- 12 CFR Part 30 Appendix D — OCC Heightened Standards [verify section labels].
- Bank Service Company Act, 12 USC §1867(c).
- FFIEC IT Examination Handbook, Audit booklet (April 2012) §§III, IV.B [verify section labels].
- FinCEN BSA recordkeeping, 31 CFR §1010.430 (general), 31 CFR §1020 series (banks).
- BCBS 239, January 2013, Principles 3, 4, 7.
- SR 11-7 / OCC Bulletin 2011-12 §V (model documentation) for model-validation binders within bank scope.

## capital-markets

### Capital-markets sector overlay — evidence-binder

Loads when the scope `sector_overlay_set` includes `capital-markets`. Binds evidence-binder content to SEC, FINRA, and CFTC examination expectations for broker-dealers, investment advisers, registered funds, and futures-market participants.

#### Supervisory frame

SEC Division of Examinations (formerly OCIE) and FINRA Member Supervision issue examination request lists at exam open. The binder reconciles each item.

For investment advisers, SEC Rule 206(4)-7 (compliance-program rule) sets the annual-review frame; the binder for an annual-review evidence pack carries the testing workpapers, deficiencies log, and remediation evidence.

For broker-dealers, FINRA Rule 3110 (supervision) and the Books and Records rules (SEA §17(a), Rules 17a-3 / 17a-4) drive evidence-list shape.

#### Recordkeeping and retention

The binding rules are sharp here:

- **SEC Rule 17a-4** — broker-dealer recordkeeping: most records retained six years (first two years in an easily accessible place); some categories (e.g., partnership articles) for the life of the enterprise plus three years. Electronic records since 2022 amendment may be stored on a write-once or audit-trail basis.
- **FINRA Rule 4511** — books-and-records general retention: six years unless a specific rule is shorter or longer.
- **SEC Investment Advisers Act Rule 204-2** — adviser recordkeeping: most records five years (first two years on premises). Performance-presentation records carry their own retention periods.
- **CFTC Regulation 1.31** — futures-market recordkeeping: five years from creation, with electronic-storage standards.

Binder rows that touch records under these rules carry a period_start that respects the retention window, not just the examination window.

#### Common request-list shapes

SEC EXAMS request lists typically cover: governance (Form ADV, code of ethics, policies and procedures), conflicts (related-party trades, soft dollars, gifts and entertainment), portfolio management (trade blotter, allocation policy, IPO allocations), best execution (broker reviews, transaction-cost analysis), valuation (pricing policies, hard-to-value asset evidence), custody (Rule 206(4)-2 evidence for advisers), marketing (Rule 206(4)-1 evidence), cybersecurity (Reg S-P, Reg S-ID, the cybersecurity risk management program), and compliance (annual-review documentation, testing workpapers).

FINRA examination requests typically cover: supervisory structure (3110 evidence), books-and-records (4511 evidence), AML (3310 evidence), customer accounts (NASD 3010 / FINRA 3110 supervisory evidence), trade reporting, communications with the public (2210 evidence), and cybersecurity.

#### Sign-off and review-gate norms

Adviser binders are signed by the chief compliance officer (named under Rule 206(4)-7). Broker-dealer binders are signed by the principal-supervisor under FINRA 3110 or by the chief compliance officer. Fund binders are signed by the fund CCO under Rule 38a-1; board materials are signed by the fund secretary.

The binder's `sign_off` field carries the role.

#### Anchors used by this overlay

- 17 CFR §240.17a-3 and §240.17a-4 — broker-dealer recordkeeping.
- FINRA Rule 4511 — books and records, general retention.
- 17 CFR §275.204-2 — Investment Advisers Act recordkeeping.
- 17 CFR §275.206(4)-7 — Investment Advisers Act compliance-program rule.
- 17 CFR §270.38a-1 — Investment Company Act fund compliance-program rule.
- FINRA Rule 3110 — supervision.
- FINRA Rule 3310 — anti-money-laundering compliance program.
- 17 CFR §1.31 — CFTC recordkeeping requirements.

## insurance

### Insurance sector overlay — evidence-binder

Loads when the scope `sector_overlay_set` includes `insurance`. Binds evidence-binder content to state-DOI and NAIC-framework expectations.

#### Supervisory frame

State Departments of Insurance run market-conduct and financial examinations under state law and the NAIC handbooks. The Market Conduct Examiners Handbook frames evidence asks for claims-handling, complaint-handling, underwriting, rating, marketing, and producer-licensing programs; the Financial Condition Examiners Handbook frames evidence asks for solvency, reserves, reinsurance, and corporate governance. The binder's `request_list` reconciles the examiner's RFIs.

NAIC accreditation drives a baseline of standards across states; state-specific amendments are common, and the binder carries the binding-state version where the two diverge.

#### Recordkeeping and retention

- NAIC Model Audit Rule (Model #205), §16: internal control over financial reporting expectations for insurers above the premium threshold. Audit-binder rows cite §16 for ICFR scope; reproducibility of the underlying control evidence is the supervisory test.
- State retention rules vary; common pattern is the longer of seven years or the policy life plus a tail. Binder rows for policy-administration evidence respect the longer window.
- ORSA (Own Risk and Solvency Assessment): annual filing in adopting states. Evidence binder for ORSA review carries the ORSA Summary Report, the supporting risk-and-capital analysis, and the governance evidence (board approval, risk-appetite statement). NAIC Risk Management and ORSA Model Act §4 [verify].

#### Common request-list shapes

State-DOI market-conduct RFIs typically cover: claims-handling timeliness and unfair-claims-settlement practices, complaint logs and responses, producer licensing and appointment, underwriting and rating sample files, marketing materials, advertising approvals, replacement and suitability evidence (life and annuities), privacy notices (NAIC Model #672 / GLBA-aligned).

Financial examinations typically cover: corporate-governance evidence, board and committee minutes, audited statutory financials, reserve adequacy, reinsurance ceded and assumed, asset valuation, related-party transactions, and ORSA where adopted.

#### Sign-off and review-gate norms

Market-conduct binders are signed by the chief compliance officer; financial-exam binders by the chief financial officer or chief risk officer. The binder's `sign_off` field carries the role.

#### Anchors used by this overlay

- NAIC Model Audit Rule (Model #205) §16 — internal control over financial reporting [verify section].
- NAIC Market Conduct Examiners Handbook — claims-handling examination standards [verify section].
- NAIC Financial Condition Examiners Handbook — financial examination standards [verify section].
- NAIC Risk Management and ORSA Model Act (Model #505) §4 [verify section].
- NAIC Model Unfair Claims Settlement Practices Act (Model #900) [verify state-specific adoption].
- State recordkeeping statutes — verify per state.

## payments-fintech

### Payments and fintech sector overlay — evidence-binder

Loads when the scope `sector_overlay_set` includes `payments-fintech`. Binds evidence-binder content to bank-partnership, money-transmitter, and payment-network supervisory expectations.

#### Supervisory frame

The supervisory map for fintechs splits by structure. A direct-chartered bank is supervised under the bank overlay. A non-bank fintech operating through a sponsor-bank arrangement is examined indirectly through the sponsor (FFIEC interagency third-party guidance, June 2023; the OCC's bank-partnership focus); the binder carries both partner-bank evidence and the fintech's own evidence. A non-bank fintech holding state money-transmitter licenses faces state-by-state examinations under the NMLS framework. Card-network participants face PCI DSS, network operating rules (Visa, Mastercard, network-specific), and FinCEN obligations as money-services businesses where applicable.

#### Recordkeeping and retention

- **Bank Secrecy Act** — for fintechs registered as MSBs: 31 CFR §1010.430 general recordkeeping, §1022 series MSB-specific. Five-year retention floor for BSA records.
- **Reg E** — 12 CFR §1005, electronic-fund-transfer evidence: error-resolution records must be retained two years.
- **Reg Z** — 12 CFR §1026: two-year retention for credit-disclosure evidence.
- **CFPB supervisory authority** — Dodd-Frank §1024 (larger participants of consumer-financial-services markets) extends CFPB exam reach to fintechs above the relevant size thresholds.
- **PCI DSS** — log retention typically one year online, with the most recent three months immediately available; binder cites the firm's PCI-DSS attestation and the QSA's findings.
- **Money-transmitter licensing** — state retention varies; typical pattern is the longer of three years or state-specific window, with NMLS-uploaded records as the canonical reference.

#### Common request-list shapes

Sponsor-bank-side RFIs typically cover the bank's TPRM evidence on the fintech: criticality assessment, due-diligence pack, contract, ongoing-monitoring evidence, BSA-program evidence (the fintech-side program plus the bank's oversight), Reg E and Reg Z evidence on consumer-facing flows, complaint logs, and the bank's own remediation tracking.

Fintech-side RFIs (state DFS, CFPB exams, network audits) typically cover: licensing and registrations, BSA program (program description, risk assessment, transaction-monitoring evidence, SAR filings), consumer-protection evidence (Reg E, Reg Z, UDAAP), complaint logs, dispute-handling evidence, and compliance with the network's operating rules.

#### Sign-off and review-gate norms

Sponsor-bank binders for fintech-partnership exams are signed by the sponsor-bank's BSA officer or chief compliance officer. Fintech-side binders are signed by the fintech's BSA officer (where MSB-registered) or chief compliance officer.

For BaaS arrangements, the binder may need to evidence both sides; the scope record names which side this binder represents.

#### Anchors used by this overlay

- Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FRB/FDIC, June 2023).
- 31 CFR §1010.430 — FinCEN general recordkeeping.
- 31 CFR §1022 series — MSB-specific FinCEN rules.
- 12 CFR §1005 — Reg E (Electronic Fund Transfers Act implementation).
- 12 CFR §1026 — Reg Z (Truth in Lending Act implementation).
- Dodd-Frank Act §1024 — CFPB supervisory authority over larger participants.
- PCI DSS v4.0 — current version of the Payment Card Industry Data Security Standard.
