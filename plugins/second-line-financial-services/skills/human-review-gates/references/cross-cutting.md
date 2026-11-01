# cross-cutting

One section per topic. Read only the sections the scope calls for.

## conduct

### Conduct cross-cutting overlay — human-review-gates

Loads when the scope `cross_cutting_overlay_set` includes `conduct`. The overlay shapes the gate matrix when gates cover customer-facing decisions: product approval, fee-change approval, marketing approval, restitution approval, fair-lending second-look on adverse action, sales-practice supervision, and complaint-handling escalation.

#### Why conduct belongs in customer-facing gate matrices

Customer-impact decisions carry distinct supervisory expectations: the CFPB UDAAP exam manual frames the unfair, deceptive, or abusive lens; ECOA frames the second-review-of-adverse-action lens; FINRA's Rule 2111 (suitability) and Reg BI (Regulation Best Interest) frame the broker-dealer customer-impact lens; state DOI conduct-of-business regulation frames the insurance-claims-and-sales lens. A gate matrix that treats customer-facing decisions as administrative misses the substantive criteria that examiners will probe and the restitution-eligibility analysis that often follows from a gate failure.

#### Source basis

- **CFPB Supervision and Examination Manual — UDAAP**. The CFPB's UDAAP analytical framework is the reference for "unfair", "deceptive", and "abusive" determinations on consumer-facing acts and practices. The framework's three-prong tests (substantial injury, not reasonably avoidable, not outweighed by countervailing benefits — for unfairness; representations, omissions, and practices that mislead, materially — for deception; specific abusive criteria) are the named criteria for UDAAP risk-review gates.
- **CFPB Supervision and Examination Manual — Compliance Management System (CMS)**. The CMS chapter framing the four CMS pillars: board and management oversight, compliance program, consumer complaint response, and compliance audit. The CMS framework anchors the customer-facing decision-authority structure (CCO function as the named gate-decision-holder for many customer-impact decisions).
- **Equal Credit Opportunity Act (ECOA) and Reg B (12 CFR Part 1002)**. ECOA's anti-discrimination requirements and Reg B's adverse-action notice and second-review provisions. §1002.6 (rules concerning evaluation of applications) and §1002.9 (notifications) are the primary anchors for fair-lending second-review gates.
- **Truth in Lending Act (TILA) and Reg Z (12 CFR Part 1026)**. Disclosure requirements and ability-to-repay determinations for covered loans; named gates on disclosure-review and ability-to-repay decisions.
- **Real Estate Settlement Procedures Act (RESPA) and Reg X (12 CFR Part 1024)**. Loan-servicing customer-impact decisions including loss-mitigation and default management.
- **FINRA Rule 2111 — Suitability** and **Regulation Best Interest (17 CFR §240.15l-1)**. Broker-dealer customer-impact framework; named gates on customer-suitability assessment and Reg BI compliance.
- **NYDFS Section 200 fair access regulations and other state DFS conduct rules** (varies). State-specific conduct rules layered onto federal expectations.
- **NAIC Unfair Trade Practices Act and state DOI claims-handling regulations**. Insurance-claims and sales conduct framework; gates on claims-decision review and policyholder-complaint escalation.
- **CFPB Circulars** (when issued). Specific interpretive circulars frame named-conduct gates; firms typically refresh gate matrices in response to material circulars (e.g., Circular 2022-03 on adverse action notice provisions for AI-driven credit decisions).

#### What the overlay adds to the matrix

##### Decision authority — CCO function

For consumer-finance firms anchored on the CFPB's CMS framework, the Chief Compliance Officer (or equivalent role under the CMS structure) is the named decision-authority for customer-impact gates. The matrix's decision-authority block names:
- The CCO as the operational decision-holder for product approval, fee-change approval, marketing approval, and restitution-decision gates.
- The compliance committee or consumer compliance committee as the standing committee body where named gates fire.
- The board (typically through a board compliance committee, audit committee, or consumer-products committee where the firm has one) as the oversight body for material customer-impact gate decisions.

For broker-dealers, the named decision-authority shifts to the supervisory principal under FINRA Rule 3110 plus the CCO under SEC Rule 206(4)-7 (for dual-registrants). For insurers, the decision-authority shifts to the named claims-handling officer (per state DOI requirements) and the named market-conduct officer.

