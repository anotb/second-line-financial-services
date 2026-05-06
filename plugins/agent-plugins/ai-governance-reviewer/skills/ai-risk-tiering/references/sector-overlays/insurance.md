# Insurance sector overlay for ai-risk-tiering

When the engagement-scope record names sector `insurance`, this overlay tells the tier rubric what is insurance-specific and which named bulletins set the bar. Tier names and cutoffs are firm policy; this overlay names which factors elevate, which gates trigger by default, and which re-tiering events to name.

Loaded by: `ai-risk-tiering/SKILL.md` when `engagement_scope.sector_overlay_set` includes `insurance`. Source content derived from the insurance lead's overlay snippets in the phase-1 spec sheets, mapped here into the tiering context. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023) is the spine. The Bulletin frames a graduated expectation: greater oversight where AI affects consumers in eligibility, premium, claims, or coverage; lighter touch where the use case is back-office. The tier rubric reads "potential to harm consumers" as the test that drives elevation, not a bolt-on label.
- Colorado Division of Insurance regulation implementing SB 21-169 (life-underwriting AI / ECDIS) [verify regulation number].
- New York DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting (January 2024).
- California DOI bulletin on AI use in insurance.
- NAIC Unfair Trade Practices Act (Model #880) for unfair-claims-settlement and unfair-discrimination framing in claims AI.
- NAIC ORSA (Model #505) for enterprise materiality.
- HIPAA Privacy and Security Rules where PHI is in the data flow.

## Insurance-specific tier criteria

The insurance use-case categories fall into a graduated structure that the tier rubric absorbs. The categories are anchored to the NAIC Bulletin; tier values remain firm policy.

### Accelerated underwriting AI (life and health)

- The use case influences eligibility, rating class, premium, or coverage in life or health. Customer-binding by definition.
- ECDIS likely in the input set; CO regulation and NY DFS Circular Letter elevate the regulatory factor when the operating footprint includes those states.
- HIPAA touch is frequent (prescription history, medical underwriting data); privacy factor elevates.
- AIS Program element-by-element coverage demanded under the NAIC Bulletin; documentation factor reads as primary.
- Default tier elevation: tier-1 in firm-policy-typical mappings; gates include full validation, AIS Program element status, ECDIS-provenance review, state-DOI-strictest disclosure posture.

### Claims AI (FNOL triage, severity prediction, fraud-indicator scoring, claims chatbot)

- The use case affects claim acceptance, denial, severity, or fraud-indicator routing. Customer-binding for any decision that touches claim outcome.
- NAIC Model #880 unfair-claims-settlement standards apply regardless of decision technology; conduct factor elevates.
- State unfair-claims-settlement-practices acts set timing, notice, and reasoned-denial requirements; regulatory factor elevates.
- HIPAA touch is frequent (health and life claims); privacy factor elevates.
- Where the AI is consumer-facing (claims chatbot), UPL and producer-licensing boundaries matter and the conduct factor scores at minimum medium.
- Default tier elevation: tier-1 or tier-2 in firm-policy-typical mappings depending on autonomy and customer-facing posture; gates include claim-handling control family review against Model #880 and state UCSPA.

### Marketing AI to existing policyholders

- The use case touches product targeting, replacement-risk scenarios, or annuity suitability.
- NAIC Model #275 [verify model number] for annuity suitability, where in scope, elevates the conduct factor.
- TCPA / Do-Not-Call where outbound communications are involved.
- Default tier elevation: tier-2 in firm-policy-typical mappings when annuity suitability is implicated; tier-3 otherwise.

### Pricing / rating ML factors

- State DOI rate-filing and prior-approval regimes apply where the model touches filed rates; the regulatory factor elevates and the rate analyst is a downstream audience.
- Unfair-discrimination test under Model #880 applies; the fairness vocabulary differs from ECOA / Reg B disparate-impact framing.
- Default tier elevation: tier-1 or tier-2 depending on filed-rate reach and state footprint.

### Agent-AI co-pilots (producer-AI tools)

- Suitability and best-interest standards apply; the human-in-the-loop control must be designed against those standards rather than against generic AI fairness.
- Default tier elevation: tier-2 in firm-policy-typical mappings when the co-pilot influences suitability or best-interest analysis.

### Back-office AI (call-centre summarisation, mailroom OCR)

- No customer-facing decision; no rate or claim impact; no PHI unless flagged.
- Default tier: tier-3 or tier-4. AIS Program documentation expectations remain (proportional).

## Cross-cutting tier modifiers

- **State DOI bulletin in operating footprint**: the presence of a state DOI bulletin on AI in insurance in the operating footprint raises the disclosure and governance demands of the tier (not necessarily the inherent risk). The strictest applicable state sets the floor.
- **ORSA materiality**: any AI use case meeting the carrier's ORSA materiality threshold under Model #505 lands in the top tier for governance purposes regardless of the rubric's other dimensions.
- **HIPAA touch**: any insurance AI use case that processes PHI gets a privacy-flag tier modifier; the privacy cross-cutting overlay carries the data-sensitivity scoring.
- **Vendor-supplied AI**: per NAIC Bulletin December 2023 third-party AI accountability, vendor-supplied AI used on the carrier's policies elevates the vendor-dependence factor and pulls AIS Program third-party-AI element coverage into triggered gates.
- **TPA / claims-administrator operation**: where the AI runs at a TPA on the carrier's policies, NAIC Insurance Data Security Model Law (Model #668) §4.F third-party service-provider obligations apply. The tier decision names the TPA's controls as the carrier's controls for §4.F purposes.

## Worked tier-criterion table (illustrative, firm policy governs)

| Use case category | Default tier | Dominant factor elevation | Default triggered gates |
|---|---|---|---|
| Accelerated underwriting (life/health, ECDIS) | tier-1 | customer_impact, conduct, data_sensitivity (PHI), regulatory (CO/NY) | Full validation; AIS Program coverage; ECDIS provenance; state-DOI strictest-applicable disclosure |
| Claims AI (decisioning) | tier-1 or tier-2 | customer_impact, conduct (Model #880), data_sensitivity (PHI) | Claim-handling control review; Model #880 UCSPA controls; HIPAA controls; UPL boundary check on chatbots |
| Pricing / rating ML | tier-1 or tier-2 | regulatory (state rate filing), conduct (#880 unfair discrimination) | Rate-filing alignment; unfair-discrimination test; state DOI exam-prep posture |
| Marketing AI (annuity/suitability) | tier-2 | conduct (#275 suitability), regulatory (TCPA) | Suitability control review; outbound communications controls |
| Agent-AI co-pilots | tier-2 | conduct (suitability / best-interest) | Human-in-the-loop control design against suitability standards |
| Back-office AI (OCR, summarisation) | tier-3 or tier-4 | none dominant | AIS Program proportional documentation |

## Insurance-specific re-tiering triggers

Add to the re-tiering trigger block for insurance sector use cases:

- State DOI bulletin adoption or amendment in the operating footprint (CO, NY, CA, others). Owner: regulatory change function with insurance compliance. Detection: regulatory horizon scan.
- ORSA materiality reassessment. Owner: ORSA function. Detection: annual ORSA review or material business change.
- ECDIS source addition or substitution. Owner: data governance with insurance compliance. Detection: change-management notice.
- HIPAA BAA posture change with a vendor handling PHI. Owner: vendor management with privacy office. Detection: vendor contract management.
- TPA AI scope change on the carrier's policies. Owner: outsourcing governance. Detection: TPA contract change-control.

## Common pitfalls in insurance tiering

- Treating the NAIC Bulletin as US-uniform; adoption is state-by-state and the Bulletin is itself non-binding until state adoption.
- Importing ECOA / Reg B fairness vocabulary without translating to Model #880 unfair-discrimination framing; the test is different and a state DOI rate analyst will read the wrong artefact.
- Tiering claims AI low because the chatbot "just answers questions"; Model #880 fair-claims-settlement standards apply regardless of who or what produces the claim decision, and an unmonitored chatbot is a control gap not a low-tier feature.
- Missing HIPAA touch on a life-underwriting AI using prescription-history data; the privacy factor stays low when it should be high.
- Forgetting that the TPA's controls are the carrier's controls under Model #668 §4.F; tiering the use case as if the TPA's posture absolves the carrier.
- Treating the AIS Program elements as a checklist rather than a structure; the tier decision evidences each element with source-trace pointers, not just a tick.
