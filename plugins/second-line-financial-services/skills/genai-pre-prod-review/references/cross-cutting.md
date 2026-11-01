# cross-cutting

One section per topic. Read only the sections the scope calls for.

## ai-ethics

### AI ethics cross-cutting overlay for genai-pre-prod-review

When the scope record flags `ai-ethics` for a pre-prod gate review, this overlay adds ethics-specific gate considerations: AI-ethics co-review, stakeholder-impact and dignity framing, bias-and-fairness coverage beyond statistical disparity, transparency and recourse posture, autonomy-creep framing for agentic deployments, vulnerable-population exposure read, workforce-AI considerations, and recommended-action items typical of ethics-flagged GenAI gate reviews. The overlay is the seam between the firm's published responsible-AI posture and the operational evidence on this use case.

Loaded by: `genai-pre-prod-review/SKILL.md` when `scope.cross_cutting_set` includes `ai-ethics`. Cited and section-referenced anchors live in `references/source-anchors.md`.

Load when any of the following holds:

- Customer-facing AI flow with autonomous decisioning (the system makes or routes a decision affecting a consumer without a human in the loop on the per-decision path).
- AI assisting in adverse-action contexts: lending, credit pricing, account closure, employment decisioning, insurance underwriting and pricing, claims-handling decisions, dispute-handling outcomes.
- Vulnerable-population exposure: older adults, customers in financial hardship or distress, language minorities or LEP populations, persons with disabilities (ADA Title III digital-accessibility surface), unbanked or underbanked populations, recent immigrants, minors where the surface reaches them.
- Safety-of-life or safety-of-property surfaces where false-positives and false-negatives carry asymmetric harm: fraud decisioning, AML triage and SAR-decisioning support, sanctions screening, account-takeover triage, debit-block decisioning, life-and-health insurance underwriting where coverage denials carry consequence.
- AI-generated content reaching customers without human review: customer-facing chatbots, summaries shown to customers, recommendation surfaces, generated marketing copy, in-product explanations.
- Workforce-AI use: hiring and candidate-screening tools, performance-management or productivity-monitoring systems, scheduling or task-routing systems with consequence to compensation or retention, surveillance-adjacent monitoring of employees or contractors.
- High-stakes agentic deployments where cumulative authority across many low-stakes per-action decisions can rise to consequential aggregate impact.
- The firm holds itself out publicly on responsible-AI practices (published principles, EU AI Pact signatory, voluntary White House AI commitments, sustainability / proxy AI commitments, NAIC AIS Program self-attestation) and could be tested against that posture on the use case.

Do not load `ai-ethics` when the use case is:

- Pure infrastructure or model-ops AI with no customer-facing or workforce-facing surface and no decision-affecting output (e.g., capacity-planning forecasts inside infra, log-anomaly detection inside SRE).
- B2B AI flow that genuinely does not touch consumers and does not handle consumer data downstream. Verify carefully: many B2B flows (vendor-management tools, contract-review surfaces, regulatory-correspondence drafters) handle documents that encode customer-facing obligations or carry consumer data, and the conduct overlay's narrow-scope-conduct trigger applies. Where the B2B flow does touch consumer data downstream, load the overlay.
- Narrow internal-only technical assists with no consequential output (e.g., developer code-completion in dev environments, internal documentation search across non-sensitive corpora). Verify the corpus and the use pattern; "internal-only" is not by itself the disqualifier.

The reflexive "internal equals safe" framing is the recurring failure mode the overlay is built to challenge.

#### Source basis

Primary anchors (load-bearing):

- NIST AI Risk Management Framework 1.0 (January 2023): Govern function, especially Govern 1.4 (legal and regulatory considerations) and Govern 4 (organisational accountability for AI risks); Map function for context-of-use, especially Map 5.1 (impact on individuals, groups, society); Manage function 4.3 for risk-prioritisation and ongoing risk treatment `[verify section]`.
- NIST AI 600-1 (Generative AI Profile, July 2024): subcategories on transparency, human oversight, content provenance, harmful-bias-or-homogenisation, human-AI-configuration, information-integrity, obscene-degrading-and-abusive-content `[verify section]`.
- ISO/IEC 42001:2023: §6.1.2 (AI policy) for ethics scope and §6.1.4 (AI system impact assessment) for the impact-assessment expectation `[verify section]`.
- EU AI Act (Regulation (EU) 2024/1689): Article 14 (effective human oversight) and Article 27 (Fundamental Rights Impact Assessment for deployers of certain high-risk AI systems, mandatory in scope) where applicable; Chapter V (general-purpose AI models and systemic-risk GPAI) for foundation-model-driven systems `[verify section]`. The formal classification belongs to `ai-act-triage`; this overlay carries the framing and the FRIA decision in scope.
- IEEE 7000-2021 (model process for addressing ethical concerns during system design) as industry framework for systematic ethics-by-design.
- OECD AI Principles (2019, updated 2024) for the inclusive growth, human-centred values, transparency, robustness, and accountability framing.
- The firm's own published responsible-AI principles, AI ethics charter, and AI ethics committee or responsible-AI council charter; firm-side charters are the operative reference, the external frames are the basis.

Sector and use-case-specific anchors (cite where load-bearing):

- Consumer credit: ECOA / Reg B (12 CFR Part 1002) disparate-impact theory; FCRA (15 USC §1681 et seq.) accuracy obligations on consumer-report content where AI generates or scores reportable items; Fair Housing Act for housing-related credit. The conduct overlay's primary co-signer (consumer compliance / fair-lending function) remains binding; this overlay adds the ethics framing.
- Employment: EEOC technical assistance "The Americans with Disabilities Act and the Use of Software, Algorithms, and Artificial Intelligence to Assess Job Applicants and Employees" (May 2022) and follow-on EEOC guidance on Title VII and AI in employment decisions; ADA Title III digital-accessibility expectations for any surface customers or employees use; state-level employment-AI statutes (e.g., NYC Local Law 144 on automated employment decision tools, Illinois AI Video Interview Act, California regulations as applicable).
- Insurance: NAIC Model Bulletin on the Use of AI Systems by Insurers (December 2023) for the AIS Program framework; state DOI bulletins on algorithmic discrimination and unfair-discrimination governance; Colorado SB 21-169 implementing regulation on unfair-discrimination governance for predictive models in life insurance; NYDFS Insurance Circular Letter (January 2024) on ECDIS for NY-licensed insurers; the conduct overlay's chief-actuarial-officer co-signer remains binding for unfair-discrimination exposure.
- Healthcare-adjacent: HHS Office for Civil Rights guidance on nondiscrimination and AI under Section 1557 of the ACA, and HIPAA-covered information considerations where AI touches PHI; the privacy overlay is the primary carrier for HIPAA, and this overlay adds the nondiscrimination ethics framing.
- For EU-deployer footprint: EU AI Act Article 9 (risk management), Article 14 (oversight), Article 26 (deployer obligations), Article 27 (FRIA), Article 50 (transparency to natural persons), Chapter V (GPAI). FRIA is a deployer-side mandatory artefact for certain Annex III high-risk uses; the gate review records the FRIA decision and routes the FRIA itself to the appropriate firm-side workstream.
- The US Blueprint for an AI Bill of Rights (October 2022) is non-binding aspirational guidance; cite as reference where the firm has pointed to it in its own published posture, otherwise treat as background.

