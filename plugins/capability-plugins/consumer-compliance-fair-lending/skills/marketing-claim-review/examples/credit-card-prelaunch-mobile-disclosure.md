# Example: pre-launch marketing-claim review of a credit-card rewards campaign with an AI-personalised landing page

## Input

A national credit-card issuer is launching a new rewards card. The pre-launch marketing campaign covers: a hero web page; three paid-social variants (Meta and TikTok); two pre-approval emails to a warm-list audience; an AI-personalised landing page where the rewards-bonus headline is generated from a small set of input variables (current cardholder relationship; spending category mix; tenure). The marketing-compliance committee has scheduled a launch decision in two weeks. The CCO requests a second-line marketing-claim review memo for the committee read.

Source posture is public-plus-firm-policy-plus-evidence. Counsel directs the review for privilege.

## Why this scenario matters

This is a structurally common pre-launch fact pattern: multi-channel campaign; warm-list email; AI-personalised landing page; trigger-term-driven Reg Z disclosures with mobile-vs-desktop layout drift; superlative claim; foreign-transaction-fee disclosure mechanic; privacy-claim adjacency to CCPA / CPRA disclosures. The memo has to handle the per-asset claim register (each variant served), the device-class capture of disclosure layout, and the AI-content review on the personalised variants.

## Output sketch

