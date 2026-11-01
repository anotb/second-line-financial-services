# Second Line Financial Services

Claude skills for the people who check the work in regulated financial firms: compliance, risk, model risk, third-party risk, financial crime, and internal testing teams, plus the advisers who support them. Ask for the artifact you need, and Claude drafts it the way a second-line practitioner would, citing dated public sources and flagging what still needs evidence.

One plugin, 68 skills. Add it once and everything is available. Install nothing else.

## Try it

- Scope a second-line review of third-party onboarding at a mid-size US bank, including regulators, source posture, and overlays.
- Draft an issue write-up: quarterly user-access reviews on the wire system were missed in two of the last four quarters.
- Assess the impact of the 2024 Regulation S-P amendments on a mid-size registered investment adviser.
- Tier the risk of an internal GenAI assistant that summarizes commercial loan files for credit analysts.
- Draft an exit plan for replacing a sole-source KYC utility provider.
- Analyze these results and draft the workpaper conclusion: 3 of 25 sampled access reviews had no approver evidence.
- Draft a management response to a fictional MRA on stale customer-risk ratings, with milestones and an effectiveness plan.
- Design a second-line QA review of a sample of SAR no-file decisions.
- Review this marketing claim for UDAAP risk: "Get approved in minutes with no impact to your credit."
- Prepare a supervision-readiness pack for an upcoming OCC exam at a fictional USD 20B regional bank.

Each skill also runs directly as `/second-line-financial-services:<skill>`, such as `/second-line-financial-services:scoping`.

## Where to start

Start with `scoping` to set the institution, regulators, and source posture. Later skills read that scope record, and you can also call any skill by itself. Skills carry their own source anchors, templates, schemas, worked examples, and banking, insurance, capital-markets, and payments overlays, which load when relevant. The source base is deepest for the US, with EU overlays and UK see-also notes.

## Skills

### Core GRC

Guide: [`risk-compliance-core`](references/groups/risk-compliance-core.md)

| Skill | What it does |
|---|---|
| `control-matrix` | Build a risk-control matrix mapping obligations to control objectives, owners, frequency, and evidence. |
| `evidence-binder` | Assemble an evidence binder index for a regulatory exam, audit, validation, or vendor review. |
| `human-review-gates` | Design human-review gates for a workflow or AI output: triggers, reviewers, independence, sign-off. |
| `issue-writeup` | Write up a compliance or audit issue: condition, criteria, cause, effect, severity, remediation. |
| `obligation-mapping` | Map rules, guidance, or exam requests into a structured obligation register linked to owners and controls. |
| `policy-gap-review` | Review a firm policy or procedure against named regulatory benchmarks and report the gaps. |
| `scoping` | Scope a second-line review or engagement: institution, regulators, persona, source posture, overlays. |

### Regulatory change

Guide: [`regulatory-change-management`](references/groups/regulatory-change-management.md)

| Skill | What it does |
|---|---|
| `exam-brief` | Prepare a playbook for a live regulator exam or engagement: themes, requests, messaging, owners. |
| `implementation-plan` | Sequence regulatory change or remediation into a workplan with milestones, owners, dependencies. |
| `policy-diff` | Compare two versions of a firm policy and produce a section-by-section change log with impact. |
| `regulatory-impact-assessment` | Assess the impact of a new rule, bulletin, or supervisory letter on a financial firm. |
| `rule-to-obligation-extraction` | Break new regulatory rule text into atomic obligations for a compliance register. |

### AI governance and model risk

Guide: [`ai-governance-model-risk`](references/groups/ai-governance-model-risk.md)

| Skill | What it does |
|---|---|
| `agentic-ai-controls` | Review and propose controls for an agentic AI use case that calls tools or acts on systems. |
| `ai-act-triage` | Classify an AI use case under the EU AI Act and list the obligations that result from it. |
| `ai-risk-tiering` | Assign a defensible risk tier to an AI or model use case using a multi-factor rubric. |
| `ai-use-case-intake` | Turn an AI or model use case description into a structured governance intake record. |
| `board-ai-risk-pack` | Draft a board or committee AI risk pack: inventory, heat map, top risks, decisions. |
| `genai-pre-prod-review` | Run a pre-production gate review for a GenAI use case before release or material expansion. |
| `llm-vendor-evidence-review` | Review a foundation-model vendor's system cards, evals, and attestations for a regulated firm. |
| `model-card-builder` | Draft a model card for a financial-services AI or model: use, data, performance, limits. |
| `prompt-injection-risk` | Review prompt-injection exposure and controls for a GenAI use case at a regulated firm. |
| `rag-evaluation-review` | Review retrieval and grounding evaluation for a RAG-based GenAI use case at a regulated firm. |
| `validation-plan` | Draft an AI or model validation plan: scope, soundness, data, outcomes, and monitoring tests. |

