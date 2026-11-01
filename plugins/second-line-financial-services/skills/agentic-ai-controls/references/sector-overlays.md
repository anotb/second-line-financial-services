# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay for agentic-ai-controls

When the scope record names `banking` as the sector, this overlay adds banking-specific authority-statement constraints, tool-inventory expectations, monitoring signals, regulator-notification triggers, and co-reviewer expectations.

Loaded by: `agentic-ai-controls/SKILL.md` when `scope.sector_overlay_set` includes `banking`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- 12 CFR Part 53 (OCC), 12 CFR Part 225 Subpart M (FRB), 12 CFR Part 304 Subpart C (FDIC) — banking computer-security incident notification rule (36-hour notification, effective May 2022).
- FFIEC IT Examination Handbook, Information Security and Architecture, Infrastructure, and Operations booklets, applied to the agent's serving environment.
- Joint OCC, FRB, and FDIC Interagency Guidance on Third-Party Relationships (June 2023) — OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023.
- The joint interagency Revised Guidance on Model Risk Management (OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026; supersedes SR 11-7 and SR 21-8) expressly excludes agentic AI from its scope (footnote 3); the agentic system is not within the bulletin. Where the bank's model risk programme treats the agent as a model by analogy, the principles inform but the binding hook is firm policy.
- NYDFS 23 NYCRR Part 500 for NY-licensed bank-affiliated entities; NYDFS October 2024 AI Industry Letter.
- BSA / AML expectations for AML-touching agent flows (FinCEN; FFIEC BSA/AML Examination Manual).
- CFPB UDAAP framings under 12 USC §§5531 and 5536 for consumer-financial-product flows.
- Reg E (12 CFR Part 1005) for electronic-funds-transfer flows touched by agents.
- Reg DD (12 CFR Part 1030) and Reg Z (12 CFR Part 1026) for deposit-disclosure and credit-disclosure flows touched by agents.

#### Recurring banking agentic-AI use-case patterns

- **Customer-service representative (CSR) co-pilot**: agent assists CSR with summarisation, next-best-action suggestion, drafted communications, light actuation (temporary card lock, callback scheduling). Tool-use surface is moderate; consumer-protection seams are CFPB UDAAP and Reg E.
- **Servicing assistant**: agent reads account state and proposes routine servicing actions (address change, statement re-issue, fee inquiry). UDAAP and Reg DD/Z disclosure framings apply.
- **AML-investigation co-pilot**: agent reads transaction history, KYC records, news content; assists with case-narrative drafting, alert-disposition triage. BSA officer is a co-reviewer; SAR-quality and false-positive-rate are operational metrics.
- **Lending agent**: read tools on credit data; communication tools on customer-facing communications; proposed actuation on routine workflow steps. ECOA / Reg B and Fair Lending overlap; CFPB UDAAP overlap.
- **Fraud-response agent**: agent reads fraud-detection signals; agentic actuation in card-lock, transaction-hold, customer-outreach. Cyber overlay is structural; consumer-recourse posture matters.
- **Sponsor-bank operations agent for fintech-backed BaaS**: agent runs at the sponsor bank or at the fintech with read/write to the sponsor-bank's systems; shared-responsibility allocation is the load-bearing question (see payments-fintech overlay).

#### Authority-statement constraints specific to banking

For consumer-facing banking agents the out-of-scope list at minimum includes: no funds movement; no permanent account closure; no fee imposition or fee waiver; no permanent card actions; no rate adjustments. These are non-optional and the controls review fails the section if the list is generic.

For AML-investigation co-pilots: no SAR filing, no SAR closing, no customer-notification on AML investigations (tipping-off prohibition under 31 CFR §1010.310).

#### Tool-inventory expectations

- Per-customer query scoping at retrieval and at write tools; cross-customer access is a structural privacy and UDAAP risk.
- Funds-movement tools are not in the agent's inventory unless the use case explicitly requires it and the authority statement carries the matched in-scope action with reversibility framing.
- Communication tools (outbound email, SMS, in-app message) carry blast-radius framing in policy units (e.g., "could send up to N outbound communications per minute"); rate limits at the tool layer are non-optional.
- For AML-touching agents: no tool that posts to FinCEN, no tool that closes SAR cases, no tool that opens or closes monitoring rules.

