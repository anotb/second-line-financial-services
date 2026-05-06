# Insurance overlay snippets

Plugin: `sector-plugins/insurance-risk-compliance`
Phase: 1 (overlay outlines that feed capability-skill spec sheets and v1 phase-2 content).

These outlines define what the insurance overlay reference (`references/sector-overlays/insurance.md`) must cover inside each named capability skill. They are the v1 home for sector flavor that does not warrant a standalone insurance-only skill.

Two overlays absorb deprecated v0.2 sector skills:

- `ai-governance-model-risk/ai-act-triage` absorbs `insurance-ai-act-triage`.
- `ai-governance-model-risk/agentic-ai-controls` absorbs `claims-ai-controls`.

These two overlays are written deeper than the others because they carry the substance of the deprecated skills.

---

## ai-governance-model-risk / ai-act-triage

Purpose: when the capability skill is run on an insurance-sector AI use case, the insurance overlay tells the reviewer what to test for, what regulators are involved, and which named bulletins set the bar.

- US-deep frame: NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers, December 2023, is the spine. Capture the AIS Program structure (governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness) and tie each capability triage finding back to an AIS Program element. The Bulletin itself is not law; track state-by-state adoption status (the NAIC AI Working Group adoption tracker is the public reference).
- State DOI bulletins to enumerate by name and date: Colorado SB 21-169 implementing regulation (governance and risk management of ECDIS and predictive models in life-insurance underwriting); NY DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting (January 2024); California DOI bulletin on AI use in insurance. Each carries its own scoping (life-only in CO and NY; broader in the NAIC Bulletin and CA bulletin) and its own consumer-recourse and disclosure expectations.
- Insurance-relevant AI use-case categories the triage must explicitly recognise: accelerated underwriting (life and health), claims AI (triage, FNOL, severity prediction, fraud-indicator scoring, claims-handling chatbots), pricing / rating ML factors and ECDIS use, marketing-AI for product targeting, agent-facing AI (illustration generation, suitability triage), back-office AI (call-center summarisation, mailroom OCR). Each category lights up different state-DOI bulletins.
- Cross-walk to the EU AI Act: insurance pricing and risk-assessment in life and health is named as a high-risk use case under Annex III of Regulation (EU) 2024/1689. US carriers writing in EU branches or doing reinsurance with EU cedents can still inherit the obligation. The overlay should make the cross-walk explicit so the capability skill flags the EU-applicability question.
- HIPAA scope check: any AI touching PHI (health-claims AI; life-and-health underwriting AI using prescription-history or medical data) needs a HIPAA Privacy and Security Rule cross-check that the capability skill alone will not produce.
- Producer / agent licensing: any consumer-facing AI that takes actions on policies (binding, quoting commitments, surrendering, paying claims) can trigger producer licensing questions; flag for the licensing function.
- ORSA exposure: if the AI use case is enterprise-material, it belongs in the ORSA Summary Report under the Model #505 framing. The overlay should give the criteria for materiality.
- Fairness vs unfair-discrimination terminology: capability triage uses fairness and bias; insurance regulators use unfair discrimination under Model #880 with a different test. The overlay should hold both vocabularies and translate one to the other so the artifact reads correctly to a state DOI rate analyst.
- Vendor-AI accountability: the NAIC Bulletin Dec 2023 holds the carrier accountable for vendor and third-party AI used on its policies. Cross-link to the `vendor-diligence` insurance overlay so the triage flags vendor-AI as an explicit deliverable rather than a footnote.
- Output-template additions for insurance: AIS Program element-by-element status; per-state DOI bulletin status; ECDIS provenance for any data-input the AI uses; consumer-recourse channel; producer-licensing posture if consumer-facing; ORSA inclusion if material.

---

## ai-governance-model-risk / agentic-ai-controls

