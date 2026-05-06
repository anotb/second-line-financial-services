# Spec: marketing-rule-evidence

Plugin: capital-markets-asset-management-compliance
Status: phase 1 spec sheet, pending phase 2 build
Date: 2026-05-06
Sector overlay: capital-markets (SEC-registered investment advisers, including private fund advisers)

## Activation-tuned description

Builds a Marketing Rule evidence pack for a single piece of adviser advertising under SEC Rule 206(4)-1. Drafts the substantiation file: classifies the statement (advertisement, performance presentation, hypothetical, testimonial, endorsement, third-party rating), maps required disclosures, lists required substantiation, applies hypothetical-performance pre-conditions, runs the testimonial/endorsement compliance checklist, and assembles the books-and-records artifact under Rule 204-2(a)(11) and (a)(15)-(16). Output is a reviewer-ready memo and evidence index that the CCO or designated reviewer can sign off before the ad is disseminated.

Best for:
- An investment adviser is about to disseminate a piece of marketing (pitch deck, fact sheet, website page, RFP response, social post) and needs a pre-dissemination review pack.
- A CCO is conducting a periodic look-back on advisertising for an annual Rule 206(4)-7 review and needs evidence files reconstructed for sampled ads.
- An adviser is responding to a Division of Examinations document request that calls for marketing materials, substantiation, and disclosures.
- The advertisement contains hypothetical performance, predecessor performance, related performance, model performance, testimonials, endorsements, or third-party ratings, where Rule 206(4)-1 imposes specific pre-conditions and required disclosures.

