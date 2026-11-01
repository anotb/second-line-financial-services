# sector-overlays

One section per sector. Read only the sections the scope calls for.

## capital-markets

### Capital markets sector overlay for marketing-rule-evidence

This skill is sector-unique to SEC-registered investment advisers and the asset-management entities that operate under that regime. The capital-markets overlay is the default and only sector overlay; it carries the adviser- and asset-manager-specific mechanics that the SKILL.md body refers to in generic workflow language.

Loaded by: `marketing-rule-evidence/SKILL.md` by default for any engagement in this plugin's scope. The overlay also fires from `scope.sector_overlay_set` when the scope record names `capital-markets`.

Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Adviser registration class and the rule perimeter

The Marketing Rule applies to SEC-registered investment advisers (Form ADV Part 1A registered) and, as a matter of antifraud reach, informs the conduct expected of state-registered advisers under analogous state rules. Routing decisions:

- *SEC-registered investment adviser* — Marketing Rule (Rule 206(4)-1) applies; the pack runs in full. The Form ADV Part 1A Item 5.L. cross-check fires.
- *Exempt reporting adviser (ERA) — venture-capital adviser exemption or private-fund adviser exemption* — the Marketing Rule does not apply by its terms; the §206 antifraud reach does. The pack runs the antifraud overlay (general prohibitions; fair-and-balanced read) but not the rule-specific disclosure mechanics. The pack flags the ERA posture in the identification block.
- *Dual registrant (BD-IA)* — the Marketing Rule applies to advisory communications; FINRA Rule 2210 applies to broker-dealer communications. Many communications fall under both regimes. The pack runs the Marketing Rule analysis on the advisory-side; the firm's broker-dealer compliance function runs the Rule 2210 analysis on the BD-side. The pack flags the dual-track routing.
- *Broker-dealer only (no IA registration)* — the Marketing Rule does not apply; FINRA Rule 2210 governs. The pack does not run; route to the broker-dealer compliance function.

Where the operative entity is a registered investment company (mutual fund; ETF; closed-end fund; UIT) and the advertisement is the fund's advertisement (rather than the adviser's advertisement of its advisory services), the routing is Rule 482 / Rule 156, not the Marketing Rule. The pack flags the routing decision; registered-fund advertisement review routes to the fund's marketing-review function and the fund-board oversight (see `fund-board-reporting`).

#### The Rule 206(4)-7 written-compliance-program tie-in

The Marketing Rule operates inside the firm's Rule 206(4)-7 written compliance program. The pack pins the relevant policy and procedure for each section that requires one:

- *Hypothetical-performance audience-appropriateness policy.* Rule 206(4)-1(d)(6) requires policies and procedures designed to ensure the hypothetical performance is relevant to the likely audience. The pack records whether the firm has a written policy and whether the procedure was actually applied to the in-scope advertisement.
- *Substantiation policy and the substantiation-file retention.* The general prohibition against unsubstantiated material claims operates with the firm's substantiation policy and the substantiation-file practice that lives under Rule 204-2(a)(11) and (a)(16).
- *Testimonial / endorsement oversight policy.* Rule 206(4)-1(c) requires oversight of testimonials and endorsements; the pack records the oversight procedure and the evidence of its operation.
- *Ineligible-person screening procedure.* The pack records the firm's screening procedure (initial screen at agreement; continuing-basis re-screen cadence; remediation pathway when a screen returns a positive).

The annual Rule 206(4)-7 review reads the recurring marketing-review findings; the pack flags items that should feed the annual review.

#### Books-and-records discipline under Rule 204-2

The recordkeeping discipline runs through every section of the pack. Common pin points the pack records explicitly:

- *Calculation worksheet retention.* Rule 204-2(a)(11) requires records sufficient to demonstrate the calculation of any performance shown. The worksheet, the methodology pin, the underlying-account trail, and the date-stamped attestation are all in scope. A worksheet that cannot be produced renders the performance claim unsubstantiated for recordkeeping purposes regardless of whether the underlying calculation is correct.
- *Written-promoter-and-endorser-agreement retention.* Rule 204-2(a)(15) requires retention of the written agreement where compensation exceeds the prescribed threshold, the testimonial / endorsement itself, the ineligible-person determination, and the compensation paid.
- *Records sufficient to demonstrate compliance for oral advertisements.* Webinars, podcasts, conference talks, and recorded interviews are advertisements where the two-prong definition is met. The pack records the retention of the recording, the outline or transcript where used, and the substantiation file for any material claim made orally.
- *Distribution log.* The pack records the distribution log: who received the advertisement, when, by what channel. The distribution log supports the one-on-one carve-out claim where the firm relies on it (showing the advertisement was disseminated to a single recipient at a time) and supports the audience-composition analysis under (d)(6).

