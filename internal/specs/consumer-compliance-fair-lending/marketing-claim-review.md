# marketing-claim-review — Phase 1 spec sheet

Date: 2026-05-06
Plugin: consumer-compliance-fair-lending
Phase: 1 (per-skill scoping; no SKILL.md content)

## Activation-tuned description

Reviews consumer-financial marketing material (web, in-app, email, push, paid social, digital display, broadcast, print, scripts, MAP / call-center) for claim substantiation, MAPR / APR / fee disclosure adequacy, dark-pattern presence, fair-lending distribution / targeting, privacy claim accuracy, and UDAAP triggers. Produces a second-line review memo with claim-level findings, requested edits, controls observations, and escalations.

Best for:
- Pre-launch second-line review of a marketing campaign for a consumer-financial product (deposit, credit card, mortgage, BNPL, personal loan, auto, small business).
- Periodic in-market sweep of live marketing inventory — particularly where the firm is post-consent-order or post-MRA on marketing.
- Targeted review after a complaint theme on disclosure or "fees not disclosed" (cross-reference complaint-theme-analysis).
- Review of AI-generated marketing copy or AI-personalized landing pages (claim substantiation, accuracy, privacy implications).

Not the right tool when:
- The question is the adverse action notice (use adverse-action-review).
- The question is fair-lending statistical testing of marketing distribution (use fair-lending-test-plan; this skill flags distribution concerns, the plan operationalizes them).
- The question is a UDAAP risk rating on the product overall (use udaap-risk-review; this skill is asset-by-asset).
- The question is small-business 1071 data submission (use section1071-readiness).

Anchored to: UDAAP — Dodd-Frank §1031 / §1036 (12 U.S.C. §5531 / §5536); CFPB UDAAP Examination Manual (current edition); Truth in Lending / Regulation Z 12 CFR 1026 advertising rules — 1026.16 (open-end), 1026.24 (closed-end), 1026.40 (HELOC), 1026.60 (credit and charge card applications and solicitations); TILA-RESPA Integrated Disclosures (TRID) 12 CFR 1026.37 / 1026.38 — disclosure form mechanics where marketing previews terms; Military Lending Act / 32 CFR 232 MAPR disclosure where consumer is covered borrower; ECOA / Reg B 12 CFR 1002.4(b) (discouragement) — marketing that discourages applications on a prohibited basis; Fair Housing Act §3604(c) — discrimination in advertising of dwellings; FTC Endorsement Guides 16 CFR 255 (where applicable to non-bank fintech); GLBA Privacy Rule 16 CFR 313 / Reg P 12 CFR 1016 — privacy notice and use claims; CFPB / FTC / DOJ / EEOC Joint Statement (April 2023) where AI personalization touches protected-class steering or algorithmic discrimination; CFPB guidance on dark patterns in digital marketing [verify specific bulletin / circular].

## Source anchors

- UDAAP — Dodd-Frank §1031 / §1036 (12 U.S.C. §5531 / §5536); CFPB UDAAP Examination Manual (current edition) [verify edition date] — deception, unfairness, abusiveness with marketing-relevant fact patterns.
- Regulation Z 12 CFR 1026.16 — open-end credit advertising rules; trigger terms and required disclosures.
- Regulation Z 12 CFR 1026.24 — closed-end credit advertising rules; clear and conspicuous standard; trigger terms.
- Regulation Z 12 CFR 1026.40 — HELOC advertising rules.
- Regulation Z 12 CFR 1026.60 — credit and charge card applications and solicitations (Schumer box equivalents and required disclosures in solicitation).
- TILA-RESPA Integrated Disclosures (TRID) 12 CFR 1026.37 / 1026.38 — disclosure mechanics for closed-end mortgage where marketing previews terms.
- Military Lending Act / 32 CFR 232 — MAPR disclosure where consumer is a covered borrower; identification of covered borrower.
- ECOA / Reg B 12 CFR 1002.4(b) — prohibition on discouraging applications on a prohibited basis.
- Fair Housing Act 42 U.S.C. §3604(c) — making, printing, or publishing discriminatory dwelling-related advertising; HUD advertising regulations 24 CFR 109 [verify current text].
- FTC Endorsement Guides 16 CFR 255 — applicable to fintech / non-bank advertising; influencer disclosure.
- GLBA Privacy Rule 16 CFR 313 (FTC) and Regulation P 12 CFR 1016 (CFPB / banking agencies) — privacy notice content; advertising claims about privacy must be accurate.
- AdChoices self-regulatory program — Digital Advertising Alliance (DAA); applicable where the firm participates in interest-based advertising and represents AdChoices compliance.
- CFPB enforcement actions and consent orders on UDAAP marketing deception (used as worked-example anchors).
- CFPB / FTC / DOJ / EEOC Joint Statement (April 25, 2023) — algorithmic targeting that excludes protected classes is enforceable under existing laws.
- CFPB on dark patterns [verify specific reference; the bureau has discussed dark patterns in supervisory highlights and circulars; pin the most recent and named source in phase 2].
- FTC dark patterns reports (e.g., "Bringing Dark Patterns to Light," September 2022) — useful pattern catalog.
- Sector-specific advertising regulators where applicable (FINRA Rule 2210 for broker-dealer; NAIC unfair trade practices for insurance) — flagged but generally out of UDAAP scope.

