# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## credit-card-prelaunch-mobile-disclosure

### Example: pre-launch marketing-claim review of a credit-card rewards campaign with an AI-personalised landing page

#### Input

A national credit-card issuer is launching a new rewards card. The pre-launch marketing campaign covers: a hero web page; three paid-social variants (Meta and TikTok); two pre-approval emails to a warm-list audience; an AI-personalised landing page where the rewards-bonus headline is generated from a small set of input variables (current cardholder relationship; spending category mix; tenure). The marketing-compliance committee has scheduled a launch decision in two weeks. The CCO requests a second-line marketing-claim review memo for the committee read.

Source posture is public-plus-firm-policy-plus-evidence. Counsel directs the review for privilege.

#### Why this scenario matters

This is a structurally common pre-launch fact pattern: multi-channel campaign; warm-list email; AI-personalised landing page; trigger-term-driven Reg Z disclosures with mobile-vs-desktop layout drift; superlative claim; foreign-transaction-fee disclosure mechanic; privacy-claim adjacency to CCPA / CPRA disclosures. The memo has to handle the per-asset claim register (each variant served), the device-class capture of disclosure layout, and the AI-content review on the personalised variants.

#### Output sketch

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

#### What this memo does and does not do

The memo operationalises the pre-launch marketing-claim review for the marketing-compliance committee. It does not approve the campaign for launch, take down any live asset (the campaign is pre-launch), finalise the UDAAP determination on the AI-personalisation pipeline (chained to `udaap-risk-review`), or finalise the privacy-claim accuracy decision on the "we will never sell your data" representation (open legal question for counsel).

The asset-level findings are the work product. The marketing-compliance committee decides on the recommended edits and the kill-switch (the AI-personalisation kill-switch is recommended); the CCO and counsel decide on the chained UDAAP and privacy questions; the conduct committee gets a read on the AI-personalisation finding because the pipeline-level finding is a conduct-event candidate.

Pattern derived from public CFPB and FTC enforcement themes on credit-card marketing, on AI-generated marketing claims, and on the gap between marketing voice and CCPA / CPRA disclosure voice. No named institution is implied; the campaign structure (multi-channel; warm-list email; AI-personalised landing page; lookalike-audience paid social) is the structural pattern, not a specific firm.

## fintech-paid-social-superlative-and-targeting

### Example: in-market sweep of a fintech personal-loan acquisition funnel with AI-rotated creative and lookalike-audience targeting

#### Input

A fintech personal-loan provider operates a paid-social acquisition funnel through Meta and TikTok. The funnel uses lookalike-audience targeting (lookalike sources: current borrowers; high-intent leads; converted-applicants). Creative variants rotate via an AI-rotation engine that selects from a pool of 30+ headline-image combinations per audience based on observed engagement. Marketing copy themes include "approval in 60 seconds", "no fees, ever", and creator-affiliate placements with three named creators on TikTok. The product is offered through a sponsor-bank arrangement; the bank is the creditor of record.

A complaint cluster has surfaced in the firm-direct complaint channel and in CFPB-portal complaints on "fees not disclosed" and "credit not as advertised". The fintech's CCO and the sponsor-bank's consumer-compliance officer commission a joint in-market sweep. Source posture is public-plus-firm-policy-plus-evidence; sponsor-bank counsel directs.

#### Why this scenario matters

This is a recurring fintech in-market sweep fact pattern: AI-rotated creative variants where substantiation per served variant is the discipline; superlative claim with a fee-disclosure conflict; lookalike-audience targeting with a fair-lending distribution angle; creator-affiliate placements with FTC Endorsement Guides applicability; sponsor-bank attribution. The complaint cluster is the trigger.

#### Output sketch

