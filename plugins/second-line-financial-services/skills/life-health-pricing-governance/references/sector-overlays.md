# sector-overlays

One section per sector. Read only the sections the scope calls for.

## insurance

### Sector overlay — insurance

This skill is the insurance-risk-compliance flagship for life and health pricing governance. The overlay is not "extra insurance flavour layered on a generic primitive"; it is the workflow itself. This file carries the rating-factor permission posture, the AU-and-ML governance content, the AIS Program cross-walk, the ECDIS provenance check, and the state-by-state bulletin variation that the artifact must reflect.

The overlay is required-on for every engagement run through this skill. SKILL.md does not gate on it.

#### Rating-factor permission posture

The unfair-discrimination test under Model #880 is actuarial-justification-driven and state-defined. Before the analysis, build the per-factor map; the map is what a DOI rate analyst reads.

- **Permitted, prohibited, silent, requires-justification.** Each rating factor needs a state-by-state status against the operative state insurance code. A factor permitted in one state and prohibited in another is the common case; the artifact names the divergence rather than collapsing to a federal answer. Where the state insurance code is silent, the factor still needs actuarial justification under #880; silence is not approval.
- **Protected classes are state-defined.** Insurance unfair-discrimination protected classes are not coterminous with ECOA / Reg B. Race, religion, national origin, gender / sex are common; sexual orientation, gender identity, marital status, genetic information, credit-based insurance score are state-by-state. Verify per state in scope.
- **Prohibited rating factors typical to life and health.** Race (universal). Religion (most states). National origin (most states). Genetic information per the Genetic Information Nondiscrimination Act (GINA) Title I for health insurance and Title II employment overlap; verify scope on the analysis date. Credit-based insurance score for life and health (state-by-state; some states permit it, others restrict). Domestic-violence-survivor status (most states for health). HIV status (most states for life). Sexual orientation and gender identity (state-by-state; verify).
- **Permitted-with-justification factors.** Age (subject to ACA bands for individual / small-group health; freer in life). Sex (state-by-state; some states require unisex rating; the Pennsylvania Mercy lifeline of cases and the Colorado SB 21-169 application are dated reference points). Tobacco use (subject to ACA 1.5:1 cap for individual / small-group health). Geography (subject to ACA rating-area structure for individual / small-group health). Health status / pre-existing conditions (prohibited in ACA-regulated individual and small-group health; permitted in life and disability subject to underwriting and #880).
- **ECDIS-derived factors.** Any rating factor derived from external consumer data (prescription history, motor-vehicle records, public records, credit-bureau attributes, location-based attributes, social-determinants-of-health attributes) carries the ECDIS layer. Provenance, consumer-disclosure, consumer-recourse, and proxy-variable risk all apply per CO regulation and NY DFS Circular Letter (where life-insurance underwriting in CO or NY is in scope).

#### AIS Program cross-walk against the NAIC AI Bulletin (December 2023)

The Bulletin is model text adopted state-by-state. Where adopted, the AIS Program is the carrier-level governance vehicle the DOI expects. The artifact runs the cross-walk element-by-element.

- **Governance.** Senior-management oversight, board awareness, named accountable role, AI-risk policy, integration with the carrier's enterprise risk-management framework. Status row: in-place / partial / gap / not-applicable plus evidence pointer (charter, policy text, committee minutes).
- **Risk management.** AI-risk-tiering rubric (cross-link to `ai-risk-tiering` with the insurance overlay), pre-deployment review, change-management triggers, incident-response posture for AI failures.
- **Testing and validation.** Pre-deployment validation, fairness testing (in unfair-discrimination terminology and in disparate-impact terminology where state DOI guidance imports it), back-testing, sensitivity analysis. Vendor-supplied AI carries vendor-validation-evidence and carrier-level validation evidence; vendor self-attestations are not evidence.
- **Third-party AI accountability.** The Bulletin holds the carrier accountable for vendor AI used on its policies. Contractual clauses, due-diligence records, monitoring posture, off-ramp posture. Cross-link to `insurance-outsourcing-review` for the outsourcing-review side.
- **Monitoring.** Ongoing performance monitoring, drift detection, fairness-metric monitoring, intervention thresholds, owner role, reporting cadence.
- **Documentation.** Model documentation, data-lineage documentation, decision-record documentation, retention posture.
- **Transparency.** Internal transparency to the model-risk function and to the second-line review function; consumer-facing transparency where state DOI guidance requires it (CO regulation; NY DFS Circular Letter).
- **Fairness.** Translate to the unfair-discrimination vocabulary for the DOI audience; state DOI guidance increasingly imports a disparate-impact-style monitoring expectation alongside the #880 actuarial-justification standard.

Where the carrier has not yet adopted an AIS Program, the artifact says so and tags the gap to the regulatory-affairs lead.

#### ECDIS provenance check

Where any rating factor is derived from external consumer data, run the ECDIS layer.

- **Source identification.** Which third party supplied the data; which underlying record types are in scope; what jurisdictions the data covers.
- **Permitted-use posture.** Whether the data source's terms of use permit insurance-underwriting use; whether the underlying records carry consumer-consent requirements (FCRA where in scope; HIPAA where PHI; state insurance information privacy frameworks per Model #670).
- **Proxy-variable risk.** Whether the factor or its components proxy for prohibited rating factors. Run the test factor-by-factor; do not collapse to a single statement.
- **Consumer-recourse channel.** Where required by state regulation (CO; NY DFS), name the channel, the SLA, and the documentation posture.
- **Adverse-information-disclosure posture.** Where required, name the consumer notification timing and content.
- **Monitoring metric.** Drift in the input distribution; drift in the output distribution; fairness-metric trend; consumer-complaint volume tied to the factor.

#### State-by-state bulletin variation

Build the per-state row using the NAIC AI Working Group adoption tracker as the source of truth on the analysis date. Do not freeze a state list in the artifact; verify on engagement.

- **Colorado.** SB 21-169 implementing regulation. Most prescriptive on ECDIS in life-insurance underwriting. Verify whether the regulation has been extended beyond life-insurance underwriting on the analysis date.
- **New York.** NY DFS Insurance Circular Letter (January 2024) on AI and ECDIS in life-insurance underwriting. Disclosure, fairness, governance, consumer-recourse.
- **California.** CA DOI bulletin on AI use in insurance. Broader scope than CO and NY.
- **Other adopting states.** NAIC December 2023 Model Bulletin adoption status tracked by the NAIC AI Working Group. Adoption may be by bulletin, by regulation, or by guidance letter; the format affects the artifact's bulletin-alignment row.
- **Non-adopting states.** Where a state has not adopted the Model Bulletin or analogous guidance, the artifact carries the standard state DOI rate-filing checklist and the federal-baseline analysis only; do not import expectations the state has not adopted.

#### Federal model-risk-equivalent posture

State DOIs cite the **Joint Interagency Revised Guidance on Model Risk Management (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026)** — which supersedes SR 11-7 — as analogous model-risk expectation language for ML pricing models. Treat as analogous, not binding. (GenAI / agentic AI is out of scope of the joint guidance per footnote 3; state DOI AI bulletins remain the operative source for AI-specific governance.)

- **Model documentation.** Purpose, theory, design choices, data-input documentation, assumptions, limitations.
- **Validation evidence.** Independent validation; conceptual-soundness review; ongoing-monitoring plan; outcomes analysis; benchmarking.
- **Performance-monitoring plan.** Performance metrics; drift detection; threshold-breach response; monitoring cadence; owner role.
- **Change-management process.** Trigger criteria for revalidation; approval chain; documentation update obligations.

Cite the joint guidance (OCC 2026-13 / SR 26-2 / FIL-15-2026, April 17, 2026) by reference into `references/source-anchors.md`. SR 11-7 is superseded; cite only when reading pre-April-17-2026 evidence.

#### ACA bright-lines (where individual / small-group health is in scope)

Bright-line rules under PHSA §2701 and 45 CFR Part 147. The artifact carries each as a check, not a discussion.

- **Permitted rating factors.** Family size, geography, age (within 3:1 band for adults), tobacco use (within 1.5:1 band).
- **Prohibited rating factors.** Health status, gender, occupation, claims history, duration of coverage, and any factor not on the permitted list.
- **Geographic rating area.** State-defined within the federal default rules at 45 CFR §147.102.
- **Rating-area-vs-zip-code mismatch.** Common refile-issue source; verify the mapping.

#### Illustration check (where life is in scope and the change touches illustrated values)

Model #582. Carry the section-by-section status against the model regulation.

- **Disciplined-current-scale.** Current-scale assumptions documented and within the carrier's experience.
- **Self-support test.** Model #582 §6 (or successor — verify section).
- **Lapse-support test.** Model #582 §7 (or successor — verify section).
- **Illustration-actuary certification.** Annual certification on file; named role.
- **Illustrated-vs-non-illustrated-vs-actual tracking.** Variance reports.

#### Common pitfalls

- Treating Model #880 unfair-discrimination as if it were ECOA / Reg B disparate-treatment. The statutory test is different (actuarial justification matters; permitted-vs-prohibited rating factors differ; protected classes are state-defined).
- Letting the actuarial memorandum stand in for the governance review. The actuarial work justifies the rates; the second-line file justifies the governance over the actuaries and the model.
- Skipping ECDIS provenance for any rating factor that touches third-party consumer data. CO and NY DFS guidance is explicit.
- Forgetting the AIS Program structure. Carriers are increasingly being asked for the AIS Program document by state DOIs.
- Treating the federal model-risk frame (now OCC 2026-13 / SR 26-2 / FIL-15-2026, superseding SR 11-7) as a banking-only thing. State DOIs cite the federal frame as analogous; address it explicitly.
- Missing the ACA layer when individual or small-group health is in scope.
- Conflating illustration governance (Model #582) with rate-filing governance.
- Drafting the artifact as a model-validation report. The artifact is a pricing-governance review; validation is one input.
- Collapsing state-by-state divergence into a federal answer.
- Naming institutions in narrative beyond public defendants in finalised state-DOI consent orders or rate-filing rejections.
