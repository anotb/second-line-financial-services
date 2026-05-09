# Example: AI-driven life-insurance pricing model deployed by a US insurer with EU operations

Public-source-derived. No named institution. Triage pattern drawn from EU AI Act (Regulation (EU) 2024/1689) Annex III(5)(c) reference to risk assessment and pricing in life and health insurance, and from the NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023) for the parallel US-side AIS Program touch.

## Input description

A US-headquartered life and health insurer operates a regulated subsidiary in Ireland that writes term-life and group-health business across several EU member states. The first-line product team has built an in-house gradient-boosted pricing model that assigns a risk-class differential at quote time, fed by traditional underwriting variables plus an external-consumer-data feed that summarises prescription-fill patterns. The Irish subsidiary deploys the model on EU-resident applicants. Second-line AI governance has been asked for the EU AI Act triage before pre-prod gate.

Engagement scope provided by `scoping`:

- Institution type: life and health insurer; EU subsidiary in Ireland; US parent.
- Primary regulators in scope of this engagement: Central Bank of Ireland (insurance-supervisor capacity), state DOI for the US parent's home state, NAIC adoption posture for the operating-state footprint.
- Persona: AI Governance Lead (second line), reporting to the CRO; legal and compliance review at sponsor level.
- Sector overlay set: insurance. Cross-cutting overlays: privacy (special-category data via prescription history, GDPR Article 9), conduct (consumer-pricing impact).
- Source posture: public-plus-firm-policy-plus-system-of-record-evidence.

## Output sketch

Triage decision (abbreviated):

- **Use case scope and EU exposure** — the model is operated by the Irish subsidiary on EU-resident applicants; eu_users true, eu_operations true, eu_data_subjects true, market_placement true (system put into service in the EU). EU exposure clear.
- **Operator role** — the Irish subsidiary is provider (in-house build) and deployer (it operates the system on its own quotes). The US parent is not in the chain on EU-side decisions. Role basis: Article 3(3) provider definition (develops and places into service under own name) and Article 3(4) deployer definition (uses under own authority).
- **Article 5 prohibited screen** — clear. Each Article 5 sub-practice screened individually: subliminal techniques (no), exploitation of vulnerabilities (no, pricing context not the targeted vulnerability lens), social scoring (no, single-product underwriting context not general-purpose social evaluation), the law-enforcement and biometric sub-practices (n/a), emotion recognition (no), biometric categorisation (no).
- **Article 6 high-risk classification** — high_risk_annex_III. Annex III row cited: Annex III(5)(c) "AI systems intended to be used for risk assessment and pricing in relation to natural persons in the case of life and health insurance". Article 6(3) derogation considered and not invoked: the system materially influences the risk class and price, not a narrow procedural step.
- **Article 50 transparency** — limited screen; no Article 50 sub-obligation fires by the use case alone (no GenAI output to a natural person, no deepfake, no emotion recognition). Recorded explicitly so reviewer sees the screen ran.
- **GPAI considerations** — gpai_in_scope false. The pricing model is a firm-built classifier, not a GPAI-derived deployment. Recorded explicitly.
- **Obligations summary** (selected, with article reference and operator role):
  - Article 9 risk management system across the lifecycle (provider obligation; AI governance and model risk as joint owners; current state: partial, model risk policy covers some elements).
  - Article 10 data and data governance, including representativeness and bias examination across protected groups (provider; data engineering plus AI governance; partial, GDPR DPIA addresses some elements but Article 10 reach is broader).
  - Article 11 plus Annex IV technical documentation (provider; model owner with AI governance review; gap, model card built under `model-card-builder` covers most but not all Annex IV sub-points).
  - Article 13 transparency to the deployer (provider; in this case provider and deployer are the same legal entity; documented internally rather than to a third-party deployer).
  - Article 14 human oversight (provider designs; deployer operates; partial, current human-in-the-loop is at underwriter referral threshold not at every quote).
  - Article 15 accuracy, robustness, cybersecurity (provider; engineering plus security; partial, robustness tests not yet run on the EU-deployment configuration).
  - Article 26 deployer obligations including human oversight, monitoring, logging, incident reporting (deployer; AI governance plus operations; partial, monitoring stack inherited from US deployment, EU-specific logging not yet wired).
  - Article 27 fundamental rights impact assessment (deployer; required because the deployer is a private operator providing services that include essential private services in the form of insurance under Article 27(1)(b); legal owner; not yet started). FRIA-vs-DPIA reconciliation note: GDPR DPIA exists but does not cover the fundamental-rights elements Article 27 requires; both required.
