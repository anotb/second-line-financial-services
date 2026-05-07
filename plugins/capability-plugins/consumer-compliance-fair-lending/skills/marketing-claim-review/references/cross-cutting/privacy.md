# Privacy cross-cutting overlay for marketing-claim-review

This overlay loads on every digital-channel review because privacy-claim accuracy, AdChoices representation, dark-pattern privacy, and state-privacy-law interaction are recurring asset-level findings. Where the marketing surface is broadcast or print only and includes no privacy-claim or privacy-disclosure element, the overlay can be skipped; in practice, almost every modern campaign has a digital-channel asset and the overlay applies.

Loaded by: `marketing-claim-review/SKILL.md` when `engagement_scope.cross_cutting_set` includes `privacy` or when any digital-channel asset is in scope. Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for privacy-flagged marketing-review memos

### 1. Privacy-claim accuracy under GLBA Privacy Rule and Regulation P

For every on-asset privacy claim ("we will never sell your data"; "your data is safe with us"; "we don't share with third parties"; "you control how your data is used"; "we use bank-level encryption"), the asset-level review reads the claim against:

- The firm's GLBA / Reg P privacy notice (the §1016.6 content-required notice).
- The firm's actual data-handling practice as evidenced by privacy-program documentation, vendor contracts, sub-processor lists, and (where available) data-flow diagrams.
- The firm's state-privacy-law disclosures (CCPA / CPRA Notice at Collection; equivalent state-law notices) where the firm operates in those footprints.

