# Validation plan: [model name and version]

Starting structure for a validation plan. Depth flexes per pillar with tier and validation type; the section list does not. A targeted revalidation may compress conceptual soundness to a paragraph; a full initial validation expands every section. Items without evidence carry `[evidence needed]` and route to the engagement issue log.

The plan is a draft until the validator and the model risk committee (or equivalent reviewer) attest. The downstream validation report consumes this plan as its scope contract; this plan does not execute the testing.

---

## 1. Plan metadata

- Model ID and version: [canonical firm model ID]
- Tier: [tier-1 / tier-2 / tier-3 / tier-4 / tier-unassigned, with reference to `ai-risk-tiering` output]
- Validator: [function or role; never named individuals]
- Model owner: [function or role]
- Validation type: [initial / annual-revalidation / vendor-swap-revalidation / off-cycle-trigger / post-incident]
- Scope date: [YYYY-MM-DD]
- Use-case ID (links to `ai-use-case-intake`): [ID]
- Engagement-scope ID (if `scoping` was run): [ID]

---

## 2. Validation depth

Depth is set per pillar, not as a single label. Tier drives the default; pillar-level deviations are explained.

| Pillar | Depth | Justification |
|---|---|---|
| Conceptual soundness | [full / targeted / light-touch / monitor-only] | [why this depth for this pillar this cycle] |
| Outcomes analysis | [full / targeted / light-touch / monitor-only] | [why] |
| Ongoing monitoring | [full / targeted / light-touch / monitor-only] | [why] |

Tier justification: [one paragraph explaining how the tier and the validation type drove the depth distribution].

---

## 3. Conceptual soundness scope

What the validator will read against the model's design. For a vendor-opaque foundation model, the conceptual soundness work pivots from theory replication to vendor evidence review plus firm-side rationale.

- Scope items: [theory and design rationale; segmentation choice; alternatives considered; foundation-model selection rationale where applicable; RAG architecture review; prompt design review; tool boundary review for agentic systems]
- Methods: [document review, replication, benchmark against challenger, vendor system-card review, red-team summary review]
- Vendor model card review: [required when foundation model is third-party; enumerate vendor evidence in scope (system card, evaluation report, red-team summary, contract addenda)]
- Success criteria: [what makes the conceptual soundness review pass]

---

## 4. Data review scope

- Scope items: [training data fitness, evaluation data construction, retrieval corpora inventory and access controls, lineage to system of record, exclusions check]
- Methods: [data-quality profiling, lineage trace, access-control review, exclusion verification]
- Lineage evidence: [pointers to system-of-record extracts, data dictionaries, governance artifacts]
- Exclusions check: [prohibited rating factors, fairness-sensitive proxies removed in prior reviews, fields outside lawful basis under applicable privacy law]
- Success criteria: [what makes the data review pass]

For foundation-model training data, firm visibility is typically limited to vendor system-card statements; record this as a known limitation, not as a data-review failure.

---

## 5. Outcomes analysis scope

For each test the validator will run or supervise:

| Test name | Method | Dataset | Segment cuts | Success criterion | Owner | Benchmark against |
|---|---|---|---|---|---|---|
| [test] | [method] | [dataset] | [segments] | [criterion in firm-policy units] | [function] | [challenger / prior version / vendor benchmark / external reference] |

Deployed-environment metrics dominate where the model is in production. For initial validation, the test set construction is itself a scope item. For GenAI: faithfulness, citation precision, refusal rate, hallucination rate, agent-edit rate, latency are the typical baseline; tailor to the use case.

---

## 6. Robustness, adversarial, and stress testing scope

Attack class catalogue is tied to architecture flags; missing the most relevant attack class is the recurring defect.

| Attack class | Method | Success criterion | Owner |
|---|---|---|---|
| [out-of-time / stress scenario / adversarial input / direct prompt injection / indirect prompt injection via retrieved content / jailbreak / RAG poisoning / model extraction / tool misuse / goal hijack] | [method] | [criterion] | [function] |

For traditional ML: out-of-time backtest, stress scenario, segment robustness, adversarial input. For RAG: add indirect prompt injection on retrieved content, RAG poisoning. For agentic: add tool misuse, goal hijack. For vendor-hosted GenAI: add a vendor model-version swap drill. For execution algos in capital markets: align with SEC Rule 15c3-5 controls (load `references/sector-overlays.md#capital-markets`).

---

## 7. Fairness, explainability, and transparency scope

| Dimension | Method | Success criterion | Method limitations |
|---|---|---|---|
| [protected or policy-relevant dimension] | [method] | [criterion] | [known limitations of the method as applied] |