##### Product-approval gate

A product-approval gate for a consumer financial product names:
- **Trigger**: introduction of a new product, material change to an existing product, or extension of a product to a new customer segment or geography.
- **Required reviewers**: business sponsor (line 1), CCO (line 2), CRO (line 2), General Counsel, fair-lending officer, BSA Officer (when AML-relevant), CISO (when cyber-relevant), and (for sponsor-bank arrangements) the partner-fintech lead.
- **Decision criteria**: UDAAP risk assessment (substantial injury, reasonable avoidability, countervailing benefits); fair-lending impact assessment under ECOA; disclosure adequacy under TILA / RESPA; suitability framework under Rule 2111 / Reg BI for broker-dealer products; complaint-handling readiness; restitution-readiness for likely-error scenarios.
- **Stop conditions**: no go-live if the UDAAP risk assessment surfaces unmitigated risks; no go-live if the fair-lending impact analysis is incomplete; no go-live if disclosures are not finalized and reviewed by counsel; no go-live for AI-driven decisions if the adverse-action-notice framework is not validated against Reg B §1002.9 and Comment 9(b)(2)-3 of the Official Staff Commentary.
- **Documentation requirement**: product approval memorandum, UDAAP risk assessment, fair-lending impact analysis, disclosure review record, suitability/Reg BI documentation (where applicable), CCO sign-off log.

##### Fee-change and marketing-change gates

Fee-change approval gates and marketing-change approval gates carry the same scaffolding as product approval but at lighter weight, with the CCO function as the named decision-holder. The decision criteria typically address: UDAAP risk on the change, customer-disclosure adequacy, fair-lending impact (where the change affects customer segments differently), and consumer-complaint-handling readiness. Stop conditions address: material UDAAP risk; missing disclosures; potential disparate impact under ECOA without supporting analysis.

##### Fair-lending second-review gate

For credit decisions, ECOA and Reg B frame the second-review-of-adverse-action expectation. Some firms run a structured second-review program where adverse-action decisions on protected-class applicants flow through a second reviewer before final decision; the gate is named, the second reviewer is independent of the original decision, and the documentation requirement names the second-review log. Reg B §1002.9 and Comment 9(b)(2)-3 of the Official Staff Commentary (for AI-driven credit decisions) require that adverse-action notices be specific and accurate; the gate's decision criteria address notice-quality independent of the second-review-of-decision question.

##### Restitution-decision gate

Where a consumer-impact issue surfaces (compliance-testing exception, complaint-pattern, regulatory finding), the restitution-decision is itself a gate. The matrix names: the trigger (issue confirmed with customer-population scope); the required reviewers (CCO, General Counsel, finance, business sponsor, board committee for material restitutions); the decision criteria (population scope, harm calculation, restitution methodology, communications-and-disbursement plan); the stop conditions (no execution if population scope is unsupported; no execution if methodology has not been reviewed by an independent reviewer); the documentation requirement (restitution memorandum, board approval where material, third-party-administrator scope-of-work where applicable).

##### Complaint-pattern escalation gate

Consumer complaints, in the aggregate, are a leading indicator of customer-impact issues. The CMS framework expects firms to monitor complaint patterns and escalate material patterns to compliance or risk committees. The matrix names the complaint-pattern escalation gate: the trigger (complaint-volume threshold, root-cause-pattern threshold, regulator-inquiry trigger); the required reviewers (CCO, head of complaints function, business owner of the affected product); the decision criteria (whether the pattern reflects a substantive issue, requires product or process change, requires restitution analysis); the documentation requirement (escalation memorandum, complaint-pattern analysis, root-cause analysis).

##### Insurance claims-handling gate

For insurers, state DOI claims-handling regulations frame named gates on disputed-claim escalation, claim-denial review, and material-loss-reserve-change decisions. The decision authority typically routes through the chief claims officer with claims committee oversight; the documentation requirement names the claim file and the claims committee minutes.

#### Common patterns

