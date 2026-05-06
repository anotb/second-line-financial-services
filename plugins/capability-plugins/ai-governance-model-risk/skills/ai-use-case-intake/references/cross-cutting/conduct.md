# Conduct cross-cutting overlay for ai-use-case-intake

When the engagement-scope record flags `conduct` for the use case, this overlay supplies the conduct-specific intake fields and the named flags that route into downstream tier, fairness-testing, and complaint-surveillance work. Conduct in financial services is broader than fair lending alone: customer-binding decisions, fairness exposure, complaint vector, and market-integrity reach all sit in the conduct lens.

Loaded by: `ai-use-case-intake/SKILL.md` when `engagement_scope.cross_cutting_set` includes `conduct`. Source-anchored in `references/source-anchors.md`.

## Source basis

- ECOA (15 USC §1691) and Reg B (12 CFR Part 1002) — credit-decision conduct frame.
- CFPB Circulars on adverse action with complex algorithms (Circular 2022-03; Circular 2023-03 [verify]) — specific reasons under ECOA when complex algorithms drive credit decisions.
- UDAAP (Dodd-Frank §§1031, 1036) — consumer-financial-services conduct frame, applied across the CFPB's reach.
- FTC Act §5 (15 USC §45) — UDAP frame applied to non-CFPB-supervised entities.
- NAIC Unfair Trade Practices Act (Model #880) — insurance conduct frame, including unfair claims-settlement standards and fair-claims-settlement standards.
- SEC Investment Advisers Act §206 antifraud and Rule 206(4)-1 Marketing Rule — adviser conduct frame.
- SEC Reg BI — BD conduct frame for retail customers.
- FINRA 2010 (just and equitable principles) and FINRA 2111 (suitability) — BD conduct frame.
- MAR (Market Abuse Regulation) and Reg AC — research integrity and market-integrity conduct.

## Conduct-specific intake fields

In addition to the capability intake spine, the conduct overlay adds the following:

- Customer-binding posture: whether the use case binds the firm to a customer-facing decision (origination, pricing, line management, claims acceptance / denial, account closure, hold) or surfaces a recommendation a human acts on.
- Fairness-sensitive dimensions: protected classes under federal and state law (race, colour, religion, national origin, sex including sexual orientation and gender identity, marital status, age, receipt of public assistance, exercise of rights under the Consumer Credit Protection Act); insurance-specific protected classifications; state-specific protected classes.
- Complaint vector: whether the use case is likely to generate consumer complaints, and through which channels (firm complaint line, sponsor-bank-routed complaints, CFPB Consumer Complaint Database, state DOI complaint, regulator inquiry).
- Adverse-action posture: whether the use case drives an adverse-action notice (credit decision under ECOA / Reg B; insurance underwriting denial under state DOI rules; insurance claims denial under Model #880 reasoned-denial standards).
- Marketing-claim posture: where the use case generates or personalises marketing content, the marketing-claim review flag.

## Conduct-specific regulatory flags

When the conduct overlay is loaded, the intake's regulatory-flags table picks up:

- `CFPB_Circular_2022_03` and `CFPB_Circular_2023_03` [verify] for credit-decision use cases driving adverse action.
- `UDAAP` (or `FTC_5` for non-CFPB-reach entities) for any consumer-facing use case with a conduct surface.
- `NAIC_Model_880` for insurance use cases (unfair claims and unfair acts; fair-claims-settlement standards).
- `Reg_BI` for BDs serving retail customers where the use case influences a recommendation.
- `SEC_Marketing_Rule` for advisers where the use case touches client-facing material.
- `FINRA_2111` for BDs where the use case influences a suitability determination.
- State DOI bulletins and state UCSPA where insurance customer-facing.
- `MAR` and `Reg_AC` where research integrity is in question.

## Conduct-specific open questions for downstream skills

The intake routes the following open questions when relevant:

- For `validation-plan`: fairness-testing scope (which protected and policy-relevant dimensions, what test, what threshold); inferred-attribute risk where the model infers a fairness-sensitive attribute from proxies; segment-level performance evidence for any customer-binding decision.
- For `model-card-builder`: the limitations and known failure modes for fairness-sensitive segments; the adverse-action reason generation method (where applicable); the marketing-claim posture (where applicable).
- For complaint surveillance: how does the firm trace a complaint back to the use case, and what is the cadence for AI-attributable complaint review.
- For consumer-compliance review: where does the use case sit in the firm's UDAAP review cycle (or state UCSPA review cycle for insurance); what is the dark-pattern risk in onboarding or product-selection flows the use case touches.
- For regulator-engagement: examiner-facing posture on the use case (which examiner is most likely to engage on it; what the firm's prepared narrative is).

## Common pitfalls in conduct-flagged intake

- Treating conduct as a synonym for fair lending. Fair lending is one slice; UDAAP, NAIC Model #880, Reg BI, Marketing Rule, and MAR each cover distinct conduct surfaces with their own tests.
- Recording "no customer impact" on a use case that surfaces a recommendation a human acts on. The recommendation is the conduct surface; the human review point does not eliminate the conduct exposure.
- Using fairness terminology where unfair-discrimination terminology is the operative legal frame (insurance pricing and underwriting under NAIC Model #880); the test is different (actuarial justification matters; permitted vs prohibited rating factors are state-defined; protected classes per state insurance code).
- Missing the inferred-attribute open question. A model that does not take race or ethnicity as input may still drive disparate outcomes through proxies; the conduct-flagged intake records this as an open question for `validation-plan`.
- Recording an internal-use research summariser as no-conduct-exposure when the output may be incorporated into a published research note. Reg AC and Marketing Rule reach attach to the published output, not to the underlying tool.
- Recording a fintech account-closure use case as low-conduct without flagging the CFPB UDAAP theme. Account closures and account holds without adequate notice or recourse have been the most-frequent fintech UDAAP theme in recent CFPB Supervisory Highlights [verify date and exact reference].
