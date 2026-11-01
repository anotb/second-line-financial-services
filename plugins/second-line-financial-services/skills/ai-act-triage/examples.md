# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## insurance-pricing-high-risk

### Example: AI-driven life-insurance pricing model deployed by a US insurer with EU operations

Public-source-derived. No named institution. Triage pattern drawn from EU AI Act (Regulation (EU) 2024/1689) Annex III(5)(c) reference to risk assessment and pricing in life and health insurance, and from the NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023) for the parallel US-side AIS Program touch.

#### Input description

A US-headquartered life and health insurer operates a regulated subsidiary in Ireland that writes term-life and group-health business across several EU member states. The first-line product team has built an in-house gradient-boosted pricing model that assigns a risk-class differential at quote time, fed by traditional underwriting variables plus an external-consumer-data feed that summarises prescription-fill patterns. The Irish subsidiary deploys the model on EU-resident applicants. Second-line AI governance has been asked for the EU AI Act triage before pre-prod gate.

Engagement scope provided by `scoping`:

- Institution type: life and health insurer; EU subsidiary in Ireland; US parent.
- Primary regulators in scope of this engagement: Central Bank of Ireland (insurance-supervisor capacity), state DOI for the US parent's home state, NAIC adoption posture for the operating-state footprint.
- Persona: AI Governance Lead (second line), reporting to the CRO; legal and compliance review at sponsor level.
- Sector overlay set: insurance. Cross-cutting overlays: privacy (special-category data via prescription history, GDPR Article 9), conduct (consumer-pricing impact).
- Source posture: public-plus-firm-policy-plus-system-of-record-evidence.

#### Output sketch

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

#### Why this scenario matters

- It exercises the high-risk Annex III(5)(c) row directly: insurance pricing in life and health is one of the named rows, and the route from the use-case description to the row is short. A reviewer must still walk Article 5 explicitly and consider Article 6(3) derogation; the example shows the screen running.
- It exercises the operator-role analysis: the same legal entity is provider and deployer, which is common for in-house builds at EU subsidiaries. The triage records both roles and attaches obligations to each, rather than collapsing to one.
- It exercises Article 27 FRIA: the credit-institution-or-insurance-undertaking limb of Article 27(1)(b) reaches life insurance, but the analysis should be on the record because counsel may want to clarify (and the FRIA-vs-DPIA reconciliation is non-trivial; the firm cannot rely on its existing DPIA alone).
- It exercises the insurance overlay: NAIC Bulletin AIS Program elements are documented in parallel for the US-parent governance posture; ECDIS provenance and HIPAA touch are flagged. The EU triage and the US-side AIS Program coexist; the artifact is explicit about which lens is which.
- It exercises the phasing: the system is in pre-prod and the 2 August 2026 high-risk date is the binding constraint; the triage carries the date and the registration prerequisite.

## internal-tool-minimal-risk

### Example: vendor-hosted GenAI assistant for pension-document summarisation, EU institutional clients

Public-source-derived. No named institution. Triage pattern drawn from EU AI Act (Regulation (EU) 2024/1689) Article 6, Annex III, and Article 50; AI Office guidance on the boundary between deployer and provider obligations for vendor-hosted GenAI; and the EU Code of Practice on General-Purpose AI as a soft-law reference.

#### Input description

A US asset-management group with an Irish UCITS management-company subsidiary deploys a vendor-hosted GenAI assistant inside the institutional-client servicing function. The assistant ingests scheme documents (trust deeds, statements of investment principles, annual reports), summarises them on request, and drafts written responses to scheme-trustee queries that the client servicing team reviews before sending. No automated trade execution, no investment recommendation generation, no client-facing chatbot. Human-in-the-loop on every output. Second-line AI governance has been asked for the EU AI Act triage so the deployment can clear the AI risk committee gate before go-live in the Irish entity.

Engagement scope provided by `scoping`:

