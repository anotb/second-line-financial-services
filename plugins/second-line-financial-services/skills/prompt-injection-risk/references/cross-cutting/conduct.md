# Conduct cross-cutting overlay for prompt-injection-risk

When the scope record flags `conduct` for a prompt-injection review, this overlay loads to address the conduct-risk dimension of prompt-injection exposure on customer-facing or distribution-touching GenAI use cases. The threat is not abstract: a successful injection on a customer-facing assistant can produce a misleading representation, a misstated material fact about a product, an undisclosed AI-generated communication on a matter of public interest, or an off-policy promise the firm has to honour or remediate. Those outcomes are conduct events on their face.

Loaded by: `prompt-injection-risk/SKILL.md` when `scope.cross_cutting_set` includes `conduct`. The conduct overlay loads where the use case generates or assists customer-facing communications, distribution materials, marketing assets, fiduciary-or-recommendation surfaces, or where the firm's conduct framework names the use case under its scope. The cyber overlay is the primary lens on this skill; conduct sits as a parallel lens, not a substitute. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- **CFPB UDAAP authority** — 12 USC §5531 (unfair, deceptive, or abusive acts or practices); the bureau's authority reaches algorithmic outcomes that produce UDAAP exposure. Where prompt-injection causes the system to generate a deceptive or misleading communication to a consumer, the conduct frame applies.
- **FTC Section 5** — 15 USC §45 unfair or deceptive acts or practices; for non-bank entities outside CFPB scope or for marketing-facing surfaces.
- **SEC Marketing Rule** — 17 CFR §275.206(4)-1 — for SEC-registered investment advisers, the Marketing Rule reaches advertisements and testimonial content; an AI-generated communication that constitutes an advertisement under the rule's definition is in scope.
- **FINRA communications rules** — Rule 2210 (communications with the public); Rule 2111 (suitability); Rule 2090 (KYC) — for broker-dealer customer-facing AI use cases.
- **Reg BI** — 17 CFR §240.15l-1 — Care Obligation, Disclosure Obligation, Conflict of Interest Obligation for broker-dealers making recommendations; AI-assisted recommendation surfaces inherit the obligations.
- **NAIC Model Acts and AI Bulletin (December 2023)** — Model #880 (Unfair Trade Practices), Model #900 (Unfair Claims Settlement Practices), and the AI Bulletin on insurer use of AI; for life, health, and P&C insurance customer-facing AI surfaces.
- **April 2023 Joint Statement** — CFPB, EEOC, DOJ Civil Rights Division, FTC — on enforcement of civil rights, fair competition, consumer protection, and equal opportunity laws against algorithmic discrimination and automated systems; the statement underwrites the conduct-and-fair-lending lens on AI.
- **CFPB AI / complex-model framing** — the bureau has reaffirmed that algorithmic outcomes are reachable under existing UDAAP, ECOA, and FCRA authorities; specific Circulars (2022-03 and 2023-03) were withdrawn May 12, 2025 and live in the source-anchors file as historical context, but the underlying regulatory reach was not the source of the obligation.
- **FCA SMCR and Consumer Duty** — for UK-licensed firms operating into the US or with US customer overlap; the cross-border perimeter of Consumer Duty is its own triage point and the senior-manager-accountability frame survives jurisdictional debate.

## What changes when conduct is flagged

### 1. Threat surface gains a customer-outcome read

Each carrier in the threat-surface table is read for its potential to produce a customer-facing outcome on injection success. The user-input carrier ties to whatever the consumer says next; the retrieved-content carrier ties to whatever the system tells the consumer based on content the consumer cannot see; the tool-output carrier ties to actions taken on the consumer's account; the multi-agent message carrier ties to upstream-agent decisions that shape the customer-facing agent's output. The conduct lens reads each carrier for: does an injection on this carrier produce a customer-facing communication, an account action, a recommendation, or a representation about a product. Where the answer is yes, the trust-basis column carries weight; "trusted because firm-controlled" reads differently when the failure mode is a UDAAP exposure than when the failure mode is a system-prompt leak.

### 2. Tested attack classes expand to include conduct-relevant outcomes

The AI-native attack classes carry through; the conduct overlay adds explicit testing for conduct-relevant outcomes on injection success:

