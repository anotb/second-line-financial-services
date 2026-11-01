---
name: udaap-risk-review
description: "Draft a UDAAP risk review of a product, fee, disclosure, marketing, or customer flow."
argument-hint: "[product, feature, fee, flow, complaint cluster, enforcement theme; period; channel; population; AI-in-path flag]"
---

# UDAAP risk review

A UDAAP review memo is what the second-line consumer-compliance team produces so the CCO, the head of fair lending, the conduct-risk lead, the product committee, and (where directing) outside counsel can decide. The work is reading a product, fee, flow, marketing motion, or complaint pattern against the three element tests in Dodd-Frank §1031 (unfairness, deception, abusiveness), naming the consumer-harm hypothesis with a population estimate, and writing the recommended remediation that the decision-makers act on. The memo stops at the recommendation. The decision-makers decide.

The CFPB withdrew a substantial portion of its UDAAP advisory guidance on May 12, 2025 (overdraft, NSF representment, reopened-account, AAN-with-algorithms circulars; the April 2023 Abusiveness Policy Statement). The withdrawals do not change the statutory framework — §1031 and §1036 still set the standards, and state AGs, banking regulators (FRB, OCC, FDIC, NYDFS), and private plaintiffs continue to pursue analogous theories under their own authority. The skill anchors element analysis to the statute and to the Reg B / Reg E / Reg Z / Reg V text rather than to withdrawn CFPB items. Where the withdrawn items are still useful as analytical scaffolding (the unfairness three-prong; the abusiveness three statutory bases of unreasonable advantage), the memo cites the statute, not the rescinded interpretation. Where pre-2025 enforcement actions (consent orders) imposed remediation, those obligations remain in force and the firm's residual exposure follows the consent order, not the withdrawn circular.

The skill serves both lenses. A 1.5-line product compliance officer inside the business uses it to consolidate the UDAAP read as the product or campaign moves through the design and launch process; a 2-line independent UDAAP reviewer or conduct-risk officer uses the same skill to challenge what was drafted and to surface the elements that were not tested honestly. The seam between the two is the source-trace block, the open-questions list, and the severity rubric applied per element rather than as a single global rating.

The memo is a draft until the relevant decision forum (product committee, conduct committee, fair-lending committee, or counsel) acts on it. Approval is the gate; this skill stops short of finalising a UDAAP determination, approving products for launch, taking down live products, executing consumer redress, issuing customer-facing communications, or any other operational action.

## When to use

Drafts a second-line UDAAP review memo for a product, feature, fee, disclosure or customer-experience flow, marketing motion, complaint pattern, or enforcement theme. Element-by-element analysis under Dodd-Frank §1031 (unfairness, deception, abusiveness) and §1036; consumer-harm hypothesis with population and magnitude; AI / algorithmic-discrimination tie-in where automated systems are in path; severity rating with rubric; conduct-risk implications; recommended remediation; cross-references to complaint, marketing, adverse-action, and fair-lending review. The memo surfaces UDAAP risk for human decision; it does not finalize a UDAAP determination, take down a live product, execute consumer redress, or issue any customer-facing action.

Best for:
- Pre-launch UDAAP review of a new product, feature, fee structure, or disclosure flow before a product or risk committee approves launch.
- Targeted review after a complaint cluster (chain to `complaint-theme-analysis`), a regulator inquiry, or a peer enforcement action signals potential exposure on an analogous fact pattern in the firm's footprint.
- Annual UDAAP risk-assessment refresh by product line, including overdraft, deposit-fee, card, mortgage-servicing, auto add-on, BNPL, instant-funding, and subscription-style fee mechanics.
- Post-incident root-cause review where consumer harm has been alleged through complaints, social signals, employee escalations, or regulator engagement.
- Annual review of an AI-driven personalization, pricing, or communication surface where the bureau's existing UDAAP authority reaches the algorithmic outcome.

