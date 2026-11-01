# Troubleshooting: udaap-risk-review

Recurring failure modes when a UDAAP review memo looks complete but is not. The drafter should preempt these; the decision-forum reviewer (CCO, conduct-risk lead, head of consumer compliance, fair-lending committee, counsel) should catch the rest.

## The memo covers only the deception prong

Symptom: the memo lays out the marketing copy and the disclosure document, runs the deception analysis, and stops. Unfairness and abusiveness blocks are absent or marked `not-applicable` without rationale.

Why it happens: deception is the easiest prong to evidence with marketing artifacts; firms over-index on deception because the evidence is on hand and the legal framing is familiar. Unfairness requires population estimates and magnitude analysis; abusiveness requires the consumer-journey design and the material-interference read. Both take more work.

Fix: schema requires `unfairness` and `abusiveness` blocks. Abusiveness can land at `not-applicable` but only with `applicability_rationale` filled. A memo that surfaces only deception is a marketing review, not a UDAAP review.

## "Some customers were charged" is the unfairness finding

Symptom: the unfairness block has injury_type filled but the population and magnitude fields are vague ("a number of customers", "some accountholders", "the affected segment").

Why it happens: the drafter wrote the unfairness analysis from policy text or marketing assets without pulling transaction-data evidence. UDAAP findings without population and magnitude do not support remediation framing.

Fix: schema requires `unfairness.substantial_injury.population_estimate` and `magnitude_per_consumer` or `magnitude_aggregate`. Where evidence is not yet available, mark `population_evidence_flag: evidence-needed` rather than handwaving. The memo carries the analytical work; vagueness is a reviewer flag.

## "The disclosure was technically correct" is the deception defence

Symptom: the deception block records the disclosure document and concludes that because the document is materially-correct, deception does not apply.

Why it happens: the drafter is reading the disclosure in isolation from the consumer-journey context. CFPB has consistently pursued context-driven deception; the disclosure document is one input to the analysis, not the analysis.

Fix: the deception block names the consumer-journey context in `representation_or_omission` and reads the reasonable-consumer framing in the actual journey, not from the document text alone. Materially-correct disclosure can still mislead a reasonable consumer in context.

## Countervailing-benefits read is the first line's marketing pitch

Symptom: the unfairness block records the countervailing-benefits assertion as a list of product features and concludes that the benefits outweigh the injury without independent reviewer assessment.

Why it happens: the drafter consolidated the first-line's marketing pitch into the countervailing-benefits field. The prong is not a sales argument.

Fix: schema separates `first_line_assertion` and `reviewer_assessment`. The reviewer must independently assess; the first-line assertion is recorded but not sufficient. The `outweighs_injury` enum forces a reviewer judgment.

## AI is in path; AI block is empty

Symptom: the in-scope flow includes an AI / ML / complex-algorithm surface (personalisation engine, retention-offer engine, conversational AI, AI-generated communication), and the `ai_algorithmic_findings` block is empty or marked `ai_in_path: false`.

Why it happens: the drafter built the memo from a non-AI template; or treated AI as a model-risk issue rather than a UDAAP issue; or hesitated to apply UDAAP framing to algorithmic outcomes.

Fix: when AI / ML / complex-algorithm is in the in-scope flow, `ai_in_path: true` and the `model_inventory` and `udaap_theory` fields are populated. The bureau has been explicit under the April 2023 Joint Statement and CFPB Circulars 2022-03 and 2023-03 that existing UDAAP authority reaches algorithmic outcomes; novel technology is not a defence.

## Severity rating without a rubric

Symptom: aggregate severity is set but no rubric is referenced and no per-element severity is recorded; the rationale field is generic ("significant risk" or "moderate exposure") with no per-element reasoning.

Why it happens: severity drift is the single most common audit finding on UDAAP processes. Drafters set severity by feel.

Fix: schema requires `severity_per_element` and `severity_rationale`. SKILL.md names the rubric (Low / Medium / High / Critical with explicit definitions). The rationale per element is mandatory.

## Conduct-risk implications block is checkbox content

Symptom: the conduct-risk implications block lists the conduct-risk taxonomy categories as a generic checklist with no narrative; the conduct-accountable manager role is unfilled; the conduct-event candidate flag is missing.

Why it happens: the drafter consumed the conduct overlay as a checklist rather than as a substantive overlay; or treated the conduct-risk function as out of scope.

Fix: conduct overlay is mandatory on this skill. `conduct_risk_implications.taxonomy_tie_back` is populated; `conduct_accountable_manager_role` names a role under SMCR or the firm's conduct framework, distinct from the UDAAP-decision forum. The conduct overlay is what makes UDAAP review more than just element analysis.

## Recommended remediation reads as generic policy advice