- **Misleading-representation generation** — does the injected prompt cause the system to generate a misstated material fact about a product, fee, term, or risk. Tested against the firm's product-fact library and the operative disclosure language.
- **Off-policy promise generation** — does the injected prompt cause the system to commit the firm to a course of action outside policy (a fee waiver, a rate match, a settlement offer, a regulatory-treatment representation). Tested against the firm's commitment-authority matrix.
- **Recommendation-surface manipulation** — for systems with recommendation reach (Reg BI, suitability, IA fiduciary), does an injection cause the system to recommend a product the customer's profile does not support. Tested against the firm's suitability and recommendation-governance rules.
- **AI-disclosure suppression** — does an injection cause the system to suppress the AI-interaction disclosure or the AI-generated-content disclosure where one is required. Tested against the firm's disclosure-language inventory.
- **Vulnerable-customer-handling override** — does an injection cause the system to bypass the firm's vulnerable-customer-handling protocols (escalation triggers, hold-the-line scripts, mandatory transfer to a human). Tested against the firm's vulnerable-customer policy.
- **Complaint-pattern generation** — where the firm's complaint surveillance has flagged a theme tied to AI-generated communications, does an injection reproduce or amplify the theme. Tested where the complaint signal is present.

The `dataset_or_redteam_ref` field on these attack classes names whether the test set was constructed from the firm's product-fact library, the firm's complaint-monitoring extracts, or a third-party conduct-test corpus. Where the test was vendor-side only and did not exercise the firm's conduct surface, that gap is a recommended-action item.

### 3. Mitigations expand to include the conduct control set

In addition to the AI-native and cyber-tagged mitigations, the conduct overlay expects the review to record:

- **Output-side fact-checking against the firm's product-fact library**: detection and refusal where the generated content states a fact that conflicts with the canonical product representation.
- **Commitment-authority enforcement**: detection of off-policy commitments (fee waivers, rate matches, settlement offers, regulatory-treatment representations) and routing to human approval.
- **AI-disclosure enforcement**: structured-output enforcement on the AI-interaction disclosure, the AI-generated-content disclosure (Marketing Rule, NAIC AI Bulletin posture), and any sector-specific disclosure tied to the use case.
- **Vulnerable-customer-handling guardrails**: hard-coded escalation triggers and transfer paths that injection cannot suppress; verified through testing.
- **Recommendation-surface controls** for Reg BI and suitability use cases: pre-decision review chain, reasoned-basis documentation, conflict-of-interest disclosure enforcement.
- **Customer-recourse path**: how a customer challenges an output the system produced; how complaints tied to the system route into the firm's complaint-handling and surveillance program; how complaints feed back to model change management.
- **Conduct-event taxonomy alignment**: tagging of injection-driven incidents as conduct-event candidates with a path to the conduct-risk function for classification.

Each conduct-tagged mitigation entry retains the schema's required fields (mitigation, type, evidence pointer, owner, exercised_in_test); the owner field for conduct-tagged entries typically names the conduct function (Head of Conduct Risk, Head of Consumer Compliance, Head of Sales Practices, Head of Distribution Compliance, Head of Marketing Review) or a named conduct-accountable manager role under SMCR for UK-licensed firms.

### 4. Monitoring adds the conduct-tagged signal set

Beyond the cyber and privacy signals, the conduct overlay adds:

- **Off-policy-output detection rate**: rate at which output-side filters detect content conflicting with the firm's product-fact library or commitment-authority matrix.
- **Disclosure-omission rate**: rate at which generated communications lack the required AI-interaction or AI-generated-content disclosure.
- **Vulnerable-customer-handling bypass rate**: where the system serves a population that includes vulnerable customers, the rate of escalation-trigger non-fire.
- **Recommendation-rejection-on-review rate**: where the recommendation surface is human-reviewed pre-decision, the rate at which review rejects the AI-suggested recommendation; a sustained drop is a signal of either reviewer fatigue or upstream control regression.
- **Complaint-theme correlation**: the rate at which complaints tagged to AI-driven communication or AI-driven recommendation map to the use case under review; the conduct-risk function consumes the signal.

Each signal retains the schema's required fields (signal, threshold, frequency, owner, escalation path); conduct-tagged entries escalate to the conduct function in addition to or in place of the model owner.

### 5. Incident-response section names conduct-relevant routing

