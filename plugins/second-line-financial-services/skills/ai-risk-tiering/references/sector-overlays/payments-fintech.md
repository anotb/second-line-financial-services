# Payments and fintech sector overlay for ai-risk-tiering

When the scope record names sector `payments-fintech`, this overlay tells the tier rubric what is rail-, sponsor-bank-, and money-transmitter-specific. Tier names and cutoffs are firm policy; this overlay names which factors elevate, which gates trigger by default, and which re-tiering events to name.

Loaded by: `ai-risk-tiering/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`, or when the institution type implicates a money transmitter, payments processor, fintech program, sponsor-bank arrangement, BIN sponsor, prepaid issuer, or non-bank consumer-finance entity.

Source content derived from the payments-fintech lead's overlay snippets, mapped here into the tiering context. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023 (Interagency Guidance on Third-Party Relationships, June 6, 2023) for sponsor-bank programs.
- OCC / FRB / FDIC Joint Statement on Bank-Fintech Arrangements (July 25, 2024) [verify date and title] as the operative document for sponsor-bank deposit programs.
- FFIEC BSA/AML Examination Manual for transaction monitoring, sanctions screening, customer risk rating.
- FinCEN MSB rules at 31 CFR Part 1022 where the operator is itself a money transmitter.
- NACHA Operating Rules (current edition) Third-Party Sender registration and risk-management rules [verify rule citations].
- Reg E (12 CFR Part 1005), Reg DD (12 CFR Part 1030); CFPB UDAAP authority under Dodd-Frank Title X.
- NYDFS 23 NYCRR Part 504 (transaction monitoring) and Part 500 (cyber) for NY-licensed entities.
- CFPB Larger-Participant Rule for Digital Wallets and Payment Apps (December 2024) [verify Federal Register citation, effective date, and current state].

## Payments and fintech tier criteria

The use-case categories below are the most-frequent shapes; tier values remain firm policy.

### Onboarding-decisioning AI (KYC scoring, account-opening risk, identity-verification scoring)

- The model triages or scores onboarding outcomes; CIP and KYC integration is a downstream control, not a tier-down feature.
- Adverse-decisioning posture for ECOA reach where the onboarding implicates credit (card programs); for deposit-only programs, ECOA may not reach but UDAAP does.
- Default tier elevation: tier-1 or tier-2 for credit-implicating onboarding; tier-2 for deposit-only with UDAAP reach.

### Transaction-monitoring (TM) AI for AML/BSA

- The model triages or scores potentially suspicious activity; FFIEC manual exposure is operative; BSA officer or designee is a named approver.
- For NYDFS Part 504 covered entities, the senior-officer certification posture elevates the regulatory factor.
- For state-licensed money transmitters, state TM-program expectations layer on top of FFIEC manual.
- Default tier elevation: tier-1 for any TM model in scope; tier-2 minimum even where the rule reach is debated.

### Sanctions-screening AI

- OFAC compliance program structure is operative; corridor-by-corridor screening posture, fuzzy-matching threshold setting, and false-positive disposition QA are tier-side controls.
- Cross-border payments and correspondent flows elevate the regulatory factor; virtual-currency exposure layers FinCEN guidance on top.
- Default tier elevation: tier-1 in firm-policy-typical mappings.

### Fraud and ATO detection AI

- The model decides or scores fraud holds, declines, and step-up authentication.
- Reg E reach for unauthorised consumer transactions; the tier flags the consumer-recourse channel for false declines as a triggered control gate.
- For card programs, network rules apply in addition to regulatory expectations.
- Default tier elevation: tier-1 or tier-2 depending on autonomy and customer-impact directness.

### Consumer-facing GenAI (chatbots, support agents, dispute intake)

