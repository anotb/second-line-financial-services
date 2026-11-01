# cross-cutting

One section per topic. Read only the sections the scope calls for.

## conduct

### Conduct cross-cutting overlay for udaap-risk-review

This overlay is mandatory on this skill. UDAAP findings are the dominant conduct-risk signal in US consumer financial services; every UDAAP review memo carries a conduct-risk implications block. The overlay names what changes when the scope record flags `conduct` (which it does by default for this skill).

Loaded by: `udaap-risk-review/SKILL.md` whenever invoked. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What changes for conduct-flagged UDAAP review memos

##### 1. UDAAP-conduct vocabulary clarified

Conduct in second-line vocabulary names a customer-outcome lens, a named-manager accountability lens, and a regulatory-engagement lens. UDAAP is one specific legal regime under that umbrella. The overlap is not total: every UDAAP defect is potentially a conduct defect, but not every conduct defect rises to UDAAP. The memo is explicit about which lens is doing the analytical work; the seam between "this is a UDAAP §1031 element finding" and "this is a conduct-framework finding that does not yet rise to UDAAP" matters because the regulatory consequences differ.

##### 2. Conduct-risk taxonomy tie-back

The memo records the conduct-risk taxonomy tie-back per the firm's framework. Common categories include:

- *Incentives* — sales or LO compensation design that encourages the conduct under review.
- *Product design* — fee architecture, disclosure design, default-state design, choice-architecture design.
- *Communication* — marketing copy, in-product messaging, AI-generated communication, dynamic disclosure.
- *Sales practices* — branch and digital sales conduct, retention-offer conduct, friction-design.
- *Customer outcome* — outcome disparity across policy-relevant segments (rural, low-balance, digital-only, English-as-second-language, recent-immigrant cohorts).
- *Complaint linkage* — whether the underlying complaint signal already surfaced in the firm's complaint-monitoring loop and what was done with it.

The memo lists each category that the in-scope fact pattern touches; the conduct committee reads against the taxonomy.

##### 3. Named conduct-accountable manager

For UK-licensed firms in SMCR scope, the senior manager with the prescribed responsibility for the relevant business is a named sign-off audience. For non-UK firms, the firm's conduct framework names a manager (often the head of the relevant business or the head of consumer / customer); the memo names the role, not the individual. The UDAAP-decision forum (product committee, CCO, conduct committee, fair-lending committee, counsel) and the conduct-accountable manager are separable items; the memo is explicit about which is which and which forum decides what.

##### 4. Customer-outcome lens supplements the protected-class lens

Where the UDAAP review intersects fair-lending themes (steering, marketing distribution, servicing, loss-mitigation), the customer-outcome lens extends the analysis beyond the protected-class lens. Customer-outcome disparity across policy-relevant segments is a conduct concern even where the protected-class disparity tests pass. The memo records:

- Whether policy-relevant segments under the conduct framework are affected by the fact pattern, in addition to or instead of protected-class segments.
- Whether the fact pattern raises a parallel ECOA / FHA theory (cross-reference `fair-lending-test-plan`).
- Whether complaint-monitoring drift in the relevant complaint codes was a leading indicator (cross-reference `complaint-theme-analysis`).

##### 5. Conduct-event taxonomy classification

Where the firm operates a conduct-event taxonomy (a register of conduct-risk events with severity, root cause, and customer-impact classification), the memo names whether the in-scope finding is a conduct-event candidate. The classification is not the memo's job to finalise; the conduct-risk function classifies. The memo carries the recommendation.

##### 6. Regulatory-engagement intersection

Where the UDAAP memo is responding to a regulatory-engagement event (CFPB inquiry, OCC Matter Requiring Attention, FDIC corrective action, state AG inquiry, FCA Section 166 review for UK-licensed entities), the conduct overlay records:

- The event that triggered the memo.
- The regulator-engagement counsel posture (privilege, work-product, response-file management).
- Whether the conduct committee gets a read alongside the UDAAP-decision forum.
- Whether the firm's conduct-event reporting to the regulator is implicated (e.g., FCA reportable concern under Principle 11 for UK-licensed entities; or a CFPB self-reporting consideration for US entities).

##### 7. Complaint-monitoring loop closure

The memo names the downstream complaint-monitoring posture: which complaint codes the firm will watch for re-emergence after remediation; the cadence; the escalation trigger if complaints persist. UDAAP remediation that does not close the complaint-monitoring loop is incomplete; the conduct overlay surfaces the loop as a controls-hypothesis item.

#### Conduct-specific memo template additions

The following fields and sections are added to the memo (mapped to schema where present):