- Institution type: UCITS management company (Irish ManCo); US group asset manager; in-scope engagement covers the EU deployment only.
- Primary regulators: Central Bank of Ireland (UCITS-supervisor capacity); Marketing Rule reach considered for the US parent if any output is reused into US-client materials (out of scope of this engagement).
- Persona: AI Governance Lead (second line), reporting to the EMEA CRO; legal review at sponsor level.
- Sector overlay set: capital markets. Cross-cutting overlays: privacy (GDPR; document content includes some scheme-member personal data in tables and trustee correspondence), conduct (institutional-client communication; Marketing Rule reach in US considered separately).
- Source posture: public-plus-firm-policy-plus-vendor-evidence.

#### Output sketch

Triage decision (abbreviated):

- **Use case scope and EU exposure** — assistant is operated by the Irish ManCo on EU institutional clients; eu_users true, eu_operations true, eu_data_subjects true (limited; scheme-member data appears in source documents), market_placement true. EU exposure clear.
- **Operator role** — the Irish ManCo is deployer (uses under its own authority, on its own clients). The vendor is provider of the underlying GenAI system and provider of the GPAI model upstream of the system. The triage notes both relationships and the related obligations the deployer must evidence from the vendor.
- **Article 5 prohibited screen** — clear. Each sub-practice screened: subliminal techniques (no, professional summarisation context), exploitation of vulnerabilities (no, institutional client base), social scoring (no), the law-enforcement and biometric sub-practices (n/a), emotion recognition (no), biometric categorisation (no). Recorded explicitly.
- **Article 6 high-risk classification** — not high-risk. Walk of Annex III row by row recorded:
  - Annex III(1) biometrics — no.
  - Annex III(2) critical infrastructure — no.
  - Annex III(3) education and vocational training — no.
  - Annex III(4) employment, workers' management, access to self-employment — no.
  - Annex III(5)(a) public assistance benefits — no.
  - Annex III(5)(b) creditworthiness or credit scoring of natural persons — no; this is institutional servicing, not consumer credit.
  - Annex III(5)(c) life and health insurance pricing — no.
  - Annex III(5)(d) emergency dispatch — no.
  - Annex III(6) law enforcement — no.
  - Annex III(7) migration, asylum, border control — no.
  - Annex III(8) administration of justice and democratic processes — no.
- **Article 50 transparency** — applies. The assistant generates synthetic content (summaries and draft responses); Article 50 sub-obligations screen as follows:
  - 50(1) interaction with AI system disclosure: applies inside the firm (employees know they are interacting with the assistant; documented in firm policy).
  - 50(2) synthetic content marking: applies; output that leaves the firm to clients carries a disclosure that the draft was AI-generated and reviewed by the named team. Disclosure owner: client servicing.
  - 50(3) deepfake disclosure: not applicable (no synthetic image, audio, or video).
  - 50(4) AI-generated text on matters of public interest: not applicable (institutional-servicing context, not public-interest publication).
  - 50(5) emotion recognition / biometric categorisation disclosure: not applicable.
- **GPAI considerations** — gpai_in_scope true. The vendor's underlying GPAI model is in scope of Article 51-55 obligations on the vendor; the firm's deployer-side asks include training-data summary per Article 53(1)(d), copyright posture, and transparency documentation for the deployer's own evidence file. The vendor's signature status on the EU AI Office Code of Practice is recorded (signed). Systemic-risk designation of the vendor's model: recorded as the vendor's published status; the deployer's own obligations do not change, but the evidence-asks tier up if the vendor is a designated systemic-risk GPAI provider.
- **Classification** — primary: limited_risk_article_50. Secondary: gpai (vendor-side; recorded so the deployer's evidence file picks up the GPAI provider's published documentation under Article 53). Out of high-risk; Annex III walk recorded so the analysis is auditable.
- **Obligations summary** (selected):
  - Article 50(1) and 50(2) transparency to users (deployer-shared with provider where the disclosure is technically generated; firm-side owner: client servicing for the marking on outbound drafts; AI governance for the policy).
  - Article 26 deployer obligations are limited where the system is not high-risk; the assistant is in scope of Article 50 only, so the substantive deployer obligations of Article 26 (logging, monitoring, instruction-of-use compliance, human oversight at deployer level) do not attach in the same way they would for a high-risk system. Recorded explicitly.
  - GPAI vendor-evidence asks per Article 53 documentation (deployer-side; asks logged in the vendor diligence record cross-linked to `vendor-diligence` and to `llm-vendor-evidence-review`).
