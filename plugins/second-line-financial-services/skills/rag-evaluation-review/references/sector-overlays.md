# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay for rag-evaluation-review

When the scope record names `banking` as the sector, this overlay adds banking-specific corpora considerations, mitigations, monitoring signals, and review-coordination expectations to the RAG evaluation review. Loaded by `rag-evaluation-review/SKILL.md` when `scope.sector_overlay_set` includes `banking`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- FFIEC IT Examination Handbook, Information Security and AIO booklets, applied to the data-integrity controls on retrieval corpora and to the retrieval-side access enforcement.
- Joint Interagency Guidance on Third-Party Relationships (June 2023; OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023) where the corpus is vendor-supplied or the foundation model is vendor-hosted.
- The joint interagency Revised Guidance on Model Risk Management (OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, supersedes SR 11-7 and SR 21-8) expressly excludes generative AI from its scope (footnote 3); a RAG system is generative AI and is not within the bulletin. Where the bank's model risk programme treats the use case as a model by analogy, data-review and outcomes-analysis expectations apply at firm policy level rather than as binding regulator language.
- FFIEC BSA/AML Examination Manual where the use case touches AML alert handling, customer risk rating, or SAR drafting.
- 12 CFR Part 30 Appendix D (OCC Heightened Standards) for OCC-supervised large banks where the use case sits inside a risk-appetite-statement-relevant function.

#### Corpora typical of banking and the fitness considerations they raise

The recurring banking RAG corpora and the fitness questions that bite:

- **Customer relationship management (CRM)**: client interaction history, meeting notes, emails, chat. Sensitivity is internal-to-confidential; provenance is firm-controlled but content originates externally (client-supplied content can carry adversarial instructions, see `prompt-injection-risk` for the focused review). Coverage assessment for relationship-manager use cases keys off the CRM's currency and the relationship-team's discipline on note capture.

- **Compliance policy library**: firm policies, procedures, standards, and supporting materials. Sensitivity is confidential; provenance is firm-controlled with named owners and approval workflow. Freshness is the first-order question: a quarterly refresh cycle with a known post-effective-date lag is the common pattern, and the lag is a real residual risk (stale-policy answer). Coverage gaps on adjacent document sets (BSA programme manual, code of conduct, vendor management policy) are common where the policy library does not house all firm rules.

- **Regulatory text**: vendor-supplied federal banking regulations, supervisory guidance, agency publications. Sensitivity is public; provenance is vendor-tagged. Coverage gaps on state-level guidance, CFPB Circulars, or supervisory letters not in the vendor's set are common; the gap goes in the corpus-fitness assessment, not in retrieval-quality.

- **AML alert narratives, customer risk profiles, transaction-monitoring system output, sanctions-screening hits, third-party intelligence feeds**: the AML alert-triage and KYC/EDD use cases. Sensitivity ranges across confidential to MNPI-adjacent. Provenance is mixed (system-generated, analyst-authored, vendor-supplied). The BSA officer is a co-reviewer where the use case touches alert disposition, and BSA programme-integrity expectations apply to the grounding evaluation: a hallucination on an AML alert narrative is a programme issue, not a model issue.

- **Treasury-management and payments operations content**: client cash-management profiles, payment-pattern documentation, fraud-rule documentation. Sensitivity is confidential; sanctions and OFAC screening on outputs that include third-party identifying information is the load-bearing output filter.

- **Credit and collections content**: credit policy, account-status documentation, collections-script content. Where the use case touches collections, FDCPA reach and customer-facing accuracy are the conduct-overlay seams.

#### Mitigations the review should expect to see

Beyond the standard set:

- Retrieval-side role-based access aligned to the banking entitlement model. Per-customer or per-account scoping for any customer-facing or customer-handling assistant; the review confirms scope at the retrieval layer rather than only at the prompt layer.
- BSA/AML output filtering where the system contributes to alert disposition or SAR narratives; the BSA officer signs off on the filtering specification.
- Sanctions and OFAC name-screening on any output that could include third-party identifying information.
- UDAAP and consumer-disclosure-equivalent output filtering for any customer-facing communication generated or assisted by the system; the conduct overlay carries the broader framing.
- Foundation-model and vendor change-of-version notice and audit rights, captured in the third-party risk register and consistent with the June 2023 interagency guidance.

