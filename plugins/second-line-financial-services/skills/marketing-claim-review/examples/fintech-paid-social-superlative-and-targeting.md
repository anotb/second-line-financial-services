# Example: in-market sweep of a fintech personal-loan acquisition funnel with AI-rotated creative and lookalike-audience targeting

## Input

A fintech personal-loan provider operates a paid-social acquisition funnel through Meta and TikTok. The funnel uses lookalike-audience targeting (lookalike sources: current borrowers; high-intent leads; converted-applicants). Creative variants rotate via an AI-rotation engine that selects from a pool of 30+ headline-image combinations per audience based on observed engagement. Marketing copy themes include "approval in 60 seconds", "no fees, ever", and creator-affiliate placements with three named creators on TikTok. The product is offered through a sponsor-bank arrangement; the bank is the creditor of record.

A complaint cluster has surfaced in the firm-direct complaint channel and in CFPB-portal complaints on "fees not disclosed" and "credit not as advertised". The fintech's CCO and the sponsor-bank's consumer-compliance officer commission a joint in-market sweep. Source posture is public-plus-firm-policy-plus-evidence; sponsor-bank counsel directs.

## Why this scenario matters

This is a recurring fintech in-market sweep fact pattern: AI-rotated creative variants where substantiation per served variant is the discipline; superlative claim with a fee-disclosure conflict; lookalike-audience targeting with a fair-lending distribution angle; creator-affiliate placements with FTC Endorsement Guides applicability; sponsor-bank attribution. The complaint cluster is the trigger.

## Output sketch

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
  - {claim: "FTC Endorsement Guides require clear-and-conspicuous material-connection disclosure", source: references/source-anchors.md (Endorsement Guides anchor); references/sector-overlays/payments-fintech.md, confidence: high}
  - {claim: "lookalike-audience-source skew raises ECOA / Reg B §1002.4(b) theory", source: references/source-anchors.md (ECOA / Reg B anchor; April 2023 Joint Statement), confidence: medium-high}
  - {claim: "cookie-banner asymmetric choice and pre-checked opt-ins are dark-pattern privacy findings", source: references/cross-cutting/privacy.md; references/source-anchors.md (FTC dark-pattern report; state privacy law landscape), confidence: high}
  - confidence_label: high (asset-level findings) / medium-high (cross-campaign findings pending fair-lending distribution test)
```

## What this memo does and does not do

The memo operationalises the in-market sweep for the joint marketing-compliance committee. It does not approve any of the assets to remain live (the kill-switch and edit recommendations frame the committee decision); it does not execute the recommended edits (the named owners do); it does not run the fair-lending distribution test (chained to `fair-lending-test-plan`); it does not finalise state-AG exposure or the lookalike-audience-source legal question (open for counsel).

The asset-level findings are the work product. The joint marketing-compliance committee decides on the kill-switch and edits; counsel decides on the open legal questions; the fair-lending committee receives the cross-referenced distribution-test request; the conduct committee receives the read because the pattern is a campaign-level conduct-risk signal feeding back from the complaint cluster that triggered the sweep.

Pattern derived from public FTC enforcement themes on dark-pattern consent flows, public CFPB observations on BNPL and small-dollar credit marketing, and the FTC Endorsement Guides framework for influencer marketing. No named institution is implied; the funnel structure (lookalike-audience targeting; AI-rotated creative; creator-affiliate placements; sponsor-bank attribution) is the structural pattern, not a specific firm.