Not the right tool when:
- The artifact is not adviser advertising under Rule 206(4)-1 (e.g., broker-dealer communications under FINRA Rule 2210; fund prospectus under Rule 482 or Rule 156; account statements; one-on-one tax discussions excluded from the advertisement definition).
- The objective is to draft new marketing copy. This skill reviews and substantiates existing copy.
- The objective is overall compliance program design. Use risk-compliance-core/policy-gap-review or adviser-exam-readiness in this plugin.
- The advertisement is from a broker-dealer for a non-adviser product (use FINRA Rule 2210 framework; not in this skill's scope).

Anchored to: SEC Rule 206(4)-1 (Marketing Rule, adopted Dec 22 2020, compliance date Nov 4 2022); Rule 206(4)-1(d) prohibitions; Rule 206(4)-1(b) testimonials and endorsements; Rule 206(4)-1(c) third-party ratings; Rule 206(4)-1(d)(6) hypothetical performance; Rule 206(4)-1(e) definitions; Rule 204-2(a)(11), (a)(15), (a)(16) recordkeeping; Marketing Rule Adopting Release IA-5653 (Dec 22 2020); SEC Risk Alert "Examinations Focused on the New Investment Adviser Marketing Rule" (Sept 19 2022); SEC Risk Alert "Marketing Rule: Compliance Issues" (Apr 17 2023) [verify exact title and date]; SEC Marketing Rule FAQ (current).

## Source anchors

- 17 CFR 275.206(4)-1 — Marketing Rule.
  - (a) definitions of "advertisement" (two prongs: indirect/direct communication offering advisory services; compensated testimonials and endorsements).
  - (b) general prohibitions: untrue, unsubstantiated, omissions, fair and balanced, materially misleading.
  - (c) testimonials and endorsements: required disclosures (status as client/non-client, compensation, material conflicts), oversight, written agreement for >$1,000 over 12 months, ineligible-person disqualification.
  - (d) third-party ratings: reasonable basis, disclosures (date, period, identity, compensation).
  - (d)(6) hypothetical performance: policies/procedures for likely audience; sufficient information to understand criteria and assumptions; sufficient information to understand risks/limitations.
  - (e) prohibited performance presentations: gross without net (with limited one-on-one exception); prescribed time periods (1-, 5-, 10-year) for any performance unless related to portfolio with shorter life; predecessor performance conditions; related performance; extracted performance.
  - 17 CFR 275.204-2(a)(11), (a)(15), (a)(16) — books-and-records: copies of advertisements; documentation of performance computations; testimonial/endorsement records; records to support oral advertisements.
- SEC Investment Adviser Marketing Rule, Final Rule Release IA-5653 (Dec 22 2020) — preamble interpretive guidance.
- SEC Division of Examinations Risk Alert, "Examinations Focused on the New Investment Adviser Marketing Rule" (Sept 19 2022).
- SEC Division of Examinations Risk Alert, "Marketing Rule: Compliance Issues" (Apr 17 2023). [verify exact title]
- SEC Marketing Rule FAQ (staff FAQ, periodically updated). [verify current state]
- Public enforcement actions: SEC orders against advisers for hypothetical performance violations (Sept 2023 sweep, 9 advisers); SEC orders for testimonial/endorsement and third-party rating violations (2023-2024). [pin specific releases in phase 2]
- Investment Advisers Act §206 anti-fraud foundation; §206(4) rulemaking authority.

## Sector overlays needed

Only `capital-markets`. This skill is sector-unique to SEC-registered IAs. No banking/insurance/payments overlay. No other-sector overlay file in `references/sector-overlays/`.

## Cross-cutting overlays needed

- `cyber.md` — only when an advertisement makes claims about the firm's cybersecurity posture, vendor security, AI safety, or incident-free record. Must square with Reg S-P, the SEC cyber proposed rules for advisers, and Item 20 of Form ADV Part 2A. [verify cyber rule current state]
- `conduct.md` — fair-and-balanced obligation; manipulative or misleading testimonial framing; non-cherry-picked performance presentations. UDAAP-adjacent reasoning even though UDAAP itself does not apply to non-consumer advisory.
- `privacy.md` — testimonials that disclose client identity require client consent and Reg S-P consideration when account-level details appear.
- `climate.md` — only when ESG-labeled fund/strategy marketing makes climate claims. Must square with the Names Rule (Rule 35d-1) for funds and ESG anti-greenwashing posture; CCM "Greenwashing" releases. [verify Names Rule revision applicability]

## Output template named sections

1. Advertisement identification (advertisement ID, file path/URL, channel, date of dissemination, target audience, retail/non-retail flag, languages)
2. Statement-type classification (advertisement under Rule 206(4)-1(e); contains testimonial; contains endorsement; contains third-party rating; contains hypothetical performance; contains predecessor/related/extracted performance; one-on-one or to multiple recipients)
3. Required disclosures matrix (per statement type, what must be present, where it appears in the artifact, exact wording or citation)
4. Substantiation file (every material claim, what supports it, location of source, date of source, whether claim is "fair and balanced," reviewer notes)
5. Performance presentation review (gross/net pairing; 1-, 5-, 10-year periods; calculation methodology; benchmark selection; fees and expenses treatment; predecessor portability conditions met; related performance composite construction; extracted performance disclosure)
6. Hypothetical performance pre-conditions (audience appropriateness policy; criteria/assumptions disclosed; risks/limitations disclosed; written policies and procedures applied)
7. Testimonial/endorsement checklist (compensated yes/no; client/non-client status disclosed; conflicts disclosed; promoter agreement on file; ineligible-person screening run; recordkeeping under 204-2(a)(15))
8. Third-party rating checklist (rating identity, period, methodology, compensation paid)
9. Books-and-records pack (Rule 204-2 evidence index: ad copy, calculation worksheets, written agreements, attestations, screening evidence, distribution log)
10. Reviewer sign-off (reviewer name/role, date, status: approved / approved with edits / not approved, residual issues, escalation flag)
11. Source trace and confidence

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| review_id | string | Stable ID for this review |
| advertisement.id | string | Stable advertisement ID |
| advertisement.channel | enum {pitch_deck, fact_sheet, website, rfp, social, email, video, podcast, print, third_party_platform} | Dissemination channel |
| advertisement.audience | enum {retail, qualified_client, qualified_purchaser, institutional, mixed} | Target audience |
| advertisement.dissemination_status | enum {pre_dissemination, in_market, withdrawn, archived} | Lifecycle |
| statement_types | array<enum {advertisement_general, performance, hypothetical_performance, predecessor_performance, related_performance, extracted_performance, model_performance, testimonial, endorsement, third_party_rating}> | Classifications applied |
| required_disclosures | array<{type, required_text_or_topic, present, location_in_artifact, citation}> | Per statement type, what must be present |
| substantiation_items | array<{claim_text, claim_type, evidence_summary, evidence_location, evidence_date, fair_and_balanced_assessment, reviewer_note}> | Per material claim |
| performance_presentation | object {has_performance, gross_present, net_present, one_on_one_exception_invoked, periods_1_5_10_present, methodology_pin, benchmark_pin, fees_treatment, predecessor_conditions_met, related_composite_method, extracted_disclosure_present} | Performance review |
| hypothetical_performance | object {present, audience_appropriateness_policy_pin, criteria_assumptions_disclosed, risks_limitations_disclosed, policies_and_procedures_pin} | Hypothetical pre-conditions |
| testimonials_endorsements | array<{compensated, client_status_disclosed, conflicts_disclosed, written_agreement_on_file, ineligible_person_screen_date, recordkeeping_pin}> | Per testimonial/endorsement |
| third_party_ratings | array<{rating_provider, rating_period, methodology_disclosed, compensation_paid, compensation_disclosed}> | Per rating |
| books_and_records | array<{record_type, citation_204_2, location, retention_through}> | 204-2 evidence index |
| reviewer_signoff | object {reviewer, role, date, status, residual_issues, escalation} | Reviewer determination |
| confidence | enum {high, medium, low, unknown} | Reviewer confidence |
| open_questions | array<{question, blocker_for}> | Items needing legal/CCO input |

## Example scenarios (public-source-derived)

1. **Hypothetical performance in a pitch deck (Sept 2023 sweep pattern).** A registered adviser circulates a pitch deck to prospective institutional clients showing a "model" allocation strategy with 7-year backtested returns. The skill classifies this as hypothetical performance under Rule 206(4)-1(e), runs the (d)(6) pre-conditions checklist, finds the firm has no policies and procedures specifying that hypothetical performance is appropriate for the institutional audience receiving it, finds the criteria-and-assumptions disclosure present but the risks-and-limitations disclosure incomplete, and surfaces a books-and-records gap on the calculation worksheet retention. Pattern derived from the September 2023 SEC enforcement sweep against nine advisers for hypothetical-performance violations (publicly announced). [verify exact release]

2. **Compensated testimonial on a website (Apr 2023 risk alert pattern).** An adviser's public-facing website carries a video testimonial from an existing client receiving a fee discount in exchange. The skill classifies this as a compensated testimonial, checks for the three required disclosures (client status, that compensation was paid, material conflicts), checks for a written agreement on file under Rule 206(4)-1(b)(3) since the value of compensation exceeds $1,000 over 12 months, runs the ineligible-person screen against §3(a)(39) of the Exchange Act and §202(a)(17) of the Advisers Act categories, and assembles the 204-2(a)(15) records. Finding: the website disclosure is present but does not appear "clearly and prominently" in the testimonial itself; conflicts disclosure missing; ineligible-person screen documented but stale.

## Common pitfalls

1. Treating the advertisement definition as obvious. The Rule's definition has two prongs and several carve-outs (one-on-one communications excluded except for hypothetical performance; extemporaneous oral communications excluded; required regulatory communications excluded). Misclassifying scope produces a wrong evidence pack.
2. Skipping the "fair and balanced" overlay. Rule 206(4)-1(b)(2) is the antifraud backbone of the Rule. A claim can be technically true and still fail fair-and-balanced.
3. Treating one-on-one as a free pass for hypothetical performance. The one-on-one exception in (d)(6) does not exist for hypothetical performance: the (d)(6) conditions apply regardless of whether the communication is to one client or many.
4. Confusing predecessor, related, model, and hypothetical performance. Each has separate conditions. A presentation often combines two or three categories. Map each performance series to the right category before running disclosures.
5. Net-of-fees presentation errors. Net must be presented with the same prominence as gross, computed using the same methodology and time periods. The "one-on-one to a private fund investor" exception is narrow. Misreading the exception is one of the most common SEC findings.
6. Stale ineligible-person screening. The screen must be done at agreement time and on a continuing basis. A screening attestation older than the look-back window is a finding.
7. Missing recordkeeping for oral advertisements. Rule 204-2(a)(11) requires records sufficient to demonstrate compliance with the Marketing Rule. Webinars, podcasts, and conference talks are advertisements; an outline or transcript and the substantiation file must be retained.
8. Confusing the Marketing Rule with FINRA 2210 and Rule 482. Same conduct, three different rule sets depending on entity and product. This skill is the IA Marketing Rule lane only.
