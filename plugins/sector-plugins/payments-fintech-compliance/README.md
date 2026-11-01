# Payments and Fintech Compliance

Sector overlay plugin for US payments firms, fintechs, money transmitters, sponsor-bank programs, BaaS providers, BIN sponsors, program managers, wallet operators, neobanks, and payments processors.

Audience: head of compliance, BSA officer, head of TPRM (sponsor-bank side), head of payment operations, head of risk, general counsel, and the advisory teams running the same work for those firms.

## Posture

This is a strict sector-overlay plugin. It ships skills that are genuinely payments-fintech-only, shaped by Reg E, Reg II, Reg DD, NACHA Operating Rules, the card-network rulebooks, FedNow and RTP procedures, FinCEN MSB rules, state Money Transmitter laws, the CFPB §1033 Personal Financial Data Rights Final Rule, the Interagency Guidance on Third-Party Relationships, and the OCC / FRB / FDIC joint statements on bank-fintech arrangements. Capability skills that already cover the underlying second-line function (vendor diligence, exit plan, concentration review, AML monitoring, sanctions screening QA, UDAAP review, exam brief, risk assessment, regulatory change management, AI governance, risk reporting) are not duplicated here. Payments-fintech nuance for those capability skills lives as a `references/sector-overlays/payments-fintech.md` reference inside each capability skill.

## Skills

| Skill | What it produces |
|---|---|
| `fintech-partner-controls` | Fintech-side control inventory and self-evidence pack for a sponsor-bank or BaaS arrangement: Reg E error-resolution timing, NACHA obligations the program operator owes upstream, MSB BSA posture where applicable, FBO-account mechanics, program-agreement oversight clause map, and the artifact list a sponsor-bank TPRM team will request. |
| `open-banking-data-controls` | Controls inventory and self-evidence pack for consumer-permissioned data sharing under the CFPB §1033 Personal Financial Data Rights Final Rule: data-provider duties (covered data, developer interface, authorization, revocation), data-recipient duties (collection, use, retention, deletion, reauthorization), and screen-scraping migration plan. |
| `payment-operations-incident-review` | Payments-incident review pack: chronology, customer-impact population, rail-by-rail Reg E / NACHA / card-network / FedNow / RTP notification triggers, sponsor-bank reporting log, root cause, remediation, and forward-control feed back to `fintech-partner-controls` and `payments-risk-assessment`. |
| `payments-risk-assessment` | Matrix-shaped risk assessment denominated by rail, customer segment, and geography: fraud, AML / sanctions, operational resilience, third-party / sponsor-bank dependence, customer-harm / UDAAP exposure, and reporting controls. Suitable for sponsor-bank annual review, state MTL exam preparation, internal audit kickoff, or enterprise risk committee read-out. |

## Try it

- Assess the risks of a fintech adding instant-payment send capability through a sponsor bank.
- Review a fictional payment-operations incident in which a duplicate ACH file was released.
- Review the controls for an open-banking data-sharing program under Section 1033.

## Payments overlays into capability skills

- `third-party-operational-resilience/vendor-diligence` — Interagency TPRM (June 2023), 2024 OCC / FRB / FDIC Joint Statement on Bank-Fintech Arrangements, NACHA Third-Party Sender posture, MSB / state MTL diligence, BIN-sponsor diligence, payments-specific fourth-party register.
- `third-party-operational-resilience/exit-plan` — payments-rail wind-down (ACH, Same Day ACH, wire, FedNow, RTP, card debit / credit, check, cross-border), sponsor-bank termination, in-flight-clock preservation across Reg E / NACHA / card / faster-payments, customer-transfer mechanics.
- `third-party-operational-resilience/concentration-risk-review` — three axes (sponsor-bank, processor, BIN-sponsor) plus geography overlay; cross-references `payments-risk-assessment` concentration views.
- `financial-crime-governance/aml-model-monitoring` — MSB BSA monitoring under FFIEC BSA / AML manual and FinCEN MSB rules (31 CFR Part 1022); payment-channel-specific scenario library; faster-payments-specific signals.
- `financial-crime-governance/sanctions-screening-qa` — cross-border corridor screening, correspondent-banking exposure, virtual-currency exposure (FinCEN guidance, Travel Rule under 31 CFR §1010.410(f)), vendor-tuning QA against OFAC Compliance Commitments.
- `consumer-compliance-fair-lending/udaap-risk-review` — fintech UDAAP themes including account-closure / hold practice, Reg E timing as a UDAAP signal, fee disclosure / junk-fee patterns, FDIC misrepresentation framing post-2024 joint statement, BNPL themes, dark-pattern risk, and the CFPB larger-participant rule for digital wallets and payment apps (December 2024).
- `regulatory-change-management/exam-brief` — three-track exam-prep posture: sponsor-bank-led review, CFPB direct supervision under the larger-participant rule, and state MTL exam via NMLS.

## Source posture

Public anchors only. Named anchors include:

- Reg E (12 CFR Part 1005), Reg DD (12 CFR Part 1030), Reg II (12 CFR Part 235), Reg Z (12 CFR Part 1026) where credit-side products are in scope.
- NACHA Operating Rules (current edition; paywalled, conceptual citation; specific sections to be confirmed against the firm's licensed copy).
- Card-network rules: Visa Core Rules, Visa Product and Service Rules, Mastercard Rules (current edition; paywalled, conceptual citation).
- FedNow Service Operating Procedures and RTP Operating Rules (current versions).
- State Money Transmitter laws under the Money Transmitter Modernization Act framework as adopted state-by-state via NMLS [verify state-by-state adoption status as of each review date]; Multistate MSB Licensing Agreement.
- CFPB Personal Financial Data Rights Final Rule under §1033 (October 2024) [verify Federal Register citation, effective date, implementation tiers, and current litigation status as of each review date].
- CFPB larger-participant rule for digital wallets and payment apps (December 2024) [verify Federal Register citation and current state including any litigation or congressional review].
- Interagency Guidance on Third-Party Relationships (OCC / FRB / FDIC, June 6 2023).
- OCC / FRB / FDIC Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services (July 25 2024) [verify exact date].
- FFIEC BSA / AML Examination Manual; FinCEN MSB rules at 31 CFR Part 1022; FinCEN administrative-ruling library (configuration-specific).
- OFAC Framework for Compliance Commitments (May 2019) and 31 CFR Part 501.
- GLBA Safeguards Rule (16 CFR Part 314); GLBA Privacy Rule (16 CFR Part 313 / Reg P at 12 CFR Part 1016).
- FFIEC Authentication and Access Guidance (August 2021); NIST SP 800-63B; OAuth 2.0 (RFC 6749) and FAPI 1.0 Final / current profile [verify].
- FDX API specification, current major version [verify version].
- FDIC misrepresentation rule (12 CFR Part 328 Subpart B, May 2022).
- NYDFS Part 500 (where covered); SEC cyber disclosure (Form 8-K Item 1.05) [verify citation specifics where the program operator or its sponsor is a public registrant].
- CFPB Circular series and CFPB Supervisory Highlights (current cycles).

The payments-fintech regulatory pipeline has been unusually active in 2023-2026 (Interagency TPRM Guidance, joint statements on bank-fintech arrangements, §1033 final rule with active litigation, larger-participant rule for digital wallets, state MTMA adoption proceeding state-by-state). Skills must be re-validated against current regulatory state before each major release; minimum annual refresh.

## Components

- `skills/` — the four skills above. Each ships its own `SKILL.md`, `references/source-anchors.md`, `templates/`, and (where useful) `schemas/` and `examples/`.
- `references/` — plugin-level shared references: payments source map, policy-control library rows, named decision forums.
- `schemas/` — payments-specific artifacts.

## Operating posture

The skills draft second-line work product for qualified review by the firm's Head of Compliance, BSA Officer, Head of TPRM at the sponsor bank, Head of Payment Operations, Head of Risk, General Counsel, or external counsel. They do not approve filings, file SARs, file regulatory reports, certify compliance programs, sign customer-facing notices, certify FBO subledger reconciliations, close issues, decline counterparties, or produce filed work product. Categorical money-transmitter-status assertions are out of scope; the right answer is configuration-specific against the FinCEN administrative-ruling library and the state-by-state MTL footprint, and a qualified human reviewer must make that call. Every output is staged for human sign-off.

## Install

In Claude Code:

```
/plugin install payments-fintech-compliance --marketplace anotb/second-line-financial-services
```

Pair with `regulatory-change-management`, `risk-compliance-core`, `risk-reporting`, `compliance-testing`, `financial-crime-governance`, `consumer-compliance-fair-lending`, `third-party-operational-resilience`, and `ai-governance-model-risk` for the full second-line stack.

This plugin works on its own. Mentions of `risk-compliance-core` in the skills are optional hand-offs. Add that plugin for the shared `scoping`, `control-matrix`, and `issue-writeup` skills; installing from the GitHub marketplace adds it automatically.

## Data and behavior

The plugin is Markdown and JSON only: skills, references, schemas, and templates. It has no hooks, scripts, or MCP servers, and it does not send or store data itself. `.mcp.example.json` is an inactive template that Claude does not load, and it connects to nothing until a firm replaces it with an approved server. Documents you share are handled by Claude under your account's terms, so apply your firm's rules for confidential supervisory information, suspicious-activity material, and personal data before sharing them.

## Human review and AI disclosure

Intended for second-line and compliance professionals. Outputs are AI-assisted drafts. A qualified person with authority to change an output must review it before it is delivered or used in a decision, and stays accountable for it. Where an output supports advice to an individual or a decision about an individual, such as credit, insurance, employment, or legal rights, tell that individual AI was used to produce it. The plugin does not make credit, underwriting, claims, filing, or other final decisions, gives no personalized investment advice, and does not execute transactions or move money. It is not legal or regulatory advice.
