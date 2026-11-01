# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — exam-brief

When the scope flags banking and the regulator is one of OCC, FRB, FDIC, NCUA, or a state banking department running a non-full-scope engagement (e.g., a CFPB-coordinated exam at a bank, an NYDFS cyber exam at a state-chartered bank, a coordinated trust exam, an IT-focused exam), load this overlay alongside `references/source-anchors.md`. For a full-scope federal banking exam at a bank carrying the Heightened Standards, route to `banking-supervision-readiness` instead; the readiness sprint there carries the substantive scaffolding. This overlay carries the engagement playbook for the slice that the generic skill owns.

#### Examiner-in-charge convention

The federal banking agencies all run an examiner-in-charge model. The OCC EIC sits inside the assigned supervisory office (Large Bank Supervision, Midsize and Community Bank Supervision, or the Federal Branches and Agencies group); the FRB EIC sits inside the regional Reserve Bank for state-member banks and BHCs; the FDIC EIC sits inside the regional office. The single-point-of-contact relationship matters: the firm's head of regulatory affairs or general counsel runs the day-to-day relationship; the CRO and chief compliance officer run topic-specific contact for their domains. Mapping points of contact to the agency's supervisory team structure (EIC, deputy EIC, subject-matter-expert examiners) avoids the common failure mode of routing every question through one bottleneck.

#### Document-handling — bank examination posture

Federal bank examiners enjoy broad statutory examination access (12 USC §484 for the OCC; equivalent for FRB and FDIC). The firm does not negotiate examiner reach the way a non-bank firm might in an SEC adviser exam. Document handling is therefore production-shaped, not negotiation-shaped. Key practitioner notes:

- Privilege exists but is constrained. Bank-examination privilege protects the agency's own examination materials and confidential supervisory information; the firm's own attorney-client and work-product privilege still attach to firm-side documents. Counsel sets the privilege posture for each request line.
- Confidential supervisory information from prior cycles (supervisory letters, MRAs, MRIAs, exam reports) is the agency's, not the firm's. The firm cannot share CSI outside the firm without the agency's written authorisation under 12 CFR Part 4 Subpart C (OCC), Part 261 (FRB), or Part 309 (FDIC). Onward sharing inside the firm is constrained to a need-to-know population; ensure the production log records who has had CSI access.
- Production typically runs through agency-provided portals or examiner laptops on-site. On-site reading rooms remain common for sensitive material (loan files, board minutes, SARs).

#### MRA / MRIA / consent-order posture

Federal banking MRAs and MRIAs are the two-tier supervisory finding mechanism shared across OCC, FRB, and FDIC. The convention:

- **MRA (Matter Requiring Attention)** — deficiency the bank must address. Typically resolved through the bank's standard issue-management process with bank-side commitment dates.
- **MRIA (Matter Requiring Immediate Attention)** — deficiency of greater significance requiring immediate management attention; expectations of board or board-committee oversight, faster commitment dates, and more frequent agency progress check-ins.
- **Consent order** — formal enforcement action, public, with specific articles, named compliance committee, monitor designation in some cases. Response posture is shaped by the order's articles and milestones; chains to `implementation-plan` for the milestone build-out.

The brief's response-posture section names: who owns the response (typically head of compliance, CRO, or general counsel for the formal letter); what triggers the response clock (receipt of the supervisory letter, not the exit memo); whether board reporting is required (almost always for MRIAs and consent orders, often for material MRAs); whether outside counsel is engaged for the response.

#### Bank-specific anticipated-questions patterns