```yaml
review_id: MCR-2026-FT-PL-INMARKET-SWEEP-01
trigger: post-complaint-trigger
as_of_date: 2026-05-06
unit_of_analysis: single-campaign
campaign_id: FT-PL-2026-PAID-SOCIAL-FUNNEL
period_in_market: {start: 2026-01-01, end: 2026-04-30}
channels_in_scope: [paid-social, landing-page]

scope:
  sector_overlay_set: [payments-fintech]
  cross_cutting_overlay_set: [conduct, privacy]
  source_posture: public-plus-firm-policy-plus-evidence
  sampling_basis: risk-based-sample
  sampling_frame_description: >
    Of ~30 served variants per audience, sample 3 highest-impression variants per
    audience plus all variants in the audiences with elevated complaint volume.
    Total 24 variants reviewed across 8 audience segments.
  exclusions:
    - The application-page disclosure (separate review with sponsor-bank consumer-compliance)
    - The post-application servicing communication (out of scope)
    - Underwriting fairness testing (separate fair-lending-test-plan)

reviewer_posture:
  reviewer_role: joint-with-sponsor-bank
  review_independence: independent-second-line (joint)
  counsel_directing: true
  legal_privilege_posture: attorney-client-privileged

asset_register:
  (24 variant entries omitted for brevity; see /reviews/2026/FT-PL-INMARKET/asset-register.csv)
  representative entries:
  - asset_id: FT-PL-META-VAR-007
    channel: paid-social
    audience: lookalike-source-current-borrowers
    version: 7 (AI-rotated; engagement-selected)
    dates_in_market: {start: 2026-02-15, end: 2026-04-30}
    device_classes_captured: [mobile]
    screenshot_reference: /reviews/2026/FT-PL-INMARKET/meta-var-007.png
  - asset_id: FT-PL-TIKTOK-CREATOR-A-VAR-3
    channel: paid-social
    audience: tiktok-broad-acquisition-25-34
    version: 3 (AI-rotated)
    dates_in_market: {start: 2026-03-01, end: 2026-04-30}
    device_classes_captured: [mobile]
    screenshot_reference: /reviews/2026/FT-PL-INMARKET/tiktok-creator-a-var-3.mp4
  - asset_id: FT-PL-LANDING-COOKIE-BANNER
    channel: landing-page
    audience: all-incoming-traffic
    version: 1.0
    dates_in_market: {start: 2026-01-01, end: 2026-04-30}
    device_classes_captured: [desktop, mobile]
    screenshot_reference: /reviews/2026/FT-PL-INMARKET/landing-cookie-banner-{desktop,mobile}.png

per_asset_findings:
  FT-PL-META-VAR-007:
    claim_register:
      - claim_text: "Approval in 60 seconds"
        category: time-to-funding
        substantiation_status: partially-substantiated
        substantiation_source: internal-data
        date: 2026-02-01
        notes: "Median approval time is 73 seconds; 60 seconds is the 25th percentile."
      - claim_text: "No fees, ever"
        category: fee
        substantiation_status: not-substantiated
        substantiation_source: ""
        date: 2026-05-06
        notes: "The product cardholder agreement discloses a late-payment fee and a returned-payment fee."
    udaap_findings:
      - prong: deception
        claim_or_element: "no fees, ever"
        reasoning: >
          The on-asset claim is materially inconsistent with the cardholder agreement
          disclosure of late-payment and returned-payment fees. A reasonable consumer
          reading the asset would understand "no fees, ever" as inclusive of
          delinquency-related fees; the materiality is high because fee mechanics
          drive cost-of-credit understanding.
        severity: high

  FT-PL-TIKTOK-CREATOR-A-VAR-3:
    claim_register:
      - claim_text: "(creator) shares why this is the personal loan she recommends to friends"
        category: endorsement
        substantiation_status: partially-substantiated
        substantiation_source: third-party-study
        date: 2026-02-01
        notes: "Creator agreement discloses material connection in the creator's profile, but the on-asset 'sponsored' label is below the fold and the creator's verbal disclosure occurs at second 28 of a 30-second video."
    udaap_findings:
      - prong: deception
        claim_or_element: endorsement disclosure timing and prominence
        reasoning: >
          The FTC Endorsement Guides require clear-and-conspicuous disclosure of
          material connections. The on-asset disclosure (sponsored label below the
          fold; verbal disclosure at second 28 of 30) does not meet the clear-and
          -conspicuous standard for the platform; most viewers will not see the
          disclosure before forming an impression.
        severity: medium

  FT-PL-LANDING-COOKIE-BANNER:
    privacy_findings:
      - category: dark-pattern-privacy
        claim_or_element: cookie-banner consent flow
        reasoning: >
          The banner uses asymmetric button weight ("Accept all" is full-width
          coloured CTA; "Manage preferences" is a small text link). The accept-all
          path is a single click; the reject path requires navigating to the
          preference center, unchecking three pre-checked categories, and clicking
          save. Pre-checked opt-ins on three categories at the preference center
          (analytics, advertising, personalisation) violate the symmetric-choice
          expectation under the FTC dark-pattern catalog and the CCPA / CPRA
          dark-pattern prohibition.
    dark_pattern_findings:
      - taxonomy_entry: interface-interference (asymmetric choice)
        location_in_asset: cookie banner; first interaction on landing page
        consumer_harm_hypothesis: >
          Consumers are channeled into accepting consent they would not provide
          under symmetric choice; the data collected enables additional targeting
          and personalisation downstream.
        severity: high
      - taxonomy_entry: forced-action (pre-checked opt-ins on the preference center)
        location_in_asset: cookie-banner preference center
        consumer_harm_hypothesis: >
          Consumers reaching the preference center face the consent-by-default
          state on three categories; the design takes advantage of friction to
          maintain consent.
        severity: medium

cross_campaign_findings:
  fair_lending_distribution_and_targeting:
    - finding: lookalike-audience source review
      category: targeting-parameter
      channel: paid-social (Meta)
      geographic_scope: national
      audience_targeting_parameters: >
        Lookalike-source = current borrowers; the source population's geographic
        distribution skews toward MSAs with elevated minority-population shares.
        Preliminary BISG-derived audience-share estimates suggest elevated
        minority-population exposure in the lookalike audience compared to the
        general-population baseline.
      protected_class_implication: >
        ECOA / Reg B §1002.4(b) discouragement is the operative theory if the
        lookalike-audience design materially over-or-under-concentrates marketing
        on protected classes in a way that affects application-volume disparity.
        FHA §3604(c) is not in play here (personal-loan product; not dwelling
        related).
      ai_personalisation_in_path: yes (AI-rotation engine selects creative variants)
      cross_reference_to_fair_lending_test_plan: yes
      cross_reference_note: >
        Distribution-test specification needed; this asset-level review flags the
        finding, the test plan operationalises the disparity test. Cite April 2023
        Joint Statement on the algorithmic-targeting framing.

  ai_content_review:
    ai_in_path: true
    rotation_engine: AI-CREATIVE-ROTATE-v2
    variants_in_pool: ~30 per audience segment; ~240 total served
    output_review_status: pre-pool review at variant-creation time; no post-rotation review of which variants are served at scale
    fabrication_risk: low (variants are pre-approved; the rotation does not generate new claim text)
    privacy_implication: addressed in cookie-banner privacy-findings
    joint_statement_cite: true

edits_requested:
  - edit: "Pull the 'no fees, ever' creative variants from rotation immediately; reconcile fee claims across all variants and re-substantiate or revise."
    owner: head-of-marketing-compliance (fintech); sponsor-bank-marketing-compliance
    due_date: 2026-05-15
    severity: high
    kill_switch_candidate: yes
  - edit: "Re-design the cookie banner to symmetric choice (equivalent visual weight on accept and reject; one-click reject; no pre-checked opt-ins on the preference center). Re-test against CCPA / CPRA dark-pattern prohibition before re-deployment."
    owner: head-of-product (fintech); head-of-privacy
    due_date: 2026-05-30
    severity: high
    kill_switch_candidate: no
  - edit: "Revise creator-affiliate content to meet FTC Endorsement Guides clear-and-conspicuous standard: sponsorship disclosure in first three seconds of video; on-screen text disclosure visible throughout; verbal disclosure repeated."
    owner: head-of-creator-marketing
    due_date: 2026-05-30
    severity: medium
    kill_switch_candidate: no
  - edit: "Revise 'approval in 60 seconds' claim to align with median approval time, or restructure to a representative-time framing (e.g., 'most applicants approved within 90 seconds')."
    owner: head-of-marketing
    due_date: 2026-05-30
    severity: medium
    kill_switch_candidate: no

requested_controls:
  - control: "Fair-lending-aware lookalike-audience design control: lookalike-source review with audience-distribution audit before audience activation."
    control_type: marketing-review-gate
    owner: head-of-marketing-compliance; head-of-fair-lending
    rationale: "Closes the algorithmic-targeting concentration risk at the audience-design step rather than after the fact."
  - control: "Per-served-variant substantiation control on the AI-rotation engine: variants in the pool must carry substantiation that travels with the variant; rotation does not create new substantiation gaps."
    control_type: ai-personalisation-review
    owner: head-of-marketing-compliance
    rationale: "Closes the substantiation drift across rotated variants."
  - control: "Creator-affiliate disclosure-design control: every creator content piece reviewed for FTC Endorsement Guides clear-and-conspicuous standard before live."
    control_type: marketing-review-gate
    owner: head-of-creator-marketing; head-of-marketing-compliance
    rationale: "Closes the per-platform disclosure-mechanic gap."
  - control: "Symmetric-choice consent-design control: every consent flow reviewed for symmetric choice and absence of pre-checked opt-ins."
    control_type: dark-pattern-design-review
    owner: head-of-privacy; head-of-design
    rationale: "Closes the dark-pattern-privacy fact pattern at the design root."

open_legal_questions:
  - "Whether state-AG enforcement under state baby-FTC acts is a plausible exposure on the 'no fees, ever' fact pattern in any program state, particularly where the state has issued recent dark-pattern enforcement guidance."
  - "Whether the lookalike-audience source-of-truth selection (current borrowers; high-intent leads; converted applicants) is itself the fair-lending finding, or whether the finding turns on the distribution audit downstream."
  - "Whether the creator-affiliate framework requires the creator to make an additional disclosure on the creator's own profile in addition to the on-asset disclosure for the sponsored content."

cross_references:
  - udaap-risk-review (for the product-level UDAAP read on the fee-mechanic disclosure)
  - fair-lending-test-plan (for the lookalike-audience distribution test)
  - complaint-theme-analysis (the underlying trigger for this sweep; close the loop)
  - llm-vendor-evidence-review (where the AI-rotation-engine vendor relationship needs additional governance review)

decision_forum:
  named_forum: joint marketing-compliance committee (sponsor bank and fintech) with conduct committee read
  decision_status: submitted
  decision_date: ""
  conditions: []

source_trace_and_confidence:
  - {claim: "'no fees, ever' is materially inconsistent with cardholder agreement", source: references/source-anchors.md (CFPB UDAAP module; FTC Policy Statement on Deception), confidence: high}
  - {claim: "FTC Endorsement Guides require clear-and-conspicuous material-connection disclosure", source: references/source-anchors.md (Endorsement Guides anchor); references/sector-overlays.md#payments-fintech, confidence: high}
  - {claim: "lookalike-audience-source skew raises ECOA / Reg B §1002.4(b) theory", source: references/source-anchors.md (ECOA / Reg B anchor; April 2023 Joint Statement), confidence: medium-high}
  - {claim: "cookie-banner asymmetric choice and pre-checked opt-ins are dark-pattern privacy findings", source: references/cross-cutting.md#privacy; references/source-anchors.md (FTC dark-pattern report; state privacy law landscape), confidence: high}
  - confidence_label: high (asset-level findings) / medium-high (cross-campaign findings pending fair-lending distribution test)
```