#### Monitoring signals the overlay adds

- AML alert-disposition anomaly where the system supports alert handling; escalation to the BSA officer.
- UDAAP-relevant output spot-check on customer-facing summaries or drafts; escalation to consumer compliance.
- Per-corpus retrieval-source distribution audit; sudden drift in the share of retrievals from one corpus is a leading indicator of either content-pipeline issue or query-distribution shift.
- For OCC large-bank scope (12 CFR Part 30 Appendix D), KRIs on faithfulness and citation precision rolling up to the chief risk executive function for risk-appetite-statement-relevant use cases.

#### Review-coordination considerations

- Where the use case is in OCC large-bank scope, the review records the connection to the bank's risk-appetite-statement framework and surfaces residual-risk acceptance to the chief risk executive function.
- Where the use case is vendor-hosted or relies on a foundation-model provider, the third-party risk register entry is updated to reference the RAG evaluation review and the foundation-model swap re-validation flag.
- Where the use case touches AML alert handling, the BSA officer co-signs the residual-risk acceptance and the programme-integrity-relevant residual risks.
- Where the use case is customer-facing, consumer compliance is in the room for the conduct overlay's UDAAP framing.

#### Common pitfalls specific to banking

- Treating a "compliance corpus" as a single source when it is in fact the policy library plus the regulatory-text database plus the BSA programme manual plus supervisory letter excerpts. Per-source enumeration is non-optional.
- Reporting a single global faithfulness number on an AML alert-triage use case where the alert types differ by typology and the failure mode varies. Segment-level reporting by alert type is required for AML-touching use cases.
- Asserting per-customer scoping at the prompt layer rather than the retriever layer. Prompt-layer scoping is bypassable; retrieval-layer scoping is the load-bearing control. The review confirms the layer at which the control sits.
- Not involving the BSA officer when the use case touches alert handling. An integrity issue with AI-assisted alert disposition is a BSA programme issue.
- Not refreshing the corpus-fitness assessment when the firm rolls out a major policy change. The policy library refresh-cadence question changes when the rate of policy change spikes.

## capital-markets

### Capital markets sector overlay for rag-evaluation-review

When the scope record names `capital-markets` as the sector, this overlay adds capital-markets-specific corpora considerations, mitigations, monitoring signals, and review-coordination expectations to the RAG evaluation review. Loaded by `rag-evaluation-review/SKILL.md` when `scope.sector_overlay_set` includes `capital-markets`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- SEC Investment Advisers Act Rule 206(4)-1 (Marketing Rule) and Rule 204-2 (Books and Records) for any AI-generated client-facing content from a registered investment adviser.
- SEC Regulation Analyst Certification (Reg AC) and FINRA Rule 2241 (Research) for research-assistant use cases.
- Market Abuse Regulation (MAR) for EU-touch capital-markets entities, particularly Articles 7 (inside information), 14 (insider dealing), and 15 (market manipulation), where retrieval over MNPI-adjacent corpora can create selective-disclosure or biased-retrieval exposure.
- SEC Rule 17a-4 and FINRA Rule 4511 (books and records preservation) for retained AI-generated outputs.
- SEC Reg BI (Regulation Best Interest) for broker-dealer client-facing content; SEC fiduciary-standard framing for adviser content.
- MiFID II Article 24 (information to clients) and product governance framing where applicable.
- SEC cyber disclosure rules (8-K Item 1.05 and Reg S-K Item 106) for public registrants where retrieval-driven exfiltration of MNPI could be a material cyber event; pointer to the cyber overlay.

#### Corpora typical of capital markets and the fitness considerations they raise

The recurring capital-markets RAG corpora and the fitness questions that bite:

- **Research notes and analyst content**: published research, internal research drafts, analyst commentary, target-price models. Sensitivity ranges across published (public) to internal-pre-publication (MNPI-adjacent). Reg AC and FINRA Rule 2241 framings apply where retrieval feeds research output. Coverage assessment keys off the research universe and the recency of the content.