Not the right tool when:
- The question is fair-lending under ECOA, the FHA, or §1071 (use `fair-lending-test-plan`; UDAAP and fair-lending overlap on themes such as steering and marketing distribution but are distinct legal frameworks).
- The question is the adverse-action notice itself (use `adverse-action-review`; UDAAP touches AAN content where reasons obscure the actual decision logic, but the AAN-specific Reg B §1002.9 review lives next door).
- The question is asset-level marketing-claim substantiation on a single creative or piece of copy (use `marketing-claim-review`; this skill addresses UDAAP at the product, fee, flow, or theme level, not the asset level).
- The question is whether to file a complaint-theme escalation memo to the conduct or consumer-outcome committee (use `complaint-theme-analysis`; that skill produces the theme; this one tests a theme against the UDAAP elements).
- A final UDAAP determination, a launch decision, a takedown, or a consumer-redress program is required. The memo is the input to the decision; the decision is reserved for the CCO, conduct-risk lead, head of consumer compliance, fair-lending committee, conduct committee, product committee, and counsel.

## Ask yourself first

Most of what the memo needs is on the table by the time someone reaches for this skill. A few things to settle before drafting:

- What triggered the review. Pre-launch gate, complaint-theme escalation, regulator inquiry, peer enforcement action in the firm's footprint, post-incident review, annual refresh, or model deployment into a consumer-facing surface. Trigger drives scope, severity weighting, and which upstream artifact the memo consumes.
- Who decides. Product committee at pre-launch; CCO and conduct committee at recurring cycle; fair-lending committee where the UDAAP and fair-lending themes overlap (marketing distribution, steering, servicing); counsel at any post-incident or regulator-engagement posture. Decision forum drives audience, format, and privilege posture.
- What is in scope. A single product or feature; a fee or disclosure mechanic; a customer-experience flow (application, authentication, account closure, fee dispute, loss-mit); a marketing motion (pre-screen, lookalike, retention offer); a complaint pattern; an enforcement-theme parallel. The memo reviews one scope at a time; multi-scope reviews split into separate memos that cross-reference.
- Whether AI or an algorithm is in path. The answer flips on the AI / algorithmic-discrimination block, pulls in CFPB Circulars 2022-03 and 2023-03 and the April 2023 Joint Statement, and adds the algorithmic-feature read to the unfairness analysis. The bureau has used existing UDAAP authority against algorithmic harms; novel technology is not a defence.
- What the source posture is. Public-only, public-plus-firm-policy, public-plus-firm-policy-plus-evidence, or connector-aware. Source posture sets what evidence the memo can actually cite (complaints, transaction data, call recordings, marketing assets, policy text, training records, system-output logs, model-card pointer) and what carries `[evidence needed]`.

When `scope` is supplied, the skill consumes it for institution, persona, source posture, sector overlay set, and cross-cutting overlay set. Otherwise it asks the practitioner the few facts it needs and defaults to public posture if the practitioner declines, noting in the memo that scope was not formalised.

## How the memo gets built

The memo has the same spine across products, fees, and enforcement themes. A senior practitioner walks it roughly in the order below, but the conversation surfaces sections in whatever order the upstream artifacts and the in-scope inventory arrive; the structured record sorts itself.

**Scope and reviewer posture.** Product, feature, fee, disclosure, or process; period; channel (branch, digital, broker, marketplace, partner-of-record, sponsor-bank-program operator); population (applicants, accountholders, defaulted borrowers, the affected segment). Reviewer identification (who is writing); review posture (independent second-line, embedded 1.5-line, advisory engagement); legal-privilege posture (`attorney-client-privileged`, `attorney-work-product`, `dual-purpose-business-and-privileged`, `not-privileged`, or `posture-pending-counsel`); and the evidence base (sources, dates, completeness flag per source). Privilege posture is mandatory because UDAAP review memos commonly attract attorney-client and attorney-work-product privilege; the field is filled, not left for later.

**Element-by-element analysis.** The three prongs are tested separately. Each prong gets its own block; the analysis surfaces what is supported, what is `[evidence needed]`, and what is `indeterminate-pending-counsel`. A memo that covers only deception (the easiest to evidence with marketing artifacts) is not a UDAAP review.

