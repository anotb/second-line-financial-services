# Board AI risk pack: [Committee name] — [Period]

Starting structure for an AI risk committee pack (or the AI section of a board risk committee). Depth flexes with firm posture (Heightened Standards covered bank, mid-cap regional, RIA, insurer, payments-fintech) and audience (standalone AI risk committee, board-level AI section, regulator-attended meeting, annual program review). The named sections do not flex; if a section is omitted, the rationale is documented (for example, "EU AI Act Article 9 not in scope; firm has no EU-deployer or EU-provider exposure" goes in the AI governance maturity section).

The pack is a draft until the AI Governance Lead and the head of model risk review and the committee secretary distributes.

---

## Cover

- Committee: [e.g., AI Risk Committee / Board Risk Committee (AI Section) / Technology and Innovation Committee]
- Meeting date: [YYYY-MM-DD]
- Period covered: [start YYYY-MM-DD] to [end YYYY-MM-DD]
- Classification: [internal / board-confidential / regulator-shareable]
- Pack version: [v1 / v1-revised]
- Engagement-scope ID (if `scoping` was run): [ID]

---

## Decisions requested

The first body section a committee member reads. A pack with no decision items is a status update, not a committee instrument.

| ID | Decision requested | Recommended motion | Vote / acknowledgement | Owner |
|---|---|---|---|---|
| D1 | [decision] | [motion] | [vote-required / acknowledgement-only / noting-only] | [role] |
| D2 | [decision] | [motion] | [vote-required / acknowledgement-only / noting-only] | [role] |

Full detail of each decision (options, rationale, dissents, requested vote) is in the Decisions section below.

---

## Executive summary

Up to five bullets, in AI Governance Lead voice. The call-outs the chair reads first.

