# cross-cutting

One section per topic. Read only the sections the scope calls for.

## ai-ethics

### AI ethics cross-cutting overlay for ai-use-case-intake

When the scope record flags `ai-ethics` for an intake record, this overlay adds ethics-specific intake considerations: AI-ethics routing flag, stakeholder-impact and dignity framing, bias-and-fairness scoping beyond statistical disparity, transparency and recourse posture, autonomy-creep framing for agentic deployments, vulnerable-population exposure read, workforce-AI considerations, and the open-question routing tags ethics-flagged use cases carry into tiering, validation, controls review, and pre-prod gate. The overlay is the seam between the firm's published responsible-AI posture and the operational evidence on this use case at the front of the AI governance pipeline.

Loaded by: `ai-use-case-intake/SKILL.md` when `scope.cross_cutting_set` includes `ai-ethics`. Cited and section-referenced anchors live in `references/source-anchors.md`.

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

In the structured object (`schemas/ai-use-case-intake.schema.json`):

- `cross_cutting_overlay_notes.ai_ethics` carries ethics-specific fields: stakeholder-impact and dignity check status, vulnerable-population exposure read status, explainability and recourse design status, bias-and-fairness coverage status by harm class, safety-of-life-or-property asymmetric-harm read status (where applicable), transparency-and-disclosure posture status, effective-oversight evidence status, FRIA decision (where applicable), action-ceiling configuration status (agentic), generative-coverage status (generative), workforce-AI coverage status (workforce), public-commitment alignment status.
- `signoff[]` array includes the named ethics co-signer (AI ethics committee, Chief Ethics Officer, AI Governance Lead, or firm-equivalent) plus HR co-signer for workforce-AI use cases.
- `monitoring_readiness[]` entries with ethics-tagged escalation path (AI Governance Lead, ethics committee, conduct or CISO co-signer where applicable, HR co-signer where applicable).
- `incident_response_readiness.regulator_notification_triggers` populated with the named ethics-specific triggers.
- `overlay_signoffs[]` includes an ai-ethics entry with named owner role.

#### Common pitfalls in ai-ethics-flagged intakes

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

### Conduct cross-cutting overlay for ai-use-case-intake

When the scope record flags `conduct` for the use case, this overlay supplies the conduct-specific intake fields and the named flags that route into downstream tier, fairness-testing, and complaint-surveillance work. Conduct in financial services is broader than fair lending alone: customer-binding decisions, fairness exposure, complaint vector, and market-integrity reach all sit in the conduct lens.

Loaded by: `ai-use-case-intake/SKILL.md` when `scope.cross_cutting_set` includes `conduct`. Source-anchored in `references/source-anchors.md`.

#### Source basis

