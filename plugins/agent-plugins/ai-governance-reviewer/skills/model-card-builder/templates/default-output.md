# Model card: [model name and version]

Starting structure for a model card. Depth flexes with tier and audience; the section list does not. A tier-4 card may compress sections to two or three lines; a tier-1 card expands each. Items without evidence carry `[evidence needed]` and route to the engagement issue log.

The card is a draft until a human reviewer attests.

---

## 1. Card metadata

- Model ID and version: [canonical firm model ID]
- Model owner and function: [name, function]
- Validator: [name, function]
- Second-line reviewer: [name, function]
- Card date: [YYYY-MM-DD]
- Tier: [tier-1 / tier-2 / tier-3 / tier-4 / tier-unassigned, with reference to `ai-risk-tiering` output]
- Lifecycle stage: [development / pre-prod / prod / monitoring-only / retirement]
- Classification: [internal / restricted / confidential as per firm classification]
- Use-case ID (links to `ai-use-case-intake`): [ID]
- Engagement-scope ID (if `engagement-scoping` was run): [ID]

---

## 2. Intended use

- Purpose: [one or two sentences on what the model is for]
- Intended users: [function or role names; never named individuals]
- In-scope decisions: [bulleted list of decisions the model is intended to support]
- Out-of-scope decisions: [bulleted list of decisions the model is explicitly not used for]
- Geographic scope: [jurisdictions, states, countries]
- Customer segment scope: [segments in or out of scope]

---

## 3. System description

- Model type: [traditional ML class, prompted LLM, RAG, agent, or hybrid]
- Foundation model (if applicable): provider, name, version, version pinning posture (pinned, floating, rolling-with-notice)
- Retrieval-augmented generation (if applicable): RAG corpora named, retrieval scoping rules, refresh cadence
- Tools (if applicable): tool inventory, tool boundary controls, autonomy level
- Autonomy level: [advisory / advisory-with-suggested-action / human-in-the-loop / human-on-the-loop / agentic-with-tool-use / fully-autonomous]
- Dependencies: [upstream systems, vendors, data feeds]

---

## 4. Training and reference data

For each data source the model uses:

| Source | Purpose | Sensitivity | Licensing | Retention | Lineage | Exclusions |
|---|---|---|---|---|---|---|
| [source] | [training / fine-tuning / retrieval / evaluation / monitoring / reference] | [NPI, PHI, public, confidential] | [licence terms] | [retention period] | [system of record reference] | [excluded fields, prohibited rating factors] |

For foundation-model training data, firm visibility is typically limited to vendor system-card statements; record at appropriate confidence in source trace. Excluded fields cover prohibited rating factors, proxy variables identified as fairness-sensitive in upstream review, and fields outside lawful basis under applicable privacy law.

---

## 5. Performance summary

For each performance metric:

| Metric | Value | Segment | Evaluation set | Deployed-environment | Date | Owner |
|---|---|---|---|---|---|---|
| [metric] | [value] | [overall, by FICO band, by region, by line of business, by call-type] | [test-set name] | [yes/no] | [YYYY-MM-DD] | [function] |

Segment-level reporting on protected and policy-relevant dimensions belongs here even when overall performance is acceptable. Deployed-environment metrics dominate production cards; lab-only metrics carry separately and are labelled. For GenAI, the typical core set is faithfulness, citation precision, refusal rate, and latency, supplemented with task-specific metrics.

---

## 6. Robustness and stress testing

For each test:

| Test | Method | Result | Owner | Date |
|---|---|---|---|---|
| [test name] | [method, e.g. out-of-time, stress scenario, adversarial, prompt injection, RAG poisoning, jailbreak] | [pass / fail / specific result] | [function] | [YYYY-MM-DD] |

For GenAI use cases the typical baseline is prompt injection, jailbreak, RAG poisoning, and the vendor-supplied test set. Add tests proportionate to the threat surface identified by `prompt-injection-risk` and `rag-evaluation-review`.

---

## 7. Fairness and explainability

Fairness:

| Dimension | Metric | Value | Disparity assessment | Method limitations |
|---|---|---|---|---|
| [protected or policy-relevant dimension] | [metric, e.g. AIR, AUC by segment, agent-edit-rate by segment] | [value] | [pass / monitor / breach against firm policy] | [method limitation] |

Explainability:

- Method: [SHAP, LIME, citation-of-source for RAG, attention attribution]
- Scope: [decision-level, model-level, feature-level]
- Limitations: [known limitations of the method as applied]

