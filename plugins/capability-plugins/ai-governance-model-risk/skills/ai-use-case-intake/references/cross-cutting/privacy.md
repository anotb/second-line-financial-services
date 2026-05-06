# Privacy cross-cutting overlay for ai-use-case-intake

When the engagement-scope record flags `privacy` for the use case, this overlay supplies the privacy-specific intake fields and the named flags that route into downstream tier, model-card, and validation work. Privacy in financial services has both a federal regime (GLBA Safeguards Rule, HIPAA where applicable) and a state regime (state privacy laws and state insurance privacy rules); the intake captures the fields each regime needs at intake.

Loaded by: `ai-use-case-intake/SKILL.md` when `engagement_scope.cross_cutting_set` includes `privacy`. Source-anchored in `references/source-anchors.md`.

## Source basis

- GLBA Safeguards Rule (16 CFR Part 314) — applies to non-public personal information (NPI) held by financial institutions.
- HIPAA Privacy Rule (45 CFR Part 160 and Part 164 Subpart E) and Security Rule (Subpart C) — applies to protected health information (PHI) held by covered entities and business associates.
- Reg P (12 CFR Part 1016) — privacy notice and opt-out for consumer NPI.
- State privacy laws applying to financial-services entities: California Consumer Privacy Act (CCPA) as amended by CPRA, Virginia CDPA, Colorado CPA, Connecticut CTDPA, Utah UCPA, and others. Most state privacy laws carve out GLBA-covered data; intake distinguishes regulated NPI (GLBA-covered) from non-GLBA-covered consumer data.
- State insurance privacy rules (NAIC Model #672 Insurance Information and Privacy Protection Model Act, where adopted) — adoption status varies by state.

## Privacy-specific intake fields

In addition to the capability intake spine, the privacy overlay adds the following:

- Field-level data sensitivity tagging for any data source flagged regulated NPI, regulated PHI, regulated PCI, biometric, or children's data. A "CRM extract" source labelled "internal" hides regulated NPI inside an aggregate source; the intake requires the field-level breakout for any source flagged regulated.
- Consumer notice posture: whether the firm's privacy notice (Reg P) and any state-law notice cover the AI use case, or whether a notice update is required.
- Sensitive-attribute use: any attributes the model uses, learns from, or infers that are sensitive under federal or state law (race, ethnicity, religion, sexual orientation, health status, immigration status, biometric identifiers, precise geolocation). Each named with the use posture (input, training feature, inferred output).
- Sub-processor and vendor PII flow: any vendor receiving NPI or PHI, with the BAA (HIPAA) or written-contract (GLBA / state law) posture noted.
- Data residency: where the data is stored, processed, and transmitted, with cross-border transfer noted where applicable.
- Retention posture: how long the data is retained, the deletion mechanism, and the firm-side process for honoring deletion requests under state privacy laws (where applicable).

## Privacy-specific regulatory flags

When the privacy overlay is loaded, the intake's regulatory-flags table picks up:

- `GLBA_Safeguards` (where any data source is regulated NPI) with routing to `ai-risk-tiering` and `validation-plan`.
- `HIPAA` (where any data source is regulated PHI) with routing to `ai-risk-tiering` and `validation-plan`.
- `Reg_P` (consumer NPI subject to privacy notice and opt-out) with routing to `model-card-builder` for the consumer-notice posture.
- `CCPA_CPRA` and other state privacy laws as applicable (most exempt GLBA-covered data, but cover non-GLBA consumer data the firm holds).
- `NAIC_Model_672` for insurance entities in adopting states.

## Privacy-specific open questions for downstream skills

The intake routes the following open questions when relevant:

- For `validation-plan`: how is sensitive-attribute use validated against the firm's privacy-impact-assessment posture, and how is inferred-attribute risk (where the model infers a sensitive attribute even when not given as input) tested.
- For `model-card-builder`: what is the consumer-notice posture for this use case (Reg P, state-law notice, sector-specific bulletin where applicable), and where does it sit in the privacy-notice update cycle.
- For `vendor-diligence`: BAA / written-contract status for any vendor receiving NPI or PHI; sub-processor flow-down evidence.
- For `agentic-ai-controls`: where the use case has tool privileges that read or write personal data, what controls limit personal-data scope of the tool actions.
- For privacy function review: data-residency posture and cross-border transfer mechanism (where applicable); deletion mechanism for state-privacy-law deletion requests.

## Common pitfalls in privacy-flagged intake

- Source-level sensitivity tagging without field-level breakout. A regulated source typically contains a mix of regulated and non-regulated fields; the intake needs the field-level breakout to support data-sensitivity tiering and the privacy-impact-assessment downstream.
- Treating GLBA NPI as covering all consumer data the firm holds. Many state privacy laws apply to consumer data the firm holds in a non-GLBA capacity (employee data, marketing prospect data, B2B contact data); intake should reflect both regimes when both apply.
- Missing the inferred-attribute question. A model that does not take race or ethnicity as input may still infer them from proxies; the privacy-flagged intake records this as an open question for `validation-plan` rather than treating absence-of-input as absence-of-exposure.
- Skipping the BAA / written-contract status for vendors. The intake captures the vendor with role and criticality; the contract-status question routes to `vendor-diligence`, but the vendor presence with PHI or NPI flow is the intake fact.
- Recording a HIPAA-touch use case without the field-level PHI tagging. Life and health insurance underwriting AI using prescription-history data is the canonical case; "uses prescription data" is not enough, the intake needs the field categories.
- Recording a use case using biometric data without flagging children's data exposure separately. Biometric is one regulated category; children's data (under COPPA, state laws) is another; the intake distinguishes them.
