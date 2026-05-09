# Source anchors: adverse-action-review

Cited regulatory sources this skill anchors to. Every primary anchor names the source, the section reference (or `[verify section]` flag), a one-paragraph excerpt or paraphrase of the relevant content, and the link.

The skill cites these by file path. SKILL.md does not restate excerpts.

## Primary anchors

### 1. Equal Credit Opportunity Act (ECOA) — 15 U.S.C. §1691

- Citation: Equal Credit Opportunity Act, 15 U.S.C. §1691; §1691(d) (notification of action taken on credit applications and statement of specific reasons).
- Excerpt-paraphrase: Each applicant against whom adverse action is taken is entitled to a statement of reasons for such action from the creditor. The statement either gives specific reasons for the adverse action, or discloses the applicant's right to a statement of specific reasons within thirty days after receipt of a request made within sixty days of the notification.
- Link: https://www.ecfr.gov/current/title-15/chapter-41/subchapter-IV/section-1691 — §1691(d) statement-of-reasons requirement.
- Notes: ECOA is the statutory anchor; Regulation B (12 CFR Part 1002) carries the operational detail consumed by this skill.

### 2. Regulation B — 12 CFR §1002.2(c) (definition of adverse action)

- Citation: Regulation B, 12 CFR §1002.2(c) (CFPB-administered): definition of "adverse action" including denial, termination, change in terms unfavorable to the applicant, refusal to grant credit on substantially the terms applied for, and refusal to increase an existing line on a request.
- Excerpt-paraphrase: Adverse action means a refusal to grant credit in substantially the amount or on substantially the terms requested in an application unless the creditor makes a counteroffer (to grant credit in a different amount or on other terms) and the applicant uses or expressly accepts the credit offered; a termination of an account or an unfavorable change in the terms of an account that does not affect all or substantially all of a class of the creditor's accounts; and a refusal to increase the amount of credit available to an applicant who has made an application for an increase. The definition reaches counteroffers not accepted, terms-less-favorable actions, and existing-account adverse changes — not only outright denials.
- Link: https://www.ecfr.gov/current/title-12/chapter-X/part-1002/section-1002.2 — §1002.2(c) definition.
- Notes: The scope of the notice population reviewed by this skill is set by §1002.2(c); a review that covers only outright denials misses counteroffers-not-accepted and terms-less-favorable populations that are also adverse action.

### 3. Regulation B — 12 CFR §1002.9 (notifications)

- Citation: Regulation B, 12 CFR §1002.9 (notification of action taken). Subsections cited by this skill: §1002.9(a)(1) (timing — 30 days after receiving completed application or after taking adverse action on incomplete application or counteroffer not accepted; 90 days for incomplete-application alternative under §1002.9(c)); §1002.9(a)(2) (statement of specific reasons or disclosure of right to request); §1002.9(b)(2) (form of ECOA notice content); §1002.9(c) (incomplete applications).
- Excerpt-paraphrase: A creditor must notify an applicant of action taken within 30 days after receiving a completed application; within 30 days after taking adverse action on an incomplete application unless notice of incompleteness was provided; within 30 days after taking adverse action on an existing account; or within 90 days after notifying the applicant of a counteroffer if the applicant does not accept it. The notice must contain a statement of the specific reasons for the action taken or disclose the applicant's right to a statement of specific reasons. The Official Staff Commentary to §1002.9 sets the specificity standard, including that a statement that the applicant failed to achieve a qualifying score on the creditor's credit-scoring system is not specific enough; the principal reason or reasons that contributed to the score must be disclosed.
- Link: https://www.ecfr.gov/current/title-12/chapter-X/part-1002/section-1002.9 — §1002.9(a)(1) timing, §1002.9(a)(2) reasons, §1002.9(b)(2) form, §1002.9(c) incomplete.
- Notes: Operative anchor for the per-notice timing-compliance and content-compliance fields. The Staff Commentary on specificity is the bridge to the CFPB Circulars on AI / complex models.

### 4. Official Staff Commentary to Regulation B §1002.9

- Citation: Official Interpretations to 12 CFR Part 1002, Comment 9(b)(2)-3 (specificity of reasons), Comment 9(b)(2)-4 (number of specific reasons), Comment 9(b)(2)-5 (source of specific reasons), and related comments addressing form and content of the §1002.9 notice.
- Excerpt-paraphrase: The specific reasons disclosed must relate to and accurately describe the factors actually considered or scored by a creditor. A creditor need not describe how or why a factor adversely affected an applicant. Disclosure of more than four reasons is not likely to be helpful to the applicant. Generic statements such as "you did not meet our credit standards" are not sufficient to satisfy the specificity requirement; "credit application incomplete" is permissible only when accurate.
- Link: https://www.consumerfinance.gov/rules-policy/regulations/1002/Interp-9/ — Comments to §1002.9.
- Notes: Operative anchor for the specificity standard against which cited reasons are tested in the per-notice content-compliance field.