- The model interacts with customers in service, dispute, or sales surfaces; UDAAP reach is operative for any interaction that could be deceptive, unfair, or abusive.
- Reg E error-resolution timing applies if the bot intakes claims; the 10 / 45 / 90-day clock does not stop because intake is automated.
- Account-closure and account-hold themes (CFPB's most-frequent fintech UDAAP enforcement theme) elevate the conduct factor when the bot can effect or confirm account actions.
- Default tier elevation: tier-1 if the bot can take account-affecting actions; tier-2 advisory-only.

### Underwriting and pricing AI for non-bank consumer finance

- Where the use case influences credit-limit, APR, or approval/decline decisions outside a sponsor-bank context, the consumer-protection authority sits with the CFPB plus state regulators.
- ECOA / Reg B applies to the credit decision; Reg B §1002.9 and Comment 9(b)(2)-3 read directly on the adverse-action notice (CFPB Circulars 2022-03 / 2023-03 **withdrawn May 12, 2025; historical only**); conduct factor scores high.
- Default tier elevation: tier-1.

## Cross-cutting tier modifiers

- **Sponsor-bank arrangement**: where the AI sits in the program operator's stack but the regulated activity sits at the sponsor bank, the tier decision names the sponsor bank's federal banking regulator and the bank-side committee path. Vendor-dependence and concentration factors elevate. The bank-fintech contract allocates model-risk responsibility but the bank inherits the model risk under the June 2023 interagency guidance.
- **State money-transmitter footprint**: state-by-state MTL exam expectations elevate the regulatory factor; the strictest state in the footprint sets the floor for licensure-tied gates.
- **NYDFS Part 504 covered entity**: senior-officer certification posture for TM models is a triggered gate; the regulatory factor scores high for any TM, sanctions-screening, or KYC use case.
- **CFPB larger-participant rule for digital consumer payment applications** (12 CFR Part 1090, finalized November 21, 2024) — verify current operative status on the engagement date (CFPB has been reconsidering and litigating multiple late-2024 final rules); where in scope and operative, the entity is under direct CFPB supervisory authority and the regulatory factor elevates for any consumer-facing AI.
- **Concentration risk on sponsor-bank, processor, BIN sponsor**: three distinct concentration axes; each fails differently. The concentration factor scores against the dominant axis for the use case.
- **Faster-payments rails (FedNow, RTP, Same Day ACH inbound)**: irrevocability shifts the fraud-control playbook; the conduct factor reads against request-for-return-of-funds dynamics rather than chargeback paths.

## Payments-fintech-specific tier-elevation factors

In addition to the capability rubric:

- Sponsor-bank arrangement → vendor-dependence and concentration factors elevate; bank-side committee path named.
- TM, sanctions-screening, or KYC use case → regulatory factor high (FFIEC manual exposure named); BSA officer signoff as triggered gate.
- NYDFS Part 504 senior-officer certification posture → regulatory factor high.
- CFPB Larger-Participant Rule in scope → regulatory factor elevated for consumer-facing AI.
- Reg E reach on consumer-facing AI that intakes claims or affects transactions → conduct factor at minimum medium.
- FDIC misrepresentation rule (12 CFR Part 328 Subpart B; **2023 final rule with 2024-2025 effective-date extensions** — verify current effective date for the engagement): any "FDIC-insured" framing on a fintech surface elevates the conduct factor and triggers a customer-disclosure control gate.

## Payments-fintech-specific re-tiering triggers

Add to the re-tiering trigger block for payments-fintech sector use cases:

- Sponsor-bank change (new sponsor, dual-sponsor add, sponsor exit). Owner: program operations with bank's third-party risk function. Detection: program-agreement change-control plus bank-side notification.
- Rail expansion (adding FedNow, RTP, Same Day ACH, cross-border corridor). Owner: payments operations. Detection: change-management notice.
- New state MTL or BitLicense in the operating footprint. Owner: licensing function. Detection: NMLS filing plus regulatory horizon scan.
- CFPB Larger-Participant Rule applicability change (volume threshold crossing). Owner: regulatory change function with CCO. Detection: volume monitoring plus annual self-assessment.
- NYDFS Part 504 senior-officer certification cycle. Owner: BSA officer with CCO. Detection: annual certification calendar.
- Material change in NACHA Third-Party Sender posture, Visa / Mastercard fraud-rate program escalation, or processor change. Owner: payments operations with vendor management. Detection: rule-change notice plus return-rate / fraud-rate monitoring.

## Common pitfalls in payments-fintech tiering

- Treating the fintech as the sole owner of model risk when a sponsor-bank arrangement is operative; the bank inherits the model risk wholesale and the tier should reflect bank-side reach.
- Omitting BSA officer signoff on a TM model; FFIEC manual expectation is clear and the gate should fire at tier decision, not at validation hand-off.
- Reporting fraud-model performance as AML-effectiveness evidence; the two are doctrinally distinct and conflating them at tier-decision time hides the real exposure.
- Missing Reg E error-resolution posture on a chatbot or support-agent AI that intakes claims or confirms account actions; the 10 / 45 / 90-day clock applies regardless of who or what intakes the claim.
- Treating state money-transmission exams as a footnote; state examiners regularly review TM and onboarding models in money-transmission exams and the regulatory factor should reflect that.
- Underweighting concentration risk on sponsor-bank, processor, or BIN-sponsor axis; the three axes fail differently and a single concentration metric hides the failure mode.
- Treating "FDIC-insured" framing on a fintech surface as a marketing question; under the FDIC misrepresentation rule the framing is a regulatory-factor input and the tier should reflect the disclosure gate.
- Missing the irrevocability shift on faster-payments rails; the fraud playbook is request-for-return-of-funds plus monitoring escalation, not chargeback, and the conduct factor reads differently.