- *Deception.* The CFPB UDAAP examination framework decomposes deception into three elements: a representation, omission, act, or practice that is likely to mislead the consumer; the consumer's interpretation is reasonable under the circumstances; and the representation, omission, act, or practice is material. The memo identifies the representation or omission (with the consumer-journey context, not just the disclosure document); evaluates likely-to-mislead from the reasonable-consumer perspective in the actual journey; and tests materiality (would a reasonable consumer's decision have changed). Materially-correct technical disclosure can still mislead a reasonable consumer in context; the bureau has consistently pursued context-driven deception. The deception block ends with a `likely_to_mislead` enum (`yes`, `no`, `indeterminate`) and a `materiality` enum (`material`, `not-material`, `indeterminate`).
- *Unfairness.* The §1031(c) statutory standard requires substantial injury that is not reasonably avoidable and is not outweighed by countervailing benefits to consumers or to competition. The memo populates `substantial_injury` (injury type, magnitude per consumer or in aggregate, affected population) with a population estimate; `reasonably_avoidable` (`yes`, `no`, `indeterminate`) with the avoidability analysis (was the consumer able to anticipate the injury, take reasonable steps to avoid it, and did the firm structure the choice to permit avoidance); and `countervailing_benefits` with the first-line's asserted benefit and the reviewer's independent assessment. "Some customers were charged" is not a UDAAP finding; the memo carries a population estimate or marks the finding as `[evidence needed: population magnitude]`.
- *Abusiveness.* The §1031(d) statutory standard reaches an act or practice that materially interferes with the ability of a consumer to understand a term or condition of a consumer financial product or service, or that takes unreasonable advantage of (i) a consumer's lack of understanding of the material risks, costs, or conditions; (ii) a consumer's inability to protect their own interests in selecting or using a product; or (iii) the reasonable reliance by the consumer on a covered person to act in their interests. The April 2023 CFPB Policy Statement on Abusive Acts or Practices clarifies the analytical posture and the evidentiary expectations. The memo populates `material_interference` (description and evidence) and `unreasonable_advantage` (with the type and the evidence). Abusiveness can land at `not-applicable` but only with the rationale on the record; the prong is not skipped silently.

**Consumer-harm hypothesis.** Population affected (with sourcing); magnitude (per-consumer dollar value; aggregate over the period); frequency (one-time, recurring, repeated); redress posture (whether redress is plausible and at what scale). The bureau and DOJ both center remedy framing on population-and-magnitude; the memo gives the decision-makers what they need to size the response.

**AI / algorithmic-discrimination tie-in.** Populated where any AI / ML / complex algorithm sits in the customer-facing surface (personalised pricing, retention offer engine, loan-approval pre-screen, conversational AI, AI-generated copy, agentic flow, dynamic disclosure, AI-driven communication scheduling). The block records: model id and version; decision use; ai_ml flag; vendor or in-house; validation status; model-card pointer where one exists (consume `model-card-builder` output where present). The block then names the unfairness theory specifically (substantial injury through algorithmic outcome; reasonably-avoidable analysis under the algorithmic-design choice; countervailing-benefits read on the algorithmic alternative). The bureau's posture under the April 2023 Joint Statement and CFPB Circulars 2022-03 and 2023-03 is that existing UDAAP and consumer-protection authority reach automated systems; the memo does not need novel theory to pursue the algorithmic outcome.

**Severity rating with rubric.** Severity is set per element (deception severity, unfairness severity, abusiveness severity), with an aggregate severity that reflects the highest per-element rating, the population magnitude, and the recurrence. The rubric:

- *Critical* — pattern matches a public CFPB or DOJ enforcement theme directly; large population; ongoing harm; remediation cannot wait for the next committee cycle.
- *High* — pattern matches a Supervisory Highlights focal item or a peer enforcement theme; meaningful population or magnitude; remediation needed within one committee cycle.
- *Medium* — element analysis surfaces real risk; population or magnitude is bounded or uncertain; remediation enters the controls roadmap.
- *Low* — element tests pass with no material concerns; the memo records the read and stops.

Severity drift is the single most common audit finding on UDAAP processes. The memo names the rubric and applies it per element, with the severity_rationale field carrying the per-element reasoning. A severity rating without a rubric is a vibe.

**Conduct-risk implications.** Loaded as cross-cutting overlay. The memo records the conduct-risk taxonomy tie-back (incentives, product design, communication, sales practices, customer outcome, complaint linkage); the named conduct-accountable manager (the role under SMCR for UK-licensed firms, or the firm's conduct framework's named role for non-UK firms); whether the conduct or customer-outcome committee gets a read alongside the UDAAP-decision forum; and whether the finding is a conduct-risk-event candidate under the firm's conduct-event taxonomy. UDAAP findings are the dominant conduct-risk signal in US consumer FS; the conduct overlay is mandatory on this skill.

