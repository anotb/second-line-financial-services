# Payments and fintech sector overlay for rag-evaluation-review

When the scope record names `payments-fintech` as the sector, this overlay adds payments-and-fintech-specific corpora considerations, mitigations, monitoring signals, and review-coordination expectations to the RAG evaluation review. Loaded by `rag-evaluation-review/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- Joint Interagency Guidance on Third-Party Relationships (June 2023; OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023) and the BaaS-specific guidance from the agencies for sponsor-bank arrangements.
- Regulation E (12 CFR Part 1005) for consumer electronic fund transfers including dispute handling.
- Regulation Z (12 CFR Part 1026) and the CFPB credit-card and small-business-financing framings.
- CFPB UDAAP framework for consumer-facing communications.
- BSA/AML programme expectations applied to the fintech's BSA officer or to the sponsor bank's BSA officer per the responsibility allocation.
- GLBA Safeguards Rule (16 CFR Part 314) for non-bank fintech in FTC scope; pointer to the privacy overlay for the notification trigger.
- State money transmitter licensing and state-specific consumer protection where applicable.

## Corpora typical of payments and fintech and the fitness considerations they raise

The recurring payments-and-fintech RAG corpora and the fitness questions that bite:

- **Terms-of-service, user agreements, fee schedules, disclosure documents**: customer-facing documents the assistant references when answering customer questions or drafting customer communications. Sensitivity is public-to-internal. Coverage assessment keys off currency (terms versions per effective date) and per-product completeness. Stale-content answers on a superseded ToS version are a UDAAP-relevant failure mode.

- **Dispute evidence**: dispute filings, supporting documents, prior disposition records, network rule references (card-network chargeback rules where applicable). Sensitivity is confidential. Per-dispute scoping at retrieval is non-optional. Provenance per document is the corpus-fitness spine.

- **Sponsor-bank policy and procedure**: the sponsor bank's BaaS policy, AML policy, consumer-protection policy, sanctions policy, change-of-version notice, audit reports. Sensitivity is confidential. Coverage assessment keys off the responsibility-allocation document between the fintech and the sponsor bank.

- **Customer interaction history**: support tickets, chat transcripts, prior dispute records, complaint records. Sensitivity is confidential, with NPI exposure. Per-customer scoping at retrieval is non-optional. Provenance per channel.

- **Compliance and risk content for the fintech itself**: AML rule documentation, sanctions screening results, transaction-monitoring case files. Sensitivity is confidential to MNPI-adjacent.

- **Vendor and partner content**: card-network rule documentation, processor documentation, KYC vendor documentation, identity-verification vendor outputs. Sensitivity is internal.

## Mitigations the review should expect to see

Beyond the standard set:

- Per-customer, per-account, per-dispute retrieval scoping at the retriever for any customer-handling assistant.
- UDAAP-relevant output controls on customer-facing communications (drafts of dispute responses, account-related explanations, fee disclosures).
- Sponsor-bank shared-responsibility allocation explicit in the corpus-fitness section: which corpora are fintech-owned, which are sponsor-bank-owned, which are shared. The responsibility-allocation table from the BaaS arrangement is a reference document; the review confirms the corpora align.
- BSA/AML output controls where the use case supports alert-handling, KYC, or SAR work; the BSA officer (fintech-side or sponsor-bank-side per the allocation) signs off.
- Reg E dispute-handling framing where the use case touches consumer EFT disputes: the 10-business-day provisional-credit window and the 45/90-day investigation window are operational deadlines that the RAG output must support, not undermine. Hallucinated dispute facts are a Reg E and UDAAP issue.
- Card-network rule citations carry the same supports-the-claim definition as regulatory citations.

## Monitoring signals the overlay adds

- UDAAP-relevant output spot-check on customer-facing summaries or drafts; escalation to consumer compliance.
- Reg E dispute-handling output check (does the assistant correctly state provisional-credit timing, investigation timing, recredit posture); escalation to consumer compliance plus operations.
- AML alert-disposition anomaly where the use case supports alert handling; escalation to the BSA officer per the allocation.
- Sponsor-bank corpus refresh-cadence monitoring; sponsor-bank policy changes that the fintech's RAG system has not absorbed are a programme-integrity issue.
- Customer-complaint-rate and complaint-code drift as a downstream-acceptance signal; complaint codes that map to RAG-output issues route to the AI risk committee.

## Review-coordination considerations

- The sponsor bank's AI governance or model risk function is a named co-reviewer for BaaS arrangements. The responsibility-allocation document drives who signs off on what.
- The fintech's BSA officer (or the sponsor bank's per the allocation) is a named co-reviewer for any AML-touching use case.
- Consumer compliance is in the room for any customer-facing use case; the conduct overlay carries the broader framing.
- For state money-transmitter licensed entities, the state regulatory engagement function is a named co-reviewer where the use case touches money-transmission consumer protection.

## Common pitfalls specific to payments and fintech

- Treating the sponsor-bank policy library and the fintech's own policy library as a single corpus. They are separately owned, separately refreshed, and the responsibility-allocation drives which one is authoritative on which topic. Per-source enumeration is non-optional.
- Asserting per-customer scoping at the prompt layer. Retrieval-layer scoping is the load-bearing control.
- Reporting a single faithfulness number on a customer-handling assistant where the question types differ (account inquiry, dispute inquiry, fee inquiry, product-feature inquiry). Segment-level reporting by question type is required.
- Omitting the sponsor-bank co-reviewer from the reviewer attestation. The shared-responsibility allocation is the operational framing; co-acceptance is the second-line manifestation.
- Reg E timing facts hallucinated as "general guidance" rather than precise statutory deadlines. Reg E timing is the canonical example of a fact the assistant cannot afford to get wrong; citation-precision on the relevant CFR sections is non-optional.
- Treating sponsor-bank corpus refresh cadence as the sponsor bank's problem. The fintech's RAG system carries the residual risk if the sponsor-bank policy change has not been absorbed.
