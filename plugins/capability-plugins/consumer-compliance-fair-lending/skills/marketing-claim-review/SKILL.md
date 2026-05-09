---
name: marketing-claim-review
description: |
  Drafts a second-line marketing-claim review memo for one creative or one campaign of consumer-financial marketing. Asset-by-asset and claim-by-claim: substantiation status per claim; deception, unfairness, and (where applicable) abusiveness reads on the displayed asset; required disclosures (Reg Z trigger terms, MAPR / APR / fees, FDIC insurance, Reg DD, MLA where in scope, TRID-adjacent where the marketing previews mortgage terms); fair-lending distribution and targeting findings; privacy-claim accuracy; dark-pattern findings against a named taxonomy; AI-generated and AI-personalised content review; and recommended edits with kill-switch candidates. The memo is the input to the marketing-compliance decision forum; it does not approve marketing for launch, take down live assets, or finalize UDAAP, fair-lending, or privacy determinations.

  Best for:
  - Pre-launch second-line review of one consumer-financial marketing campaign (deposit, credit card, mortgage, BNPL, personal loan, auto, small business) before the marketing-compliance committee approves launch.
  - Periodic in-market sweep of live marketing inventory, particularly post-MRA or post-consent-order on marketing.
  - Targeted review after a complaint theme on disclosure adequacy or undisclosed fees (chain to `complaint-theme-analysis`).
  - Review of AI-generated marketing copy or AI-personalised landing pages where substantiation, accuracy, or privacy claims are in scope.

  Not the right tool when:
  - The question is the adverse-action notice (use `adverse-action-review`).
  - The question is fair-lending statistical testing of marketing distribution (use `fair-lending-test-plan`; this skill flags distribution concerns, the test plan operationalises them).
  - The question is UDAAP at the product, fee, or flow level (use `udaap-risk-review`; this skill is asset-level).
  - The question is Section 1071 small-business data submission (use `section1071-readiness`).
  - The question is investment-adviser Marketing Rule (Rule 206(4)-1) evidence (use `marketing-rule-evidence` in `capital-markets-asset-management-compliance`; the doctrinal lane is antifraud, not UDAAP).
argument-hint: "[creative or campaign id; channels in scope; assets list; AI-in-path flag; sector and cross-cutting overlay flags]"
---

# Marketing claim review

A marketing-claim review memo is what the second-line consumer-compliance team produces so the marketing-compliance committee, the head of marketing review, the CCO, and (where directing) outside counsel can decide whether the asset or the campaign is fit to launch or fit to remain live. The work is asset-by-asset and claim-by-claim: each claim is logged with category, substantiation status, and source of substantiation; each asset is read for disclosure adequacy on the device class consumers actually use; the deception, unfairness, and (where applicable) abusiveness reads run on the displayed asset; fair-lending distribution and targeting findings, privacy-claim accuracy, and dark-pattern findings round out the analysis; recommended edits and kill-switch candidates close it.

The skill serves both lenses. A 1.5-line marketing-compliance reviewer inside the marketing function uses it to consolidate the read as the campaign moves through copy, design, and channel-launch. A 2-line independent consumer-compliance reviewer or fair-lending lead uses the same skill to challenge what was drafted and to surface the claims the first line did not test honestly. The seam between them is the per-claim substantiation source field, the device-class capture of the disclosure layout, and the AI-content review block.

The memo is a draft until the marketing-compliance committee acts on it. The skill stops at the recommendation. It does not approve marketing for launch, take down live assets, finalize UDAAP or fair-lending or privacy-claim determinations, or issue customer-facing actions.

## Ask first

Before drafting, get plain answers to a few things. Defaults are fine when an answer is missing; flag the default in the memo.

- What is the unit of analysis. One creative (a single asset across one or more device classes) or one campaign (a coordinated set of creatives across channels). Multi-campaign or program-level reviews split into separate memos that cross-reference.
- What channels are in scope. Web, in-app, email, push, paid social, digital display, broadcast, print, scripts (call-center or retail), landing page, app store. Channel drives the disclosure framework that applies and the dark-pattern surface area.
- Whether AI is in path. AI-generated copy, AI-personalised headlines, AI-driven audience targeting, AI-rotated creative variants. The answer flips on the AI-content review block, pulls in the April 2023 Joint Statement, and adds substantiation discipline on every model-generated variant the consumer can be served.
- What the source posture is. Public-only, public-plus-firm-policy, public-plus-firm-policy-plus-evidence, or connector-aware. Source posture sets what the memo can actually cite (substantiation files, MAP records, audience-definition exports, served-impression logs, screenshots by device class) and what carries `[evidence needed]`.
- Who decides. Marketing-compliance committee at pre-launch and routine sweep; CCO and counsel where the finding is high-severity or where regulator engagement is in posture; conduct committee where the finding crosses UDAAP themes.

