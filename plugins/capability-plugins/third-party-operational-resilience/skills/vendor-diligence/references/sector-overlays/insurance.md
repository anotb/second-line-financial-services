# Insurance sector overlay — vendor-diligence

When the scope flags insurance, load this overlay alongside `references/source-anchors.md`. The insurance overlay carries what the bank-flavoured capability skill does not.

## Vendor types specific to insurance

The diligence must recognise the insurance-specific vendor population: managing general agent (MGA), managing general underwriter (MGU), third-party administrator (TPA), claims administrator, underwriting bureau, actuarial outsourcer, IT outsourcer, AI / ML vendor, ECDIS data provider, illustration-software vendor. Each pulls a different model-law set into the diligence.

## Operative model laws

- **NAIC Insurance Holding Company System Regulatory Act (Model #440)** [verify model number] and **Holding Company Model Regulation (Model #450)** [verify model number]: Form B and Form D filings where the vendor is an affiliate of the carrier. This is not a federal-banking concept; the bank-flavoured generic skill misses it.
- **NAIC Insurance Data Security Model Law (Model #668), §4.F third-party service-provider obligations**: due-diligence, written-contract terms, monitoring, incident-response cooperation, breach-notification chain. Distinct from federal interagency-guidance third-party expectations. Adoption is state-by-state; the NAIC adoption tracker is the public reference.
- **NAIC Producer Licensing Model Act** [verify model number]: any vendor exercising binding or producer authority requires per-state producer licensing. The diligence checklist must include a per-state licensing confirmation for any vendor that quotes, binds, services, or sells.
- **NAIC Unfair Trade Practices Act (Model #880)** and the carrier's state-by-state unfair-claims-settlement-practices acts: where the vendor sits in a claims process, the standards apply regardless of who actually executes the claim decision.
- **State Department of Insurance bulletins** on specific outsourced functions where the carrier is licensed; pin the bulletins by state and date.

## ORSA fit

- **NAIC Risk Management and Own Risk and Solvency Assessment Model Act (Model #505)** [verify model number]: critical outsourced functions belong in the ORSA Summary Report. The diligence pack must call out ORSA-fit as a named status. Materiality is carrier-specific; the diligence consumes the carrier's ORSA materiality threshold and applies it.

## AI vendor mode at an insurer

When `ai_vendor=true` and the firm is an insurer:

- **NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023)**: the carrier remains accountable for vendor and third-party AI used on its policies. AIS Program elements (governance, risk management, testing, validation, third-party-AI accountability, monitoring, documentation, transparency, fairness) apply to the vendor through the carrier. Adoption is state-by-state; consult the NAIC AI Working Group adoption tracker.
- **State DOI AI bulletins**: Colorado SB 21-169 implementing regulation (life-insurance underwriting); NY DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting (January 2024) [verify exact circular number]; California DOI bulletin on AI use in insurance [verify exact bulletin]. Each has its own scoping (life-only in CO and NY; broader in CA); pin by state.
- **HIPAA Privacy and Security Rules** apply where the AI touches PHI (health-claims AI, life-and-health underwriting AI using prescription-history or medical data). HIPAA business-associate posture must be evidenced.
- **Producer / agent licensing**: any consumer-facing AI that takes actions on policies (binding, quoting commitments, surrendering, paying claims) can trigger producer licensing questions. Flag for the licensing function.
- **EU AI Act extraterritoriality**: insurance pricing and risk-assessment in life and health is named as a high-risk use case under Annex III of Regulation (EU) 2024/1689. US carriers writing in EU branches or doing reinsurance with EU cedents can inherit the obligation.
- **NIST AI RMF 1.0** Govern function for AI vendors; **NIST AI 600-1** for GenAI vendors.

Cross-link to `ai-governance-model-risk/llm-vendor-evidence-review` via `ai_specific_findings.eval_evidence_status = deferred-to-evidence-review` for the deeper evidence-pack review.

## Cyber sub-overlay

- **NAIC Insurance Data Security Model Law (Model #668)** is the insurance-specific cybersecurity frame. Where adopted, it applies in addition to or in some states instead of NYDFS Part 500. §4.F third-party-service-provider obligations carry the cyber expectation chain to the vendor and its sub-processors. Incident-response cooperation language has to be in the contract; this is a frequent gap.

## Cross-link inside the plugin

- **`exit-plan` insurance overlay** carries TPA / claims-administrator transition mechanics, ORSA notification, and policyholder-communication responsibilities.
- **`contract-gap-review` insurance overlay** carries Model #668 §4.F clauses, HIPAA BAA terms, NAIC Bulletin Dec 2023 third-party-AI accountability clauses, and the producer-licensing representation set.
- **`concentration-risk-review`**: TPA, reinsurance, and claims-AI vendor concentration feed the insurance-overlay concentration calculation.

## Output-template additions for insurance

- Vendor-type-by-applicable-Model crosswalk row: which NAIC Model applies to this vendor type.
- Per-state producer-licensing confirmation table where the vendor exercises producer authority.
- HIPAA business-associate posture as a named line.
- ORSA-fit status as a named line.
- AIS Program element-by-element status when `ai_vendor=true`.
- Form B / Form D applicability check when the vendor is an affiliate.

## Common pitfalls in insurance vendor diligence

- Applying federal banking guidance and skipping NAIC Model #668 §4.F.
- Missing the per-state producer-licensing confirmation.
- Treating the NAIC AI Bulletin as US-uniform when adoption is state-by-state.
- Skipping the HIPAA business-associate analysis on a "tech vendor" that incidentally touches PHI.
- Missing the ORSA-fit assessment and only producing a third-party-risk-forum-grade pack when the vendor is enterprise-material.