Purpose: when the capability skill reviews controls for agentic AI in an insurance setting (claims AI, FNOL bots, agent-AI co-pilots, autonomous-action systems), the overlay sets the insurance-specific control bar.

- Claims-AI is the dominant insurance-sector use case for agentic systems. The overlay must be opinionated about claims-AI controls because it absorbs the deprecated `claims-ai-controls` skill. Specifically:
  - NAIC Unfair Trade Practices Act, Model #880, fair-claims-settlement standards apply regardless of who or what produces the claims decision. Agentic AI cannot move the standard.
  - State unfair-claims-settlement-practices acts (most states have one; cite by state when used) set timing, notice, documentation, and reasoned-denial requirements. The overlay should list the standard control families: prompt-acknowledgement, reasoned-denial drafting, complaint flow, supervisor-override path, audit trail, denial-letter human review.
  - NAIC Bulletin Dec 2023 expectations apply: AIS Program element-by-element coverage of the agentic claims system, including governance, third-party AI accountability, monitoring, transparency.
  - State DOI bulletins on AI use (CO, NY DFS, CA) inform the disclosure and consumer-recourse posture for claims AI even where the bulletins are scoped to underwriting; carriers are increasingly extending the same controls to claims to anticipate state action.
- HIPAA layer on health-claims and life-claims AI: the agent reads PHI in many flows; HIPAA Privacy and Security Rule controls (workforce training, access logs, minimum-necessary, breach-notification) apply to the agent and to its vendor.
- Producer-licensing / unauthorised-practice-of-law check on consumer-facing claims chatbots: where the bot crosses into legal advice or coverage opinions, the carrier risks UPL exposure on top of unfair-trade-practices exposure. The overlay should flag the boundary.
- TPA / claims-administrator overlap: where the agentic system runs at a TPA or claims administrator on the carrier's policies, NAIC Insurance Data Security Model Law (Model #668) §4.F third-party service-provider obligations apply. Cross-link to `insurance-outsourcing-review` so the artifact does not double-cover the TPA contract.
- Marketing-AI agentic systems that contact policyholders trigger UDAP exposure under Model #880 §4 (unfair claims and unfair acts) and TCPA / Do-Not-Call where outbound communications are involved. Brief, named overlay.
- Agent-AI (the producer-AI, not the autonomy concept) co-pilot tools used by agents and brokers: suitability-rule overlap on annuity sales (NAIC Suitability in Annuity Transactions Model Regulation, Model #275 [verify model number]) and best-interest standards apply; the human-in-the-loop control must be designed against those standards, not against generic AI fairness.
- ORSA fit: an agentic system that handles claims volume at scale or makes binding-equivalent decisions can be enterprise-material and therefore in scope for the ORSA Summary Report.
- Output-template additions for insurance agentic-AI controls: claim-handling control family status against Model #880 and state UCSPA; HIPAA control-family status; TPA / Model #668 §4.F overlap status; consumer-disclosure posture; AIS Program element status; UPL boundary check; ORSA inclusion if material.
- Common pitfalls to capture in the overlay: relying on a fairness-only test where a fair-claims-settlement test is required; missing the UPL question on chatbots; forgetting that the TPA's controls are the carrier's controls for §4.F purposes; treating the AI Bulletin as US-uniform when it is state-by-state in adoption.

---

## ai-governance-model-risk / ai-risk-tiering

Purpose: insurance-sector tier criteria that the capability tiering rubric must absorb.

- Tier-criteria additions specific to insurance:
  - **Accelerated underwriting and rating-factor AI**: tier elevation when the model influences eligibility, premium, or coverage in life or health; further elevation when ECDIS is in the input set.
  - **Claims AI**: tier elevation when the AI affects claim acceptance, denial, severity, or fraud-indicator routing; further elevation when consumer-facing chatbot is in scope.
  - **Marketing-AI to existing policyholders**: tier elevation when product-suitability or replacement risk could be implicated (NAIC #275 [verify] for annuities).
  - **Vendor-supplied AI**: tier elevation per NAIC Bulletin Dec 2023 third-party AI accountability.
- State-by-state tier-modifier: presence of a state DOI bulletin on AI in insurance in the operating footprint should raise the disclosure / governance demands of the tier (not necessarily the inherent risk).
- ORSA-materiality cross-check: any AI use case meeting the carrier's ORSA materiality threshold automatically lands in the top tier for governance purposes regardless of the rubric's other dimensions.
- HIPAA-touch flag: any insurance AI use case that processes PHI gets a privacy-flag tier modifier.
- 4-6 bullets for the overlay reference, plus a short worked tier-criterion table in the overlay.

---

## ai-governance-model-risk / llm-vendor-evidence-review

Purpose: insurance-sector evidence-review demands when the LLM vendor is in scope for insurance AI use cases.

- NAIC Bulletin Dec 2023 third-party AI accountability is the spine: the carrier remains accountable for the vendor's AI; evidence-review must show governance and oversight at the carrier level, not just vendor self-attestations.
- Evidence categories specific to insurance: training-data exclusions for prohibited rating factors; bias-evaluation evidence framed against unfair-discrimination (#880) terminology, not only generic fairness; safety evidence for chatbot use in claims and quoting; HIPAA-compliance posture where PHI is in the input or output stream; data-residency for state-licensed carriers operating in states with insurance-data-localization expectations.
- TPA / MGA crossover: where the LLM vendor serves a TPA or MGA on the carrier's policies, NAIC Insurance Data Security Model Law §4.F applies; evidence must include the TPA's own oversight of the vendor, not just the carrier's.
- Producer-licensing on consumer-facing LLM chat surfaces: confirm the use case does not cross into producer activity without licensing.
- State-by-state disclosure expectations from CO regulation, NY DFS Circular Letter, CA bulletin: align the consumer-disclosure language and the consumer-recourse flow to the most-prescriptive state in the footprint.
- 6 bullets for the overlay reference plus a small evidence-element checklist tying to AIS Program elements.

---

## third-party-operational-resilience / vendor-diligence

Purpose: insurance overlay covers what the bank-flavored capability vendor-diligence does not.

- Insurance vendor types the diligence must recognise: MGA, MGU, TPA, claims administrator, underwriting bureau, actuarial outsourcer, IT outsourcer, AI / ML vendor, ECDIS data provider, illustration-software vendor.
- NAIC Insurance Holding Company System Regulatory Act (Model #440) [verify] and Holding Company Model Regulation (Model #450) [verify]: Form B and Form D filings where the counterparty is an affiliate; this is not a federal-banking concept and the capability skill alone will miss it.
- NAIC Insurance Data Security Model Law (Model #668), §4.F third-party service-provider obligations: due-diligence, written-contract, monitoring, incident-response cooperation, breach-notification chain. Distinct from federal banking interagency guidance.
- NAIC Producer Licensing Model Act [verify]: any vendor exercising binding or producer authority requires per-state producer licensing; the diligence checklist must include a per-state producer-licensing confirmation.
- HIPAA business-associate-agreement posture for any vendor handling PHI; cross-link to the privacy cross-cutting overlay.
- NAIC Bulletin Dec 2023 vendor-AI accountability: any vendor providing AI tooling used on the carrier's policies pulls AIS Program third-party-AI elements into the diligence.
- ORSA-fit check: critical outsourced functions belong in the ORSA Summary Report under Model #505.
- 6-8 bullets in the overlay, plus a vendor-type-by-applicable-Model crosswalk table.

---

## third-party-operational-resilience / vendor-diligence (cyber sub-overlay note)

Purpose: insurance-specific cyber additions, paired with the existing cyber cross-cutting reference.

- NAIC Insurance Data Security Model Law (Model #668) is the insurance-specific cybersecurity frame and applies in addition to or instead of NYDFS Part 500 in some states.
- Adoption status of #668 is state-by-state; the overlay should point to the NAIC adoption tracker as the way to scope per-state expectations.
- §4.F third-party-service-provider obligations carry the cyber expectation chain to the vendor and to its sub-processors.
- Incident-response cooperation language has to be in the contract; the overlay should call this out as a frequent gap.

(This sub-overlay can live as a short section inside the main vendor-diligence insurance overlay rather than a separate file.)

---

## risk-reporting / risk-committee-pack

Purpose: ORSA reporting overlay so the capability committee-pack skill produces an artifact a state DOI examiner will accept as ORSA-aligned.

- ORSA Model Act (Model #505) sets the Summary Report structure: risk-management framework, insurer's assessment of risk exposure, group risk-capital and prospective solvency assessment. The overlay should map the capability committee-pack template sections to the ORSA Summary Report sections.
- Material risk categories that the insurance overlay should add to the committee pack: pricing / underwriting risk; reserving risk; reinsurance and credit risk; market and ALM risk; insurance operational risk including outsourced functions; AI risk per NAIC Bulletin Dec 2023 where material; cyber risk per Model #668.
- Stress-testing and prospective-solvency narrative: ORSA expects forward-looking stress and capital-adequacy commentary; the overlay should give the section template.
- Cross-link to NAIC Corporate Governance Annual Disclosure Model Act (Model #305) [verify model number]: the CGAD is the governance counterpart to ORSA and the committee pack often supports both filings.
- State DOI variation: some states require own-risk and solvency assessment in narrative form, others receive it as an attachment; the overlay should flag the variation.
- 5-6 bullets in the overlay, plus a section-by-section mapping table from capability committee-pack sections to ORSA Summary Report sections.

---

## consumer-compliance-fair-lending / fair-lending-test-plan

Purpose: insurance unfair-discrimination overlay, since the capability skill is built around ECOA / Reg B and that is the wrong statutory frame for most insurance work.

- Statutory-frame swap: insurance pricing and underwriting unfair-discrimination is governed by NAIC Unfair Trade Practices Act (Model #880) and state insurance code, not by ECOA / Reg B. The test is different (actuarial justification matters; permitted vs prohibited rating factors are state-defined; protected classes per state insurance code).
- Where ECOA does still apply in insurance contexts: credit-insurance products underwritten through bank channels; some auto-insurance financing arrangements. Flag these explicitly so the capability skill does not misroute the analysis.
- State DOI AI bulletins (CO, NY DFS, CA) introduce disparate-impact-style monitoring expectations on top of the #880 actuarial-justification test for AI-driven rating and underwriting. The overlay should describe how the two coexist (Model #880 is the legal standard; the AI-bulletin expectations are governance and monitoring on top).
- ECDIS-driven rating: external-consumer-data inputs require provenance, consumer-disclosure, and recourse channels per CO regulation and NY DFS Circular Letter; this is closer to fair-lending vocabulary than the #880 vocabulary, and the overlay should give the bridge.
- Class-of-business scope: life and health is the densest area for unfair-discrimination governance; auto and homeowners P&C have their own state DOI rating-bureau frames not covered in v1; reinsurance is largely out of scope.
- HIPAA-touch flag for any test plan touching PHI.
- 6 bullets in the overlay plus a short crosswalk table mapping ECOA / Reg B test-plan elements to Model #880 unfair-discrimination test-plan elements.

---

## Notes

- Each overlay-snippet outline above feeds two artefacts in phase 2: the insurance overlay reference inside the relevant capability skill, and an explicit cross-link from the capability skill's `SKILL.md` so the reviewer is prompted to check the overlay when an insurance use case is in scope.
- Where a model number is marked [verify], phase 2 should confirm the exact NAIC Model number in the live NAIC Model Laws & Regulations index before the citation goes into a SKILL.md.
- No invented regulatory facts. Public sources only.
