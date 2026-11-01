# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Sector overlay: banking — board AI risk pack

Loaded when the scope names banking. The overlay carries content that lands in the pack, not background reading. An overlay loaded but not reflected in the pack body is the standing failure mode.

#### Framing

The pack at a banking holding company aligns to the board's standing oversight of the risk-governance framework. For OCC Heightened Standards covered banks, the AI risk committee (or the AI section of the board risk committee) sits inside that framework. The pack carries the joint interagency Revised Guidance on Model Risk Management (OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17 2026; supersedes SR 11-7 and SR 21-8) for traditional models in scope, with the GenAI/agentic scope exclusion (footnote 3) noted. For GenAI and agentic use cases the substantive anchor is NIST AI RMF and ISO/IEC 42001. BCBS 239 data confidence framing applies to the AI inventory aggregation where the firm is a G-SIB or D-SIB.

Standalone AI risk committees are common at the larger bank holding companies; mid-cap regionals more often run AI as a section of the board risk committee. The pack's depth and the cadence flex accordingly.

#### Inventory state

- Tier taxonomy aligns to the firm's model risk policy. SR 11-7 framing of model materiality, complexity, and reliance is the typical basis. Where the firm's AI risk-rating taxonomy diverges from model tiering, both are reported (model-tier and AI-tier).
- Inventory completeness is the recurring exam topic. OCC continuous-monitoring letters and FRB SR 11-7 horizontal reviews recur on this point. The inventory completeness statement in Appendix C carries the second-line position.
- BCBS 239 data confidence label is required for G-SIB and D-SIB firms; recommended for any firm aggregating the AI inventory through enterprise data infrastructure.

#### Top AI risks

Banking-specific risk vocabulary lands here:

- Consumer-credit decisioning fairness exposure (ECOA / Reg B), with the conduct cross-cutting overlay providing the depth.
- BSA/AML transaction-monitoring model performance and threshold-tuning posture (FFIEC BSA/AML examination expectation).
- Fair-lending posture on AI-touched products (Reg B §1002.9 adverse-action posture; CFPB Circulars 2022-03 / 2023-03 are **withdrawn May 12, 2025; historical only**).
- Vendor concentration on foundation-model providers, where the firm's GenAI bets are concentrated.
- Cyber surface from AI-enabled threats, where the cyber cross-cutting overlay carries the NYDFS October 2024 framing for NY-footprint firms.

#### In-flight reviews and decisions

Pre-prod gate decisions on consumer-credit AI use cases that touch ECOA / Reg B require legal and consumer compliance sign-off in addition to model risk; the pack flags the cross-functional review state. Foundation-model swap approvals for production tier-1 and tier-2 use cases are committee items at most banks; the pack carries the swap pipeline.

#### Regulator and exam interactions

Federally regulated banks: open MRAs and MRIAs from FRB, OCC, FDIC. The SR 12-17 framing for the FRB's expectation that the committee manages, not just counts, the open population is the standing reference for the over-age item commentary. CFPB exam findings on AI-touched consumer products land here when the firm has CFPB jurisdiction.

State banking interactions land here where the firm has state-chartered subsidiaries; NYDFS for NY-footprint firms covers both cyber (Part 500) and AI in financial services (where in scope).

#### Foundation-model and AI vendor exposure

The interagency third-party guidance (OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023) is the framing reference for the vendor exposure section at banks. Foundation-model providers, evaluation vendors, RAG infrastructure, and agent platforms are all in scope of the third-party risk-management lifecycle. The pack carries the vendor exposure with the third-party-guidance lens; depth lives in `vendor-diligence` outputs in AI-vendor mode.

#### AI governance maturity posture

Banking firms typically anchor the maturity narrative to NIST AI RMF Govern function (Govern 1.x organisational governance, Govern 4.x accountability, Govern 6.x third-party considerations) plus SR 11-7 §III governance posture. The maturity narrative explicitly addresses board oversight (SR 11-7 §II), the policy-and-standards layer, the inventory-of-record posture, the model-validation function independence, and the third-party-AI accountability framing.

#### CCAR and stress test linkage