Symptom: the remediation block lists items like "review the disclosure", "update the marketing copy", "consider remediation" without owners, due dates, or accountable forums.

Why it happens: the drafter wrote the remediation in advisory voice rather than as a structured set of recommendations the decision-forum acts on. Generic remediation does not get executed.

Fix: schema requires `recommended_remediation[]` with `action`, `type`, `owner`, `due_date`, and `accountable_forum`. Each entry is specific and verifiable. "Restructure the application-page APR to include the instant-funding fee in the cost-of-credit math by 2026-06-30, owned by the head-of-product (fintech-side), with the joint product committee as the accountable forum" is a remediation. "Review the disclosure" is not.

## Privilege posture is unfilled or marked `n-a`

Symptom: `legal_privilege_posture` is blank, `n-a`, or marked optimistically as "not privileged" without counsel direction.

Why it happens: the drafter treated privilege as a counsel decision to be made later; or treated the UDAAP memo as a routine compliance artifact that does not need a privilege posture.

Fix: privilege posture is a basic discipline for the UDAAP memo; the field is mandatory. Record `attorney-client-privileged`, `attorney-work-product`, `dual-purpose-business-and-privileged`, `not-privileged`, or `posture-pending-counsel`. If counsel has not yet directed, surface the question to counsel before the memo lands at the decision forum, not after.

## Decision forum is unnamed

Symptom: the memo is fully drafted, the recommendations are well-specified, and there is no record of which forum decides on the remediation.

Why it happens: the drafter treated the memo as the work product itself rather than as the input to a decision-forum gate.

Fix: `decision_forum.named_forum` is filled. The memo is in `draft` until the named forum decides; the remediation execution does not begin until the gate clears (with the exception of urgent kill-switch or marketing-takedown actions where counsel directs an interim posture).

## The memo is the determination

Symptom: the memo reads like it has already concluded that a UDAAP violation has occurred; or reads like it has already concluded that no violation has occurred. Either is a failure mode.

Why it happens: the drafter conflated the memo with the determination. The memo is the analytical input; the determination, where required, is reserved for counsel and the bureau or other decision-makers.

Fix: the memo states the element analysis and the severity rating; it does not declare a final UDAAP determination. Where the element analysis supports a finding, the memo carries the recommendation for human decision.

## Sponsor-bank arrangement treated as a footnote

Symptom: the memo covers a sponsor-bank fintech program and lists the sponsor bank as a passive recipient of the review rather than as the accountable creditor of record (or accountable consumer-relationship holder).

Why it happens: the drafter is operating from the program-operator's perspective and treating sponsor-bank involvement as administrative.

Fix: where the in-scope fact pattern runs through a sponsor-bank arrangement, the bank is the accountable party under most arrangements and the bank's consumer-compliance program owns second-line review. The memo reflects joint ownership, joint approval, and a clear statement of which entity carries which duty.

## Source trace and confidence label absent

Symptom: the memo cites no sources for material claims. Element-test conclusions appear without citation; population estimates appear without sourcing; the severity rating appears without rubric reference.

Why it happens: the drafter borrowed from prior memos or from external references without recording the source.

Fix: every material claim cites a source from `references/source-anchors.md` (or a loaded overlay) by file path. Source evidence, management assertions, public-source obligations, generated inferences, and open legal questions stay distinguishable. The confidence label at the end reflects how well the memo supports the recommended decision.

## Element analysis ignores the AI overlay where AI is in path

Symptom: the deception block reviews the marketing copy; the unfairness block reviews the fee mechanics; the AI block is populated, but the element analysis does not specifically address the algorithmic outcome under any of the prongs.

Why it happens: the drafter treated the AI block as a separate section rather than letting it inform the element analysis.

Fix: where AI is in path, the element analysis names the algorithmic outcome specifically. The unfairness analysis addresses substantial injury through the algorithmic outcome and the reasonably-avoidable analysis under the algorithmic-design choice; the deception analysis addresses AI-generated communication where it misleads; the abusiveness analysis addresses algorithmic dark-pattern design where it materially interferes. The AI block is what makes the element analysis specific to the AI-in-path fact pattern.

## Insurance-side fact pattern in scope

Symptom: the memo is reviewing an insurance underwriting model or an insurance pricing decision and applying the §1031 element tests directly.

Why it happens: the drafter loaded the wrong skill; UDAAP review is not the right tool for most insurance work.

Fix: route to the insurance unfair-trade-practice framework (NAIC Model #880; state-DOI market-conduct procedures; NAIC AI Model Bulletin where AI is involved). The narrow exception is bank-affiliated credit-protection insurance bundled with credit, where the credit-side bundling mechanic is in UDAAP scope and the insurance-side decision is out. The insurance sector overlay names the boundary.