#### What this memo does and does not do

The memo operationalises the in-market sweep for the joint marketing-compliance committee. It does not approve any of the assets to remain live (the kill-switch and edit recommendations frame the committee decision); it does not execute the recommended edits (the named owners do); it does not run the fair-lending distribution test (chained to `fair-lending-test-plan`); it does not finalise state-AG exposure or the lookalike-audience-source legal question (open for counsel).

The asset-level findings are the work product. The joint marketing-compliance committee decides on the kill-switch and edits; counsel decides on the open legal questions; the fair-lending committee receives the cross-referenced distribution-test request; the conduct committee receives the read because the pattern is a campaign-level conduct-risk signal feeding back from the complaint cluster that triggered the sweep.

Pattern derived from public FTC enforcement themes on dark-pattern consent flows, public CFPB observations on BNPL and small-dollar credit marketing, and the FTC Endorsement Guides framework for influencer marketing. No named institution is implied; the funnel structure (lookalike-audience targeting; AI-rotated creative; creator-affiliate placements; sponsor-bank attribution) is the structural pattern, not a specific firm.

## troubleshooting

### Troubleshooting: marketing-claim-review

Recurring failure modes when a marketing-claim review memo looks complete but is not. The drafter should preempt these; the decision-forum reviewer (marketing-compliance committee, CCO, conduct-risk lead, counsel) should catch the rest.

