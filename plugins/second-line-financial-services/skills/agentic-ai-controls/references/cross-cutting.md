# cross-cutting

One section per topic. Read only the sections the scope calls for.

## ai-ethics

### AI ethics cross-cutting overlay for agentic-ai-controls

When the scope record flags `ai-ethics` for an agentic-controls review, this overlay adds ethics-specific control considerations: AI-ethics co-review, stakeholder-impact and dignity framing, bias-and-fairness coverage beyond statistical disparity, transparency and recourse posture, autonomy-creep framing on cumulative authority, vulnerable-population exposure read, workforce-AI considerations, and recommended-action items typical of ethics-flagged agentic-control reviews. The overlay is the seam between the firm's published responsible-AI posture and the operational evidence on the agentic surface.

Loaded by: `agentic-ai-controls/SKILL.md` when `scope.cross_cutting_set` includes `ai-ethics`. Cited and section-referenced anchors live in `references/source-anchors.md`.

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

#### Common pitfalls in ai-ethics-flagged agentic-controls reviews

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

### Conduct cross-cutting overlay for agentic-ai-controls

When the scope record flags `conduct` for an agentic-controls review, this overlay adds conduct-specific scoping rules, monitoring signals, regulator-notification triggers, and co-reviewer expectations. The conduct overlay is the seam where customer-impact actuation intersects with consumer-protection regimes (CFPB UDAAP, NAIC #880 fair-claims-settlement, state insurance advertising rules, FINRA supervisory and Marketing Rule frameworks).

Loaded by: `agentic-ai-controls/SKILL.md` when `scope.cross_cutting_set` includes `conduct`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- Consumer Financial Protection Act §§1031 and 1036 (12 USC §§5531 and 5536) — UDAAP framings (banking, lending, deposit servicing, payments to consumers).
- NAIC Unfair Trade Practices Act (Model #880) and state Unfair Claims Settlement Practices Acts — fair-claims-settlement standards.
- State insurance advertising rules (NAIC Advertisements of Life Insurance and Annuities Model Regulation, Model #570 [verify], and parallel state regulations).
- SEC Investment Advisers Act Rule 206(4)-1 — Marketing Rule; FINRA Rule 2210 — Communications with the Public; NASAA model rules.
- TCPA (47 USC §227) and Do-Not-Call where outbound communication is involved.
- CAN-SPAM (15 USC Chapter 103) for commercial email.
- ECOA / Reg B (12 CFR Part 1002) for adverse-action notices in lending.
- FCRA (15 USC §1681) for adverse-action notices when consumer-report data is used.
- Producer-licensing state regulations and unauthorised-practice-of-law (UPL) state rules where the agent generates communications crossing into legal advice or coverage opinions.

#### What changes when conduct is flagged

##### Authority statement gains a customer-impact framing

The out-of-scope list gains explicit conduct-relevant entries: no actuation that creates a UDAAP-relevant unfair, deceptive, or abusive act; no communication that violates state insurance advertising rules where insurance is in scope; no communication that crosses producer-licensing or UPL boundaries; no adverse-action notice generation without ECOA / FCRA-aligned reasoning.

The in-scope list specifies, per consumer-impact action class, the consumer-recourse channel the agent's actuation engages (complaint flow, dispute path, appeal process). Consumer-recourse posture is the conduct-overlay's load-bearing addition.

##### Tool inventory gains conduct-impact tagging

Each tool that produces or assists customer-facing output is tagged with the consumer-protection regime in scope (CFPB UDAAP, state insurance advertising, Marketing Rule, FINRA 2210, TCPA / Do-Not-Call, CAN-SPAM, ECOA / Reg B, FCRA). The blast-radius framing accounts for consumer-impact volume ("could send up to N customer-facing communications per minute") and the worst-case consumer-impact framing ("could deny up to N claims in a batch", "could trigger up to N adverse-action notices").

##### Human-oversight bar specific to conduct

The conduct overlay raises the oversight bar above generic AI governance:

- For consumer-facing communications generated by the agent: block-and-wait human review by the responsible function (CSR / supervisor for banking; licensed adjuster for insurance claims; adviser / supervisor for capital markets; producer / supervisor for insurance sales). Post-hoc sampling on high-volume non-bespoke communications is acceptable for tier-3 / tier-4 use cases with explicit conduct-team sign-off and a sampling-rate floor.
- For adverse-action class outputs (claim denial, lending denial, adverse-action notice, claim closure with payment less than demand, policy cancellation): block-and-wait human review is non-optional and the reviewer carries the named role required by the consumer-protection regime in scope.
- For compliance-flagged communications (Marketing Rule, FINRA 2210, state insurance advertising): the deployed surface goes through the firm's communication-review process; AI-generated communications are not exempt.

##### Threat assessment adds the customer-impact lens

In addition to the cross-cutting agentic attack classes:

- Communication-injection — adversarial content in retrieved customer or third-party content is reproduced in agent-generated customer communications, potentially creating UDAAP, advertising-rule, or Marketing-Rule violations.
- Adverse-action-notice manipulation — injected content shifts the agent's reasoning on an adverse action without the human reviewer catching the inflection.
- Producer-boundary crossing — agent-generated content drifts into producer activity (binding, quoting commitments, suitability recommendations) without licensed-producer review.
- UPL-boundary crossing — agent-generated content drifts into legal advice or coverage opinions without attorney review.

##### Mitigations expand to include the conduct control set

- Pre-send communication review (block-and-wait) for any consumer-facing output that is bespoke, adverse-action-related, or compliance-flagged.
- Communication-review audit trail aligned to firm policy (Marketing Rule preservation, FINRA 2210 review, state insurance advertising review chains).
- Suppression rules for prohibited language, prohibited content, prohibited advice categories.
- Per-jurisdiction compliance overlay on agent output (state insurance advertising rules, ECOA / FCRA reasoning, Marketing Rule fair-and-balanced presentation).
- Complaint-flow integration: the agent's output is captured in the firm's complaint-management system when a complaint surfaces.
- Adverse-action-notice review pipeline: ECOA / FCRA reasoning is generated in a way the human reviewer can validate.

##### Monitoring signals the overlay adds

- Complaint-rate and complaint-code drift (UDAAP and conduct signal).
- Communication-suppression-rule trip rate.
- Bespoke-communication ratio (agent's output bespoke vs templated; bespoke content carries higher review load).
- Adverse-action-notice volume and reviewer override rate.
- Producer-boundary crossing detection rate.
- For insurance: claim-denial-rate change, fair-claims-settlement timing distribution, state DOI complaint-volume change.
- For capital markets: Marketing Rule suppression-rule trip rate, FINRA 2210 review-cycle-time.
- For payments-fintech: Reg E dispute-handling timing, customer-recourse channel volume.

##### Incident-response and regulator-notification triggers

- CFPB UDAAP enforcement risk on consumer-facing actuation; the firm's CFPB-touchpoint chain runs.
- State DOI notification on fair-claims-settlement events (insurance overlay).
- State insurance commissioner advertising-rule complaints.
- SEC and FINRA enforcement risk on Marketing Rule and FINRA 2210 violations.
- TCPA / Do-Not-Call class-action exposure on outbound-communication misfires.
- Producer-licensing state regulator notification where the agent crossed producer activity.

##### Recommended actions add conduct-specific items

- Conduct-team co-sign on residual-risk acceptance for any consumer-facing actuation.
- Communication-review pipeline integration evidence (sample of reviewed agent-generated communication) before pre-prod sign-off.
- Complaint-rate and complaint-code baseline before go-live; monitoring threshold relative to baseline.
- For insurance claims AI, fair-claims-settlement timing baseline and per-state matrix.
- For lending agents, ECOA / Reg B and FCRA adverse-action-notice review process documented and exercised.
- For agents in capital markets adviser / broker-dealer scope, Marketing Rule and FINRA 2210 review process documented.
- For consumer-facing chatbots, UPL boundary check documented.

#### Conduct-specific output additions

In the structured object (`schemas/agentic-controls-review.schema.json`):

- `cross_cutting_overlay_notes.conduct` carries the conduct-specific fields: consumer-protection-regime tagging on tool-inventory entries, communication-review pipeline evidence, complaint-rate baseline, adverse-action-notice review evidence.
- `tool_inventory[]` entries with conduct-regime tagging.
- `human_oversight[]` entries with named-function reviewer roles per regime.
- `incident_response[]` entries with conduct-relevant `regulator_notification_trigger` populated.
- `recommended_actions[]` entries with conduct-team owner role.

#### Common pitfalls in conduct-flagged agentic-controls reviews

- Treating UDAAP framings as a CFPB-only concern. State analogues exist (state UDAP, NY Executive Law §63(12), state AG enforcement) and apply to non-bank entities.
- Designing post-hoc sampling oversight on adverse-action-notice generation. ECOA / FCRA timing and accuracy requirements demand block-and-wait review.
- Omitting state insurance advertising rules from the conduct overlay where the agent is in insurance scope. State patchwork applies.
- Treating Marketing Rule reach on AI-generated adviser communications as a compliance-team-only concern. The agentic-controls review records the human-oversight design.
- Failing to map the consumer-recourse channel. An agent that creates a customer impact without a recourse path creates a UDAAP exposure.
- For consumer-facing chatbots, ignoring the UPL boundary. The agent does not generate legal advice or coverage opinions; the boundary is enforced at the guardrail layer and exercised in test.
- For producer / agent co-pilots, ignoring the producer-licensing boundary. The agent does not actuate producer activity (binding, quoting commitments) without licensed-producer review.

## cyber

### Cyber cross-cutting overlay for agentic-ai-controls

When the scope record flags `cyber` for an agentic-controls review, this overlay sits as the primary lens, not a secondary one. Tool use, identity, and external-system actuation widen the cyber surface materially. The AI governance team often owns the artifact, but the CISO function is a co-reviewer and a co-decision-maker on residual-risk acceptance, not a downstream consumer.

Loaded by: `agentic-ai-controls/SKILL.md` when `scope.cross_cutting_set` includes `cyber`. For most agentic deployments inside regulated entities (any agent with tool use, identity, or external-system actuation), this overlay should be considered the default. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- NYDFS 23 NYCRR Part 500, especially §500.6 (audit trail), §500.9 (risk assessment), §500.11 (third-party service-provider security), §500.16 (incident-response and BCDR plan), §500.17(a) (notice to superintendent), and the October 2024 Industry Letter on AI cybersecurity that maps these obligations onto AI deployments.
- SEC cyber disclosure rules: 8-K Item 1.05 (material cybersecurity incident disclosure within four business days of materiality determination) and Reg S-K Item 106 (annual disclosure of cyber risk-management, strategy, and governance).
- 12 CFR Part 53 / Part 225 / Part 304 — banking computer-security incident notification rule (36-hour notification for "notification incidents") for bank-affiliated entities.
- FFIEC IT Examination Handbook, Information Security and AIO booklets, applied to the agent's serving environment, change controls, access controls, and incident-response integration.
- NIST SP 800-53 Rev. 5 control families (AC, AU, IR, SI, SR, SC) as the underlying control catalogue for the cyber-side mitigations the review records.
- NIST AI 600-1 Generative AI Profile cyber considerations and the OWASP LLM Top 10 / MITRE ATLAS / NCSC framings as the practitioner taxonomy for the agentic threat surface.

#### What changes when cyber is flagged

##### Authority statement gains a cyber-impact framing

The out-of-scope list gains explicit cyber-relevant entries: no credential issuance or rotation by the agent; no security-tool reconfiguration; no IR-system or audit-system writes; no privileged-account actions. These are non-optional for any agent operating in or near regulated systems.

##### Tool inventory gains control-family tagging

Each tool is tagged with the relevant NIST SP 800-53 control families and the responsible CISO sub-function. Read tools tie to AC and AU; write tools tie to AC, AU, and SI; execute tools tie to SC (sandboxing) and SI; communicate tools tie to AC, SC, and the application-security framing; compute tools tie to SC and resource-quota controls.

The tagging is not bureaucratic; it is the seam that lets the cyber team integrate the review into existing control mappings without re-doing the work in a parallel taxonomy.

##### Identity and authorisation get the cyber-side bar

The CISO identity-team is the named owner for service-account scoping, credential rotation, and secrets handling. The minimum bar:

- Service account separated from any human identity, with named owner and rotation cadence.
- Least-privilege scopes per tool, per customer, per case, per session — enforced at the platform layer, not asserted in policy.
- Secrets not in the agent's prompt context; if they appear, the exfiltration risk is structural and the residual-risk view records it.
- Identity-layer rate limits sized against the blast-radius framing, not against expected operational load.

##### Tested attack classes are framed in the cyber team's vocabulary alongside the AI vocabulary

A second-line review presented in OWASP-only vocabulary lands as a foreign object on the CISO's desk. The same review presented with MITRE ATLAS technique IDs and with mappings to existing offensive-security testing categories (application security, red-team engagement, third-party assessment) lands as an extension of work already on the cyber team's plan. Both vocabularies should appear on the same row of `threat_assessment[]`.

The agentic-specific attack classes that are non-optional under the cyber overlay: tool hijack, cross-scope tool query, excessive agency exploitation (LLM08), planner-executor seam, multi-agent message injection (where applicable), memory poisoning (where persistent memory applies), sandbox escape (where code execution applies). The `dataset_or_redteam_ref` field on each entry should name the source explicitly: vendor red-team set (vendor-self-attestation confidence), firm-internal red team (firm CISO red team or contracted offensive-security partner), third-party AI-specific assessment.

##### Sandbox guarantees are the cyber overlay's load-bearing addition

For agents with code execution, browser automation, or shell access, the sandbox section is examined under the SC family lens. Process isolation, filesystem scoping, network-egress controls, secret isolation, time-bounded execution, resource quotas, and snapshot-and-rollback posture each carry an enforcement-evidence pointer. Policy without enforcement evidence routes to recommended actions, not to coverage. For tool-use-only systems without execution, the explicit boundary statement is the cyber-side artifact ("no code-execution surface; agent is restricted to enumerated tool calls").

##### Mitigations expand to include the standard cyber control set

In addition to the AI-native guardrails (input filtering, output filtering, structured-output enforcement, refusal behaviour, content provenance), the cyber overlay expects the review to record:

- Authentication and authorisation on the agent's serving endpoint and on each tool.
- Audit logging of every model invocation, every retrieval, every tool call, every inter-agent message, every oversight event, every kill-switch action, with retention aligned to firm cyber log-retention policy and to NYDFS Part 500 §500.6 audit-trail expectations.
- Network-layer controls on the serving environment and on outbound calls.
- Secrets handling in the prompt context — secrets should not appear in the system prompt or in retrieved content; if they do, the exfiltration risk is structural.
- Vendor and supply-chain controls — foundation-model provider security posture, model-artefact integrity controls, dependency-tree controls for self-hosted components.
- Incident-response runbook integration — the AI-misuse playbook, the foundation-model-compromise playbook, and the agentic-tool-misuse playbook are named runbooks under the firm's IR programme, not standalone AI artefacts.

##### Kill-switch and drill cadence are the cyber overlay's other load-bearing addition

Drill cadence is examined under the IR family lens. Annual at minimum; quarterly for tier-1 agentic use cases; on every tool addition or major version change for any tier. The drill exercises both the technical kill-switch (cutting tool privileges, pausing serving endpoint) and the operational decision chain (who calls it, who confirms, who records, who signs off on resumption). Drill records carry into the source-trace at high confidence.

##### Monitoring adds the cyber-tagged signal set

The baseline cyber signals to add when the overlay is flagged:

- Authentication and authorisation anomalies on the agent's serving endpoint and per tool.
- Tool-invocation rate and pattern per tool — for systems with tool use, sudden expansion of tool use, off-hours activity, or new-tool-call patterns are investigation triggers.
- Cross-scope tool query anomaly — the agent invokes a tool with arguments outside its allowed scope (e.g., the system queries a market-data API on tickers outside the analyst's coverage; retrieves customer records outside the agent's case load; sends an outbound communication to a non-customer recipient).
- Output-anomaly detection (sudden shifts in refusal rate, citation patterns, response-length distribution) as a leading indicator of compromise as well as drift.
- Vendor change-of-version signals for foundation-model and serving-environment dependencies.
- Sandbox-escape signal — for systems with code execution, any boundary-violation event is a signal regardless of whether it caused harm.

Each signal retains the schema's required fields (signal, threshold, frequency, owner, escalation path); cyber-tagged entries escalate to the CISO function or to the security operations centre.

##### Incident-response section names regulator-notification triggers

The cyber overlay's most load-bearing addition. The `incident_response[]` entries list, per incident class, the regulator-notification trigger that applies in the firm's footprint:

- NYDFS-covered entities: 23 NYCRR Part 500 §500.17(a) requires notice to the superintendent within 72 hours of determining a cybersecurity event has occurred that meets the rule's criteria. Tool-misuse events resulting in unauthorised access, unauthorised action, or impairment to the security or integrity of the information system meet the criteria. The October 2024 Industry Letter signals that AI-deployment-driven events fall within scope.
- Bank-affiliated entities: 12 CFR Part 53 / Part 225 / Part 304 require notification to the primary federal regulator within 36 hours of determining a "notification incident" has occurred. Agentic tool-misuse events that materially disrupt or degrade banking services meet the threshold.
- SEC public registrants: 8-K Item 1.05 requires disclosure of material cybersecurity incidents within four business days of materiality determination. Agentic-AI-driven events causing or contributing to material cyber incidents are within scope.
- GLBA Safeguards Rule entities (FTC scope): 16 CFR §314.5(d) requires FTC notification of notification events involving the unauthorised acquisition of unencrypted customer information of 500 or more consumers.
- State breach laws: cross-state patchwork; the firm's privacy and incident-response programme normally maintains a state-by-state notification matrix that the review references rather than restating.
- Sector-specific notification triggers (state insurance commissioner notices for adopting Insurance Data Security Model Law states, banking-agency notification under 12 CFR Part 53 / Part 225 / Part 304) are loaded from the relevant sector overlay.

The off-switch criterion column is where the cyber overlay bites operationally: a cyber incident class without a defined off-switch is a finding, not an acceptable position.

##### Recommended actions add the cyber-specific items

The standard cyber-tagged recommended-actions items the overlay surfaces:

- `foundation_model_swap_revalidation` flag in change management with explicit re-run of the agentic-controls review on every vendor change-of-version notice; cyber signs off on the re-run.
- Kill-switch drill cadence ratification — annual at minimum, quarterly for tier-1, on every tool addition or major version change.
- IR drill cadence including agentic-specific incident classes (confirmed tool-misuse outside scope, confirmed cross-scope tool query, confirmed external-system unauthorised action, suspected agent compromise, foundation-model behaviour shift, sandbox-escape attempt).
- Cyber tabletop exercise with the privacy officer and the relevant business function for any agentic use case handling NPI, PHI, or material non-public information.
- Notification-decision rehearsal: the materiality-assessment process for SEC 8-K Item 1.05, the §500.17(a) notification process for NYDFS-covered entities, and the 36-hour banking-rule process for bank-affiliated entities, exercised against agentic-AI incident scenarios.
- Per-tool blast-radius re-validation on any tool addition; cyber co-signs the re-validation.

#### Cyber-specific output additions

In the structured object (`schemas/agentic-controls-review.schema.json`):

- `cross_cutting_overlay_notes.cyber` carries the cyber-specific fields: control-family tagging on tool-inventory entries, MITRE ATLAS technique mapping on threat-assessment entries, named cyber-side mitigations, named regulator-notification triggers per incident class, drill records.
- `tool_inventory[]` entries with cyber control-family tagging in `notes` or `evidence_pointer`.
- `kill_switch[]` entries with `last_drilled` and `drill_cadence` populated.
- `incident_response[]` entries with `regulator_notification_trigger` populated where applicable.
- `escalation_triggers[]` entries with cyber-tagged escalation path.
- `recommended_actions[]` entries with cyber-tagged owner role.

#### Common pitfalls in cyber-flagged agentic-controls reviews

The recurring failure modes the review should not fall into:

- Treating the AI governance team as the sole reviewer. Agentic AI with tool use is, in NYDFS framing, a cybersecurity risk class; the CISO function co-reviews and co-decides on residual-risk acceptance.
- Treating vendor adversarial-test results as evidence the deployed agent is hardened. The firm's tool inventory, authority logic, sandbox configuration, and oversight design are firm-side surfaces and need firm-side testing.
- Recording sandbox guarantees as policy assertion without enforcement evidence. A sandbox the firm has not exercised is a sandbox that does not bind in incident response.
- Treating "documented" kill switch as evidence. The drill record is the evidence; absence is theatre.
- Failing to integrate the agentic-tool-misuse runbook into the firm's IR programme. A standalone AI playbook that does not connect to the named cyber IR runbook is a paper artefact.
- Recording residual risk without a regulator-notification trigger evaluation. NYDFS §500.17(a), 12 CFR Part 53 36-hour rule, SEC 8-K Item 1.05 are not optional considerations.
- Omitting the off-switch criterion for cyber-relevant incident classes.
- Using AI-only vocabulary in a review the cyber team has to consume. MITRE ATLAS mappings cost little to add and turn the artefact into something the cyber team can integrate without translation.

## privacy

### Privacy cross-cutting overlay for agentic-ai-controls

When the scope record flags `privacy` for an agentic-controls review, this overlay adds privacy-specific scoping rules, monitoring signals, regulator-notification triggers, and co-reviewer expectations. The privacy officer co-signs residual-risk acceptance for any agent reading or writing regulated personal data with potential for tool-misuse exfiltration.

Loaded by: `agentic-ai-controls/SKILL.md` when `scope.cross_cutting_set` includes `privacy`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- GLBA Safeguards Rule (16 CFR Part 314) for FTC-scope financial institutions; notification under 16 CFR §314.5(d).
- HIPAA Privacy Rule (45 CFR Part 164 Subparts A and E), HIPAA Security Rule (45 CFR Part 164 Subpart C), Breach Notification Rule (45 CFR §§164.400-414) where the agent reads or writes PHI.
- Federal NPI definitions under 12 CFR Part 1016 (Reg P) and parallel banking-regulator regulations.
- State privacy laws: California CCPA / CPRA, Virginia VCDPA, Colorado CPA, Connecticut CTDPA, and an evolving multi-state patchwork; the firm's per-state matrix is the operative reference.
- State breach-notification laws: 50-state patchwork; firm's privacy and IR programmes maintain the matrix.
- NAIC Insurance Data Security Model Law (Model #668) where the agent operates in insurance scope.
- EU GDPR (Regulation (EU) 2016/679) for EU-nexus operations.

#### What changes when privacy is flagged

##### Authority statement gains a privacy-impact framing

The out-of-scope list gains explicit privacy-relevant entries: no cross-customer access; no data export outside firm boundary without authorisation; no sharing of regulated personal data with non-need-to-know audiences. These are non-optional for any agent operating on customer-data or PHI surfaces.

##### Tool inventory gains data-classification tagging

Each tool that touches regulated personal data is tagged with the data-classification (NPI, PHI, public, confidential, restricted) and the per-customer or per-policy scoping rule. Cross-customer or cross-policy access via a single tool call is a structural risk and should not be possible at the tool layer; if it is possible, the controls review records it as a residual risk and routes it to recommended actions.

##### Identity and authorisation get the privacy-side bar

- Service-account scopes are minimum-necessary per data-classification: an agent operating on consumer-banking customer accounts does not have read access to the mortgage subsidiary's accounts.
- Per-session, per-customer, per-case scoping is enforced at the platform layer; assertion in policy is insufficient.
- Secret management for any vendor-side privacy-relevant operations: the firm's data-vendor secrets are not in the agent's prompt context.

##### Threat assessment adds the privacy-event framing

The agentic-specific attack classes that bite hardest from a privacy perspective:

- Cross-scope retrieval bleed (cross-customer / cross-policy access via injection or misconfiguration).
- Tool hijack or cross-scope tool query that exfiltrates regulated personal data.
- Excessive-agency chains that cumulatively expose more data than any single action would justify.
- Memory poisoning on persistent-memory systems where past sessions seed the agent with cross-customer content.

The threat-assessment table records, per relevant attack class, the data-classification of the carrier and the data-classification of the impact: an injection event that exfiltrates PHI is a different residual-risk row from one that exfiltrates only NPI.

##### Mitigations expand to include the privacy control set

- Per-session and per-customer scoping enforced at the retrieval and at the tool layer.
- Data-loss-prevention controls on outbound communications generated by the agent.
- Minimum-necessary review on training and reference data; PHI is not used for foundation-model training without HIPAA-aligned authorisation.
- HIPAA-aligned access controls on PHI-touching tools (45 CFR §164.312).
- State-by-state consumer-rights handling: agent does not generate or actuate consumer-rights-handling responses without privacy-officer review.
- Vendor-side privacy controls: the foundation-model vendor does not retain inputs containing regulated personal data without HIPAA-aligned BAA or GLBA-aligned contractual provisions.

##### Monitoring signals the overlay adds

- Per-customer / per-policy retrieval audit; any confirmed cross-scope event is a privacy-officer-led investigation trigger.
- Output-anomaly detection on response length and content classification (exfiltration leading indicator).
- DLP-trip rate on agent-generated outbound communications.
- For PHI-handling agents: per-encounter audit trail per HIPAA §164.308(a)(1)(ii)(D).
- Sub-processor change signals where the foundation-model vendor or retrieval platform changes.

##### Incident-response and regulator-notification triggers

- HIPAA Breach Notification Rule (45 CFR §§164.400-414): notification to affected individuals, HHS, and in some cases the media following discovery of a breach of unsecured PHI. Tool-misuse or cross-scope events causing PHI exfiltration are within scope.
- GLBA Safeguards Rule (16 CFR §314.5(d)): FTC notification for unauthorised acquisition of unencrypted customer information of 500 or more consumers (FTC-scope entities).
- State breach-notification laws: the firm's matrix governs; the controls review references rather than restates.
- NAIC Insurance Data Security Model Law-adopting jurisdictions: state insurance commissioner notification for insurer-scope events.
- EU GDPR: Article 33 (notification to supervisory authority within 72 hours) and Article 34 (notification to data subjects) for EU-nexus events.

The off-switch criterion column is examined under the privacy-event lens: a confirmed cross-scope event takes the agent out of service pending investigation; partial-scope events get rapid-detection-and-quarantine.

##### Recommended actions add privacy-specific items

- Privacy officer co-signs residual-risk acceptance for any tool-inventory change touching regulated personal data.
- Cross-scope retrieval audit cadence: continuous detection plus quarterly sampling audit at minimum.
- DLP rule set is reviewed against the agent's actual output distribution at least quarterly.
- Vendor BAA or GLBA-aligned contractual review on every foundation-model vendor change.
- For consumer-rights handling (CCPA, GDPR data-subject access requests): the agent does not generate the response; human privacy-team review is block-and-wait.

#### Privacy-specific output additions

In the structured object (`schemas/agentic-controls-review.schema.json`):

- `cross_cutting_overlay_notes.privacy` carries the privacy-specific fields: data-classification tagging on tool-inventory entries, per-customer / per-policy scoping evidence, per-encounter audit trail confirmation, breach-notification-trigger evaluation per incident class.
- `tool_inventory[]` entries with data-classification tagging in `notes` or `evidence_pointer`.
- `incident_response[]` entries with privacy-relevant `regulator_notification_trigger` populated.
- `recommended_actions[]` entries with privacy-officer owner role.

#### Common pitfalls in privacy-flagged agentic-controls reviews

- Treating cross-scope retrieval as a probabilistic risk to be tested. It is a structural risk to be enforced at the retrieval and tool layer; tested coverage validates the enforcement.
- Recording PHI-handling without HIPAA-aligned BAA evidence on the foundation-model vendor. The BAA is the load-bearing contract; absence routes to recommended actions.
- Failing to involve the privacy officer when the use case handles PHI or when the agent's tool inventory includes data-export-class tools.
- Treating GDPR Article 33 / 34 notification timelines as a non-firm concern when the firm has EU operations or EU customers.
- Designing post-hoc sampling on consumer-rights-handling responses. Block-and-wait privacy-team review is the correct mode; CCPA / GDPR timelines require human accuracy review.
- Omitting the cross-state breach-notification matrix from the source trace. The state patchwork is the firm's responsibility to maintain.
