# Capital markets sector overlay for validation-plan

When the scope record names sector `capital-markets`, this overlay adds capital-markets-specific scope items to the validation plan. Where there is conflict between the capability defaults and this overlay, the overlay governs the capital-markets-sector elements.

Source content derives from the capital-markets lead's overlay snippets and is adapted to the validation-plan context. Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for capital-markets validation plans

### 1. SR 11-7 reach is partial, not blanket

For investment advisers and broker-dealers that are not part of a bank holding company, SR 11-7 is not directly binding. The plan uses NIST AI RMF Measure function and ISO/IEC 42001 §9 as the primary anchor; SR 11-7 is referenced where the parent BHC inherits model risk through a banking subsidiary. Plan-writer should not assert SR 11-7 reach to standalone advisers / BDs.

The substantive validation expectations (three pillars, depth per pillar, effective challenge, source trace) carry forward; the regulator constellation differs.

### 2. SEC and FINRA expectations come through Rule 206(4)-7, FINRA 3110, Reg BI, and the Marketing Rule

For an investment adviser, the model's role in the compliance program connects through Rule 206(4)-7 (compliance program adoption and annual review). For a broker-dealer, FINRA Rule 3110 (supervisory system) and Reg BI (best interest, care obligation) are the primary frames.

Plan-side implications:

- For an adviser: the CCO is a plan-acceptance audience; the annual Rule 206(4)-7 review is a re-validation cadence trigger in monitoring scope.
- For a BD: supervisory system documentation is a plan-acceptance audience; FINRA WSPs reference the model.
- For both: validation evidence supports the compliance-program review file.

### 3. SEC predictive-data-analytics rulemaking

The SEC proposed rules on conflicts of interest in the use of predictive data analytics by broker-dealers and investment advisers (proposed July 2023) [verify current state — proposal, withdrawal, or further action]. The plan flags the conflict-of-interest question for any model that interacts with retail-investor decisions. Where the rule is currently in proposal or non-final state, the plan records the firm's monitoring posture rather than asserting compliance with a non-final rule.

### 4. Marketing Rule and AI-generated client communications

For investment advisers under the IAA, Marketing Rule (Rule 206(4)-1) coverage extends to AI-generated client communications, AI-generated hypothetical performance, and AI-generated testimonials/endorsements. The plan's outcomes-analysis scope for any model that produces client-facing content includes a Marketing-Rule-required-disclosure check; a Marketing Rule effective-challenge question asks how the firm catches AI-generated content that meets the advertisement definition without manual flagging.

### 5. Best-execution surveillance, execution algos, and trading models

For execution algorithms and trading-related models, additional anchors apply:

- SEC Rule 15c3-5 (Market Access Rule) controls overlap; the plan's controls scope tests financial and regulatory pre-trade controls per Rule 15c3-5. Kill-switch testing is in robustness scope.
- FINRA Rule 5310 best-execution obligations; for models that influence execution-venue choice, the plan scopes best-execution-monitoring methodology.
- For surveillance models (insider trading, market manipulation, spoofing detection, layering), FINRA Rule 3110 supervisory expectations apply; outcomes-analysis scope includes precision/recall on alert quality and time-to-alert tests.

### 6. Books-and-records reach (Rule 204-2 for advisers; Rule 17a-3/4 for BDs)

For any model that supports an advisory recommendation or a trading decision, books-and-records rules apply to the model output and to the inputs that drove it. The plan:

- Scopes the firm's books-and-records system of record for AI-generated content (frequent gap on GenAI use cases).
- Adds a retention-evidence check to data-review scope (output retention; input and decision retention where the rule reaches the underlying basis).
- Adds an effective-challenge question on books-and-records reach for AI-generated content.

### 7. Sub-adviser and fund-board awareness

Where the model is operated by a sub-adviser on the registrant's funds, sub-adviser oversight under 38a-1(a)(4) applies. The plan identifies sub-adviser operation, the firm's oversight cadence, and the fund-board reporting posture. For a 1940 Act fund context, the fund's CCO is a plan-acceptance audience.

### 8. AIFMD / MiFID II for cross-border activity

For US advisers serving EU professional or retail clients, AIFMD / MiFID II overlay can extend; the plan flags EU client exposure and routes to `ai-act-triage` for the EU-applicability scoping.

## Capital-markets-specific output template additions

- `plan_metadata.legal_entity_type` — investment adviser / broker-dealer / dual registrant / 1940 Act fund / 1933 Act issuer / municipal-securities entity.
- `plan_metadata.primary_regulator_constellation` — SEC / FINRA / state-IA / MSRB / NYSE / CBOE / FOREX / other.
- `plan_metadata.fund_board_reporting_inscope` — boolean; for 1940 Act fund use cases.
- `plan_metadata.sub_adviser_operated` — boolean; if true, sub-adviser oversight cadence is a controls-scope item.
- `plan_metadata.marketing_rule_reach` — boolean; for AI generating client-facing content.
- `plan_metadata.market_access_rule_inscope` — boolean; for execution algo or order-routing models under Rule 15c3-5.
- `data_review.scope_items[]` — books-and-records retention statement aligned to Rule 204-2 or Rule 17a-3/4 as applicable.
- `outcomes_analysis[]` — execution-algo slippage / market-impact tests; surveillance-model precision/recall and time-to-alert tests; Marketing-Rule-required-disclosure check for AI-generated client content.
- `robustness_testing[]` — kill-switch testing for execution algos under Rule 15c3-5; vendor model-version swap drill where applicable.
- `effective_challenge_questions[]` — capital-markets-specific (CCO sign-off, fund-board reporting posture, books-and-records reach, predictive-analytics rulemaking posture, Marketing Rule reach where applicable).

## Common pitfalls in capital-markets validation plans

- Importing SR 11-7 vocabulary into an adviser/BD plan without confirming SR 11-7 reach; it does not directly apply to non-bank registrants.
- Omitting books-and-records reach for AI-generated client content; Rule 204-2 catches the firm at exam time.
- Treating the SEC predictive-analytics proposal as binding when it is currently in non-final state; or treating it as irrelevant when the firm's risk register already monitors the proposal.
- Missing Marketing Rule reach for AI-generated investment-letter drafts or RFP-response generation.
- Forgetting fund-board reporting posture for sub-adviser-operated AI on the registrant's funds.
- Treating execution-algo Market Access Rule controls as engineering controls rather than validation-scope controls; Rule 15c3-5 controls are governance controls and belong in the plan.
- Treating surveillance-model alert volume as a quality metric without precision/recall and time-to-alert; FINRA 3110 supervisory expectation is for alert quality, not just alert volume.