## Sector overlays needed

- `references/sector-overlays/banking.md` — deposit advertising under 12 CFR 1030 (Reg DD); FDIC insurance advertising 12 CFR 328; CRA-related advertising; mortgage ads under TILA / RESPA / TRID interplay.
- `references/sector-overlays/capital-markets.md` — FINRA Rule 2210 (communications with the public) for broker-dealer advertising; SEC marketing rule for advisers (Rule 206(4)-1) — flagged but usually out of UDAAP / Reg Z scope; included so the reviewer knows when to redirect.
- `references/sector-overlays/payments-fintech.md` — sponsor-bank attribution of marketing claims; CFPB BNPL marketing observations [verify current state]; app-store ad rules; Reg E error-resolution claims in marketing.
- `references/sector-overlays/insurance.md` — bank-affiliated insurance disclosures; NAIC unfair trade practices framework for advertising (state-DOI jurisdiction); flag scope boundary so the reviewer redirects.

## Cross-cutting overlays

- `references/cross-cutting/privacy.md` — privacy claim accuracy under GLBA Privacy Rule (Reg P) and FTC Privacy Rule; AdChoices self-regulatory representation accuracy; dark-pattern privacy (deceptive consent flows, manipulated cookie banners, pre-checked opt-ins, hidden settings); CCPA / CPRA implications for marketing claims about data sale or sharing [verify current state]; treatment of "we will not sell your data" claims and how they map to CCPA's broader definitions; biometric and sensitive-attribute targeting claims.
- (AI-related cross-cutting is implicit where AI is used in copy generation, audience targeting, or personalization. SKILL.md must reference the April 2023 Joint Statement and CFPB circulars on algorithmic discrimination where targeting touches protected classes; substantiation discipline applies to AI-generated copy.)

Conduct not applicable as a primary overlay (overlap with udaap-risk-review). Cyber not applicable as a primary overlay. Climate not applicable.

## Output template named sections

1. Asset register (every reviewed asset with channel, audience, dates, version)
2. Reviewer and review posture (scope, sampling basis if not full review, legal-privilege posture)
3. Per-asset claim register (every claim, with category, substantiation status, source of substantiation)
4. Disclosure adequacy (Reg Z trigger terms, MAPR / APR / fees, TRID-adjacent, MLA where applicable, FDIC insurance, deposit / Reg DD where applicable)
5. Fair-lending distribution / targeting findings (channel skew, geographic distribution, audience-targeting parameters, AI-personalization audit)
6. UDAAP findings (deception, unfairness, abusiveness; with claim and reasoning)
7. Privacy claim findings (GLBA / Reg P, AdChoices, dark-pattern privacy, sensitive-attribute targeting)
8. Dark-pattern findings (taxonomy, location in asset, consumer harm hypothesis)
9. AI-generated content review (where applicable: provenance, substantiation, fabrication risk, personalization)
10. Recommended edits / kill-switch list / requested controls
11. Open legal questions
12. Source trace and confidence label

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| `review_id` | string | Unique reference. |
| `assets[]` | array of objects | One per reviewed asset. |
| `assets[].asset_id` | string | Internal reference. |
| `assets[].channel` | enum | `web`, `in_app`, `email`, `push`, `paid_social`, `digital_display`, `broadcast`, `print`, `script`, `landing_page`, `app_store`, `other`. |
| `assets[].audience` | string | Targeted segment, geography, channel. |
| `assets[].version` | string | Versioning for change tracking. |
| `assets[].claims[]` | array of objects | Per-claim findings. |
| `assets[].claims[].claim_text` | string | As it appears. |
| `assets[].claims[].claim_category` | enum | `rate`, `fee`, `apr_mapr`, `eligibility`, `endorsement`, `comparative_superlative`, `privacy`, `security`, `rewards`, `availability`, `time_to_funding`, `green_or_esg`, `ai_capability`, `other`. |
| `assets[].claims[].substantiation_status` | enum | `substantiated`, `partially_substantiated`, `not_substantiated`, `not_substantiable`, `evidence_needed`. |
| `assets[].claims[].substantiation_source` | string | Internal data, third-party study, regulator data, controlled study, MAP. |
| `assets[].disclosure_findings[]` | array of objects | Reg Z / MLA / TRID / Reg DD / FDIC findings; clear-and-conspicuous assessment. |
| `assets[].fair_lending_findings[]` | array of objects | Distribution / targeting findings; AI-personalization findings. |
| `assets[].udaap_findings[]` | array of objects | UDAAP element (deception / unfairness / abusiveness), reasoning. |
| `assets[].privacy_findings[]` | array of objects | GLBA / Reg P / AdChoices / dark-pattern privacy. |
| `assets[].dark_pattern_findings[]` | array of objects | Taxonomy (FTC dark-pattern catalog), location, harm hypothesis. |
| `assets[].ai_content_review` | object | AI-generated copy / personalization findings. |
| `assets[].edits_requested[]` | array of objects | Edit, owner, due date, severity. |
| `assets[].kill_switch` | bool | Recommend pulling the asset. |
| `legal_privilege_posture` | string | Privilege flag. |
| `open_questions[]` | array of strings | For counsel. |
| `source_trace[]` | array of objects | Claim, source, evidence, confidence. |

