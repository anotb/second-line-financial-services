# Troubleshooting: marketing-claim-review

Recurring failure modes when a marketing-claim review memo looks complete but is not. The drafter should preempt these; the decision-forum reviewer (marketing-compliance committee, CCO, conduct-risk lead, counsel) should catch the rest.

## The disclosure was reviewed on desktop and not on mobile

Symptom: the memo records the disclosure adequacy read against the desktop layout and the asset is approved; the mobile layout drifts the trigger-term-driven additional disclosures below the fold and the disclosure is no longer clear-and-conspicuous on the actual served device.

Why it happens: the marketing brief and the design files are in desktop-resolution; the reviewer reads what is in front of them. The clear-and-conspicuous standard runs by device class.

Fix: the asset register names the device classes captured per asset; the disclosure adequacy block records the disclosure location per device class; the device-class-delta column is populated and a non-trivial delta surfaces a mobile-layout finding. Add a device-class disclosure-test control to the requested controls.

## A substantiation file is treated as substantiation

Symptom: the per-claim substantiation column is filled with "MAP file 234"; the file is from a different campaign, an earlier product version, or a study that does not support the in-scope claim.

Why it happens: substantiation files are reused across campaigns without per-claim review; the MAP record system records that a file exists, not whether it supports the specific claim.

Fix: per-claim source-of-substantiation field with date is populated and read; substantiation must reference the in-scope product and be within a reasonable currency window for the claim category. Add a substantiation-recency control to the requested controls.

## AI-personalised or AI-generated copy is treated as out of scope

Symptom: the per-asset claim register reads against the brief; the AI block is empty or marked `ai_in_path: false`. The actual displayed claim on the served variant is different from the brief; or the claim is a personalised assertion fabricated by the headline-generation pipeline.

Why it happens: drafters treat AI personalisation as a model-risk question rather than a marketing-claim question. The bureau and the FTC have been explicit that UDAAP / UDAP authority reaches the displayed claim; novel technology is not a defence.

Fix: when AI is in the production path or the personalisation path, the AI-content review block fires; per-served-variant review and per-variant substantiation are the discipline. The April 2023 Joint Statement is cited from `references/source-anchors.md`. Where the personalisation pipeline asserts a probability, eligibility, or other claim that is not connected to a model output supporting the assertion, the finding is fabrication and the kill-switch is the immediate remediation.

## Fair-lending distribution and targeting treated as not-applicable to marketing

Symptom: the fair-lending distribution-and-targeting block is empty or marked `n-a`. The asset is a personal-loan or credit-card or BNPL marketing campaign; the audience-targeting parameters include lookalike-audience seeds, ZIP-based targeting, or interest-category combinations.

Why it happens: drafters scope fair-lending to underwriting and pricing; ECOA / Reg B §1002.4(b) discouragement and FHA §3604(c) discriminatory advertising on dwelling-related products are treated as edge cases.

Fix: the fair-lending distribution-and-targeting block is populated for any product that ECOA / FHA touches; the block records the audience-targeting parameters, the channel skew, and the protected-class implication. Where the finding raises a parallel disparity-test question, cross-reference `fair-lending-test-plan`.

## Privacy claims are reviewed against the privacy notice only

Symptom: the on-asset privacy claim ("we will never sell your data") is checked against the firm's GLBA / Reg P privacy notice; the AdChoices representation, the dark-pattern privacy fact patterns, and the state-privacy-law (CCPA / CPRA) interaction are not addressed.

Why it happens: privacy review is treated as a matter of notice-content compliance; the state-law surface and the dark-pattern surface expand the analysis but are not always loaded.

Fix: load the privacy cross-cutting overlay on every digital-channel review. The on-asset privacy claim is read against the privacy notice, the AdChoices representation (if in play), the dark-pattern privacy fact patterns, the state-privacy-law footprint, and (where AI is in path) the AI-personalisation privacy implication.

## Dark-pattern findings written as "the UX is confusing"

Symptom: the dark-pattern findings block lists "the consent flow is confusing" or "the cancellation path is unclear" without naming a taxonomy entry, the location in the asset, or the consumer-harm hypothesis.

Why it happens: drafters treat dark patterns as a UX-quality issue rather than a regulatory finding under existing UDAAP / UDAP authority.

Fix: each dark-pattern finding names the FTC dark-pattern catalog entry (nagging, obstruction, sneaking, interface interference, forced action, social-proof manipulation, asymmetric choice, hidden subscription, confirmshaming, or other), the location in the asset, and the consumer-harm hypothesis. "The cookie banner uses interface-interference (asymmetric button weight; pre-checked accept; reject path requires three additional clicks) at the first interaction on the landing page; consumers are channeled into accepting consent they would not provide under symmetric choice" is a finding. "The UX is confusing" is not.

## Asset-level UDAAP findings are conflated with product-level UDAAP findings

Symptom: the memo's UDAAP findings block reads as a product-level UDAAP review; the population estimate covers the product, not the served-asset audience; the abusiveness analysis runs on the fee mechanic rather than on the asset's representation of the fee mechanic.

