# Banking sector overlay — regulatory-impact-assessment

When the scope flags banking and the rule under assessment touches OCC, FRB, FDIC, or NCUA-supervised entities (or state-chartered banks under shared examination authority), load this overlay alongside `references/source-anchors.md`. The overlay carries the regulator-specific scoping conventions, threshold tier semantics, named-policy and named-control patterns, and the strategy-lens posture for the federal banking agencies.

## Institution-type scoping conventions

Federal banking impact assessments turn on chartering, primary federal regulator, and tier categorisation:

- **National banks and federal savings associations** are OCC-supervised. Scope reads against OCC bulletins, the Comptroller's Handbook, and 12 CFR Parts 1 through 195 [verify subpart and section per assessment].
- **State member banks and bank holding companies (BHCs)** are FRB-supervised. Scope reads against SR letters and 12 CFR Parts 200 through 270 [verify subpart and section].
- **State non-member banks and FDIC-insured state savings associations** are FDIC-supervised. Scope reads against FILs and 12 CFR Parts 300 through 391 [verify subpart and section].
- **Federally insured credit unions** are NCUA-supervised. Scope reads against NCUA Letters to Credit Unions and 12 CFR Parts 700 through 799 [verify subpart and section].
- **Foreign banking organisations (FBOs) with US operations** are FRB-supervised at the consolidated level under the Enhanced Prudential Standards (Regulation YY, 12 CFR Part 252) [verify subpart], with the US branches' day-to-day supervision often shared with OCC or state regulators.

When the rule applies inter-agency (the June 2023 third-party-risk guidance, the heightened standards), the assessment cites all three or four agencies in the source-identification block.

## Threshold tier semantics

The assessment's threshold determination reads against the federal banking tier framework:

- **Heightened Standards**: 12 CFR Part 30 Appendix B applies to insured national banks, federal savings associations, and federal branches with average total consolidated assets of $50B or more (parallel under Part 30 Appendix D for FRB and FDIC supervised entities) [verify subsection]. The Heightened Standards drive the second-line authority, board governance, and risk-management framework expectations the assessment reads against for in-scope rule changes.
- **FRB tailoring framework**: Categories I through IV under 12 CFR Part 252 [verify section] tier capital, liquidity, stress-testing, and resolution-planning expectations by asset size and complexity. A Category I firm absorbs a rule differently from a Category III firm; the assessment cites the firm's category and the corresponding tier expectations.
- **CFPB direct supervision threshold**: $10B in total assets for depository institutions (CFPB has direct supervisory authority for $10B+ banks and for non-bank consumer-finance providers). The assessment reads CFPB-rule scope against this threshold for bank-side applicability.
- **Community banks**: Generally below $10B in total assets, with FDIC, OCC Midsize and Community Bank Supervision, or FRB community-bank supervision as primary; the assessment reads against community-bank tailoring (e.g., the FDIC's community-bank-tailored expectations on operational resilience, BSA-AML proportionality).

## Named-policy and named-control patterns

Federal banking impact assessments routinely touch the named-policy areas below; the policy-impact section typically references one or more:

- **Risk Governance Framework** under Heightened Standards Appendix B II.B [verify subsection].
- **Compliance Risk Management Programme** under OCC, FRB, FDIC supervisory guidance and the FFIEC Compliance Manual.
- **Third-Party Risk Management Policy** anchored on the June 2023 interagency guidance.
- **Information Security Programme** anchored on the GLBA Safeguards Rule, 12 CFR Part 30 Appendix B (security guidelines), and the FFIEC IT Examination Handbook.
- **Model Risk Management Policy** anchored on the joint interagency Revised Guidance on Model Risk Management (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026), which superseded SR 11-7 / OCC Bulletin 2011-12 (April 4, 2011) and SR 21-8 (April 9, 2021). GenAI and agentic AI are explicitly out of scope of the joint guidance; AI scope for those models routes to NIST AI RMF / NIST AI 600-1 / EU AI Act.
- **BSA-AML Programme** anchored on the FFIEC BSA/AML Examination Manual, 31 CFR Chapter X, and the AMLA 2020 implementation rules.
- **Fair-Lending Programme** anchored on Reg B (12 CFR Part 1002), Reg C (12 CFR Part 1003), and the FFIEC Interagency Fair Lending Examination Procedures.
- **Operational Resilience Programme** anchored on the FFIEC Business Continuity Management booklet and the FRB / OCC / FDIC operational-resilience papers (Sound Practices to Strengthen Operational Resilience; the 2020 paper) [verify publication date].
- **Capital Adequacy Process and ICAAP** anchored on 12 CFR Part 217 (FRB) and parallel OCC / FDIC subparts [verify subpart] for Category I-IV firms.
- **CCAR / DFAST stress-testing programme** for Category I-IV firms [verify regulation citation].
- **Recovery and Resolution Plans** for Category I-II firms under 12 CFR Parts 243, 381 [verify section].

The assessment's policy-impact section names the policy area, the expected change type, and the rationale; the skill does not draft policy language.

## Reporting-impact patterns

Federal banking reporting touches:

- **Call Report (FFIEC 031, 041, 051)** schedules. Rule changes affecting balance-sheet classification, loan-segment reporting, fair-value reporting, or liquidity reporting drive Call Report schedule changes.
- **FR Y-9C, FR Y-9LP, FR Y-14A/Q/M** for BHCs. Tier-specific reporting expectations [verify form numbers].
- **HMDA LAR (Reg C)** for institutions meeting the HMDA threshold. https://www.consumerfinance.gov/data-research/hmda/ .
- **CRA Performance Evaluations** under 12 CFR Part 25 / 228 / 345 [verify subpart] and the 2023 interagency CRA modernisation final rule [verify implementation date and section].
- **CFPB 1071 Small Business Lending Register** under 12 CFR 1002.107 [verify subsection], phased by origination tier.
- **Suspicious Activity Reports (SAR)** and Currency Transaction Reports (CTR) under 31 CFR 1010, 1020 [verify subsection].

## Strategy-lens posture for federal banking

The federal banking strategy lens has identifiable patterns:

- **Industry-association alignment**: BPI for large banks; ABA for the broader bank trade-association posture; ICBA for community banks; NAFCU for credit unions. The assessment names which association(s) the firm is engaged with on the rule.
- **Comment-letter convention**: Bank comment letters typically run through the BPI or ABA committee structure first, then the firm signs as a member or files its own. Coordination with the trade-association draft is standard; firm-direct comment letters are reserved for items where the firm's posture diverges from industry consensus or where the firm wants to make a specific record.
- **Supervisor meeting convention**: Federal banking agencies hold pre-comment meetings with supervised institutions on significant rulemakings. The CRO chief of staff or head of regulatory affairs runs the meeting; counsel attends; the head of the business affected provides the substantive read.
- **Examiner-posture-shift signal**: Speeches by the OCC Comptroller, FRB Chair or Vice Chair for Supervision, FDIC Chair, and the Director of the CFPB are read for examiner-posture signal; the assessment cites the specific speech URL and date when the signal is the trigger for the impact read.
- **Escalation triggers**: For federally supervised banks, a high-impact rule (cost-to-comply over $50M, multi-policy refresh, multi-control-objective change, board-reporting expectation) typically escalates to the board risk committee for the regulatory-strategy posture. A Heightened-Standards firm carries an additional gate: the chief risk officer's independent risk management view feeds the board's read.

## Cost-to-comply patterns

Federal banking cost-to-comply reads typically calibrate against:

- **OMB Circular A-4 RIAs** published in the federal banking agencies' adopting releases for significant rules (the "Effects of the Rule" section).
- **Peer-firm benchmark**: where peer-firm cost reads are available through trade-association working groups or public disclosures, the firm calibrates against them.
- **Vendor-quote ranges**: for technology and vendor remediation costs, the assessment uses indicative vendor-quote ranges as the basis.
- **Prior-project benchmarks**: the firm's prior-project cost-to-comply reads (e.g., the firm's CECL implementation cost as a benchmark for a new accounting-rule impact) feed indicative ranges.

Agency cost estimates routinely diverge from firm-side reads. The assessment names the divergence and the basis; the federal banking strategy lens often picks up that divergence as a comment-letter input.

## When to escalate beyond regulatory-change-committee

For federal banking, the escalation triggers below typically fire:

- **CRO**: any rule with a Heightened-Standards Risk Governance Framework implication; any rule introducing a new annual board-attestation expectation.
- **General counsel**: any rule with a litigation-posture implication (judicial review pending; a vacatur or stay affecting the effective date); any rule requiring counsel to set the comment-letter signature posture.
- **Executive committee**: any rule with a cost-to-comply read over $50M one-time or $20M run-rate (illustrative threshold; firm-specific thresholds in `references/firm-overlay.md`).
- **Board risk committee**: any rule introducing a new board-committee-reporting expectation; any rule under a Heightened-Standards Risk Governance Framework category; any consent-order-pattern theme that names a peer institution under the same primary regulator.
- **Full board**: any rule with strategic-business-model implications (e.g., the Basel III Endgame final rule's capital implications for affected firms); any rule with a board-attestation expectation.

The escalation triggers are firm-specific; the overlay names the pattern, and `references/firm-overlay.md` overrides with firm-specific thresholds.
