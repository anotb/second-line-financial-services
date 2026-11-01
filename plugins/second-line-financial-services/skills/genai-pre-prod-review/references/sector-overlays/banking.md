# Banking sector overlay for genai-pre-prod-review

When the scope record names `banking` as the sector, this overlay adds banking-specific gate considerations: named co-reviewers, additional notification triggers, sector-specific monitoring expectations, and recommended-action items typical of banking GenAI gate reviews. Loaded by `genai-pre-prod-review/SKILL.md` when `scope.sector_overlay_set` includes `banking`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- The joint interagency Revised Guidance on Model Risk Management (OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17 2026; supersedes SR 11-7 and SR 21-8) for traditional non-generative components in scope. The bulletin expressly excludes generative AI and agentic AI from its scope (footnote 3); for the GenAI use case itself the firm's model risk programme reaches it by analogy at firm policy level, and the pre-prod gate exercises the governance, validation, and documentation expectations the firm has elected to apply.
- Joint Interagency Guidance on Third-Party Relationships (June 2023; OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023) where the GenAI system is vendor-hosted or relies on a foundation-model provider.
- 12 CFR Part 30 Appendix D (OCC Heightened Standards) for OCC-supervised large banks where the GenAI use case sits inside a risk-appetite-statement-relevant function; the chief risk executive function signs the residual-risk acceptance.
- 12 CFR Part 53 (OCC), 12 CFR Part 225 Subpart N (FRB), 12 CFR Part 304 (FDIC) — the 36-hour banking computer-security incident notification rule (effective 2022).
- NYDFS 23 NYCRR Part 500 and the October 2024 AI Industry Letter for NY-footprint covered entities.
- FFIEC IT Examination Handbook, Information Security and AIO booklets, applied to the GenAI system's serving environment, change controls, and access controls.
- FFIEC BSA/AML Examination Manual where the use case touches AML alert handling, customer risk rating, KYC narrative drafting, or SAR drafting.

## Co-reviewers the gate review brings in

Beyond the standard sign-off set (AI Governance Lead, model risk lead, CISO function, compliance, privacy, legal):

- **BSA officer** for any use case touching AML alert handling, KYC, customer risk rating, or SAR narrative. The BSA officer evaluates programme-integrity exposure and signs the residual-risk acceptance for AML-touching items.
- **Consumer compliance** for any customer-facing or customer-handling use case; UDAAP exposure on AI-generated or AI-assisted customer communication is the seam.
- **Chief risk executive function** for OCC large-bank scope where the use case sits inside a risk-appetite-statement-relevant function; the residual risk surfaces to the chief risk executive per Heightened Standards.
- **Vendor management** for any vendor-hosted or foundation-model-dependent use case; the third-party risk register entry references the gate review and the foundation-model swap re-validation policy.

## Open conditions the overlay typically adds

- For OCC large-bank scope: documentation of the connection to the bank's risk-appetite-statement framework and named acceptance by the chief risk executive function.
- For BSA/AML-touching use cases: BSA officer co-signature on the residual-risk acceptance and on the monitoring-readiness section's AML-relevant signals (KYC narrative quality, alert-disposition-anomaly rate where applicable).
- For NY-footprint covered entities: NYDFS §500.17(a) notification-decision rehearsal as part of the IR drill scope.
- For vendor-hosted use cases: third-party risk register entry updated to reference the gate review and the foundation-model swap re-validation policy; vendor management co-signature.

## Monitoring signals the overlay expects to see live before go-live

In addition to the standard signal set:

- Per-customer retrieval audit signal where the architecture handles customer data; the signal must be live before go-live for any customer-handling use case.
- AML alert-disposition anomaly signal where the use case supports alert handling; escalation to the BSA officer.
- KYC narrative quality signal (citation precision on KYC source attributions, analyst-edit rate) where the use case supports KYC analysis; escalation to the BSA officer with model owner.
- Marketing Rule analogue output-filter trip rate where the use case is customer-facing communication and the institution carries dual registrations (joint trust company / RIA / BD); escalation to compliance.

## Incident-response triggers the overlay adds

In addition to the cyber-overlay-named triggers:

- 12 CFR Part 53 / Part 225 / Part 304 — the 36-hour banking computer-security incident notification rule. The bank notifies its primary federal regulator within 36 hours of determining a notification incident has occurred. Prompt-injection-driven or cross-customer-disclosure events causing material disruption, degradation, or actual harm to bank operations are within scope. The notification decision sits with the cyber and operational-resilience leads with general counsel.
- BSA/AML programme-integrity event triggers if the use case touches alert disposition, KYC narrative, or SAR drafting and the integrity of those outputs is in question; the BSA officer evaluates against the SAR continuing-activity reporting framework and against programme-integrity examination expectations.
- Consumer-protection event triggers if customer-facing AI output causes a UDAAP-relevant communication issue; consumer compliance evaluates.

The IR drill scope before go-live should exercise at minimum one banking-specific incident class (e.g., confirmed cross-customer information bleed for a customer-handling use case; KYC narrative integrity issue for a KYC use case; alert-disposition integrity issue for an AML use case).

## Recommended-action items the overlay surfaces

- Where the use case is in OCC large-bank scope, the residual-risk acceptance routes to the chief risk executive function and the connection to the risk-appetite statement is documented.
- Where the use case is vendor-hosted or relies on a foundation-model provider, the third-party risk register entry references the gate review and the foundation-model swap re-validation policy.
- Where the use case touches AML alert handling or KYC narrative drafting, the BSA officer co-signs and BSA-relevant monitoring signals are live before go-live.
- Where the use case is customer-facing in NY footprint, the NYDFS §500.17(a) notification-decision process is rehearsed against AI-specific incident scenarios as part of the IR drill scope.

## Common pitfalls specific to banking gate reviews

- Treating a vendor-hosted GenAI on a vendor-hosted foundation model as a single-vendor relationship. The vendor's foundation-model behaviour shift is a third-party event and a cyber event; the third-party risk register and the cyber overlay both bind.
- Omitting the 36-hour banking computer-security incident notification rule. It is distinct from the NYDFS 72-hour notice and from the SEC 8-K four-business-day disclosure; all three can apply concurrently for a single material event in a NY-footprint public-registrant bank.
- Failing to involve the BSA officer when the use case touches alert handling, KYC, or SAR drafting; an integrity issue with AI-assisted alert disposition or AI-assisted KYC narrative is a BSA programme issue, not just a model-risk issue.
- Treating the chief risk executive role under 12 CFR Part 30 Appendix D as out-of-scope for AI use cases. AI use cases inside risk-appetite-relevant functions are within the Heightened Standards seam; the residual-risk acceptance routes accordingly.
- Recording vendor SOC 2 or vendor system card as substituting for firm-side gate evidence. Vendor evidence is a foundation, not a substitute; the gate review records vendor evidence at vendor-self-attestation confidence and the firm-side gate items are firm-side responsibilities.
