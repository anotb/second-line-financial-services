# Conduct cross-cutting overlay for ai-act-triage

When the scope record flags `conduct` for the use case, this overlay adds conduct-risk content to the AI Act triage artifact. High-risk classification under Article 6 / Annex III frequently triggers conduct-risk considerations because the systems named in Annex III (creditworthiness, life and health insurance pricing, employment, essential public and private services) are precisely the systems that produce material customer outcomes. The triage records the conduct lens alongside the classification so the downstream conduct function inherits the work rather than duplicating it.

Loaded by: `ai-act-triage/SKILL.md` when `scope.cross_cutting_set` includes `conduct`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- EU AI Act Article 5(1)(a) and (b) on subliminal techniques and exploitation of vulnerabilities. The prohibitions overlap with consumer-protection and conduct-risk doctrine in member-state law (UCPD 2005/29/EC, national consumer-protection regimes).
- EU AI Act Article 50 transparency obligations. The synthetic-content marking and AI-interaction disclosure obligations are conduct-relevant where the AI surface reaches consumers, customers, or counterparties.
- EU AI Act Article 27 fundamental rights impact assessment. The FRIA includes elements (impact on affected persons, mitigation, governance, complaints handling) that align with conduct-risk taxonomy.
- FCA Senior Managers and Certification Regime (SMCR) for UK-licensed entities operating in or into the EU; the named-manager accountability extends to AI use cases inside in-scope firms.
- FCA Consumer Duty (PRIN 2A) for UK-authorised firms with EU customer overlap; the cross-border perimeter of Consumer Duty is itself a triage point.
- Member-state conduct frameworks (BaFin MaRisk AT 9 outsourcing and conduct expectations; ACPR conduct-supervision practice; Central Bank of Ireland Consumer Protection Code 2025) where the scope names a member state of operation.
- Firm-specific conduct framework lives in `references/firm-overlay.md` when present.

## What changes for conduct-flagged AI Act triages

### 1. Article 5 prohibited screen gains a manipulation and vulnerability lens

Article 5(1)(a) prohibits AI systems that deploy subliminal techniques beyond a person's consciousness or purposefully manipulative or deceptive techniques with the objective or effect of materially distorting behaviour. Article 5(1)(b) prohibits AI systems that exploit vulnerabilities of a person or specific group due to age, disability, or specific social or economic situation.

The conduct lens sharpens these prohibitions for financial-services use cases:

- A consumer-facing recommendation surface that uses behavioural-economics levers (loss-aversion framing, urgency cues, social-proof injection) at scale needs the Article 5(1)(a) screen on the record. Where the lever is purposefully designed to alter consumer behaviour against their interest, the screen is non-trivial.
- A vulnerability-aware customer-segmentation model that targets cohorts identified by age, disability, or specific social or economic situation needs the Article 5(1)(b) screen on the record. The screen is not automatic where vulnerability targeting is for protective purposes (vulnerable-customer support flows); the screen is sharp where the targeting is for revenue capture.
- The triage records the screen for both (1)(a) and (1)(b) as separate items even where the answer is "does not apply"; the screen running is the auditable evidence.

Article 5 reaches are legal interpretations. The triage records the screen and routes to legal for any close call.

### 2. High-risk classification surfaces the customer-outcome lens

Where the use case lands in Annex III(5)(b) creditworthiness, Annex III(5)(c) life and health insurance pricing, Annex III(4) employment, or Annex III(5)(a) essential public services, the customer-outcome lens is on the table by definition. The triage adds a conduct subsection that names:

- The customer cohort exposed to the decision (consumer credit applicant, life-insurance applicant, employee or candidate, benefits recipient).
- The customer-outcome distribution the system produces (decision distribution, price distribution, eligibility distribution) in vocabulary the conduct function uses.
- The customer-outcome disparity assessment scope (protected-class disparity per Annex III data-governance reach, plus policy-relevant cohort disparity per the firm's conduct framework).
- The customer-recourse path: how a consumer challenges a decision the system produced; how the firm handles complaints tied to the system; how complaints feed back to model change management.

This is not a substitute for the Article 27 FRIA where Article 27 applies. It is the conduct content the triage produces so the FRIA-vs-DPIA-vs-conduct-assessment reconciliation is on the record.

### 3. Article 50 transparency aligns to conduct-disclosure standards

For Article 50 sub-obligations that reach consumers (50(1) AI-interaction disclosure, 50(2) synthetic-content marking, 50(3) deepfake disclosure, 50(4) AI-generated text on matters of public interest), the disclosure language is a conduct artifact. The triage records:

- The current disclosure language posture (drafted / under legal review / in production).
- The owner of the disclosure language (typically client-facing function with legal review).
- The cadence of the language refresh (linked to vendor change-of-version triggers and to firm conduct-framework refresh cycles).
- The interaction with sector-specific disclosure regimes (Marketing Rule for US-side reuse of EU-deployed systems; PROD product-governance disclosures for UK-licensed firms; member-state advertising and pre-contractual disclosure regimes).

### 4. Article 27 FRIA aligns to conduct-risk assessment vocabulary

When Article 27 applies, the FRIA elements (impact on affected persons' rights, mitigation measures, governance arrangement, complaints-handling arrangement) align to conduct-risk-assessment vocabulary the firm already uses. The triage records the alignment so the FRIA author does not duplicate the conduct-risk assessment but consumes it. Conduct function as a named owner or reviewer on the FRIA when the scope flags conduct.

### 5. Sign-off names the conduct-accountable manager

For UK-licensed firms operating in or into the EU, the SMCR senior manager with allocated responsibility for the relevant prescribed responsibility is a named sign-off audience on the triage. For non-UK firms, the firm's conduct framework names a manager (often the head of the relevant business or the head of consumer / customer); the triage names the role, not the individual. The model owner is not by default the conduct-accountable manager; the triage is explicit about which is which.

### 6. Re-classification triggers gain conduct events

A complaint-rate breach on a system in scope of the triage, a regulatory engagement (member-state DPA inquiry, FCA Section 166 review, member-state conduct-supervisor inquiry), and a conduct-framework refresh that changes target-market or distribution scope are each re-classification triggers. The triage records the trigger list with conduct events named.

## Conduct-specific output template additions

The triage artifact adds the following blocks when this overlay loads:

- A conduct subsection inside the use-case-scope block naming customer cohort, customer-outcome distribution, customer-outcome disparity scope, and customer-recourse path.
- A sharpened Article 5(1)(a) and 5(1)(b) screen with the manipulation and vulnerability lens applied; recorded as separate items even where the answer is "does not apply".
- A disclosure-language posture entry under each Article 50 sub-obligation that fires.
- A FRIA-vs-conduct-assessment reconciliation note when Article 27 applies, with the conduct function as named owner or reviewer.
- A `conduct_accountable_manager_role` field naming the role under SMCR or the firm's conduct framework, distinct from the triage owner.
- Conduct-tagged re-classification triggers (complaint-rate breach, regulatory engagement, conduct-framework refresh).

## Common pitfalls in conduct-flagged AI Act triages

- Treating Article 5(1)(a) and (b) as a quick yes/no rather than as a screen with documented reasoning. Where a behavioural-economics lever or a vulnerability-aware segmentation is in the use case, the screen is substantive and routes to legal.
- Assuming a high-risk classification automatically satisfies the conduct lens. Annex III classification produces obligations under Articles 9 to 15 and Articles 26 to 27; the customer-outcome distribution and the customer-recourse path are conduct content the triage must surface separately.
- Conflating the FRIA with the conduct-risk assessment. They overlap; they are not the same. The reconciliation note tells the reviewer what each instrument carries.
- Treating the disclosure language as a legal artifact alone. Disclosure language is a conduct artifact; the conduct function owns the customer-comprehension assessment and the refresh cadence.
- Naming the model owner as the conduct-accountable manager when the firm's conduct framework names a different role. The two are separable and frequently are separated; the triage is explicit.
- Carrying enforcement-theme risk into the triage as a generic warning. Where the firm has a specific monitoring posture for a specific enforcement theme (CFPB-style adverse-action AI scrutiny in transatlantic-comparable practice; FCA Consumer Duty enforcement in UK reach), the triage records the firm posture; where it does not, the gap is recorded as a sign-off question.