#### The disclosure was reviewed on desktop and not on mobile

Symptom: the memo records the disclosure adequacy read against the desktop layout and the asset is approved; the mobile layout drifts the trigger-term-driven additional disclosures below the fold and the disclosure is no longer clear-and-conspicuous on the actual served device.

Why it happens: the marketing brief and the design files are in desktop-resolution; the reviewer reads what is in front of them. The clear-and-conspicuous standard runs by device class.

Fix: the asset register names the device classes captured per asset; the disclosure adequacy block records the disclosure location per device class; the device-class-delta column is populated and a non-trivial delta surfaces a mobile-layout finding. Add a device-class disclosure-test control to the requested controls.

#### A substantiation file is treated as substantiation

Symptom: the per-claim substantiation column is filled with "MAP file 234"; the file is from a different campaign, an earlier product version, or a study that does not support the in-scope claim.

Why it happens: substantiation files are reused across campaigns without per-claim review; the MAP record system records that a file exists, not whether it supports the specific claim.

Fix: per-claim source-of-substantiation field with date is populated and read; substantiation must reference the in-scope product and be within a reasonable currency window for the claim category. Add a substantiation-recency control to the requested controls.

#### AI-personalised or AI-generated copy is treated as out of scope

Symptom: the per-asset claim register reads against the brief; the AI block is empty or marked `ai_in_path: false`. The actual displayed claim on the served variant is different from the brief; or the claim is a personalised assertion fabricated by the headline-generation pipeline.