- **Marketing approval treated as creative-review only**. Marketing approval often runs through marketing and legal but skips the CCO function. For consumer financial products, the CFPB treats marketing as a UDAAP risk surface; the matrix elevates marketing approval to a CCO-named gate.
- **Fair-lending second-review delegated to underwriting**. The second-review on adverse-action decisions is sometimes delegated within the underwriting function; this fails the independence test under ECOA second-review framing. The matrix flags the conflict and recommends an independent second-reviewer slot.
- **Restitution treated as operational reconciliation**. Restitution decisions sometimes run through finance and operations without committee oversight; the matrix elevates material restitutions to a board-committee-adopted decision with the methodology and population-scope independently reviewed.
- **Reg BI and FINRA suitability treated as separate gates with conflicting criteria**. For dual-registrant firms, Reg BI and FINRA Rule 2111 set parallel customer-impact frameworks with overlapping but distinct criteria. The matrix harmonizes the two with named decision criteria that satisfy both.
- **CFPB circular gap**. Firms sometimes delay refreshing gate criteria in response to material CFPB circulars; the matrix's gap section flags the unaddressed circulars and recommends specific gate-criteria updates.

#### Anchors used by this overlay

- CFPB Supervision and Examination Manual — UDAAP module. https://www.consumerfinance.gov/compliance/supervision-examinations/
- CFPB Supervision and Examination Manual — Compliance Management System module. https://www.consumerfinance.gov/compliance/supervision-examinations/
- 15 USC §1691 et seq. — Equal Credit Opportunity Act. https://www.consumerfinance.gov/rules-policy/regulations/1002/
- 12 CFR Part 1002 — Reg B (ECOA implementing regulation), §1002.6 evaluation of applications, §1002.9 notifications. https://www.ecfr.gov/current/title-12/chapter-X/part-1002
- 12 CFR Part 1026 — Reg Z (TILA implementing regulation). https://www.ecfr.gov/current/title-12/chapter-X/part-1026
- 12 CFR Part 1024 — Reg X (RESPA implementing regulation). https://www.ecfr.gov/current/title-12/chapter-X/part-1024
- FINRA Rule 2111 — Suitability. https://www.finra.org/rules-guidance/rulebooks/finra-rules/2111
- 17 CFR §240.15l-1 — Regulation Best Interest. https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.15l-1
- CFPB Circular 2022-03 — Adverse Action Notification Requirements in Connection with Credit Decisions Based on Complex Algorithms. **Withdrawn May 12, 2025; historical only.** Reg B §1002.9 and Comment 9(b)(2)-3 of the Official Staff Commentary continue to apply on their own terms. https://www.consumerfinance.gov/compliance/circulars/circular-2022-03/
- NAIC Unfair Trade Practices Act (MDL-880) and state DOI claims-handling regulations. https://content.naic.org/sites/default/files/MO880.pdf
- State market-conduct regulations — vary by state; firm-overlay names the state-specific rules that apply.

## cyber

### Cyber cross-cutting overlay — human-review-gates

Loads when the scope `cross_cutting_overlay_set` includes `cyber`. The overlay shapes the gate matrix when gates cover incident-response decisions, materiality determinations for cyber events, cyber-disclosure decisions, and cyber-third-party arrangements.

#### Why cyber belongs in many gate matrices

Cyber gates are rarely standalone; they layer onto substantive gates (vendor onboarding includes a cyber-due-diligence sub-gate; product launch includes a security-architecture-review sub-gate; incident response includes a materiality-determination gate that feeds the disclosure decision). Where the underlying gate touches information-security controls, customer-data exposure, or third-party-provided technology, the cyber overlay adds named criteria, specific independence requirements, and the documentation discipline a CISO function and an examiner will recognise.

#### Source basis