When `engagement-scope` is supplied, the skill consumes it for institution, persona, source posture, sector overlay set, and cross-cutting overlay set. Otherwise it asks the practitioner the few facts it needs and defaults to public posture if the practitioner declines, noting in the memo that scope was not formalised.

## How the memo gets built

The memo has the same spine across creatives and campaigns. A senior practitioner walks it roughly in the order below, but the conversation surfaces sections in whatever order the asset inventory and the substantiation evidence arrive; the per-asset structure sorts itself.

**Asset register.** Every reviewed asset gets an entry: asset id, channel, audience, dates in market, version, device classes captured, screenshot or recording reference. The register is what the reviewer comes back to when a finding refers to "the mobile variant of asset 3"; without the register, the memo loses the ability to point at the thing being reviewed.

**Reviewer and review posture.** Reviewer role (marketing-compliance reviewer; independent consumer-compliance second line; advisory engagement; joint with sponsor bank); review independence; counsel-directing flag; legal-privilege posture (`attorney-client-privileged`, `attorney-work-product`, `dual-purpose-business-and-privileged`, `not-privileged`, `posture-pending-counsel`). Sampling basis if the review is not full-coverage (random sample, risk-based sample, channel-stratified sample); the memo names the sampling frame and the inference it supports.

**Per-asset claim register.** For each asset, every claim the consumer can be served gets a row: claim text as it appears (not as it appears in the brief); claim category (rate, fee, APR / MAPR, eligibility, endorsement, comparative or superlative, privacy, security, rewards, availability, time-to-funding, green or ESG, AI-capability, other); substantiation status (`substantiated`, `partially-substantiated`, `not-substantiated`, `not-substantiable`, `evidence-needed`); source of substantiation (internal data, third-party study, regulator data, controlled study, MAP record); date of the substantiation source. A substantiation file from a different campaign is not substantiation; per-claim source-and-date is what catches the recycle.

**Disclosure adequacy.** The clear-and-conspicuous standard lives in the layout, not in the script. The disclosure block reads each in-scope rule against the displayed asset by device class:

- *Trigger-term-driven open-end credit advertising disclosures* under the open-end advertising rule.
- *Trigger-term-driven closed-end credit advertising disclosures* under the closed-end advertising rule.
- *HELOC advertising disclosures* under the HELOC advertising rule where the in-scope product is a HELOC.
- *Credit and charge card application and solicitation disclosures* (Schumer-box equivalents) under the card application and solicitation rule.
- *Deposit-account advertising disclosures* under the truth-in-savings rule where the in-scope product is a deposit account.
- *FDIC insurance representation* under the FDIC advertising rule for insured-depository advertising; non-bank attribution where the consumer-facing surface might lead a reasonable consumer to believe the deposit is FDIC-insured.
- *MAPR and MLA-covered-borrower disclosures* under the MLA framework where the consumer is a covered borrower.
- *TRID-adjacent disclosure mechanics* under the TILA-RESPA integrated disclosures where marketing previews closed-end mortgage terms.

The disclosure block names the operative rule per asset, the in-asset location of the required disclosure (above the fold or below; on first interaction or after click), the device-class delta (mobile-vs-desktop is the recurring failure mode), and the clear-and-conspicuous read. Where the disclosure is required and absent or inadequate, the memo records the finding and the recommended remediation; the regulatory citations live in `references/source-anchors.md` and the sector overlay where the rule is sector-specific.