Examination priorities for federal banking agencies cycle through the year in published statements (semi-annual operating plan from the OCC; annual supervisory priorities communications from FRB; FDIC's published supervisory priorities and FILs). Recent recurring themes that shape anticipated-question lists across OCC, FRB, and FDIC engagements:

- BSA/AML programme effectiveness and 2020 AML Act implementation (priorities cycle).
- Third-party risk management against the June 2023 inter-agency guidance.
- Liquidity and interest-rate risk in the context of recent regional-bank stress.
- Operational resilience and cyber, including incident-notification under the 36-hour rule (12 CFR 53 / 12 CFR 225 / 12 CFR 304).
- Fair lending and CRA where the engagement touches consumer credit.
- Model risk management against SR 11-7 / OCC 2011-12 (and the revised 2026 guidance per OCC Bulletin 2026-13 where applicable [verify bulletin number and current title]).

#### Exit-meeting and supervisory-letter response

The federal banking agencies typically hold an exit conference, then issue a supervisory letter or report of examination, then expect a written firm response within an agency-specific window (commonly 30 to 60 days; agency-specific). The brief should record the response window calculation as: clock starts on receipt of the supervisory letter or final report (not the exit memo), unless the agency has stated otherwise in writing. For MRIAs and consent orders, board-level commitment is expected and the response is typically reviewed by the agency before acceptance.

#### When to hand off to banking-supervision-readiness

If the engagement is a full-scope OCC, FRB, or FDIC bank examination, the substantive readiness sprint belongs in `banking-supervision-readiness`. The generic exam-brief is right when the engagement is:

- A targeted or topic-specific exam at a bank (cyber, IT, BSA-only, model risk, third-party, fair lending, trust).
- A CFPB exam at a depository (CFPB has direct supervisory authority for $10B+ banks and for non-bank consumer-finance providers).
- A state regulator exam (state banking department, NYDFS) that is not the federal full-scope cycle.
- A horizontal review across multiple banks where the bank's piece is one of several.

Where the line is unclear, default to chaining: the generic exam-brief produces the engagement playbook (scope, points of contact, document handling, response posture); the sector-readiness sprint produces the substantive evidence pack.

## capital-markets

### Capital-markets sector overlay — exam-brief

When the scope flags capital-markets activity and the regulator is the SEC Division of Examinations (EXAMS), FINRA, a state securities regulator under NASAA convention, or NYDFS for a NY-licensed broker-dealer, load this overlay alongside `references/source-anchors.md`. For a substantive adviser/asset-manager exam-readiness sprint, route to `adviser-exam-readiness` instead; that readiness sprint carries the IAA Rule 206(4)-7 cadence, marketing rule, custody rule, books-and-records, and Form ADV-specific scaffolding. This overlay carries the engagement playbook for the slice that the generic skill owns, plus the niche capital-markets cases where the generic shape is the right starting point.

#### Examiner convention — SEC EXAMS

The SEC Division of Examinations runs adviser, broker-dealer, investment-company, transfer-agent, and clearing-agency examinations through specialised programs. The engagement playbook differs from federal banking in important respects:

- The exam relationship runs from a regional office (eleven SEC regional offices, plus the home office), with the examiner-in-charge sitting inside the assigned office. The firm's head of compliance or general counsel runs the day-to-day relationship; the CCO is typically the named primary contact for examination correspondence.
- EXAMS issues a notification letter (sometimes by phone with confirming letter), then a document request list with a typical 14-day initial production window. Rolling production is common for large requests; the brief's request-list section captures the staging.
- EXAMS engagements are non-adversarial in posture, but findings can refer to the Division of Enforcement; counsel posture for sensitive areas (custody, marketing, conflicts, MNPI, electronic communications) is calibrated accordingly.
- Exit interview and deficiency letter are the standard close. The deficiency letter sets the firm's response window (typically 30 days). Material findings can lead to a Wells process on referral to Enforcement; that is a separate workflow and the brief flags the trigger when the signals appear.

#### Examiner convention — FINRA

FINRA examinations of member firms (broker-dealers and dual-registrants on the BD side) run on three patterns:

- **Cycle exam** — periodic risk-based cycle, frequency tied to firm risk profile (typically 1, 2, or 4 years).
- **Cause exam** — triggered by specific event (complaint pattern, regulatory referral, FINRA 4530 self-report, customer-arbitration pattern).
- **Sweep / horizontal review** — topic-specific across multiple member firms.

FINRA Rule 8210 governs the production of information and testimony. The 8210 letter is the operative document-request mechanism; failure to comply has its own disciplinary track. The brief's document-handling section names the 8210 letter as the production trigger; counsel posture for 8210 productions and for on-the-record (OTR) testimony is shaped by the topic and by the parallel possibility of FINRA Department of Enforcement referral.

FINRA findings flow through the firm's exam report; significant findings can become Letters of Acceptance, Waiver and Consent (AWC) or formal disciplinary complaints. The brief flags when AWC or complaint signals appear.

#### Document-handling — capital-markets examination posture

Document handling differs from banking in three operative respects:

- The privilege posture is more contestable. SEC EXAMS engagements are non-adversarial in posture, but the firm's attorney-client and work-product privileges are routinely asserted on internal compliance reviews, internal investigations, and counsel-driven testing. The firm's privilege log typically accompanies any redacted production. Counsel sets the privilege posture before each wave.
- Books-and-records under IAA Rule 204-2 (advisers) and Exchange Act Rule 17a-4 (BDs) define what the firm must have available; the request list cannot extend beyond what the regulator's statutory reach supports, but books-and-records reach is broad. The brief notes the rule basis on each request line.
- Electronic communications are a recurring focus area. Off-channel-communications enforcement (driven by SEC and FINRA actions starting 2021 against multiple broker-dealers and advisers) drives request-list emphasis on personal-device messaging, encrypted-app use, and the firm's electronic-communications policy and surveillance evidence. The brief carries the firm's surveillance-evidence posture for this topic.

Production typically runs through agency-provided portals or secure file transfer; on-site fieldwork is more limited than in banking, with virtual-conduct increasingly the norm.

#### Findings and response posture — capital markets

Capital-markets findings do not use the MRA / MRIA convention. The mechanisms:

- **EXAMS deficiency letter** — issues identified during the exam, communicated in the closing letter. The firm responds in writing within the agency-specified window (typically 30 days). Response posture is owner-named (typically CCO or general counsel for the cover letter, with topic SMEs drafting the substantive responses), with an explicit remediation-plan section for any material finding.
- **EXAMS referral to Enforcement** — material findings may refer to the Division of Enforcement; the Wells process is the separate workflow and the brief flags the trigger.
- **FINRA cycle-exam findings** — communicated through the exam report; firm response embeds in the report.
- **FINRA AWC** — formal settlement with sanction; negotiated through Enforcement; the brief notes when the engagement is heading toward AWC posture.
- **FINRA disciplinary complaint** — formal disciplinary proceeding through the FINRA Office of Hearing Officers; outside counsel posture is the default.

The response-posture section names: who owns the response (CCO for the standard EXAMS deficiency letter; general counsel for FINRA disciplinary; outside counsel for any matter heading toward Wells, AWC, or complaint); what triggers the response clock (deficiency-letter date for EXAMS, exam-report date for FINRA cycle); whether board reporting is required (typically yes for fund-board reporting on adviser issues that materially affect the fund, under 38a-1; for BDs and IAs, the firm's governance posture sets the trigger).

#### Anticipated-questions patterns — current capital-markets supervisory priorities

Recurring themes from the SEC EXAMS annual examination priorities and from FINRA's annual Regulatory Oversight Report shape anticipated-question lists:

- Marketing Rule (IAA Rule 206(4)-1) — performance presentation, hypothetical performance use, testimonials and endorsements, books-and-records on marketing materials, third-party-rating use.
- Custody Rule (IAA Rule 206(4)-2) — qualified custodian status, surprise audits, SLOA inventory and authorisations, account statements; pending Safeguarding Rule replacement (proposed February 2023; status [verify current state]).
- Off-channel communications — personal-device messaging, encrypted-app use, surveillance evidence, attestation programs.
- Cybersecurity and Reg S-P (May 2024 amendments) — customer-information safeguarding, breach-notice posture (30-day customer notice), service-provider contractual posture; pending adviser/fund cybersecurity rule [verify current state].
- AI and predictive analytics — adviser/BD use of AI in research, marketing, and client communications; SEC proposed rule on conflicts in predictive data analytics (proposed July 2023, status [verify current state]); marketing-rule reach for AI-generated content.
- Conflicts of interest and Reg BI (BD) and IA fiduciary duty — care obligation documentation, retail-investor protection, complex-products distribution.
- Private-fund advisers — ongoing supervisory attention notwithstanding the June 2024 vacatur of the Private Fund Advisers Rule; antifraud, recordkeeping, and conflicts-disclosure reach remains.
- Books-and-records currency — IAA Rule 204-2 and Exchange Act Rule 17a-4 compliance, including electronic-communications records.
- 38a-1 program adequacy — fund-adviser CCO testing, board reporting, annual review documentation.

For BDs specifically, FINRA themes recur: net capital under Exchange Act Rule 15c3-1, customer protection under Rule 15c3-3, OBA / PST under FINRA Rule 3270 / 3280, AML program under FINRA Rule 3310 (with Bank Secrecy Act reach), best execution under FINRA Rule 5310, Reg BI compliance, communications with the public under FINRA Rule 2210.

#### State-securities and NASAA convention

For state-registered IAs (under $100M AUM threshold and not federally covered for other reasons), the state securities regulator runs the exam under state law. NASAA model rules harmonise practice across states, but the adopting statute is the operative authority. The brief's regulator field names the state and the office; document-handling follows state convention.

#### NYDFS overlay for NY-licensed BDs

For NYDFS engagements at NY-licensed BDs, layer NYDFS-specific conventions:

- NYDFS Cybersecurity Regulation (23 NYCRR Part 500) applies; cyber-targeted exam scaffolding applies (cf. `cyber.md` cross-cutting overlay when present).
- NYDFS Virtual Currency Regulation (23 NYCRR Part 200) applies for BitLicense-holding entities; the engagement playbook differs materially.

#### When to hand off to adviser-exam-readiness

If the engagement is a substantive SEC adviser, BD, or investment-company exam at the firm and the firm has the capacity to run the readiness sprint, route to `adviser-exam-readiness`. The generic exam-brief is right when the engagement is:

- A targeted EXAMS sweep on a single topic (Marketing Rule sweep, off-channel communications sweep, AI sweep) where the substantive readiness pack is too broad.
- A FINRA cycle exam at a BD where the engagement playbook (8210 production, OTR posture, AWC trigger) is the operative scaffolding rather than the substantive readiness review.
- A state-securities exam at a state-registered IA where NASAA convention applies.
- A horizontal review across multiple firms where the firm's piece is one of several.
- A cyber-targeted or AI-targeted slice within a larger engagement led by a sister skill.

Where the line is unclear, default to chaining: the generic exam-brief produces the engagement playbook (regulator, scope confirmation, document-handling and privilege posture, points of contact, response window); the sector-readiness sprint produces the substantive evidence pack and the obligation-by-obligation status mapping.

## insurance

### Insurance sector overlay — exam-brief

When the scope flags insurance and the regulator is a state department of insurance (state DOI), a coordinated multi-state team led under NAIC framework, the lead-state regulator on a financial exam, or NYDFS for an NY-domiciled or NY-licensed insurer, load this overlay alongside `references/source-anchors.md`. The federal-banking exam-readiness sprint pattern does not apply to insurance; there is no single insurance equivalent to the OCC, FRB, or FDIC examiner-in-charge convention because state DOIs run their own examination programs under their own statutes. The NAIC handbooks set inter-state convention for adoption by state DOIs, but the adopting statute is the operative authority, not the handbook itself.

#### Two-track examination model

State DOIs run two distinct examination tracks. The brief carries which track is in scope; running the wrong scaffolding is the most common failure mode.

- **Financial examination** — solvency-focused, conducted on a multi-year cycle (typically every three to five years per state law), led by the lead-state DOI for multi-state coordination. The examiner-in-charge sits inside the lead-state DOI; participating-state examiners may join the team. The output is a public Report of Examination (ROE) filed under state insurance code. Anchored to the NAIC Financial Condition Examiners Handbook structure (planning, risk assessment, examination procedures, reporting, communication of findings).

- **Market conduct examination** — consumer-protection-focused, may run on a triennial cycle, may run for-cause based on complaint patterns or market-conduct annual statement (MCAS) data, may run as a multi-state coordinated examination through the NAIC Market Action Working Group. Anchored to the NAIC Market Conduct Examiners Handbook structure (Chapter 16 standardised data calls; chapter-by-chapter exam standards covering operations and management, complaint handling, marketing and sales, producer licensing, policyholder services, underwriting and rating, claims).

A combined or "comprehensive" exam runs both tracks in parallel; the brief still carries the two scopes separately because the document-handling postures and the finding mechanisms differ.

#### Document-handling — insurance examination posture

State DOIs enjoy broad statutory examination access under each state's insurance code (typically modelled on NAIC Model Laws #390 Examiner Handbook Authority and #392 Market Conduct Surveillance). Document handling differs from federal banking on three dimensions:

- The lead-state DOI in a coordinated financial exam has the production relationship; participating states receive the work product through the lead state. The brief names the lead state and the participating-state list; document production runs through the lead.
- Confidential examination materials are protected under each state's confidentiality statute (typically modelled on NAIC Model Law #210 §6 or equivalent) and under NAIC's confidentiality regime for shared work product. The firm's onward sharing of supervisory letters, exam reports, and ROE drafts is constrained; counsel sets the posture per state.
- The examination-by-contractor model is common: state DOIs frequently engage outside accounting and actuarial firms as deputy examiners. The contractor sits inside the agency for examination purposes; the firm's privilege posture treats them as agency.

Production typically runs through agency-provided portals, secure file transfer, or examiner laptops on-site; on-site reading rooms remain common for sensitive material (claim files, complaint files, executive compensation, reinsurance treaties).

#### Findings and response posture

Insurance examinations do not use the MRA / MRIA two-tier convention from federal banking. The findings mechanism is:

- **Examiner comment / examination finding** — issue identified during fieldwork, communicated in the examination report draft. The firm responds in writing; the response becomes part of the examination record.
- **Recommendation** — formal recommendation in the examination report; the firm's response posture and remediation plan attach to the public ROE in some states.
- **Order or stipulation** — formal regulatory action, public, with specific articles, often with monetary penalty and required corrective action plan. Response posture is shaped by the order's articles and by state administrative procedure.

The brief's response-posture section names: who owns the response (head of compliance for market-conduct findings; CFO or chief actuary for financial findings; general counsel for any matter heading toward an order); what triggers the response clock (typically receipt of the draft examination report, with an agency-specific window of 30 to 60 days commonly, state-specific); whether board reporting is required (typically yes for any matter that will land in the public ROE); whether outside counsel is engaged.

#### Insurance-specific anticipated-questions patterns

Recurring market-conduct themes shaping anticipated-question lists across state DOI engagements:

- Complaint handling and root-cause-analysis quality (driven by NAIC Complaint Database and MCAS data); is the firm's complaint taxonomy aligned with NAIC categories.
- Producer licensing and appointment management; producer training currency; producer compensation conflicts.
- Claims practices, including unfair claims settlement practices under NAIC Model Law #900 and state-specific unfair-claims statutes; timeliness, denial-rationale documentation, claim-file-completeness.
- Underwriting and rating, including filed-form-and-rate compliance, rate-deviation justification, accelerated underwriting and external-data use under NAIC Bulletin and state-specific guidance, AI and predictive-model use under NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (adopted 2023, state-by-state adoption status varies — [verify state-by-state adoption]).
- Policyholder services, including replacement-and-suitability for life and annuity, free-look handling, premium-handling.
- Privacy and cybersecurity under NAIC Insurance Data Security Model Law (#668), state-by-state adoption status varies; NYDFS Part 500 for NY-licensed entities.

Recurring financial-exam themes:

- Reserves adequacy and actuarial-opinion quality; consistency with the appointed-actuary's report.
- Investment portfolio and SAP-vs-GAAP treatment; affiliate transactions under NAIC Model Law #440.
- Reinsurance, including credit-for-reinsurance and collateral arrangements, under NAIC Model Law #785 / #786.
- ORSA (own risk and solvency assessment) under NAIC Model Law #505; recent ORSA Summary Report quality.
- Holding company filings under NAIC Model Law #440 (Form A, B, D, F as applicable).

#### Lead-state coordination for multi-state engagements

For multi-state insurers, the lead-state DOI runs the financial exam under NAIC Financial Condition Examiners Handbook coordination conventions. The brief's scope-window section names: lead state, participating states, NAIC support if any, and the convention for sharing the draft report among participating states before issuance to the firm. Multi-state market-conduct exams run through the NAIC Market Action Working Group (MAWG) where adopted; the brief names the MAWG-coordinated states.

#### NYDFS-specific posture

For NYDFS engagements at NY-licensed insurers, layer NYDFS-specific conventions on top of the NAIC scaffolding:

- NYDFS regulates both market conduct and solvency for NY-licensed insurers; the conventions differ from generic state DOI in the formality of the supervisory-letter and consent-order machinery.
- NYDFS Cybersecurity Regulation (23 NYCRR Part 500) applies to most NY-licensed insurers (with limited exemptions); cyber-targeted exam scaffolding applies (cf. cross-cutting `cyber.md` overlay when present in the plugin).
- NYDFS Insurance Regulation 187 (suitability and best interests in life insurance and annuity transactions) drives a distinct examination posture for NY annuity sales.

#### When this overlay applies and when it does not

This overlay applies for the engagement playbook on a state DOI examination. There is no separate sector exam-readiness skill for insurance in this plugin set; the substantive readiness work runs against the firm's existing program, with this overlay framing the engagement-side mechanics. If a future `insurance-prudential-conduct/insurance-exam-readiness` skill is added, the substantive readiness sprint moves there and this overlay continues to carry the engagement playbook.

## payments-fintech

### Payments and fintech sector overlay — exam-brief

When the scope flags payments or fintech activity and the regulator is the CFPB exercising direct supervisory authority over a larger non-bank participant, FinCEN for an MSB examination, a state money-transmitter regulator (under NMLS / state-by-state framework, with growing alignment under the CSBS Money Transmission Modernization Act adopted by states beginning 2022), or a state UDAP/consumer-protection authority, load this overlay alongside `references/source-anchors.md`. The federal-banking sector skill does not apply to a non-bank fintech without a sponsor bank; the substantive readiness sprint runs against the firm's existing program with this overlay framing the engagement-side mechanics.

#### Two distinct supervisory tracks

Payments and fintech firms face two operative supervisory tracks; the brief carries which track is in scope.

- **CFPB direct non-bank supervision** — under the Consumer Financial Protection Act (CFPA), the CFPB has direct supervisory authority over (i) any non-bank in the residential mortgage, private student lending, and payday lending markets; (ii) any "larger participant" in a market the CFPB has defined by rule (consumer reporting, consumer debt collection, international money transfers, automobile financing, student loan servicing, general-use digital consumer payment applications added by November 21, 2024 final rule [verify current operative status; the rule has been the subject of post-publication challenge and CFPB reconsideration since 2025]); (iii) any non-bank the CFPB determines, after notice and reasonable opportunity to respond, poses risks to consumers under the "risk-based" authority. The CFPB exam playbook for non-banks parallels its bank-side playbook (CFPB Supervision and Examination Manual; baseline review modules; on-site or virtual fieldwork; supervisory letter; Matters Requiring Attention).

- **State money-transmitter examination** — state-by-state under each state's money-transmitter act, increasingly harmonised under the Money Transmission Modernization Act (MTMA, adopted by a growing number of states 2022-2026 [verify current state-by-state adoption count]). NMLS is the licensing system; multi-state examinations are coordinated through the Multistate MSB Examination Taskforce (MMET) for licensed money transmitters operating in multiple states.

- **FinCEN Bank Secrecy Act examination of MSBs** — FinCEN delegates BSA examination authority for MSBs to the IRS Small Business / Self-Employed Division (IRS-SBSE BSA Examination Program) as a general matter, with state regulators also conducting BSA-related work as part of state money-transmitter exams. Federal MSB BSA exams therefore typically come through the IRS BSA Examination program, not directly from FinCEN. The brief names the operative examiner.

A non-bank fintech with a bank-partnership model carries a fourth track: the sponsor bank's regulator (OCC, FRB, FDIC, or state banking) examines the bank's third-party-risk program over the fintech, which can produce a parallel examiner request to the fintech under the bank's TPRM regime. That is not a direct supervisory engagement; the brief names it as a sponsor-bank-driven request and routes the substantive scaffolding through `vendor-diligence` and `third-party-operational-resilience` skills.

#### Document-handling — non-bank supervision posture

CFPB non-bank examinations carry document-handling posture similar to CFPB bank-side examinations:

- The CFPB Confidential Supervisory Information rule (12 CFR Part 1070 Subpart D) restricts the firm's onward sharing of CSI; the firm cannot share CSI outside the firm without CFPB authorisation.
- Privilege exists; the firm's attorney-client and work-product privileges still attach to firm-side documents; CFPB-side examination materials are CFPB's CSI.
- Production typically runs through CFPB-provided portals; on-site fieldwork remains common for the larger non-bank-participant engagements.

State money-transmitter examinations vary by state; multi-state MMET examinations run through a coordinated production model with the lead state taking primary delivery. The brief names the lead state and the participating-state list.

IRS BSA examinations of MSBs run under IRS examination convention; production is through agency-provided channels. Privilege posture is set by counsel.

#### Findings and response posture — payments and fintech

CFPB findings use Matters Requiring Attention by parallel convention to the federal banking agencies. Material findings can refer to the CFPB Office of Enforcement; the firm's response posture flags the trigger when the signals appear. The CFPB's Civil Investigative Demand (CID) authority sits separately from supervision and is the operative mechanism on the enforcement track.

State money-transmitter findings flow through the state's examination report; multi-state MMET findings are communicated through the lead state. State enforcement (consent orders, license suspensions) is the formal mechanism for material non-compliance.

IRS BSA examinations of MSBs can result in deficiency notices and, in serious cases, FinCEN civil money penalty referrals.

The response-posture section names: who owns the response (head of compliance for the standard CFPB or state response; general counsel for any matter heading toward enforcement); what triggers the response clock (CFPB supervisory-letter receipt date; state-specific for money-transmitter exams; IRS examination-report date for BSA); whether board reporting is required (typically yes for material findings at the firm's governance level); whether outside counsel is engaged.

#### Anticipated-questions patterns — payments and fintech

Recurring themes shaping anticipated-question lists in CFPB non-bank engagements:

- UDAAP — unfair, deceptive, or abusive acts or practices under CFPA §1031; recurring CFPB Supervisory Highlights themes drive the topic mix (the most recent edition is the operative source for the firm's anticipated-question list).
- Fair lending and consumer-credit reach where the firm extends credit (ECOA / Reg B; FCRA / Reg V if consumer-reporting touched).
- Reg E (Electronic Fund Transfer Act) error-resolution and unauthorised-transaction handling for prepaid and digital-wallet products.
- Remittance Rule (Reg E Subpart B) for international money-transfer providers covered by the larger-participant rule.
- Section 1071 small-business-lending data collection where the firm extends business credit (**§1071 revised final rule, May 1, 2026: 1,000 covered transactions; effective June 30, 2026; compliance January 1, 2028** — supersedes the 2023 tiered schedule).
- Buy-now-pay-later, earned-wage access, and other newer product categories. The CFPB BNPL interpretive rule (May 2024) was **nullified by Pub. L. 119-11 (May 9, 2025); historical only**; current CFPB BNPL supervisory posture has receded with the broader May 12, 2025 guidance withdrawal — verify current state on the engagement date.
- Junk-fee themes from CFPB Supervisory Highlights and the regulatory text. (Many CFPB Circulars on overdraft, NSF, junk-fee, and abusive-practices were **withdrawn May 12, 2025**; treat as historical interpretive context.)
- Complaint-handling effectiveness against the CFPB Consumer Complaint Database pattern for the firm's product line.
- Authorised-push-payment fraud and the firm's Reg E error-resolution posture for fraud-induced transactions [verify current CFPB position].

Recurring themes for state money-transmitter examinations:

- Permissible investments and net-worth requirements under state law (with MTMA adoption progressively harmonising the standards).
- Customer funds segregation and trust-account or permissible-investment posture.
- BSA / AML program effectiveness — overlap with the IRS BSA examination scope; the brief names the coordination posture if both are running.
- OFAC sanctions screening effectiveness.
- Surety bond adequacy.
- Disclosures, receipts, and fee transparency under state-specific consumer-protection statutes.
- Sub-agent and authorised-delegate oversight.

Recurring themes for IRS BSA examinations of MSBs:

- AML program adequacy under 31 CFR §1022.210 (program rule for MSBs), including the four-pillar program requirements as they apply to MSBs (the FinCEN beneficial-ownership rule's Customer Due Diligence requirement applies to banks and certain other covered financial institutions, not to MSBs as a categorical matter [verify current CDD-rule applicability to MSBs]).
- Currency Transaction Report and Suspicious Activity Report filing quality and timeliness.
- Recordkeeping under 31 CFR §1022.410 and §1022.420.
- Agent oversight and the MSB principal's obligations for sub-agent compliance.
- OFAC and FinCEN GTO compliance where applicable.

#### Sponsor-bank-driven request handling

Where a non-bank fintech operates under a sponsor-bank model and receives an examiner request driven by the sponsor bank's regulator (OCC, FRB, FDIC, or state banking), the brief carries the request as a third-party-driven engagement, not as a direct supervisory engagement. The fintech's response runs through the sponsor bank under the partnership agreement; the sponsor bank's regulator does not have direct supervisory authority over the non-bank fintech absent CFPB or other direct authority. The substantive scaffolding for the response runs through `vendor-diligence` and the `third-party-operational-resilience` skills.

#### Multi-track coordination posture

Where two or more tracks run concurrently (CFPB non-bank exam + state money-transmitter cycle exam, IRS BSA + state money-transmitter, sponsor-bank-driven + direct CFPB), the brief carries each engagement separately but maintains a coordination posture: shared evidence asks across exams should be answered consistently; the firm-side production log records which document went to which regulator; CSI from one regulator does not get shared with another without explicit authorisation.

#### When this overlay applies and when it does not

This overlay applies for the engagement playbook on payments and fintech examinations. There is no separate sector exam-readiness skill for payments-fintech in this plugin set; the substantive readiness work runs against the firm's existing program with this overlay framing the engagement-side mechanics. If a future `payments-fintech-supervision/non-bank-exam-readiness` skill is added, the substantive readiness sprint moves there and this overlay continues to carry the engagement playbook.