### 5. CFPB Circular 2022-03 — Adverse action with complex algorithms

- Citation: CFPB Circular 2022-03 (May 26, 2022), "Adverse action notification requirements in connection with credit decisions based on complex algorithms".
- Excerpt-paraphrase: Creditors using complex algorithms, including algorithms that use what are sometimes referred to as artificial intelligence or machine learning, are not absolved from their obligation to provide a statement of specific reasons under ECOA and Regulation B. The complexity of the model is not a defense to the specificity requirement; if a creditor cannot accurately identify the principal reasons relied on, the creditor cannot meet the requirement and may be in violation of ECOA.
- Link: https://www.consumerfinance.gov/compliance/circulars/circular-2022-03-adverse-action-notification-requirements-in-connection-with-credit-decisions-based-on-complex-algorithms/ — Circular sections "Question Presented" and "Response".
- Notes: Operative anchor for the model-supported-reasons review. A creditor that cannot produce per-decision feature contribution evidence cannot demonstrate compliance with §1002.9(a)(2) on a complex-algorithm decision; this skill's per-decision `reasons_model_supported[]` field operationalizes the test.

### 6. CFPB Circular 2023-03 — Sample reason codes and AI / complex models

- Citation: CFPB Circular 2023-03 (September 19, 2023), "Adverse action notification requirements and the proper use of the CFPB's sample forms provided in Regulation B".
- Excerpt-paraphrase: Creditors must provide accurate and specific reasons for adverse action. Creditors cannot rely on the checklist of reasons in CFPB sample forms (Appendix C to Regulation B) when those sample reasons do not reflect the principal reasons that actually contributed to the adverse action. The accuracy obligation reaches creditors using complex models (AI / ML); a creditor whose model relied principally on factors not present on the sample form must disclose those factors specifically, not select the closest sample-form proxy.
- Link: https://www.consumerfinance.gov/compliance/circulars/circular-2023-03-adverse-action-notification-requirements-and-the-proper-use-of-the-cfpbs-sample-forms-provided-in-regulation-b/ — Circular section "Required Information" [verify section title].
- Notes: Operative anchor for the reason-mapping-accuracy review. Skills that find a notice citing sample-form reasons that do not match the model's principal feature contributions flag this circular as the controlling guidance.

### 7. Joint Statement on Enforcement of Civil Rights, Fair Lending, Fair Housing, and Consumer Financial Protection Laws (April 2023)

- Citation: Joint Statement issued April 25, 2023 by the Consumer Financial Protection Bureau, the Civil Rights Division of the Department of Justice, the Federal Trade Commission, and the Equal Employment Opportunity Commission, "Joint Statement on Enforcement Efforts Against Discrimination and Bias in Automated Systems".
- Excerpt-paraphrase: The four agencies confirm that existing legal authorities apply to the use of automated systems and innovative new technologies, including in the consumer financial-services context. Discrimination and bias in automated systems are enforceable under the agencies' existing statutes; novel technology is not a defense to ECOA, FHA, FCRA, the FTC Act §5, or Title VII obligations.
- Link: https://www.consumerfinance.gov/about-us/newsroom/cfpb-federal-partners-confirm-automated-systems-advanced-technology-not-an-excuse-for-lawbreaking-behavior/ — Joint Statement text, signatories section.
- Notes: Cross-anchored on every adverse-action review where any in-scope decision involves an AI / ML model; sets the framing for the AI / complex-model findings section of the artifact.

### 8. Fair Housing Act — 42 U.S.C. §3605

- Citation: Fair Housing Act, 42 U.S.C. §3605 (discrimination in residential real estate-related transactions); 42 U.S.C. §3604 (discrimination in the sale or rental of housing and other prohibited practices).
- Excerpt-paraphrase: It is unlawful for any person or other entity whose business includes engaging in residential real estate-related transactions to discriminate against any person in making available such a transaction, or in the terms or conditions of such a transaction, because of race, color, religion, sex, handicap, familial status, or national origin. Residential real estate-related transactions include the making or purchasing of loans or providing other financial assistance secured by residential real estate.
- Link: https://www.law.cornell.edu/uscode/text/42/chapter-45/subchapter-I — §3605 residential real estate transactions.
- Notes: Reaches dwelling-secured credit (mortgage, HELOC, home-improvement); the disparate-impact red-flag panel cites FHA on the dwelling-secured perimeter alongside ECOA.