- [Headline tier-mix movement in the period]
- [Top AI risk drawing the committee's attention]
- [Material incident or near-miss]
- [Foundation-model exposure posture]
- [Decision pointer]

---

## AI inventory state

| Metric | Current | Prior | Change |
|---|---|---|---|
| Total in-scope use cases | | | |
| Tier-1 | | | |
| Tier-2 | | | |
| Tier-3 | | | |
| Tier-4 | | | |
| In production | | | |
| In pre-prod gate | | | |
| Retired this period | | | |

By architecture flag:

| Architecture | Count |
|---|---|
| Traditional ML | |
| Foundation-model | |
| Foundation-model + RAG | |
| Agentic | |
| Agentic with tool use | |

By sector or business line:

| Segment | Count |
|---|---|
| | |

Tier movements in the period:

| Use case | From tier | To tier | Rationale |
|---|---|---|---|
| | | | |

Inventory reconciliation against the inventory of record: [reconciled / partial / not-reconciled]. If partial or not-reconciled, the data confidence label is constrained.

---

## Top AI risks

Each named risk has trajectory (improving / stable / worsening / new) with a one-line basis. Owners are roles, not named individuals.

| Risk ID | Risk name | Trajectory | Trajectory basis | Exposure | Key drivers | Owner | Linked use cases or programs | Target action |
|---|---|---|---|---|---|---|---|---|
| TR1 | [risk name] | [improving / stable / worsening / new] | [one line] | [number with unit, or null] | [drivers] | [role] | [IDs] | [action with date] |

For risks flagged `new`, include the `logged_date` in the structured object.

---

## In-flight reviews and decisions

| Use case or program | Stage | Decision due | Second-line recommendation |
|---|---|---|---|
| | [intake / tiered / validated / pre-prod-gate / in-prod / retired] | [YYYY-MM-DD] | |

Items the committee may carry forward rather than decide are flagged with the reason.

---

## Incidents and near-misses

### Incidents

| Incident ID | Date | Classification | Severity | Regulator notification | Customer impact | Owner | Status |
|---|---|---|---|---|---|---|---|
| I1 | [YYYY-MM-DD] | [classification enum] | [informational / low / medium / high / critical] | [not-applicable / evaluating / notified / no-notification-required-rationale-on-file] | | [role] | [open / under-investigation / remediated / closed] |

Tier-1 and high/critical incidents get a paragraph of commentary in the body; the rest sit in the structured object.

### Near-misses

[Either: list near-misses table, or: "No near-misses logged in this period." Empty section without statement is the standing trap.]

| Near-miss ID | Date | Classification | Narrative | Owner |
|---|---|---|---|---|
| NM1 | [YYYY-MM-DD] | | | [role] |

---

## Regulator and exam interactions

| Regulator | Item | Topic | Status | Owner | Target close | Slippage commentary (if over age) |
|---|---|---|---|---|---|---|
| | [MRA / MRIA / supervisory-letter / exam-finding / information-request / consent-order] | | [open / in-remediation / responded / closed] | [role] | [YYYY-MM-DD] | |

For federally regulated banks, SR 12-17 expects committee management of the open population, not just counting. Over-age items carry slippage commentary.

---

## Foundation-model and AI vendor exposure

### Top vendors

| Vendor | Category | Use-case count | Version-change posture |
|---|---|---|---|
| | [foundation-model-provider / evaluation-vendor / rag-infrastructure / agent-platform / ml-platform / other] | | [pinned / floating / rolling-with-notice / unknown] |

### Foundation-model concentration

| Provider | Model | Use-case count |
|---|---|---|
| | | |

Top-three concentration ratio: [0.0 to 1.0]. The ratio that exceeds firm threshold is a decision item.

### Key dependencies

- [Foundation-model providers, evaluation vendors, RAG infrastructure, agent platforms]

### Watch list

| Vendor | Concern | Narrative |
|---|---|---|
| | [deprecation-notice / security-incident / regulatory-action / quality-drift / other] | |

---

## Model performance trends

Population view; use-case-level depth lives in the model cards.

- **Tier-1 and tier-2 in-production count**: [number]
- **Red breaches**: [list with use case ID, metric, owner role, status]
- **Drift signals across the population**: [summary]
- **Fairness-metric drift on customer-facing use cases**: [summary]
- **GenAI-specific drift (refusal rate, faithfulness, citation precision)**: [summary]

---

## GenAI program status

The section the committee will spend most time on. Velocity and visibility require its own block.

### Pipeline

| Pipeline stage | Count |
|---|---|
| Intake | |
| In pre-prod gate | |
| In production | |
| Retired this period | |

### Pre-prod gate throughput

- Decisions made: [number]
- Exceptions granted: [number]
- Items returned: [number]
- Exception rationale summary: [narrative]

### RAG and agentic posture

- RAG corpora under governance: [count]
- Agentic deployments by autonomy level: [list with autonomy level enum and count]

### GenAI incident posture

- Prompt-injection signal trend: [narrative]
- Retrieval-source audit findings: [narrative]
- Agentic tool-boundary events: [narrative]

---

## AI governance maturity posture

Framework: [nist-ai-rmf / iso-42001 / naic-ais-program / eu-ai-act-deployer / firm-bespoke / blended]

Narrative summary: [one-paragraph posture statement against the named framework, calibrated to current cycle]

Evidence appendix pointer: [pointer to the maturity self-assessment artifact when one exists]

For insurers operating an AIS Program, this section maps to the AIS Program elements (governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness). For firms pursuing or holding ISO/IEC 42001 certification, the section is one of the standing inputs to §9.3 management review.

---

## Policy and framework changes since last meeting

| Change | Effective date | Owner |
|---|---|---|
| | [YYYY-MM-DD] | [role] |

The committee's standing question: did anything material change under the AI governance framework without committee visibility?

---

## Forward look

Two cycles ahead, named, dated, regulator-anchored. "Continuing to monitor the landscape" is filler.

- [Regulator developments expected (rule, date, implication)]
- [Use cases on the runway for tier escalation or pre-prod gate]
- [GenAI deployments on the runway for production]
- [Foundation-model vendor changes expected]
- [Validation cycles due]
- [Training and capability program milestones]

---

## Decisions (full detail)

For each decision listed at the top of the pack:

### [Decision ID]: [Decision title]

- **Background**: [one paragraph]
- **Options considered**: [option A, option B, option C]
- **Recommended motion**: [motion, with rationale]
- **Dissents (if any)**: [named role and dissent rationale]
- **Requested action**: [vote-required / acknowledgement-only / noting-only]
- **Owner**: [role]

---

## Appendix A: Data confidence

- **Data confidence label**: [high / medium / low / unknown]
- **BCBS 239 known limitations** (where firm in scope): [list from the most recent self-assessment]
- **Inventory reconciliation status**: [reconciled / partial / not-reconciled]

If known limitations are non-empty or inventory reconciliation is partial or not-reconciled, the data confidence label cannot be high.

---

## Appendix B: Source trace

For every material claim in the pack:

| Claim | Source | Evidence reference | Confidence |
|---|---|---|---|
| [claim] | [system, document, or `[evidence needed]`] | [pointer] | [high / medium / low / evidence-needed] |

---

## Appendix C: AI inventory completeness statement

- **Total in-scope use cases identified**: [number]
- **Use cases not yet intaked but known to second line**: [number, with discovery channel]
- **Use cases newly identified through second-line scan, third-party diligence, or shadow-AI review**: [number]
- **Open MRAs or self-identified issues on inventory completeness**: [list]

---

## Sign-off block

The pack is a draft until the AI Governance Lead and the head of model risk review.

- **AI Governance Lead**: [role; sign-off date]
- **Head of model risk**: [role; sign-off date]
- **Committee chair acknowledgement**: [date once distributed]

Reviewer questions for the secretary to surface in the meeting, tagged to specific sections:

1. [Question tagged to the tier-mix movement]
2. [Question tagged to the foundation-model concentration]
3. [Question tagged to the over-age MRA or MRIA on AI scope]
4. [Question tagged to the GenAI gate exception]
5. [Question tagged to an agentic deployment or autonomy escalation]