### Third-party risk and resilience

Guide: [`third-party-operational-resilience`](references/groups/third-party-operational-resilience.md)

| Skill | What it does |
|---|---|
| `concentration-risk-review` | Assess third-party concentration across vendors, fourth parties, geographies, and services. |
| `contract-gap-review` | Review a vendor contract against regulatory clause expectations and report the gaps. |
| `criticality-assessment` | Set a third party's criticality tier and tie it to the firm's important business services. |
| `dora-register-builder` | Build EU DORA Register of Information entries for a firm's ICT third-party arrangements. |
| `exit-plan` | Draft an exit plan for a critical third-party arrangement: triggers, options, transition. |
| `resilience-testing-pack` | Draft an operational resilience testing pack with severe-but-plausible scenarios. |
| `vendor-diligence` | Draft a vendor due diligence pack for an ICT, fintech, cloud, data, or AI provider. |

### Compliance and controls testing

Guide: [`compliance-testing`](references/groups/compliance-testing.md)

| Skill | What it does |
|---|---|
| `control-sampling` | Design a control test sample: population, method, size, and selection rationale. |
| `evidence-request-builder` | Draft a provided-by-client (PBC) evidence request list for one control test cycle. |
| `exception-analysis` | Classify control-test exceptions into design, operating, and evidence failures, with severity. |
| `qa-workpaper` | Quality-review a completed control-test workpaper for scope, evidence, and conclusions. |
| `test-plan-builder` | Draft a compliance or controls test plan: scope, objective, criteria, population, procedures. |
| `workpaper-drafter` | Draft a testing workpaper from inspected evidence: criteria, procedures, results, conclusion. |

### Risk reporting

Guide: [`risk-reporting`](references/groups/risk-reporting.md)

| Skill | What it does |
|---|---|
| `attestation-pack` | Draft a management attestation pack: scope, controls, evidence, exceptions, assertion language. |
| `bcbs239-gap-assessment` | Assess risk data aggregation and reporting against the fourteen BCBS 239 principles. |
| `cyber-disclosure-readiness` | Prepare SEC cyber disclosure readiness: 8-K Item 1.05 materiality and 10-K Item 106. |
| `kri-commentary` | Draft second-line commentary on KRI and KCI movements and breaches for a risk report. |
| `management-response` | Draft a management response to an MRA, MRIA, or audit finding, with an action plan. |
| `risk-committee-pack` | Draft an enterprise risk committee pack: heat map, top risks, KRIs, issues, decisions. |

### Financial crime

Guide: [`financial-crime-governance`](references/groups/financial-crime-governance.md)

| Skill | What it does |
|---|---|
| `aml-model-monitoring` | Review ongoing monitoring evidence for an AML transaction-monitoring system or model. |
| `cdd-risk-review` | Quality-review a customer due diligence file against CDD pillars and exam expectations. |
| `edd-escalation-pack` | Draft an enhanced due diligence escalation pack for a higher-risk customer profile. |
| `negative-news-triage` | Triage adverse-media hits on a customer for identity confidence, reliability, and materiality. |
| `sanctions-screening-qa` | Quality-review a sanctions screening program: lists, configuration, tuning, alert handling. |
| `sar-decision-qa` | Quality-review a SAR or no-SAR decision file against SAR rules and FFIEC expectations. |

### Consumer compliance and fair lending

Guide: [`consumer-compliance-fair-lending`](references/groups/consumer-compliance-fair-lending.md)