The conduct overlay's load-bearing addition to the IR section is conduct-event classification and conduct-function routing. Per incident class, the entries record:

- **Conduct-event candidate flag** — whether the incident class is on the firm's conduct-event taxonomy (typically yes for any injection-driven misleading communication, off-policy commitment, recommendation-surface override, or disclosure suppression).
- **Conduct-function notification** — the path to the Head of Conduct Risk and to the conduct-accountable manager (under SMCR for UK-licensed; under firm framework otherwise) on confirmed incidents.
- **Customer-redress decision path** — where the incident produced customer harm or potential harm, the path to the redress decision (typically the consumer compliance function, with counsel on close calls).
- **Complaint-response and surveillance-loop integration** — the path back to complaint surveillance to set or refresh the watch theme on complaint coding for the affected population.
- **Regulator-engagement posture** — separate from the cyber-notification triggers (which the cyber overlay carries), the conduct overlay records the regulator-engagement triggers tied to conduct exposure (CFPB inquiry, state-AG referral, FINRA Rule 4530 reportable event, FCA Section 166 review, NAIC market-conduct exam scope).

The conduct-event candidate flag is non-optional on customer-facing systems. An injection-driven incident on a customer-facing surface that the IR section does not classify as a conduct-event candidate is a finding.

### 6. Recommended actions add the conduct-specific items

The standard conduct-tagged recommended-actions items the overlay surfaces:

- **Conduct review on every change-of-version notice and every material change in retrieval corpus, tool inventory, or system prompt.** The conduct function or named conduct-accountable manager signs.
- **Customer-outcome distribution monitoring** — where the use case affects pricing, eligibility, or recommendation, periodic review of the distribution against the firm's conduct-framework expectations.
- **Disclosure-language refresh cadence** — the AI-interaction and AI-generated-content disclosure language is reviewed against the firm conduct-framework refresh cycle and against vendor change-of-version triggers; the customer-comprehension assessment is a conduct artifact.
- **Vulnerable-customer-handling tabletop** — annual at minimum; quarterly for tier-1 customer-facing use cases. Tests the escalation triggers, the hold-the-line scripts, and the mandatory-transfer paths against injection-driven scenarios.
- **Complaint-loop closure** — defined complaint codes the firm watches post-deployment, the cadence of the read, the escalation trigger if a theme persists.

## Conduct-specific output additions

In the structured object (`schemas/prompt-injection-review.schema.json`):

- `cross_cutting_overlay_notes.conduct` carries the conduct-specific fields: customer-outcome read on threat-surface entries, conduct-relevant tested-attack classes, named conduct-side mitigations, conduct-event candidate classification per incident class, conduct-function routing path, conduct-accountable manager role.
- `mitigations[]` entries with conduct-tagged owner (conduct function or sub-function; named conduct-accountable manager role).
- `monitoring_detection[]` entries with conduct-tagged escalation path.
- `incident_response[]` entries with `conduct_event_candidate` and `conduct_function_notification_path` populated where applicable.
- `recommended_actions[]` entries with conduct-tagged owner role.

## Common pitfalls in conduct-flagged prompt-injection reviews

- Treating prompt injection as cyber-only when the use case is customer-facing. The cyber overlay covers the access, logging, and notification; the conduct overlay covers the customer-outcome path, which is where the firm gets sued, fined, or remediated.
- Reading vendor red-team coverage as evidence the firm's conduct surface is hardened. Vendor red-team sets do not exercise the firm's product-fact library, commitment-authority matrix, or vulnerable-customer-handling protocols.
- Recording residual risk on a customer-facing use case without a conduct-event-candidate evaluation. Injection-driven misleading communications and off-policy commitments are conduct events; the IR section names the classification.
- Naming the model owner as the conduct-accountable manager when the firm's conduct framework names a different role. The two are separable and frequently are separated; the review is explicit.
- Treating disclosure-language as a legal artifact alone. Disclosure language is a conduct artifact; the conduct function owns the customer-comprehension assessment and the refresh cadence.
- Skipping the complaint-loop closure. A use case that ships without defined complaint codes the firm watches post-deployment is shipping without a feedback mechanism.
- Using cyber-only IR runbooks for conduct-relevant incidents. The IR runbook integration includes the path to conduct, consumer compliance, and customer-redress decision-makers.
