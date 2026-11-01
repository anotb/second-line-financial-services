# cross-cutting

One section per topic. Read only the sections the scope calls for.

## ai-ethics

### AI ethics cross-cutting overlay for board-ai-risk-pack

When the scope record flags `ai-ethics` for a board AI-risk pack, this overlay adds ethics-specific board read: AI-ethics seam in the program narrative, stakeholder-impact and dignity framing at portfolio level, bias-and-fairness coverage beyond statistical disparity, transparency and recourse posture, autonomy-creep framing for agentic deployments, vulnerable-population exposure read, workforce-AI considerations, public-commitment alignment to the firm's published responsible-AI posture, and the named ethics signals the board is expected to track. The overlay is the seam between what the firm has said publicly on responsible AI and what the board is being told in private.

Loaded by: `board-ai-risk-pack/SKILL.md` when `scope.cross_cutting_set` includes `ai-ethics`. Cited and section-referenced anchors live in `references/source-anchors.md`.

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

#### Common pitfalls in ai-ethics-flagged board packs

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

### Cross-cutting overlay: conduct — board AI risk pack

Loaded when the scope flags conduct (consumer compliance, fair-lending, fair-pricing, claims-handling fairness, consumer-facing AI generally). The overlay carries content that lands in the pack body, not background reading.

#### Where it lands in the pack

The conduct overlay threads through several pack sections:

- **Inventory state**: customer-facing AI use cases surface as a separate line in the by-architecture or by-business-line breakdown. The committee's standing question is what fraction of in-production AI directly touches customers (decisioning, customer-service assistant, complaint handling, marketing, lead generation), and how that fraction has moved.
- **Top AI risks**: customer-impact and fairness exposure named explicitly when elevated. Adverse-action notice quality on AI-driven credit decisions, fairness-metric drift on AI-driven underwriting, claims-handling AI fairness and accuracy, complaint-rate drift on AI-touched products.
- **Incidents and near-misses**: customer-impact incidents named explicitly. Fairness exposure events (disparate-impact pattern detected by monitoring), customer harm events from AI failures (incorrect decisioning, incorrect customer-facing communication), complaint surges on AI-touched products.
- **Model performance trends**: fairness-metric drift on customer-facing use cases is the standing line. Disparity ratio trending across protected and policy-relevant dimensions on tier-1 and tier-2 customer-facing AI.
- **AI governance maturity posture**: conduct program integration is one of the standing maturity dimensions. Coverage of AI in the consumer compliance program, integration with the firm's complaint-handling process, integration with adverse-action notice generation pipeline for credit decisioning AI.

#### Top AI conduct risks (catalogue for selection, not all-required)

- Adverse-action notice quality on AI-driven credit decisioning. Reg B §1002.9 and Comment 9(b)(2)-3 of the Official Staff Commentary set the framing; the principal-reasons standard under ECOA / Reg B applies to AI-driven decisions. Specificity is the recurring exam topic. (CFPB Circulars 2022-03 / 2023-03 are **withdrawn May 12, 2025; historical only.**)
- Fairness exposure on AI-driven underwriting (credit, life and health insurance). The conduct overlay carries the firm-side fairness testing posture; depth lives in `validation-plan` outputs and the model card fairness sections.
- Claims-handling AI fairness and accuracy. Multistate market-conduct exam focus on claims AI; consumer-protection enforcement on claims-AI accuracy and recourse.
- AI-generated client communications quality and accuracy where the firm is an investment adviser (Marketing Rule scope) or a broker-dealer (FINRA communications standards). Capital-markets sector overlay carries the depth.
- Customer-facing GenAI assistant accuracy and harm risk: hallucination on policy questions, incorrect statements about products or fees, refusal patterns that block legitimate customer requests.
- Complaint-rate drift on AI-touched products. The complaint-rate metric is a standing detective signal for conduct exposure that the model card monitoring section calls out; the pack carries the population view.

#### Sign-off questions tagged to conduct

Surface in the reviewer-questions section of the pack when applicable:

- For consumer-credit AI: how does the firm assure principal-reasons specificity in adverse-action notices, and what was the most recent quality review finding.
- For life or health insurance underwriting AI: what is the firm's unfair-discrimination testing cadence, and what is the most recent test finding (NAIC Bulletin fairness element; NYDFS Circular Letter; CO SB 21-169 framework where applicable).
- For customer-facing GenAI assistants: how does the firm monitor accuracy and harm, and what is the trend in customer complaints classified to AI-touched paths.
- How does the firm assure that the adverse-action notification pipeline for AI-driven credit decisions remains compliant when the underlying model is updated, swapped, or migrated to a foundation model.

