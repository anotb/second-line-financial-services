# Vendor diligence pack

**Vendor**: [legal entity; brand name if different]
**Service type**: [concise, e.g., cloud IaaS, foundation-model API, claims TPA]
**Arrangement ID**: [stable ID; reused across criticality-assessment, contract-gap-review, exit-plan]
**Engagement ID**: [pointer to engagement-scope record, or "none — scope not formalised"]
**As of**: [date]
**Review type**: [pre-onboarding | annual-recertification | off-cycle-trigger | exit-triggered-re-review | post-incident-re-review | scope-change-re-review]
**Owner (role)**: [e.g., third-party risk manager]
**Approver (role)**: [per firm policy for this criticality tier]
**Confidence label**: [high | medium | low | unknown]

## Service description and risk classification

- Business process and important business service supported.
- Customer-impact path; whether the vendor is on the IBS critical chain.
- Data scope (NPI, PHI, PCI, model prompts, model outputs, training data, etc.).
- Data locations and cross-border flows.
- Inherent risk summary (one paragraph).
- Criticality tier (sourced from `criticality-assessment`; do not re-set here): [not-critical | important | critical | unknown].

## Risk-based diligence summary

Where the diligence stands against the named criteria. Headline findings only; details below. Cite sources by file path (`references/source-anchors.md`) rather than restating excerpts here.

- Planning and risk assessment status.
- Due-diligence and selection status.
- Contract negotiation status (pointer to `contract-gap-review`).
- Ongoing monitoring posture.
- Termination and exit status (pointer to `exit-plan`).

## Operational resilience evidence

| Item | Vendor claim | Evidence status | Meets firm tolerance? | Notes |
|---|---|---|---|---|
| RTO | | sufficient / partial / missing | yes / no | |
| RPO | | sufficient / partial / missing | yes / no | |
| BCDR test scope | | sufficient / partial / missing | n/a | |
| Failover-region tabletop | | sufficient / partial / missing | n/a | |

Impact tolerance for the supported important business service: [from the firm's IBS map; not the vendor's claim].

## Cyber and information-security evidence

- SOC 2 Type II: [scope, period, exceptions, key CUECs].
- ISO/IEC 27001 certificate and Statement of Applicability: [scope, exclusions].
- Penetration-test summary: [date, findings status, remediation].
- Vulnerability-management evidence: [cadence, MTTR, exception register].
- Encryption posture: [in-transit, at-rest, key-management model].
- Identity and access: [SSO, SCIM, PAM, JIT].
- Logging and monitoring: [customer access, retention, SIEM integration].
- Incident-response: [severity taxonomy, customer-notification clock by severity].
- Status: `cyber_evidence_status = [sufficient | partial | missing | not-applicable]`.

## Privacy and data protection evidence

- GLBA Safeguards posture (where applicable).
- HIPAA business-associate posture (where PHI is in scope).
- State-privacy-law posture by state of customer footprint.
- Data-processing register, retention, sub-processor list, data-residency posture.
- Privacy-incident-response posture.
- Status: `privacy_evidence_status = [sufficient | partial | missing | not-applicable]`.

## Financial-condition evidence

- What was reviewed: audited financials / public filings / D&B / credit rating / runway disclosure (early-stage).
- Going-concern qualifier: [yes / no / not assessed].
- Status: `financial_condition_status = [sound | watch | concern | unknown]`.

## Concentration and sub-contractor footprint

- Subcontractors known.
- Subcontractor visibility: [full | partial | none].
- Concentration considerations raised: [hyperscaler region, sponsor-bank, BIN sponsor, claims TPA, foundation-model vendor, other].
- Status: `concentration_flag = [none | watch | breach]` — full analysis in `concentration-risk-review`.

## AI-specific findings

> Populate this section only when `ai_vendor = true`. Otherwise omit. The deeper question of "is this published evidence pack sufficient for our deployment context" chains to `llm-vendor-evidence-review` (in `ai-governance-model-risk`) via `eval_evidence_status = deferred-to-evidence-review` and the linked record ID.

- AI use case category: [foundation-model-api | ai-saas-product | embedded-ai-feature | agentic-system | rag-application | fine-tuned-model | specialised-classifier | other].
- Model provenance: [base / fine-tuned / RAG-augmented / agent-orchestrated; vendor-managed deprecation calendar].
- Training-data posture: [contractual commitment; abuse-monitoring exception; trust-and-safety modifications to defaults].
- Eval evidence status: [sufficient | partial | missing | deferred-to-evidence-review].
- Eval coverage on deployed system: [true | false] — base-model evals on vendor benchmarks do not count.
- Shared-responsibility clarity: [clear | partial | unclear].
- Fine-tune data isolation: [isolated | shared-tenant | not-applicable | unknown].
- Agent tool posture: [boundary, action-authorisation, audit-trail].
- System card fit to deployment: [fit | partial-fit | not-fit | no-system-card].
- Prompt-as-customer-data assessment: [NPI / PHI / PCI / other regulated data that prompts may carry; redaction posture if any; HIPAA BAA posture if applicable].
- Linked `llm-vendor-evidence-review` record: [ID].

## Contract gap summary

One-paragraph headline of contract-coverage findings. Pointer to `contract-gap-review` for the clause-by-clause analysis.

- Contract gap record: [ID].
- Headline gaps: [examiner-access clause; breach-notification clock; sub-processor change consent; model-version pin and deprecation notice (AI vendors); deposit-insurance representation (BaaS); Reg S-P clause set (advisers/BDs/funds); HIPAA BAA terms; etc.].

## Recommended onboarding decision and review gates

- **Recommended decision**: [approve | approve-with-conditions | defer | decline | escalate].
- **Conditions** (if approve-with-conditions): [bulleted, specific, verifiable].
- **Open evidence gaps**: [bulleted; what was asked, not received, by when].
- **Reviewer questions**: [bulleted; each question names the decision it supports].
- **Review gates this pack must clear**: [scope, evidence, authority, impact, decision].
- **Next-review trigger**: [annual cycle date; scope-change trigger; incident-driven re-review condition; for AI vendors, model-version-change trigger].
- The pack does not approve. The named approver decides.

## Source trace

| Claim | Source | Section | Date | URL or file ref |
|---|---|---|---|---|
| | | | | |

Cite `references/source-anchors.md` for canonical citations. Use `[verify section]` if the section reference is unknown; do not invent.

---

*Pack depth scales to vendor tier.* For a not-critical vendor, operational resilience and BCDR may collapse to a single paragraph, cyber may be a status line, the AI overlay may be a single applicability check. A critical vendor gets full depth with reviewer questions clustered for the relevant forums (TPRM, AI committee, risk committee, fund board where applicable).

*Audience shapes the pack.* A TPRM forum reads it differently from a risk committee or a fund board. Lead with the decision the audience must make.