For Category I-IV firms, the pack carries the CCAR governance reporting cadence linkage where AI is implicated in a material model used in stress projections (consumer-credit loss models, deposit attrition models, op-loss models). The board AI risk committee oversees AI governance; CCAR oversight sits with the board risk committee or capital management; the pack notes the cross-reference where applicable.

#### Sign-off block

For banks: the AI Governance Lead, the head of model risk, and the chief risk officer. For Heightened Standards covered banks, the chief risk executive is named.

## capital-markets

### Sector overlay: capital markets — board AI risk pack

Loaded when the scope names capital markets (broker-dealer, investment adviser, or both). The overlay carries content that lands in the pack, not background reading.

#### Framing

The pack at a broker-dealer or investment adviser aligns to the firm's compliance and risk program rather than to a bank-style risk-governance framework. For investment advisers, SEC Rule 206(4)-7 sets the compliance program rule including the annual review; the AI risk committee (or the firm's risk committee with an AI section) is one of the standing inputs to the annual review. For broker-dealers, FINRA AI guidance and existing supervisory and risk-management frameworks apply to AI applications in the securities business.

Adviser firms typically run the AI committee as a firm-level enterprise view (firm fiduciary risk, firm operational risk, firm vendor risk). Fund-level AI items go to the fund boards via separate reporting; cross-link if material to both, do not collapse. Sponsor-firm AI items at insurance-affiliated advisers cross-link to the insurance overlay where applicable.

#### Inventory state

- AI-touched activities surface explicitly: investment research and recommendation, surveillance and trade monitoring, execution algorithms and routing, client-facing AI assistants, marketing and client communications, operations and middle-office automation.
- Tier taxonomy is firm-specific. Common patterns at advisers map fiduciary-risk impact to tier; at broker-dealers map customer-facing exposure and best-execution impact to tier.
- The AI-generated-content inventory is its own line: which AI applications produce client-facing content (research, recommendations, communications) and which produce internal-only content. SEC Marketing Rule scope hinges on the distinction.

#### Top AI risks

Capital-markets-specific risk vocabulary lands here:

- Fiduciary-risk exposure from AI-supported recommendations (advisers), with the integration to the firm's fiduciary-duty framework.
- Best-execution exposure from execution algorithms or AI-driven routing (broker-dealers), with the SEC Rule 605 / 606 reporting linkage and FINRA Rule 5310 framing.
- Surveillance gap or false-positive posture from AI-driven surveillance (broker-dealers), where the regulator-driven look-back is a recurring exam topic.
- Marketing Rule exposure on AI-generated client communications (advisers), where the testimonial / endorsement / performance-presentation framing applies.
- Books-and-records preservation posture for AI-generated content supporting recommendations or trading decisions (advisers under Rule 204-2; broker-dealers under Rules 17a-3 / 17a-4).

#### In-flight reviews and decisions

Pre-prod gate decisions on AI applications that produce client-facing content require legal and compliance sign-off in addition to risk; the pack flags the cross-functional review state. Foundation-model swap approvals for production AI applications producing client-facing content require Marketing Rule re-assessment.

#### Regulator and exam interactions

SEC Division of Examinations on AI sweeps (where active), SEC enforcement on AI-related disclosures and Marketing Rule violations, FINRA exams that include AI scope, NYAG and state AG inquiries on AI in financial services. The CFTC where the firm has commodity pool or swap-dealer activity.

The Rule 206(4)-7 annual review is the standing input from the program; AI scope items in the annual review surface to the AI risk committee or the firm risk committee.

#### Foundation-model and AI vendor exposure

Vendor concentration on foundation-model providers is the increasing committee topic at adviser firms operating GenAI assistants for research, client communications, and operations. The pack carries the vendor exposure with the cross-reference to the firm's vendor risk management framework and the SEC adviser examination focus on third-party risk.

#### AI governance maturity posture

Capital-markets firms typically anchor the maturity narrative to NIST AI RMF Govern function plus the firm's compliance program (Rule 206(4)-7 for advisers; FINRA supervisory framework for broker-dealers). The maturity narrative addresses:

- Compliance program integration with AI use cases (the named CCO has visibility and accountability).
- Fiduciary-duty framework integration where the firm is an adviser.
- Marketing Rule scoping for AI-generated content.
- Books-and-records preservation posture.
- Supervisory framework coverage of AI-driven surveillance and execution decisions where the firm is a broker-dealer.
- Third-party AI accountability framing.

#### Sign-off block

For advisers: the AI Governance Lead (or the named senior officer with AI accountability), the chief compliance officer, the chief operating officer or president, and the head of model risk where the firm has a model risk function. For broker-dealers: the AI Governance Lead, the chief compliance officer, the head of supervision, and the head of risk management.

## insurance

### Sector overlay: insurance — board AI risk pack

Loaded when the scope names insurance. The overlay carries content that lands in the pack, not background reading.

#### Framing

The pack at an insurer aligns to the NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023) AIS Program elements: governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness. The board (or the committee designated under the AIS Program) is the standing audience. State adoption of the NAIC Bulletin is tracked by the NAIC AI Working Group; binding status varies by jurisdiction. For NY-footprint life-insurance writers, the NYDFS Insurance Circular Letter (January 2024) on AI and ECDIS in life-insurance underwriting is the additional anchor; for CO life-insurance writers, the Colorado SB 21-169 implementing regulation is the anchor.

The pack rolls into the Own Risk and Solvency Assessment (ORSA) governance cadence at the holding-company level. For insurers that file an ORSA Summary Report under Model #505, the AI section of ORSA Summary Report Section 1 (governance) and Section 3 (risk capital) consumes a brief from this pack rather than re-anchoring the AI sources.

#### Inventory state

- The AIS Program element of "documentation" requires a detailed AI use-case inventory with intended use, data sources, performance, and oversight. The inventory state section in the pack reports the inventory in NAIC AIS Program vocabulary.
- AI-touched lines of business surface explicitly: life underwriting, P&C underwriting, claims handling, claims fraud, marketing and lead generation, customer service, agent productivity, actuarial pricing and reserving.
- Tier taxonomy is firm-specific. Common patterns map AIS Program oversight intensity to tier (high-impact AI = AIS Program full elements; lower-impact AI = scaled elements with documentation evidence).

#### Top AI risks

Insurance-specific risk vocabulary lands here:

