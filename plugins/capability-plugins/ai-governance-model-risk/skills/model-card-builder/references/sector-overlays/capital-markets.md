# Capital markets sector overlay for model-card-builder

When the scope record names sector `capital-markets`, this overlay adds capital-markets-specific fields and review demands to the card. Where there is conflict between the capability defaults and this overlay, the overlay governs the capital-markets-sector elements.

Source content in this overlay derives from the capital-markets lead's overlay snippets in the phase-1 spec sheets, adapted to the model-card context. Cited and section-referenced anchors in `references/source-anchors.md`.

## What changes for capital-markets model cards

### 1. SR 11-7 reach is partial, not blanket

For investment advisers and broker-dealers that are not part of a bank holding company, SR 11-7 is not directly binding. The card uses NIST AI RMF and ISO/IEC 42001 as the primary anchor; SR 11-7 is referenced where the parent BHC inherits the model risk through a banking subsidiary. Card-writer should not assert SR 11-7 reach to standalone advisers/BDs.

The substantive expectations (intended use, data, performance, monitoring, controls, sign-off) are the same; the regulator constellation differs.

### 2. SEC and FINRA expectations come through Rule 206(4)-7, FINRA 3110, Reg BI, and Marketing Rule

For an investment adviser, the model's role in the compliance program connects through Rule 206(4)-7 (compliance program adoption and annual review). For a broker-dealer, FINRA Rule 3110 (supervisory system) and Reg BI (best interest, care obligation) are the primary frames. The model card supports the supervision and disclosure evidence the rules expect.

Card-side implications:

- For an adviser: the CCO is an audience; the annual Rule 206(4)-7 review is a re-validation cadence trigger.
- For a BD: supervisory system documentation is a card audience; FINRA WSPs reference the model.

### 3. SEC predictive-data-analytics rulemaking

The SEC proposed rules on conflicts of interest in the use of predictive data analytics by broker-dealers and investment advisers (proposed July 2023) [verify current state — proposal, withdrawal, or further action]. The card flags the conflict-of-interest question for any model that interacts with retail-investor decisions. Where the rule is currently in proposal or non-final state, the card records the firm's monitoring posture rather than asserting compliance with a non-final rule.

### 4. AI in marketing materials and the Marketing Rule

For investment advisers under the IAA, Marketing Rule (Rule 206(4)-1) coverage extends to AI-generated client communications, AI-generated hypothetical performance, and AI-generated testimonials/endorsements. The card flags Marketing Rule reach when the model output reaches clients or prospective clients; required disclosures are a controls-section item.

### 5. Best-execution surveillance, execution algos, and trading models

For execution algorithms and trading-related models, additional anchors apply:

- SEC Rule 15c3-5 (Market Access Rule) controls overlap; the card section on controls names financial and regulatory risk management controls per Rule 15c3-5.
- FINRA Rule 5310 best-execution obligations; for models that influence execution venue choice, the card carries a best-execution-monitoring control reference.
- For surveillance models (insider trading, market manipulation, spoofing detection, layering), FINRA Rule 3110 supervisory expectations apply; the card section on controls names the supervisory-system integration.

### 6. Books-and-records reach (Rule 204-2 for advisers; Rule 17a-3/4 for BDs)

For any model that supports an advisory recommendation or a trading decision, books-and-records rules apply to the model output and to the inputs that drove it. The card carries:

- A retention statement for model outputs that support recommendations.
- A retention statement for inputs and decisions where the rule reaches the underlying basis.
- A note on the firm's books-and-records system of record for AI-generated content (for GenAI use cases, this is a frequent gap).

### 7. Sub-adviser and fund-board awareness

Where the model is operated by a sub-adviser on the registrant's funds, sub-adviser oversight under 38a-1(a)(4) applies. The card identifies sub-adviser operation, the firm's oversight cadence, and the fund-board reporting posture. For a 1940 Act fund context, the fund's CCO is an additional card audience.

### 8. AIFMD / MiFID II for cross-border activity

For US advisers serving EU professional or retail clients, AIFMD / MiFID II overlay can extend; the card flags EU client exposure and routes to `ai-act-triage` for the EU-applicability scoping.

## Capital-markets-specific output template additions

- `card_metadata.legal_entity_type` — investment adviser / broker-dealer / dual registrant / 1940 Act fund / 1933 Act issuer / municipal-securities entity.
- `card_metadata.primary_regulator_constellation` — SEC / FINRA / state-IA / MSRB / NYSE / CBOE / FOREX / other.
- `card_metadata.fund_board_reporting_inscope` — boolean; for 1940 Act fund use cases.
- `card_metadata.sub_adviser_operated` — boolean; if true, sub-adviser oversight cadence is a controls field.
- `card_metadata.marketing_rule_reach` — boolean; for AI generating client-facing content.
- `card_metadata.market_access_rule_inscope` — boolean; for execution algo or order-routing models under Rule 15c3-5.
- `data[].books_and_records_retention` — retention statement aligned to Rule 204-2 or Rule 17a-3/4 as applicable.
- `controls[]` — best-execution monitoring (Rule 5310) where applicable; supervisory-system integration (FINRA 3110) where applicable; conflict-of-interest disclosure where applicable.
- `signoff_questions[]` — capital-markets-specific (CCO sign-off, fund-board reporting posture, books-and-records reach, predictive-analytics rulemaking posture, Marketing Rule reach where applicable).

## Common pitfalls in capital-markets model cards

- Importing SR 11-7 vocabulary into an adviser/BD card without confirming SR 11-7 reach; it does not directly apply to non-bank registrants.
- Omitting books-and-records reach for AI-generated client content; Rule 204-2 catches the firm at exam time.
- Treating the SEC predictive-analytics proposal as binding when it is currently in non-final state; or treating it as irrelevant when the firm's risk register already monitors the proposal.
- Missing Marketing Rule reach for AI-generated investment-letter drafts or RFP-response generation.
- Forgetting fund-board reporting posture for sub-adviser-operated AI on the registrant's funds.
- Treating execution-algo Market Access Rule controls as engineering controls rather than card-section controls; Rule 15c3-5 controls are governance controls and belong in the card.
