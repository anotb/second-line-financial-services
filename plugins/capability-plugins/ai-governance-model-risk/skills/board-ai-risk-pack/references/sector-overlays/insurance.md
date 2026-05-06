# Sector overlay: insurance — board AI risk pack

Loaded when the engagement scope names insurance. The overlay carries content that lands in the pack, not background reading.

## Framing

The pack at an insurer aligns to the NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023) AIS Program elements: governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness. The board (or the committee designated under the AIS Program) is the standing audience. State adoption of the NAIC Bulletin is tracked by the NAIC AI Working Group; binding status varies by jurisdiction. For NY-footprint life-insurance writers, the NYDFS Insurance Circular Letter (January 2024) on AI and ECDIS in life-insurance underwriting is the additional anchor; for CO life-insurance writers, the Colorado SB 21-169 implementing regulation is the anchor.

The pack rolls into the Own Risk and Solvency Assessment (ORSA) governance cadence at the holding-company level. For insurers that file an ORSA Summary Report under Model #505, the AI section of ORSA Summary Report Section 1 (governance) and Section 3 (risk capital) consumes a brief from this pack rather than re-anchoring the AI sources.

## Inventory state

- The AIS Program element of "documentation" requires a detailed AI use-case inventory with intended use, data sources, performance, and oversight. The inventory state section in the pack reports the inventory in NAIC AIS Program vocabulary.
- AI-touched lines of business surface explicitly: life underwriting, P&C underwriting, claims handling, claims fraud, marketing and lead generation, customer service, agent productivity, actuarial pricing and reserving.
- Tier taxonomy is firm-specific. Common patterns map AIS Program oversight intensity to tier (high-impact AI = AIS Program full elements; lower-impact AI = scaled elements with documentation evidence).

## Top AI risks

Insurance-specific risk vocabulary lands here:

- Unfair discrimination exposure in life and health underwriting and pricing (NAIC #880 framing, NAIC AI Bulletin fairness element, NYDFS Circular Letter, CO SB 21-169 framework).
- ECDIS sourcing and accuracy posture for life-insurance writers, where the data-source inventory and the consumer-recourse mechanism are recurring DOI topics.
- AI in claims handling: fairness, accuracy, transparency to insureds, recourse pathways. Multistate consumer-protection enforcement on claims AI is the increasing exam focus.
- Foundation-model vendor concentration in claims summarisation, customer-service assistants, and underwriting support, where the firm's GenAI bets are concentrated.
- Third-party AI accountability under the AIS Program element: the firm retains AIS Program accountability for vendor-supplied AI; vendor self-attestation is not sufficient evidence.

## Regulator and exam interactions

State DOI inquiries and information requests land here; the inventory of state DOI interactions on AI is part of the standing pack. NAIC inquiries through the AI Working Group when the firm is a participant. NYDFS for NY-footprint life-insurance writers; Colorado DOI for CO writers; California DOI inquiries on AI in claims handling. Multistate market-conduct exams that include AI scope land here.

## Foundation-model and AI vendor exposure

Third-party AI accountability is an explicit AIS Program element. The pack carries vendor exposure with the AIS Program lens: governance documentation for the vendor relationship, evidence of vendor risk management, evidence the firm has tested and validated the vendor AI for the firm's use case, monitoring evidence, and the third-party-AI documentation set. The vendor exposure section consumes outputs from `third-party-operational-resilience/skills/vendor-diligence` in AI-vendor mode and adds the AIS Program-specific overlay.

NAIC outsourcing standards (where adopted by the relevant state DOIs) layer over the third-party-AI framing.

## AI governance maturity posture

For insurers, the maturity narrative is anchored to the NAIC Model Bulletin AIS Program elements with each named element addressed:

- **Governance**: board or designated committee oversight, named senior officer accountability, AIS Program policy, integration with enterprise governance.
- **Risk management**: AI risk identification, classification, and management; integration with the firm's enterprise risk management.
- **Testing**: testing approach for AI systems, including unfair discrimination testing for in-scope use cases.
- **Validation**: independent validation for AI systems where in scope of the firm's model risk policy.
- **Third-party AI accountability**: the firm retains accountability for vendor AI; documented evidence required.
- **Monitoring**: ongoing monitoring of AI system performance, including drift and fairness drift.
- **Documentation**: AI use-case inventory, model cards or equivalent, vendor documentation.
- **Transparency**: disclosures to consumers and producers as appropriate to the use case.
- **Fairness**: testing and remediation for unfair discrimination.

The annual AIS Program self-assessment is one of the standing deeper-cycle items in the pack; the quarterly cadence carries the one-paragraph posture summary.

## Sign-off block

For insurers: the AI Governance Lead (or the named senior officer accountable under the AIS Program), the head of model risk, the CRO, the chief actuary where actuarial AI is in scope, and the head of consumer compliance where claims and underwriting AI is in scope.
