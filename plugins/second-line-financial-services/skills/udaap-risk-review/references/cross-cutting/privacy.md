# Privacy cross-cutting overlay for udaap-risk-review

This overlay is secondary on this skill. It loads when the in-scope flow processes NPI in a way that itself raises a UDAAP angle: a deceptive privacy disclosure, a dark-pattern privacy-consent flow, a fee mechanic tied to privacy-permission state, a data-sharing arrangement that misleads the consumer, or an AI-driven personalisation that materially relies on consumer data the consumer believes is restricted.

Loaded by: `udaap-risk-review/SKILL.md` when `scope.cross_cutting_set` includes `privacy` or when the in-scope fact pattern touches a privacy-meets-UDAAP angle. Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for privacy-flagged UDAAP review memos

### 1. Privacy-meets-UDAAP fact patterns

The recurring intersections:

- *Deceptive privacy disclosure.* The privacy notice or in-product privacy disclosure represents data-handling practices in a way that is materially inconsistent with the actual practice. Element analysis: deception (representation likely to mislead; reasonable consumer; materiality); the actual data-handling practice is the omitted or contradicted truth.
- *Dark-pattern privacy-consent flow.* The consent flow uses choice-architecture design that materially interferes with the consumer's ability to make a privacy-related choice (defaults, friction, asymmetric framing, repeated re-prompting). Element analysis: abusiveness (material interference) plus deception where the framing misleads.
- *Fee mechanic tied to privacy-permission state.* A fee, credit decision, or service tier varies with the consumer's privacy permissions in a way that is not adequately disclosed, or in a way the consumer cannot reasonably avoid, or in a way that takes unreasonable advantage of the consumer's reliance on the firm. Element analysis spans all three prongs depending on the specifics.
- *Data-sharing or sub-processor arrangement misleading the consumer.* The firm shares consumer data with a sub-processor or partner in a way that is not adequately disclosed or that the consumer cannot reasonably avoid. Element analysis: deception primarily; unfairness where the data-sharing produces substantial injury (e.g., downstream targeting, unrelated marketing, identity-resolution against the consumer).
- *AI-driven personalisation materially relying on restricted data.* Personalised pricing, retention offers, or risk decisions rely on consumer data the consumer believes is restricted to a specific purpose; the algorithmic outcome surfaces the data in a way that misleads or takes unreasonable advantage. Element analysis ties to the AI / algorithmic-discrimination block in the main flow.

### 2. GLBA Safeguards posture as a contextual control

The Safeguards Rule (16 CFR Part 314 for FTC-supervised; 12 CFR Part 30 Appendix B for OCC; 12 CFR Part 364 Appendix B for FDIC) sets the firm's information-security program for NPI. The UDAAP memo does not finalise GLBA findings; it records the GLBA posture as context. Where the in-scope fact pattern interacts with GLBA-protected NPI, the memo:

- Names the data classification involved (NPI per GLBA; PHI per HIPAA where applicable; PCI; CCPA-defined personal information; state-specific categories).
- Notes whether the firm's information-security program is operating against the data flow at issue (e.g., whether the data-sharing arrangement at issue carries an appropriate sub-processor contract, vendor diligence, and DPA).
- Cross-references `vendor-diligence` (in `third-party-operational-resilience`) where the in-scope fact pattern involves a third-party vendor handling consumer data.

### 3. State-privacy-law footprint

Where the firm operates in a state-privacy-law footprint (CCPA / CPRA, VCDPA, CTDPA, and the rolling roster of state laws), the customer-rights workflow (right to know, right to delete, right to limit, right to correct) reaches the data implicated in the in-scope flow. The UDAAP memo records:

- Whether the in-scope flow is subject to a customer-rights request received during the review period.
- Whether the firm's state-privacy-law obligations are aligned with the disclosures and the consumer-journey design at issue.
- Whether a state-privacy-law angle (e.g., dark-pattern prohibition under CCPA / CPRA) supports the deception or abusiveness analysis under federal UDAAP.

### 4. Privacy-disclosure consistency

A recurring failure mode: the privacy notice promises one thing, the consumer-experience flow does another, the marketing copy implies a third. The UDAAP memo reads the privacy disclosure against the actual flow:

- Privacy notice text vs. observed data flow.
- In-product privacy controls vs. observed default state.
- Marketing copy vs. privacy notice (cross-reference `marketing-claim-review` for asset-level marketing-claim review).
- AI-driven communication vs. privacy disclosure (cross-reference any AI-governance review of the in-scope model).

### 5. AI personalisation and prompt-as-customer-data lens

Where the in-scope flow includes an AI surface (conversational AI, agentic flow, AI-driven communication scheduling, AI-personalised disclosure), consumer prompts and contextual signals to the AI are themselves customer data. The UDAAP memo records:

- Whether the AI-vendor contract addresses use of customer prompts (training, fine-tuning, model improvement, abuse monitoring).
- Whether the disclosure to the consumer addresses prompt-as-customer-data handling.
- Whether the AI personalisation surfaces consumer data in a way that materially interferes with the consumer's understanding (abusiveness) or misleads (deception).

The memo does not duplicate AI-vendor evidence review (chain to `llm-vendor-evidence-review` in `ai-governance-model-risk`); it records the UDAAP read at the consumer surface.

## Privacy-specific memo template additions

The following fields are added to the memo when the privacy overlay loads:

- `privacy_intersection_type` — enum (`deceptive-privacy-disclosure`, `dark-pattern-privacy-consent`, `fee-tied-to-privacy-state`, `data-sharing-misleading`, `ai-personalisation-on-restricted-data`, `other`).
- `data_classification_involved[]` — list of data classifications implicated (NPI, PHI, PCI, state-personal-information categories).
- `state_privacy_law_footprint[]` — list of state laws applicable to the in-scope flow.
- `privacy_disclosure_consistency_finding` — string describing the consistency or inconsistency between the privacy notice, the in-product flow, and the marketing copy.
- `ai_prompt_as_customer_data_finding` — string where AI is in the in-scope flow.
- `cross_reference_skills[]` — extends to include `vendor-diligence`, `marketing-claim-review`, `llm-vendor-evidence-review` where the privacy intersection invokes those.

## Common pitfalls in privacy-flagged UDAAP review memos

- Treating privacy as a separate review track and producing a UDAAP memo that does not address the privacy-meets-UDAAP angle even where it is in the fact pattern; the consumer does not perceive the regimes as separate.
- Reading the privacy notice in isolation from the consumer-experience flow; the gap between notice and flow is the recurring source of the deception finding.
- Defaulting to "the firm is GLBA-compliant" as a UDAAP defence; GLBA compliance is necessary but not sufficient; the UDAAP element tests reach the consumer-facing representation and the consumer-journey design.
- Treating dark-pattern design as a UX problem rather than as an abusiveness or deception angle; the bureau and the FTC have both pursued dark-pattern fact patterns under existing UDAAP / UDAP authority.
- Missing the state-privacy-law overlay where the firm operates in a CCPA / CPRA or similar footprint; the state regime can both support the federal UDAAP analysis and trigger separate state-AG attention.
- Treating consumer prompts to AI surfaces as routine telemetry; they are customer data and they raise their own UDAAP and privacy questions when the AI vendor's contract is open on training-data use.
- Conflating privilege posture across the privacy and UDAAP review tracks; the artifacts overlap but the privilege framework is set per artifact.