Firm external commitments where applicable: EU AI Pact signatory commitments, voluntary White House AI commitments, sustainability / proxy / annual-report AI commitments, NAIC Model Bulletin AIS Program self-attestation for insurers, ISO/IEC 42001 certification posture.

#### Co-reviewer expectation

The named ethics co-signer depends on firm AI governance design. Most-common patterns:

- An AI ethics committee, AI ethics review board, or responsible-AI council where one exists is the co-signer for tier-1 and material tier-2 use cases.
- The AI Governance Lead carries the ethics seam where there is no dedicated ethics committee.
- A Chief Ethics Officer or equivalent is named for firms that have one.

Layered sign-offs by use-case shape:

- Consumer-facing or decision-affecting use cases: the conduct overlay's consumer-compliance co-signer remains binding; the ethics overlay adds the ethics-failure framing rather than duplicating the conduct sign-off. For credit-decisioning, the fair-lending function remains the binding fair-lending co-signer.
- Insurance underwriting and pricing: the conduct overlay's chief-actuarial-officer remains the binding unfair-discrimination co-signer.
- Agentic deployments: the cyber overlay's CISO co-signer remains; the ethics overlay adds the autonomy-creep framing on the residual-risk side.
- Workforce-affecting use cases: the head of HR is named as co-signer; the firm's labour-and-employment-law function is consulted for protected-class exposure, ADA digital-accessibility, works-council exposure (EU footprint), and state-level employment-AI statute applicability.
- Vulnerable-population exposure: the firm's accessibility lead or equivalent is consulted for ADA-relevant surfaces; the consumer-recourse function is consulted for hardship-exposed populations.

For tier-1 use cases the overlay's named co-signer is on the reviewer-attestation block; a tier-1 ethics-flagged gate decision proceeding without a named ethics co-signer is itself a finding.

#### What changes when ai-ethics is flagged

The deliverable carries an explicit AI-ethics check, specific monitoring signals, named IR triggers, and ethics-tagged sign-offs.

##### Open conditions the overlay typically adds