Why it happens: drafters treat AI personalisation as a model-risk question rather than a marketing-claim question. The bureau and the FTC have been explicit that UDAAP / UDAP authority reaches the displayed claim; novel technology is not a defence.

Fix: when AI is in the production path or the personalisation path, the AI-content review block fires; per-served-variant review and per-variant substantiation are the discipline. The April 2023 Joint Statement is cited from `references/source-anchors.md`. Where the personalisation pipeline asserts a probability, eligibility, or other claim that is not connected to a model output supporting the assertion, the finding is fabrication and the kill-switch is the immediate remediation.

#### Fair-lending distribution and targeting treated as not-applicable to marketing

Symptom: the fair-lending distribution-and-targeting block is empty or marked `n-a`. The asset is a personal-loan or credit-card or BNPL marketing campaign; the audience-targeting parameters include lookalike-audience seeds, ZIP-based targeting, or interest-category combinations.

Why it happens: drafters scope fair-lending to underwriting and pricing; ECOA / Reg B §1002.4(b) discouragement and FHA §3604(c) discriminatory advertising on dwelling-related products are treated as edge cases.

Fix: the fair-lending distribution-and-targeting block is populated for any product that ECOA / FHA touches; the block records the audience-targeting parameters, the channel skew, and the protected-class implication. Where the finding raises a parallel disparity-test question, cross-reference `fair-lending-test-plan`.