- **Earnings-call transcripts and management-presentation materials**: vendor-supplied transcripts, internal call notes, management roadshow materials. Sensitivity is public for issued transcripts; internal-pre-publication for management materials carries MNPI risk. Provenance per source is the corpus-fitness spine.

- **Regulatory filings**: 10-K, 10-Q, 8-K, proxy filings, prospectus and offering documents, beneficial-ownership filings. Sensitivity is public. Coverage gaps on filings outside the firm's coverage universe are common; the gap goes in corpus-fitness, not retrieval-quality.

- **Trading and surveillance content**: trade blotters, order books, communication surveillance corpora (chat, email, voice transcripts). Sensitivity is confidential to MNPI-adjacent. Per-trader and per-desk scoping at retrieval is non-optional; surveillance-system retrieval is a separate use-case pattern with its own framing under Rule 17a-4 / FINRA 4511 records-preservation.

- **Client-portfolio content**: position data, allocation history, client documentation, advisory agreements, IPS documents. Sensitivity is confidential. Per-client scoping at retrieval is non-optional for adviser-facing or client-facing assistants.

- **Counterparty due-diligence and credit content**: counterparty profiles, credit memos, ISDA documentation, collateral agreements. Sensitivity is confidential.

#### Mitigations the review should expect to see

Beyond the standard set:

- Per-trader, per-desk, per-client retrieval scoping enforced at the retriever for trading-floor and client-facing assistants.
- MNPI segregation at the corpus level: pre-publication research, deal-team materials, and counterparty-MNPI corpora are separately indexed with information-barrier controls; retrieval-side enforcement of the information barrier is the load-bearing control. Where retrieval is permissioned across corpora, the information-barrier review is non-optional.
- Marketing Rule and books-and-records output controls for any AI-generated content reaching clients: the output is preserved per Rule 17a-4 / 204-2 and is reviewable against the Marketing Rule's general prohibitions before delivery.
- Reg AC certification framing for research-assistant outputs where the AI-generated content informs a published research report.
- Where the use case is bank-affiliated and in OCC large-bank scope, the cross-overlay banking framing applies.

#### Monitoring signals the overlay adds

- Per-corpus retrieval-source distribution audit with attention to MNPI-adjacent corpora; any retrieval from a barrier-protected corpus by an unauthorised user is an information-barrier event and an investigation trigger.
- Marketing Rule output-filter trip rate where AI-generated content reaches clients; escalation to compliance.
- Surveillance-system retrieval and citation precision where the system supports surveillance analyst work; misattributed surveillance findings are a programme-integrity issue.
- For research-assistant use cases, citation-precision sampling on regulatory and financial-document citations (a wrongly-cited filing in a research note is a Reg AC and conduct issue).

#### Review-coordination considerations

- The compliance officer (specifically the Marketing Rule reviewer for adviser-facing entities, the supervisory analyst for research entities) is a named co-reviewer for any client-facing or research-feeding use case.
- The information-barrier coordinator is a named co-reviewer where the corpus set spans permissioned and barrier-protected content.
- The CCO is a named co-acceptor for residual risk on Marketing Rule and Reg AC framings.
- For dual-registered entities (BD plus IA), both compliance functions co-review.
- For EU-touch entities, the MAR seam is named in the residual-risk section where retrieval over MNPI-adjacent corpora is in play.

#### Common pitfalls specific to capital markets

- Treating a "research corpus" as a single source when it is in fact published research plus internal pre-publication drafts plus vendor-supplied research. The MNPI-adjacency posture differs by source; per-source enumeration is non-optional.
- Asserting information-barrier enforcement at the prompt layer. The information barrier is structural; retrieval-layer enforcement is the load-bearing control. Prompt-layer enforcement is bypassable and is a finding.
- Reporting a single citation-precision number on a research-assistant use case where the citation types differ (regulatory filings, peer research, news, internal data). Segment-level reporting by citation type is required for research-feeding use cases.
- Omitting the supervisory analyst or the Marketing Rule reviewer from the reviewer attestation. Reg AC and Marketing Rule reach are co-acceptor framings, not background context.
- Not preserving AI-generated client-facing outputs per Rule 17a-4 / 204-2. Books-and-records preservation is a compliance gap, not a model gap; the recommended-action item names the records-management owner.
- Treating surveillance-system retrieval as the same use case as research retrieval. Surveillance use cases have their own evaluation framing and their own programme-integrity expectations.