Why it happens: drafters treat UDAAP as one analysis regardless of unit; the product-level review and the asset-level review are conflated.

Fix: asset-level UDAAP findings are scoped to the displayed asset (the deception in the served claim; the unfairness in the asset's misrepresentation of cost; the abusiveness in the asset's dark-pattern design). Where the asset-level finding chains to a product-level UDAAP read, the cross-reference to `udaap-risk-review` is named; the product-level analysis lives there, not in this memo.

## Endorsement disclosures reviewed against firm policy only

Symptom: the creator-affiliate or influencer placement is reviewed against the firm's material-connection disclosure policy (sponsorship label is present); the disclosure timing, placement, and platform-specific mechanics are not addressed against the FTC Endorsement Guides framework.

Why it happens: drafters check for the presence of a sponsorship label and stop; the channel-specific Endorsement Guides expectations are not loaded.

Fix: per-platform Endorsement Guides review is part of the endorsement-claim block; sponsorship disclosure timing, placement (above-the-fold; first-three-seconds for video), prominence, and verbal-vs-visual mechanics are read. The 2023 Endorsement Guides revisions [verify exact treatment of AI-generated endorsements] address synthetic-content elements and should be loaded where AI-generated avatars or testimonials are in play.

## Kill-switch is treated as outside the memo's scope

Symptom: the recommended edits block lists revisions but no asset is marked as a kill-switch candidate; assets with critical findings (fabricated claims; clear-and-conspicuous failures on operative disclosures; FDIC-insurance misrepresentation; sensitive-attribute targeting findings) remain in market pending edit.

Why it happens: drafters treat the kill-switch as a takedown decision reserved for the committee; the memo does not flag candidates.

Fix: the kill-switch column on the recommended-edits block is populated; assets with critical findings are flagged as kill-switch candidates with rationale. The committee decides on the takedown; the memo names the candidates so the committee has the asset-level finding in front of it.

## "We will never sell your data" claim not reconciled with state-privacy-law disclosures

Symptom: the privacy-claim block records the on-asset claim and notes that the privacy notice is consistent; the firm's CCPA / CPRA Notice at Collection discloses "share for cross-context behavioral advertising" which is broader than the marketing voice's "sell" but the gap is not addressed.

Why it happens: the marketing voice and the legal voice operate on different vocabularies; the gap is treated as a vocabulary issue rather than a deception finding.

Fix: the on-asset privacy claim is read against the firm's CCPA / CPRA disclosures and the actual data-flow practice; the gap between marketing voice and state-law disclosure voice is named and surfaced as a deception finding or as an open legal question for counsel.

## Sponsor-bank arrangement treated as the program-operator's marketing review

Symptom: the asset bears the sponsor bank's name or logo; the review is conducted by the program-operator's marketing-compliance function only; the sponsor-bank consumer-compliance officer does not see the memo until after launch.

Why it happens: the program operator owns the marketing function operationally; the sponsor bank is treated as a passive recipient.

Fix: where the asset bears the bank's name or logo, joint review and joint approval are the discipline. The reviewer-and-review-posture block records `joint-with-sponsor-bank` or names the joint review structure; the recommended edits and the kill-switch decisions are joint between the marketing-compliance functions and the sponsor-bank consumer-compliance function.

## Source trace and confidence label absent

Symptom: the memo cites no sources for findings. Element-test conclusions appear without citation; substantiation conclusions appear without source; the privacy-claim findings appear without citation to the privacy notice or to the operative state law.

Why it happens: the drafter borrowed from prior memos or from external references without recording the source.

Fix: every material claim cites a source from `references/source-anchors.md` (or a loaded overlay) by file path. Source evidence (the served asset; the substantiation file; the MAP record), management assertions (the marketing-team brief), public-source obligations (the operative regulation), generated inferences (the reviewer's read), and open legal questions stay distinguishable. The confidence label at the end reflects how well the memo supports the recommended decision.

## Capital-markets or insurance asset routed into this skill in error

Symptom: the memo is reviewing an investment-adviser performance advertisement, a FINRA broker-dealer communication, or a life-insurance advertising asset and applying Reg Z and UDAAP framing to it.

Why it happens: the drafter loaded the wrong skill; the consumer-financial UDAAP / Reg Z lane is not the SEC Marketing Rule, FINRA Rule 2210, or NAIC Model #570 lane.

Fix: route to the firm's investment-adviser compliance, broker-dealer compliance, or insurance-conduct function. The boundary skill in `capital-markets-asset-management-compliance/skills/marketing-rule-evidence` is the closer-fit surface inside this repo for the SEC investment adviser Marketing Rule lane. The capital-markets and insurance sector overlays in this skill name the boundary explicitly; check the overlay before drafting.

## Decision forum is unnamed

Symptom: the memo is fully drafted, the recommendations are well-specified, and there is no record of which forum decides on the edits and the kill-switch.

Why it happens: the drafter treated the memo as the work product itself rather than as the input to a decision-forum gate.

Fix: `decision_forum.named_forum` is filled. The memo is in `draft` until the named forum decides; the edit execution and the kill-switch begin once the gate clears (or earlier where counsel directs an interim posture on a critical finding).
