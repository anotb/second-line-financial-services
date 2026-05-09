# Banking sector overlay for agentic-ai-controls

When the engagement-scope record names `banking` as the sector, this overlay adds banking-specific authority-statement constraints, tool-inventory expectations, monitoring signals, regulator-notification triggers, and co-reviewer expectations.

Loaded by: `agentic-ai-controls/SKILL.md` when `engagement_scope.sector_overlay_set` includes `banking`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- 12 CFR Part 53 (OCC), 12 CFR Part 225 Subpart M (FRB), 12 CFR Part 304 Subpart C (FDIC) — banking computer-security incident notification rule (36-hour notification, effective May 2022).
- FFIEC IT Examination Handbook, Information Security and Architecture, Infrastructure, and Operations booklets, applied to the agent's serving environment.
- Joint OCC, FRB, and FDIC Interagency Guidance on Third-Party Relationships (June 2023) — OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023.
- The joint interagency Revised Guidance on Model Risk Management (OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026; supersedes SR 11-7 and SR 21-8) expressly excludes agentic AI from its scope (footnote 3); the agentic system is not within the bulletin. Where the bank's model risk programme treats the agent as a model by analogy, the principles inform but the binding hook is firm policy.
- NYDFS 23 NYCRR Part 500 for NY-licensed bank-affiliated entities; NYDFS October 2024 AI Industry Letter.
- BSA / AML expectations for AML-touching agent flows (FinCEN; FFIEC BSA/AML Examination Manual).
- CFPB UDAAP framings under 12 USC §§5531 and 5536 for consumer-financial-product flows.
- Reg E (12 CFR Part 1005) for electronic-funds-transfer flows touched by agents.
- Reg DD (12 CFR Part 1030) and Reg Z (12 CFR Part 1026) for deposit-disclosure and credit-disclosure flows touched by agents.

## Recurring banking agentic-AI use-case patterns

- **Customer-service representative (CSR) co-pilot**: agent assists CSR with summarisation, next-best-action suggestion, drafted communications, light actuation (temporary card lock, callback scheduling). Tool-use surface is moderate; consumer-protection seams are CFPB UDAAP and Reg E.
- **Servicing assistant**: agent reads account state and proposes routine servicing actions (address change, statement re-issue, fee inquiry). UDAAP and Reg DD/Z disclosure framings apply.
- **AML-investigation co-pilot**: agent reads transaction history, KYC records, news content; assists with case-narrative drafting, alert-disposition triage. BSA officer is a co-reviewer; SAR-quality and false-positive-rate are operational metrics.
- **Lending agent**: read tools on credit data; communication tools on customer-facing communications; proposed actuation on routine workflow steps. ECOA / Reg B and Fair Lending overlap; CFPB UDAAP overlap.
- **Fraud-response agent**: agent reads fraud-detection signals; agentic actuation in card-lock, transaction-hold, customer-outreach. Cyber overlay is structural; consumer-recourse posture matters.
- **Sponsor-bank operations agent for fintech-backed BaaS**: agent runs at the sponsor bank or at the fintech with read/write to the sponsor-bank's systems; shared-responsibility allocation is the load-bearing question (see payments-fintech overlay).

## Authority-statement constraints specific to banking

For consumer-facing banking agents the out-of-scope list at minimum includes: no funds movement; no permanent account closure; no fee imposition or fee waiver; no permanent card actions; no rate adjustments. These are non-optional and the controls review fails the section if the list is generic.

For AML-investigation co-pilots: no SAR filing, no SAR closing, no customer-notification on AML investigations (tipping-off prohibition under 31 CFR §1010.310).

## Tool-inventory expectations

- Per-customer query scoping at retrieval and at write tools; cross-customer access is a structural privacy and UDAAP risk.
- Funds-movement tools are not in the agent's inventory unless the use case explicitly requires it and the authority statement carries the matched in-scope action with reversibility framing.
- Communication tools (outbound email, SMS, in-app message) carry blast-radius framing in policy units (e.g., "could send up to N outbound communications per minute"); rate limits at the tool layer are non-optional.
- For AML-touching agents: no tool that posts to FinCEN, no tool that closes SAR cases, no tool that opens or closes monitoring rules.

## Human-oversight bar specific to banking

- For consumer-facing communications generated or assisted by the agent, block-and-wait CSR or supervisor review applies; UDAAP and Reg DD/Z disclosure expectations require human accuracy review.
- For AML alert disposition, block-and-wait analyst review is the default; post-hoc sampling on alert-disposition triage requires explicit BSA officer sign-off and sampling-rate evidence.
- For fraud-response actuation (card lock, transaction hold), notify-and-revocable is acceptable for tier-3 / tier-4 use cases; block-and-wait for tier-1 / tier-2.
- Sponsor-bank fintech BaaS: the human-oversight design names the responsible function on each side of the bank-fintech boundary; allocation is in the contract and the controls review surfaces gaps.

## Monitoring signals the overlay adds

- AML-touching agents: false-positive-rate change on alert disposition, SAR-quality drift, alert-volume drift, BSA-officer override rate.
- Consumer-facing agents: complaint-rate and complaint-code drift (UDAAP signal), customer-recourse channel volume.
- Funds-movement-adjacent agents: transaction-anomaly signals tied to the agent's actuation.
- Sponsor-bank BaaS: shared-monitoring posture per the contract.

## Incident-response and regulator-notification triggers

- 12 CFR Part 53 / Part 225 / Part 304 — 36-hour notification to primary federal regulator for "notification incidents" affecting banking services.
- NYDFS Part 500 §500.17(a) for NY-licensed entities; 72-hour notice on cybersecurity events meeting the rule's criteria.
- SEC 8-K Item 1.05 for public-registrant banking organisations.
- GLBA Safeguards Rule (16 CFR §314.5(d)) for FTC-scope non-bank financial institutions; less commonly applicable to bank-affiliated entities but loaded for non-bank affiliates.
- BSA-officer-led notification chains for AML-related events.

## Recommended-action items the overlay surfaces

- For AML-touching agents, BSA officer sign-off on the residual-risk acceptance.
- For consumer-facing agents, UDAAP risk-framing in the residual-risk view; complaint-rate baseline before go-live is non-optional.
- For sponsor-bank BaaS: the bank-fintech contract reflects the controls review's findings (notice rights, audit rights, off-switch ownership, IR-runbook integration).
- For agents touching the deposit, lending, or payments rails: the consumer-disclosure posture is mapped against Reg DD, Reg Z, Reg E.

## Common pitfalls specific to banking

- Treating the AML-investigation co-pilot as low-risk because the agent does not file SARs. The alert-disposition assistance shapes filing decisions; BSA officer involvement is non-optional.
- Omitting the consumer-disclosure framing on agents that generate or modify customer communications. Reg DD and Reg Z accuracy expectations apply to AI-assisted communications.
- Treating the 36-hour banking computer-security incident notification rule as out-of-scope because the event is "AI-related". A tool-misuse event that materially disrupts banking services is within scope of the rule regardless of the AI framing.
- Sponsor-bank BaaS: assuming the fintech's controls are sufficient. The sponsor bank is accountable; the controls review records the sponsor-bank-side coverage independently.