## Example scenarios (public-source-derived, anonymous)

1. A national credit-card issuer's pre-launch marketing campaign for a new rewards card. Review of: hero web page, three paid-social variants, two pre-approval emails, an AI-personalized landing page where the rewards-bonus headline is generated from a small set of variables. Findings: rewards bonus headline omits a trigger-term-driven Reg Z 1026.16 disclosure on the variant served to mobile users (clear-and-conspicuous fail); the personalized landing page's "you're 99% likely to be approved" claim is not substantiated (substantiation_status `not_substantiated`); a foreign-transaction fee is disclosed below the fold on mobile; a "we will never sell your data" privacy claim conflicts with the firm's CCPA disclosure of "share for cross-context behavioral advertising" [verify state-specific scope]. Recommended edits: re-layout disclosure on mobile; remove or substantiate the 99% claim; reconcile the privacy claim with CCPA disclosures; add MAP control for AI-personalized claim substantiation.

2. A fintech personal-loan provider's paid-social acquisition funnel uses lookalike audiences and AI-driven creative rotation. In-market sweep finds: a creative variant promising "approval in 60 seconds" runs against an audience defined by ZIP code and interest categories that materially correlate with race and ethnicity (cross-reference fair-lending-test-plan for distribution test); a "no fees, ever" superlative claim omits the late-payment fee disclosed in the cardholder agreement (UDAAP deception finding); a cookie banner uses a pre-checked "accept all" with a non-symmetric "reject" path (dark-pattern privacy finding). Cite-back to April 2023 Joint Statement on algorithmic discrimination for the targeting finding. Recommended edits: pull the creative; restructure audience targeting; rebuild the cookie banner to symmetric choice; add MAP control for superlative claims. (Pattern derived from public FTC dark-pattern enforcement themes and CFPB BNPL marketing observations.)

## Common pitfalls

1. Reviewing copy without reviewing the live asset on each device class. Mobile and desktop disclosures often differ; clear-and-conspicuous lives in layout, not script. Mitigation: review on actual device classes and capture screenshots dated.
2. Treating a substantiation file as substantiation. The file may be old, generic, or from a different campaign. Mitigation: per-claim source-of-substantiation field and date check.
3. Ignoring AI-generated and AI-personalized copy because "the model only personalized it." UDAAP and Reg Z apply to the displayed claim, not the upstream pipeline. Mitigation: AI content review block is mandatory where AI is in the production path.
4. Treating fair-lending as not applicable to marketing. Reg B 1002.4(b) discouragement and FHA §3604(c) cover marketing distribution and content. Mitigation: distribution / targeting block is mandatory for any product that ECOA / FHA touches.
5. Privacy claims reviewed only against the firm's own privacy notice. AdChoices, CCPA / state privacy law, and dark-pattern privacy expand the surface. Mitigation: privacy cross-cutting reference doc is mandatory for digital-channel reviews.
6. Dark-pattern findings written as "the UX is confusing." That is not a regulatory finding. Mitigation: name the dark-pattern taxonomy entry (e.g., FTC catalog: nagging, obstruction, sneaking, interface interference, forced action, social proof manipulation), point to the location in the asset, state the consumer-harm hypothesis.
7. Skill issues a kill switch or finalizes a UDAAP determination. It does not. The skill recommends edits and kill-switch candidates; legal and compliance owners decide.

## Guardrail (mandatory in SKILL.md)

This skill does not approve marketing for launch, finalize UDAAP or fair-lending determinations, take down live marketing assets, or finalize privacy-claim accuracy decisions. It produces review artifacts and surfaces red flags for human decision by qualified compliance, marketing, fair-lending, privacy, and legal reviewers.