### 9. Fair Credit Reporting Act — 15 U.S.C. §1681m and Regulation V — 12 CFR §1022.74

- Citation: Fair Credit Reporting Act, 15 U.S.C. §1681m (requirements on users of consumer reports); Regulation V, 12 CFR §1022.74 (content, form, and timing of risk-based pricing notices and credit-score disclosure exception notices).
- Excerpt-paraphrase: Where a creditor takes adverse action based in whole or in part on information contained in a consumer report, the creditor must provide a notice including the name, address, and telephone number of the consumer reporting agency, a statement that the agency did not make the decision and cannot explain why it was made, and a statement of the consumer's right to obtain a free copy of the report and to dispute its accuracy. Where a credit score was used in taking adverse action, the creditor must include the score, range, and key factors as set out in §1022.74 and 15 U.S.C. §1681g(f).
- Link: https://www.ecfr.gov/current/title-12/chapter-X/part-1022/section-1022.74 — §1022.74 risk-based pricing and credit-score disclosure content.
- Notes: Anchors the per-decision `fcra_overlay_applied` flag. Reg B notice content does not satisfy FCRA risk-score disclosure where a score was used; the two regimes operate in parallel and the notice review checks both where applicable.

### 10. Regulation B — Appendix C to Part 1002 (sample notification forms)

- Citation: Regulation B, Appendix C to 12 CFR Part 1002 — Sample Notification Forms (Forms C-1 through C-9 and the related sample reason-code list).
- Excerpt-paraphrase: Appendix C provides sample notification forms that, when completed accurately and used in the contexts described, are deemed to comply with §1002.9 notification content requirements. The sample reason-code list (e.g., "Income insufficient for amount of credit requested", "Length of employment", "Insufficient credit references") is not the universe of permissible reasons; creditors using the sample forms must still disclose the principal reasons actually relied upon, including reasons not on the sample list.
- Link: https://www.ecfr.gov/current/title-12/chapter-X/part-1002/appendix-Appendix%20C%20to%20Part%201002 — Appendix C to 12 CFR Part 1002, sample forms C-1 through C-9.
- Notes: The CFPB Circular 2023-03 anchor refines the use of these sample forms; creditors selecting the closest sample reason instead of the principal reason actually relied upon do not satisfy §1002.9(a)(2).

## Secondary anchors (sector and cross-cutting)

### 11. Joint OCC, FRB, and FDIC Interagency Guidance on Third-Party Relationships (June 2023)

- Citation: OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023, "Interagency Guidance on Third-Party Relationships: Risk Management" (issued June 6, 2023).
- Excerpt-paraphrase: The interagency guidance sets risk-management expectations for banking organizations engaging third parties, including fintech and AI vendors. Where adverse action decisions or notice generation is performed by a third-party model or vendor service, the bank retains accountability for ECOA / Regulation B compliance; sponsor-bank fair-lending duty allocates per the program agreement and the bank's own fair-lending program.
- Link: https://www.occ.gov/news-issuances/bulletins/2023/bulletin-2023-17.html — Bulletin 2023-17.
- Notes: Payments-fintech sector overlay anchor; relevant where the adverse-action notice or model is vendor-supplied.

### 12. CFPB BNPL Interpretive Rule (May 2024)

- Citation: CFPB Interpretive Rule, "Use of Digital User Accounts to Access Buy Now, Pay Later Loans" (89 Fed. Reg. 47068; May 31, 2024) [verify Federal Register citation].
- Excerpt-paraphrase: The bureau interprets BNPL lenders that issue digital user accounts to access credit as card issuers under Regulation Z; the interpretive rule clarifies application of Regulation Z requirements to BNPL products. Regulation B and ECOA continue to apply to BNPL credit decisions independently of Regulation Z; adverse action notices on BNPL declines remain subject to §1002.9.
- Link: https://www.consumerfinance.gov/rules-policy/final-rules/truth-in-lending-regulation-z-use-of-digital-user-accounts-to-access-buy-now-pay-later-loans/ — Interpretive Rule [verify section].
- Notes: Payments-fintech sector overlay anchor; clarifies that BNPL adverse action falls under Reg B even where Reg Z applicability has been the contested question.

### 13. SR 11-7 — Guidance on Model Risk Management