#### Linkage

The depth on conduct-AI controls lives in the model card fairness and explainability section, the validation-plan fairness scope, and outputs from `consumer-compliance-fair-lending` skills (where the firm has run them). The board AI risk pack consumes briefs from those outputs rather than re-anchoring the conduct sources.

## cyber

### Cross-cutting overlay: cyber — board AI risk pack

Loaded when the scope flags cyber. The overlay carries content that lands in the pack body, not background reading. The standing anchor for AI cyber posture in financial services is the NYDFS Industry Letter on Cybersecurity Risks Arising from AI (October 16, 2024) for NY-footprint firms, layered over existing cyber program expectations (23 NYCRR Part 500, FFIEC IT Booklet, FRB SR 20-15, sector-specific frameworks).

#### Where it lands in the pack

The cyber overlay does not get its own appendix. It threads through several pack sections:

- **Top AI risks**: AI-cyber risks named explicitly when elevated. AI-enabled threats (deepfake-driven social engineering, AI-aided phishing, voice-clone attacks on call centres, synthetic identity fraud) are one bucket; the firm's own use of AI as a cyber surface (prompt injection, indirect prompt injection through retrieved content, data exposure through GenAI outputs, vendor concentration on AI providers) is the other.
- **Incidents and near-misses**: AI-cyber incident classifications surface here. Prompt-injection signal events, data-leakage events through AI systems, AI-vendor security incidents, deepfake-attempt events targeting customer authentication, and AI-aided phishing campaigns directed at the firm.
- **Foundation-model and AI vendor exposure**: AI vendor security posture is part of the standing exposure picture. Vendor security incidents, vendor breach notifications, vendor SOC 2 / ISO 27001 / FedRAMP posture, vendor model-supply-chain integrity attestations.
- **GenAI program status**: prompt-injection signal trend is the standing GenAI cyber metric. Indirect prompt injection through retrieved content (RAG poisoning, retrieved-document tampering) is an explicit sub-line where RAG is in production. Agentic tool-boundary events are the agentic-cyber metric.
- **AI governance maturity posture**: cyber program integration is one of the standing maturity dimensions. Coverage of AI in the cybersecurity program governance, integration with the firm's incident response runbook, integration with the third-party cyber-risk program for AI vendors.

#### Top AI cyber risks (catalogue for selection, not all-required)

The pack does not enumerate every category every cycle; the top-risks list carries the small number that drove committee attention this period.

- AI-enabled external threats: deepfake voice for call-centre social engineering; AI-aided phishing including spear-phishing and BEC; voice-clone attacks on executive-impersonation channels; synthetic-identity fraud on customer onboarding.
- Firm's own use of AI as cyber surface: prompt injection (direct and indirect through RAG, tool inputs, agentic context); data exposure through GenAI outputs (NPI leakage, PHI leakage where applicable, IP exposure); inappropriate use of GenAI by employees with confidential firm data (shadow AI).
- AI vendor cyber surface: foundation-model vendor security incidents; foundation-model vendor breach posture; AI-evaluation vendor security; agent-platform security; RAG infrastructure security; supply-chain integrity of vendor model artifacts.
- AI-driven monitoring degradation: cyber-AI tools (SIEM, XDR, fraud monitoring) degrading over time without re-tuning; false-positive volume spikes; coverage gaps from over-tuning.

#### Sign-off questions tagged to cyber

Surface in the reviewer-questions section of the pack when applicable:

- How does the firm monitor prompt-injection signal in production GenAI systems, and what is the trend this period.
- How does the firm assure foundation-model vendor breach posture, and what is the inventory of vendor incidents disclosed to the firm in the period.
- How does the firm address AI-enabled external threats in the cybersecurity program, and where in the program is the named ownership.
- For NY-footprint firms: how does the firm document NYDFS October 2024 Industry Letter alignment in the cybersecurity program.

#### Linkage

The depth on cyber-AI controls lives in `prompt-injection-risk` and `agentic-ai-controls` outputs (where the firm has run them). The board AI risk pack consumes briefs from those outputs rather than re-anchoring the cyber sources.