- **Annex IV documentation deltas** — not required at this classification (not high-risk). The model card produced under `model-card-builder` covers the firm-side governance artifact; Annex IV is not the applicable obligation.
- **FRIA** — not required (not high-risk and not Article 27 trigger).
- **Registration** — not required (Article 71 register is for high-risk systems).
- **Applicable date** — Article 50 transparency obligations applicable from 2 August 2026 per Article 113. GPAI obligations on the vendor applicable from 2 August 2025. The deployer's go-live can proceed against current vendor documentation; the 2 August 2026 date is the binding constraint for the Article 50 disclosure language being live on every outbound draft.
- **Monitoring for re-classification** — re-triage triggers: change in scope of the assistant (e.g., adding investment-recommendation generation; adding consumer-facing surface; adding emotion-recognition feature); change in vendor model that materially shifts capabilities; change in the EU AI Office's interpretation of Article 6 or Annex III boundaries (track AI Office guidance and Code of Practice updates); change in the firm's product line that brings the assistant into a high-risk Annex III row by extension. Owner: AI Governance Lead, frequency quarterly plus at trigger events.
- **Open questions and dissent** — one item flagged for legal: whether the inclusion of scheme-member personal data in the source documents (tables of beneficiaries) tips the GDPR profile materially enough to require a fresh DPIA scoped to the assistant deployment. Counsel position pending. Article 50 disclosure language pre-cleared by legal as a separate workstream.
- **Source trace** — every material claim cited to article and annex; AI Office Code of Practice referenced as soft-law for vendor-evidence framing; vendor's published Article 53 documentation cited at confidence high (vendor-issued, dated, and signed under Code of Practice); deployer-side evidence asks recorded in the vendor diligence record.
- **Capital-markets overlay notes** — Marketing Rule reach considered for any reuse of the assistant's output in US-client materials (out of scope of this engagement, flagged for the US parent's compliance team); MiFID II considerations for any reuse in EU professional-client communications (within scope; firm policy already requires the human-review gate for any such reuse).

#### Why this scenario matters

- It exercises the Article 6 / Annex III walk for a use case that ends in not-high-risk. A senior reviewer should not skip the row-by-row analysis just because the obvious answer is "no". The analysis is auditable evidence that the screen ran.
- It exercises Article 50 in the limited-risk landing zone, including the explicit screen of each sub-obligation. The triage shows that 50(2) synthetic content marking is the load-bearing obligation for outbound drafts; the firm's disclosure language is a deliverable consequence.
- It exercises the GPAI-as-secondary-classification pattern: the vendor's GPAI obligations on the upstream model do not transfer to the deployer, but the deployer's evidence file picks up the vendor's published documentation and tracks Code of Practice signature status. The triage routes the deployer-side asks to the vendor-diligence record and to `llm-vendor-evidence-review`.
- It exercises the deployer-vs-provider distinction without conflating the two: the vendor is provider; the firm is deployer; the obligations attach differently. The triage records the vendor's role and the firm's role, and attaches obligations to each.
- It exercises the phasing: Article 50 obligations applicable from 2 August 2026, GPAI obligations on the vendor from 2 August 2025. The triage carries both dates and the disclosure-language deliverable as the binding go-live constraint on the firm side.

## troubleshooting

### Troubleshooting: ai-act-triage

Recurring failure modes when an AI Act triage looks finished but is not. The reviewer pass should catch these; the triage pass should preempt them.

#### The triage skips the row-by-row Annex III walk and asserts a conclusion

