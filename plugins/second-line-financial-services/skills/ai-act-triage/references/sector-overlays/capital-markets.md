# Capital-markets sector overlay for ai-act-triage

When the scope record names sector `capital-markets`, this overlay adds capital-markets-specific scoping, Article 2 exclusion analysis, and parallel-regime reconciliation to the EU AI Act triage. EU branches of US asset managers and broker-dealers, EU-authorised investment firms (MiFID II), UCITS management companies, AIFMs, and EU-authorised central counterparties and trading venues all use this overlay alongside the capability triage. Where there is conflict between the capability defaults and this overlay, the overlay governs the capital-markets-specific elements.

Loaded by: `ai-act-triage/SKILL.md` when `scope.sector_overlay_set` includes `capital-markets`, or when the institution type implicates an investment firm, asset manager, broker-dealer, UCITS ManCo, AIFM, trading venue, central counterparty, central securities depository, or related capital-markets entity. Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for a capital-markets triage

### 1. Annex III rarely lands directly for adviser and BD use cases

The Annex III high-risk list focuses on use cases with material impact on natural persons (creditworthiness, life and health insurance pricing, employment selection, biometric, education, essential services, law enforcement, migration, justice). Most adviser, BD, asset-management, and trading-venue AI use cases do not land in Annex III directly:

- Investment recommendation and portfolio-management AI: not Annex III. The fiduciary and best-interest analysis sits in MiFID II and member-state conduct frameworks, not in the AI Act high-risk regime.
- Trading and execution algorithms: not Annex III. The MiFID II algorithmic trading regime (Article 17 and RTS 6) reaches separately.
- Surveillance algorithms (insider trading, market abuse, manipulation, layering, spoofing): not Annex III. MAR / market-abuse regime reaches separately.
- Research and marketing GenAI: not Annex III. Article 50 transparency typically applies; Marketing Rule and member-state advertising regimes reach separately.

The triage walks Annex III row by row and records the conclusion. The walk is not perfunctory because boundary cases reach:

- Employment selection AI used by the firm for staff hiring or evaluation: Annex III(4) applies. Common in larger advisers and BDs; the triage flags this as a separate workstream from the investment-side AI.
- Biometric AI for office access or trading-floor identification: Annex III(1) applies in defined circumstances.
- Consumer-credit-style scoring inside a BD retail-onboarding flow: Annex III(5)(b) applies where the BD extends consumer credit (e.g., margin-equivalent products with consumer-credit characteristics); rare but worth the row-by-row check.

### 2. Article 2 exclusion analysis: the MiFID II surveillance and market-abuse boundary

Article 2(3) of the AI Act excludes AI systems and models specifically developed and put into service for the sole purpose of scientific research and development. This exclusion does not reach production trading-venue surveillance or market-abuse detection systems.

The triage walks Article 2 exclusions on the record where the use case is research-or-pilot adjacent. The triage does not invoke the research exclusion for a system that has moved into production use.

### 3. MiFID II algorithmic trading regime runs in parallel

For investment firms engaged in algorithmic trading, MiFID II Article 17 and Commission Delegated Regulation 2017/589 (RTS 6) impose substantive governance obligations: governance of the algorithm, testing, kill functionality, change management, conformance testing, and notifications to competent authorities. AI Act obligations attach in addition where a row of Annex III applies, but typically do not for trading algos.

The triage records the regime overlap as a side-by-side block; reviewers downstream need both lenses visible. The side-by-side block names:

- The MiFID II Article 17 / RTS 6 obligations (governance, testing, kill switch, change management, notification).
- The AI Act obligations attaching where any do (rare; typically Article 50 if the algo's outputs reach a natural-person interface, otherwise none from the high-risk regime).
- The reconciliation: MiFID II is the operative governance frame; AI Act adds where it adds.

### 4. Article 50 transparency for client-facing GenAI

For client-facing AI surfaces (chatbots, RFP-response generation, investment-letter drafting, research summarisation reaching clients), Article 50 sub-obligations screen individually:

- 50(1) AI-interaction disclosure: applies inside the firm and on client surfaces.
- 50(2) synthetic-content marking: applies on outbound text drafts that reach clients.
- 50(3) deepfake disclosure: applies where synthetic image, audio, or video is used in client communications.
- 50(4) AI-generated text on matters of public interest: applies where the firm publishes commentary on matters of public interest (e.g., macro research released publicly) generated or substantially assisted by AI.
- 50(5) emotion recognition / biometric categorisation: typically not applicable to capital-markets use cases.

The disclosure language sits alongside the Marketing Rule disclosures (US-side) and member-state advertising regimes (EU-side). The triage records the disclosure-language posture and routes the language drafting to the firm's marketing-and-disclosures function with legal review.

### 5. Books-and-records reach for AI-generated content

For US-registered advisers under Rule 204-2 and BDs under Rule 17a-3 / 17a-4, AI-generated content supporting a recommendation or decision falls within books-and-records preservation scope. The EU AI Act does not directly impose a books-and-records obligation on the same surface, but Article 12 (record-keeping obligations on providers of high-risk AI systems) and Article 26(6) (deployer obligation to keep automatically generated logs for at least six months) attach where the system is high-risk.

For most capital-markets use cases that are not high-risk, the books-and-records reach is the US-side or member-state-side regime; the AI Act does not add a parallel obligation. The triage records the operative books-and-records regime per jurisdiction and notes where AI Act Article 12 / 26(6) attaches in addition.

### 6. Marketing Rule (US) and member-state marketing regimes

For investment advisers under the IAA, Marketing Rule (Rule 206(4)-1) coverage extends to AI-generated client communications, AI-generated hypothetical performance, and AI-generated testimonials/endorsements. For EU-authorised investment firms, the MiFID II marketing communications regime (Article 24 plus Commission Delegated Regulation 2017/565) reaches.

The triage records the marketing-regime reach per jurisdiction; AI Act Article 50 is the AI-side disclosure obligation that runs alongside but does not replace the marketing-regime disclosures.

### 7. Sub-adviser and fund-board awareness

Where the AI is operated by a sub-adviser or by a delegate of an EU UCITS ManCo or AIFM, the delegation-and-oversight regime applies (UCITS Directive Article 13 and Commission Delegated Regulation 2010/43; AIFMD Article 20 and AIFMR). The triage records:

- The sub-adviser or delegate's operator role under the AI Act (typically deployer).
- The principal entity's oversight obligations under the delegation regime.
- The fund-board reporting posture for material AI use changes.

### 8. GPAI and vendor-LLM evidence asks

For client-facing GenAI surfaces using a vendor LLM, the vendor's GPAI obligations under Articles 51 to 55 do not transfer to the deploying firm. The deploying firm is the deployer of the system and may be the provider of the system if it builds the system on top of the GPAI model. The triage records:

- The vendor's GPAI status (general-purpose AI model under Article 51; systemic-risk GPAI under Article 51(2) where designated).
- The vendor's Code of Practice signature status (the EU AI Office Code of Practice on General-Purpose AI is voluntary; signature is a deployer-side evidence-quality signal).
- The deployer-side evidence asks: training-data summary per Article 53(1)(d), copyright posture, transparency documentation; routed to vendor diligence.
- The Article 25 flip-to-provider analysis where the firm fine-tunes or substantially modifies the vendor model.

### 9. AIFMD / MiFID II extraterritorial reach

For US advisers serving EU professional or retail clients, AIFMD (for AIF marketing into the EU) and MiFID II (for cross-border investment-services provision) reach. The AI Act overlay attaches where any Annex III row applies (rare for adviser/BD use cases) or where Article 50 transparency obligations attach to client-facing surfaces. The triage records:

- Whether the US adviser markets AIFs into the EU under AIFMD national private placement regimes.
- Whether the US adviser provides investment services into the EU under MiFID II reverse solicitation, third-country branch regime, or third-country firm access (where established by an equivalence decision).
- The AI Act exposure on the EU side (typically Article 50 transparency for client-facing surfaces; Annex III rare).

### 10. Capital-markets-AI use-case categories the triage explicitly recognises

The triage labels the use-case category up front:

- Investment-recommendation or portfolio-management AI: not Annex III; MiFID II / IAA fiduciary frame is operative.
- Trading and execution algorithms: not Annex III; MiFID II Article 17 / RTS 6 is operative on the EU side; SEC Rule 15c3-5 on the US side.
- Surveillance and market-abuse detection: not Annex III; MAR (EU) and FINRA / SEC supervisory rules (US) operative.
- Client-facing chatbot or assistant: not Annex III; Article 50 transparency applies.
- Research and marketing GenAI: not Annex III; Article 50 sub-obligations screened; Marketing Rule (US) and MiFID II marketing-communications (EU) overlay.
- Internal productivity GenAI (RFP response, board materials, summarisation): not Annex III; books-and-records reach where output supports a recommendation or decision.
- Employment selection AI for staff hiring: Annex III(4) applies; separate workstream from investment-side AI.
- Biometric AI for office access: Annex III(1) applies in defined circumstances.

## Capital-markets-specific output template additions

The triage artifact adds the following blocks when this overlay loads:

- A use-case category line at the top (per the categories above).
- A MiFID II Article 17 / RTS 6 cross-walk for any algorithmic-trading use case.
- A Marketing Rule / MiFID II marketing-communications cross-walk for any client-facing GenAI use case.
- A books-and-records reach line per applicable jurisdiction.
- A delegation-and-oversight regime line for sub-adviser or delegate operation.
- A GPAI vendor-evidence-asks block for vendor-LLM-backed surfaces, including Code of Practice signature status.
- An employment-AI separate-workstream flag where staff-hiring AI is on the firm's inventory.

## Common pitfalls in capital-markets AI Act triages

- Assuming the AI Act has nothing to say about capital-markets AI because Annex III rarely lands directly; Article 50 transparency reaches client-facing GenAI surfaces and the screen must run.
- Conflating the MiFID II Article 17 / RTS 6 algorithmic-trading regime with the AI Act high-risk regime; they are separate and both attach where their own conditions are met.
- Treating books-and-records reach as the AI Act's reach; the operative books-and-records regime is the US-side adviser/BD rule or the member-state-side investment-firm rule; AI Act Article 12 / 26(6) attaches only for high-risk systems.
- Importing US-side Marketing Rule disclosure language as the AI Act Article 50 disclosure; the two are separate and both apply where their conditions are met.
- Skipping the delegation-and-oversight analysis for sub-adviser or delegate AI use; UCITS Article 13 and AIFMD Article 20 reach the principal's oversight obligation regardless of where the AI sits.
- Treating GPAI provider obligations as the deployer's obligations; the deployer's obligations are the deployer's; the GPAI provider obligations sit with the model provider.
- Missing the staff-hiring AI workstream as Annex III(4); the workstream is separate from investment-side AI but reaches under the same triage.
- Asserting MiFID II reverse-solicitation as a basis for ignoring AI Act exposure on EU clients; reverse solicitation does not displace AI Act obligations on the firm where the firm's AI surface reaches EU users.