**Fair-lending distribution and targeting findings.** Marketing distribution and content reach are a fair-lending surface under the discouragement prohibition in Reg B and the discriminatory-advertising prohibition in the Fair Housing Act for dwelling-related advertising. The block records: channel skew across policy-relevant segments and protected classes; geographic distribution (MSA, census tract, ZIP); audience-targeting parameters (lookalike-source seeds, interest-category exclusions, ZIP-based targeting, language preferences); AI-personalisation audit (where personalisation drives audience selection, headline variation, or claim selection). Where the distribution or targeting raises a parallel ECOA / FHA theory, the memo cross-references `fair-lending-test-plan` and stops short of running the disparity test (that is the test plan's job).

**UDAAP findings.** Each finding names the prong (deception, unfairness, abusiveness), the claim or asset element implicated, and the reasoning. Asset-level UDAAP findings are scoped to the displayed asset; product-level UDAAP belongs in `udaap-risk-review`. Deception is the most common asset-level finding (a headline likely to mislead a reasonable consumer in the served context; a substantiation gap on a comparative or superlative claim; a privacy claim materially inconsistent with the privacy notice). Unfairness applies on asset-level fee or rate mechanics where the asset misrepresents the cost; abusiveness applies on dark-pattern asset design where the consumer-journey through the asset materially interferes with understanding.

**Privacy claim findings.** Privacy claims and privacy-adjacent disclosures get their own block: GLBA Privacy Rule and Reg P consistency between the privacy notice and the on-asset claim; AdChoices representation accuracy where the firm participates in the DAA self-regulatory program; dark-pattern privacy (deceptive consent flows, manipulated cookie banners, pre-checked opt-ins, hidden settings); state-privacy-law interaction with marketing claims (CCPA / CPRA "share for cross-context behavioral advertising" disclosures vs. on-asset "we will not sell your data" claims, and the rolling roster of state laws). Sensitive-attribute targeting claims (e.g., representing that targeting does not use sensitive categories where audience definitions or AI personalisation in fact use proxies) are recorded here.

**Dark-pattern findings.** Each finding names the taxonomy entry, the location in the asset, and the consumer-harm hypothesis. The FTC dark-pattern report catalog supplies the taxonomy (nagging, obstruction, sneaking, interface interference, forced action, social-proof manipulation, asymmetric choice, hidden subscription mechanics, confirmshaming, and the related entries); the firm's own UX taxonomy may supplement. "The UX is confusing" is not a regulatory finding; "the consent flow uses interface-interference (asymmetric button weight; pre-checked accept; reject path requires three additional clicks) at the cookie banner on asset 5" is.

**AI-generated and AI-personalised content review.** Where AI is in the production path or the personalisation path, the AI block fires. The block records: provenance per variant (model id, prompt template, variable inputs, output review status); fabrication risk (a personalised headline that asserts approval probability without an underlying model output supporting the assertion); substantiation per variant (the substantiation file applies to the served claim, not to the brief); accuracy posture on personalisation (the same disclaimer surfaces when the personalised headline does); privacy implications (whether the personalisation inputs include consumer data the consumer believes is restricted). UDAAP and the credit advertising rules apply to the displayed claim, not to the upstream pipeline; an AI-generated variant that omits a triggered disclosure is a clear-and-conspicuous failure on the variant.

**Recommended edits, kill-switch list, requested controls.** Each remediation entry names: edit (what changes), owner role, due date, severity. The kill-switch list names assets the memo recommends pulling pending edit. Requested controls name the MAP control, marketing-review checkpoint, or AI-personalisation-review control the memo recommends adding to close the failure mode at the root, not just on the asset under review.

**Open legal questions.** Items deferred to counsel: state-attorney-general exposure on the in-scope claim under state baby-FTC acts; FTC Endorsement Guides applicability for non-bank fintech influencer arrangements; treatment of "we will not sell your data" claims under CCPA / CPRA's broader sale-and-share definitions; whether a substantiation file is sufficient where the underlying study is the firm's own.

**Source trace and confidence.** Every material claim cites a source from `references/source-anchors.md` (or the relevant overlay) by file path. Source evidence (the served asset, the substantiation file, the MAP record), management assertions (the marketing-team brief), public-source obligations (the operative regulation), generated inferences (the reviewer's read), and open legal questions stay distinguishable. The confidence label at the end reflects how well the memo supports the recommended decision; the label is honest, not aspirational.

### AI overlay

When AI is in the production path or the personalisation path on any in-scope asset, the AI block fires inside the named sections rather than as a separate document. The asset register flags the AI-in-path variants; the claim register records substantiation per served variant; the disclosure adequacy block reads each device-class layout including the personalised variants; the deception read addresses AI-generated copy where it misleads; the fair-lending distribution block addresses algorithmic targeting where it concentrates marketing on (or away from) protected-class or policy-relevant segments. The April 2023 Joint Statement is cited from `references/source-anchors.md` whenever algorithmic targeting or AI personalisation touches protected-class or policy-relevant segment exposure. The substantiation discipline is the same as for any other claim; the bureau and the FTC have both pursued AI-generated marketing fact patterns under existing UDAAP / UDAP authority.

### Sector overlays

When the engagement scope names a sector, load the matching `references/sector-overlays/<sector>.md`:

- *Banking* — deposit-advertising specifics under the truth-in-savings rule; FDIC insurance representation under the FDIC advertising rule; mortgage advertising under the TILA / RESPA / TRID interplay; CRA-related advertising; deposit-account fee mechanics on the asset.
- *Payments-fintech* — sponsor-bank attribution of marketing claims; BNPL marketing observations; app-store ad rules; Reg E error-resolution claims in marketing; influencer and creator endorsements under the FTC Endorsement Guides for non-bank fintech surfaces.
- *Capital markets* — scope-boundary first: the SEC investment adviser Marketing Rule (Rule 206(4)-1) and FINRA Rule 2210 communications-with-the-public framework live next door doctrinally and are reviewed by the firm's broker-dealer compliance or investment-adviser compliance function under the antifraud lane; this skill is the consumer-financial UDAAP / Reg Z lane and does not extend into the SEC Marketing Rule. Where capital-markets-affiliated entities advertise consumer credit (e.g., margin facilities offered to retail customers; wealth credit), the consumer-credit-side asset is in scope.
- *Insurance* — scope-boundary first: insurance advertising sits with state insurance departments under the NAIC Unfair Trade Practices Act framework (Model #880) and the NAIC Advertisements of Life Insurance and Annuities Model Regulation (Model #570) and similar A&H model regulations. The skill does not extend into insurance advertising as such. The narrow exception is bank-affiliated credit-protection insurance bundled with credit, where the credit-side bundling representation is in scope and the insurance-side advertising routes separately.

### Cross-cutting overlays

Conduct overlap with UDAAP is in `references/cross-cutting/conduct.md` and loads where the asset-level finding chains up to a product-level UDAAP read; cross-reference `udaap-risk-review`. Privacy overlay loads on every digital-channel review because privacy-claim accuracy, AdChoices representation, dark-pattern privacy, and state-privacy-law interaction are recurring asset-level findings; the privacy file lives at `references/cross-cutting/privacy.md`. Climate is not applicable.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays/banking.md`, `payments-fintech.md`, `capital-markets.md`, `insurance.md` — sector-specific framing loaded per engagement-scope.
- `references/cross-cutting/conduct.md` — UDAAP overlap with the asset-level finding; `references/cross-cutting/privacy.md` — privacy-claim substantiation, AdChoices, dark-pattern privacy, and state-privacy-law interaction.
- `references/firm-overlay.md` — firm-installed marketing taxonomy, named MAP, marketing-compliance committee, AI-personalisation governance, system-of-record paths (consumed when present).
- `templates/default-output.md` — memo template (named sections, asset-level fields).
- `examples/credit-card-prelaunch-mobile-disclosure.md`, `examples/fintech-paid-social-superlative-and-targeting.md` — public-source-derived worked examples.
- `TROUBLESHOOTING.md` — recurring failure modes the drafter should preempt and the reviewer should catch.

## Output

The deliverable is a Word memo. The skill defines the artifact substance (named sections, per-asset fields, populated content per `templates/default-output.md`) and delegates rendering to the `docx` skill in the `document-skills` plugin. The marketing-compliance committee, the head of marketing review, the CCO, or counsel acts on the memo; counsel sets privilege posture. Downstream consumers: `udaap-risk-review` reads the memo where the asset-level finding chains to a product-level UDAAP read; `fair-lending-test-plan` reads the distribution and targeting findings where the parallel ECOA / FHA theory needs a disparity test; `complaint-theme-analysis` reads the privacy and disclosure findings where the asset-level pattern feeds a complaint cluster.