Symptom: the artifact lands at "not high-risk" or "high-risk" with one sentence of reasoning. No row-by-row walk of Annex III. No record of the screen running for rows that did not apply.

Why it happens: the answer feels obvious from the use-case description, so the practitioner skips the audit trail.

Fix: every Annex III row is recorded as applies / does not apply, with one-line reasoning. The artifact is auditable. A reviewer reading the triage in two years should see the screen ran. The Article 5 prohibited-practice screen carries the same expectation: each sub-practice screened on the record, including the ones that obviously do not apply.

#### Operator role conflated to a single label

Symptom: the triage says "the firm is the deployer" without naming what the vendor is, or names the firm as "user" without distinguishing provider, deployer, importer, distributor, or authorised representative under Article 3.

Why it happens: the practitioner imports a generic vendor-management vocabulary instead of the AI Act's role definitions.

Fix: enumerate every operator role for every entity in the chain. A US parent with an EU subsidiary deploying a vendor-built system involves at least three actors and frequently picks up multiple roles per entity (e.g., a firm that fine-tunes a vendor model becomes a provider for the fine-tuned variant under Article 25). The schema field `operator_roles` is array-typed for a reason.

#### Article 27 FRIA collapsed into the GDPR DPIA

Symptom: the artifact claims FRIA coverage by reference to the existing DPIA, with no FRIA-vs-DPIA reconciliation note.

Why it happens: practitioner pattern-matches "impact assessment" to the most familiar instrument.