## insurance

### Insurance sector overlay for rag-evaluation-review

When the scope record names `insurance` as the sector, this overlay adds insurance-specific corpora considerations, mitigations, monitoring signals, and review-coordination expectations to the RAG evaluation review. Loaded by `rag-evaluation-review/SKILL.md` when `scope.sector_overlay_set` includes `insurance`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023), AIS Program elements including testing-and-validation, third-party AI accountability, and documentation; binding only to the extent state DOIs adopt it (the NAIC AI Working Group state-adoption tracker is the public reference).
- HIPAA Privacy and Security Rules (45 CFR Parts 160 and 164) where the corpus contains PHI. Minimum-necessary at the retrieval layer is the load-bearing privacy control.
- State Insurance Data Security Model Law (NAIC Model 668), as adopted by domiciliary states.
- State unfair claims-settlement-practices acts and state insurance-fairness frameworks (e.g., Colorado Reg 10-1-1 on AI-driven external consumer data in life insurance underwriting; Connecticut Insurance Department guidance) for retrieval-driven decision-support use cases.
- Where the insurer is a registered investment adviser, the SEC overlay applies; this overlay does not duplicate that framing.

#### Corpora typical of insurance and the fitness considerations they raise

The recurring insurance RAG corpora and the fitness questions that bite:

- **Claim-file documents**: correspondence, medical records, prior summaries, adjuster notes, prior adjudication. Sensitivity is regulated-PHI for medical records; HIPAA minimum-necessary applies at retrieval. Per-claim scoping at the retriever is the load-bearing control. Provenance per document type is the corpus-fitness spine.

- **Policy documents (insurance policies)**: master policy wordings, endorsements, schedule pages, renewal letters. Sensitivity is confidential. Coverage gaps on legacy policy forms or jurisdiction-specific endorsements are common; coverage assessment by line of business and state is the right segmentation.

- **Underwriting content**: application data, third-party data feeds (motor vehicle records, prescription histories, credit-based insurance scoring inputs, ECDIS sources where applicable). Sensitivity ranges across confidential to regulated-PHI. State unfair-discrimination and state insurance-fairness frameworks apply where retrieval drives decision support; the conduct overlay carries the broader framing.

- **Medical records and clinical content**: clinical notes, lab reports, imaging reports, ICD-coded discharge summaries. Sensitivity is regulated-PHI; HIPAA minimum-necessary at retrieval is non-optional. OCR-driven retrieval is common on legacy medical records and the OCR confidence gate is load-bearing.

- **Loss-control and engineering reports (commercial lines)**: site inspection reports, loss-prevention recommendations, engineering surveys. Sensitivity is confidential. Provenance and retention-bound to the policy lifecycle.

- **Producer and broker correspondence**: emails, chat, meeting notes. Sensitivity is internal-to-confidential. Where the use case supports producer-facing assistants, conduct framing applies (producer training, suitability, sales-practice compliance).

#### Mitigations the review should expect to see

Beyond the standard set:

- Per-claim or per-policy retrieval scoping enforced at the retriever (HIPAA minimum-necessary mapping).
- OCR confidence threshold for any document type ingested via OCR, with a defined re-OCR or human-review path for sub-threshold documents.
- PHI handling controls aligned to HIPAA Security Rule technical safeguards (encryption at rest and in transit, audit logging on retrieval, access controls).
- State insurance-fairness output filtering where the use case drives decision support; the conduct overlay carries the framing.
- NAIC AIS Program documentation linkage: the RAG evaluation review's grounding evaluation and monitoring sections feed the AIS Program testing-and-validation and monitoring elements.

#### Monitoring signals the overlay adds