- Citation: Federal Reserve SR 11-7 / OCC Bulletin 2011-12, "Guidance on Model Risk Management" (April 4, 2011), §V (Model Documentation) and §VI (Third-Party Models). OCC Bulletin 2026-13 refreshes the model risk framework for traditional models but does not extend it to generative AI, retrieval-augmented generation, tool use, or agentic AI.
- Excerpt-paraphrase: SR 11-7 sets supervisory expectations for model risk management at federally regulated banks; documentation, validation, and explainability expectations are the structural anchor for any model that drives adverse-action decisions. Where the model is AI / ML, the model-card, validation-plan, and adverse-action-reason-generation evidence form a single governance fabric. For GenAI / RAG / tool-use / agentic-AI scope, anchor to NIST AI RMF (1.0, January 2023), NIST AI 600-1 (Generative AI Profile, July 2024), and the EU AI Act (Regulation (EU) 2024/1689) where extraterritorial reach applies.
- Link: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm — §V documentation, §VI third-party.
- Notes: Banking sector overlay anchor; relevant where the adverse-action review consumes model documentation produced under the bank's MRM program. The 2026-13 carrying-forward language earlier in this file overstated reach and has been corrected.

### 14. GLBA Safeguards Rule — 16 CFR Part 314

- Citation: Gramm-Leach-Bliley Act Safeguards Rule, 16 CFR Part 314 (FTC; financial institutions not under primary federal banking regulator supervision); 12 CFR Part 30 Appendix B (OCC parallel for national banks); 12 CFR Part 364 Appendix B (FDIC parallel for state nonmember banks).
- Excerpt-paraphrase: Financial institutions must maintain a written information security program with administrative, technical, and physical safeguards for non-public personal information. Customer applicant data, model feature inputs, and BISG inputs used in adverse-action analytics fall within the program's scope; access, transfer, and disposal of this data is governed accordingly.
- Link: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314 — 16 CFR Part 314.
- Notes: Privacy cross-cutting overlay anchor; sets the data-handling expectations for the adverse-action review workflow itself, not for the underwriting decision.

### 15. Regulation T — 12 CFR Part 220 (margin lending; capital-markets boundary)

- Citation: Federal Reserve Regulation T, 12 CFR Part 220 (Credit by Brokers and Dealers); related FINRA Rule 4210 (Margin Requirements).
- Excerpt-paraphrase: Reg T governs the extension of credit by brokers and dealers to customers for the purpose of purchasing or carrying securities. Margin calls and forced liquidations occur under the rules of the broker-dealer's customer margin agreement; treatment as "adverse action" under ECOA is narrow and turns on whether the margin extension was a covered consumer credit transaction.
- Link: https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-220 — 12 CFR Part 220.
- Notes: Capital-markets sector overlay anchor; flags the narrow scope where securities-based lending interacts with Reg B.

### 16. NAIC Unfair Trade Practices framing (insurance scope boundary)

- Citation: NAIC Unfair Trade Practices Act (Model #880); state-DOI unfair-discrimination statutes implementing the model.
- Excerpt-paraphrase: Insurance underwriting and pricing discrimination is regulated under state-DOI unfair-discrimination statutes, not under ECOA. The vocabulary is "unfair discrimination" rather than "adverse action"; substantive tests (actuarial-justification framing) differ from ECOA effects-test framing.
- Link: https://content.naic.org/sites/default/files/MO880.pdf — Model #880, unfair-discrimination section [verify section].
- Notes: Insurance overlay anchor; flags the boundary where the skill does not extend (insurance underwriting) versus where it does extend (bank-affiliated credit-protection insurance bundled with a credit decision).

## Verification flags

The following items carry `[verify ...]` flags and must be confirmed at SKILL.md write time and at review-write time:

- CFPB Circular 2023-03 — confirm exact section title within the circular.
- CFPB BNPL Interpretive Rule — confirm Federal Register citation and operative section reference.
- OCC Bulletin 2026-13 — confirm bulletin number and date for the model-risk refresh; the bulletin scope does not include GenAI / RAG / tool use / agentic AI, which anchor to NIST AI RMF, NIST AI 600-1, and the EU AI Act.
- NAIC Model #880 — confirm current model edition and unfair-discrimination section reference.

Where verification is incomplete, the SKILL.md cites with the `[verify section]` flag carried forward; do not invent.

## Firm overlay placeholder

A firm using this skill in production overlays its policy, taxonomy, named owners, and named first-line controls (notice template version, reason-code dictionary, model release control, comparative-file-review owner) via `references/firm-overlay.md` (not committed in this repo). The firm overlay does not modify this source-anchors file. An advisory firm shipping a client-specific overlay does the same thing under a separate overlay file.