- **NYDFS 23 NYCRR Part 500 — Cybersecurity Requirements for Financial Services Companies**. November 2023 amendment introduced new tiering (Class A companies, covered entities, small businesses) and tighter incident-notice requirements. §500.4 (cybersecurity governance — senior governing body responsibility; CISO reporting to senior governing body; CISO annual report) is the primary anchor for cyber-gate decision authority. §500.17 (notice of cybersecurity event; 72-hour reporting to NYDFS) anchors the incident-notice readiness gate.
- **SEC Cybersecurity Rules (effective December 2023)**. Form 8-K Item 1.05 (material cybersecurity incident disclosure within 4 business days of materiality determination); 17 CFR §229.106 (Reg S-K Item 106 cybersecurity risk management, strategy, and governance — annual disclosure for public registrants). The materiality-determination gate is a named gate at public-registrant firms; the disclosure-committee or its equivalent is the named decision authority.
- **FFIEC IT Examination Handbook**. The Information Security booklet (governance, logical security, change management) and the Audit booklet (IT-audit reportable conditions). The Information Security booklet's governance section (§II.A) frames the senior-management oversight expectation that flows into cyber-gate decision authority.
- **Reg S-P (17 CFR §248.30)**. Customer-information safeguards for SEC-registered entities. The 2024 amendment introduced incident-response and customer-notification requirements with named timelines.
- **GLBA Safeguards Rule (16 CFR Part 314)**. FTC version with functional-regulator equivalents for banks. The Safeguards Rule names the qualified individual (a designated information-security program lead) as a regulatory expectation that informs cyber-gate decision authority.
- **NIST Cybersecurity Framework 2.0 (February 2024)**. Used as a control taxonomy and as a governance scaffolding; the Govern function (introduced in CSF 2.0) overlaps directly with gate-architecture concerns and provides language for governance-gate criteria.
- **CISA cross-sector cybersecurity performance goals (CPGs)**. Voluntary baseline; sometimes referenced in supervisor expectations for critical-infrastructure-tagged entities.

#### What the overlay adds to the matrix

##### Decision authority — CISO and disclosure-committee gates

For NYDFS-covered entities, NYDFS §500.4 names the senior governing body and the CISO as the decision-authority backbone for cyber-program decisions. The matrix's decision-authority block names:
- The senior governing body (board of directors or equivalent) as the ultimate adopting body for cyber-program changes; the annual CISO report under §500.4(b) is a named annual gate.
- The CISO (or qualified equivalent) as the operational decision-holder for cyber-gate decisions, with reporting-line independence preserved (CISO reports to senior governing body, not to a CIO or COO that owns the IT function being reviewed).

For SEC public registrants, the disclosure committee (or equivalent body that reviews 8-K filings) is the named decision-authority for the materiality-determination gate. The named members typically include the General Counsel, the CFO, the CISO, the Chief Compliance Officer, and an independent disclosure adviser. The gate documentation requirement names the disclosure-committee minute and the materiality-determination memorandum.

##### Materiality-determination gate (SEC public registrants)

The Form 8-K Item 1.05 disclosure obligation is triggered by a materiality determination, not by the incident itself. The gate matrix elevates the materiality-determination decision to a named gate with:
- **Trigger**: detection of a cybersecurity incident with potential material impact, escalated by the CISO function within a stated internal timeline.
- **Required reviewers**: disclosure committee membership; the CISO presents the technical facts, the General Counsel and CCO present the disclosure analysis, the CFO presents the financial impact, the disclosure committee renders the decision.
- **Decision criteria**: SEC materiality standard (whether a reasonable investor would consider the incident important to an investment decision), with the SEC's published interpretive guidance (the December 2023 Compliance & Disclosure Interpretations on Item 1.05) as the source anchor.
- **Stop conditions**: no go on filing if the materiality determination is not supported by the incident facts; no delay past 4 business days from materiality determination unless the Attorney General has notified that disclosure poses a substantial risk to national security or public safety (the §1.05 carve-out).
- **Documentation requirement**: the materiality-determination memorandum, the disclosure committee minutes, the legal analysis, the technical timeline, and the filing record.

##### Incident-notice readiness gate

Incident-notice readiness is a control, not an event. The matrix carries an incident-notice readiness gate (typically annual or after each material exercise) with criteria sourced from NYDFS §500.17, Reg S-P amended customer-notification timing, SEC 8-K Item 1.05, GLBA Safeguards Rule customer-notification provisions, and state breach-notification statutes (which vary by state). The decision criteria address: documented materiality-determination workflow with named approver; notification template library covering each applicable jurisdiction and regulator; tabletop exercise evidence with named participants and lessons-learned tracking; dispatch-path readiness across regulator portals, customer-channels, and counterparty channels.

##### Third-party cyber gates