- Unfair discrimination exposure in life and health underwriting and pricing (NAIC #880 framing, NAIC AI Bulletin fairness element, NYDFS Circular Letter, CO SB 21-169 framework).
- ECDIS sourcing and accuracy posture for life-insurance writers, where the data-source inventory and the consumer-recourse mechanism are recurring DOI topics.
- AI in claims handling: fairness, accuracy, transparency to insureds, recourse pathways. Multistate consumer-protection enforcement on claims AI is the increasing exam focus.
- Foundation-model vendor concentration in claims summarisation, customer-service assistants, and underwriting support, where the firm's GenAI bets are concentrated.
- Third-party AI accountability under the AIS Program element: the firm retains AIS Program accountability for vendor-supplied AI; vendor self-attestation is not sufficient evidence.

#### Regulator and exam interactions

State DOI inquiries and information requests land here; the inventory of state DOI interactions on AI is part of the standing pack. NAIC inquiries through the AI Working Group when the firm is a participant. NYDFS for NY-footprint life-insurance writers; Colorado DOI for CO writers; California DOI inquiries on AI in claims handling. Multistate market-conduct exams that include AI scope land here.

#### Foundation-model and AI vendor exposure

Third-party AI accountability is an explicit AIS Program element. The pack carries vendor exposure with the AIS Program lens: governance documentation for the vendor relationship, evidence of vendor risk management, evidence the firm has tested and validated the vendor AI for the firm's use case, monitoring evidence, and the third-party-AI documentation set. The vendor exposure section consumes outputs from `vendor-diligence` in AI-vendor mode and adds the AIS Program-specific overlay.

NAIC outsourcing standards (where adopted by the relevant state DOIs) layer over the third-party-AI framing.

#### AI governance maturity posture

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

#### Sign-off block

For insurers: the AI Governance Lead (or the named senior officer accountable under the AIS Program), the head of model risk, the CRO, the chief actuary where actuarial AI is in scope, and the head of consumer compliance where claims and underwriting AI is in scope.

## payments-fintech

### Sector overlay: payments-fintech — board AI risk pack

Loaded when the scope names payments-fintech. The overlay carries content that lands in the pack, not background reading.

#### Framing

The pack at a payments or fintech firm typically operates without the same chartered-institution governance machinery as a bank holding company. The audience is the firm's risk committee or program-management committee, with AI risk surfaced as a standing section. For BaaS partners and fintechs operating under a sponsor-bank arrangement, the pack feeds the sponsor-bank's third-party AI oversight and the firm's own management committee. The sponsor-bank governance reporting cadence and the firm's program-management committee cadence are both reflected in the pack distribution.

#### Inventory state

- AI-touched activities surface explicitly: fraud and AML transaction monitoring, customer onboarding and KYC, dispute and chargeback handling, customer-service assistants, lending decisioning where the firm is a lender or a loan originator under partnership, marketing and acquisition.
- The sponsor-bank-shared AI inventory is its own line: which AI applications process sponsor-bank customer data or feed sponsor-bank decisions, and which are firm-only.
- Tier taxonomy is firm-specific; for sponsor-bank partnerships, the sponsor's tier taxonomy may apply for shared AI use cases.

#### Top AI risks

Payments-fintech-specific risk vocabulary lands here:

- Sponsor-bank consent and oversight posture for shared AI use cases. The 2023 interagency third-party guidance set the bar for sponsor-bank accountability for fintech-developed models; the fintech pack carries the firm-side view.
- Fraud and AML model performance, with the cross-reference to the BSA/AML program (where the firm is the BSA-covered party) or to the sponsor-bank's BSA program (where the sponsor retains BSA responsibility).
- Customer-onboarding KYC AI exposure, including disparate-impact testing posture and consumer-disclosure framing.
- Lending decisioning AI exposure under ECOA / Reg B where the firm is a lender; the conduct cross-cutting overlay carries the depth.
- Foundation-model vendor concentration in customer-service assistants, where the firm's GenAI bets are concentrated.
- Cyber surface from AI-enabled threats targeting customer-onboarding and KYC processes (synthetic identity, deepfake-driven onboarding fraud), where the cyber cross-cutting overlay carries the depth.

#### Regulator and exam interactions

CFPB scrutiny on consumer-finance AI use cases (where in scope under the firm's authority); FinCEN on BSA-related AI; OCC, FRB, FDIC scrutiny landing through the sponsor-bank's third-party oversight where the firm operates under partnership; state regulator inquiries (state money transmitter regulators where in scope; state lending regulators where the firm is a lender). NY DFS for NY-footprint firms.

The sponsor-bank's exam findings on the partnership often surface as derivative findings to the fintech; the pack carries these as a separate sub-bucket under regulator interactions.

#### Foundation-model and AI vendor exposure

Vendor concentration is typically high at payments-fintech firms because the firm relies on third-party infrastructure for foundation models, evaluation, and increasingly customer-service assistants. The pack carries the vendor exposure with the cross-reference to the firm's vendor management framework and the sponsor-bank's third-party AI oversight where the sponsor-bank consumes the same vendor exposure.

#### AI governance maturity posture

Payments-fintech firms typically anchor the maturity narrative to NIST AI RMF Govern function, the interagency third-party guidance for sponsor-bank arrangements, and where applicable BSA/AML program expectations for AI-driven monitoring. The maturity narrative addresses:

- Sponsor-bank accountability and partnership governance for shared AI.
- BSA program integration where the firm is BSA-covered.
- Consumer-protection program integration for customer-facing AI.
- Cyber program integration covering AI-enabled threats and the firm's own use of AI.
- Third-party AI accountability framing.

#### Sign-off block

For payments-fintech firms: the AI Governance Lead (or the named senior officer with AI accountability), the chief risk officer or head of risk, the chief compliance officer, the BSA officer where the firm is BSA-covered, and the head of vendor management. For BaaS partners, the sponsor-bank relationship owner is named in the distribution list.