#### Privacy claims are reviewed against the privacy notice only

Symptom: the on-asset privacy claim ("we will never sell your data") is checked against the firm's GLBA / Reg P privacy notice; the AdChoices representation, the dark-pattern privacy fact patterns, and the state-privacy-law (CCPA / CPRA) interaction are not addressed.

Why it happens: privacy review is treated as a matter of notice-content compliance; the state-law surface and the dark-pattern surface expand the analysis but are not always loaded.

Fix: load the privacy cross-cutting overlay on every digital-channel review. The on-asset privacy claim is read against the privacy notice, the AdChoices representation (if in play), the dark-pattern privacy fact patterns, the state-privacy-law footprint, and (where AI is in path) the AI-personalisation privacy implication.

#### Dark-pattern findings written as "the UX is confusing"

Symptom: the dark-pattern findings block lists "the consent flow is confusing" or "the cancellation path is unclear" without naming a taxonomy entry, the location in the asset, or the consumer-harm hypothesis.

Why it happens: drafters treat dark patterns as a UX-quality issue rather than a regulatory finding under existing UDAAP / UDAP authority.

Fix: each dark-pattern finding names the FTC dark-pattern catalog entry (nagging, obstruction, sneaking, interface interference, forced action, social-proof manipulation, asymmetric choice, hidden subscription, confirmshaming, or other), the location in the asset, and the consumer-harm hypothesis. "The cookie banner uses interface-interference (asymmetric button weight; pre-checked accept; reject path requires three additional clicks) at the first interaction on the landing page; consumers are channeled into accepting consent they would not provide under symmetric choice" is a finding. "The UX is confusing" is not.

#### Asset-level UDAAP findings are conflated with product-level UDAAP findings

Symptom: the memo's UDAAP findings block reads as a product-level UDAAP review; the population estimate covers the product, not the served-asset audience; the abusiveness analysis runs on the fee mechanic rather than on the asset's representation of the fee mechanic.

Why it happens: drafters treat UDAAP as one analysis regardless of unit; the product-level review and the asset-level review are conflated.

Fix: asset-level UDAAP findings are scoped to the displayed asset (the deception in the served claim; the unfairness in the asset's misrepresentation of cost; the abusiveness in the asset's dark-pattern design). Where the asset-level finding chains to a product-level UDAAP read, the cross-reference to `udaap-risk-review` is named; the product-level analysis lives there, not in this memo.

#### Endorsement disclosures reviewed against firm policy only

Symptom: the creator-affiliate or influencer placement is reviewed against the firm's material-connection disclosure policy (sponsorship label is present); the disclosure timing, placement, and platform-specific mechanics are not addressed against the FTC Endorsement Guides framework.

Why it happens: drafters check for the presence of a sponsorship label and stop; the channel-specific Endorsement Guides expectations are not loaded.

Fix: per-platform Endorsement Guides review is part of the endorsement-claim block; sponsorship disclosure timing, placement (above-the-fold; first-three-seconds for video), prominence, and verbal-vs-visual mechanics are read. The 2023 Endorsement Guides revisions [verify exact treatment of AI-generated endorsements] address synthetic-content elements and should be loaded where AI-generated avatars or testimonials are in play.