For insurance pricing or underwriting, frame the test against unfair discrimination per state insurance code (NAIC Model #880 vocabulary) in addition to or in place of generic fairness vocabulary. Load `references/sector-overlays.md#insurance`.

For credit decisioning under ECOA / Reg B: load `references/sector-overlays.md#banking` and integrate with the firm's fair-lending test plan; the validator's scope and the consumer-compliance test plan reference each other but stay distinct artifacts.

---

## 8. Ongoing monitoring scope

For each monitoring entry the validator expects to see in production:

| Metric | Threshold | Frequency | Owner | Escalation path | Revalidation trigger |
|---|---|---|---|---|---|
| [metric] | [threshold in firm-policy units] | [continuous / daily / weekly / monthly / quarterly] | [function] | [named committee / officer / process] | [yes / no] |

All six columns are required on every entry. The `revalidation_trigger` column is what distinguishes the validator's monitoring view from the model owner's operational monitoring view; the same metric may be both, but the trigger flag makes the seam explicit.

For GenAI baseline: foundation-model version monitoring, prompt-injection signal monitoring, retrieval-source audit, citation precision sampling, agent-edit rate (when human-in-the-loop), customer complaint code drift.

---

## 9. Effective challenge questions

For each question:

| Question | Design choice or assumption it interrogates | Expected evidence | Owner of response |
|---|---|---|---|
| [question] | [the specific design choice, assumption, or failure mode] | [the evidence the validator expects to receive] | [function] |

Each question names the design choice or assumption it probes. "Does the model meet our policy" is compliance theatre, not effective challenge. "The agent-review gate is the only preventive control between the assistant output and the customer; what is the off-switch criterion if agent-edit rate falls below threshold for two consecutive months" probes a specific design choice and a specific failure mode.

---

## 10. Dependencies and prerequisites

- Data access: [extracts, feeds, system-of-record access required]
- Environment: [validation environment, sandbox, replay capability]
- Vendor evidence: [system card, evaluation report, red-team summary, contract addenda]
- Foundation-model card: [where applicable]
- Upstream artifacts: [`ai-use-case-intake` record, `ai-risk-tiering` output, prior validation report, prior model card]
- Cross-function access: [consumer compliance for fair-lending integration, information security for cyber tests, vendor management for vendor evidence chase]

---

## 11. Timeline, owner, deliverables

| Milestone | Date | Owner |
|---|---|---|
| [start] | [YYYY-MM-DD] | [function] |
| [data assembly] | [date] | [function] |
| [conceptual soundness review] | [date] | [function] |
| [outcomes analysis] | [date] | [function] |
| [robustness and adversarial testing] | [date] | [function] |
| [fairness review] | [date] | [function] |
| [draft validation report] | [date] | [function] |
| [reviewer attestation] | [date] | [function] |

Deliverables: [downstream validation report; refreshed model card via `model-card-builder`; issue-log entries; pre-prod or production approval input].

---

## 12. Source trace and confidence

For every material scope claim:

| Claim | Source | Evidence reference | Confidence |
|---|---|---|---|
| [claim] | [document, system, person, vendor evidence, or `[evidence needed]`] | [pointer] | [high / medium / low / evidence-needed] |

Vendor self-attestation carries low to medium confidence. Firm-independent evaluation carries higher confidence. Do not collapse vendor and firm evidence into one line.

---

## 13. Sector overlay notes (when applicable)

When the scope names a sector, the matching `references/sector-overlays.md#<sector>` adds named scope items here. Examples:

- Banking: ECOA / Reg B fair-lending integration; CCAR / DFAST overlap if model is stress-eligible; FFIEC BSA/AML manual scope for AML models; OCC Heightened Standards governance touchpoint.
- Insurance: AIS Program element coverage per NAIC Bulletin Dec 2023; per-state DOI bulletin alignment (CO, NY DFS, CA); unfair-discrimination framing under Model #880; ORSA materiality.
- Capital markets: SEC Rule 15c3-5 controls overlap for execution algos; Rule 206(4)-7 annual review cadence for adviser models; books-and-records reach (Rule 204-2); Marketing Rule overlap for AI-generated communications.
- Payments and fintech: sponsor-bank model risk responsibility allocation; transaction monitoring model risk overlap with BSA/AML; account-takeover detection model surface.

If no sector overlay is loaded, this section is omitted.

---

## 14. Cross-cutting overlay notes (when applicable)

When the scope flags cyber, privacy, or conduct, the matching `references/cross-cutting.md#<topic>` adds named scope items here.

- Cyber: prompt-injection robustness scope, RAG poisoning, model extraction, NYDFS October 2024 letter alignment.
- Privacy: PII memorisation tests, training-data leak tests, retrieval over inappropriate corpora.
- Conduct: fairness, harmful content, customer impact monitoring tied to UDAAP and consumer compliance.

If no cross-cutting overlay is flagged, this section is omitted.

---

## Reviewer attestation block

The plan is reviewable when every named section is filled and source trace is complete. The human reviewer attests:

- **Reviewer**: [function]
- **Reviewer date**: [YYYY-MM-DD]
- **Decision**: [accept / accept with conditions / reject and re-work]
- **Conditions (if any)**: [conditions, owners, dates]
- **Onward routing**: [validation execution / pre-prod gate via `genai-pre-prod-review` for GenAI / model risk committee]

The plan is filed only after attestation. The downstream validation report consumes this plan as its scope contract.
