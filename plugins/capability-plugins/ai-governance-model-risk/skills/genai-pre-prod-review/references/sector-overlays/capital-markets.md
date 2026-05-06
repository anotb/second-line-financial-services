# Capital markets sector overlay for genai-pre-prod-review

When the engagement-scope record names `capital-markets` as the sector, this overlay adds capital-markets-specific gate considerations: named co-reviewers, additional notification triggers, sector-specific monitoring expectations, and recommended-action items typical of capital-markets GenAI gate reviews (research assistants, surveillance assistants, analyst assistants, execution-related assistants). Loaded by `genai-pre-prod-review/SKILL.md` when `engagement_scope.sector_overlay_set` includes `capital-markets`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- SEC Rule 206(4)-1 (Investment Adviser Marketing Rule) and Rule 204-2 (Books and Records) for AI-generated client-facing content from registered investment advisers.
- SEC Rule 17a-3 and Rule 17a-4 (broker-dealer books and records) and FINRA Rule 2210 (communications with the public) and Rule 3110 (supervision) for AI-generated or AI-assisted communications and supervisory review.
- SEC Rule 15c3-5 (Market Access Rule) for execution-related AI controls; pre-trade controls and risk management.
- SEC Regulation Best Interest (Reg BI) and the related fiduciary-lens framing for retail-facing investment recommendations.
- Market Abuse Regulation (MAR) Articles 12 and 15 (market manipulation and inside information) for surveillance-system adjacency.
- SEC and FINRA cybersecurity-related rules and guidance; SEC Reg S-P (privacy) where customer information is in scope.
- NYDFS 23 NYCRR Part 500 for NY-licensed entities including state-licensed broker-dealers and money managers.

## Co-reviewers the gate review brings in

Beyond the standard sign-off set:

- **Chief compliance officer (registered investment adviser)** or **head of compliance (broker-dealer)** for any client-facing or supervised-communication use case; Marketing Rule and FINRA Rule 2210 review.
- **Head of supervision** for any use case touching FINRA Rule 3110 supervisory review (research, communications, trade surveillance).
- **Head of trading or chief market structure officer** for any execution-adjacent use case (algorithm-related research, execution-quality analysis, pre-trade controls).
- **Head of research** for research-assistant use cases; Marketing Rule reach to research output is the seam.
- **Surveillance / market integrity** for surveillance-system AI augmentation; MAR and SEC market-manipulation framing.
- **Books-and-records function** for any AI-generated or AI-assisted output that constitutes a book or record subject to retention.

## Open conditions the overlay typically adds

- Books-and-records preservation policy explicitly covering AI-generated and AI-assisted communications; the retention policy applies to AI artefacts including prompts, retrieved content, and outputs to the extent they constitute communications subject to Rule 17a-4 or Rule 204-2.
- Marketing Rule output-filter specification signed off by chief compliance officer for any client-facing communication generated or assisted by the system.
- FINRA Rule 2210 supervisory-review workflow named for any broker-dealer use case generating or assisting public communications.
- For surveillance-augmenting use cases: documented evaluation that the AI augmentation does not introduce false-negative bias against MAR-relevant patterns; surveillance / market integrity co-sign.
- For execution-adjacent use cases: SEC Rule 15c3-5 pre-trade control review; head of trading co-sign.
- For client-facing recommendation-adjacent use cases: Reg BI or fiduciary-lens framing documented; chief compliance officer signs.

## Monitoring signals the overlay expects to see live before go-live

In addition to the standard signal set:

- Marketing Rule output-filter trip rate; escalation to chief compliance officer.
- FINRA Rule 2210 supervisory-review queue throughput where the use case generates public communications; escalation to head of supervision.
- For research assistants: citation accuracy and source-attribution audit; escalation to head of research and chief compliance officer.
- For surveillance assistants: false-negative-rate sampling against known-positive patterns; escalation to surveillance / market integrity.
- For execution-adjacent: pre-trade control trip rate; escalation to head of trading.
- Books-and-records retention coverage signal: completeness of capture for AI-relevant artefacts; escalation to books-and-records function.

## Incident-response triggers the overlay adds

In addition to the cyber-overlay-named triggers:

- SEC Reg S-P notification triggers for customer-information-relevant events.
- FINRA reporting obligations under Rule 4530 for certain reportable events including specified disciplinary events that may arise from AI-assisted communications causing supervisory-review failures.
- SEC self-reporting expectations under SEC Enforcement guidance where AI-assisted communications cause material misleading statements.
- State Marketing Rule analogues and state insurance advertising rules where the institution carries dual licensure.

The IR drill scope before go-live should exercise at minimum one capital-markets-specific incident class (e.g., confirmed Marketing Rule violation in AI-assisted client communication; confirmed surveillance false-negative in AI-augmented surveillance; confirmed books-and-records gap in AI-relevant artefact capture).

## Recommended-action items the overlay surfaces

- Books-and-records preservation policy updated to cover AI artefacts; books-and-records function co-signs.
- Marketing Rule and FINRA Rule 2210 supervisory-review workflow updated to integrate AI-assisted output for any public-communication-adjacent use case.
- For surveillance-augmenting use cases: documented baseline against the prior surveillance system's true-positive and false-negative rate, with a defined regression-test cadence.
- For execution-adjacent use cases: SEC Rule 15c3-5 pre-trade control review; coordination with the existing market-access risk-management framework.
- For dual-licensed entities (RIA + BD or BD + insurance): cross-regulator notification matrix documented per the firm's regulator constellation.

## Common pitfalls specific to capital-markets gate reviews

- Treating an AI-assisted research draft as out of Marketing Rule scope because the analyst reviews before publication. The Marketing Rule applies to the output as published; the AI-assisted draft is one input but the published communication carries the same obligation. The supervisory-review workflow needs to handle AI-assisted material distinctly enough that the supervisor can apply Marketing Rule judgement.
- Treating books-and-records as a downstream IT problem. Rule 17a-4 and Rule 204-2 apply to AI artefacts to the extent they constitute communications subject to retention; the books-and-records function is a co-reviewer and co-signer, not a downstream consumer.
- Treating a surveillance-augmenting use case as a control improvement without baseline-against-prior-system evidence. A new AI surveillance layer that improves true positives while shifting false negatives in unrelated MAR-relevant patterns is a net regression; the gate review records the regression test explicitly.
- Treating an execution-adjacent use case as not in SEC Rule 15c3-5 scope because the AI does not directly execute. Pre-trade controls apply to inputs to execution; AI-assisted decision support that materially shapes execution decisions is within scope of the firm's market-access risk-management framework.
- Omitting the chief compliance officer co-signature on client-facing AI use cases at registered investment advisers. The Marketing Rule fiduciary-lens framing is the chief compliance officer's seat; the gate decision is incomplete without it.
