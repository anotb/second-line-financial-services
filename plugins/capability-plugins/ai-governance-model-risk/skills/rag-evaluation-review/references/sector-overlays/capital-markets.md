# Capital markets sector overlay for rag-evaluation-review

When the scope record names `capital-markets` as the sector, this overlay adds capital-markets-specific corpora considerations, mitigations, monitoring signals, and review-coordination expectations to the RAG evaluation review. Loaded by `rag-evaluation-review/SKILL.md` when `scope.sector_overlay_set` includes `capital-markets`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- SEC Investment Advisers Act Rule 206(4)-1 (Marketing Rule) and Rule 204-2 (Books and Records) for any AI-generated client-facing content from a registered investment adviser.
- SEC Regulation Analyst Certification (Reg AC) and FINRA Rule 2241 (Research) for research-assistant use cases.
- Market Abuse Regulation (MAR) for EU-touch capital-markets entities, particularly Articles 7 (inside information), 14 (insider dealing), and 15 (market manipulation), where retrieval over MNPI-adjacent corpora can create selective-disclosure or biased-retrieval exposure.
- SEC Rule 17a-4 and FINRA Rule 4511 (books and records preservation) for retained AI-generated outputs.
- SEC Reg BI (Regulation Best Interest) for broker-dealer client-facing content; SEC fiduciary-standard framing for adviser content.
- MiFID II Article 24 (information to clients) and product governance framing where applicable.
- SEC cyber disclosure rules (8-K Item 1.05 and Reg S-K Item 106) for public registrants where retrieval-driven exfiltration of MNPI could be a material cyber event; pointer to the cyber overlay.

## Corpora typical of capital markets and the fitness considerations they raise

The recurring capital-markets RAG corpora and the fitness questions that bite:

- **Research notes and analyst content**: published research, internal research drafts, analyst commentary, target-price models. Sensitivity ranges across published (public) to internal-pre-publication (MNPI-adjacent). Reg AC and FINRA Rule 2241 framings apply where retrieval feeds research output. Coverage assessment keys off the research universe and the recency of the content.

- **Earnings-call transcripts and management-presentation materials**: vendor-supplied transcripts, internal call notes, management roadshow materials. Sensitivity is public for issued transcripts; internal-pre-publication for management materials carries MNPI risk. Provenance per source is the corpus-fitness spine.

- **Regulatory filings**: 10-K, 10-Q, 8-K, proxy filings, prospectus and offering documents, beneficial-ownership filings. Sensitivity is public. Coverage gaps on filings outside the firm's coverage universe are common; the gap goes in corpus-fitness, not retrieval-quality.

- **Trading and surveillance content**: trade blotters, order books, communication surveillance corpora (chat, email, voice transcripts). Sensitivity is confidential to MNPI-adjacent. Per-trader and per-desk scoping at retrieval is non-optional; surveillance-system retrieval is a separate use-case pattern with its own framing under Rule 17a-4 / FINRA 4511 records-preservation.

- **Client-portfolio content**: position data, allocation history, client documentation, advisory agreements, IPS documents. Sensitivity is confidential. Per-client scoping at retrieval is non-optional for adviser-facing or client-facing assistants.

- **Counterparty due-diligence and credit content**: counterparty profiles, credit memos, ISDA documentation, collateral agreements. Sensitivity is confidential.

## Mitigations the review should expect to see

Beyond the standard set:

- Per-trader, per-desk, per-client retrieval scoping enforced at the retriever for trading-floor and client-facing assistants.
- MNPI segregation at the corpus level: pre-publication research, deal-team materials, and counterparty-MNPI corpora are separately indexed with information-barrier controls; retrieval-side enforcement of the information barrier is the load-bearing control. Where retrieval is permissioned across corpora, the information-barrier review is non-optional.
- Marketing Rule and books-and-records output controls for any AI-generated content reaching clients: the output is preserved per Rule 17a-4 / 204-2 and is reviewable against the Marketing Rule's general prohibitions before delivery.
- Reg AC certification framing for research-assistant outputs where the AI-generated content informs a published research report.
- Where the use case is bank-affiliated and in OCC large-bank scope, the cross-overlay banking framing applies.

## Monitoring signals the overlay adds

- Per-corpus retrieval-source distribution audit with attention to MNPI-adjacent corpora; any retrieval from a barrier-protected corpus by an unauthorised user is an information-barrier event and an investigation trigger.
- Marketing Rule output-filter trip rate where AI-generated content reaches clients; escalation to compliance.
- Surveillance-system retrieval and citation precision where the system supports surveillance analyst work; misattributed surveillance findings are a programme-integrity issue.
- For research-assistant use cases, citation-precision sampling on regulatory and financial-document citations (a wrongly-cited filing in a research note is a Reg AC and conduct issue).

## Review-coordination considerations

- The compliance officer (specifically the Marketing Rule reviewer for adviser-facing entities, the supervisory analyst for research entities) is a named co-reviewer for any client-facing or research-feeding use case.
- The information-barrier coordinator is a named co-reviewer where the corpus set spans permissioned and barrier-protected content.
- The CCO is a named co-acceptor for residual risk on Marketing Rule and Reg AC framings.
- For dual-registered entities (BD plus IA), both compliance functions co-review.
- For EU-touch entities, the MAR seam is named in the residual-risk section where retrieval over MNPI-adjacent corpora is in play.

## Common pitfalls specific to capital markets

- Treating a "research corpus" as a single source when it is in fact published research plus internal pre-publication drafts plus vendor-supplied research. The MNPI-adjacency posture differs by source; per-source enumeration is non-optional.
- Asserting information-barrier enforcement at the prompt layer. The information barrier is structural; retrieval-layer enforcement is the load-bearing control. Prompt-layer enforcement is bypassable and is a finding.
- Reporting a single citation-precision number on a research-assistant use case where the citation types differ (regulatory filings, peer research, news, internal data). Segment-level reporting by citation type is required for research-feeding use cases.
- Omitting the supervisory analyst or the Marketing Rule reviewer from the reviewer attestation. Reg AC and Marketing Rule reach are co-acceptor framings, not background context.
- Not preserving AI-generated client-facing outputs per Rule 17a-4 / 204-2. Books-and-records preservation is a compliance gap, not a model gap; the recommended-action item names the records-management owner.
- Treating surveillance-system retrieval as the same use case as research retrieval. Surveillance use cases have their own evaluation framing and their own programme-integrity expectations.