- Stakeholder-impact and dignity check. The gate review documents who can be harmed by the use case, in what way, on what timescale, and how reversibly. Affected populations (consumers, sub-populations within consumers, employees, sub-populations within employees, third parties exposed via the firm's actions) and concrete harm classes (allocative, representational, quality-of-service, dignitary, autonomy-related, attributable-misrepresentation) are named, not asserted as covered. Vulnerable-population sub-populations (older adults, customers in hardship, LEP populations, persons with disabilities, unbanked / underbanked, minors where in scope) are walked explicitly where the use-case shape implicates them.
- Vulnerable-population exposure read. For each named sub-population in scope: the harm pathway, the mitigation in design (accommodation surface, plain-language disclosure, alternative-channel availability, hardship-routing), and the evidence the mitigation works (sampling, testing, complaint coding). ADA Title III digital-accessibility evidence (WCAG 2.x conformance level, assistive-technology testing) is recorded for surfaces consumers or employees use.
- Explainability and recourse design at the impact-scaled bar. For consequential decisions affecting consumers or employees, the affected party can know the reason for the outcome at a level supporting contestability: Reg B-quality adverse-action reasons for credit; FCRA accuracy expectations where AI generates or scores consumer-report content; comparable specificity for insurance underwriting, claims handling, and employment decisions. For supportive uses, the human reviewer can know what the AI surface contributed and at what confidence. The recourse channel is named with SLA and evidence the channel works.
- Bias-and-fairness coverage beyond statistical disparity. The gate review records what was tested across the harm-class taxonomy: allocative (disparate-impact, lives in conduct overlay primarily), representational (output-content stereotyping or under-representation, particularly for generative use cases producing content about people or groups), quality-of-service (stratified performance across populations including LEP and disability-relevant populations), dignitary (deflection patterns, refusal patterns, tone differences regardless of outcome metric), autonomy-related (system substitutes its judgement for the user's), attributable-misrepresentation (generative output makes claims about identifiable people or institutions). Classes not tested are recorded as `[evidence needed]` and route to recommended actions.
- Safety-of-life and safety-of-property asymmetric-harm read for fraud, AML triage, sanctions screening, account-takeover, debit-block, and life-and-health insurance use cases. False-positive and false-negative pathways are named with their specific population-impact (e.g., false-positive sanctions hit on a name common to a refugee population; false-negative fraud miss on an elder-financial-exploitation pattern). The trade-off is recorded explicitly with the population most exposed to each error class.
- Transparency-and-disclosure posture. Disclosure that AI is in use scaled to context: customer-facing chatbot discloses non-human status (EU AI Act Article 50 in EU footprint, FTC and state-level expectations elsewhere); staff-intermediated agent records the staff disclosure; agentic deployment routing customer interactions discloses appropriately. For generative outputs that could be mistaken for human work or source-of-record content, the provenance posture (cryptographic provenance, watermarking, in-text disclosure, source-citation per NIST AI 600-1 content-provenance subcategory) is named. Disclosure-by-press-release does not substitute for in-product disclosure where the use case warrants it.
- Effective-oversight evidence for human-in-the-loop and human-on-the-loop designs. The reviewer has the skill to challenge the AI's output, the authority to override without process friction defaulting to the AI, the time and cognitive bandwidth to do more than rubber-stamp, and incentives that do not reward speed over accuracy. Sampling-audit cadence and reviewer-rotation policy are recorded; the EU AI Act Article 14 effective-oversight expectation applies in scope and frames by analogy elsewhere.
- FRIA decision. Where the use case may fall in EU AI Act scope as a deployer-side high-risk system requiring a Fundamental Rights Impact Assessment under Article 27, the gate review records the FRIA decision (mandatory / not-mandatory / under-evaluation) and routes the FRIA itself to the firm-side workstream that owns it. The gate review does not substitute for the FRIA; it records that the FRIA is in flight or complete and that the gate is consistent with the FRIA's findings.
- For agentic deployments: action-ceiling configuration at the platform layer (maximum financial impact, maximum customers or employees affected per batch, maximum scope of system change per invocation), reversibility scoping with named exceptions and the off-switch criterion, auditability (every consequential action logged with reasoning step, input, output, oversight event, and system-of-record state before-and-after), and the autonomy-creep framing where low-stakes per-action ceilings combined with high-frequency invocation can constitute high-stakes cumulative authority. Ceilings recorded in policy without configuration enforcement are recorded as `[evidence needed]`.
- For generative use cases: content-attribution posture (firm posture on attributable claims about products, services, people, institutions; refusal-and-deflection design for out-of-scope generation; source-citation requirements for generative outputs about regulated content) and red-team coverage on ethics-specific harm classes (representational, dignitary, attributable-misrepresentation, autonomy-related, demographic-stratified quality-of-service, vulnerable-population-specific failure modes). Classes not tested are recorded as `[evidence needed]`.
- For workforce-AI use cases (hiring, performance management, productivity surveillance, scheduling with consequence): EEOC technical-assistance alignment evidence; ADA accommodation surface for candidates and employees; Title VII protected-class testing where applicable; state employment-AI statute alignment (NYC Local Law 144 bias audit and candidate notice where in scope, Illinois AI Video Interview Act notice and consent where in scope, applicable California regulations); works-council notification for EU footprint; the surveillance-creep framing where productivity monitoring exceeds documented purpose. The HR co-signer attests; the labour-and-employment-law function is consulted.
- Public-commitment alignment check. Where the firm has published responsible-AI principles, signed external commitments (EU AI Pact, voluntary White House AI commitments, sustainability / proxy commitments), or made AI-specific NAIC AIS Program attestations, the gate review records the operational evidence that maps to those commitments on this use case. Gaps are recorded explicitly.

##### Monitoring readiness adds the ethics-tagged signal set

In addition to the standard signal set:

- Demographic stratified performance drift where data and consent allow; drift detection on the stratified surface, not only the aggregate; escalation to the ethics co-signer with the conduct co-signer for consumer-facing surfaces. Stratifications include LEP, disability-status proxies where lawful, and hardship-flag where the firm operationalises one.
- Refusal-rate and deflection-rate monitoring stratified by user population; differential refusal rates across populations are an ethics signal as well as a quality signal; escalation to the AI Governance Lead with the consumer-compliance function for customer-facing use cases.
- AI-relevant ethics complaint codes in the consumer-recourse or employee-recourse channel: misleading content, refused or deflected legitimate request, dignitary complaint, autonomy-related complaint, accessibility complaint, hardship-handling complaint. The conduct overlay covers complaint-channel readiness; the ethics overlay adds the named ethics codes.
- Human-reviewer override rate where the design includes a human-in-the-loop. Sustained low override rate (rubber-stamping) and sustained high override rate (the AI is wrong or the workflow is misdesigned) are both signals; escalation to the AI Governance Lead with the function that owns the reviewers.
- For agentic deployments: cumulative action volume per agent, cumulative customer or employee impact per agent, average action-ceiling utilisation; sudden expansion is the autonomy-creep investigation trigger. Escalation to the CISO function with the AI Governance Lead.
- For workforce-AI: candidate or employee complaint rate stratified by protected class (where lawful and consented); accommodation-request rate; adverse-impact ratio against the four-fifths benchmark for hiring-decision support. Escalation to HR co-signer with the labour-and-employment-law function.
- Foundation-model behaviour shift on ethics-specific properties. The vendor change-of-version event re-runs the ethics-specific red-team coverage; behaviour shifts on the ethics surface are an ethics signal as well as a model-risk signal.

##### Incident-response readiness names ethics-specific notification triggers

The `incident_response_readiness.regulator_notification_triggers` list adds, alongside the privacy / conduct / cyber overlay triggers and the sector-overlay triggers:

- Confirmed misleading communication or attributable misrepresentation with material consumer or external impact: routes through the conduct overlay's CFPB UDAAP / Marketing Rule / FINRA 2210 trigger evaluation; the ethics overlay names the underlying ethics-failure class.
- Confirmed differential quality-of-service event with demographic impact, including LEP and disability-relevant populations: routes through the conduct overlay's fair-lending / unfair-discrimination trigger evaluation; the ethics overlay names the underlying class for sub-statistical-disparity events the conduct overlay alone might miss; ADA-relevant accessibility failure routes to the firm's accessibility-incident process.
- Confirmed safety-of-life or safety-of-property asymmetric-harm event in fraud, AML triage, sanctions screening, account-takeover, or insurance underwriting decisioning: routes through the relevant sector overlay's notification triggers; the ethics overlay names the population-specific impact for the harm-class record.
- Confirmed dignitary harm event with consumer or employee impact, where the firm's published responsible-AI principles or external commitments are tested.
- Confirmed autonomy-creep event where agentic action exceeded documented authority or cumulative authority diverged from documented scope; routes through the cyber overlay's incident triggers and adds the ethics framing.
- Confirmed contestability failure where an affected party could not access recourse the use case design promised.
- Confirmed workforce-AI failure: bias-audit failure on a hiring tool covered by NYC Local Law 144 or comparable statute; ADA accommodation failure; surveillance-purpose creep beyond documented scope; works-council notification failure (EU footprint).
- Public-attribution event where the firm's published responsible-AI commitments are tested by an external claim, regulator inquiry, media event, or activist campaign; for EU AI Pact signatories, the in-scope reporting expectations apply where applicable `[verify section]`.

The IR drill scope before go-live should exercise at minimum one ethics-specific incident class (e.g., confirmed attributable misrepresentation on customer-facing generative output; confirmed autonomy-creep event on agentic deployment; confirmed contestability failure where adverse-action recourse did not function; confirmed workforce-AI bias-audit failure for hiring use cases).

##### Recommended-action items the overlay surfaces

- Stakeholder-impact and dignity check completed and signed by the named ethics co-signer; harm-class taxonomy walked rather than asserted; vulnerable-population sub-populations named explicitly.
- Vulnerable-population exposure read documented; mitigations named with evidence; ADA digital-accessibility evidence recorded for surfaces in scope.
- Explainability and recourse design at the impact-scaled bar; affected-party-side recourse named for consequential-decision use cases with SLA and channel evidence.
- Bias-and-fairness coverage across the named harm classes; classes not tested route to follow-up work with owner role and SLA.
- Safety-of-life / safety-of-property asymmetric-harm read documented for fraud, AML, sanctions, account-takeover, life-and-health insurance use cases; population-specific impact named.
- Transparency-and-disclosure posture decided; in-product disclosure configured where applicable; generative-output provenance signals named.
- Effective-oversight evidence recorded for human-in-the-loop and human-on-the-loop designs; sampling-audit cadence set; reviewer-rotation and reviewer-incentive review documented.
- FRIA decision recorded for EU-footprint Annex III use cases; routing to the firm-side FRIA workstream confirmed.
- For agentic deployments: action-ceiling configuration evidence at the platform layer; off-switch criterion named; autonomy-creep monitoring signal live.
- For generative use cases: content-attribution and ethics-specific red-team coverage completed and recorded; provenance signals configured.
- For workforce-AI: EEOC alignment evidence; ADA accommodation surface; state employment-AI statute alignment (NYC LL 144 bias audit and notice; Illinois AI Video Interview Act; California regulations); works-council notification (EU); HR co-signer attestation; labour-and-employment-law consultation recorded.
- Demographic stratified performance-drift monitoring and ethics-coded complaint-channel readiness live before go-live.
- Ethics-failure incident class added to the IR runbook with named scenarios drilled.
- Public-commitment alignment check recorded; mapping from published responsible-AI principles to operational evidence on this use case documented; gaps named.

#### Ethics-specific output additions

In the structured object (`schemas/genai-pre-prod-review.schema.json`):

- `cross_cutting_overlay_notes.ai_ethics` carries ethics-specific fields: stakeholder-impact and dignity check status, vulnerable-population exposure read status, explainability and recourse design status, bias-and-fairness coverage status by harm class, safety-of-life-or-property asymmetric-harm read status (where applicable), transparency-and-disclosure posture status, effective-oversight evidence status, FRIA decision (where applicable), action-ceiling configuration status (agentic), generative-coverage status (generative), workforce-AI coverage status (workforce), public-commitment alignment status.
- `signoff[]` array includes the named ethics co-signer (AI ethics committee, Chief Ethics Officer, AI Governance Lead, or firm-equivalent) plus HR co-signer for workforce-AI use cases.
- `monitoring_readiness[]` entries with ethics-tagged escalation path (AI Governance Lead, ethics committee, conduct or CISO co-signer where applicable, HR co-signer where applicable).
- `incident_response_readiness.regulator_notification_triggers` populated with the named ethics-specific triggers.
- `overlay_signoffs[]` includes an ai-ethics entry with named owner role.

#### Common pitfalls in ai-ethics-flagged pre-prod gate reviews

- Treating "internal-only" as ethics-exempt. Internal tools with consequential authority over employees, internal tools that shape customer-affecting decisions through staff intermediation, and internal tools that surface employee-monitoring or workforce-management decisions all sit within the overlay's scope. The reflexive "internal equals safe" framing is the recurring failure mode the overlay is built to challenge, mirroring the conduct-overlay pattern on staff-intermediated customer impact.
- Collapsing fairness to "no statistical disparity in outcomes". Allocative parity on the headline metric does not address representational, quality-of-service, dignitary, autonomy-related, or attributable-misrepresentation harms. The harm-class taxonomy in the open-conditions section exists to surface what the disparate-impact test does not.
- Skipping vulnerable-population exposure because the headline population is "general consumers". Aggregate metrics hide LEP, disability, and hardship sub-populations; the gate review walks the sub-populations explicitly where the use-case shape implicates them.
- Treating safety-of-life and safety-of-property surfaces as cyber-only or AML-only concerns. False-positive and false-negative trade-offs in fraud, sanctions, AML, and insurance underwriting decisioning have ethics-specific population-impact framing the operational overlays alone do not surface.
- Treating explainability as a single global property of the model. Affected-party-side recourse on consequential decisions, reviewer-side explainability for human-oversight designs, and developer-side explainability for diagnosis are different bars; the gate review records the layer that is thin (typically affected-party-side recourse) and routes it to recommended actions.
- Assuming RAG or grounding solves hallucination as an ethics issue. Retrieval reduces some confabulation classes but does not address representational harm, attributable misrepresentation about people or institutions, or content-attribution exposure on generative outputs. The grounding posture is a control input; ethics-specific red-team coverage is the evidence.
- Recording vendor responsible-AI policy as substituting for firm-side ethics review. Vendor system-card statements about training-data provenance and vendor-side fairness testing are one input; firm-side stakeholder-impact, recourse design, and effective-oversight evidence are firm-side responsibilities.
- AI-ethics-by-press-release. The firm's published responsible-AI principles, EU AI Pact signatory commitments, and sustainability-report AI commitments do not constitute ethics review on the use case. The public-commitment alignment check is the seam between the published posture and operational evidence; the gap is where the gate reviewer concentrates.
- Treating effective oversight as established by the presence of a human in the workflow. Production-pressure rubber-stamping, reviewer-incentive misalignment, insufficient reviewer skill, and process-friction defaults that favour the AI's recommendation are the failure modes; the gate review records evidence the oversight catches what it is meant to catch.
- Omitting the autonomy-creep framing on agentic deployments. Per-action ceilings configured to "low" do not control cumulative-authority risk; the gate review records the cumulative pattern as a residual-risk row.
- Treating workforce-AI as an HR-only concern. EEOC technical assistance, ADA accommodation, state employment-AI statutes, and EU works-council expectations all carry firm-side AI governance seams; the ethics overlay surfaces them at the gate rather than after the deployment.
- Loading the overlay as a paper exercise. The overlay's load-bearing surface is the named ethics co-signer, the harm-class taxonomy in the fairness section, the vulnerable-population exposure read, the impact-scaled recourse bar, the safety-of-life / safety-of-property asymmetric-harm read where applicable, the FRIA decision in EU scope, and the ethics-failure incident class. A gate review loaded with the overlay but missing those seams reads as overlay-by-checkbox.

## conduct

### Conduct cross-cutting overlay for genai-pre-prod-review

When the scope record flags `conduct` for a pre-prod gate review, this overlay adds conduct-specific gate considerations: consumer-compliance co-review, fairness and harmful-content posture, complaint-readiness, and recommended-action items typical of conduct-flagged GenAI gate reviews. Loaded when any of the following holds:

- The use case generates or assists customer-facing communications.
- The use case makes or supports decisions that affect consumer outcomes.
- The tool is internal-only but operates on contract content, regulatory-correspondence content, marketing assets, complaint files, regulatory submissions, or other documents that encode customer-facing obligations. Internal-scope does not displace conduct loading where the documents the tool acts on carry obligations that flow through to customers (a contract-review tool inside legal still touches consumer-protection terms; a marketing-asset reviewer still touches advertising content the firm publishes; a regulatory-correspondence drafter still shapes positions taken with examiners on consumer matters). Load narrow-scope conduct review on these; the 1L "internal-only, no consumer-facing implications" assertion is the trap this trigger closes.

Loaded by: `genai-pre-prod-review/SKILL.md` when `scope.cross_cutting_set` includes `conduct`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- CFPB UDAAP authority under the Consumer Financial Protection Act and the FTC Act §5 (12 USC §5531 and 15 USC §45) for unfair, deceptive, or abusive acts or practices.
- CFPB Circulars and Bulletins on AI-related consumer-compliance considerations (CFPB Circular 2022-03 on adverse-action notices and AI and CFPB Circular 2023-03 on adverse-action accuracy under ECOA were **withdrawn May 12, 2025; historical only.** Reg B §1002.9 and Comment 9(b)(2)-3 of the Official Staff Commentary continue to apply on their own terms. CFPB Bulletin and policy statements on AI in chatbots and customer service remain).
- ECOA / Reg B (12 CFR Part 1002) and the Fair Housing Act for credit-decisioning use cases; adverse-action accuracy and fair-lending exposure.
- Reg E (12 CFR Part 1005) for AI-assisted dispute handling on electronic fund transfers.
- Reg Z (12 CFR Part 1026) for credit-product communication exposure.
- SEC Investment Adviser Marketing Rule (Rule 206(4)-1) and Reg BI for investment-recommendation-adjacent use cases.
- FINRA Rule 2210 (communications with the public) for broker-dealer use cases.
- State unfair-discrimination statutes (NAIC Model #880 vocabulary) for insurance underwriting and pricing use cases.
- State insurance advertising rules and state suitability requirements for insurance customer-facing use cases.
- State consumer-protection laws (state UDAP analogues) for state-licensed non-bank financial entities.
- For NY-licensed insurers: NYDFS Insurance Circular Letter (January 2024) on ECDIS and underwriting fairness.
- For Colorado life insurance: SB 21-169 implementing regulation on unfair-discrimination governance for predictive models.

#### Co-reviewer expectation

Consumer compliance is a co-signer on the gate decision for any conduct-flagged use case. For credit-decisioning use cases the fair-lending function (within consumer compliance or a separate fair-lending office) is also a co-signer. For insurance underwriting and pricing use cases the chief actuarial officer is a co-signer for the unfair-discrimination seam.

For tier-1 use cases the head of consumer compliance or chief compliance officer is named on the sign-off block; the gate decision does not proceed without that role.

#### What changes when conduct is flagged

##### Open conditions the overlay typically adds

- UDAAP output-filter specification signed off by consumer compliance for any consumer-facing communication generated or assisted by the system.
- Adverse-action notice quality review for any credit-decisioning use case where the AI affects the adverse-action reason or score; Reg B §1002.9 and Comment 9(b)(2)-3 of the Official Staff Commentary set the quality bar (CFPB Circulars 2022-03 / 2023-03 are **withdrawn May 12, 2025; historical only.**).
- Fair-lending integration: the consumer-compliance fair-lending test plan and the gate review reference each other; fair-lending residual risk is recorded in the gate residual-risk section with the fair-lending owner.
- For insurance underwriting and pricing: unfair-discrimination output-filter specification signed off by the underwriting actuary; the chief actuarial officer signs the residual-risk acceptance for unfair-discrimination exposure.
- Complaint-channel readiness: consumer-recourse channel covers AI-relevant complaints; complaint-coding includes AI-specific codes for downstream signal.
- Refusal and deflection-behaviour review: documented refusal posture for out-of-scope queries (e.g., legal advice, medical advice, regulated-product recommendations beyond Reg BI scope, financial advice beyond SR/IA fiduciary scope); appropriate to the audience.
- For multi-state operations: state consumer-protection-law alignment matrix.

##### Monitoring readiness adds the conduct-tagged signal set

In addition to the standard signal set:

- Complaint-rate and complaint-code drift; specific AI-relevant complaint codes (e.g., misleading communication, refused or deflected legitimate request, harmful content); escalation to consumer compliance.
- UDAAP output-filter trip rate; escalation to consumer compliance.
- For credit-decisioning: adverse-action notice quality sampling; escalation to fair-lending function.
- For insurance underwriting and pricing: unfair-discrimination output-filter trip rate; escalation to chief actuarial officer.
- For investment-recommendation-adjacent: Marketing Rule output-filter trip rate; escalation to chief compliance officer.
- Refusal-rate sampling on out-of-scope queries; escalation to AI governance team with consumer compliance.

##### Incident-response readiness names conduct-specific notification and remediation triggers

The `incident_response_readiness.regulator_notification_triggers` list adds:

- CFPB UDAAP-relevant event triggers if AI-assisted output causes an unfair, deceptive, or abusive practice with material consumer harm; the firm's consumer-complaint-handling and regulatory-affairs functions evaluate.
- Adverse-action notice integrity event triggers under ECOA / Reg B if AI-driven output causes an inaccurate or non-compliant adverse-action notice.
- For insurance: state DOI notification triggers for unfair-discrimination events affecting underwriting or pricing decisions.
- For investment recommendations: SEC self-reporting expectations under SEC Enforcement guidance where AI-assisted communications cause material misleading statements; FINRA Rule 4530 reporting where applicable.
- Reg E integrity triggers if AI-assisted dispute handling causes a procedural failure that affects a consumer's rights under Reg E.
- Customer remediation framework: for material consumer-impact events, the firm's customer remediation framework activates (file-and-resolve, restitution, regulator notification per the relevant overlay).

The IR drill scope before go-live should exercise at minimum one conduct-specific incident class (e.g., confirmed UDAAP-relevant misleading communication; confirmed adverse-action notice integrity issue for credit-decisioning; confirmed unfair-discrimination event for insurance underwriting).

##### Recommended-action items the overlay surfaces

- UDAAP output-filter specification documented and signed off; consumer compliance co-signs.
- For credit-decisioning use cases: fair-lending integration explicit and documented; adverse-action notice quality sampling pipeline live before go-live.
- For insurance use cases: unfair-discrimination output-filter and the underwriting-actuary sign-off documented; state insurance advertising rule output-filter documented for customer-facing use cases.
- Complaint-channel readiness documented; complaint coding includes AI-relevant codes.
- For investment-recommendation-adjacent: Marketing Rule and Reg BI fiduciary-lens framing documented; chief compliance officer signs.
- For multi-state operations: state-by-state consumer-protection-law alignment matrix documented; consumer compliance signs off on per-state readiness.

#### Conduct-specific output additions

In the structured object (`schemas/genai-pre-prod-review.schema.json`):

- `cross_cutting_overlay_notes.conduct` carries conduct-specific fields: UDAAP output-filter specification status, adverse-action notice quality review status, fair-lending integration status, unfair-discrimination output-filter status, complaint-channel readiness status, refusal posture documentation status.
- `signoff[]` array includes consumer compliance as a co-signer; fair-lending function for credit use cases; chief actuarial officer for insurance underwriting and pricing use cases.
- `monitoring_readiness[]` entries with conduct-tagged escalation path (consumer compliance, fair-lending function, chief actuarial officer where applicable).
- `incident_response_readiness.regulator_notification_triggers` populated with the named conduct-specific triggers.
- `overlay_signoffs[]` includes a conduct entry with named owner role.

#### Common pitfalls in conduct-flagged pre-prod gate reviews

- Treating UDAAP exposure as a downstream consumer-compliance review. UDAAP is the seat consumer compliance owns at the gate, not after; the gate decision is incomplete without consumer compliance sign-off.
- Treating fair-lending as a separate workstream that runs after AI gate. For credit-decisioning use cases the fair-lending integration is a gate-time co-review; the gate review's residual-risk section names the fair-lending residual risk explicitly.
- Treating refusal behaviour as a vendor-side concern. The refusal posture is firm-side configuration (system prompt, guardrails, output filtering) and a firm-side gate decision; vendor refusal behaviour is one input.
- Recording adverse-action notice quality as compliant by assertion. Reg B §1002.9 and Comment 9(b)(2)-3 of the Official Staff Commentary set a substantive quality bar; the gate review records sampling evidence, not assertion.
- Treating complaint-channel readiness as a downstream concern. Complaint channels need AI-relevant codes live before go-live so the post-go-live signal exists; adding the codes after a complaint surfaces is too late.
- Omitting the chief actuarial officer co-signature on insurance underwriting and pricing use cases. The unfair-discrimination seam is the chief actuarial officer's seat; the gate decision is incomplete without it.
- Treating multi-state operations as having a uniform consumer-protection posture. State UDAP statutes and state insurance advertising rules vary; the gate review records state-by-state status.

## cyber

### Cyber cross-cutting overlay for genai-pre-prod-review

When the scope record flags `cyber` for a pre-prod gate review, this overlay sits as a primary lens. The CISO function is a co-reviewer and a co-signer on the gate decision, not a downstream consumer of the memo. For most GenAI use cases inside regulated entities the cyber overlay should be considered the default cross-cutting overlay.

Loaded by: `genai-pre-prod-review/SKILL.md` when `scope.cross_cutting_set` includes `cyber`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- NYDFS 23 NYCRR Part 500, especially §500.9 (risk assessment), §500.11 (third-party service-provider security), §500.16 (incident-response and BCDR plan), §500.17(a) (notice to superintendent), and the October 2024 Industry Letter on AI cybersecurity that maps these obligations onto AI deployments.
- SEC cyber disclosure rules: 8-K Item 1.05 (material cybersecurity incident disclosure within four business days of materiality determination) and Reg S-K Item 106 (annual disclosure of cyber risk-management, strategy, and governance).
- FFIEC IT Examination Handbook, Information Security and AIO booklets, applied to the AI system's serving environment, change controls, access controls, and incident-response integration.
- US Treasury Department report on Managing Artificial Intelligence-Specific Cybersecurity Risks in the Financial Services Sector (March 2024) for sector-specific cyber-AI considerations.
- 12 CFR Part 53 / Part 225 / Part 304 — the 36-hour banking computer-security incident notification rule for federally regulated banks (loaded via the banking sector overlay).
- NIST SP 800-53 Rev. 5 control families (AC, AU, IR, SI, SR) as the underlying control catalogue for cyber-side mitigations.
- NIST AI 600-1 Generative AI Profile cyber considerations and the OWASP / MITRE / NCSC framings as the practitioner taxonomy for AI threat modelling.

#### Co-reviewer expectation

The CISO function is a co-signer on the gate decision. The reviewer-attestation block on the gate review names the CISO function explicitly; a gate decision without CISO function sign-off on a cyber-flagged GenAI use case is incomplete.

For tier-1 GenAI use cases the CISO function brings the named cyber sub-functions to the table at gate time: the identity team (authentication and authorisation on the model serving endpoint), the network security team (network-layer controls), the security operations centre (monitoring integration and IR runbook readiness), and the IR team (drill execution).

#### What changes when cyber is flagged

##### Open conditions the overlay typically adds

- IR drill scope before go-live includes at minimum one AI-specific incident class (confirmed system-prompt exfiltration, confirmed indirect-injection-driven misrouted action, suspected RAG corpus poisoning, foundation-model behaviour shift suggesting upstream compromise). Annual at minimum; quarterly for tier-1 GenAI use cases.
- Cyber tabletop exercise with the privacy officer and the relevant business function for any GenAI use case handling NPI, PHI, or material non-public information.
- Notification-decision rehearsal: the materiality-assessment process for SEC 8-K Item 1.05 (for public registrants) and the §500.17(a) notification process (for NY-footprint covered entities) exercised against AI-specific incident scenarios.
- Audit-log retention aligned to the firm's cyber log-retention policy and to NYDFS Part 500 §500.6 audit-trail expectations; the audit-log retention is the load-bearing control for many AI-specific monitoring signals.
- Authentication and authorisation review on the AI system's serving endpoint and on each tool the system can invoke (where applicable for tool-using systems); the identity team co-signs.
- Vendor and supply-chain cyber posture documented for the foundation-model provider and any model-artefact dependencies.

##### Monitoring readiness adds the cyber-tagged signal set

The baseline cyber signals that should be live before go-live when the overlay is flagged:

- Authentication and authorisation anomalies on the AI system's serving endpoint; escalation to the security operations centre.
- For tool-using systems: tool-invocation rate and pattern; sudden expansion of tool use or off-hours activity is an investigation trigger.
- Cross-scope tool query anomaly (e.g., the system queries a market-data API on tickers outside the analyst's coverage; the system retrieves customer records outside the agent's case load).
- Output-anomaly detection (sudden shifts in refusal rate, citation patterns, response-length distribution) as a leading indicator of compromise as well as drift.
- Vendor change-of-version signals for foundation-model and serving-environment dependencies; an unannounced version swap is a cyber signal as well as a model-risk signal.
- For retrieval-using systems, retrieval-source integrity signals (last-modified, content hash drift on dynamic sources).

Each signal retains the schema's required fields (signal, threshold, frequency, owner, escalation path); cyber-tagged entries escalate to the CISO function or to the security operations centre, in addition to or in place of the model owner.

##### Incident-response readiness names regulator-notification triggers

This is the cyber overlay's load-bearing addition to the gate review. The `incident_response_readiness.regulator_notification_triggers` list names, in the firm's footprint:

- NYDFS-covered entities: 23 NYCRR Part 500 §500.17(a) requires notice to the superintendent within 72 hours of determining a cybersecurity event has occurred that meets the rule's criteria. Prompt-injection-driven cyber events that result in unauthorised access, unauthorised action, or impairment to the security or integrity of the information system meet the criteria. The October 2024 Industry Letter signals AI-deployment-driven events fall within scope.
- SEC public registrants: 8-K Item 1.05 requires disclosure of material cybersecurity incidents within four business days of materiality determination. Prompt-injection or AI-related cyber events causing or contributing to material cyber incidents are within scope.
- GLBA Safeguards Rule entities (FTC scope): 16 CFR §314.5(d) requires FTC notification of notification events involving the unauthorised acquisition of unencrypted customer information of 500 or more consumers.
- State breach laws: cross-state patchwork; the firm's privacy and incident-response programme normally maintains a state-by-state notification matrix that the gate review references rather than restates.
- Sector-specific notification triggers (state insurance commissioner notices via the insurance overlay; the 36-hour banking computer-security incident notification rule via the banking overlay; state money-transmitter notifications via the payments-fintech overlay) are loaded from the relevant sector overlay.

##### Off-switch documentation

The off-switch criterion column in the gate review's incident-response section is where the cyber overlay bites operationally. A cyber-relevant incident class without a defined off-switch is a finding, not an acceptable position. For agentic systems with tool use, the off-switch is typically a combination of cutting tool privileges and pausing the model serving endpoint. For human-in-the-loop systems, the off-switch is typically a combination of pausing the assistant and switching to the manual workflow.

`incident_response_readiness.off_switch_documented = true` is required for the gate decision to proceed to `go` or `go_with_conditions` on a cyber-flagged use case.

##### Recommended-action items the overlay surfaces

The standard cyber-tagged recommended-actions items:

- `foundation_model_swap_revalidation` flag in change management with explicit re-run of the prompt-injection review and the gate review on every vendor change-of-version notice; cyber signs off on the re-run.
- IR drill cadence including AI-specific incident classes; annual at minimum, quarterly for tier-1.
- Cyber tabletop exercise with the privacy officer and the relevant business function for any GenAI use case handling sensitive data.
- Notification-decision rehearsal for the named regulator-notification triggers.

#### Cyber-specific output additions

In the structured object (`schemas/genai-pre-prod-review.schema.json`):

- `cross_cutting_overlay_notes.cyber` carries cyber-specific fields: control-family tagging on monitoring entries, MITRE ATLAS mapping references on residual-risk entries that derive from the prompt-injection review, named cyber-side recommended-action items.
- `signoff[]` array includes the CISO function or named cyber sub-function as a co-signer.
- `monitoring_readiness[]` entries with cyber-tagged escalation path (security operations centre, IR team, identity team).
- `incident_response_readiness.regulator_notification_triggers` populated with the named triggers per the firm's footprint.
- `overlay_signoffs[]` includes a cyber entry with named owner role.

#### Common pitfalls in cyber-flagged pre-prod gate reviews

- Treating the AI Governance Lead as the sole gate decision-maker. Prompt injection and other cyber-relevant AI risk classes are, in regulator framing, cybersecurity risk classes; the CISO function co-decides on the gate.
- Recording vendor SOC 2 or vendor system card as substituting for firm-side cyber gate evidence. Vendor evidence is one input; firm-side serving environment, identity, network, and IR integration are firm-side responsibilities.
- Failing to integrate the AI-misuse runbook into the firm's IR programme. A standalone AI playbook that does not connect to the named cyber IR runbook is a paper artefact; the gate review records the integration explicitly.
- Recording residual risk without a regulator-notification trigger evaluation. NYDFS §500.17(a), SEC 8-K Item 1.05, the 36-hour banking computer-security incident notification rule, GLBA Safeguards Rule notification, and state breach laws are not optional considerations; the trigger evaluation is recorded in `incident_response_readiness.regulator_notification_triggers`.
- Omitting the off-switch criterion for cyber-relevant incident classes; a confirmed exfiltration with no defined off-switch blocks `go`.
- Using AI-only vocabulary in a gate review the cyber team has to consume. MITRE ATLAS mappings and control-family tagging cost little to add and turn the artefact into something the cyber team can integrate without translation.

## privacy

### Privacy cross-cutting overlay for genai-pre-prod-review

When the scope record flags `privacy` for a pre-prod gate review, this overlay adds privacy-specific gate considerations: Privacy Officer co-review, regulated-data-handling expectations, additional notification triggers, and recommended-action items typical of privacy-flagged GenAI gate reviews. Loaded for any use case handling NPI, PHI, biometric data, or other regulated personal data with potential for inappropriate disclosure or use.

Loaded by: `genai-pre-prod-review/SKILL.md` when `scope.cross_cutting_set` includes `privacy`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- GLBA Safeguards Rule (16 CFR Part 314), as amended December 2021, with FTC notification provisions added October 2023 effective May 2024 (16 CFR §314.5(d)).
- GLBA Privacy Rule (16 CFR Part 313 and parallel federal-banking-agency rules at 12 CFR Part 1016) for the consumer-privacy notice and information-sharing framing.
- HIPAA Privacy Rule (45 CFR Part 164) and Security Rule (45 CFR Part 164 Subpart C) for PHI under covered-entity or business-associate relationships.
- HIPAA Breach Notification Rule (45 CFR §§164.400-414) for PHI exfiltration events.
- SEC Reg S-P (17 CFR Part 248) for broker-dealer and investment-adviser customer-information privacy.
- State comprehensive privacy laws (CCPA / CPRA in California, VCDPA in Virginia, CPA in Colorado, CTDPA in Connecticut, UCPA in Utah, and the growing state patchwork) where consumer rights and data-handling obligations apply.
- State biometric privacy laws (BIPA in Illinois and analogues) where the use case handles biometric data.
- State breach-notification laws (50-state patchwork; the firm's privacy programme maintains the state-by-state matrix).
- For NY-licensed entities: NYDFS 23 NYCRR Part 500 cybersecurity-and-privacy intersection; NYDFS Insurance Circular Letter (January 2024) for ECDIS and underwriting privacy considerations.
- COPPA (15 USC §6501-6506) where the use case may interact with content from users under 13.

#### Co-reviewer expectation

The Privacy Officer is a co-signer on the gate decision for any privacy-flagged use case. The reviewer-attestation block names the Privacy Officer explicitly. For HIPAA-relevant use cases, the privacy-officer role is typically the HIPAA Privacy Official; for GLBA-only use cases the role may be a privacy lawyer or chief privacy officer depending on firm structure.

For tier-1 use cases handling regulated personal data, the data protection officer (where the firm has one), the records-management function (for retention and deletion), and the consumer-recourse function (for consumer-rights handling) are also expected at gate time.

#### What changes when privacy is flagged

##### Open conditions the overlay typically adds

- Data-minimisation review: the gate review documents that the data the model consumes (training, retrieval corpora, prompt context, persistent memory) is the minimum necessary for the use case purpose. Excess data in the prompt path is a structural risk multiplier for exfiltration events.
- Retention review: documented retention period for prompt logs, retrieved content snapshots, output artefacts, and any persistent memory; alignment with regulator-required minima and firm policy.
- Consent and notice posture review: where the use case consumes content covered by an applicable privacy notice (GLBA notice, HIPAA notice of privacy practices, CCPA disclosure), the use of the data for AI processing is consistent with the notice.
- For HIPAA covered entities: business-associate agreement coverage for any vendor in the AI processing path (foundation-model provider, retrieval infrastructure, observability tools).
- For state-comprehensive-privacy-law footprint: consumer-rights-handling workflow (access, deletion, correction, opt-out of certain processing) covers AI artefacts where applicable; deletion requests propagate to retrieved content snapshots and persistent memory.
- For biometric-data use cases: BIPA-and-analogue consent capture and retention-schedule documentation.

##### Monitoring readiness adds the privacy-tagged signal set

In addition to the standard signal set:

- Cross-record retrieval audit signal where the architecture handles regulated personal data (per-customer query scoping, per-claim query scoping, per-policy query scoping); any confirmed cross-record event is a privacy investigation trigger.
- PHI / NPI / biometric-data exfiltration leading-indicator signals (anomalous output length, unusual identifier surface in output, output-content sampling for regulated-data tokens).
- Consumer-rights-handling SLA tracking where applicable; escalation to the Privacy Officer.
- Retention-policy-violation signal: outputs or prompt logs retained beyond policy are themselves a privacy event.

##### Incident-response readiness names privacy-specific notification triggers

The `incident_response_readiness.regulator_notification_triggers` list adds:

- HIPAA Breach Notification Rule (45 CFR §§164.400-414) for PHI exfiltration or unauthorised use; notification to affected individuals, HHS, and in some cases the media.
- GLBA Safeguards Rule notification under 16 CFR §314.5(d): FTC notification for unauthorised acquisition of unencrypted customer information of 500 or more consumers; required for FTC-scope financial institutions.
- State breach-notification laws: per state, with timing and scope variation; the firm's matrix is the reference.
- For state-comprehensive-privacy-law footprint: where applicable, state Attorney General notification per state law.
- For NY-licensed entities: NYDFS §500.17(a) overlap with privacy-tagged events that meet the cybersecurity-event criteria.
- COPPA-related notification where the use case interacts inappropriately with under-13 content.

The IR drill scope before go-live should exercise at minimum one privacy-specific incident class (e.g., confirmed cross-record disclosure of regulated personal data; confirmed PHI exfiltration via output channel; confirmed biometric-data inappropriate retention).

##### Recommended-action items the overlay surfaces

- For HIPAA-relevant use cases: HIPAA breach-notification process rehearsal as part of the IR drill scope; business-associate agreement coverage documented for all vendors in the processing path.
- For GLBA Safeguards Rule entities: notification-decision process rehearsal for FTC notification under 16 CFR §314.5(d).
- For state-comprehensive-privacy-law footprint: consumer-rights-handling workflow updated to cover AI artefacts; deletion-request propagation documented.
- For biometric-data use cases: BIPA-and-analogue consent capture and retention-schedule documented.
- Data-minimisation and retention review documented; signed off by the Privacy Officer.

#### Privacy-specific output additions

In the structured object (`schemas/genai-pre-prod-review.schema.json`):

- `cross_cutting_overlay_notes.privacy` carries privacy-specific fields: data-minimisation review status, retention review status, consent and notice posture review status, business-associate agreement coverage status, consumer-rights-handling workflow status.
- `signoff[]` array includes the Privacy Officer as a co-signer.
- `monitoring_readiness[]` entries with privacy-tagged escalation path (Privacy Officer, data protection officer where applicable).
- `incident_response_readiness.regulator_notification_triggers` populated with the named privacy-specific triggers.
- `overlay_signoffs[]` includes a privacy entry with named owner role.

#### Common pitfalls in privacy-flagged pre-prod gate reviews

- Treating data minimisation as a downstream control. The data the model consumes is the structural risk surface for exfiltration; minimisation is a gate-time decision, not a post-go-live optimisation.
- Omitting the business-associate agreement check for HIPAA-relevant use cases. Every vendor in the processing path (foundation-model provider, retrieval infrastructure, observability) needs BAA coverage; a vendor in the path without a BAA is a HIPAA programme issue.
- Treating state-comprehensive-privacy-law consumer-rights handling as out-of-scope for AI artefacts. Deletion requests need to propagate to retrieved content snapshots and persistent memory; access requests need to handle AI-generated output where it constitutes personal data.
- Treating retention as policy without runtime enforcement. Retained-beyond-policy prompt logs and output artefacts are themselves a privacy event; the retention policy needs runtime enforcement and the gate review records the enforcement evidence.
- Recording vendor system card statements about training-data privacy as substituting for firm-side data-minimisation review. Vendor practices on training data are one consideration; the firm's prompt-path data minimisation is firm-side responsibility.
- Failing to involve the Privacy Officer at gate time. A privacy-flagged use case without Privacy Officer sign-off proceeds with unaccepted privacy residual risk; the gate decision is incomplete.
