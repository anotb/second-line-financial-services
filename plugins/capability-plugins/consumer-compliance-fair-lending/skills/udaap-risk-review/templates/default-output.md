# UDAAP risk review memo

> Status: draft until the named decision forum acts. The memo surfaces UDAAP risk for human decision; it does not finalize a UDAAP determination, take down a live product, execute consumer redress, or issue any customer-facing action.

## 1. Scope

| Field | Value |
|---|---|
| Review ID | `[review_id]` |
| As of date | `[YYYY-MM-DD]` |
| Trigger | `pre-launch-gate` / `complaint-theme-trigger` / `regulator-inquiry` / `peer-enforcement-action` / `post-incident-review` / `annual-refresh` / `model-deployment-trigger` / `self-identified-issue` / `other` |
| In-scope subject | `[product / feature / fee / disclosure / flow / marketing motion / complaint pattern / enforcement-theme parallel]` |
| Subject type | `product` / `feature` / `fee` / `disclosure` / `customer-experience-flow` / `marketing-motion` / `complaint-pattern` / `enforcement-theme-parallel` / `policy-or-procedure` / `other` |
| Period | `[start] to [end]` |
| Channels | `[branch, digital, broker, marketplace, partner-of-record, sponsor-bank-program-operator]` |
| Population | `[description with sourcing]` |
| Sector overlay set | `[banking / payments-fintech / capital-markets / insurance]` |
| Cross-cutting overlay set | `conduct (mandatory)` `+ privacy (where loaded)` |
| Source posture | `public-only` / `public-plus-firm-policy` / `public-plus-firm-policy-plus-evidence` / `connector-aware` |
| Exclusions | `[explicit out-of-scope items]` |

## 2. Reviewer and review posture

- Reviewer role: `[independent second-line / embedded 1.5-line / advisory engagement / joint with program bank]`
- Review independence: `independent-second-line` / `embedded-1-5-line` / `advisory` / `joint-with-program-bank` / `other`
- Counsel directing: `[yes / no]`
- Legal privilege posture: `attorney-client-privileged` / `attorney-work-product` / `dual-purpose-business-and-privileged` / `not-privileged` / `posture-pending-counsel`

## 3. Evidence base

| Source | Type | Date | Completeness |
|---|---|---|---|
| | regulatory-anchor / supervisory-highlights-issue / enforcement-action / complaint-data / transaction-data / call-recording / marketing-asset / policy-text / training-record / system-output-log / model-card / vendor-documentation / firm-internal-memo / other | | complete / partial / missing / unknown |

## 4. Element-by-element analysis

### 4.a Deception

- Representation or omission: `[describe with consumer-journey context]`
- Likely to mislead: `yes` / `no` / `indeterminate`
- Reasonable-consumer basis: `[reasoning]`
- Materiality: `material` / `not-material` / `indeterminate`
- Materiality rationale: `[reasoning]`
- Evidence pointers: `[file paths or evidence-base entries]`

### 4.b Unfairness

- Substantial injury:
  - Injury type: `[describe]`
  - Magnitude per consumer: `[dollar value or quantified harm]`
  - Magnitude aggregate: `[dollar value over period]`
  - Population estimate: `[number with sourcing]` `[evidence-needed if not yet evidenced]`
- Reasonably avoidable: `yes` / `no` / `indeterminate`
- Reasonably-avoidable analysis: `[was the consumer able to anticipate the injury, take reasonable steps to avoid it, and did the firm structure the choice to permit avoidance]`
- Countervailing benefits:
  - First-line assertion: `[as represented by product or business owner]`
  - Reviewer assessment: `[independent second-line read]`
  - Outweighs injury: `yes` / `no` / `indeterminate`
- Evidence pointers: `[file paths or evidence-base entries]`

### 4.c Abusiveness

- Applicability: `applicable` / `not-applicable` / `indeterminate`
- Applicability rationale: `[reasoning; mandatory if not-applicable]`
- Material interference:
  - Description: `[describe]`
  - Evidence: `[file paths or evidence-base entries]`