#### Human-oversight bar specific to banking

- For consumer-facing communications generated or assisted by the agent, block-and-wait CSR or supervisor review applies; UDAAP and Reg DD/Z disclosure expectations require human accuracy review.
- For AML alert disposition, block-and-wait analyst review is the default; post-hoc sampling on alert-disposition triage requires explicit BSA officer sign-off and sampling-rate evidence.
- For fraud-response actuation (card lock, transaction hold), notify-and-revocable is acceptable for tier-3 / tier-4 use cases; block-and-wait for tier-1 / tier-2.
- Sponsor-bank fintech BaaS: the human-oversight design names the responsible function on each side of the bank-fintech boundary; allocation is in the contract and the controls review surfaces gaps.

#### Monitoring signals the overlay adds

- AML-touching agents: false-positive-rate change on alert disposition, SAR-quality drift, alert-volume drift, BSA-officer override rate.
- Consumer-facing agents: complaint-rate and complaint-code drift (UDAAP signal), customer-recourse channel volume.
- Funds-movement-adjacent agents: transaction-anomaly signals tied to the agent's actuation.
- Sponsor-bank BaaS: shared-monitoring posture per the contract.

#### Incident-response and regulator-notification triggers

- 12 CFR Part 53 / Part 225 / Part 304 — 36-hour notification to primary federal regulator for "notification incidents" affecting banking services.
- NYDFS Part 500 §500.17(a) for NY-licensed entities; 72-hour notice on cybersecurity events meeting the rule's criteria.
- SEC 8-K Item 1.05 for public-registrant banking organisations.
- GLBA Safeguards Rule (16 CFR §314.5(d)) for FTC-scope non-bank financial institutions; less commonly applicable to bank-affiliated entities but loaded for non-bank affiliates.
- BSA-officer-led notification chains for AML-related events.

#### Recommended-action items the overlay surfaces

- For AML-touching agents, BSA officer sign-off on the residual-risk acceptance.
- For consumer-facing agents, UDAAP risk-framing in the residual-risk view; complaint-rate baseline before go-live is non-optional.
- For sponsor-bank BaaS: the bank-fintech contract reflects the controls review's findings (notice rights, audit rights, off-switch ownership, IR-runbook integration).
- For agents touching the deposit, lending, or payments rails: the consumer-disclosure posture is mapped against Reg DD, Reg Z, Reg E.

#### Common pitfalls specific to banking

- Treating the AML-investigation co-pilot as low-risk because the agent does not file SARs. The alert-disposition assistance shapes filing decisions; BSA officer involvement is non-optional.
- Omitting the consumer-disclosure framing on agents that generate or modify customer communications. Reg DD and Reg Z accuracy expectations apply to AI-assisted communications.
- Treating the 36-hour banking computer-security incident notification rule as out-of-scope because the event is "AI-related". A tool-misuse event that materially disrupts banking services is within scope of the rule regardless of the AI framing.
- Sponsor-bank BaaS: assuming the fintech's controls are sufficient. The sponsor bank is accountable; the controls review records the sponsor-bank-side coverage independently.

## capital-markets

### Capital markets sector overlay for agentic-ai-controls

When the scope record names `capital-markets` as the sector, this overlay adds capital-markets-specific authority-statement constraints, tool-inventory expectations, monitoring signals, regulator-notification triggers, and co-reviewer expectations.