Where the gate is a vendor-onboarding or vendor-monitoring gate at a NYDFS-covered entity, NYDFS §500.11 (third-party service-provider security policy) layers onto the substantive interagency-TPRM-anchored gate. The matrix carries cyber-specific decision criteria (vendor cybersecurity assessment, vendor's incident-notification commitment, vendor's encryption commitments under §500.15, vendor's MFA commitments under §500.12) and the CISO concurrence as a required reviewer on critical-vendor gates touching customer data or privileged-system access.

##### CISO independence

For NYDFS-covered entities and for firms anchored on the GLBA Safeguards Rule's qualified-individual concept, the matrix flags CISO reporting-line independence. The CISO that reports to a CIO that owns the IT function being reviewed has structural conflict; NYDFS §500.4 explicitly addresses this by naming the senior governing body as the CISO's reporting destination. The matrix's `independence_basis` for CISO-anchored gates cites §500.4 and (for non-NYDFS firms) the firm's own policy or the GLBA Safeguards Rule.

##### CSF 2.0 Govern function as scaffolding

For firms that anchor on NIST CSF 2.0, the Govern function categories (GV.OC organizational context, GV.RM risk management strategy, GV.RR roles, responsibilities, and authorities, GV.PO policy, GV.OV oversight, GV.SC cybersecurity supply chain risk management) provide gate-architecture scaffolding. Each Govern category maps to one or more gates in the matrix; the source anchor cites the specific CSF 2.0 subcategory.

#### Common patterns

- **Materiality determination buried in the incident-response runbook**. Many firms have an incident-response runbook that names a materiality-determination step but does not elevate it to a board- or disclosure-committee gate. For SEC public registrants, this is a gap; the matrix's gap section flags it and recommends a named disclosure-committee gate.
- **CISO reports to CIO; CIO sits on cyber gates**. Reporting-line conflict is common in firms that have not refreshed governance to NYDFS §500.4. The matrix flags the conflict and recommends a CISO reporting-line refresh as part of the gate-architecture refresh.
- **Vendor cyber gate without CISO concurrence**. A critical-vendor onboarding gate that does not include the CISO function as a required reviewer on cyber-relevant arrangements misses the §500.11 anchor and the SEC Reg S-P safeguards-rule anchor. The matrix flags this.
- **Annual CISO report treated as a one-pager**. NYDFS §500.4(b) requires the CISO's annual report to the senior governing body to address material cybersecurity risks, the firm's cybersecurity program, and material cybersecurity events. Some firms produce a one-pager; the matrix elevates the annual CISO report to a named gate with substantive content criteria.

#### Anchors used by this overlay

- 23 NYCRR Part 500 — NYDFS Cybersecurity Requirements (post-November 2023 amendment).
  - §500.4 (cybersecurity governance — senior governing body, CISO, CISO annual report)
  - §500.11 (third-party service-provider security policy)
  - §500.12 (multi-factor authentication)
  - §500.15 (encryption of nonpublic information)
  - §500.16 (incident response and business continuity)
  - §500.17 (notice of cybersecurity event; 72-hour reporting)
  https://www.dfs.ny.gov/industry_guidance/cybersecurity
- FFIEC IT Examination Handbook, Information Security booklet (September 2016). §II.A governance. https://ithandbook.ffiec.gov/it-booklets/information-security/
- 17 CFR §229.106 — SEC Reg S-K Item 106 (cybersecurity disclosure). https://www.ecfr.gov/current/title-17/chapter-II/part-229/section-229.106
- Form 8-K Item 1.05 — material cybersecurity incident disclosure (effective December 2023). https://www.sec.gov/files/form-8-k.pdf
- SEC Compliance & Disclosure Interpretations — Item 1.05 (December 2023). https://www.sec.gov/divisions/corpfin/guidance/exchange-act-form-8-k.htm
- 17 CFR §248.30 — Reg S-P (Safeguards Rule and 2024-amendment incident-response and notification). https://www.ecfr.gov/current/title-17/chapter-II/part-248/subpart-A/section-248.30
- 16 CFR Part 314 — FTC Safeguards Rule. https://www.ftc.gov/legal-library/browse/rules/safeguards-rule
- NIST Cybersecurity Framework 2.0 — Govern function (February 2024). https://www.nist.gov/cyberframework
- CISA Cross-Sector Cybersecurity Performance Goals. https://www.cisa.gov/cross-sector-cybersecurity-performance-goals
- State breach-notification statutes — vary by state; firm-overlay names the statutes that apply to the institution's jurisdictional footprint.