**Recommended remediation.** Each remediation entry names: action; type (`consumer-redress`, `control-change`, `policy-change`, `disclosure-change`, `training`, `kill-switch-candidate`, `marketing-takedown-candidate`, `model-change-candidate`, `vendor-renegotiation`, `monitoring-uplift`); owner role; due date; and the accountable forum. The memo does not execute remediation; it recommends it and names who decides. Where remediation includes consumer redress, the memo flags the redress as a recommendation only; redress execution sits with operations under counsel direction.

**Open legal questions.** Items the memo defers to counsel. The list is not a hedge; it is a record of the decisions reserved for legal review (whether a fact pattern crosses the §1031 threshold, whether the response carries privilege, whether the remediation triggers a regulatory-notification obligation, whether the firm has self-reporting expectations).

**Cross-references.** Pointers to the related skills the decision forum should consume alongside this memo: `complaint-theme-analysis` for the complaint signal; `marketing-claim-review` for the marketing-asset-level review where marketing is in the fact pattern; `adverse-action-review` for AAN content overlap; `fair-lending-test-plan` where the same fact pattern raises an ECOA / FHA theory in parallel.

**Source trace and confidence.** Every material claim cites a source from `references/source-anchors.md` (or the relevant overlay) by file path. Source evidence, vendor or first-line management assertions, public-source obligations, generated inferences, and open legal questions stay distinguishable in the memo. The confidence label at the end reflects how well the memo can support the recommended decision; the label is honest, not aspirational.

### AI / algorithmic-discrimination overlay

When any AI / ML / complex algorithm is in path on the in-scope product, fee, flow, or marketing motion, the AI overlay fires inside the named sections rather than as a separate document:

- *Element analysis:* the unfairness prong is the most common UDAAP angle on algorithmic outcomes (substantial injury, reasonably-avoidable analysis, countervailing-benefits read on the algorithmic alternative). The deception prong applies where algorithmic communication or AI-generated copy misleads a reasonable consumer. The abusiveness prong applies where the algorithmic surface materially interferes with the consumer's ability to understand a term or condition.
- *AI-block fields:* model id and version; decision use; ai_ml; vendor or in-house; validation status; model-card pointer.
- *Source anchors:* the April 2023 Joint Statement, CFPB Circulars 2022-03 and 2023-03, and any operative CFPB AI circular at memo date are cited from `references/source-anchors.md`.
- *Cross-skill chain:* where the algorithmic outcome also raises an ECOA / FHA theory, the memo names the cross-reference to `fair-lending-test-plan` and stops short of an LDA-search specification (that is the test-plan job).

The overlay is mandatory once triggered. Missing the AI block on a memo where AI is in path is what the second-line reviewer or the conduct-risk lead flags first when the memo lands for committee.

### Sector overlays

When the scope names a sector, load the matching `references/sector-overlays/<sector>.md`:

- *Banking* — depository-specific themes: overdraft and NSF practices including authorize-positive-settle-negative; deposit-account fee mechanics; surprise-representment fees; mortgage-servicing themes (loss-mitigation conduct, force-placed insurance, fee assessment); credit-card UDAAP themes (deferred-interest promotions, rewards-program changes, balance-transfer mechanics, retention-offer mechanics); auto-loan add-ons (GAP, VSC, debt-cancellation).
- *Payments-fintech* — sponsor-bank attribution and joint accountability; BNPL UDAAP themes; P2P and Reg E error-resolution conduct; subscription and negative-option mechanics; tip and "instant funding" fee mechanics; junk-fee themes; algorithmic personalisation themes specific to digital-first fintech surfaces.
- *Capital markets* — narrow: retail brokerage UDAP overlay where Reg BI and FINRA Rule 2010 overlap on the same fact pattern (sales-practice fairness; customer-outcome harm in retail-broker steering and revenue-sharing arrangements). Securities-based-lending and margin-call mechanics where the consumer-experience flow on the credit side raises UDAAP-equivalent concerns. Most capital-markets activity sits outside the CFPB's UDAAP perimeter; the overlay is named so reviewers do not over-extend.
- *Insurance* — generally not applicable. Insurance unfair-trade-practice review sits with state DOIs under the NAIC Unfair Trade Practices Act framework, not under Dodd-Frank UDAAP. The overlay flags the boundary so reviewers do not over-extend UDAAP into insurance underwriting, pricing, or claims handling. The narrow exception is bank-affiliated credit-protection insurance bundled with a credit product, where the credit-side UDAAP read covers the bundling mechanics.

