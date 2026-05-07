# Insurance sector overlay for complaint-theme-analysis

When the engagement-scope record names sector `insurance`, this overlay flags the scope boundary, names the analogous regime, and adapts the theme-analysis pattern for state-DOI complaint surfaces and MGA program complaints. Insurance complaint-handling sits outside the CFPB's jurisdiction; the theme-analysis method is reusable but the regulatory exposure mapping shifts entirely to state insurance departments and the NAIC framework.

Loaded by: `complaint-theme-analysis/SKILL.md` when `engagement_scope.sector_overlay_set` includes `insurance`, or when the institution type implicates a property and casualty insurer, life insurer, health insurer (in the consumer-finance scope where applicable), MGA / MGU, or insurance-licensed bank affiliate.

Cited and section-referenced anchors live in `references/source-anchors.md`.

## Scope boundary first

Insurance complaint-handling sits with state insurance departments under the NAIC Unfair Trade Practices Act framework (Model #880) and the NAIC Unfair Claims Settlement Practices Act framework (Model #900). The vocabulary differs: "unfair discrimination" between similarly-situated risks; "unfair claims settlement practices"; the substantive standards differ from the federal consumer-protection framework. State DOIs operate consumer complaint portals analogous to the CFPB Complaint Database; the NAIC Complaints Database (CDS) aggregates a subset of state complaint data.

The overlay is named so reviewers do not over-extend the CFPB framing into insurance underwriting, pricing, or claims handling. It is also named so reviewers can run the same theme-analysis discipline (taxonomy, coding, trend, severity, root-cause hypothesis, recommended action) on insurance complaints under the state-DOI framework.

The narrow exception is bank-affiliated credit-protection insurance bundled with a credit product, where the credit-side complaint theming runs under the consumer-finance framework and the insurance-side runs under the state-DOI framework; the memo carries both reads where the theme spans both surfaces.

## What the theme-analysis method looks like under the state-DOI / NAIC framework

### 1. Recurring insurance complaint themes

A non-exhaustive theme catalogue (the categories vary by line):

- *Underwriting themes.* Application-decision themes (denial reasons; rate-class themes; coverage-exclusion themes); rating-factor themes (the use of credit-based insurance score; the use of telematics or usage-based-insurance variables; the use of catastrophe modeling at the territory level); accelerated-underwriting themes for life insurance.
- *Claims-handling themes.* Claim-denial themes (reasonability of denial; claims-investigation conduct); claim-delay themes (failure to acknowledge, investigate, or pay within the prompt-payment statutes); claim-settlement-amount themes (low-ball offer pattern; depreciation-application themes; replacement-cost-vs-actual-cash-value); subrogation themes; coverage-interpretation themes (the policy-language dispute pattern).
- *Premium and billing themes.* Premium-increase themes (rate filing intersection); cancellation and non-renewal themes (statutory notice requirements; reason-for-cancellation themes); refund-handling themes; lender-placed insurance themes (where the insurance is placed by the credit lender; cross-references the banking sector overlay).
- *Marketing and producer-conduct themes.* Producer-misrepresentation themes; needs-analysis themes (annuity sales suitability); replacement-of-existing-coverage themes; producer-licensing themes.
- *AI / algorithmic-decisioning themes.* Themes that touch automated underwriting, automated claims-decisioning, AI-driven pricing, or generative-AI-driven communication; the NAIC Model Bulletin on AI (December 2023) [verify exact title and adoption status by state] is the operative cross-state framing.

### 2. NAIC framework regulatory exposure mapping

For insurance themes, the regulatory exposure cites:

- NAIC Unfair Trade Practices Act (Model #880) section as adopted by the operative state(s).
- NAIC Unfair Claims Settlement Practices Act (Model #900) section as adopted by the operative state(s).
- State-specific market-conduct examination procedures.
- Line-specific regulatory framework (NAIC Annuity Suitability Model #275 and the best-interest amendments; NAIC Life Insurance Illustrations Model #582; etc.).
- For credit-based insurance scoring, the NAIC Credit-Based Insurance Score model and the state-specific filing posture.
- For the AI / algorithmic surfaces, the NAIC AI Model Bulletin (December 2023) and any state-adopted bulletin variants [verify per state].

The memo cites the operative state's adoption of the relevant NAIC model rather than citing the model alone, because adoption varies by state.

### 3. State-DOI complaint portals and the NAIC CDS

Insurance complaint surveillance pulls from:

- State-DOI consumer complaint portals (each operative state).
- The NAIC Complaints Database (CDS) for the firm's complaint history and for peer comparison (where the firm is in CDS reporting scope).
- The firm's internal complaint records (call center, web form, broker channel, claims-team escalation).
- Producer-channel complaint records (where complaints route through the producer rather than direct to the carrier).

The memo names the channels reviewed; the firm-direct channel typically dwarfs the state-DOI channel by volume but the state-DOI channel carries weight because it is the regulator's own surveillance signal.

### 4. MGA / MGU and program-business attribution

Where the firm operates through MGAs (managing general agents), MGUs (managing general underwriters), or program-business arrangements, the complaint-handling responsibility is allocated by the program agreement and the carrier's reinsurance posture. The memo records, per theme:

- Which entity holds the consumer-facing relationship (typically the MGA on the agent-side and the carrier on the policyholder relationship).
- Which entity owns the underwriting, pricing, or claims decision that the theme traces to.
- Which entity holds the ultimate coverage liability (the carrier; sometimes a reinsurer with cut-through).
- Joint-review framing where the theme runs through both the MGA and the carrier.

### 5. Customer-outcome themes vs. unfair-discrimination themes

The state-DOI framework's "unfair discrimination" vocabulary is narrower than the federal framework's protected-class-disparate-impact vocabulary. Unfair discrimination in insurance generally refers to differential treatment among similarly-situated risks not justified by actuarial or other objective considerations; it is not coterminous with the disparate-impact framework. The memo is explicit about which framework is doing the analytical work; the customer-outcome lens (carried by the conduct overlay) extends the analysis where the policy-relevant segment lens supplements the actuarial-justification lens.

For lines where the federal framework also applies (credit insurance bundled with a federally-regulated credit product; ERISA-governed health insurance for the §1557 nondiscrimination angle), the memo cites both frameworks.

### 6. Credit-protection insurance bundled with credit (the narrow CFPB intersection)

Where the in-scope theme involves credit-protection insurance bundled with a credit product (GAP, credit life, credit disability, credit unemployment, debt cancellation), the credit-side complaint theme runs under the consumer-finance framework (the bundling mechanic; the disclosure timing relative to closing; the cancellation-and-refund mechanic; the value-of-coverage-vs-cost analysis), and the insurance-side complaint theme runs under the state-DOI framework. The memo carries both reads. Cross-skill chain into `udaap-risk-review` for the credit-side bundling mechanic; the insurance-side stays in this overlay.

### 7. AI / algorithmic surfaces in insurance

Insurance carriers deploy AI / ML in automated underwriting, accelerated underwriting, claims-decisioning, fraud-deny decisioning, customer-service voice agents, and policy-language summarisation. Themes that touch these surfaces carry `ai_flag: true`. The NAIC Model Bulletin on AI (December 2023) [verify] is the operative cross-state framing; state adoption varies. The memo cites the model bulletin and the state-specific adoption posture.

The April 2023 Joint Statement applies in spirit (the four federal agencies' framing on automated systems extends to insurance where federal authorities reach, though the EEOC, FTC, and CFPB are not the operating regulators on most insurance themes); the memo names the federal framing where the theme touches a federally-regulated decision.

## Insurance-specific theme matrix additions

Per theme:

- `state_doi_complaint_count` — count of complaints in the operative state-DOI portal(s) for this theme.
- `naic_cds_count` — count of complaints in the NAIC Complaints Database for this theme (where firm is in CDS scope).
- `naic_model_intersection` — list of NAIC models that the theme touches (Model #880; Model #900; Model #275; etc.).
- `state_adoption_status` — for each NAIC model cited, the operative state's adoption status.
- `mga_program_attribution` — `carrier-of-record` / `mga-of-record` / `joint` / `under-program-agreement-allocation`.
- `bundled_with_credit` — boolean; if true, the credit-side cross-skill chain into `udaap-risk-review` is named.

## Common pitfalls in insurance complaint-theme analysis

- Applying CFPB UDAAP framing to insurance underwriting, pricing, or claims-handling themes. The substantive regime is state-DOI under the NAIC framework; the federal authorities do not reach most insurance themes.
- Citing the NAIC model without naming the operative state's adoption status. NAIC models are guides; only state adoption is binding.
- Treating insurance "unfair discrimination" as equivalent to federal disparate-impact. The vocabulary and the substantive standards differ; the memo is explicit about which lens is operating.
- Missing the MGA / program-business attribution question. Program-business arrangements allocate the complaint-handling duty between MGA and carrier; the memo names the allocation.
- Theming credit-protection-insurance complaints as either pure-credit or pure-insurance when the theme spans both surfaces. The memo carries both reads.
- Reading state-DOI complaint volume in isolation from the NAIC CDS peer benchmark; the CDS comparison is part of how the regulator reads the firm's complaint posture.
- Treating accelerated-underwriting AI themes as model-risk-only issues; the consumer-experience surface is in scope and the theme analysis covers it.
- Missing the producer-channel complaint records when complaints route through the producer rather than direct to the carrier; both channels are in the population.
