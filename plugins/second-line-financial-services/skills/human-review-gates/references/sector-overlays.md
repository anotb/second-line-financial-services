# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — human-review-gates

Loads when the scope `sector_overlay_set` includes `banking`. The overlay shapes the decision-authority block, the independence requirements, the documentation conventions, and the board-oversight expectations for gate matrices at federally regulated US banks (national, state-member, state-non-member, savings, holding companies, and US IHCs of foreign banking organizations).

#### Why the banking overlay matters

The federal banking supervisors (FRB, OCC, FDIC) have specific, published expectations on risk governance, three-lines-of-defense architecture, board risk-committee oversight, and senior-management challenge. A gate matrix that does not reflect those expectations reads as misaligned with the firm's continuous-monitoring posture and is harder to defend in the next examination cycle. The overlay is the contract between the gate matrix and the supervisor's expected governance architecture.

#### Source basis

- **12 CFR Part 30, Appendix D — OCC Heightened Standards for Large Insured National Banks**. Standards I–V on the risk governance framework, three-lines-of-defense, independent risk management, front-line-unit responsibilities, and the board's oversight responsibility. Threshold for application: covered banks at the OCC's asset-size population (currently $50B+ at the OCC's discretion).
- **Reg YY (12 CFR Part 252) — Enhanced Prudential Standards for large bank holding companies**. Risk-management and risk-committee requirements that frame governance gates, including the requirement that BHCs at $50B+ maintain a risk committee of the board with at least one risk-management expert and an independent CRO with stature in the organization.
- **Federal Reserve SR 11-7 / OCC Bulletin 2011-12**. Validation independence as the ground for independence in model-risk gates; effective challenge as the source for the dissent-path discipline.
- **OCC Bulletin 2026-13**. Refreshed effective-challenge gate language, human oversight for AI-extended models, third-party model gates.
- **Federal Reserve SR 16-11**. Risk-management-framework expectations for sub-$100B FRB-supervised institutions.
- **Federal Reserve SR 13-13 / CA 13-10**. MRA / MRIA framework and the firm-side expectation that issues are tracked through closure with named-reviewer documentation.
- **FDIC Risk Management Manual of Examination Policies and FDIC Compliance Examination Manual**. MRBA framing; FDIC convention that significant findings address the board rather than management alone.
- **FFIEC Uniform Rating System (CAMELS for banks; ROCA for FBOs)**. Composite-rating framing that informs gate-criticality calibration; gates touching CAMELS components carry higher-stakes rationale.

#### What the overlay adds to the matrix

##### Decision authority — board oversight

For Heightened-Standards-covered banks and Reg YY-covered BHCs, the matrix's decision-authority block names the board risk committee as the ultimate adopting body for material gate-architecture changes. The board reporting cadence is named (typically quarterly to the risk committee, with an annual report on the gate-architecture refresh to the full board). For BHCs covered by Reg YY, the risk committee charter is itself a regulatory document; gate-architecture changes flow through risk-committee adoption with a documented decision.

##### Three-lines-of-defense independence

The Heightened Standards' three-lines-of-defense architecture is the primary source for independence on banking-overlay gates:
- **Front-line unit (line 1)** — the business sponsor. Owns the risk-taking and the artifact under review.
- **Independent risk management (line 2)** — the independent reviewer. Owns the challenge function. Independence is structural: line-2 reviewers report to the CRO, not to the front-line unit.
- **Internal audit (line 3)** — the audit reviewer where the gate is one that internal audit certifies (e.g., the annual review of the gate matrix itself; the validation of effective-challenge implementation).

The matrix's `required_reviewers` block carries primary and backup roles per line; the `independence_required` flag is true for line-2 and line-3 reviewers; the `independence_basis` cites 12 CFR Part 30 Appendix D Standard II (risk governance framework) and Standard IV (front-line-unit responsibilities).

##### Senior-management challenge

For sub-$100B FRB-supervised institutions, SR 16-11 frames the senior-management-challenge expectation. The matrix typically names a "senior management committee" gate distinct from the board risk committee gate; the senior management committee is the operational decision-holder, and the board risk committee is the oversight body that reviews the senior management committee's record on a periodic cadence.

##### Reg YY risk-committee gates

For BHCs at $50B+ under Reg YY enhanced prudential standards, gates touching enterprise-wide risk-management framework refresh, risk-appetite-statement updates, or material change to the CRO function flow through the board risk committee with a documented decision. The matrix names the risk committee as the primary committee for these gates; the documentation requirement names the board risk-committee minutes as the system of record.

##### Heightened Standards severity flavour

For OCC-Heightened-Standards-covered banks, gate-design issues (a missing independence requirement, an absent escalation path, a documentation requirement that does not retain attesters) carry severity weight tied to the specific Heightened Standard they impair. A missing line-1 / line-2 separation impairs Standard II; a missing front-line-unit accountability impairs Standard IV; a missing board-oversight cadence impairs Standard V. The gap section of the matrix names the specific Standard.

##### CAMELS / ROCA component implications

Gates that govern decisions touching CAMELS components (Capital, Asset quality, Management, Earnings, Liquidity, Sensitivity) carry severity weight tied to the component. A gate-design weakness on the M (Management) component is itself a Management-rating consideration; the gap is sourced to the FFIEC Uniform Rating System framing.

#### Common patterns

- **One-committee monoculture**. A bank where the same committee owns AI use-case approval, model-risk approval, vendor onboarding, issue rating, and customer-impact action does not have a gate matrix; it has one committee. Heightened Standards Standard II expects independent risk management with stature; one-committee monoculture fails the independence test. The gap section names this and recommends a committee-charter refresh.
- **MRA-driven gate refresh**. An MRA on governance prompts a gate-architecture refresh; the recommended charter language and the gap section frame the refresh against the MRA's specific finding.
- **Pre-emptive Heightened Standards readiness**. Banks approaching the $50B Heightened Standards threshold typically refresh gate architecture in advance of the threshold trigger. The matrix's `recommended_charter_language` block frames the readiness posture.
- **Validator-as-developer failure**. A model-risk gate where the named validator is also the named developer (or reports to the developer's chain) fails SR 11-7. The matrix's gap section flags this with the specific section reference.

#### Implications for gate construction

- Independence is named explicitly per reviewer, with the source anchor in `independence_basis`. Banking overlay matrices typically have independence flagged on the line-2 reviewer slot for every gate that touches risk-taking, risk-control, or regulatory-disclosure decisions.
- Decision criteria for banking gates often cite the specific Heightened Standard, Reg YY section, or SR letter; the criteria block carries the source anchor.
- Documentation requirement names the system of record at granularity: GRC platform record ID type, board-portal location, board-minutes retention period (typically 7-year retention for federal banking exam files; firm-overlay specifies the firm's actual cadence).
- The gap section explicitly checks for: missing independent reviewer slot, missing board-oversight cadence (for Heightened Standards / Reg YY firms), missing escalation path to the risk committee, missing dissent-path discipline.

#### Anchors used by this overlay

- 12 CFR Part 30, Appendix D — OCC Heightened Standards (Standards I–V). https://www.ecfr.gov/current/title-12/chapter-I/part-30/appendix-Appendix%20D%20to%20Part%2030
- 12 CFR Part 252 (Reg YY) — Enhanced prudential standards for large BHCs. [verify current section labels for risk committee and risk-management requirements.] https://www.federalreserve.gov/supervisionreg/reglisting.htm
- Federal Reserve SR 11-7 / OCC Bulletin 2011-12 — Supervisory Guidance on Model Risk Management. §V (validation independence), §VI (governance). https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm
- OCC Bulletin 2026-13 — Revised Interagency Model Risk Management Guidance. §III.E (independent challenge), §III.F (human oversight). [verify section labels] https://www.occ.gov/news-issuances/bulletins/
- Federal Reserve SR 16-11 — Risk-management framework for sub-$100B institutions. https://www.federalreserve.gov/supervisionreg/srletters/sr1611.htm
- Federal Reserve SR 13-13 / CA 13-10 — Communication of Supervisory Findings (MRA / MRIA). https://www.federalreserve.gov/supervisionreg/srletters/sr1313.htm
- FDIC Risk Management Manual of Examination Policies. https://www.fdic.gov/regulations/safety/manual/
- FDIC Compliance Examination Manual. https://www.fdic.gov/resources/supervision-and-examinations/consumer-compliance-examination-manual/
- FFIEC Uniform Rating System (CAMELS / ROCA). [verify current edition.]

## capital-markets

### Capital markets sector overlay — human-review-gates

Loads when the scope `sector_overlay_set` includes `capital-markets`. The overlay shapes the decision-authority block, the supervision and compliance-program gate framing, and the documentation conventions for gate matrices at SEC- and FINRA-regulated firms (broker-dealers, investment advisers, fund complexes, CFTC-registered swap dealers and FCMs, and exchange-traded-product issuers).

#### Why the capital-markets overlay matters

The supervision concept is central to broker-dealer governance under FINRA Rule 3110; the compliance-program concept is central to investment adviser governance under SEC Rule 206(4)-7. Both concepts are directly anchored in the firm's gate architecture: supervision is itself a continuous gate function, and the annual compliance-program review under Rule 206(4)-7 is itself an annual gate. A gate matrix at a broker-dealer or investment adviser that does not name supervision or the annual compliance review correctly will not align with the SEC EXAMS or FINRA examination posture.

#### Source basis

- **FINRA Rule 3110 — Supervision**. The supervision system requirement: written supervisory procedures, supervision of registered persons by qualified principals, supervision of customer accounts and transactions, supervision of correspondence and internal communications, and the supervision-of-supervisors requirement.
- **FINRA Rule 3120 — Supervisory Control System**. The supervisory control system requirement, distinct from but layered onto Rule 3110: testing and verification of the firm's supervisory procedures, with the chief executive officer's annual certification.
- **SEC Rule 206(4)-7 — Compliance Programs of Investment Advisers (17 CFR §275.206(4)-7)**. The requirement that registered investment advisers adopt and implement written compliance policies and procedures reasonably designed to prevent violations, designate a chief compliance officer, and conduct an annual review of the adequacy of the policies and procedures and the effectiveness of their implementation.
- **SEC Rule 38a-1 — Compliance Procedures and Practices of Investment Companies (17 CFR §270.38a-1)**. The fund-complex parallel to Rule 206(4)-7: written compliance policies, designated CCO, annual board approval and review.
- **SEC Rule 17a-3 and 17a-4 — Broker-dealer recordkeeping (17 CFR §240.17a-3 and §240.17a-4)**. The records the broker-dealer must make and preserve, with named retention periods. The recordkeeping rule is itself a gate-decision evidence anchor.
- **SEC Rule 204-2 — Investment Adviser recordkeeping (17 CFR §275.204-2)**. The investment-adviser parallel.
- **SEC Rule 15c3-5 — Risk Management Controls for Brokers or Dealers with Market Access (17 CFR §240.15c3-5)**. Pre-trade risk-management controls and the CEO certification of effectiveness of those controls; named pre-trade gates with documented criteria.
- **FINRA Rule 4511 — General Recordkeeping**. Books-and-records retention requirements layered onto SEC 17a-3 / 17a-4.
- **FINRA Rule 3170 — Tape Recording of Registered Persons (taping rule)**. Specific firms; named gate where applicable.
- **CFTC Part 3 — Registration and CFTC Part 23 — Swap Dealers** and the CFTC's compliance-program requirements for swap dealers.

#### What the overlay adds to the matrix

##### Decision authority — supervision and CCO functions

The capital-markets matrix names two distinct decision-authority structures:

- **For broker-dealers**: the supervision system under Rule 3110, with named principals (Series 24 General Securities Principal, Series 9/10 Branch Office Manager, Series 4 Registered Options Principal, Series 27/28 Financial and Operations Principal, etc.) carrying gate-decision authority for the activities they supervise. The supervisory control system under Rule 3120 names the senior officer (often the President or CEO) who certifies the supervisory system annually. Branch-office gates flow through branch managers; firm-level gates flow through the senior principal in the relevant function.
- **For investment advisers**: the chief compliance officer designated under Rule 206(4)-7 as the named decision-holder for compliance-program gates. The annual compliance review is itself a gate; the documentation requirement names the annual review report and the CCO sign-off.

For dual-registrant firms (broker-dealer and adviser), both structures exist; the matrix names the structure relevant to each gate's subject matter.

##### Annual compliance review as a gate

Rule 206(4)-7 explicitly requires registered investment advisers to review their compliance program annually. This is itself a gate: the trigger is annual; the required reviewer is the CCO; the required inputs are the firm's compliance policies, the year's compliance monitoring outputs, and the year's exception log; the decision criteria are adequacy and effectiveness; the documentation requirement is the annual review report, retained per Rule 204-2. Funds under Rule 38a-1 carry the same gate with board-approval framing.

##### Pre-trade risk-management gates (Rule 15c3-5)

For broker-dealers with market access, Rule 15c3-5 names a specific class of gates: pre-trade risk-management controls, with the CEO's annual certification of effectiveness. The matrix carries these as a distinct gate cluster, with the CEO as the named attester for the annual certification gate.

##### Recordkeeping framing

The recordkeeping rules (17a-3, 17a-4, 204-2, 4511) frame the documentation requirement on every capital-markets gate. The retention period is rule-specific (typically 3 to 6 years depending on the record type, with the first 2 years in an easily accessible location); the storage standard is rule-specific (the 2022 SEC amendment to 17a-4 changed the electronic-storage standard from WORM to a more flexible audit-trail-based standard). The matrix's documentation requirement column names the rule and the retention period.

##### CFTC-regulated activity

For swap dealers and FCMs, the CFTC's compliance-program requirements layer onto the matrix. The chief compliance officer for a swap dealer carries specific duties under CFTC rules; the annual CCO report to the CFTC is itself a gate-anchored deliverable.

#### Common patterns

- **Supervision is not a gate; supervision is the continuous function**. A common confusion: practitioners name "supervision" as a gate. Supervision under Rule 3110 is the continuous oversight function performed by qualified principals; the gate is the decision point inside the supervision function (account approval, transaction review threshold, correspondence escalation). The matrix names the gates within the supervisory function, not "supervision" as a gate itself.
- **Annual compliance review treated as administrative**. The annual review under Rule 206(4)-7 is sometimes treated as an administrative box-check; the SEC EXAMS staff treat it as a substantive gate. The matrix elevates the annual review to a named gate with criteria, stop conditions (e.g., "no sign-off if material deficiencies are not remediated or scheduled"), and documentation discipline.
- **Dual-registrant ambiguity**. Firms registered as both broker-dealer and investment adviser sometimes have unclear gate boundaries between supervision (Rule 3110) and compliance-program (Rule 206(4)-7). The matrix names both structures and assigns each gate to the structure relevant to its subject matter.
- **CEO certification under-evidenced**. The Rule 3120 supervisory-control-system certification and the Rule 15c3-5 pre-trade-risk certification are CEO-level attestations; the documentation requirement on these gates names the certification record retained per Rule 17a-4.

#### Implications for gate construction

- Decision authority for capital-markets matrices typically names: the supervision system (broker-dealer side), the CCO function (adviser/fund side), the senior officer carrying Rule 3120 / Rule 15c3-5 certifications, and the board (for fund advisers under Rule 38a-1).
- Independence on capital-markets gates is grounded in SEC Rule 206(4)-7's framing that the CCO has "competence and knowledge" and "sufficient authority to develop and enforce appropriate policies and procedures"; firms sometimes also flag CCO independence from front-office reporting lines, though the rule does not explicitly require it.
- Documentation requirement on capital-markets gates names the recordkeeping rule (17a-3, 17a-4, 204-2, 4511) and the retention period; the system of record is the firm's books-and-records system per SEC and FINRA expectations.
- The gap section explicitly checks for: supervision-named-as-gate confusion (correct it); annual review under Rule 206(4)-7 missing or under-evidenced; CEO certification gates (Rule 3120, Rule 15c3-5) missing or with no clear attester; correspondence and internal communications supervision gates missing under Rule 3110.

#### Anchors used by this overlay

- FINRA Rule 3110 — Supervision. https://www.finra.org/rules-guidance/rulebooks/finra-rules/3110
- FINRA Rule 3120 — Supervisory Control System. https://www.finra.org/rules-guidance/rulebooks/finra-rules/3120
- FINRA Rule 4511 — General Recordkeeping. https://www.finra.org/rules-guidance/rulebooks/finra-rules/4511
- FINRA Rule 3170 — Tape Recording of Registered Persons. https://www.finra.org/rules-guidance/rulebooks/finra-rules/3170
- 17 CFR §275.206(4)-7 — SEC Rule 206(4)-7, Compliance Programs of Investment Advisers. https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-7
- 17 CFR §270.38a-1 — SEC Rule 38a-1, Compliance Procedures and Practices of Investment Companies. https://www.ecfr.gov/current/title-17/chapter-II/part-270/section-270.38a-1
- 17 CFR §240.17a-3 — Records to be made by certain exchange members, brokers, and dealers. https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.17a-3
- 17 CFR §240.17a-4 — Records to be preserved by certain exchange members, brokers, and dealers. https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.17a-4
- 17 CFR §275.204-2 — Investment Adviser recordkeeping. https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.204-2
- 17 CFR §240.15c3-5 — Risk Management Controls for Brokers or Dealers with Market Access. https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.15c3-5
- CFTC Part 3 (Registration) and Part 23 (Swap Dealers). https://www.ecfr.gov/current/title-17/chapter-I

## insurance

### Insurance sector overlay — human-review-gates

Loads when the scope `sector_overlay_set` includes `insurance`. The overlay shapes the decision-authority block, the independence requirements, the documentation conventions, and the board-oversight expectations for gate matrices at US insurance companies (life, P&C, health insurers, plus reinsurers and insurance holding companies regulated by state DOIs and coordinated through the NAIC).

#### Why the insurance overlay matters

State insurance regulators coordinate via the NAIC, which publishes Model Acts and Model Regulations the states adopt with variation. The governance architecture is distinct from federal banking governance: insurance commissioners, not federal banking supervisors, are the primary regulators; ORSA (Own Risk and Solvency Assessment) is the enterprise-risk artifact rather than the bank-style risk-appetite-statement; the audit committee requirement under most state insurance-holding-company statutes is statutory rather than supervisory. A gate matrix for an insurer that uses bank governance vocabulary will read as misaligned to a state insurance examiner.

#### Source basis

- **NAIC Risk Management and Own Risk and Solvency Assessment (ORSA) Model Act (MDL-505)**. ORSA is the insurer's enterprise risk-management framework and capital-assessment artifact; the ORSA process is itself a gated set of decisions, and gate matrices for insurer enterprise risk reference the ORSA framework. Operative for insurance groups at the states' premium thresholds (typically $500M individual or $1B group, with state variation).
- **NAIC Corporate Governance Annual Disclosure Model Act (MDL-305) and Model Regulation (MDL-306)**. Annual disclosure to the domiciliary state of the insurer's corporate governance practices, including board composition, committee structure, and policies on senior officer oversight. The disclosure framing informs how gates are documented and how the board-committee structure is named.
- **NAIC Model Audit Rule — Annual Financial Reporting Model Regulation (MDL-205)**. Audit committee independence requirements; the audit committee is a statutory committee under most state insurance laws, with named independence requirements that flow into gate matrices for finance, audit, and internal-control-related decisions.
- **NAIC Insurance Holding Company System Regulatory Act (MDL-440) and Regulation (MDL-450)**. Group-supervision framework; Form B annual filing requirements include governance disclosures.
- **NAIC AI Bulletin (2023)**. State insurance regulator expectations on AI governance for insurer use cases (underwriting, claims, fraud detection); the Bulletin's governance-framework language informs AI-related gate construction at insurers.
- **State DOI bulletins** (varies by state). Specific governance and committee-charter expectations from individual state insurance commissioners; California, New York DFS (which regulates insurers as well as banks), and Texas tend to publish the most-cited state-specific guidance.

#### What the overlay adds to the matrix

##### Decision authority — board and audit committee

The insurer's matrix names the board of directors as the ultimate adopting body, with the audit committee as the named statutory body for finance, audit, and internal-control-related gates (Model Audit Rule). Risk-related governance gates flow through a risk committee or a combined risk-and-audit committee depending on the firm's structure (NAIC Corporate Governance Annual Disclosure framework documents the structure annually). For insurance groups under the NAIC Holding Company framework, the holding-company board has additional oversight on group-level gates.

##### ORSA-anchored governance gates

For insurers above the ORSA threshold (state-by-state, typically $500M individual or $1B group), the ORSA framework is itself the source for enterprise-risk gates. The matrix references ORSA for: enterprise risk identification gates, capital assessment gates, prospective solvency assessment gates, and the annual ORSA Summary Report sign-off gate. The ORSA Summary Report sign-off is itself a high-stakes gate; the documentation requirement names the report, the named attesters (typically the CRO and the CEO with board concurrence), the date, and the regulator submission.

##### Audit committee independence

The Model Audit Rule sets named independence requirements for the audit committee that flow into gate matrices for finance and internal-control-related decisions. Audit committee members must meet specific independence criteria (no material relationship with the insurer; no compensation other than committee fees and equity-based compensation under the Model Audit Rule's framing). The matrix's `independence_basis` for audit-committee-anchored gates cites the Model Audit Rule.

##### Statutory accounting and reserving gates

Gates touching statutory accounting decisions (reserves, asset valuation, capital classification under risk-based capital rules) are statutory under state insurance law. The matrix references the relevant SAP (Statutory Accounting Principles) standard; reserving gates name the appointed actuary as the independent reviewer (the appointed actuary is a state-statutory role with named independence from management on actuarial opinion).

##### NAIC AI Bulletin governance for AI use cases

For insurers deploying AI in underwriting, claims, fraud detection, or pricing, the NAIC AI Bulletin (2023) frames the governance expectations. The matrix references the Bulletin's governance-framework language for AI-related gates: senior management oversight, board awareness, governance committee structure, third-party AI vendor oversight, and consumer-impact assessment. For New York-regulated insurers, the NYDFS AI Industry Letter (2024) layers onto the NAIC framework with state-specific language on insurer AI use.

##### State DOI variation

Gates at multi-state insurers reflect the domiciliary state's specific governance expectations, with secondary-state extensions where licensed-state requirements add to (rather than replace) domiciliary requirements. The matrix's `scope_notes` block names the domiciliary state and the multi-state footprint; the `firm-overlay.md` lists the state-specific bulletins the firm has implemented.

#### Common patterns

- **Audit committee under-staffed for material-control gates**. Audit committee composition under the Model Audit Rule requires independence and financial literacy; smaller insurers often staff the audit committee at minimum statutory requirements, which is fine until a material-control gate (Sarbanes-Oxley-equivalent for filers, or material reserving change for any insurer) puts strain on the committee. The matrix surfaces this in the gap section when the audit-committee gate count is high relative to committee capacity.
- **ORSA Summary Report sign-off as a single annual gate**. For insurers above the ORSA threshold, the ORSA Summary Report is filed annually with the lead state. The sign-off gate is annual; the upstream gates (ERM framework refresh, capital-assessment refresh, prospective-solvency-assessment refresh) feed it. The matrix sequences these.
- **Appointed-actuary independence**. The appointed actuary's independence on reserving-decision gates is statutory; the matrix carries the independence flag with the specific state-statutory citation (varies by state).
- **NAIC AI Bulletin gap on legacy use cases**. Insurers with AI in production from before the 2023 NAIC AI Bulletin sometimes have governance gates that pre-date the Bulletin's expectations. The matrix's gap section flags the specific Bulletin sections not yet reflected.

#### Implications for gate construction

- Decision authority for insurer matrices typically names: board of directors, audit committee (statutory), risk committee or combined risk/audit committee, governance/nominating committee, and enterprise risk management committee at the management level. The board overrides at the top; specific gate types route to specific committees based on subject matter.
- Independence on insurer gates is grounded in the Model Audit Rule for audit-committee-anchored gates, the Holding Company framework for group-level gates, and state-statutory citations for reserving and actuarial opinion gates.
- Documentation requirement on insurer gates names the system of record (typically the GRC platform plus the board-portal), the retention (state-by-state; California is among the longest at 5+ years for board minutes), and the regulator-submission cadence where the gate's record is filed (Form B, ORSA Summary Report, Corporate Governance Annual Disclosure).
- The gap section explicitly checks for: missing audit-committee independence on Model-Audit-Rule-anchored gates; missing appointed-actuary independence on reserving gates; missing ORSA Summary Report sign-off gate for above-threshold insurers; missing NAIC AI Bulletin alignment for AI-using insurers.

#### Anchors used by this overlay

- NAIC Risk Management and Own Risk and Solvency Assessment (ORSA) Model Act (MDL-505). https://content.naic.org/sites/default/files/MO505.pdf
- NAIC Corporate Governance Annual Disclosure Model Act (MDL-305). https://content.naic.org/sites/default/files/inline-files/MDL-305.pdf
- NAIC Corporate Governance Annual Disclosure Model Regulation (MDL-306). https://content.naic.org/sites/default/files/inline-files/MDL-306.pdf
- NAIC Annual Financial Reporting Model Regulation (Model Audit Rule, MDL-205). https://content.naic.org/sites/default/files/inline-files/MDL-205.pdf
- NAIC Insurance Holding Company System Regulatory Act (MDL-440). https://content.naic.org/sites/default/files/inline-files/MDL-440.pdf
- NAIC AI Bulletin — Use of Artificial Intelligence Systems by Insurers (2023). https://content.naic.org/sites/default/files/inline-files/2023-12-04%20Model%20Bulletin_Adopted_0.pdf
- NYDFS AI Industry Letter (2024) — Use of AI in Underwriting and Pricing. https://www.dfs.ny.gov/industry_guidance/circular_letters
- State DOI bulletins — varies by state; firm-overlay names the state-specific bulletins the firm has implemented.

## payments-fintech

### Payments and fintech sector overlay — human-review-gates

Loads when the scope `sector_overlay_set` includes `payments-fintech`. The overlay shapes the decision-authority block and the gate framing for sponsor-bank arrangements, money-services-business state-licensing, and consumer-payment-product oversight at fintechs and the banks that sponsor them.

#### Why the payments-fintech overlay matters

The governance architecture in payments and fintech is shaped by two distinct regimes that often coexist: the sponsor-bank arrangement (where a bank charters or partners with a fintech to deliver bank products and the OCC, FRB, FDIC, and CFPB have specific expectations on the bank's oversight of the fintech) and the money-services-business framework (where a non-bank money transmitter is regulated state-by-state under MSB licensing, with FinCEN BSA/AML registration on top). A gate matrix at a fintech or sponsor bank must reflect both regimes when both apply.

#### Source basis

- **Interagency Guidance on Third-Party Relationships: Risk Management (OCC / FRB / FDIC, June 2023)**. The base third-party-risk framework that applies to bank-fintech partnerships from the bank side. The lifecycle phases (planning, due diligence, contract, ongoing monitoring, termination) frame the sponsor-bank gate matrix.
- **OCC, FRB, FDIC Bank-Fintech Partnership Guidance**. The federal banking supervisors have published joint and individual guidance on bank-fintech partnerships. The specific guidance includes: OCC guidance on bank operations through bank service company arrangements; FRB SR letters on third-party relationships including fintech-specific addenda; FDIC bank-fintech guidance issued through FILs.
- **CFPB Supervision and Examination Manual — relevant chapters**. The CFPB asserts supervisory authority over banks and over larger participants in certain consumer-financial markets; CFPB's CMS framework and product-specific exam manual chapters frame consumer-product gates.
- **NACHA Operating Rules**. ACH originator and ODFI obligations; gate-anchoring for ACH-product launches and ongoing monitoring.
- **Reg E (12 CFR Part 1005) and Reg Z (12 CFR Part 1026)**. Consumer protections on electronic fund transfers and consumer credit; specific rules drive product-level gates (Reg E error-resolution timelines, Reg Z disclosure requirements, Reg Z ability-to-repay for credit products).
- **State money-transmitter licensing (varies by state; harmonized in many states by the Conference of State Bank Supervisors' Money Transmission Modernization Act)**. State licensing requirements include named permissible-investment requirements, surety-bond requirements, and ongoing reporting; gate-anchoring for state-licensed money transmitters.
- **FinCEN BSA/AML registration (31 CFR Chapter X, Part 1022 for MSBs)**. AML program requirements for non-bank MSBs, including designated AML compliance officer, training, independent review, and SAR/CTR filing obligations.

#### What the overlay adds to the matrix

##### Decision authority — sponsor-bank dual structure

For a sponsor-bank-and-fintech arrangement, the matrix often names two coordinated decision authorities:

- **Sponsor bank side**: the bank's risk committee, vendor risk committee, and (for products subject to CFPB supervision) the consumer compliance committee. The bank carries primary regulatory responsibility for the fintech's activities under the bank's charter and so the bank's gates govern the partnership.
- **Fintech side**: the fintech's own compliance and risk function, with a designated officer (CCO, BSA Officer, or both) responsible for fintech-side execution. The fintech's gates feed the bank's gates; a gate at the fintech that does not produce evidence the bank can inspect creates an oversight gap on the bank side.

The matrix names both structures and the coordination mechanism (typically a joint operating committee or a sponsor-bank oversight forum) where decisions affecting both flow through.

##### MSB-only structures

For non-bank MSBs without a sponsor-bank arrangement (typical for some money transmitters and some payments processors), the matrix names: the firm's executive risk committee, the BSA Officer (FinCEN BSA program requirement), the AML compliance officer (often the same person), the designated state-licensing officer (the named individual on state licenses), and the board oversight mechanism (varies by state). The state-by-state variation lands in `firm-overlay.md`.

##### Sponsor-bank gate sequence

A canonical sponsor-bank gate matrix names:
1. **Fintech onboarding gate** at the bank (interagency TPRM §III.B due-diligence gate adapted for fintech-specific risks: business-model viability, regulatory licensing, technology stack, financial condition).
2. **Contract gate** at the bank (interagency TPRM §III.C contract gate, with named bank-side approvers for risk-management terms, exit terms, and information rights).
3. **Product-launch gate** at the bank (a product-specific gate where the consumer compliance, BSA, fraud, and risk functions concur on go-live; often distinct from the broader fintech onboarding gate).
4. **Ongoing-monitoring gate** at the bank (interagency TPRM §III.D, with cadence aligned to the criticality of the fintech relationship; typically quarterly to annual depending on criticality).
5. **Issue-rating gate** when fintech-originated issues land at the bank (the bank's issue-rating committee gate fires on fintech-monitoring exceptions).
6. **Termination gate** at the bank (interagency TPRM §III.E, with named bank-side approvers and exit-plan attestation).

The fintech side mirrors several of these with internal coordination (product-launch concurrence, monitoring evidence production, exit-plan execution).

##### Consumer-product gates

Gates touching consumer products carry the conduct cross-cutting overlay automatically (load `references/cross-cutting.md#conduct`). The matrix references specific rule-anchored gates:
- Reg E error-resolution-timeline gate (10-business-day provisional-credit decision, 45-day final resolution; specific rule-anchored stop conditions and documentation).
- Reg Z disclosure-review gate (annual percentage rate accuracy, TILA-required disclosures, ability-to-repay decisions for covered loans).
- CFPB UDAAP risk-review gate for product changes (fee-change approval, marketing-change approval, terms-and-conditions changes affecting consumers).
- Restitution-decision gate where a consumer-impact issue surfaces.

##### MSB-specific BSA gates

For MSB-licensed entities, the matrix names BSA-specific gates: the SAR-filing decision gate (BSA Officer attestation; FinCEN's 30-day filing window from initial detection of facts that may constitute a basis for filing, with up to 30 additional days for identifying a suspect); the CTR-filing operational gate; the OFAC-screening match-review gate; the periodic AML risk-assessment refresh gate; the AML independent review gate (annual or biennial, depending on size and complexity, performed by an independent reviewer per FinCEN expectations).

#### Common patterns

- **Bank-side oversight gap on fintech-side execution**. The bank's gates exist; the fintech's gates exist; but the evidence pipeline that lets the bank inspect the fintech's execution does not. The matrix's gap section flags this as a critical oversight gap; the recommended action names a specific evidence-pipeline (typically a monthly or quarterly fintech-monitoring pack with named reviewers on both sides).
- **Product-launch gate compressed into the fintech onboarding gate**. Banks sometimes treat the fintech's products as part of the fintech's onboarding rather than as separate product-launch gates. This compresses the consumer-compliance and BSA review into the onboarding diligence; the matrix flags this and recommends separating product-launch gates per product.
- **MSB BSA program treated as a single gate**. The BSA program for an MSB is a set of distinct gates (SAR filing, CTR filing, OFAC review, training cadence, independent review); some firms run a single "BSA review" gate that compresses these into one decision. The matrix surfaces the under-specified gate and recommends a gate per BSA program element.
- **State-licensing renewal gate buried in operations**. State money-transmitter renewal is annual or biennial in most states with named documentation requirements. Firms sometimes run renewal as an operational task without committee oversight; the matrix elevates the renewal as a named gate with the licensing officer as the named attester.

#### Implications for gate construction

- Decision authority for payments-fintech matrices typically names: the bank's risk committee (sponsor-bank case), the bank's consumer compliance committee (consumer-product case), the bank's vendor risk committee (TPRM case), the fintech's executive risk committee, the BSA Officer (designated under FinCEN regs for any BSA-covered entity), the named state-licensing officer (per state), and the board oversight body (varies by state and by structure).
- Independence on payments-fintech gates is grounded in: the interagency TPRM line-1 / line-2 separation (sponsor-bank case); the FinCEN-required AML independent review (MSB case); CFPB CMS framework's compliance-audit independence (consumer-product case).
- Documentation requirement names the system of record at the bank (GRC platform), the fintech-side system, the regulator-submission cadence (Form FFIEC reporting if applicable, Reg E/Reg Z compliance records, BSA filing records, state regulator filings), and the cross-firm coordination record (typically a shared committee minutes archive accessible to both bank and fintech).
- The gap section explicitly checks for: missing fintech-side evidence pipeline to bank-side gates; product-launch gates compressed into onboarding; BSA program treated as a single gate; state-licensing renewal not gated at committee level; consumer-product change gates without conduct-overlay alignment.

#### Anchors used by this overlay

- Interagency Guidance on Third-Party Relationships: Risk Management (June 2023). https://www.federalreserve.gov/supervisionreg/srletters/SR2304.htm
- OCC, FRB, FDIC bank-fintech partnership guidance — varies by agency and date; firm-overlay names the specific bulletins, FILs, and SR letters in scope.
- CFPB Supervision and Examination Manual. https://www.consumerfinance.gov/compliance/supervision-examinations/
- NACHA Operating Rules (annual). https://www.nacha.org/rules
- 12 CFR Part 1005 — Reg E. https://www.ecfr.gov/current/title-12/chapter-X/part-1005
- 12 CFR Part 1026 — Reg Z. https://www.ecfr.gov/current/title-12/chapter-X/part-1026
- 31 CFR Part 1022 — FinCEN MSB rules including SAR and CTR filing, AML program requirements. https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1022
- CSBS Money Transmission Modernization Act and state money-transmitter licensing — varies by state. https://www.csbs.org/