Loaded by: `agentic-ai-controls/SKILL.md` when `scope.sector_overlay_set` includes `capital-markets`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- SEC Rule 15c3-5 — Market Access Rule (17 CFR §240.15c3-5): pre-trade controls, post-trade surveillance, immediate access to a kill switch.
- FINRA Rule 3110 — Supervision; FINRA Rule 4530 — Reporting Requirements.
- SEC Investment Advisers Act Rule 206(4)-1 — Marketing Rule (17 CFR §275.206(4)-1) and Rule 204-2 — Books and Records.
- SEC Reg AC (17 CFR §242.501-505) — research-analyst certification.
- MAR (Market Abuse Regulation, EU 596/2014) for EU-nexus operations and surveillance integrity.
- SEC 8-K Item 1.05 and Reg S-K Item 106 for public registrants (cybersecurity disclosure).
- NYDFS Part 500 for NY-licensed broker-dealers and investment advisers.
- The joint interagency Revised Guidance on Model Risk Management (OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026; supersedes SR 11-7) for bank-affiliated broker-dealers — note the bulletin expressly excludes agentic AI from scope (footnote 3) and reaches non-agentic components only.

#### Recurring capital-markets agentic-AI use-case patterns

- **Research-analyst assistant**: agent retrieves over price data, public-source databases, internal research; drafts client-facing notes for analyst review. Marketing Rule reach for adviser-side notes; Reg AC for research-analyst certification.
- **Surveillance-system assistant**: agent reads trade and communication surveillance signals; assists with alert disposition, narrative drafting, escalation triage. Surveillance integrity is structural; injected content in flagged communications is a recurring risk.
- **Adviser co-pilot**: agent reads client-portfolio data; drafts client communications, IPS updates, performance commentary. Marketing Rule and books-and-records (Rule 204-2) reach.
- **Order-routing or order-management agent**: agent makes or assists in routing decisions; Rule 15c3-5 is the load-bearing anchor; kill switch and pre-trade controls are non-optional.
- **Operations agent for trade-lifecycle workflows**: agent handles confirmations, allocations, settlement-exception triage. Less consumer-facing; books-and-records and surveillance integrity apply.

#### Authority-statement constraints specific to capital markets

For research-analyst assistants the out-of-scope list at minimum includes: no client-communication actuation (no auto-send); no order-routing or order-management interaction; no client-list access; no confidential-information cross-contamination across analysts. These are non-optional.

For order-routing agents (where in scope): the in-scope actions are bounded by the firm's pre-trade control framework under Rule 15c3-5; the out-of-scope list includes no order routing outside firm risk thresholds, no order routing outside client mandate, no override of pre-trade controls.

For adviser co-pilots: no client-communication actuation without the adviser's affirmative review; no recommendation that bypasses fiduciary-lens standards; no books-and-records-relevant action without preservation evidence.

#### Tool-inventory expectations

- Order-routing tools (where in scope): integrate with the firm's pre-trade control framework; rate limits and value limits at the tool layer are mandatory; the kill switch on the agent is the kill switch on the order flow.
- Communication tools: blast-radius framing in policy units; books-and-records preservation under Rule 204-2 is non-optional.
- Surveillance tools: read-only on alert data; agent does not close alerts or modify case state without human supervisor approval.
- Research-data tools: per-analyst scoping; cross-coverage retrieval is a structural risk for information-barrier integrity.

#### Human-oversight bar specific to capital markets

- For research-analyst assistants: block-and-wait analyst review of any client-facing draft; Reg AC certification is on the human, not the agent; Marketing Rule expectations apply to the deployed surface.
- For order-routing agents: the kill-switch operational decision and the pre-trade control gating are the oversight surface; human-in-the-loop or human-on-the-loop posture per Rule 15c3-5; rapid-disable capability is non-optional.
- For surveillance-system assistants: block-and-wait supervisor review on alert closure; FINRA Rule 3110 supervisory bar applies.
- For adviser co-pilots: block-and-wait adviser review on any client-impacting communication; fiduciary-lens framing on recommendations.

#### Monitoring signals the overlay adds

- Order-routing agents: order-rate and order-value distributions per agent; pre-trade control trip rate; cross-mandate query anomaly; kill-switch activation events (any activation is signal).
- Research-analyst assistants: cross-coverage retrieval audit; client-facing draft volume; Marketing Rule trip rate on draft scanning.
- Surveillance-system assistants: alert-closure rate, alert-reopen rate, false-negative review rate.
- Adviser co-pilots: client-communication volume, suitability-trip rate where applicable.