#### Private-fund-adviser specifics

Private-fund advisers operate under the Marketing Rule on the same basis as other SEC-registered advisers; the rule does not distinguish public-fund vs. private-fund adviser status for general application. Specific points:

- *Net-of-fees presentation: the one-on-one private-fund-investor exception.* Rule 206(4)-1(e) sets the gross-and-net pairing requirement with a narrow one-on-one exception for advertisements provided directly to a private-fund investor. The exception is narrow: the advertisement must be one-on-one with the investor (not a tear-sheet at a conference; not a deck shared with the investor and the investor's consultants in a meeting); the firm must provide the investor on request the information necessary to compute net-of-fees performance. The pack pins the exception claim, the one-on-one evidence, and the on-request-information mechanic.
- *Fund-as-advertised vs. adviser-as-advertised.* Where the advertisement promotes the adviser's advisory services to the fund (and to other prospective clients), the Marketing Rule governs. Where the advertisement promotes the fund itself as a security (regardless of the fund's regulatory wrapper), additional securities-law disclosure mechanics may apply (Section 5 of the Securities Act; Regulation D for private-fund interests). The pack flags the routing where the dual-purpose nature is operative.
- *Hypothetical performance for institutional audiences.* The (d)(6) audience-appropriateness condition asks whether the hypothetical is appropriate for the likely recipients. Institutional sophistication does not satisfy the condition by default; the firm's policy and procedure must specify the audience for which hypothetical performance is appropriate, and the procedure must have been applied to the advertisement.

#### Form ADV Item 5.L. cross-check

The pack cross-checks the in-scope advertisement against the firm's Form ADV Part 1A Item 5.L. responses on the use of testimonials, endorsements, third-party ratings, hypothetical performance, predecessor performance, and other Marketing-Rule-relevant items. Inconsistencies are an EXAMS finding pattern; the pack flags any inconsistency in the residual-issues block.

#### Capital-markets-specific pack template additions

The fields are minimal because the rule discipline drives the pack:

- `advertisement.adviser_registration_class` — enum (`sec-registered-investment-adviser`, `exempt-reporting-adviser-vc`, `exempt-reporting-adviser-private-fund`, `dual-registrant-bd-ia`, `broker-dealer-only-no-ia`, `state-registered-investment-adviser`).
- `advertisement.fund_advertiser_routing` — enum (`adviser-as-advertiser-marketing-rule`, `fund-as-advertiser-rule-482-156`, `dual-purpose-pack-flags-routing`).
- `advertisement.one_on_one_carve_out_claimed` — boolean; if true, the pack records the basis and the distribution-log evidence.
- `advertisement.private_fund_investor_one_on_one_net_exception` — boolean; if true, the pack records the on-request-information mechanic and the one-on-one evidence.
- `firm_compliance_program.audience_appropriateness_policy_pin` — string; pointer to the firm policy under Rule 206(4)-7.
- `form_adv_part_1a_item_5l_consistency` — enum (`consistent`, `inconsistent`, `not-checked`); the pack flags inconsistencies.

#### Common pitfalls when capital-markets is the default overlay

- Treating the one-on-one carve-out as available for hypothetical performance. The (d)(6) conditions apply regardless of recipient count; the carve-out from the advertisement definition does not reach hypothetical performance.
- Treating the private-fund-investor one-on-one net exception as available wherever the audience is a private-fund investor. The exception requires actual one-on-one delivery; a deck shared at a meeting attended by the investor and the investor's consultants is not one-on-one.
- Missing the BD-IA dual-track routing. Communications that are simultaneously advisory and broker-dealer in nature need both reviews; running only the Marketing Rule review leaves the BD-side compliance gap open.
- Routing a registered-fund advertisement through the Marketing Rule when the fund is the advertiser. The routing is Rule 482 / Rule 156; the Marketing Rule applies to the adviser's advertising of its advisory services.
- Treating the substantiation file as optional where the advertisement contains a third-party rating. The third-party-rating section requires a reasonable basis for the rating, the disclosures, and the records to support the firm's reliance; the substantiation file is the evidence trail.
- Treating the calculation worksheet as a back-office artifact disconnected from the advertisement review. Rule 204-2(a)(11) and (a)(16) require the worksheet, the methodology pin, and the underlying-account trail to be sufficient to demonstrate compliance; the pack closes that loop.
- Treating webinars, podcasts, and conference talks as outside the rule. Where the two-prong definition is met (and the extemporaneous-oral carve-out is not), they are advertisements; the recording, the outline or transcript, and the substantiation file are all in scope.
