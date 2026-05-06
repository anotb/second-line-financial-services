# Banking sector overlay for rag-evaluation-review

When the engagement-scope record names `banking` as the sector, this overlay adds banking-specific corpora considerations, mitigations, monitoring signals, and review-coordination expectations to the RAG evaluation review. Loaded by `rag-evaluation-review/SKILL.md` when `engagement_scope.sector_overlay_set` includes `banking`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- FFIEC IT Examination Handbook, Information Security and AIO booklets, applied to the data-integrity controls on retrieval corpora and to the retrieval-side access enforcement.
- Joint Interagency Guidance on Third-Party Relationships (June 2023; OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023) where the corpus is vendor-supplied or the foundation model is vendor-hosted.
- SR 11-7 / OCC Bulletin 2026-13 model risk framing where the bank's model risk programme treats the GenAI use case as in scope. The validation expectations on data-review and outcomes-analysis apply to retrieval corpora and grounding outputs.
- FFIEC BSA/AML Examination Manual where the use case touches AML alert handling, customer risk rating, or SAR drafting.
- 12 CFR Part 30 Appendix D (OCC Heightened Standards) for OCC-supervised large banks where the use case sits inside a risk-appetite-statement-relevant function.

## Corpora typical of banking and the fitness considerations they raise

The recurring banking RAG corpora and the fitness questions that bite:

- **Customer relationship management (CRM)**: client interaction history, meeting notes, emails, chat. Sensitivity is internal-to-confidential; provenance is firm-controlled but content originates externally (client-supplied content can carry adversarial instructions, see `prompt-injection-risk` for the focused review). Coverage assessment for relationship-manager use cases keys off the CRM's currency and the relationship-team's discipline on note capture.

- **Compliance policy library**: firm policies, procedures, standards, and supporting materials. Sensitivity is confidential; provenance is firm-controlled with named owners and approval workflow. Freshness is the first-order question: a quarterly refresh cycle with a known post-effective-date lag is the common pattern, and the lag is a real residual risk (stale-policy answer). Coverage gaps on adjacent document sets (BSA programme manual, code of conduct, vendor management policy) are common where the policy library does not house all firm rules.

- **Regulatory text**: vendor-supplied federal banking regulations, supervisory guidance, agency publications. Sensitivity is public; provenance is vendor-tagged. Coverage gaps on state-level guidance, CFPB Circulars, or supervisory letters not in the vendor's set are common; the gap goes in the corpus-fitness assessment, not in retrieval-quality.

- **AML alert narratives, customer risk profiles, transaction-monitoring system output, sanctions-screening hits, third-party intelligence feeds**: the AML alert-triage and KYC/EDD use cases. Sensitivity ranges across confidential to MNPI-adjacent. Provenance is mixed (system-generated, analyst-authored, vendor-supplied). The BSA officer is a co-reviewer where the use case touches alert disposition, and BSA programme-integrity expectations apply to the grounding evaluation: a hallucination on an AML alert narrative is a programme issue, not a model issue.

- **Treasury-management and payments operations content**: client cash-management profiles, payment-pattern documentation, fraud-rule documentation. Sensitivity is confidential; sanctions and OFAC screening on outputs that include third-party identifying information is the load-bearing output filter.

- **Credit and collections content**: credit policy, account-status documentation, collections-script content. Where the use case touches collections, FDCPA reach and customer-facing accuracy are the conduct-overlay seams.

## Mitigations the review should expect to see

Beyond the standard set:

- Retrieval-side role-based access aligned to the banking entitlement model. Per-customer or per-account scoping for any customer-facing or customer-handling assistant; the review confirms scope at the retrieval layer rather than only at the prompt layer.
- BSA/AML output filtering where the system contributes to alert disposition or SAR narratives; the BSA officer signs off on the filtering specification.
- Sanctions and OFAC name-screening on any output that could include third-party identifying information.
- UDAAP and consumer-disclosure-equivalent output filtering for any customer-facing communication generated or assisted by the system; the conduct overlay carries the broader framing.
- Foundation-model and vendor change-of-version notice and audit rights, captured in the third-party risk register and consistent with the June 2023 interagency guidance.

## Monitoring signals the overlay adds

- AML alert-disposition anomaly where the system supports alert handling; escalation to the BSA officer.
- UDAAP-relevant output spot-check on customer-facing summaries or drafts; escalation to consumer compliance.
- Per-corpus retrieval-source distribution audit; sudden drift in the share of retrievals from one corpus is a leading indicator of either content-pipeline issue or query-distribution shift.
- For OCC large-bank scope (12 CFR Part 30 Appendix D), KRIs on faithfulness and citation precision rolling up to the chief risk executive function for risk-appetite-statement-relevant use cases.

## Review-coordination considerations

- Where the use case is in OCC large-bank scope, the review records the connection to the bank's risk-appetite-statement framework and surfaces residual-risk acceptance to the chief risk executive function.
- Where the use case is vendor-hosted or relies on a foundation-model provider, the third-party risk register entry is updated to reference the RAG evaluation review and the foundation-model swap re-validation flag.
- Where the use case touches AML alert handling, the BSA officer co-signs the residual-risk acceptance and the programme-integrity-relevant residual risks.
- Where the use case is customer-facing, consumer compliance is in the room for the conduct overlay's UDAAP framing.

## Common pitfalls specific to banking

- Treating a "compliance corpus" as a single source when it is in fact the policy library plus the regulatory-text database plus the BSA programme manual plus supervisory letter excerpts. Per-source enumeration is non-optional.
- Reporting a single global faithfulness number on an AML alert-triage use case where the alert types differ by typology and the failure mode varies. Segment-level reporting by alert type is required for AML-touching use cases.
- Asserting per-customer scoping at the prompt layer rather than the retriever layer. Prompt-layer scoping is bypassable; retrieval-layer scoping is the load-bearing control. The review confirms the layer at which the control sits.
- Not involving the BSA officer when the use case touches alert handling. An integrity issue with AI-assisted alert disposition is a BSA programme issue.
- Not refreshing the corpus-fitness assessment when the firm rolls out a major policy change. The policy library refresh-cadence question changes when the rate of policy change spikes.