#### Incident-response and regulator-notification triggers

- Rule 15c3-5 events: erroneous orders, cross-mandate routing, post-trade surveillance failures may trigger SEC and FINRA reporting under Rule 17a-3, Rule 17a-4, Rule 4530.
- NYDFS Part 500 §500.17(a) for NY-licensed entities.
- SEC 8-K Item 1.05 for public registrants.
- Marketing Rule violations from agent-generated content: enforcement risk and remedial-action expectations.
- Surveillance-failure events: state and federal AG / SEC enforcement implications; the firm's compliance and surveillance escalation chain runs in parallel.

#### Recommended-action items the overlay surfaces

- For order-routing agents, the Rule 15c3-5 control review is rerun against the agent's tool inventory; pre-trade controls cover the agent's actuation surface; the kill switch is integrated with the firm's market-access kill switch.
- For research-analyst assistants, Marketing Rule and Reg AC framings are reflected in the human-oversight design and the books-and-records preservation evidence.
- For surveillance-system assistants, FINRA 3110 supervisory bar is reflected in the human-oversight design and the alert-disposition audit cadence.
- For adviser co-pilots, fiduciary-lens framing is reflected in the residual-risk view; books-and-records preservation under Rule 204-2 is exercised in test (sample log entry).

#### Common pitfalls specific to capital markets

- Treating an order-routing agent as a Rule 15c3-5-out-of-scope assistant. If the agent influences routing or order parameters, Rule 15c3-5 applies.
- Treating Marketing Rule reach on AI-generated adviser communications as a compliance-team-only concern. The agentic-controls review records the human-oversight design that operationalises the Marketing Rule expectation; absence is a finding.
- Omitting cross-coverage retrieval audit on research-analyst assistants. Information-barrier integrity is structural.
- Designing post-hoc sampling oversight on alert closure or research-note drafting. Block-and-wait is the correct mode; post-hoc on a closed alert or a published note is a supervisory failure.

## insurance

### Insurance sector overlay for agentic-ai-controls

This overlay carries the absorbed `claims-ai-controls` skill content. When the scope record names `insurance` as the sector, this overlay sits as the primary lens, not a secondary one. Claims-AI is the dominant insurance-sector use case for agentic systems and the overlay is opinionated about the controls that have to be in place.

Loaded by: `agentic-ai-controls/SKILL.md` when `scope.sector_overlay_set` includes `insurance`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

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

#### Insurance agentic-AI use-case patterns the overlay recognises

The recurring insurance use-case patterns that drive the threat surface, the authority statement, and the control set:

- **Claims-AI agent** (the dominant use case): triage, FNOL intake, severity prediction, fraud-indicator scoring, claims-handling chatbot, agentic actuation (automated payment under threshold, policy endorsement on routine flow, claim acknowledgment generation, reasoned-denial drafting). The fair-claims-settlement bar applies; the agent cannot move it.

- **Policyholder-facing chatbot**: inbound questions on coverage, claim status, billing, policy changes; agentic actuation where allowed (premium adjustments, address change, beneficiary update). UPL boundary check is non-optional.

- **Underwriting assistant** (life and health): retrieves over application data, medical records, prescription history, MVR, public-records databases, ECDIS sources; agentic actuation where allowed (case routing, additional-evidence requisition, accelerated-underwriting decision support). Unfair-discrimination overlay is structural.

- **Producer / agent co-pilot**: retrieves over product documentation, illustration software output, regulatory filings; assists with quoting, illustration generation, suitability triage. Marketing Rule analogues, state insurance advertising rules, and (for annuities) NAIC Model #275 best-interest standards apply.

- **Fraud-detection agent**: retrieves over claim files, social-media content, third-party fraud-network data; agentic actuation in SIU referral generation, claim-flag application. Indirect injection in third-party intelligence is a structural risk; SIU referral integrity is the downstream consequence.