Where the on-asset claim is materially inconsistent with the privacy notice or the actual practice, the finding is deception under §1031 (or under FTC Act §5 for FTC-jurisdictional entities). The recurring failure mode is the gap between the marketing voice ("we will never sell your data") and the legal voice (the firm's CCPA notice that discloses "share for cross-context behavioral advertising"); CCPA / CPRA's broader "share" definition is not what the marketing voice means by "sell" but is the operative state-law term.

### 2. AdChoices and DAA self-regulatory representation

Where the firm participates in the Digital Advertising Alliance program (the AdChoices icon program; the DAA AppChoices for mobile), the on-asset representation of program participation must be consistent with actual practice. The asset-level review reads:

- Whether the AdChoices icon is present where required (DAA Self-Regulatory Principles).
- Whether the consumer-choice mechanism is operational and reaches the asserted scope.
- Whether the data-collection-and-use disclosures in the asset and in the linked privacy notice align with the DAA Principles.

Misrepresentation of DAA program participation is a deception finding even where the firm is not a CFPB or FTC enforcement target; the DAA self-regulatory program operates a separate complaint-and-accountability process.

### 3. Dark-pattern privacy

The dark-pattern privacy fact patterns recur on consumer-finance digital surfaces:

- *Cookie banner asymmetry* — the consent flow uses asymmetric button weight, pre-checked accept, or a reject path that requires more interaction than the accept path.
- *Pre-checked opt-ins* — privacy-relevant choices default to the consumer-disfavored state (data sharing on; marketing communications on; analytics tracking on).
- *Hidden settings* — the privacy controls are buried behind multiple navigation steps.
- *Repeated re-prompting* — the consent flow re-prompts the consumer after each session or after a denial, manipulating toward eventual acceptance.
- *Confirmshaming* — the reject path uses language designed to make the consumer feel guilty for declining.
- *Forced consent* — access to a service is conditioned on consent that is not strictly necessary for the service.

Each finding names the FTC dark-pattern taxonomy entry, the location in the asset, and the consumer-harm hypothesis. Several state privacy laws (CCPA / CPRA among them) prohibit dark patterns in obtaining consent; the state-law angle supports the federal UDAAP analysis.

### 4. State-privacy-law footprint

Where the firm operates in a state-privacy-law footprint (CCPA / CPRA, VCDPA, CTDPA, CPA, UCPA, and the rolling roster of state laws — pin the operative footprint at memo date), the customer-rights workflow (right to know, right to delete, right to limit, right to correct, right to opt out of sale or share) reaches the data implicated in the in-scope asset. The asset-level review records:

- Whether on-asset claims about data practices align with the state-privacy-law disclosures and the operative customer-rights mechanics.
- Whether dark-pattern privacy findings on the asset implicate the state-law dark-pattern prohibition (where applicable).
- Whether sensitive-attribute targeting (race; ethnicity; religion; sexual orientation; gender identity; precise geolocation; biometric identifiers; consumer health data) is in path on the asset and whether the state-law treatment of sensitive personal information is implicated.

### 5. Sensitive-attribute and proxy-based targeting

Where the asset's audience-targeting parameters or AI-personalisation inputs include or correlate with sensitive attributes (race; ethnicity; religion; sexual orientation; gender identity; disability; precise geolocation; consumer health data), the asset-level review reads:

- Whether the audience-definition exports or model-feature documentation indicate sensitive-attribute use directly.
- Whether the audience parameters function as a proxy for a sensitive attribute (ZIP-code targeting that materially correlates with race or ethnicity; interest-category combinations that proxy for religion or sexual orientation).
- Whether the on-asset claim about targeting practices ("we do not target on the basis of...") is consistent with the actual audience definition.

The fair-lending overlap is named alongside (cross-reference `fair-lending-test-plan` for the disparity test); the privacy overlap is the focus of this block.

### 6. AI-personalisation and prompt-as-customer-data

Where the asset is AI-personalised or AI-generated, the privacy block reads:

- Whether the personalisation inputs include consumer data the consumer believes is restricted to a specific purpose.
- Whether the AI-vendor contract addresses use of consumer prompts and personalisation inputs (training, fine-tuning, model improvement, abuse monitoring).
- Whether the on-asset disclosure to the consumer addresses the AI-personalisation mechanic and the consumer's choice to opt out.

The memo does not duplicate AI-vendor evidence review (chain to `llm-vendor-evidence-review` in `ai-governance-model-risk` where a separate review is needed); it records the asset-level read.

## Privacy-specific memo template additions

The following fields are added to the per-asset block:

- `asset.privacy_claims_present[]` — list of on-asset privacy claims with text, category (data-sale, data-share, data-use, security, control, retention, other), and substantiation status.
- `asset.adchoices_representation` — boolean; if true, the AdChoices accuracy read is required.
- `asset.dark_pattern_privacy_findings[]` — list of findings with FTC taxonomy entry, asset location, and harm hypothesis.
- `asset.state_privacy_law_footprint[]` — list of state laws applicable to the in-scope asset.
- `asset.sensitive_attribute_targeting_in_path` — boolean; if true, the sensitive-attribute and proxy-based targeting read is required.
- `asset.ai_personalisation_privacy_finding` — string where AI is in the in-scope asset.
- `cross_reference_skills[]` — extends to include `fair-lending-test-plan`, `udaap-risk-review`, `llm-vendor-evidence-review` where the privacy intersection invokes those.

## Common pitfalls in privacy-flagged marketing-review memos

- Reading the on-asset privacy claim against the privacy notice only and missing the gap between the marketing voice and the state-law disclosure voice (CCPA / CPRA "share" vs. marketing "sell").
- Treating "we participate in AdChoices" as a brand-affiliate badge without testing the program-mechanism representation.
- Reading dark-pattern privacy findings as UX issues; the FTC dark-pattern taxonomy is the regulatory framework and the findings name the catalog entry.
- Treating sensitive-attribute targeting as out of scope because the audience parameters do not name a sensitive attribute directly; proxies are the recurring failure mode.
- AI-personalised assets reviewed against the brief only and missing the per-served-variant privacy-claim read.
- State-privacy-law footprint defaulted to "California only" without checking the operative state list at memo date.
- Reading the firm's privacy-program documentation as substantiation of the on-asset claim without testing the actual data-flow against the claim.
- Conflating GLBA Privacy Rule (Reg P) compliance with adequacy of the on-asset claim; Reg P compliance is necessary but not sufficient; the asset-level deception read reaches the consumer-facing representation.
