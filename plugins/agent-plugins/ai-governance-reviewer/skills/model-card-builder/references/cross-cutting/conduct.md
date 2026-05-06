# Conduct cross-cutting overlay for model-card-builder

When the engagement-scope record flags `conduct` for the model use case, this overlay adds conduct-risk content to named card sections. Conduct risk in second-line vocabulary is not the same as fairness as a model property; it is the customer-outcome and market-integrity lens, the named-manager accountability lens, and the regulatory-engagement lens. The card's conduct content sits alongside the fairness-and-explainability section, not inside it.

Loaded by: `model-card-builder/SKILL.md` when `engagement_scope.cross_cutting_set` includes `conduct`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- FCA Senior Managers and Certification Regime (SMCR) for UK-licensed entities, where named-manager accountability for prescribed responsibilities reaches into model-related decisions for in-scope firms.
- US enforcement themes on algorithmic discrimination and unfair / abusive practices, including the April 2023 Joint Statement on Enforcement Efforts Against Discrimination and Bias in Automated Systems (CFPB, DOJ, EEOC, FTC) and the CFPB Circulars on AI in adverse-action notices and consumer credit.
- Conduct risk taxonomy as commonly framed by second-line conduct functions: customer outcomes, market integrity, employee conduct, regulatory engagement, financial-crime adjacency. Firm-specific taxonomy lives in `references/firm-overlay.md` when present.
- Product-governance expectations: target-market definition, product testing, distribution suitability. For FCA-regulated entities, PROD applies; for non-UK entities, the firm's own product-governance framework applies and the conduct overlay names that framework.

## What changes for conduct-flagged model cards

### 1. Intended use gains a customer-outcome lens

The intended-use section adds a customer-outcome subsection: who the customer is, what outcome the model produces for the customer (decision, price, experience, recommendation, refusal), and which customer journeys are touched. The firm-impact framing (efficiency, throughput, loss reduction) sits separately; the conduct lens is customer-outcome first. Out-of-scope decisions are sharpened to name the customer-outcome boundary.

### 2. Fairness section addresses customer-outcome disparity, not only protected-class disparity

Customer-outcome disparity is the conduct-tagged extension of the fairness section: where the model produces materially different customer outcomes (price, eligibility, access, experience) across customer segments that are not protected classes but are policy-relevant (rural, low-balance, digital-only, English-as-second-language, recent-immigrant cohorts where lawful to consider), the conduct overlay expects those segments named and the disparity assessed. The vocabulary is "customer-outcome disparity" alongside the protected-class disparity vocabulary; the test framing is recorded so the reviewer sees which lens is in use.

### 3. Controls section adds conduct-tagged review gates

Beyond model-risk-committee and validator review, conduct-flagged cards typically include a product committee or customer-outcome committee review gate; for UK-licensed firms with PROD in scope, the product-governance committee review is a controls-section item. For consumer-facing models, the complaint surface is a controls-section item: complaint-rate monitoring, complaint-code monitoring, root-cause feedback into the change-management table.

### 4. Sign-off names the conduct-accountable manager

For UK-licensed firms in SMCR scope, the senior manager with allocated responsibility for the relevant prescribed responsibility is a named sign-off audience. For non-UK firms, the firm's conduct framework names a manager (often the head of the relevant business or the head of consumer / customer); the card names the role, not the individual. The model owner is not by default the conduct-accountable manager; the card is explicit about which is which.

### 5. Change management adds conduct re-validation triggers

A change in target market or distribution channel, a change that materially shifts customer-outcome distribution, a complaint-rate breach, and a regulatory-engagement event (CFPB inquiry, FCA Section 166 review, state DOI inquiry, fair-lending exam finding) are each conduct re-validation triggers.

## Conduct-specific output template additions

- A "Conduct considerations" subsection inside `intended_use` (in the structured object: `intended_use.conduct_subsection` covering customer-outcome lens, customer-journey impact, target market and distribution).
- Customer-outcome-disparity entries in `fairness_results[]` alongside protected-class-disparity entries, with `test_framing` set to make the lens explicit.
- Conduct-tagged entries in `controls[]` (product committee or customer-outcome committee gate, complaint-surface monitoring control, suitability or best-interest control where applicable).
- Conduct-tagged entries in `change_management[]` (target-market change, distribution-channel change, customer-outcome shift, complaint-rate breach, regulatory-engagement event).
- A `conduct_accountable_manager_role` field in `card_metadata` naming the role under SMCR or the firm's conduct framework, distinct from the model owner.
- Conduct-tagged sign-off questions (named conduct-accountable manager, customer-outcome assessment status, complaint-surface integration, target-market alignment, regulatory-engagement posture).

## Common pitfalls in conduct-flagged model cards

- Framing fairness as a model property without addressing customer-outcome disparity. A model can pass disparate-impact tests on protected classes and still produce materially different customer outcomes across policy-relevant segments; conduct frames the second lens.
- Treating SMCR or the firm's conduct framework as compliance overhead rather than as a conduct-risk-management input to the card. The named-manager role is a substantive sign-off, not a signature line.
- Assuming the model owner is the conduct-accountable manager when the conduct framework names a different role. The two are separable and frequently are separated; the card is explicit.
- Missing the customer-journey impact when the model affects customer experience but not directly customer pricing or eligibility. A chatbot that handles initial enquiries shapes customer outcome through access and friction, not only through the explicit decision; the conduct lens catches this where a fairness-only lens does not.
- Carrying enforcement-theme risk into the card as a generic warning. Where the firm has a specific monitoring posture for a specific enforcement theme (CFPB AI circulars, the April 2023 Joint Statement themes), the card records the firm posture; where it does not, the gap is recorded as a sign-off question rather than asserted as coverage.
- Treating the complaint surface as a customer-service metric rather than a conduct signal. Complaint-rate and complaint-code drift are leading indicators of customer-outcome harm and belong in the monitoring plan with named owner and escalation.