- ECOA (15 USC §1691) and Reg B (12 CFR Part 1002) — credit-decision conduct frame.
- CFPB Circulars on adverse action with complex algorithms (Circular 2022-03; Circular 2023-03 [verify]) — specific reasons under ECOA when complex algorithms drive credit decisions.
- UDAAP (Dodd-Frank §§1031, 1036) — consumer-financial-services conduct frame, applied across the CFPB's reach.
- FTC Act §5 (15 USC §45) — UDAP frame applied to non-CFPB-supervised entities.
- NAIC Unfair Trade Practices Act (Model #880) — insurance conduct frame, including unfair claims-settlement standards and fair-claims-settlement standards.
- SEC Investment Advisers Act §206 antifraud and Rule 206(4)-1 Marketing Rule — adviser conduct frame.
- SEC Reg BI — BD conduct frame for retail customers.
- FINRA 2010 (just and equitable principles) and FINRA 2111 (suitability) — BD conduct frame.
- MAR (Market Abuse Regulation) and Reg AC — research integrity and market-integrity conduct.

#### Conduct-specific intake fields

In addition to the capability intake spine, the conduct overlay adds the following:

- Customer-binding posture: whether the use case binds the firm to a customer-facing decision (origination, pricing, line management, claims acceptance / denial, account closure, hold) or surfaces a recommendation a human acts on.
- Fairness-sensitive dimensions: protected classes under federal and state law (race, colour, religion, national origin, sex including sexual orientation and gender identity, marital status, age, receipt of public assistance, exercise of rights under the Consumer Credit Protection Act); insurance-specific protected classifications; state-specific protected classes.
- Complaint vector: whether the use case is likely to generate consumer complaints, and through which channels (firm complaint line, sponsor-bank-routed complaints, CFPB Consumer Complaint Database, state DOI complaint, regulator inquiry).
- Adverse-action posture: whether the use case drives an adverse-action notice (credit decision under ECOA / Reg B; insurance underwriting denial under state DOI rules; insurance claims denial under Model #880 reasoned-denial standards).
- Marketing-claim posture: where the use case generates or personalises marketing content, the marketing-claim review flag.

#### Conduct-specific regulatory flags

When the conduct overlay is loaded, the intake's regulatory-flags table picks up:

- `CFPB_Circular_2022_03` and `CFPB_Circular_2023_03` [verify] for credit-decision use cases driving adverse action.
- `UDAAP` (or `FTC_5` for non-CFPB-reach entities) for any consumer-facing use case with a conduct surface.
- `NAIC_Model_880` for insurance use cases (unfair claims and unfair acts; fair-claims-settlement standards).
- `Reg_BI` for BDs serving retail customers where the use case influences a recommendation.
- `SEC_Marketing_Rule` for advisers where the use case touches client-facing material.
- `FINRA_2111` for BDs where the use case influences a suitability determination.
- State DOI bulletins and state UCSPA where insurance customer-facing.
- `MAR` and `Reg_AC` where research integrity is in question.

#### Conduct-specific open questions for downstream skills

The intake routes the following open questions when relevant:

- For `validation-plan`: fairness-testing scope (which protected and policy-relevant dimensions, what test, what threshold); inferred-attribute risk where the model infers a fairness-sensitive attribute from proxies; segment-level performance evidence for any customer-binding decision.
- For `model-card-builder`: the limitations and known failure modes for fairness-sensitive segments; the adverse-action reason generation method (where applicable); the marketing-claim posture (where applicable).
- For complaint surveillance: how does the firm trace a complaint back to the use case, and what is the cadence for AI-attributable complaint review.
- For consumer-compliance review: where does the use case sit in the firm's UDAAP review cycle (or state UCSPA review cycle for insurance); what is the dark-pattern risk in onboarding or product-selection flows the use case touches.
- For regulator-engagement: examiner-facing posture on the use case (which examiner is most likely to engage on it; what the firm's prepared narrative is).

#### Common pitfalls in conduct-flagged intake

- Treating conduct as a synonym for fair lending. Fair lending is one slice; UDAAP, NAIC Model #880, Reg BI, Marketing Rule, and MAR each cover distinct conduct surfaces with their own tests.
- Recording "no customer impact" on a use case that surfaces a recommendation a human acts on. The recommendation is the conduct surface; the human review point does not eliminate the conduct exposure.
- Using fairness terminology where unfair-discrimination terminology is the operative legal frame (insurance pricing and underwriting under NAIC Model #880); the test is different (actuarial justification matters; permitted vs prohibited rating factors are state-defined; protected classes per state insurance code).
- Missing the inferred-attribute open question. A model that does not take race or ethnicity as input may still drive disparate outcomes through proxies; the conduct-flagged intake records this as an open question for `validation-plan`.
- Recording an internal-use research summariser as no-conduct-exposure when the output may be incorporated into a published research note. Reg AC and Marketing Rule reach attach to the published output, not to the underlying tool.
- Recording a fintech account-closure use case as low-conduct without flagging the CFPB UDAAP theme. Account closures and account holds without adequate notice or recourse have been the most-frequent fintech UDAAP theme in recent CFPB Supervisory Highlights [verify date and exact reference].

## cyber

### Cyber cross-cutting overlay for ai-use-case-intake

When the scope record flags `cyber` for the use case, this overlay supplies the cyber-specific intake fields and the named flags that route into downstream tier and pre-prod work. It does not replace the firm's information-security risk assessment; it is the intake-side surfacing of cyber considerations a second-line reviewer (and an examiner under NYDFS Part 500 or the FFIEC IT Handbook) will look for.

Loaded by: `ai-use-case-intake/SKILL.md` when `scope.cross_cutting_set` includes `cyber`. Source-anchored in `references/source-anchors.md`.

#### Source basis

- NYDFS Industry Letter on Cybersecurity Risks Arising from Artificial Intelligence (October 16, 2024) — covered entities under 23 NYCRR Part 500 expected to address AI-related cybersecurity risks, including AI-enabled threats and risks from the entity's own use of AI.
- 23 NYCRR Part 500 (Second Amendment) — covered-entity cybersecurity program expectations.
- NIST AI 600-1 (Generative AI Profile) Manage subcategories on prompt injection, training-data poisoning, model extraction, content provenance.
- OWASP Top 10 for LLM Applications and MITRE ATLAS as the threat taxonomies that anchor the AI-cyber intake fields.
- FFIEC IT Examination Handbook, Information Security and Cybersecurity sections, applied to the model's serving environment, change controls, and access controls.

#### Cyber-specific intake fields

In addition to the capability intake spine, the cyber overlay adds the following:

- AI-enabled threat surface (the entity's exposure to AI-enhanced phishing, deepfake-driven social engineering, AI-driven credential stuffing). Fielded as a one-paragraph narrative with named exposures.
- The entity's own AI use risk surface (prompt injection, training-data poisoning, model extraction, supply-chain dependence on a foundation-model vendor, RAG-corpus poisoning, content-provenance posture). Fielded as a checklist with each exposure scored exposed / not exposed / unclear.
- NYDFS Part 500 covered-entity status. Fielded as a boolean with the operating-state footprint that triggers the status.
- Foundation-model vendor change-of-version posture (pinned, floating with notice, rolling without notice). Captured as part of the architecture block but cyber-relevant because rolling-without-notice is a supply-chain surface.
- Adversarial-test posture (vendor-supplied adversarial-test results only, firm-independent red-team evidence, none). Vendor self-attestation alone is not evidence the firm has tested its own deployed prompt surface, retrieval corpus, or tool inventory.

#### Cyber-specific regulatory flags

When the cyber overlay is loaded, the intake's regulatory-flags table picks up:

- `NYDFS_Part_500` (where the firm is a covered entity in the NY footprint) with routing to `ai-risk-tiering`.
- `NYDFS_AI_letter_2024` (where any of the named AI-enabled threats or own-AI-use risks apply) with routing to `ai-risk-tiering`, `prompt-injection-risk`, and `genai-pre-prod-review`.
- A general flag for the firm's information-security policy where applicable (for non-NYDFS firms; FFIEC IT Handbook reach for federally regulated banks).

#### Cyber-specific open questions for downstream skills

The intake routes the following open questions when relevant:

- For `prompt-injection-risk`: where is the prompt surface, what controls limit prompt-injection exposure, what evidence does the firm have of red-team testing of the deployed prompt surface (not just vendor self-attestation).
- For `rag-evaluation-review`: what is the retrieval-corpus access control, what is the corpus refresh and provenance evidence, what is the firm's posture on retrieval-corpus poisoning detection.
- For `validation-plan`: how is foundation-model version monitoring instrumented, how is the firm notified of vendor change-of-version, what is the regression-test posture on vendor change.
- For `agentic-ai-controls`: where the use case has tool privileges, what limits the tool-action scope, what is the circuit-breaker posture if the tool is used outside its boundary.
- For `vendor-diligence`: what is the foundation-model vendor's evidence pack on supply-chain integrity, model-extraction defences, and incident-response cooperation.

#### Common pitfalls in cyber-flagged intake

- Treating "vendor pen-tested" or vendor adversarial-test results as evidence the deployed prompt surface is hardened. The firm's prompt template, retrieval corpus, and tool inventory are firm-side surfaces; the intake captures evidence at the firm level, not vendor self-attestation.
- Recording an internal-only GenAI use case as low cyber-exposure. Internal-only does not eliminate cyber exposure when the use case has tool privileges, retrieval-corpus access across business lines, or vendor-hosted infrastructure.
- Treating prompt injection as a quality issue rather than a control-evasion path. When the use case has tool or agent privileges, prompt injection becomes a lateral-movement opportunity and the intake's autonomy-level and tool-inventory blocks need to reflect that.
- Failing to flag NYDFS Part 500 covered-entity status. The October 2024 NYDFS Industry Letter on AI cybersecurity is a current expectation; the flag belongs in intake regardless of which downstream skill picks it up.
- Recording the foundation-model pinning posture as "floating" without naming the vendor change-of-version notice channel. "Floating with notice" is a different posture from "rolling without notice" and the intake distinguishes them.

## privacy

### Privacy cross-cutting overlay for ai-use-case-intake

When the scope record flags `privacy` for the use case, this overlay supplies the privacy-specific intake fields and the named flags that route into downstream tier, model-card, and validation work. Privacy in financial services has both a federal regime (GLBA Safeguards Rule, HIPAA where applicable) and a state regime (state privacy laws and state insurance privacy rules); the intake captures the fields each regime needs at intake.

Loaded by: `ai-use-case-intake/SKILL.md` when `scope.cross_cutting_set` includes `privacy`. Source-anchored in `references/source-anchors.md`.

#### Source basis

- GLBA Safeguards Rule (16 CFR Part 314) — applies to non-public personal information (NPI) held by financial institutions.
- HIPAA Privacy Rule (45 CFR Part 160 and Part 164 Subpart E) and Security Rule (Subpart C) — applies to protected health information (PHI) held by covered entities and business associates.
- Reg P (12 CFR Part 1016) — privacy notice and opt-out for consumer NPI.
- State privacy laws applying to financial-services entities: California Consumer Privacy Act (CCPA) as amended by CPRA, Virginia CDPA, Colorado CPA, Connecticut CTDPA, Utah UCPA, and others. Most state privacy laws carve out GLBA-covered data; intake distinguishes regulated NPI (GLBA-covered) from non-GLBA-covered consumer data.
- State insurance privacy rules (NAIC Model #672 Insurance Information and Privacy Protection Model Act, where adopted) — adoption status varies by state.

#### Privacy-specific intake fields

In addition to the capability intake spine, the privacy overlay adds the following:

- Field-level data sensitivity tagging for any data source flagged regulated NPI, regulated PHI, regulated PCI, biometric, or children's data. A "CRM extract" source labelled "internal" hides regulated NPI inside an aggregate source; the intake requires the field-level breakout for any source flagged regulated.
- Consumer notice posture: whether the firm's privacy notice (Reg P) and any state-law notice cover the AI use case, or whether a notice update is required.
- Sensitive-attribute use: any attributes the model uses, learns from, or infers that are sensitive under federal or state law (race, ethnicity, religion, sexual orientation, health status, immigration status, biometric identifiers, precise geolocation). Each named with the use posture (input, training feature, inferred output).
- Sub-processor and vendor PII flow: any vendor receiving NPI or PHI, with the BAA (HIPAA) or written-contract (GLBA / state law) posture noted.
- Data residency: where the data is stored, processed, and transmitted, with cross-border transfer noted where applicable.
- Retention posture: how long the data is retained, the deletion mechanism, and the firm-side process for honoring deletion requests under state privacy laws (where applicable).

#### Privacy-specific regulatory flags

When the privacy overlay is loaded, the intake's regulatory-flags table picks up:

- `GLBA_Safeguards` (where any data source is regulated NPI) with routing to `ai-risk-tiering` and `validation-plan`.
- `HIPAA` (where any data source is regulated PHI) with routing to `ai-risk-tiering` and `validation-plan`.
- `Reg_P` (consumer NPI subject to privacy notice and opt-out) with routing to `model-card-builder` for the consumer-notice posture.
- `CCPA_CPRA` and other state privacy laws as applicable (most exempt GLBA-covered data, but cover non-GLBA consumer data the firm holds).
- `NAIC_Model_672` for insurance entities in adopting states.

#### Privacy-specific open questions for downstream skills

The intake routes the following open questions when relevant:

- For `validation-plan`: how is sensitive-attribute use validated against the firm's privacy-impact-assessment posture, and how is inferred-attribute risk (where the model infers a sensitive attribute even when not given as input) tested.
- For `model-card-builder`: what is the consumer-notice posture for this use case (Reg P, state-law notice, sector-specific bulletin where applicable), and where does it sit in the privacy-notice update cycle.
- For `vendor-diligence`: BAA / written-contract status for any vendor receiving NPI or PHI; sub-processor flow-down evidence.
- For `agentic-ai-controls`: where the use case has tool privileges that read or write personal data, what controls limit personal-data scope of the tool actions.
- For privacy function review: data-residency posture and cross-border transfer mechanism (where applicable); deletion mechanism for state-privacy-law deletion requests.

#### Common pitfalls in privacy-flagged intake

- Source-level sensitivity tagging without field-level breakout. A regulated source typically contains a mix of regulated and non-regulated fields; the intake needs the field-level breakout to support data-sensitivity tiering and the privacy-impact-assessment downstream.
- Treating GLBA NPI as covering all consumer data the firm holds. Many state privacy laws apply to consumer data the firm holds in a non-GLBA capacity (employee data, marketing prospect data, B2B contact data); intake should reflect both regimes when both apply.
- Missing the inferred-attribute question. A model that does not take race or ethnicity as input may still infer them from proxies; the privacy-flagged intake records this as an open question for `validation-plan` rather than treating absence-of-input as absence-of-exposure.
- Skipping the BAA / written-contract status for vendors. The intake captures the vendor with role and criticality; the contract-status question routes to `vendor-diligence`, but the vendor presence with PHI or NPI flow is the intake fact.
- Recording a HIPAA-touch use case without the field-level PHI tagging. Life and health insurance underwriting AI using prescription-history data is the canonical case; "uses prescription data" is not enough, the intake needs the field categories.
- Recording a use case using biometric data without flagging children's data exposure separately. Biometric is one regulated category; children's data (under COPPA, state laws) is another; the intake distinguishes them.