- Unreasonable advantage:
  - Type: `lack-of-understanding` / `inability-to-protect-interests` / `reasonable-reliance` / `n-a`
  - Evidence: `[file paths or evidence-base entries]`

## 5. Consumer-harm hypothesis

- Population: `[description with sourcing]`
- Population evidence flag: `evidenced` / `evidence-needed` / `indeterminate`
- Magnitude: `[per-consumer and aggregate]`
- Frequency: `one-time` / `recurring` / `repeated` / `indeterminate`
- Redress posture: `[plausible scale and population subset]`

## 6. AI / algorithmic-discrimination tie-in

(Populate when any AI / ML / complex algorithm is in the in-scope flow.)

- AI in path: `[yes / no]`
- Model inventory:

| Model ID | Version | Decision use | AI/ML | Vendor or in-house | Validation status | Card reference |
|---|---|---|---|---|---|---|
| | | marketing-targeting / personalised-pricing / retention-offer / AI-generated-communication / conversational-AI / fraud-deny / agentic-flow | true/false | vendor / in-house / vendor-fine-tuned / unknown | validated / in-validation / not-validated / unknown | |

- UDAAP theory on the algorithmic outcome: `[which prong applies; reasoning]`
- April 2023 Joint Statement cited: `[yes / no]`
- Fair-lending cross-reference: `[yes / no; if yes, also chain to fair-lending-test-plan]`

## 7. Severity rating

| Element | Severity | Rationale |
|---|---|---|
| Deception | low / medium / high / critical / n-a | |
| Unfairness | low / medium / high / critical / n-a | |
| Abusiveness | low / medium / high / critical / n-a | |
| Aggregate | low / medium / high / critical | |

Severity rubric reference: SKILL.md Severity rating section.

## 8. Conduct-risk implications

- Taxonomy tie-back: `incentives` / `product-design` / `communication` / `sales-practices` / `customer-outcome` / `complaint-linkage` / `vendor-or-third-party` / `ai-algorithmic-surface` / `other` (one or more)
- Conduct-accountable manager role: `[role under SMCR or the firm's conduct framework]`
- Conduct committee read: `[yes / no]`
- Conduct-event candidate: `[yes / no]`
- Customer-outcome segments affected: `[list policy-relevant segments]`
- Regulator-engagement trigger: `[event if any]`
- Complaint-monitoring loop closure: `[post-remediation monitoring posture]`

## 9. Recommended remediation

| Action | Type | Owner | Due date | Accountable forum |
|---|---|---|---|---|
| | consumer-redress / control-change / policy-change / disclosure-change / training / kill-switch-candidate / marketing-takedown-candidate / model-change-candidate / vendor-renegotiation / monitoring-uplift / other | | YYYY-MM-DD | product committee / conduct committee / fair-lending committee / counsel / CCO |

## 10. Open legal questions

- `[items deferred to counsel]`

## 11. Cross-references

- `complaint-theme-analysis` `[where complaint signal feeds the memo]`
- `marketing-claim-review` `[where asset-level marketing review applies]`
- `adverse-action-review` `[where AAN content overlaps]`
- `fair-lending-test-plan` `[where parallel ECOA / FHA theory applies]`
- `vendor-diligence` `[where third-party vendor is in path]`
- `model-card-builder` / `llm-vendor-evidence-review` `[where AI model is in path]`

## 12. Source trace and confidence

| Claim | Source | Section | Date | URL or file path |
|---|---|---|---|---|
| | | | | |

- Confidence label: `high` / `medium` / `low` / `unknown`
- Assumptions and dependencies: `[list]`

## Decision forum

- Named forum: `[product committee / conduct committee / fair-lending committee / counsel / CCO]`
- Decision status: `draft` / `submitted` / `in-review` / `decided` / `deferred` / `rejected`
- Decision date: `[YYYY-MM-DD]`
- Conditions: `[where applicable]`