- **Back-office agent**: call-center summarisation, mailroom OCR, document classification. Less consumer-facing; HIPAA touch is the primary concern where PHI flows through the OCR pipeline.

#### Authority-statement constraints specific to insurance

For claims-AI agents, the out-of-scope list at minimum includes: no claim denial without human review of the reasoned denial; no claim approval above the firm's automated-payment threshold without supervisor approval; no policy cancellation; no fee imposition; no out-of-state-licensing-violating actions; no UPL-crossing legal advice. These are non-optional for any consumer-facing claims-AI agent and the controls review fails the section if the list is generic.

For underwriting agents in NY-licensed life-carrier scope or CO life-carrier scope, the out-of-scope list at minimum includes: no rating-factor application outside the firm's filed rate plan; no use of prohibited rating factors per state insurance code; no consumer-disclosure-bypassing actuation. Where the firm operates across multiple states, the out-of-scope list reflects the most-prescriptive state in the footprint.

For producer co-pilots used in annuity sales, the out-of-scope list at minimum includes: no recommendation that bypasses the suitability or best-interest standard; no illustration generation that violates state insurance advertising rules; no client-communication actuation that crosses producer-licensing boundaries.

#### Tool-inventory expectations

Beyond the standard set:

- HIPAA-aligned access controls on PHI carriers; per-claim or per-policy query scoping is the default for any claim or policy-handling tool.
- Per-policyholder query scoping at retrieval and at write tools; cross-policyholder access is a structural privacy risk and a NAIC #880 reasonableness risk.
- Claim-handling control families on every claims-AI tool: prompt-acknowledgment timing meets state UCSPA; reasoned-denial drafting is reviewable by a named human role; complaint-flow tool routes to the firm's complaint-management system; supervisor-override path exists and is exercised in test; audit trail captures the agent's reasoning, retrieved evidence, and human-overrides per state UCSPA documentation expectations; denial-letter human review is a block-and-wait gate, never post-hoc.
- ECDIS-source access tools for underwriting agents: source-vetting at the data-vendor layer is recorded as a control with evidence; change-detection on ECDIS sources is a tool-supply-chain control.
- TPA / claims-administrator tool access: where a TPA runs the agent, the §4.F obligations attach; the carrier's controls review references the TPA's contract and the TPA's own §4.F compliance posture.

#### Human-oversight bar specific to insurance

The fair-claims-settlement bar is the load-bearing one and it sets the human-oversight bar higher than EU AI Act Article 14 alone would set it:

- Reasoned-denial drafting requires block-and-wait human review by a licensed adjuster (or equivalent supervisor for unlicensed-state flows). Post-hoc sampling is insufficient; a denial letter sent before human review is a fair-claims-settlement violation.
- Claim approvals above the firm's automated-payment threshold require block-and-wait supervisor approval.
- Coverage opinions and legal-advice-adjacent communications require attorney review (UPL boundary check); the agent does not generate such communications without explicit human drafting.
- Cross-policyholder data access flagged by retrieval audit requires immediate halt-and-investigate (block-and-wait), not post-hoc.
- Policyholder communications on adverse decisions (denial, claim closure with payment less than demand, policy cancellation) require block-and-wait human review.

For underwriting agents in CO or NY life-carrier scope, the consumer-disclosure expectations of SB 21-169 implementing regulation and NYDFS Circular Letter 2024-7 require the human-oversight design to surface the disclosure decision; the agent does not actuate underwriting decisions affecting eligibility, premium, or coverage without the human surfacing the disclosure to the consumer per state requirements.

#### Threat-assessment additions specific to insurance

The agentic-specific attack classes inherit from the cross-cutting set; the insurance overlay adds:

- **OCR-stage injection** for claims-AI agents handling scanned correspondence: claimant letters, third-party adjuster notes, repair estimates, medical records, attorney correspondence. OCR'd content is the point at which injected content lands in the prompt path; this is a high-likelihood vector for any claims-AI agent.
- **Indirect injection via medical-record or third-party content** for underwriting agents and claims-AI agents: third-party-controlled at source, with an adversarial actor sometimes inside the source.
- **Cross-policyholder retrieval bleed**: a structural risk from prompt-injection or from misconfigured retrieval. Any confirmed event is a HIPAA evaluation trigger and may be a NYDFS §500.17(a) trigger for NY-licensed entities.
- **ECDIS-source poisoning**: the data vendor's source-of-source is third-party-controlled; a compromise upstream of the firm's vendor-approval boundary is a structural risk for underwriting agents.
- **Unfair-discrimination output drift**: an injection-driven feature shift in an ECDIS-sourced input can produce discriminatory output that violates state unfair-discrimination law; the prompt-injection and the unfair-discrimination overlays are entangled for underwriting agents.

#### Sandbox and execution-environment guarantees specific to insurance

- For TPA-run agents, sandbox guarantees are the carrier's responsibility to verify under §4.F. Reading the TPA's policy is insufficient; the carrier's review records evidence the sandbox is enforced (or routes the gap to recommended actions with the TPA as owner).
- HIPAA Security Rule technical safeguards (§164.312) apply to agent-execution environments handling PHI.

#### Kill switch and drill cadence specific to insurance

- Drill cadence for claims-AI agents: at minimum quarterly for tier-1 / tier-2 agents; on any change to the firm's automated-payment threshold; on any change to the firm's reasoned-denial template; on any change to the state-licensing footprint.
- The kill switch operationally pauses claim actuation while leaving the human-claims-handling path operational; a kill switch that takes the entire claims pipeline offline is over-broad and creates a different fair-claims-settlement violation (timeliness).
- Rollback path includes: any claim auto-actuated since the last clean state is queued for human re-review; communications sent to policyholders during the suspect window are reviewed for retraction and corrected communication; the firm's complaint-management system is briefed.

#### Logging and audit specific to insurance

- State UCSPA documentation expectations require audit-trail capture of the agent's reasoning, the retrieved evidence supporting the claims decision, and any human overrides. Retention aligns to state-by-state record-retention requirements (typically 3-7 years; the firm's retention matrix is the operative reference).
- HIPAA audit-log requirements (§164.308(a)(1)(ii)(D)) apply to PHI-touching agents.
- For NY-licensed entities, NYDFS Part 500 §500.6 audit-trail expectations apply.

#### Incident response and regulator-notification triggers specific to insurance

The cyber-overlay-named triggers apply where the cyber overlay is loaded; the insurance overlay adds:

- HIPAA breach notification: the Breach Notification Rule (45 CFR §§164.400-414) requires notification to affected individuals, HHS, and in some cases the media following discovery of a breach of unsecured PHI. Tool-misuse or cross-policyholder events causing PHI exfiltration are within scope.
- State Insurance Data Security Model Law-adopting jurisdictions: cybersecurity event notification to the state insurance commissioner per the adopting state's regulation (timing varies; commonly 72 hours).
- State unfair-claims-settlement complaint triggers: an injection-driven or tool-misuse event that causes a UCSPA-violating outcome (untimely denial, unreasoned denial, miscommunication on coverage) may trigger state DOI notification or a state market-conduct examination response.
- State unfair-discrimination event triggers if an injection-driven event causes a discriminatory output in an underwriting or pricing decision; the state DOI may be the appropriate notification authority.
- Producer-side conduct triggers if the agent is used in a way that violates state insurance advertising rules, suitability requirements, or best-interest standards.
- TPA-run agents: §4.F third-party-service-provider notification chain runs from TPA to carrier to (where adopted) state insurance commissioner.

#### Recommended-action items the overlay surfaces

Standard items that fire for any insurance agentic deployment:

- Where the use case is in scope of the NAIC Bulletin (in adopting states), the AIS Program documentation is updated to reference the agentic-controls review and the residual-risk acceptance is recorded against the AIS Program element on documentation.
- Where the use case is in NY-licensed life-carrier underwriting scope, the NYDFS Circular Letter 2024-7 governance, fairness-testing, disclosure, and consumer-recourse expectations are mapped to the controls review's authority statement, oversight points, and recommended actions.
- Where the use case is in Colorado life-carrier underwriting scope, the SB 21-169 implementing regulation is referenced and the unfair-discrimination testing is mapped to the threat assessment and monitoring.
- Where the use case handles PHI, the privacy officer co-signs the residual-risk acceptance and the HIPAA breach-notification process is rehearsed.
- For claims-AI agents, the state-by-state UCSPA timing matrix is captured (or referenced) and the agent's actuation timing is mapped against the most-prescriptive state in the footprint.
- For TPA-run agents, the §4.F evidence pack from the TPA is requested and recorded; the gap (if any) carries `[evidence needed]` with the TPA as owner.
- For producer co-pilot agents in annuity sales, the suitability and best-interest standards are mapped to the human-oversight design; the state-by-state suitability-rule patchwork is referenced.
- ORSA inclusion if the agentic system is enterprise-material: the agent is named in the ORSA Summary Report under the Model #505 framing.

#### Common pitfalls specific to insurance

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

## payments-fintech

### Payments and fintech sector overlay for agentic-ai-controls

When the scope record names `payments-fintech` as the sector, this overlay adds payments-and-fintech-specific authority-statement constraints, tool-inventory expectations, monitoring signals, regulator-notification triggers, and co-reviewer expectations. The most distinctive issue in this sector is the bank-fintech shared-responsibility allocation in BaaS arrangements.

