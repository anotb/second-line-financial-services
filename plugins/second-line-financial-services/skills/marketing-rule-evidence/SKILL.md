---
name: marketing-rule-evidence
description: "Build Marketing Rule 206(4)-1 evidence and substantiation for an adviser advertisement."
argument-hint: "[advertisement id or file path; channel; audience; statement-type flags; one-on-one flag; sector and cross-cutting overlay flags]"
---

# Marketing Rule evidence

A Marketing Rule evidence pack is what the second-line compliance team produces so the CCO, the designated reviewer, the marketing-review committee, and (where directing) outside counsel can decide whether the adviser advertisement is fit to disseminate, fit to remain in market, or fit to defend in an examination. The work is per-advertisement and per-claim: each claim is logged with substantiation status and source; each statement type is classified against the named regulatory anchor; the required-disclosures matrix is run against the displayed asset; the testimonial / endorsement and third-party-rating checklists fire where in scope; the hypothetical-performance pre-conditions are applied where in scope; the performance-presentation review reads gross-and-net pairing, the prescribed time periods, methodology, and the predecessor / related / extracted treatment; the books-and-records evidence index closes the pack.

The skill serves both lenses. A 1.5-line embedded marketing-review reviewer inside the adviser's marketing or distribution function uses it to consolidate the pre-dissemination read as the ad moves through copy, design, and channel-launch. A 2-line independent compliance reviewer or CCO uses the same skill to challenge what the first line drafted and to surface the substantiation gaps and recordkeeping holes. The seam between them is the per-claim substantiation source-and-date field, the statement-type classification, and the books-and-records index.

The pack is a draft until the CCO or designated reviewer acts on it. The skill stops at the recommendation. It does not approve dissemination, finalize antifraud determinations, sign the books-and-records artifact, or issue customer-facing actions.

## When to use

Builds a Marketing Rule evidence and substantiation pack for one piece of SEC-registered investment-adviser advertising. Per-advertisement, per-claim review: classify the statement (advertisement, performance presentation, hypothetical, predecessor, related, extracted, model, testimonial, endorsement, third-party rating); map required disclosures by statement type; record the substantiation file claim by claim; run the testimonial / endorsement and third-party-rating compliance checklists; apply the hypothetical-performance pre-conditions; assemble the books-and-records evidence index. The pack is the input to the CCO or designated reviewer's pre-dissemination sign-off; it does not approve dissemination, finalize antifraud determinations, or replace counsel review.

Best for:
- Pre-dissemination review of one piece of adviser marketing (pitch deck, fact sheet, website page, RFP response, social post, recorded webinar, podcast script) before the CCO or designated reviewer signs off.
- Periodic look-back on adviser advertising as part of the annual Rule 206(4)-7 compliance program review, where sampled ads need their evidence files reconstructed.
- Response to a Division of Examinations document request that calls for marketing materials, performance computations, substantiation, disclosures, and the books-and-records artifact under Rule 204-2(a)(11) and (a)(15)-(16).
- The advertisement contains hypothetical performance, predecessor performance, related performance, model performance, extracted performance, testimonials, endorsements, or third-party ratings, where Rule 206(4)-1 imposes specific pre-conditions and required disclosures.

Not the right tool when:
- The artifact is not adviser advertising under Rule 206(4)-1 (broker-dealer communications under FINRA Rule 2210; registered fund prospectuses or supplemental sales literature under Rule 482 and Rule 156; account statements; one-on-one tax discussions excluded from the advertisement definition).
- The objective is to draft new marketing copy. This skill reviews and substantiates existing copy; it does not write the ad.
- The objective is overall compliance program design or annual rule-review scope-setting (use `policy-gap-review` or `adviser-exam-readiness` in this plugin).
- The doctrinal lane is consumer-financial UDAAP under Dodd-Frank §1031 (use `marketing-claim-review`; Marketing Rule lives in the Advisers Act §206 antifraud lane, not UDAAP).

## Ask first

Before drafting, get plain answers. Defaults are fine when an answer is missing; flag the default in the pack.

- What is the unit of analysis. One advertisement (a single asset, possibly across device classes), or one campaign of related assets that share substantiation. Mixed-statement pieces are reviewed as one advertisement with multiple statement-type classifications.
- What channel and audience. Channel drives the recordkeeping format (oral webinar vs. printed pitch deck) and the disclosure-mechanic read. Audience matters because hypothetical-performance pre-conditions ask whether the statement is appropriate for the likely recipients.
- One-on-one or to multiple recipients. The one-on-one carve-out from the advertisement definition is narrow; the carve-out does not extend to hypothetical performance, where the (d)(6) conditions apply regardless of recipient count.
- Source posture. Public-only, public-plus-firm-policy, public-plus-firm-policy-plus-evidence, or connector-aware. Source posture sets what the pack can actually cite (calculation worksheets, written promoter agreements, ineligible-person screening attestations, distribution logs, audience-appropriateness policy text) and what carries `[evidence needed]`.
- Who decides. CCO or designated reviewer for routine pre-dissemination; CCO and counsel for high-severity findings or where the adviser is in active EXAMS or enforcement posture; the deputy responsible for the Rule 206(4)-7 written compliance program where the finding rolls up to the annual review.