- Cross-claim or cross-policy leakage detection (rule-based detection on cross-scope ID surfaces in summary output); any confirmed event is a HIPAA-relevant incident and a privacy-overlay trigger.
- OCR confidence trend on PHI-containing documents; ingestion-pass-rate drift is a leading indicator of medical-record quality issues.
- Adjuster-edit rate or underwriter-edit rate as a downstream-acceptance signal; sustained increases indicate summary-quality drift.
- For decision-support use cases, fairness monitoring across protected-class proxies (segmentation of grounding-quality metrics by population), with annual reassessment at minimum.

#### Review-coordination considerations

- The privacy officer is a named co-reviewer for any PHI-containing corpus.
- The chief actuary or the head of underwriting is a named co-reviewer for any decision-support use case where retrieval feeds rate-, premium-, or coverage-relevant outputs.
- The NAIC AIS Program coordinator (where the firm has formalised AIS Program governance) consumes the RAG evaluation review as input to the testing-and-validation and monitoring elements.
- For multi-state insurers, the review notes the domiciliary-state binding posture on the NAIC Model Bulletin and any state-specific AI guidance (e.g., Colorado, Connecticut, New York) that applies.

#### Common pitfalls specific to insurance

- Asserting per-claim scoping at the prompt layer rather than the retriever layer for PHI corpora. The HIPAA minimum-necessary expectation is structural; prompt-layer scoping is bypassable.
- Treating OCR-driven retrieval miss as an OCR engineering issue rather than a corpus-fitness issue. The OCR confidence gate is part of the corpus-fitness control set; sub-threshold documents are corpus-incomplete documents.
- Reporting a single faithfulness number on a claims-summary use case spanning multiple lines of business (auto, life, disability, P&C). Segment-level reporting by line of business and claim type is required.
- Omitting the privacy officer from the reviewer attestation when the corpus contains PHI. The privacy officer co-signs the residual-risk acceptance.
- Not refreshing the retrieval-bias assessment with current policyholder demographic data ahead of annual revalidation for decision-support use cases. State insurance-fairness frameworks expect ongoing fairness monitoring, not a one-time baseline.
- Documenting the corpus as "claim file" without per-document-type provenance tagging. Medical records, correspondence, and adjuster notes carry different reliability postures; the corpus-fitness assessment loses the signal when they are rolled up.

## payments-fintech

### Payments and fintech sector overlay for rag-evaluation-review

