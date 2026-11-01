# Payments / fintech sector overlay for adverse-action-review

When the scope record names sector `payments-fintech`, this overlay adds payments / fintech-specific scope, methodology, and review-gate detail to the adverse-action notice review.

Loaded by: `adverse-action-review/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`, or when the institution type is a non-bank lender, BNPL provider, marketplace lender, or fintech operating under a sponsor-bank arrangement.

Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for payments / fintech adverse-action review

The payments / fintech overlay turns on three structural questions: who is the creditor of record, where the model and notice template live, and whether the program-operator or the sponsor bank carries the §1002.9 obligation.

### 1. Sponsor-bank vs. fintech-of-record allocation

In a typical sponsor-bank lending program, the bank is the creditor of record and the fintech operates the marketing, application, and decisioning workflow as a service provider under the program agreement. Reg B obligations rest on the creditor; the bank is the §1002.9 obligor. The interagency third-party guidance (June 2023) anchors the bank-side accountability, and the program agreement allocates operational duties.

Where the fintech is the lender of record (true-lender direct lending, state-licensed lender programs), the fintech carries the §1002.9 obligation directly. The review records the creditor-of-record per program at the population level, not per decision.

Joint review is the operational norm: the bank's compliance second-line and the fintech's compliance team review the notice population jointly, with sign-off allocated per the program agreement. The artifact records both review owners and both committee gates.

### 2. BNPL adverse-action posture

The CFPB Interpretive Rule on BNPL (May 2024) was **nullified by Pub. L. 119-11 (May 9, 2025); historical only.** The earlier framing treated certain BNPL lenders that issue digital user accounts as card issuers under Regulation Z; that Reg Z reach is no longer in force. Reg B and ECOA continue to apply to BNPL credit decisions on their own terms. Adverse action on a BNPL decline (including soft-decline patterns where the customer is shown only longer-tenor or smaller-amount offers) falls under §1002.9.

The §1002.2(c) action category is load-bearing: a BNPL flow that presents the customer with a smaller amount or longer tenor than requested is a counteroffer; if not accepted, it is adverse action. Many BNPL flows do not surface this as an adverse-action event today; the review tests the flow against the §1002.2(c) categories.

### 3. Vendor-supplied decisioning model

Where the underwriting decision uses a vendor-supplied model (turn-key fraud-deny, identity-deny, alternative-data score, open-banking cash-flow score), the fintech and the sponsor bank inherit the model-supported-reasons obligation. The vendor may not produce per-decision feature contributions out of the box; the review records the vendor's explainability artifact as evidence and flags where it is absent.

Vendor-of-record reason coding is a recurring defect: vendor returns a numeric score and a small set of reason flags from a fixed dictionary, the fintech's notice template selects the closest sample-form match, and neither the vendor nor the fintech can demonstrate per-decision feature contributions. Reg B §1002.9 and Comment 9(b)(2)-3 of the Official Staff Commentary are the operative anchors (CFPB Circulars 2022-03 / 2023-03 are **withdrawn May 12, 2025; historical only.**); the review records vendor explainability as a named gap when absent.

### 4. Alternative-data feature posture

Fintech underwriting models often use alternative data (cash-flow patterns, employment-platform attestations, telecom and utility tradelines, device and behavioral signals). The model-supported-reasons review tests that cited reasons reflect the actual feature contributions; "insufficient credit history" cited on a model that did not use traditional credit-bureau data, or "value of collateral" cited on an unsecured product, are recurring impossible-mapping defects.

The fair-lending exposure of alternative-data features (proxy-for-protected-class concerns) is not the adverse-action review's lane; the review flags suspicious features and routes to `fair-lending-test-plan`.

### 5. Program-agreement and exit-clause interactions

The sponsor-bank program agreement typically grants the bank approval rights over the fintech's notice template, model release, and reason-code dictionary. The review records the version of the notice template in scope and the date of the bank's last approval; out-of-version notices are an immediate finding regardless of substantive compliance. Where the program has an exit clause active or a remediation plan in flight, the review records the program status because notice-fix recommendations may interact with exit timing.

## Payments / fintech-specific review additions

- `population.creditor_of_record` enum (sponsor-bank, fintech-of-record, joint).
- `population.program_agreement_version` and `population.notice_template_version_approved_date`.
- `decisions[].vendor_decisioning_model_id` and `decisions[].vendor_explainability_artifact_present` boolean.
- `decisions[].alternative_data_feature_present` boolean.
- `model_reason_generation_review.vendor_explainability_method` string (vendor-named method) and `vendor_explainability_artifact_evidence_path`.
- `recommended_actions[].joint_committee_routing` boolean (bank fair-lending committee plus fintech compliance committee).

## Common pitfalls in payments / fintech adverse-action review

- Treating Reg B as the bank's problem when the fintech operates the workflow; the bank is the §1002.9 obligor in a sponsor-bank arrangement and the fintech is the operational owner. Both audiences read the artifact.
- Treating BNPL adverse action as a Reg Z question (the May 2024 Interpretive Rule was about Reg Z and is **nullified by Pub. L. 119-11 (May 9, 2025); historical only.**); ECOA and Reg B apply on their own terms.
- Missing the soft-decline counteroffer pattern on BNPL, where the customer is shown a smaller amount or longer tenor. Counteroffers not accepted are adverse action.
- Accepting a vendor's fixed reason-code dictionary as the creditor's compliance evidence; the creditor must demonstrate the cited reasons reflect the actual principal feature contributions per Reg B §1002.9 and Comment 9(b)(2)-3 of the Official Staff Commentary.
- Reviewing notices against the current template version when the population was decided under an earlier version; the population review tests the template version that was in force at decision time.
- Routing a finding only to the fintech compliance team where the sponsor-bank program agreement requires joint sign-off; both routes are needed and the artifact names both.
