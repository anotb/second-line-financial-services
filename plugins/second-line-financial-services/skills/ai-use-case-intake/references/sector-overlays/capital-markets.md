# Capital-markets sector overlay for ai-use-case-intake

When the scope record names sector `capital-markets`, this overlay tells the intake what additional fields to capture, which named regulators belong on the regulatory-flags table, and which open questions tag to downstream adviser/BD/fund AI work. The reach is SEC, FINRA, and state-IA; capability-plugin defaults built around bank prudential supervision miss the registration-class lens this sector reads through.

Loaded by: `ai-use-case-intake/SKILL.md` when `scope.sector_overlay_set` includes `capital-markets`, or when the institution type is an investment adviser, broker-dealer, dual-registrant, mutual fund / ETF, hedge fund, private equity adviser, or other SEC/FINRA registrant.

## Source basis

Cited and section-referenced in `references/source-anchors.md`. This overlay names the regulators and sources without restating excerpts.

## What changes for capital-markets intake

### 1. Registration-class lens

The intake purpose statement and intended-users block read against the registration class. Adviser, BD, dual-registrant, fund, and sub-adviser configurations carry different rule-set reach:

- Adviser: Investment Advisers Act §206 antifraud, Rule 206(4)-7 compliance program, Rule 206(4)-1 Marketing Rule, Rule 204-2 books-and-records.
- BD: Securities Exchange Act and FINRA rules, Reg BI care obligation where retail customers are involved, FINRA 3110 supervision, FINRA 4511 books-and-records, Exchange Act Rules 17a-3 / 17a-4.
- Dual-registrant: both rule sets apply; intake should record the registration class for the use case in scope.
- Fund: Investment Company Act, Rule 38a-1 fund compliance program, sub-adviser delegation considerations, fund-board reporting posture.
- Sub-adviser: 38a-1(a)(4) compliance program coverage by the fund's CCO, sub-adviser disclosure to the fund adviser and board.

### 2. Marketing Rule reach (Rule 206(4)-1)

Where AI output reaches client-facing material — research notes, RFP responses, client letters, marketing claims, AI-generated performance presentations, AI-generated testimonials, AI-personalised marketing — the Marketing Rule applies:

- `regulatory_flags`: `SEC_Marketing_Rule` with routing to `ai-risk-tiering`, `model-card-builder`, `validation-plan`. The basis names the client-facing path.
- An open question for `validation-plan`: how is hypothetical-performance content (where AI generates forward-looking output) controlled against Rule 206(4)-1(d)(6).
- An open question for `model-card-builder`: what is the testimonial/endorsement disclosure posture if AI-generated content includes client-experience claims.

### 3. Books-and-records reach (Rule 204-2; Rules 17a-3 and 17a-4)

Where AI output supports a recommendation or decision (research summaries, suitability analyses, trade rationales, communications), books-and-records preservation applies:

- `regulatory_flags`: `SEC_204_2_books_records` (advisers) or the BD equivalent (`SEC_17a_3_4_books_records`) with routing to `ai-risk-tiering` and `model-card-builder`.
- An open question for `model-card-builder`: how is AI-generated content captured into the books-and-records system, and what is the preservation format.

### 4. Reg BI care obligation (BDs serving retail customers)

Where the AI surfaces recommendations to retail customers (or to BD reps who then surface them), Reg BI care obligation applies on top of FINRA suitability:

- `regulatory_flags`: `Reg_BI` with routing to `validation-plan`.
- An open question for `validation-plan`: how does the BD document the care analysis for an AI-recommended product, and how is the analysis sampled.

### 5. Research-integrity and conduct adjacency

Where the use case is research summarisation, research drafting, or anything adjacent to the firm's research function:

- Reg AC research-analyst certification reach if the AI output is incorporated into a published research note.
- MAR (Market Abuse Regulation) adjacency where the firm operates in the EU and the output could be construed as forward-looking research.
- An open question for `model-card-builder`: what is the analyst review point between AI summary and any incorporation into a research note.

### 6. SEC Division of Examinations focus on AI / predictive analytics

SEC EXAMS has flagged AI/predictive analytics in adviser practices in recent risk alerts [verify current state and exact reference]. Intake captures:

- A regulatory flag noting EXAMS focus area with routing to `ai-risk-tiering`.
- An open question for downstream work: is the use case in scope for the SEC's proposed conflicts-of-interest rule on predictive data analytics (proposed July 26, 2023) [verify current state — proposal, withdrawal, or further action].

### 7. Sub-adviser AI disclosure

Where the firm uses sub-adviser AI on fund assets, the fund adviser carries 38a-1 oversight responsibility:

- `vendor_dependencies`: sub-adviser as a vendor with role `model_serving_infrastructure` or `data_provider` as appropriate.
- An open question for `vendor-diligence`: what is the fund adviser's evidence pack for the sub-adviser AI, and how is sub-adviser AI use disclosed to the fund board.

### 8. AI use in fund-board materials

Where AI is used in 38a-1 materials, 15(c) materials, or fund-board agendas:

- An open question for `model-card-builder`: what is the CCO review posture for AI-drafted board materials.

## Capital-markets-specific intake fields

In addition to the capability intake spine, the following capital-markets-specific facts belong on the record when relevant:

- Registration class for the use case (adviser, BD, dual-registrant, fund, sub-adviser).
- Client-facing path (whether AI output reaches client-facing material directly, through a representative, or not at all).
- Books-and-records preservation posture.
- Sub-adviser delegation if applicable.
- Fund-board reporting posture if applicable.
- EU footprint where MAR / MiFID II reach is in question.

## Common pitfalls in capital-markets intake

- Treating an "internal-use" research-summarisation AI as low-impact; if the output is incorporated into a published research note or supports a recommendation, Marketing Rule and books-and-records reach.
- Missing the sub-adviser AI dependency when the fund adviser intakes its own use case; the sub-adviser AI is the fund adviser's responsibility under 38a-1.
- Recording a BD's AI use case without the Reg BI care obligation flag where the AI surfaces recommendations to retail customers.
- Treating Reg AC and MAR adjacency as out of scope on a research summariser; the boundary moves quickly when output crosses into forward-looking content or non-public material.
- Skipping the EU footprint check on advisers serving EU clients (EU AI Act extraterritorial reach plus MiFID II overlap can land high-risk obligations on US-based advisers).