| Skill | What it does |
|---|---|
| `adverse-action-review` | Review adverse-action notices and credit decisions for ECOA and Reg B compliance. |
| `complaint-theme-analysis` | Theme a population of consumer complaints and flag root causes and regulatory risk. |
| `fair-lending-test-plan` | Draft a fair-lending test plan across marketing, underwriting, pricing, and servicing. |
| `marketing-claim-review` | Review consumer-financial marketing claim by claim for substantiation and compliance risk. |
| `section1071-readiness` | Assess Section 1071 small-business lending data readiness under the CFPB's revised rule. |
| `udaap-risk-review` | Draft a UDAAP risk review of a product, fee, disclosure, marketing, or customer flow. |

### Banking

Guide: [`banking-risk-compliance`](references/groups/banking-risk-compliance.md)

| Skill | What it does |
|---|---|
| `bank-fintech-partnership-review` | Review a US bank-fintech partnership from the bank's supervisory and third-party-risk view. |
| `banking-supervision-readiness` | Prepare a US bank's supervision-readiness pack for an OCC, FRB, or FDIC examination. |
| `credit-risk-governance` | Draft a second-line credit risk governance pack for a bank's credit risk committee. |
| `deposit-operations-controls` | Draft a deposit-operations control matrix for a US bank: CIP, Reg E, Reg DD, escheat. |

### Capital markets and asset management

Guide: [`capital-markets-asset-management-compliance`](references/groups/capital-markets-asset-management-compliance.md)

| Skill | What it does |
|---|---|
| `adviser-exam-readiness` | Prepare an SEC or FINRA exam-readiness pack for an adviser, broker-dealer, or fund adviser. |
| `best-execution-surveillance` | Draft a periodic best-execution surveillance review for an adviser or broker-dealer. |
| `fund-board-reporting` | Assemble a periodic compliance and risk pack for the board of a registered fund. |
| `marketing-rule-evidence` | Build Marketing Rule 206(4)-1 evidence and substantiation for an adviser advertisement. |

### Insurance

Guide: [`insurance-risk-compliance`](references/groups/insurance-risk-compliance.md)

| Skill | What it does |
|---|---|
| `insurance-outsourcing-review` | Draft an oversight pack for insurance outsourcing or delegated authority: MGA, MGU, TPA. |
| `life-health-pricing-governance` | Review life or health pricing governance for a rate change or underwriting model. |

### Payments and fintech

Guide: [`payments-fintech-compliance`](references/groups/payments-fintech-compliance.md)

| Skill | What it does |
|---|---|
| `fintech-partner-controls` | Draft a fintech's controls evidence pack for a sponsor bank's third-party risk team. |
| `open-banking-data-controls` | Draft controls for consumer-permissioned data sharing under Section 1033 open banking. |
| `payment-operations-incident-review` | Draft an incident-review pack for a payments-operations event at a fintech or BaaS program. |
| `payments-risk-assessment` | Draft a payments risk assessment for a fintech, money transmitter, BaaS, or sponsor bank. |

## Install

From the directory: open **Customize > Plugins** in Claude and search for Second Line Financial Services, or run `/plugin directory` in Claude Code.

From GitHub, in Claude Code:

```
/plugin install second-line-financial-services --marketplace anotb/second-line-financial-services
```

If you installed one of the earlier separate plugins, such as `risk-reporting`, uninstall it and add this one. Skill names did not change.

## Data and behavior

The plugin is Markdown and JSON only: skills, references, schemas, and templates. It has no hooks, scripts, or MCP servers, and it does not send or store data itself. Documents you share are handled by Claude under your account's terms, so apply your firm's rules for confidential supervisory information, suspicious-activity material, and personal data before sharing them.

## Human review and AI disclosure

Intended for second-line and compliance professionals. Outputs are AI-assisted drafts. A qualified person with authority to change an output must review it before it is delivered or used in a decision, and stays accountable for it. Where an output supports advice to an individual or a decision about an individual, such as credit, insurance, employment, or legal rights, tell that individual AI was used to produce it. The plugin does not make credit, underwriting, claims, filing, or other final decisions, gives no personalized investment advice, and does not execute transactions or move money. It is not legal or regulatory advice.

## About

An independent project, not affiliated with or endorsed by Anthropic. MIT licensed. Source, issues, and roadmap are on [GitHub](https://github.com/anotb/second-line-financial-services).
