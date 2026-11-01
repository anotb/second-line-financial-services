# Insurance sector overlay for agentic-ai-controls

This overlay carries the absorbed `claims-ai-controls` skill content. When the scope record names `insurance` as the sector, this overlay sits as the primary lens, not a secondary one. Claims-AI is the dominant insurance-sector use case for agentic systems and the overlay is opinionated about the controls that have to be in place.

Loaded by: `agentic-ai-controls/SKILL.md` when `scope.sector_overlay_set` includes `insurance`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023), AIS Program elements covering governance, risk management, testing and validation, third-party AI accountability, monitoring, and documentation; binding only to the extent state DOIs adopt it (state-adoption tracker maintained by the NAIC AI Working Group).
- NAIC Unfair Trade Practices Act (Model #880) and state Unfair Claims Settlement Practices Acts (UCSPA), governing acknowledgment timing, investigation reasonableness, prompt and reasoned denial, communication, and documentation. The standards apply regardless of who or what produces the claims decision.
- NAIC Insurance Data Security Model Law (Model #668), §4.F third-party service-provider obligations, where a TPA, claims administrator, or other vendor runs the agent on the carrier's policies.
- NYDFS Insurance Circular Letter on AI / ECDIS in life-insurance underwriting and pricing (January 2024) for NY-licensed life carriers.
- NYDFS October 2024 cyber-AI Industry Letter for NY-licensed insurers (NYDFS-covered entity status applies under 23 NYCRR Part 500).
- Colorado Division of Insurance regulation implementing SB 21-169 (governance and risk management of ECDIS and predictive models in life-insurance underwriting).
- California Department of Insurance bulletin on AI use in insurance.
- HIPAA Privacy Rule (45 CFR Part 164 Subparts A and E), HIPAA Security Rule (45 CFR Part 164 Subpart C), and Breach Notification Rule (45 CFR §§164.400-414) where the agent reads or writes PHI.
- NAIC Suitability in Annuity Transactions Model Regulation (Model #275 [verify model number]) and best-interest standards for agent / producer co-pilot tools used in annuity sales.
- NAIC ORSA Model Act (Model #505) for enterprise-material agentic systems.

## Insurance agentic-AI use-case patterns the overlay recognises

The recurring insurance use-case patterns that drive the threat surface, the authority statement, and the control set:

- **Claims-AI agent** (the dominant use case): triage, FNOL intake, severity prediction, fraud-indicator scoring, claims-handling chatbot, agentic actuation (automated payment under threshold, policy endorsement on routine flow, claim acknowledgment generation, reasoned-denial drafting). The fair-claims-settlement bar applies; the agent cannot move it.

- **Policyholder-facing chatbot**: inbound questions on coverage, claim status, billing, policy changes; agentic actuation where allowed (premium adjustments, address change, beneficiary update). UPL boundary check is non-optional.

- **Underwriting assistant** (life and health): retrieves over application data, medical records, prescription history, MVR, public-records databases, ECDIS sources; agentic actuation where allowed (case routing, additional-evidence requisition, accelerated-underwriting decision support). Unfair-discrimination overlay is structural.

- **Producer / agent co-pilot**: retrieves over product documentation, illustration software output, regulatory filings; assists with quoting, illustration generation, suitability triage. Marketing Rule analogues, state insurance advertising rules, and (for annuities) NAIC Model #275 best-interest standards apply.

- **Fraud-detection agent**: retrieves over claim files, social-media content, third-party fraud-network data; agentic actuation in SIU referral generation, claim-flag application. Indirect injection in third-party intelligence is a structural risk; SIU referral integrity is the downstream consequence.

- **Back-office agent**: call-center summarisation, mailroom OCR, document classification. Less consumer-facing; HIPAA touch is the primary concern where PHI flows through the OCR pipeline.

## Authority-statement constraints specific to insurance

For claims-AI agents, the out-of-scope list at minimum includes: no claim denial without human review of the reasoned denial; no claim approval above the firm's automated-payment threshold without supervisor approval; no policy cancellation; no fee imposition; no out-of-state-licensing-violating actions; no UPL-crossing legal advice. These are non-optional for any consumer-facing claims-AI agent and the controls review fails the section if the list is generic.

For underwriting agents in NY-licensed life-carrier scope or CO life-carrier scope, the out-of-scope list at minimum includes: no rating-factor application outside the firm's filed rate plan; no use of prohibited rating factors per state insurance code; no consumer-disclosure-bypassing actuation. Where the firm operates across multiple states, the out-of-scope list reflects the most-prescriptive state in the footprint.

For producer co-pilots used in annuity sales, the out-of-scope list at minimum includes: no recommendation that bypasses the suitability or best-interest standard; no illustration generation that violates state insurance advertising rules; no client-communication actuation that crosses producer-licensing boundaries.

## Tool-inventory expectations

Beyond the standard set:

- HIPAA-aligned access controls on PHI carriers; per-claim or per-policy query scoping is the default for any claim or policy-handling tool.
- Per-policyholder query scoping at retrieval and at write tools; cross-policyholder access is a structural privacy risk and a NAIC #880 reasonableness risk.
- Claim-handling control families on every claims-AI tool: prompt-acknowledgment timing meets state UCSPA; reasoned-denial drafting is reviewable by a named human role; complaint-flow tool routes to the firm's complaint-management system; supervisor-override path exists and is exercised in test; audit trail captures the agent's reasoning, retrieved evidence, and human-overrides per state UCSPA documentation expectations; denial-letter human review is a block-and-wait gate, never post-hoc.
- ECDIS-source access tools for underwriting agents: source-vetting at the data-vendor layer is recorded as a control with evidence; change-detection on ECDIS sources is a tool-supply-chain control.
- TPA / claims-administrator tool access: where a TPA runs the agent, the §4.F obligations attach; the carrier's controls review references the TPA's contract and the TPA's own §4.F compliance posture.

## Human-oversight bar specific to insurance

The fair-claims-settlement bar is the load-bearing one and it sets the human-oversight bar higher than EU AI Act Article 14 alone would set it:

- Reasoned-denial drafting requires block-and-wait human review by a licensed adjuster (or equivalent supervisor for unlicensed-state flows). Post-hoc sampling is insufficient; a denial letter sent before human review is a fair-claims-settlement violation.
- Claim approvals above the firm's automated-payment threshold require block-and-wait supervisor approval.
- Coverage opinions and legal-advice-adjacent communications require attorney review (UPL boundary check); the agent does not generate such communications without explicit human drafting.
- Cross-policyholder data access flagged by retrieval audit requires immediate halt-and-investigate (block-and-wait), not post-hoc.
- Policyholder communications on adverse decisions (denial, claim closure with payment less than demand, policy cancellation) require block-and-wait human review.

For underwriting agents in CO or NY life-carrier scope, the consumer-disclosure expectations of SB 21-169 implementing regulation and NYDFS Circular Letter 2024-7 require the human-oversight design to surface the disclosure decision; the agent does not actuate underwriting decisions affecting eligibility, premium, or coverage without the human surfacing the disclosure to the consumer per state requirements.

## Threat-assessment additions specific to insurance

The agentic-specific attack classes inherit from the cross-cutting set; the insurance overlay adds:

- **OCR-stage injection** for claims-AI agents handling scanned correspondence: claimant letters, third-party adjuster notes, repair estimates, medical records, attorney correspondence. OCR'd content is the point at which injected content lands in the prompt path; this is a high-likelihood vector for any claims-AI agent.
- **Indirect injection via medical-record or third-party content** for underwriting agents and claims-AI agents: third-party-controlled at source, with an adversarial actor sometimes inside the source.
- **Cross-policyholder retrieval bleed**: a structural risk from prompt-injection or from misconfigured retrieval. Any confirmed event is a HIPAA evaluation trigger and may be a NYDFS §500.17(a) trigger for NY-licensed entities.
- **ECDIS-source poisoning**: the data vendor's source-of-source is third-party-controlled; a compromise upstream of the firm's vendor-approval boundary is a structural risk for underwriting agents.
- **Unfair-discrimination output drift**: an injection-driven feature shift in an ECDIS-sourced input can produce discriminatory output that violates state unfair-discrimination law; the prompt-injection and the unfair-discrimination overlays are entangled for underwriting agents.

## Sandbox and execution-environment guarantees specific to insurance

- For TPA-run agents, sandbox guarantees are the carrier's responsibility to verify under §4.F. Reading the TPA's policy is insufficient; the carrier's review records evidence the sandbox is enforced (or routes the gap to recommended actions with the TPA as owner).
- HIPAA Security Rule technical safeguards (§164.312) apply to agent-execution environments handling PHI.

## Kill switch and drill cadence specific to insurance

- Drill cadence for claims-AI agents: at minimum quarterly for tier-1 / tier-2 agents; on any change to the firm's automated-payment threshold; on any change to the firm's reasoned-denial template; on any change to the state-licensing footprint.
- The kill switch operationally pauses claim actuation while leaving the human-claims-handling path operational; a kill switch that takes the entire claims pipeline offline is over-broad and creates a different fair-claims-settlement violation (timeliness).
- Rollback path includes: any claim auto-actuated since the last clean state is queued for human re-review; communications sent to policyholders during the suspect window are reviewed for retraction and corrected communication; the firm's complaint-management system is briefed.

## Logging and audit specific to insurance

- State UCSPA documentation expectations require audit-trail capture of the agent's reasoning, the retrieved evidence supporting the claims decision, and any human overrides. Retention aligns to state-by-state record-retention requirements (typically 3-7 years; the firm's retention matrix is the operative reference).
- HIPAA audit-log requirements (§164.308(a)(1)(ii)(D)) apply to PHI-touching agents.
- For NY-licensed entities, NYDFS Part 500 §500.6 audit-trail expectations apply.

## Incident response and regulator-notification triggers specific to insurance

The cyber-overlay-named triggers apply where the cyber overlay is loaded; the insurance overlay adds:

- HIPAA breach notification: the Breach Notification Rule (45 CFR §§164.400-414) requires notification to affected individuals, HHS, and in some cases the media following discovery of a breach of unsecured PHI. Tool-misuse or cross-policyholder events causing PHI exfiltration are within scope.
- State Insurance Data Security Model Law-adopting jurisdictions: cybersecurity event notification to the state insurance commissioner per the adopting state's regulation (timing varies; commonly 72 hours).
- State unfair-claims-settlement complaint triggers: an injection-driven or tool-misuse event that causes a UCSPA-violating outcome (untimely denial, unreasoned denial, miscommunication on coverage) may trigger state DOI notification or a state market-conduct examination response.
- State unfair-discrimination event triggers if an injection-driven event causes a discriminatory output in an underwriting or pricing decision; the state DOI may be the appropriate notification authority.
- Producer-side conduct triggers if the agent is used in a way that violates state insurance advertising rules, suitability requirements, or best-interest standards.
- TPA-run agents: §4.F third-party-service-provider notification chain runs from TPA to carrier to (where adopted) state insurance commissioner.

## Recommended-action items the overlay surfaces

Standard items that fire for any insurance agentic deployment:

- Where the use case is in scope of the NAIC Bulletin (in adopting states), the AIS Program documentation is updated to reference the agentic-controls review and the residual-risk acceptance is recorded against the AIS Program element on documentation.
- Where the use case is in NY-licensed life-carrier underwriting scope, the NYDFS Circular Letter 2024-7 governance, fairness-testing, disclosure, and consumer-recourse expectations are mapped to the controls review's authority statement, oversight points, and recommended actions.
- Where the use case is in Colorado life-carrier underwriting scope, the SB 21-169 implementing regulation is referenced and the unfair-discrimination testing is mapped to the threat assessment and monitoring.
- Where the use case handles PHI, the privacy officer co-signs the residual-risk acceptance and the HIPAA breach-notification process is rehearsed.
- For claims-AI agents, the state-by-state UCSPA timing matrix is captured (or referenced) and the agent's actuation timing is mapped against the most-prescriptive state in the footprint.
- For TPA-run agents, the §4.F evidence pack from the TPA is requested and recorded; the gap (if any) carries `[evidence needed]` with the TPA as owner.
- For producer co-pilot agents in annuity sales, the suitability and best-interest standards are mapped to the human-oversight design; the state-by-state suitability-rule patchwork is referenced.
- ORSA inclusion if the agentic system is enterprise-material: the agent is named in the ORSA Summary Report under the Model #505 framing.

## Common pitfalls specific to insurance

- Relying on a fairness-only test where a fair-claims-settlement test is required. A claims-AI agent that passes a generic fairness eval and fails state UCSPA timing or reasoned-denial requirements is operationally non-compliant.
- Missing the UPL question on consumer-facing claims chatbots. Where the bot crosses into legal advice or coverage opinions, the carrier risks UPL exposure on top of unfair-trade-practices exposure.
- Treating the TPA's controls as out-of-scope. The TPA's controls are the carrier's controls for §4.F purposes; reviewing the carrier's tools without the TPA's tools is half a review.
- Treating the NAIC AI Bulletin as US-uniform. It is state-by-state in adoption; the firm's footprint determines which adopting states' versions apply.
- Treating ECDIS-sourced content as trusted because the data vendor is on the firm's approved-vendor list. The vendor's source-of-source is third-party-controlled; ECDIS-specific source-vetting and change-detection are the load-bearing controls, not vendor approval at procurement time.
- Omitting OCR-stage sanitisation for scanned correspondence in claims-AI agents. The OCR output is the point at which injected content lands in the prompt path; sanitisation at the OCR stage is more reliable than at the prompt-construction stage.
- Failing to involve the privacy officer when the use case handles PHI. A HIPAA-relevant exfiltration is a privacy event with binding notification timelines, not a discretionary AI-governance decision.
- Treating the unfair-discrimination overlay as separable from the prompt-injection overlay for underwriting agents. The two are entangled.
- Designing post-hoc sampling oversight on reasoned-denial drafting. Block-and-wait is the correct mode; post-hoc on a denial that has already been sent is a fair-claims-settlement violation, not a control.
- Documenting kill-switch but never drilling. A claims-AI kill switch that has not been drilled is theatre; the drill record is the evidence.