Loaded by: `agentic-ai-controls/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- Joint OCC, FRB, and FDIC Interagency Guidance on Third-Party Relationships (June 2023) — OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023, applied to bank-fintech relationships.
- 12 CFR Part 53 / Part 225 / Part 304 — banking computer-security incident notification rule, applies to bank service providers.
- CFPB UDAAP framings under 12 USC §§5531 and 5536 for consumer-facing actuation.
- State money-transmitter licensing regimes (per state); the Conference of State Bank Supervisors (CSBS) Money Services Business Model Law where adopted.
- Reg E (12 CFR Part 1005) for electronic-funds-transfer flows.
- BSA / AML expectations: FinCEN regulations, FFIEC BSA/AML Examination Manual.
- Card-network rules (Visa, Mastercard, Amex, Discover) for payment-card flows.
- NYDFS 23 NYCRR Part 500 and 23 NYCRR Part 200 (virtual currency) where applicable.
- GLBA Safeguards Rule (16 CFR Part 314) for FTC-scope non-bank entities.

#### Recurring payments-fintech agentic-AI use-case patterns

- **Onboarding / KYC agent**: agent reads identity documents, verification signals, sanctions-screening results; assists with onboarding decisions, EDD triage, document-classification.
- **Transaction-monitoring agent**: agent reads transaction streams; assists with alert disposition, narrative drafting, escalation triage. BSA officer is a co-reviewer.
- **Customer-support agent for fintech consumer flows**: agent reads account state, transaction history; assists with dispute initiation, refund processing within thresholds, communication drafting. CFPB UDAAP and Reg E reach.
- **Sponsor-bank operations agent for BaaS**: agent runs at sponsor bank or at fintech with read/write to sponsor-bank systems; shared-responsibility allocation is the structural question.
- **Fraud-response agent**: agent reads fraud signals; agentic actuation in transaction blocks, customer outreach, dispute initiation.
- **Acquiring agent for merchant flows**: agent reads merchant-onboarding data; assists with merchant-risk decisions; card-network rules apply.

#### Authority-statement constraints specific to payments-fintech

The out-of-scope list at minimum includes: no funds movement outside firm-policy thresholds; no account-status changes that affect customer-money-access (freezes, holds, closures) without supervisor approval; no merchant-status changes without underwriter approval (for acquiring agents); no card-network-rule-violating actions.

For BaaS sponsor-bank flows: the out-of-scope list is bounded by the bank-fintech contract. Agents at the fintech do not actuate sponsor-bank systems outside the contractual envelope; agents at the sponsor bank do not actuate fintech-customer systems outside the same envelope.

#### Tool-inventory expectations

- Per-customer query scoping; cross-customer access is a structural privacy and UDAAP risk.
- Funds-movement tools are not in the agent's inventory unless explicitly authorised; if present, blast-radius framing is required ("could move up to $X per minute").
- Communication tools: blast-radius framing; CFPB UDAAP and Reg E preservation reach.
- Card-network-touching tools (chargebacks, retrievals, dispute lifecycle): card-network-rule-aligned scoping.
- BaaS-shared tools: the bank-fintech contract names the tool inventory each side controls; the controls review reflects this allocation.

#### Human-oversight bar specific to payments-fintech

- For onboarding decisions: notify-and-revocable is acceptable for low-risk segments; block-and-wait for high-risk segments and EDD-triggered cases.
- For transaction-monitoring alert closure: block-and-wait analyst review per BSA officer policy.
- For customer-facing communication generation: block-and-wait or notify-and-revocable per UDAAP risk; CFPB UDAAP scrutiny applies.
- For BaaS shared flows: the human-oversight design names the responsible function on each side of the bank-fintech boundary; allocation is in the contract.

#### Monitoring signals the overlay adds

- Onboarding agents: KYC-decision distribution, sanctions-hit handling cadence, EDD-triage rate.
- Transaction-monitoring agents: false-positive-rate, alert-closure-rate, alert-reopen-rate, BSA officer override rate.
- Customer-support agents: complaint-rate (UDAAP signal), Reg E dispute-handling timing compliance.
- Fraud-response agents: false-positive customer-block rate, customer-recourse channel volume.
- Acquiring agents: merchant-risk decision distribution, chargeback-rate by merchant cohort.
- BaaS shared signals: per the contract; both sides monitor.

#### Incident-response and regulator-notification triggers

- 12 CFR Part 53 / Part 225 / Part 304 — for bank service providers and bank-affiliated entities, 36-hour notification.
- NYDFS Part 500 §500.17(a) — for NY-licensed entities.
- SEC 8-K Item 1.05 — for public registrants.
- GLBA Safeguards Rule (16 CFR §314.5(d)) — for FTC-scope non-bank entities.
- State money-transmitter regulator notification — per state.
- BaaS sponsor-bank notification chain runs first; sponsor bank then runs the federal regulator chain.
- Card-network breach-notification chains where card-network rules apply.

#### Recommended-action items the overlay surfaces

- For BaaS arrangements, the bank-fintech contract reflects the controls review's findings (notice rights, audit rights, off-switch ownership, IR-runbook integration, monitoring data sharing).
- For state money-transmitter-licensed entities, the controls review references the per-state licensing footprint and the most-prescriptive state's expectations.
- For BSA/AML-touching agents, BSA officer sign-off on the residual-risk acceptance.
- For consumer-facing agents, UDAAP risk-framing in the residual-risk view; complaint-rate baseline before go-live is non-optional.
- For card-network-touching agents, card-network-rule alignment is recorded in source trace.

#### Common pitfalls specific to payments-fintech

- BaaS sponsor-bank: assuming the fintech's controls are sufficient. The sponsor bank is accountable under the interagency third-party guidance; the controls review records the sponsor-bank-side coverage independently of the fintech's own coverage.
- Treating onboarding agents as out-of-scope of BSA/AML. KYC-decision assistance shapes onboarding outcomes; FinCEN expectations apply to the firm's overall KYC program.
- Omitting state money-transmitter licensing footprint from the authority statement. State patchwork is the firm's responsibility to maintain; the agent's geographic scope reflects it.
- Treating the 36-hour banking notification rule as out-of-scope because the firm is a fintech. If the firm is a bank service provider, the rule's bank-service-provider obligations apply.
- Designing post-hoc sampling oversight on transaction-monitoring alert closure. Block-and-wait analyst review is the BSA-officer-policy norm; deviations require explicit BSA officer sign-off and sampling-rate evidence.