When `scope` is supplied, the skill consumes it for institution, persona, source posture, sector overlay set, and cross-cutting overlay set. Otherwise it asks the practitioner the few facts it needs and defaults to public posture if the practitioner declines, noting in the pack that scope was not formalized.

## How the pack gets built

The pack has the same spine across advertisements. A senior reviewer walks it roughly in the order below, but the conversation surfaces sections in whatever order the source material arrives; the per-claim and per-statement-type structure sorts itself.

**Advertisement identification.** Stable ad ID, file path or URL, channel, target audience (retail, qualified client, qualified purchaser, institutional, mixed), languages, dates of intended or actual dissemination, version, and the dissemination-status flag (pre-dissemination, in market, withdrawn, archived). The identification block is what the pack comes back to when a finding refers to "page 12 of the v3 pitch deck"; without it the pack loses the ability to point at the thing being reviewed.

**Statement-type classification.** Every advertisement gets classified against the named regulatory anchor's definitions. The classifications are not mutually exclusive: a single piece of marketing routinely contains a performance presentation, a hypothetical-performance section, a third-party rating logo, and a compensated testimonial in the same artifact. Classify each component; the disclosures matrix and the substantiation file flow from the classifications. Misclassification produces the wrong evidence pack, which is the recurring failure mode in EXAMS sweeps. Where the firm relies on the one-on-one carve-out from the advertisement definition, the pack records the carve-out claim and the basis.

**Required-disclosures matrix.** For each statement-type classification, the matrix records what disclosure is required, where it appears in the artifact (page or screen, above or below the fold, in the testimonial itself or in a footnote, on the slide or in the speaker notes), the exact language or topic, and the citation to the named regulatory anchor. The clear-and-conspicuous standard sits in the layout, not in the script: a disclosure that exists in a footnote when it should be in the testimonial itself is a finding even when the words are present.

**Substantiation file.** Every material claim in the advertisement gets a row: the claim text as it appears (not as it appears in the marketing brief), the claim category, the substantiation status (substantiated, partially-substantiated, not-substantiated, not-substantiable, evidence-needed), the source of substantiation, the date of the source, the fair-and-balanced read, and the reviewer note. A substantiation file from a different campaign is not substantiation; per-claim source-and-date is what catches the recycle. The fair-and-balanced overlay applies even where a claim is technically true; that is the antifraud backbone of the rule.