When the scope record names `payments-fintech` as the sector, this overlay adds payments-and-fintech-specific corpora considerations, mitigations, monitoring signals, and review-coordination expectations to the RAG evaluation review. Loaded by `rag-evaluation-review/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- Joint Interagency Guidance on Third-Party Relationships (June 2023; OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023) and the BaaS-specific guidance from the agencies for sponsor-bank arrangements.
- Regulation E (12 CFR Part 1005) for consumer electronic fund transfers including dispute handling.
- Regulation Z (12 CFR Part 1026) and the CFPB credit-card and small-business-financing framings.
- CFPB UDAAP framework for consumer-facing communications.
- BSA/AML programme expectations applied to the fintech's BSA officer or to the sponsor bank's BSA officer per the responsibility allocation.
- GLBA Safeguards Rule (16 CFR Part 314) for non-bank fintech in FTC scope; pointer to the privacy overlay for the notification trigger.
- State money transmitter licensing and state-specific consumer protection where applicable.

#### Corpora typical of payments and fintech and the fitness considerations they raise

The recurring payments-and-fintech RAG corpora and the fitness questions that bite:

- **Terms-of-service, user agreements, fee schedules, disclosure documents**: customer-facing documents the assistant references when answering customer questions or drafting customer communications. Sensitivity is public-to-internal. Coverage assessment keys off currency (terms versions per effective date) and per-product completeness. Stale-content answers on a superseded ToS version are a UDAAP-relevant failure mode.

- **Dispute evidence**: dispute filings, supporting documents, prior disposition records, network rule references (card-network chargeback rules where applicable). Sensitivity is confidential. Per-dispute scoping at retrieval is non-optional. Provenance per document is the corpus-fitness spine.

- **Sponsor-bank policy and procedure**: the sponsor bank's BaaS policy, AML policy, consumer-protection policy, sanctions policy, change-of-version notice, audit reports. Sensitivity is confidential. Coverage assessment keys off the responsibility-allocation document between the fintech and the sponsor bank.

- **Customer interaction history**: support tickets, chat transcripts, prior dispute records, complaint records. Sensitivity is confidential, with NPI exposure. Per-customer scoping at retrieval is non-optional. Provenance per channel.

- **Compliance and risk content for the fintech itself**: AML rule documentation, sanctions screening results, transaction-monitoring case files. Sensitivity is confidential to MNPI-adjacent.

- **Vendor and partner content**: card-network rule documentation, processor documentation, KYC vendor documentation, identity-verification vendor outputs. Sensitivity is internal.

#### Mitigations the review should expect to see

Beyond the standard set:

- Per-customer, per-account, per-dispute retrieval scoping at the retriever for any customer-handling assistant.
- UDAAP-relevant output controls on customer-facing communications (drafts of dispute responses, account-related explanations, fee disclosures).
- Sponsor-bank shared-responsibility allocation explicit in the corpus-fitness section: which corpora are fintech-owned, which are sponsor-bank-owned, which are shared. The responsibility-allocation table from the BaaS arrangement is a reference document; the review confirms the corpora align.
- BSA/AML output controls where the use case supports alert-handling, KYC, or SAR work; the BSA officer (fintech-side or sponsor-bank-side per the allocation) signs off.
- Reg E dispute-handling framing where the use case touches consumer EFT disputes: the 10-business-day provisional-credit window and the 45/90-day investigation window are operational deadlines that the RAG output must support, not undermine. Hallucinated dispute facts are a Reg E and UDAAP issue.
- Card-network rule citations carry the same supports-the-claim definition as regulatory citations.

#### Monitoring signals the overlay adds

- UDAAP-relevant output spot-check on customer-facing summaries or drafts; escalation to consumer compliance.
- Reg E dispute-handling output check (does the assistant correctly state provisional-credit timing, investigation timing, recredit posture); escalation to consumer compliance plus operations.
- AML alert-disposition anomaly where the use case supports alert handling; escalation to the BSA officer per the allocation.
- Sponsor-bank corpus refresh-cadence monitoring; sponsor-bank policy changes that the fintech's RAG system has not absorbed are a programme-integrity issue.
- Customer-complaint-rate and complaint-code drift as a downstream-acceptance signal; complaint codes that map to RAG-output issues route to the AI risk committee.

#### Review-coordination considerations

- The sponsor bank's AI governance or model risk function is a named co-reviewer for BaaS arrangements. The responsibility-allocation document drives who signs off on what.
- The fintech's BSA officer (or the sponsor bank's per the allocation) is a named co-reviewer for any AML-touching use case.
- Consumer compliance is in the room for any customer-facing use case; the conduct overlay carries the broader framing.
- For state money-transmitter licensed entities, the state regulatory engagement function is a named co-reviewer where the use case touches money-transmission consumer protection.

#### Common pitfalls specific to payments and fintech

- Treating the sponsor-bank policy library and the fintech's own policy library as a single corpus. They are separately owned, separately refreshed, and the responsibility-allocation drives which one is authoritative on which topic. Per-source enumeration is non-optional.
- Asserting per-customer scoping at the prompt layer. Retrieval-layer scoping is the load-bearing control.
- Reporting a single faithfulness number on a customer-handling assistant where the question types differ (account inquiry, dispute inquiry, fee inquiry, product-feature inquiry). Segment-level reporting by question type is required.
- Omitting the sponsor-bank co-reviewer from the reviewer attestation. The shared-responsibility allocation is the operational framing; co-acceptance is the second-line manifestation.
- Reg E timing facts hallucinated as "general guidance" rather than precise statutory deadlines. Reg E timing is the canonical example of a fact the assistant cannot afford to get wrong; citation-precision on the relevant CFR sections is non-optional.
- Treating sponsor-bank corpus refresh cadence as the sponsor bank's problem. The fintech's RAG system carries the residual risk if the sponsor-bank policy change has not been absorbed.