### Cross-cutting overlays

Conduct overlay is mandatory on this skill (UDAAP findings are the dominant conduct-risk signal). Privacy overlay loads as secondary where the in-scope flow processes NPI in a way that itself raises a UDAAP angle (e.g., a deceptive privacy disclosure; a dark-pattern privacy-consent flow; a fee mechanic tied to privacy-permission state). Climate is not applicable.

## Quality bar

Holds across every memo: every material claim cites a source from `references/source-anchors.md` (or a loaded overlay) by file path; unsupported claims are marked `[evidence needed]`; section references that cannot be confirmed get `[verify section]` in the source-anchors file (not in the memo body); source evidence, management assertions, public-source obligations, generated inferences, and open legal or compliance questions stay distinguishable; no named institutions appear in narrative unless they are public defendants in a finalised enforcement action with a published consent order; the memo stops at the recommendation and the decision forum decides; element analysis covers all three prongs (abusiveness can be `not-applicable` only with rationale); the AI block is populated whenever any AI / ML / complex algorithm is in the path; the consumer-harm hypothesis carries a population estimate (or `[evidence needed: population magnitude]`); the severity rubric is named and applied per element; `legal_privilege_posture` is filled; the conduct overlay is loaded (this skill's mandatory cross-cutting); the recommended remediation entries name owners, types, and due dates rather than reading as generic recommendations.

## Adaptation

Memo depth and length scale to the trigger and the in-scope inventory. A pre-launch review of one new fee reads short; an annual refresh on an overdraft program reads longer; a post-incident review of a complaint cluster across a fintech program with a sponsor bank reads longer still. Audience drives shape: product-committee deck reads structured around the launch decision; conduct-committee read reads denser around the conduct-risk implications; counsel-direction memo carries explicit privilege framing and is more legal in voice. The sector overlay set drives which `references/sector-overlays/<sector>.md` is loaded; a sponsor-bank fintech program may load two. Source posture (public-only through connector-aware) drives the evidence the memo can actually cite; a public-only memo flags the evidence that would be needed but is not yet accessible.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays/banking.md`, `payments-fintech.md`, `capital-markets.md`, `insurance.md` — sector-specific framing loaded per scope.
- `references/cross-cutting/conduct.md` — UDAAP-conduct intersection (mandatory on this skill); `references/cross-cutting/privacy.md` — secondary, loaded where the in-scope flow raises a privacy-meets-UDAAP angle.
- `references/firm-overlay.md` — firm-installed taxonomy, named committees, conduct-event taxonomy, system-of-record paths (consumed when present).
- `templates/default-output.md` — memo template.
- `schemas/udaap-risk-review.schema.json` — structured-output contract.
- `examples/instant-funding-tip-fee.md`, `examples/overdraft-apsn-annual-refresh.md` — public-source-derived worked examples.
- `TROUBLESHOOTING.md` — recurring failure modes the drafter should preempt and the reviewer should catch.

## Output

Two artifacts: the memo in `templates/default-output.md` shape and a structured record conforming to `schemas/udaap-risk-review.schema.json`. The product committee, the CCO, the conduct committee, the fair-lending committee, or counsel acts on the memo; counsel sets privilege posture; downstream consumers (the conduct-risk reporting workflow, the complaint-monitoring loop that watches for re-emergence after remediation, the regulator-response file where engagement is in posture) read the structured record. The schema is the cross-skill contract; additive changes only. Add fields, do not rename or repurpose them. A breaking change is a versioned migration with the downstream consumers told in advance.

## Human review and AI disclosure

Open the deliverable with this line, and remove it only after the review below: `AI-assisted draft. Requires review by a qualified person before use.`

A qualified person with authority to change the output reviews it before it is delivered or relied on, and stays accountable for it. Where the output supports advice to an individual or a decision about an individual (credit, insurance underwriting, pricing or claims, employment, legal rights, or similar), that individual must be told AI was used to produce it. This skill does not make final decisions, file with a regulator, notify customers, execute transactions, or move money or other financial assets.
