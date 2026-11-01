# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — vendor-diligence

When the scope flags banking, load this overlay alongside `references/source-anchors.md`. It carries the banking-only frame that the generic capability skill does not own.

#### Operative supervisory frame

- **Interagency Guidance on Third-Party Relationships: Risk Management** (OCC Bulletin 2023-17, FRB SR 23-4, FDIC FIL-29-2023, June 6, 2023). The diligence lifecycle (planning, due diligence and selection, contract negotiation, ongoing monitoring, termination) is the spine. Apply on a risk-based basis; community-bank tailoring narrative in the guidance is the right anchor for smaller institutions.
- **OCC Bulletin 2013-29** is still cited as the predecessor frame in supervisory practice. Where examiners reference it, treat as supplemental, not operative.
- **FFIEC IT Examination Handbook — Outsourcing Technology Services booklet** is the examiner-facing detail for technology vendors. Pin the current edition.
- **Comptroller's Handbook — Third-Party Relationships: Risk Management** [verify current edition] is the OCC examiner playbook for national banks and federal savings associations.
- **12 CFR Part 30 Appendix D (OCC Heightened Standards)** for covered banks ($50B+): vendor-diligence outputs feed the risk-governance framework and the board's third-party oversight. Diligence packs for important and critical vendors should be visible to the independent risk-management function and reflected in board reporting.
- **FRB SR 12-17** consolidated supervision framework for BHCs: where the vendor sits across legal entities or supports a consolidated activity, the diligence pack should reflect the BHC view, not just the depository view.

#### Banking-only contract anchor

- **Bank Service Company Act, 12 USC §1867(c)** — the statutory examiner-access right over bank service providers. The contract must preserve regulator examination access and audit rights. This is a banking-only clause expectation; non-bank vendor frameworks do not include it. Flag any contract that lacks the clause as a finding regardless of vendor tier.

#### Insider screen

- **Reg O, 12 CFR Part 215** — diligence on a vendor whose principals are insiders (directors, executive officers, principal shareholders) of the partner bank, or affiliates thereof, must include the Reg O screen. Most non-bank vendor-diligence frameworks do not consider this; the banking overlay always does for relevant ownership structures.

#### BaaS and bank-fintech arrangements

- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC, OCC, FRB, July 25, 2024) [verify exact title and date]: where the vendor is a fintech program operator or BaaS platform, the operative document for the diligence is this statement, not just the June 2023 interagency guidance. Specific elements the diligence must cover: end-customer reconciliation, FBO subledger posture, deposit-insurance representation review (and the customer-facing FDIC framing), program-operator operational resilience, and the fourth-party register (processor, KYC vendor, fraud-decision vendor, ledger provider).
- **OCC Bulletin on Bank-Fintech Arrangements** [verify bulletin number]: where present in the firm's source list, treat as supplemental detail.
- **FFIEC inter-agency joint statement on community-bank fintech due diligence** (August 2023) [verify exact title]: for community banks engaging fintech partners; carries an explicit due-diligence checklist.

#### Cross-link inside the plugin

- **`exit-plan` banking overlay** carries the FBO-account wind-down sequence, Reg DD §1030.5 and Reg E §1005.8 customer-notification responsibilities on deposit-account or credit-account termination, and Bank Service Company Act §1867(c) examination-access continuity through wind-down.
- **`concentration-risk-review`**: hyperscaler region, BaaS sponsor-bank reach, and core-banking vendor concentration all feed back into the banking-overlay concentration calculation.
- **`contract-gap-review` banking overlay** carries the Bank Service Company Act clause set, the deposit-insurance-representation clauses for BaaS arrangements, and the OCC Heightened Standards board-visibility clauses.

#### AI vendor mode at a bank

When `ai_vendor=true` and the firm is a bank:

- **Joint interagency Revised Guidance on Model Risk Management (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026)** applies where the vendor supplies a **traditional statistical, quantitative, or non-generative, non-agentic AI model** used in a credit, compliance, or fraud decision. The guidance is most relevant to banking organisations with total assets over $30B and is non-binding (does not set forth enforceable standards). For an in-scope traditional model, diligence must align to model-risk governance, not only third-party risk. Footnote 3 of the guidance text excludes generative and agentic AI from scope.
- **For GenAI or agentic AI vendors**, the model-risk diligence lens routes to NIST AI 600-1 (Generative AI Profile), the NIST AI Risk Management Framework, the EU AI Act where the EU subsidiary is in scope, and the firm's AI-governance framework rather than to 2026-13. Run the AI-vendor branch in the diligence workflow (system-card fit, deployment-context evals, training-data posture, shared-responsibility, prompt-as-customer-data, model-version pin, agent-tool posture for agentic vendors), and chain to `llm-vendor-evidence-review` where the question is "is this evidence pack sufficient for our deployment context".
- **Bank Service Company Act §1867(c)** still applies to AI vendors (traditional or GenAI). The examiner-access clause must extend to AI-system audit logs, evaluation evidence, and incident-response records.
- **OCC and FRB supervisory letters on AI use in banking** where applicable [verify specific letters relevant on the date of analysis] — chase the specific letter cited by the firm's regulatory affairs team.
- Cross-link to `llm-vendor-evidence-review` via `ai_specific_findings.eval_evidence_status = deferred-to-evidence-review` and the linked record ID.

#### Output-template additions for banking

- Bank Service Company Act §1867(c) clause status as a named finding line.
- Reg O insider screen as a named diligence step (status: `not-applicable | clear | flagged`).
- BaaS and bank-fintech-arrangement applicability check, with the July 2024 joint-statement element status.
- OCC Heightened Standards board-visibility status (only for $50B+ covered banks).

#### Common pitfalls in banking diligence

- Treating a non-bank-vendor TPRM checklist as adequate. The banking overlay adds Bank Service Company Act, Reg O, OCC Heightened Standards, and the BaaS / bank-fintech-arrangement layer. None of these are in a generic SaaS diligence template.
- Skipping the consolidated-supervision lens at a BHC.
- Treating the June 2023 interagency guidance as "compliance" rather than as a risk-governance framework with examiner reach. The pack feeds the risk committee, not just the third-party-risk forum.

## capital-markets

### Capital-markets sector overlay — vendor-diligence

When the scope flags capital markets (advisers, broker-dealers, registered funds, asset managers), load this overlay alongside `references/source-anchors.md`. The bank-flavoured interagency-guidance frame is not the operative supervisory frame for non-bank registrants.

#### Operative supervisory frame

There is no single interagency TPRM bulletin for SEC and FINRA registrants. Expectations come through:

- **Investment Advisers Act Rule 206(4)-7** — the compliance-program rule for advisers. The adviser must have written policies and procedures reasonably designed to prevent violations; oversight of service providers is part of that.
- **Investment Company Act Rule 38a-1(a)(4)** — the fund's compliance-program rule, including service-provider compliance-program-adequacy assessment for transfer agent, custodian, fund accountant, principal underwriter, valuation designee, pricing services. The fund CCO oversees.
- **FINRA Rule 3110 (supervision)** — for broker-dealers, supervisory obligations extend to outsourced functions.
- **SEC Division of Examinations Risk Alerts** on outsourced CCO arrangements (the SEC's 2022 Risk Alert is the most-cited; [verify exact title and date]).
- **Sub-adviser oversight**: where a sub-adviser is the vendor, oversight under the fund adviser's 38a-1 program and the contractual code-of-ethics reach are operative; soft-dollar and affiliated-broker conflicts are part of the diligence.

#### Custody Rule

- **Investment Advisers Act Rule 206(4)-2** — where the vendor touches client assets, qualified custodian status, account-statement delivery, surprise audit, SLOA inventory all enter the diligence.

#### Trade-execution venue diligence

- **Best execution** under Investment Advisers Act §206 fiduciary duty and FINRA Rule 5310 — broker selection and trade-execution venue diligence overlap with `best-execution-surveillance` (capital-markets sector skill). Where the diligence vendor is an execution venue, ATS, or broker-dealer counterparty, the best-execution diligence belongs alongside the third-party-risk diligence.

#### Reg S-P (May 2024 amendments)

- **17 CFR Part 248 (Reg S-P) as amended May 2024** [verify exact compliance dates by entity type and size]: safeguarding and customer-notice obligations imposed on covered institutions; service-provider written-contract requirements; breach-notification timing. The diligence pack must surface Reg S-P contract elements and the vendor's breach-notification-clock posture.

#### Form ADV currency

- **Form ADV Part 2A Item 10 and Item 14** disclosures of material relationships with related and unrelated third parties. Diligence outputs feed brochure currency. Where a new vendor relationship is material, the brochure-update path is part of the human-review chain.

#### Outsourced CCO

- Where the vendor is an outsourced CCO or compliance-service provider, the SEC's 2022 Risk Alert sets the bar [verify exact title and date]. Diligence must address: independence, resourcing, expertise, access to information, and reporting-line clarity to the adviser's senior management or the fund board.

#### AI vendor mode for advisers and BDs

When `ai_vendor=true`:

- **SEC focus on AI / predictive analytics in adviser practices** — risk-alert and rulemaking activity has been ongoing; pin the current state on the date of analysis [verify].
- **SEC proposed rule on conflicts of interest in the use of predictive data analytics** (proposed July 26, 2023) — track current state [verify whether final, withdrawn, repurposed].
- **Marketing Rule (Rule 206(4)-1)** — AI-generated marketing content (hypothetical performance, testimonials, endorsements, AI-personalised content) must comply. Diligence on a vendor providing marketing-AI must flag the Marketing Rule reach.
- **Reg BI care obligation** for broker-dealers — where AI surfaces a recommendation to a retail customer, the BD's documentation of the care analysis must reflect the AI's role.
- **Rule 204-2 books-and-records** — AI outputs that support an investment decision are likely required to be retained; the diligence must surface the vendor's retention and exportability posture.

Cross-link to `llm-vendor-evidence-review` via `ai_specific_findings.eval_evidence_status = deferred-to-evidence-review`.

#### Fund-board reach

- For registered funds, material vendor changes (especially custodian, transfer agent, fund accountant, sub-adviser, valuation designee) trigger fund-board notice or approval and may trigger Form N-CEN reporting on certain service-provider changes.
- ICA §15 considerations apply when the adviser or sub-adviser is being replaced — shareholder-vote thresholds and interim-contract authority are part of the planning lens.

#### Cross-link inside the plugin

- **`exit-plan` capital-markets overlay** carries the transfer-agent migration, custodian transition, fund-accountant change, sub-adviser termination mechanics, including 38a-1 board-notification posture and Reg S-P record-return obligations.
- **`contract-gap-review` capital-markets overlay** carries the Reg S-P clause set, the Custody Rule SLOA terms, and the sub-adviser code-of-ethics clauses.

#### Output-template additions for capital markets

- Registration-class scoping line: adviser, BD, registered fund, dual-registrant, state-registered IA.
- Service-provider category against Rule 38a-1(a)(4) when the firm is a fund adviser.
- Custody Rule applicability check.
- Reg S-P clause status as a named line.
- Marketing Rule applicability check when the vendor produces or distributes investment-related content.
- Form ADV Part 2A Item 10 / Item 14 brochure-update trigger as a named line.

#### Common pitfalls in capital-markets vendor diligence

- Importing the bank interagency-guidance frame as if it were operative for an adviser or BD.
- Missing the fund-board notice/approval path for service-provider changes at a registered fund.
- Treating an outsourced-CCO arrangement as a routine vendor when it is a compliance-program-design relationship subject to its own SEC focus.
- Missing the Reg S-P May 2024 service-provider clause set when reusing a pre-2024 contract template.
- Skipping the Marketing Rule analysis on a marketing-content vendor.

## insurance

### Insurance sector overlay — vendor-diligence

When the scope flags insurance, load this overlay alongside `references/source-anchors.md`. The insurance overlay carries what the bank-flavoured capability skill does not.

#### Vendor types specific to insurance

The diligence must recognise the insurance-specific vendor population: managing general agent (MGA), managing general underwriter (MGU), third-party administrator (TPA), claims administrator, underwriting bureau, actuarial outsourcer, IT outsourcer, AI / ML vendor, ECDIS data provider, illustration-software vendor. Each pulls a different model-law set into the diligence.

#### Operative model laws

- **NAIC Insurance Holding Company System Regulatory Act (Model #440)** [verify model number] and **Holding Company Model Regulation (Model #450)** [verify model number]: Form B and Form D filings where the vendor is an affiliate of the carrier. This is not a federal-banking concept; the bank-flavoured generic skill misses it.
- **NAIC Insurance Data Security Model Law (Model #668), §4.F third-party service-provider obligations**: due-diligence, written-contract terms, monitoring, incident-response cooperation, breach-notification chain. Distinct from federal interagency-guidance third-party expectations. Adoption is state-by-state; the NAIC adoption tracker is the public reference.
- **NAIC Producer Licensing Model Act** [verify model number]: any vendor exercising binding or producer authority requires per-state producer licensing. The diligence checklist must include a per-state licensing confirmation for any vendor that quotes, binds, services, or sells.
- **NAIC Unfair Trade Practices Act (Model #880)** and the carrier's state-by-state unfair-claims-settlement-practices acts: where the vendor sits in a claims process, the standards apply regardless of who actually executes the claim decision.
- **State Department of Insurance bulletins** on specific outsourced functions where the carrier is licensed; pin the bulletins by state and date.

#### ORSA fit

- **NAIC Risk Management and Own Risk and Solvency Assessment Model Act (Model #505)** [verify model number]: critical outsourced functions belong in the ORSA Summary Report. The diligence pack must call out ORSA-fit as a named status. Materiality is carrier-specific; the diligence consumes the carrier's ORSA materiality threshold and applies it.

#### AI vendor mode at an insurer

When `ai_vendor=true` and the firm is an insurer:

- **NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023)**: the carrier remains accountable for vendor and third-party AI used on its policies. AIS Program elements (governance, risk management, testing, validation, third-party-AI accountability, monitoring, documentation, transparency, fairness) apply to the vendor through the carrier. Adoption is state-by-state; consult the NAIC AI Working Group adoption tracker.
- **State DOI AI bulletins**: Colorado SB 21-169 implementing regulation (life-insurance underwriting); NY DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting (January 2024) [verify exact circular number]; California DOI bulletin on AI use in insurance [verify exact bulletin]. Each has its own scoping (life-only in CO and NY; broader in CA); pin by state.
- **HIPAA Privacy and Security Rules** apply where the AI touches PHI (health-claims AI, life-and-health underwriting AI using prescription-history or medical data). HIPAA business-associate posture must be evidenced.
- **Producer / agent licensing**: any consumer-facing AI that takes actions on policies (binding, quoting commitments, surrendering, paying claims) can trigger producer licensing questions. Flag for the licensing function.
- **EU AI Act extraterritoriality**: insurance pricing and risk-assessment in life and health is named as a high-risk use case under Annex III of Regulation (EU) 2024/1689. US carriers writing in EU branches or doing reinsurance with EU cedents can inherit the obligation.
- **NIST AI RMF 1.0** Govern function for AI vendors; **NIST AI 600-1** for GenAI vendors.

Cross-link to `llm-vendor-evidence-review` via `ai_specific_findings.eval_evidence_status = deferred-to-evidence-review` for the deeper evidence-pack review.

#### Cyber sub-overlay

- **NAIC Insurance Data Security Model Law (Model #668)** is the insurance-specific cybersecurity frame. Where adopted, it applies in addition to or in some states instead of NYDFS Part 500. §4.F third-party-service-provider obligations carry the cyber expectation chain to the vendor and its sub-processors. Incident-response cooperation language has to be in the contract; this is a frequent gap.

#### Cross-link inside the plugin

- **`exit-plan` insurance overlay** carries TPA / claims-administrator transition mechanics, ORSA notification, and policyholder-communication responsibilities.
- **`contract-gap-review` insurance overlay** carries Model #668 §4.F clauses, HIPAA BAA terms, NAIC Bulletin Dec 2023 third-party-AI accountability clauses, and the producer-licensing representation set.
- **`concentration-risk-review`**: TPA, reinsurance, and claims-AI vendor concentration feed the insurance-overlay concentration calculation.

#### Output-template additions for insurance

- Vendor-type-by-applicable-Model crosswalk row: which NAIC Model applies to this vendor type.
- Per-state producer-licensing confirmation table where the vendor exercises producer authority.
- HIPAA business-associate posture as a named line.
- ORSA-fit status as a named line.
- AIS Program element-by-element status when `ai_vendor=true`.
- Form B / Form D applicability check when the vendor is an affiliate.

#### Common pitfalls in insurance vendor diligence

- Applying federal banking guidance and skipping NAIC Model #668 §4.F.
- Missing the per-state producer-licensing confirmation.
- Treating the NAIC AI Bulletin as US-uniform when adoption is state-by-state.
- Skipping the HIPAA business-associate analysis on a "tech vendor" that incidentally touches PHI.
- Missing the ORSA-fit assessment and only producing a third-party-risk-forum-grade pack when the vendor is enterprise-material.

## payments-fintech

### Payments-fintech sector overlay — vendor-diligence

When the scope flags payments or fintech (sponsor-bank programs, BaaS platforms, money transmitters, MSBs, card-program operators), load this overlay alongside `references/source-anchors.md`.

#### Operative supervisory frame

- **Interagency Guidance on Third-Party Relationships: Risk Management** (OCC / FRB / FDIC, June 6, 2023) is the spine for any bank-side review of a fintech counterparty.
- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact date and title] is the operative document for sponsor-bank programs. Diligence on a BaaS or program-operator counterparty must cover end-customer reconciliation, FBO subledger posture, deposit-insurance representation review (and customer-facing FDIC framing), program-operator operational resilience, and the fourth-party register. The 2023 RFI on bank-fintech arrangements is not the binding statement; cite-checks must catch the conflation [verify which artifacts are operative on the date of analysis].
- **FFIEC inter-agency joint statement on community-bank fintech due diligence** (August 2023) [verify exact title]: where the firm is a community bank engaging a fintech, this statement carries an explicit due-diligence checklist.

#### Vendor-type taxonomy

The diligence must identify the counterparty's role on each rail and across the program:

- Sponsor bank
- BaaS platform / program manager
- Processor (front-end, back-end, gateway)
- BIN sponsor
- Ledger provider
- Card-issuance vendor
- KYC / CIP vendor
- Fraud-decision vendor
- Sanctions-screening vendor
- Dispute-management vendor
- FedNow / RTP gateway
- ACH originator-of-record vendor (Third-Party Sender)
- Aggregator / developer-portal vendor

Each pulls a different rule set into the diligence checklist.

#### NACHA

- **NACHA Operating Rules (current edition)** Third-Party Sender registration and risk-management rules [verify rule citations]: any counterparty acting as a Third-Party Sender on the firm's ODFI authority must have registration on file, the underlying Originator agreements documented, and return-rate-monitoring posture against current NACHA thresholds (administrative-return, overall-return, unauthorized-return) [verify current thresholds]. NACHA citations are paywalled; mark as "current edition; specific sections to be confirmed against the firm's licensed copy."

#### MSB / state money-transmitter licensing

- **FinCEN MSB rules at 31 CFR Part 1022** where the counterparty is itself a money transmitter: registration on file, written AML program, CIP applicability where applicable, SAR-filing posture.
- **State money-transmitter licensing**: NMLS status on a per-state basis. **Money Transmitter Modernization Act** adoption posture in the firm's footprint [verify state-by-state adoption status as of the date of analysis].
- **NY DFS BitLicense** (23 NYCRR Part 200) for virtual-currency activity in NY.
- **CA DFPI** rulemaking under the Money Transmission Act and California Consumer Financial Protection Law.

#### Card networks

- **Visa Core Rules and Visa Product and Service Rules; Mastercard Rules** [verify against firm's licensed copy]: BIN sponsor accountability for chargeback rights, fraud-rate program escalations (Visa Fraud Monitoring Program and Mastercard Excessive Fraud Merchant program), and program-level reporting.
- Card-network rulebooks are paywalled. Mark all citations as "current edition; specific sections to be confirmed against the firm's licensed copy."

#### Reg E reach

- **Reg E (12 CFR Part 1005)** §1005.6 (consumer-liability), §1005.11 (error-resolution), §1005.18 (prepaid-account additions): the program operator owes downstream Reg E posture to consumers even where the depository is the bank. The program agreement nearly always pushes operational ownership of error intake to the fintech, and the diligence has to capture that allocation. Examiners pursue both Reg E and UDAAP findings where the timing windows slip.

#### Cyber and resilience layer

- **NYDFS 23 NYCRR Part 500** where the counterparty is a covered entity.
- **GLBA Safeguards Rule** passed through the program agreement.
- **FFIEC IT booklets** used by sponsor-bank examiners.

#### CFPB direct supervision

- **CFPB §1024 larger-participant rules** for digital wallets and payment apps (December 2024) [verify Federal Register citation, effective date, and current state including any litigation or congressional review]. Where the fintech is a designated larger participant, the CFPB has direct supervisory and examination authority. The diligence pack must surface applicability and the fintech's CFPB-readiness posture as relevant to the firm's bank.
- **CFPB Circular series** on account closures and holds, junk-fees, dark patterns, and FDIC misrepresentation. Many CFPB Circulars (UDAAP, overdraft / NSF, adverse-action with complex algorithms, account reopening) were **withdrawn May 12, 2025; historical only** — anchor diligence findings to the regulatory text rather than the withdrawn circular layer. The CFPB BNPL Interpretive Rule (May 2024) was separately **nullified by Pub. L. 119-11 (May 9, 2025); historical only.**

#### Cross-link inside the plugin

- **`exit-plan` payments-fintech overlay** carries rail-by-rail wind-down mechanics (ACH and Same Day ACH cutover, wire and FedNow / RTP settlement-finality posture, card BIN re-sponsorship, in-flight-item carry-over register, FBO subledger reconciliation).
- **`concentration-risk-review` payments-fintech overlay** carries the three-axis concentration view: sponsor-bank, processor, BIN-sponsor.
- **`contract-gap-review` payments-fintech overlay** carries the program-agreement clause set, NACHA Third-Party Sender clauses, deposit-insurance-representation clauses, and the Reg E error-handling allocation.

#### AI vendor mode in payments

When `ai_vendor=true` and the counterparty is a payments / fintech vendor (commonly fraud-decision, CIP / KYC, dispute-decision, or customer-service AI):

- The bank-fintech-arrangement frame still applies; the AI overlay layers on top.
- Reg E §1005.11 timing applies regardless of who or what produced the decision.
- BSA / AML and sanctions diligence on AI vendors that influence transaction-monitoring or sanctions-screening outcomes: model-risk overlay applies via cross-link to model-risk skills.

#### Output-template additions for payments-fintech

- Rail-by-rail counterparty role table.
- Sponsor-bank and BIN-sponsor identification.
- MSB / MTL state-by-state licensing matrix.
- NACHA Third-Party Sender posture line.
- Subcontractor / fourth-party register.
- FBO subledger reconciliation evidence status.
- Deposit-insurance representation review status.
- CFPB larger-participant applicability check.

#### Common pitfalls in payments-fintech vendor diligence

- Treating a sponsor-bank program operator as a SaaS vendor and missing the program-agreement-driven obligation allocation (FBO posture, deposit-insurance representation, Reg E timing).
- Skipping the per-state NMLS check on a money-transmitter counterparty.
- Missing the NACHA Third-Party Sender registration question for ACH counterparties.
- Treating card-network rulebook citations as if they were public; they are paywalled.
- Conflating the 2023 RFI on bank-fintech arrangements with the binding July 2024 joint statement.
- Skipping the CFPB §1024 larger-participant applicability check on a digital-wallet or payment-app counterparty.
