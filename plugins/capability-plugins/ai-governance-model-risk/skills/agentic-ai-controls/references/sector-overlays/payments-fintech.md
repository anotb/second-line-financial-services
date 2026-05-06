# Payments and fintech sector overlay for agentic-ai-controls

When the engagement-scope record names `payments-fintech` as the sector, this overlay adds payments-and-fintech-specific authority-statement constraints, tool-inventory expectations, monitoring signals, regulator-notification triggers, and co-reviewer expectations. The most distinctive issue in this sector is the bank-fintech shared-responsibility allocation in BaaS arrangements.

Loaded by: `agentic-ai-controls/SKILL.md` when `engagement_scope.sector_overlay_set` includes `payments-fintech`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- Joint OCC, FRB, and FDIC Interagency Guidance on Third-Party Relationships (June 2023) — OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023, applied to bank-fintech relationships.
- 12 CFR Part 53 / Part 225 / Part 304 — banking computer-security incident notification rule, applies to bank service providers.
- CFPB UDAAP framings under 12 USC §§5531 and 5536 for consumer-facing actuation.
- State money-transmitter licensing regimes (per state); the Conference of State Bank Supervisors (CSBS) Money Services Business Model Law where adopted.
- Reg E (12 CFR Part 1005) for electronic-funds-transfer flows.
- BSA / AML expectations: FinCEN regulations, FFIEC BSA/AML Examination Manual.
- Card-network rules (Visa, Mastercard, Amex, Discover) for payment-card flows.
- NYDFS 23 NYCRR Part 500 and 23 NYCRR Part 200 (virtual currency) where applicable.
- GLBA Safeguards Rule (16 CFR Part 314) for FTC-scope non-bank entities.

## Recurring payments-fintech agentic-AI use-case patterns

- **Onboarding / KYC agent**: agent reads identity documents, verification signals, sanctions-screening results; assists with onboarding decisions, EDD triage, document-classification.
- **Transaction-monitoring agent**: agent reads transaction streams; assists with alert disposition, narrative drafting, escalation triage. BSA officer is a co-reviewer.
- **Customer-support agent for fintech consumer flows**: agent reads account state, transaction history; assists with dispute initiation, refund processing within thresholds, communication drafting. CFPB UDAAP and Reg E reach.
- **Sponsor-bank operations agent for BaaS**: agent runs at sponsor bank or at fintech with read/write to sponsor-bank systems; shared-responsibility allocation is the structural question.
- **Fraud-response agent**: agent reads fraud signals; agentic actuation in transaction blocks, customer outreach, dispute initiation.
- **Acquiring agent for merchant flows**: agent reads merchant-onboarding data; assists with merchant-risk decisions; card-network rules apply.

## Authority-statement constraints specific to payments-fintech

The out-of-scope list at minimum includes: no funds movement outside firm-policy thresholds; no account-status changes that affect customer-money-access (freezes, holds, closures) without supervisor approval; no merchant-status changes without underwriter approval (for acquiring agents); no card-network-rule-violating actions.

For BaaS sponsor-bank flows: the out-of-scope list is bounded by the bank-fintech contract. Agents at the fintech do not actuate sponsor-bank systems outside the contractual envelope; agents at the sponsor bank do not actuate fintech-customer systems outside the same envelope.

## Tool-inventory expectations

- Per-customer query scoping; cross-customer access is a structural privacy and UDAAP risk.
- Funds-movement tools are not in the agent's inventory unless explicitly authorised; if present, blast-radius framing is required ("could move up to $X per minute").
- Communication tools: blast-radius framing; CFPB UDAAP and Reg E preservation reach.
- Card-network-touching tools (chargebacks, retrievals, dispute lifecycle): card-network-rule-aligned scoping.
- BaaS-shared tools: the bank-fintech contract names the tool inventory each side controls; the controls review reflects this allocation.

## Human-oversight bar specific to payments-fintech

- For onboarding decisions: notify-and-revocable is acceptable for low-risk segments; block-and-wait for high-risk segments and EDD-triggered cases.
- For transaction-monitoring alert closure: block-and-wait analyst review per BSA officer policy.
- For customer-facing communication generation: block-and-wait or notify-and-revocable per UDAAP risk; CFPB UDAAP scrutiny applies.
- For BaaS shared flows: the human-oversight design names the responsible function on each side of the bank-fintech boundary; allocation is in the contract.

## Monitoring signals the overlay adds

- Onboarding agents: KYC-decision distribution, sanctions-hit handling cadence, EDD-triage rate.
- Transaction-monitoring agents: false-positive-rate, alert-closure-rate, alert-reopen-rate, BSA officer override rate.
- Customer-support agents: complaint-rate (UDAAP signal), Reg E dispute-handling timing compliance.
- Fraud-response agents: false-positive customer-block rate, customer-recourse channel volume.
- Acquiring agents: merchant-risk decision distribution, chargeback-rate by merchant cohort.
- BaaS shared signals: per the contract; both sides monitor.

## Incident-response and regulator-notification triggers

- 12 CFR Part 53 / Part 225 / Part 304 — for bank service providers and bank-affiliated entities, 36-hour notification.
- NYDFS Part 500 §500.17(a) — for NY-licensed entities.
- SEC 8-K Item 1.05 — for public registrants.
- GLBA Safeguards Rule (16 CFR §314.5(d)) — for FTC-scope non-bank entities.
- State money-transmitter regulator notification — per state.
- BaaS sponsor-bank notification chain runs first; sponsor bank then runs the federal regulator chain.
- Card-network breach-notification chains where card-network rules apply.

## Recommended-action items the overlay surfaces

- For BaaS arrangements, the bank-fintech contract reflects the controls review's findings (notice rights, audit rights, off-switch ownership, IR-runbook integration, monitoring data sharing).
- For state money-transmitter-licensed entities, the controls review references the per-state licensing footprint and the most-prescriptive state's expectations.
- For BSA/AML-touching agents, BSA officer sign-off on the residual-risk acceptance.
- For consumer-facing agents, UDAAP risk-framing in the residual-risk view; complaint-rate baseline before go-live is non-optional.
- For card-network-touching agents, card-network-rule alignment is recorded in source trace.

## Common pitfalls specific to payments-fintech

- BaaS sponsor-bank: assuming the fintech's controls are sufficient. The sponsor bank is accountable under the interagency third-party guidance; the controls review records the sponsor-bank-side coverage independently of the fintech's own coverage.
- Treating onboarding agents as out-of-scope of BSA/AML. KYC-decision assistance shapes onboarding outcomes; FinCEN expectations apply to the firm's overall KYC program.
- Omitting state money-transmitter licensing footprint from the authority statement. State patchwork is the firm's responsibility to maintain; the agent's geographic scope reflects it.
- Treating the 36-hour banking notification rule as out-of-scope because the firm is a fintech. If the firm is a bank service provider, the rule's bank-service-provider obligations apply.
- Designing post-hoc sampling oversight on transaction-monitoring alert closure. Block-and-wait analyst review is the BSA-officer-policy norm; deviations require explicit BSA officer sign-off and sampling-rate evidence.