```yaml
review_id: MCR-2026-CC-RWDS-PRELAUNCH-01
trigger: pre-launch-review
as_of_date: 2026-05-06
unit_of_analysis: single-campaign
campaign_id: CC-RWDS-2026-LAUNCH
period_in_market: {start: 2026-06-01, end: 2026-09-30}
channels_in_scope: [web, paid-social, email, landing-page]

scope:
  sector_overlay_set: [banking]
  cross_cutting_overlay_set: [conduct, privacy]
  source_posture: public-plus-firm-policy-plus-evidence
  sampling_basis: full-coverage
  exclusions:
    - The card application and solicitation form itself (separate Reg Z 1026.60 review)
    - The post-application onboarding flow (out of scope this cycle)
    - The Schumer-box content as such (separate review with first-line marketing)

reviewer_posture:
  reviewer_role: independent-consumer-compliance-second-line
  review_independence: independent-second-line
  counsel_directing: true
  legal_privilege_posture: attorney-client-privileged

asset_register:
  - asset_id: CC-RWDS-WEB-HERO-v3
    channel: web
    audience: prospects-broad-acquisition
    version: 3.0
    dates_in_market: {start: 2026-06-01, end: 2026-09-30}
    device_classes_captured: [desktop, mobile]
    screenshot_reference: /reviews/2026/CC-RWDS/web-hero-v3-{desktop,mobile}.png
  - asset_id: CC-RWDS-SOCIAL-META-v1
    channel: paid-social
    audience: lookalike-source-current-cardholders
    version: 1.0
    dates_in_market: {start: 2026-06-15, end: 2026-09-30}
    device_classes_captured: [mobile]
    screenshot_reference: /reviews/2026/CC-RWDS/social-meta-v1.png
  - asset_id: CC-RWDS-SOCIAL-TIKTOK-v1
    channel: paid-social
    audience: tiktok-broad-acquisition-25-44
    version: 1.0
    dates_in_market: {start: 2026-06-15, end: 2026-09-30}
    device_classes_captured: [mobile]
    screenshot_reference: /reviews/2026/CC-RWDS/social-tiktok-v1.png
  - asset_id: CC-RWDS-SOCIAL-META-v2
    channel: paid-social
    audience: lookalike-source-affluent-segment
    version: 2.0
    dates_in_market: {start: 2026-06-15, end: 2026-09-30}
    device_classes_captured: [mobile]
    screenshot_reference: /reviews/2026/CC-RWDS/social-meta-v2.png
  - asset_id: CC-RWDS-EMAIL-PREAPPROVAL-v1
    channel: email
    audience: warm-list-pre-approved
    version: 1.0
    dates_in_market: {start: 2026-06-01, end: 2026-09-30}
    device_classes_captured: [desktop, mobile]
    screenshot_reference: /reviews/2026/CC-RWDS/email-preapproval-v1-{desktop,mobile}.png
  - asset_id: CC-RWDS-EMAIL-PREAPPROVAL-v2
    channel: email
    audience: warm-list-pre-approved-second-touch
    version: 1.0
    dates_in_market: {start: 2026-06-15, end: 2026-09-30}
    device_classes_captured: [desktop, mobile]
    screenshot_reference: /reviews/2026/CC-RWDS/email-preapproval-v2-{desktop,mobile}.png
  - asset_id: CC-RWDS-LANDING-PERSONALIZED
    channel: landing-page
    audience: warm-list-pre-approved (personalised per cardholder profile)
    version: 1.0
    dates_in_market: {start: 2026-06-01, end: 2026-09-30}
    device_classes_captured: [desktop, mobile]
    screenshot_reference: /reviews/2026/CC-RWDS/landing-personalized-variants/

per_asset_findings:
  CC-RWDS-WEB-HERO-v3:
    claim_register:
      - claim_text: "Earn 80,000 bonus points after spending $4,000 in the first 90 days"
        category: rewards
        substantiation_status: substantiated
        substantiation_source: internal-data
        date: 2026-05-01
      - claim_text: "0% intro APR on purchases for 15 months"
        category: rate
        substantiation_status: substantiated
        substantiation_source: MAP
        date: 2026-05-01
      - claim_text: "No foreign transaction fees"
        category: fee
        substantiation_status: substantiated
        substantiation_source: MAP
        date: 2026-05-01
    disclosure_findings:
      - operative_rule: Reg Z 1026.16 (open-end credit advertising; trigger terms)
        in_scope: yes
        required_disclosure: trigger-term-driven additional disclosures (APR, fees, payment terms)
        disclosure_location_desktop: above-the-fold
        disclosure_location_mobile: below-the-fold (after two scrolls)
        device_class_delta: yes
        clear_and_conspicuous_read: inadequate-on-mobile
        finding: >
          The trigger-term-driven additional disclosures are clear-and-conspicuous on
          desktop but below-the-fold on mobile after two scrolls. The displayed asset
          on mobile fails the clear-and-conspicuous standard for the trigger terms
          stated above the fold.
    udaap_findings:
      - prong: deception
        claim_or_element: trigger-term disclosure on mobile
        reasoning: >
          A reasonable consumer on mobile would read the rewards-and-rate
          representation above the fold and would not necessarily reach the
          additional disclosures two scrolls down. The representation is likely to
          mislead a reasonable consumer in the served context; the materiality is
          high because the additional disclosures include the operative APR and
          fee detail.
        severity: high
        cross_reference_to_udaap_risk_review: no (asset-level finding; addressed by edit)

  CC-RWDS-SOCIAL-META-v2:
    claim_register:
      - claim_text: "The most rewarding card on the market"
        category: comparative-superlative
        substantiation_status: not-substantiated
        substantiation_source: ""
        date: 2026-05-06
        notes: "Substantiation file references a 2024 J.D. Power study on a different product; not transferable to this product."
    udaap_findings:
      - prong: deception
        claim_or_element: superlative claim ("the most rewarding")
        reasoning: >
          The claim is a comparative superlative; substantiation requires a current,
          methodology-disclosed comparison that supports the assertion. The 2024
          study referenced in the substantiation file relates to a different product
          and does not support the claim.
        severity: medium
        cross_reference_to_udaap_risk_review: no

  CC-RWDS-LANDING-PERSONALIZED:
    claim_register:
      - claim_text: "Based on your spending, you're 99% likely to be approved"
        category: eligibility
        substantiation_status: not-substantiated
        substantiation_source: ""
        date: 2026-05-06
        notes: >
          The personalisation engine generates this claim from spending-category mix
          and tenure. The "99% likely to be approved" assertion is not supported by
          a model output; the engine asserts the probability without an underlying
          probability estimate from the credit-decisioning model.
    udaap_findings:
      - prong: deception
        claim_or_element: AI-generated approval-probability claim
        reasoning: >
          The displayed claim is likely to mislead a reasonable consumer about
          actual approval probability. The personalisation pipeline does not feed
          from the credit-decisioning model output; the asserted probability is
          fabricated by the headline-generation pipeline.
        severity: critical
        cross_reference_to_udaap_risk_review: yes (chain to product-level UDAAP review on AI-personalisation pipeline)
    privacy_findings:
      - category: ai-personalisation-on-restricted-data
        claim_or_element: "personalisation inputs include spending-category mix"
        reasoning: >
          The personalisation engine consumes consumer spending-category data. The
          on-asset disclosure does not address the personalisation mechanic; the
          firm's privacy notice references "service personalisation" but a
          reasonable consumer reading the landing page would not understand that
          the headline is generated from their spending data.
    ai_content_review:
      ai_in_path: true
      variants_count: ~12 served per audience segment
      model_id: PERSONALIZE-RWDS-LANDING-v1
      prompt_template: "/ml/templates/rwds-landing-personalize-v1.txt"
      output_review_status: not-reviewed (variants generated at serve time; no claim-level review pre-serve)
      fabrication_risk: high
      privacy_implication: addressed in privacy_findings above
      joint_statement_cite: true
    edits_requested:
      - edit: "Remove the 'you're 99% likely to be approved' claim from all served variants of the personalised landing page; pause the personalisation engine on the approval-probability variable until the engine is connected to the credit-decisioning model output and a per-variant substantiation control is in place."
        owner: head-of-personalisation
        due_date: 2026-05-20
        severity: critical
        kill_switch_candidate: yes
      - edit: "Re-design the mobile layout on the web hero so the trigger-term-driven additional disclosures are clear-and-conspicuous above the fold or accessible through symmetrical interaction with the rewards-and-rate representation."
        owner: head-of-marketing
        due_date: 2026-05-25
        severity: high
        kill_switch_candidate: no
      - edit: "Remove or substantiate the 'most rewarding' superlative on the Meta v2 social variant; substantiation requires a current, methodology-disclosed comparison."
        owner: head-of-marketing-compliance
        due_date: 2026-05-25
        severity: medium
        kill_switch_candidate: no

  CC-RWDS-EMAIL-PREAPPROVAL-v1:
    privacy_findings:
      - category: glba-reg-p-consistency
        claim_or_element: "We will never sell your data"
        reasoning: >
          The on-asset claim represents that the firm will never sell consumer
          data. The firm's CCPA / CPRA Notice at Collection discloses "share for
          cross-context behavioral advertising", which is broader than the marketing
          voice's "sell" but is the operative state-law term. A reasonable consumer
          reading the email and the linked privacy notice may receive inconsistent
          representations.
        cross_reference: state-privacy-law-interaction; chain to compliance with CCPA / CPRA workflow

requested_controls:
  - control: "Add a MAP control on AI-personalised claim generation: every served variant requires substantiation tied to a model output or to a documented data source, with a recency review."
    control_type: ai-personalisation-review
    owner: head-of-personalisation; head-of-marketing-compliance
    rationale: "Closes the substantiation gap on AI-generated approval-probability claims at the root."
  - control: "Add a device-class disclosure-test gate on every campaign before launch; mobile-and-desktop layout review with sign-off on the clear-and-conspicuous read per device class."
    control_type: device-class-disclosure-test
    owner: head-of-marketing-compliance
    rationale: "Closes the mobile-layout-drift failure mode."
  - control: "Add a substantiation-recency control on superlative and comparative claims; the substantiation file must reference the in-scope product and be within 18 months of the asset's first-served date."
    control_type: substantiation-recency-control
    owner: head-of-marketing-compliance
    rationale: "Closes the recycled-substantiation failure mode."

open_legal_questions:
  - "Whether the AI-personalisation pipeline's 'you're 99% likely to be approved' claim, even after correction, supports an FCRA pre-screen offer-of-credit framing or whether it must be restructured."
  - "Whether the firm's CCPA / CPRA disclosure of 'share for cross-context behavioral advertising' can be reconciled with the on-asset 'we will never sell your data' claim through additional on-asset language; counsel direction needed."
  - "Whether the FTC Endorsement Guides apply to any of the warm-list email content where the firm references current-cardholder satisfaction in a way a reasonable consumer might read as a testimonial."

cross_references:
  - udaap-risk-review (chained for the AI-personalisation pipeline review)
  - fair-lending-test-plan (chained for the lookalike-audience-source-affluent-segment review)
  - complaint-theme-analysis (post-launch monitoring on the four named complaint codes)

decision_forum:
  named_forum: marketing-compliance-committee (joint with CCO and counsel for the AI-personalisation finding)
  decision_status: submitted
  decision_date: ""
  conditions: ["AI-personalisation kill-switch executed before launch decision; mobile-layout edit closed before launch decision"]

source_trace_and_confidence:
  - {claim: "trigger-term-driven additional disclosures required on web hero", source: references/source-anchors.md (Reg Z 1026.16 anchor), confidence: high}
  - {claim: "AI-generated approval-probability claim is deception under §1031", source: references/source-anchors.md (CFPB UDAAP module; FTC Policy Statement on Deception; April 2023 Joint Statement), confidence: high}
  - {claim: "superlative substantiation must be current and methodology-disclosed", source: references/source-anchors.md (FTC Policy Statement on Deception; FTC enforcement themes on superlative claims), confidence: high}
  - {claim: "CCPA / CPRA 'share' is broader than marketing 'sell'", source: references/source-anchors.md (state privacy law landscape anchor), confidence: medium}
  - confidence_label: medium-high (strong on the asset-level findings; medium on the state-privacy-law reconciliation pending counsel direction)
```

## What this memo does and does not do

The memo operationalises the pre-launch marketing-claim review for the marketing-compliance committee. It does not approve the campaign for launch, take down any live asset (the campaign is pre-launch), finalise the UDAAP determination on the AI-personalisation pipeline (chained to `udaap-risk-review`), or finalise the privacy-claim accuracy decision on the "we will never sell your data" representation (open legal question for counsel).

The asset-level findings are the work product. The marketing-compliance committee decides on the recommended edits and the kill-switch (the AI-personalisation kill-switch is recommended); the CCO and counsel decide on the chained UDAAP and privacy questions; the conduct committee gets a read on the AI-personalisation finding because the pipeline-level finding is a conduct-event candidate.

Pattern derived from public CFPB and FTC enforcement themes on credit-card marketing, on AI-generated marketing claims, and on the gap between marketing voice and CCPA / CPRA disclosure voice. No named institution is implied; the campaign structure (multi-channel; warm-list email; AI-personalised landing page; lookalike-audience paid social) is the structural pattern, not a specific firm.