For insurance pricing or underwriting, frame the test against unfair discrimination per state insurance code (NAIC Model #880 vocabulary) in addition to or in place of generic fairness vocabulary. Load `references/sector-overlays/insurance.md`.

---

## 8. Limitations and known failure modes

For each limitation:

- **[Failure mode name]** — [concrete description of the failure]
  - Example: [a specific case observed in pilot, validation, or monitoring]
  - Mitigation: [how the firm reduces the residual risk; reference the control in section 10]

Each limitation needs a concrete example and a named mitigation. "Model may not generalise" is not a limitation; it is a hedge.

---

## 9. Monitoring plan

For each monitoring entry:

| Metric | Threshold | Frequency | Owner | Escalation path |
|---|---|---|---|---|
| [metric] | [threshold value, in firm policy units] | [continuous / daily / weekly / monthly / quarterly] | [function] | [named committee / officer / process] |

All four columns (threshold, frequency, owner, escalation path) are required on every entry.

For GenAI the typical baseline is foundation-model version monitoring, prompt-injection signal monitoring, retrieval-source audit, citation precision sampling, agent-edit rate (when human-in-the-loop), and customer complaint code drift. Tailor to the architecture.

---

## 10. Controls

For each control:

| Control | Type | Owner | Evidence pointer |
|---|---|---|---|
| [control name] | [preventive / detective / response / compensating] | [function] | [system of record, evidence repository pointer] |

Preventive examples: input filtering, query scoping, agent training, tool boundary enforcement, version pinning.
Detective examples: agent review gate, sample-based faithfulness review, override sampling, monitoring-pack review, complaint-code review.
Response examples: vendor change-of-version notice triggering re-validation, off-switch criteria, incident response, customer notification posture.

Each control has a named owner and an evidence pointer. A control without an evidence pointer is policy, not a control.

---

## 11. Change management

Re-validation triggers:

| Change type | Re-validation trigger | Approver |
|---|---|---|
| [feature add / remove] | [trigger condition] | [function] |
| [training data window shift] | [trigger condition] | [function] |
| [performance breach] | [breach for N consecutive periods] | [function] |
| [foundation-model swap, GenAI only] | [vendor change-of-version notice] | [function] |
| [RAG corpus scope change, GenAI only] | [scope change description] | [function] |
| [tool addition, agent only] | [new tool added] | [function] |
| [autonomy-level change] | [shift from human-in-the-loop to human-on-the-loop, etc.] | [function] |

For tier-1 and tier-2 models, the head of model risk approves; for tier-3 and tier-4, the model owner with second-line concurrence is typical. Confirm against the firm's model risk policy.

---

## 12. Sign-off questions

For each section above, list the questions a reviewer should be answered before signing off the card:

1. **Intended use** — [concrete question that probes the boundary of the in-scope/out-of-scope split]
2. **System description** — [concrete question that probes a foundation-model, RAG, or tool dependency]
3. **Training and reference data** — [concrete question that probes a sensitivity, exclusion, or lineage gap]
4. **Performance summary** — [concrete question that probes a segment-level finding]
5. **Robustness** — [concrete question that probes the threshold at which a test result triggers action]
6. **Fairness and explainability** — [concrete question that probes a protected-class disparity or an explainability limitation]
7. **Limitations** — [concrete question that probes the firm's tolerance for a specific failure mode]
8. **Monitoring plan** — [concrete question that probes an escalation path or threshold-setting decision]
9. **Controls** — [concrete question that probes a control reliance or a single-point-of-failure]
10. **Change management** — [concrete question that probes a re-validation trigger]
11. **Sector overlay (if applicable)** — [concrete question raised by the loaded sector overlay reference]
12. **Cross-cutting overlay (if applicable)** — [concrete question raised by the loaded cross-cutting overlay reference]

Questions are tagged to sections, answerable from the card, and specific to this card. "Is this fit for purpose" applies to every card and challenges nothing.

---

## 13. Source trace and confidence

For every material claim in the card:

| Claim | Source | Evidence reference | Confidence |
|---|---|---|---|
| [claim] | [document, system, person, vendor evidence, or `[evidence needed]`] | [pointer] | [high / medium / low / evidence-needed] |

`[evidence needed]` flags route to the engagement issue log. Unresolved items either close before sign-off or are accepted with a remediation plan.

---

## 14. Sector overlay notes (when applicable)

When the engagement scope names a sector, the matching `references/sector-overlays/<sector>.md` adds named fields here. Examples:

- Banking: ECOA/Reg B adverse action surface (for credit decisioning); FFIEC manual exposure (for AML/fraud); OCC Heightened Standards 12 CFR Part 30 Appendix D risk-governance touchpoint.
- Insurance: AIS Program element status against the NAIC Bulletin on the Use of AI Systems by Insurers; per-state DOI bulletin status; ECDIS provenance; ORSA materiality posture; HIPAA touch.
- Capital markets: Rule 15c3-5 controls overlap (for execution algos); FINRA supervisory expectations (for surveillance); Marketing Rule overlap (for AI-generated client communications); books-and-records reach (Rule 204-2).
- Payments and fintech: sponsor-bank model risk responsibility allocation; transaction monitoring model risk overlap with BSA/AML; account-takeover detection model surface.

If no sector overlay is loaded, this section is omitted.

---

## Reviewer attestation block

The card is reviewable when every named section is filled and source trace is complete. The human reviewer attests:

- **Reviewer**: [name, function]
- **Reviewer date**: [YYYY-MM-DD]
- **Decision**: [accept / accept with conditions / reject and re-work]
- **Conditions (if any)**: [conditions, owners, dates]
- **Onward routing**: [model risk committee / pre-prod gate / inventory of record / regulator response file]

The card is filed only after attestation.