- **Annex IV documentation deltas** — the model-card-builder output covers Annex IV(1)(a) intended purpose, (1)(b) hardware and software, (2) data, (2)(d) testing, partially. Gaps: (1)(g) human oversight design, (3) monitoring plan in Annex IV form (the firm monitoring plan needs to be re-shaped to Annex IV vocabulary), (4) information about the system's performance in expected and foreseeably misused conditions. Cross-link to `model-card-builder` for the firm-side card; Annex IV is a related but distinct artifact.
- **Registration** — Article 71 registration in the EU database is required for high-risk AI systems before placement on the market or putting into service; registration content per Annex VIII. The Irish subsidiary as provider is the registrant. Owner: legal.
- **Applicable date** — high-risk obligations under Article 6 / Annex III applicable from 2 August 2026 per Article 113. Article 27 FRIA applicable on the same date for deployer obligations. The system is in pre-prod and the date is the binding constraint for go-live readiness.
- **Monitoring for re-classification** — re-triage triggers: change of architecture (e.g., moving to a foundation-model-based pricing assistant), change in EU footprint (adding non-EU markets in scope of the Irish entity, or moving the deployment off the EU subsidiary), AI Office guidance update on Article 6(3) derogation interpretation, change in human-oversight design that materially shifts the deployer's Article 14 posture. Owner: AI Governance Lead, frequency quarterly plus at trigger events.
- **Open questions and dissent** — three items flagged for legal: whether prescription-fill data via the third-party feed qualifies as "data concerning health" under GDPR Article 9 (legal counsel position pending); whether Article 27(1)(b) applies on the credit-institution-or-insurance-undertaking limb to a life insurer specifically (counsel position pending); applicability date interpretation for the deployer-side FRIA (Article 27 obligations effective at the same time as the high-risk obligations themselves under Article 113(3); flagged as confirm).
- **Source trace** — every material claim cited to article and annex; FRIA-applicability claim recorded at confidence medium pending counsel; AI Office Code of Practice referenced where the firm wants to track soft-law expectations on monitoring posture.
- **Insurance overlay notes** — AIS Program element-by-element reconciliation against the NAIC Bulletin (the EU triage is one input to the AIS Program documentation element); ECDIS provenance for the prescription-fill feed flagged as a card field as well; HIPAA touch-flag considered (no PHI on the EU side, prescription data is processed under EU privacy law, but the US parent reuse posture should be reviewed by the privacy team).

## Why this scenario matters

- It exercises the high-risk Annex III(5)(c) row directly: insurance pricing in life and health is one of the named rows, and the route from the use-case description to the row is short. A reviewer must still walk Article 5 explicitly and consider Article 6(3) derogation; the example shows the screen running.
- It exercises the operator-role analysis: the same legal entity is provider and deployer, which is common for in-house builds at EU subsidiaries. The triage records both roles and attaches obligations to each, rather than collapsing to one.
- It exercises Article 27 FRIA: the credit-institution-or-insurance-undertaking limb of Article 27(1)(b) reaches life insurance, but the analysis should be on the record because counsel may want to clarify (and the FRIA-vs-DPIA reconciliation is non-trivial; the firm cannot rely on its existing DPIA alone).
- It exercises the insurance overlay: NAIC Bulletin AIS Program elements are documented in parallel for the US-parent governance posture; ECDIS provenance and HIPAA touch are flagged. The EU triage and the US-side AIS Program coexist; the artifact is explicit about which lens is which.
- It exercises the phasing: the system is in pre-prod and the 2 August 2026 high-risk date is the binding constraint; the triage carries the date and the registration prerequisite.