- `conduct_risk_taxonomy_tie_back[]` — list of conduct-risk taxonomy categories the fact pattern touches.
- `conduct_accountable_manager_role` — named role under SMCR or the firm's conduct framework, distinct from the UDAAP-decision forum.
- `conduct_committee_read` — boolean; if true, the conduct or customer-outcome committee gets a read alongside the UDAAP-decision forum.
- `conduct_event_candidate` — boolean; if true, the finding is recommended for classification by the conduct-risk function under the firm's conduct-event taxonomy.
- `customer_outcome_segments_affected[]` — list of policy-relevant segments affected (in addition to or instead of protected-class segments).
- `regulator_engagement_trigger` — string; named regulator-engagement event that triggered the memo, if any.
- `complaint_monitoring_loop_closure` — string; description of the post-remediation complaint-monitoring posture.

#### Common pitfalls in conduct-flagged UDAAP review memos

- Conflating UDAAP review with conduct review and producing a memo that does not separate the findings cleanly; counsel and the regulator both need the seams visible.
- Extending the protected-class lens into customer-outcome segments without recording the test-framing change; the vocabulary matters because the legal regime differs.
- Treating complaint themes as a noisy input rather than as a leading indicator; complaint-rate and complaint-code drift are signal, not noise.
- Missing the named conduct-accountable manager on the sign-off audience list; the conduct framework names a role separate from the product owner and separate from the CCO.
- Writing the memo without recording the regulator-engagement trigger where one exists; the response-file posture and the privilege posture both turn on whether the memo is responding to engagement or running on the routine cycle.
- Recommending remediation without naming the complaint-monitoring loop-closure posture; remediation that does not close the loop is incomplete and the conduct committee will catch the gap.
- Treating UDAAP and the conduct framework as the same regime for global firms; they are aligned in spirit but the legal architecture differs and the memo should not pretend otherwise.

## privacy

### Privacy cross-cutting overlay for udaap-risk-review

This overlay is secondary on this skill. It loads when the in-scope flow processes NPI in a way that itself raises a UDAAP angle: a deceptive privacy disclosure, a dark-pattern privacy-consent flow, a fee mechanic tied to privacy-permission state, a data-sharing arrangement that misleads the consumer, or an AI-driven personalisation that materially relies on consumer data the consumer believes is restricted.

Loaded by: `udaap-risk-review/SKILL.md` when `scope.cross_cutting_set` includes `privacy` or when the in-scope fact pattern touches a privacy-meets-UDAAP angle. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What changes for privacy-flagged UDAAP review memos

##### 1. Privacy-meets-UDAAP fact patterns

The recurring intersections:

- *Deceptive privacy disclosure.* The privacy notice or in-product privacy disclosure represents data-handling practices in a way that is materially inconsistent with the actual practice. Element analysis: deception (representation likely to mislead; reasonable consumer; materiality); the actual data-handling practice is the omitted or contradicted truth.
- *Dark-pattern privacy-consent flow.* The consent flow uses choice-architecture design that materially interferes with the consumer's ability to make a privacy-related choice (defaults, friction, asymmetric framing, repeated re-prompting). Element analysis: abusiveness (material interference) plus deception where the framing misleads.
- *Fee mechanic tied to privacy-permission state.* A fee, credit decision, or service tier varies with the consumer's privacy permissions in a way that is not adequately disclosed, or in a way the consumer cannot reasonably avoid, or in a way that takes unreasonable advantage of the consumer's reliance on the firm. Element analysis spans all three prongs depending on the specifics.
- *Data-sharing or sub-processor arrangement misleading the consumer.* The firm shares consumer data with a sub-processor or partner in a way that is not adequately disclosed or that the consumer cannot reasonably avoid. Element analysis: deception primarily; unfairness where the data-sharing produces substantial injury (e.g., downstream targeting, unrelated marketing, identity-resolution against the consumer).
- *AI-driven personalisation materially relying on restricted data.* Personalised pricing, retention offers, or risk decisions rely on consumer data the consumer believes is restricted to a specific purpose; the algorithmic outcome surfaces the data in a way that misleads or takes unreasonable advantage. Element analysis ties to the AI / algorithmic-discrimination block in the main flow.

##### 2. GLBA Safeguards posture as a contextual control

The Safeguards Rule (16 CFR Part 314 for FTC-supervised; 12 CFR Part 30 Appendix B for OCC; 12 CFR Part 364 Appendix B for FDIC) sets the firm's information-security program for NPI. The UDAAP memo does not finalise GLBA findings; it records the GLBA posture as context. Where the in-scope fact pattern interacts with GLBA-protected NPI, the memo:

- Names the data classification involved (NPI per GLBA; PHI per HIPAA where applicable; PCI; CCPA-defined personal information; state-specific categories).
- Notes whether the firm's information-security program is operating against the data flow at issue (e.g., whether the data-sharing arrangement at issue carries an appropriate sub-processor contract, vendor diligence, and DPA).
- Cross-references `vendor-diligence` (in `third-party-operational-resilience`) where the in-scope fact pattern involves a third-party vendor handling consumer data.

##### 3. State-privacy-law footprint

Where the firm operates in a state-privacy-law footprint (CCPA / CPRA, VCDPA, CTDPA, and the rolling roster of state laws), the customer-rights workflow (right to know, right to delete, right to limit, right to correct) reaches the data implicated in the in-scope flow. The UDAAP memo records:

- Whether the in-scope flow is subject to a customer-rights request received during the review period.
- Whether the firm's state-privacy-law obligations are aligned with the disclosures and the consumer-journey design at issue.
- Whether a state-privacy-law angle (e.g., dark-pattern prohibition under CCPA / CPRA) supports the deception or abusiveness analysis under federal UDAAP.

##### 4. Privacy-disclosure consistency

A recurring failure mode: the privacy notice promises one thing, the consumer-experience flow does another, the marketing copy implies a third. The UDAAP memo reads the privacy disclosure against the actual flow:

- Privacy notice text vs. observed data flow.
- In-product privacy controls vs. observed default state.
- Marketing copy vs. privacy notice (cross-reference `marketing-claim-review` for asset-level marketing-claim review).
- AI-driven communication vs. privacy disclosure (cross-reference any AI-governance review of the in-scope model).

##### 5. AI personalisation and prompt-as-customer-data lens

Where the in-scope flow includes an AI surface (conversational AI, agentic flow, AI-driven communication scheduling, AI-personalised disclosure), consumer prompts and contextual signals to the AI are themselves customer data. The UDAAP memo records:

- Whether the AI-vendor contract addresses use of customer prompts (training, fine-tuning, model improvement, abuse monitoring).
- Whether the disclosure to the consumer addresses prompt-as-customer-data handling.
- Whether the AI personalisation surfaces consumer data in a way that materially interferes with the consumer's understanding (abusiveness) or misleads (deception).

The memo does not duplicate AI-vendor evidence review (chain to `llm-vendor-evidence-review` in `ai-governance-model-risk`); it records the UDAAP read at the consumer surface.

#### Privacy-specific memo template additions

The following fields are added to the memo when the privacy overlay loads:

- `privacy_intersection_type` — enum (`deceptive-privacy-disclosure`, `dark-pattern-privacy-consent`, `fee-tied-to-privacy-state`, `data-sharing-misleading`, `ai-personalisation-on-restricted-data`, `other`).
- `data_classification_involved[]` — list of data classifications implicated (NPI, PHI, PCI, state-personal-information categories).
- `state_privacy_law_footprint[]` — list of state laws applicable to the in-scope flow.
- `privacy_disclosure_consistency_finding` — string describing the consistency or inconsistency between the privacy notice, the in-product flow, and the marketing copy.
- `ai_prompt_as_customer_data_finding` — string where AI is in the in-scope flow.
- `cross_reference_skills[]` — extends to include `vendor-diligence`, `marketing-claim-review`, `llm-vendor-evidence-review` where the privacy intersection invokes those.

#### Common pitfalls in privacy-flagged UDAAP review memos

- Treating privacy as a separate review track and producing a UDAAP memo that does not address the privacy-meets-UDAAP angle even where it is in the fact pattern; the consumer does not perceive the regimes as separate.
- Reading the privacy notice in isolation from the consumer-experience flow; the gap between notice and flow is the recurring source of the deception finding.
- Defaulting to "the firm is GLBA-compliant" as a UDAAP defence; GLBA compliance is necessary but not sufficient; the UDAAP element tests reach the consumer-facing representation and the consumer-journey design.
- Treating dark-pattern design as a UX problem rather than as an abusiveness or deception angle; the bureau and the FTC have both pursued dark-pattern fact patterns under existing UDAAP / UDAP authority.
- Missing the state-privacy-law overlay where the firm operates in a CCPA / CPRA or similar footprint; the state regime can both support the federal UDAAP analysis and trigger separate state-AG attention.
- Treating consumer prompts to AI surfaces as routine telemetry; they are customer data and they raise their own UDAAP and privacy questions when the AI vendor's contract is open on training-data use.
- Conflating privilege posture across the privacy and UDAAP review tracks; the artifacts overlap but the privilege framework is set per artifact.