Fix: the FRIA covers fundamental-rights elements (impact on affected persons' rights, mitigation measures, governance arrangement, complaints handling) that the DPIA does not. Article 27 is in addition to GDPR, not in lieu of. The triage carries an explicit reconciliation note when both are in scope; legal review on the reconciliation, not just the FRIA.

#### Article 50 transparency screened as one obligation

Symptom: the triage records "Article 50 applies" or "Article 50 does not apply" without screening each sub-obligation (50(1) AI-interaction disclosure, 50(2) synthetic-content marking, 50(3) deepfake disclosure, 50(4) public-interest text marking, 50(5) emotion recognition / biometric categorisation disclosure).

Why it happens: Article 50 is treated as a binary rather than as a multi-part screen.

Fix: each sub-obligation is screened individually. A GenAI assistant that drafts customer responses fires 50(1) and 50(2); it does not fire 50(3) or 50(5). Recording each on the record both removes the gap and tells the reviewer what disclosure language is needed where.

#### GPAI obligations attached to the deployer

Symptom: the triage attaches Articles 51 to 55 obligations to the deploying firm because the firm uses a vendor LLM.

Why it happens: the practitioner reads "general-purpose AI model" and attaches every related obligation to the firm without distinguishing model-provider obligations from system-provider and deployer obligations.

Fix: GPAI obligations under Articles 51 to 55 attach to the model provider. A firm that deploys a vendor LLM-backed system is the deployer of the system; the deployer's obligations are Article 26 (when the system is high-risk) and Article 50 (when the limited-risk obligations apply), not the GPAI provider obligations. The triage records the vendor's GPAI status as deployer-side evidence (training-data summary per Article 53(1)(d), copyright posture, Code of Practice signature status) without attaching the obligations themselves to the firm. When the firm fine-tunes or substantially modifies the model, Article 25 may flip the firm into a provider role; that is a separate analysis.

#### Phasing dates ignored or misread

Symptom: the triage names the classification but not the applicable date, or asserts an obligation as currently binding when the Article 113 phasing places it in the future, or the reverse.

Why it happens: practitioner reads the obligation list and does not consult Article 113.

Fix: every obligation in the obligations summary carries its applicable date per Article 113. The schema field `applicable_date` is required. Common phasing landmarks: prohibited-practices applicable from 2 February 2025; GPAI obligations on providers applicable from 2 August 2025; high-risk and Article 50 transparency obligations applicable from 2 August 2026; the high-risk obligations for AI systems falling under Annex I product-safety legislation applicable from 2 August 2027. Confirm against Article 113 at write time; phasing for member-state implementations and AI Office secondary instruments may shift specific items.

#### Article 6(3) derogation invoked without analysis

Symptom: the triage records "Article 6(3) derogation applies" or asserts the system is not high-risk under the derogation, with no analysis of which limb of 6(3) is invoked.

Why it happens: the derogation looks like a release valve from high-risk classification, and the practitioner reaches for it.

Fix: Article 6(3) has four narrow limbs (narrow procedural task, improving previously completed human activity, detecting decision-making patterns or deviations, preparatory task). The triage records which limb is invoked and the basis. For pricing, underwriting, and creditworthiness use cases, the derogation is rarely available because the system materially influences the outcome. Profiling of natural persons disqualifies the derogation under 6(3) regardless of which limb is named. When the derogation is invoked, route to legal for sign-off.

#### Member-state implementations skipped

Symptom: the triage cites the Regulation only and does not consider member-state implementing measures, national competent authority designations, or member-state deviations on permitted enforcement.

Why it happens: the Regulation is the headline source; the implementing landscape is patchy and changes by state.

Fix: when the scope names a member state of operation, cross-walk to the implementing measure (where designated and where in force at write time). The triage records the state and the implementation status; where the implementation is in transposition or under consultation, the triage records that posture and routes to legal. Do not assert a member-state-specific obligation without confirming the implementation status.

#### Sector overlay loaded but ignored

Symptom: insurance pricing triage reads in generic Annex III(5)(c) reasoning but never names ECDIS provenance, NAIC AIS Program reconciliation, or state DOI bulletins. Banking creditworthiness triage names Annex III(5)(b) but never names CRR/CRD model-risk overlap or the OCC large-bank Heightened Standards reach. Capital-markets vendor-LLM triage cites Article 50 but never names the Marketing Rule reach or books-and-records exposure.

Why it happens: the sector overlay file exists in references/ but the triage author treated it as background.

Fix: when the scope names a sector, the matching `references/sector-overlays.md#<sector>` content lands as named items in the triage artifact. The reviewer challenges any sector-flagged engagement that produces an artifact with no sector content.

#### The triage drifts into legal advice

Symptom: the artifact says "the firm must ..." or "the firm is required to ..." in language that reads as a binding legal interpretation rather than as a triage decision routed to legal for confirmation.

Why it happens: practitioner voice slips into legal voice when the conclusion feels clear.

Fix: the triage is a draft for legal and compliance review. Practitioner voice records the classification, the article references, and the obligations the firm picks up at that classification. Final legal interpretation, especially on Article 5 prohibition reach, Article 6(3) derogation, Article 27 FRIA-vs-DPIA reconciliation, and member-state implementing measures, is for legal counsel. The artifact stops at draft; the SKILL.md non-negotiable on the human-review gate carries the practice rigidly.

#### Source trace omits AI Office and Code of Practice references

Symptom: the triage cites the Regulation and stops there. AI Office Q&A and the Code of Practice on General-Purpose AI are absent, even where the firm has elected to track them.

Why it happens: practitioner treats only the Regulation as authoritative and ignores soft-law sources.

Fix: AI Office guidance and the Code of Practice are not binding interpretations and the triage should not cite them as such. They are useful for tracking enforcement posture and vendor-evidence framing. The source trace records them with the soft-law label so the reviewer sees the firm's monitoring posture; do not collapse soft-law references into the same line as Regulation citations.

#### Re-classification triggers missing

Symptom: the triage lands a classification and stops, with no statement of what would re-open it.

Why it happens: the triage is treated as a one-time decision rather than as a living artifact tied to the use case.

Fix: every triage records re-classification triggers (architecture change, scope change, EU-footprint change, AI Office guidance update, member-state implementation update, vendor change-of-version where relevant). Owner and frequency are named. The triage is owned and refreshed; the spec sheet's `applicable_date` is one anchor for refresh cadence.