**Performance-presentation review.** Where the advertisement presents performance, the review reads the gross-and-net pairing (same prominence, same methodology, same time periods), the prescribed time periods (1-, 5-, 10-year unless the portfolio's life is shorter), the calculation methodology, the benchmark selection and rationale, the fees-and-expenses treatment, and (per applicable category) the predecessor portability conditions, the related-performance composite construction, the extracted-performance treatment, and the model-performance basis. The one-on-one to a private-fund-investor exception on net presentation is narrow; misreading it is one of the recurring EXAMS findings.

**Hypothetical-performance pre-conditions.** Where the advertisement contains hypothetical performance (model, backtested, targeted, projected), the (d)(6) pre-conditions apply regardless of audience size. The pack records the audience-appropriateness policy and procedure (does the firm have a written policy specifying that hypothetical performance is appropriate for the audience receiving this ad), whether the criteria-and-assumptions disclosure is present and complete, whether the risks-and-limitations disclosure is present and complete, and the policies-and-procedures pin under the Rule 206(4)-7 written compliance program.

**Testimonial / endorsement checklist.** For each testimonial or endorsement in the advertisement: compensated yes / no; client / non-client status disclosed clearly and prominently in the testimonial itself; material conflicts disclosed; written agreement on file where compensation exceeds the prescribed threshold over the prescribed period; ineligible-person screen run and dated; oversight evidence; recordkeeping pin under the named recordkeeping anchor. The "clearly and prominently" standard reaches the disclosure's location in the testimonial, not just its existence somewhere on the page.

**Third-party-rating checklist.** For each third-party rating in the advertisement: rating provider identity, rating period, methodology disclosure, compensation paid (and to whom), compensation disclosure, reasonable-basis read on the firm's reliance on the rating. Logos and badges count as third-party-rating use; missing the rating disclosures because the use is "just a logo" is a recurring finding.

**Books-and-records evidence index.** The pack assembles the index under the named recordkeeping anchor: the advertisement copy (every version disseminated); the calculation worksheets supporting any performance figure; the written promoter and endorser agreements; the ineligible-person screening attestations; the audience-appropriateness policy; the distribution log (who received it, when, by what channel); the records sufficient to demonstrate compliance for oral advertisements (webinar recording, podcast file, conference-talk outline or transcript). Records that should exist but cannot be produced are flagged as `[evidence needed]` and routed to the recordkeeping owner.

**Reviewer determination, residual issues, escalation.** The reviewer records: name (role, not individual), role, date, status (approved / approved with edits / not approved), residual issues, escalation flag. The CCO sign-off is the named sign-off; counsel sets privilege posture where the pack is dual-purpose or attorney-directed.

**Open legal questions.** Items deferred to counsel: scope of the one-on-one carve-out for a borderline communication; the predecessor-portability conditions where personnel and supporting records are partially carried; the application of the rule's general prohibitions to AI-generated marketing variants; treatment of social-media reposts and influencer arrangements under the testimonial / endorsement framework; the boundary between an "advertisement" and an "extemporaneous oral communication" for a recorded conference Q&A; whether a particular registered fund advertisement routes through Rule 482 / Rule 156 rather than the Marketing Rule (the funded vehicle vs. the adviser as advertiser distinction).

**Recommended remediation, hold list, requested controls.** Each remediation entry names: edit (what changes in the ad copy or layout, or what disclosure gets added), owner role, due date, severity. The hold list names ads the pack recommends pulling from dissemination pending edit (or recommending against initial dissemination for a pre-dissemination review). Requested controls name the marketing-review-gate, the substantiation-recency control, the recordkeeping control, the ineligible-person re-screen cadence, or the audience-appropriateness policy update the pack recommends adding to close the failure mode at the root, not just on the ad under review.

**Source trace and confidence.** Every material claim cites a source from `references/source-anchors.md` (or the relevant overlay) by file path. Source evidence (the served advertisement, the calculation worksheet, the written agreement, the screening attestation), management assertions (the marketing brief, the distribution-team representation), public-source obligations (the operative regulation), generated inferences (the reviewer's read), and open legal questions stay distinguishable. The confidence label at the end reflects how well the pack supports the recommended decision; honest, not aspirational.

### Sector overlay

This skill is sector-unique to SEC-registered investment advisers and the asset-management entities that operate under that regime. The capital-markets sector overlay at `references/sector-overlays.md#capital-markets` carries the adviser-specific mechanics (the Rule 206(4)-7 written compliance program tie-in; the broker-dealer Rule 2210 boundary for dual registrants; the Rule 482 / Rule 156 boundary for registered-fund advertising; the books-and-records discipline under Rule 204-2). No other sector overlay applies; engagements addressing this skill load the capital-markets overlay by default.

### Cross-cutting overlays

Conduct overlay loads where the substantiation gap, the testimonial framing, or the performance presentation crosses the antifraud "fair and balanced" threshold; the file lives at `references/cross-cutting.md#conduct`. Privacy overlay loads where a testimonial discloses client identity or where account-level details appear in the advertisement; client-consent and Reg S-P treatment live at `references/cross-cutting.md#privacy`. Cyber and climate overlays are not in scope by default; load them only where the advertisement makes claims about firm cybersecurity posture or sustainability / climate characteristics, and route to the broader programs.

## Pointers

`references/sector-overlays.md` and `references/cross-cutting.md` hold one section per sector or topic, and `examples.md` one per example. Find the heading and read only that section.

- `references/source-anchors.md` — Marketing Rule citations (Rule 206(4)-1; Rule 204-2 books-and-records; Rule 206(4)-7; Marketing Rule Risk Alerts; FINRA Rule 2210 boundary).
- `references/sector-overlays.md#capital-markets` — adviser-and-asset-manager-specific mechanics (Rule 206(4)-7; Rule 482 / Rule 156 boundary; dual-registrant FINRA Rule 2210 routing; books-and-records discipline).
- `references/cross-cutting.md#conduct` — "fair and balanced" antifraud overlay and the chained-finding posture; `references/cross-cutting.md#privacy` — testimonial-identity and Reg S-P treatment.
- `references/firm-overlay.md` — firm-installed marketing-review committee, marketing-policy, ineligible-person screening process, recordkeeping system-of-record paths (consumed when present).
- `templates/default-output.md` — pack template (named sections, per-claim and per-statement-type fields).
- `examples.md#hypothetical-performance-pitch-deck`, `examples.md#compensated-website-testimonial` — public-source-derived worked examples.
- `examples.md#troubleshooting` — recurring failure modes the drafter should preempt and the reviewer should catch.

## Output

Default to drafting against `templates/default-output.md`. Render as Word, Excel, PowerPoint, or Markdown when the audience or workflow asks for it; the typical deliverable is a Word memo via the `docx` skill in the `document-skills` plugin, with the substantiation-file and required-disclosures matrix lifting cleanly to Excel for the books-and-records evidence index. The CCO or designated reviewer acts on the pack; counsel sets privilege posture. Downstream consumers: `adviser-exam-readiness` reads the pack where EXAMS has requested marketing materials and the substantiation file; `policy-gap-review` reads the recurring substantiation or recordkeeping gaps where the annual Rule 206(4)-7 review needs them.

## Human review and AI disclosure

Open the deliverable with this line, and remove it only after the review below: `AI-assisted draft. Requires review by a qualified person before use.`

A qualified person with authority to change the output reviews it before it is delivered or relied on, and stays accountable for it. Where the output supports advice to an individual or a decision about an individual (credit, insurance underwriting, pricing or claims, employment, legal rights, or similar), that individual must be told AI was used to produce it. This skill does not make final decisions, file with a regulator, notify customers, execute transactions, or move money or other financial assets.