#### Kill-switch is treated as outside the memo's scope

Symptom: the recommended edits block lists revisions but no asset is marked as a kill-switch candidate; assets with critical findings (fabricated claims; clear-and-conspicuous failures on operative disclosures; FDIC-insurance misrepresentation; sensitive-attribute targeting findings) remain in market pending edit.

Why it happens: drafters treat the kill-switch as a takedown decision reserved for the committee; the memo does not flag candidates.

Fix: the kill-switch column on the recommended-edits block is populated; assets with critical findings are flagged as kill-switch candidates with rationale. The committee decides on the takedown; the memo names the candidates so the committee has the asset-level finding in front of it.

#### "We will never sell your data" claim not reconciled with state-privacy-law disclosures

Symptom: the privacy-claim block records the on-asset claim and notes that the privacy notice is consistent; the firm's CCPA / CPRA Notice at Collection discloses "share for cross-context behavioral advertising" which is broader than the marketing voice's "sell" but the gap is not addressed.

Why it happens: the marketing voice and the legal voice operate on different vocabularies; the gap is treated as a vocabulary issue rather than a deception finding.

Fix: the on-asset privacy claim is read against the firm's CCPA / CPRA disclosures and the actual data-flow practice; the gap between marketing voice and state-law disclosure voice is named and surfaced as a deception finding or as an open legal question for counsel.

#### Sponsor-bank arrangement treated as the program-operator's marketing review

Symptom: the asset bears the sponsor bank's name or logo; the review is conducted by the program-operator's marketing-compliance function only; the sponsor-bank consumer-compliance officer does not see the memo until after launch.

Why it happens: the program operator owns the marketing function operationally; the sponsor bank is treated as a passive recipient.

Fix: where the asset bears the bank's name or logo, joint review and joint approval are the discipline. The reviewer-and-review-posture block records `joint-with-sponsor-bank` or names the joint review structure; the recommended edits and the kill-switch decisions are joint between the marketing-compliance functions and the sponsor-bank consumer-compliance function.

#### Source trace and confidence label absent

Symptom: the memo cites no sources for findings. Element-test conclusions appear without citation; substantiation conclusions appear without source; the privacy-claim findings appear without citation to the privacy notice or to the operative state law.

Why it happens: the drafter borrowed from prior memos or from external references without recording the source.

Fix: every material claim cites a source from `references/source-anchors.md` (or a loaded overlay) by file path. Source evidence (the served asset; the substantiation file; the MAP record), management assertions (the marketing-team brief), public-source obligations (the operative regulation), generated inferences (the reviewer's read), and open legal questions stay distinguishable. The confidence label at the end reflects how well the memo supports the recommended decision.

#### Capital-markets or insurance asset routed into this skill in error

Symptom: the memo is reviewing an investment-adviser performance advertisement, a FINRA broker-dealer communication, or a life-insurance advertising asset and applying Reg Z and UDAAP framing to it.

Why it happens: the drafter loaded the wrong skill; the consumer-financial UDAAP / Reg Z lane is not the SEC Marketing Rule, FINRA Rule 2210, or NAIC Model #570 lane.

Fix: route to the firm's investment-adviser compliance, broker-dealer compliance, or insurance-conduct function. The boundary skill in `marketing-rule-evidence` is the closer-fit surface inside this repo for the SEC investment adviser Marketing Rule lane. The capital-markets and insurance sector overlays in this skill name the boundary explicitly; check the overlay before drafting.

#### Decision forum is unnamed

Symptom: the memo is fully drafted, the recommendations are well-specified, and there is no record of which forum decides on the edits and the kill-switch.

Why it happens: the drafter treated the memo as the work product itself rather than as the input to a decision-forum gate.

Fix: `decision_forum.named_forum` is filled. The memo is in `draft` until the named forum decides; the edit execution and the kill-switch begin once the gate clears (or earlier where counsel directs an interim posture on a critical finding).
