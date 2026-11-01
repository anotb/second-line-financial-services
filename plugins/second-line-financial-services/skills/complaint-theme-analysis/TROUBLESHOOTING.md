# Troubleshooting: complaint-theme-analysis

Recurring failure modes when a complaint-theme analysis looks complete but is not. The drafter should preempt these; the decision-forum reviewer (consumer compliance committee, conduct committee, head of fair lending, CCO, counsel) should catch the rest.

## Counts at the bureau's sub-issue grain instead of at the theme grain

Symptom: the matrix has rows that mirror the CFPB sub-issue taxonomy. The "themes" are "Problem with a credit reporting company's investigation into an existing problem" or "Trouble during payment process" with no firm-taxonomy theme overlay.

Why it happens: it is the path of least resistance from the public extract. The drafter pulled the bureau's sub-issue facets and called them themes.

Fix: themes are firm-taxonomy themes, mapped to but not equal to the bureau's coding. Two distinct root causes can map to the same sub-issue; one root cause can split across sub-issues. The taxonomy version is named in the memo; the mapping is filed for reproducibility.

## Confirmation-bias theme inflation

Symptom: the top theme is the theme the head of consumer compliance brought into the room. The drafter read 50 narratives, all of which seemed to confirm the theme, and wrote the matrix from those.

Why it happens: confirmation bias under time pressure. Reading narratives is the most-engaging part of the work; reading the entire population through a coding rule is the least.

Fix: theming method is pre-registered in the memo. The coding rule is applied to the entire sample, not just the narratives the drafter read. The method's coding agreement is reported (dual-read on a sample). Where the method has been adapted mid-review, the adaptation is named.

## CFPB Complaint Database treated as the firm's full complaint surface

Symptom: the matrix counts come entirely from the public CFPB Complaint Database extract; the firm's internal complaint records are not consulted.

Why it happens: the public extract is easy to pull; the firm-internal channels require the complaint-management system access.

Fix: the scope-and-population section enumerates every channel reviewed and explicitly states channels excluded. The CFPB-portal subset is one channel; the firm-direct call-center, web-form, branch-escalation, and executive-resolution channels typically dwarf it. App-store reviews, social-listening signals, state-AG referrals, and employee-escalation logs are separate channels. The memo names what was pulled and what was not.

## Counting inflation from CFPB-portal-and-firm-direct double counting

Symptom: the matrix totals exceed the firm's true complaint count for the period because CFPB-portal complaints are counted both in the public-extract pull and in the firm-internal records.

Why it happens: the CFPB-portal complaints arrive in the firm's complaint-management system through the bureau's company portal; if the deduplication is not done, both pulls capture the same complaint event.

Fix: deduplication is named in the theming-method section. The match key (consumer ID where consent-flag permits; or a composite of date, product, sub-issue, and ZIP3) is documented. Where deduplication is incomplete, the memo carries the residual-overlap estimate.

## Apparent spike that is volume-driven, not rate-driven

Symptom: a theme moves from 8 percent to 18 percent of period complaints; the memo reports the share movement as a real signal. The firm's relevant denominator (new-account openings; loss-mit-eligible borrowers; active P2P users) doubled in the period because of a campaign or a launch.

Why it happens: the drafter computed share but not rate. Volume-driven share movements are misread as substantive theme spikes.

Fix: the rate framing accompanies the share framing where the data permits. The denominator is named (e.g., per 1,000 new accounts; per 1,000 loss-mit-eligible borrowers; per 1,000 active users). Where the denominator is unavailable, the share movement is read against the relevant volume movement and the dependence is named.

## BISG signal asserted as protected-class evidence

Symptom: the matrix has `fair_lending_flag: true` on a theme with a BISG-derived demographic-skew read; the memo treats the BISG signal as evidence of disparate impact.

Why it happens: BISG is a probabilistic estimate, not a measurement. Drafters under time pressure conflate the signal with the finding.

Fix: BISG is signal, not proof. The fair-lending flag is a flag-grade signal that feeds the cross-skill chain into `fair-lending-test-plan` for finding-grade analysis. The matrix's `signal_grade` column carries `flag` or `watch-list`, not finding. For mortgage themes, HMDA self-reported demographics are the operative source where available; BISG is supplemental.

## Trend movement not cross-walked against product or campaign timeline

Symptom: a theme spikes in the period; the memo reports the spike but does not name what changed in the product, marketing, or process timeline that would account for it.

Why it happens: the drafter ran the theme analysis without consulting the product-change log or the marketing-campaign calendar.

Fix: the trends-and-movements section cross-walks the theme movement against the product / campaign / process-change timeline. Apparent theme spikes that align with a launch or a campaign are called out and the timing relationship is named explicitly. Where no in-period change accounts for the spike, that absence is also noted.

## Recommended actions read as generic policy advice

Symptom: the recommended-actions block lists items like "review the theme", "consider remediation", "engage the marketing team" without owners, due dates, named controls, or accountable forums.

Why it happens: the drafter wrote the actions in advisory voice rather than as a structured set of recommendations the decision-forum acts on.

Fix: each action names the specific intervention, the owner role, the due date, the named control to be modified or instituted, and the accountable forum. "Update the post-click landing page on the December rewards-bonus campaign to surface the FX-fee disclosure above the fold on mobile by [date], owned by the head of card marketing, with the marketing review committee as the accountable forum and the consumer compliance committee taking a read" is an action. "Review the marketing" is not.

## Conduct overlay treated as a checklist

Symptom: the conduct-risk implications block lists the conduct-risk taxonomy categories as a generic checklist with no per-theme narrative; the conduct-accountable manager role is unfilled; the conduct-event candidate flag is missing.

Why it happens: the drafter consumed the conduct overlay as a checklist rather than as the substantive overlay the conduct framework expects.

Fix: conduct overlay is mandatory on this skill. Per top theme, the taxonomy tie-back is populated, the conduct-accountable manager role is named (a role under SMCR or the firm's conduct framework, distinct from the decision forum), the conduct-event candidate flag carries a recommendation, and the complaint-monitoring loop closure is specified.

## Complaint-monitoring loop closure absent

Symptom: the recommended actions are well-specified but no post-action monitoring posture is named for any theme.

Why it happens: the drafter treated the memo as the work product itself rather than as the input to the conduct function's ongoing surveillance.

Fix: per top theme, the loop closure is named: which complaint codes the firm watches for re-emergence, the cadence of the read, the threshold for off-cycle re-review, the escalation trigger if the theme persists. Theme analysis without loop closure is incomplete.

## Skill produces a UDAAP determination or fair-lending finding

Symptom: the memo concludes that a UDAAP violation has occurred or that disparate impact has been established. Or the memo concludes that no violation or disparate impact is present.

Why it happens: the drafter conflated the theme analysis with the determination. Theme analysis surfaces signal; the determinations live in `udaap-risk-review` and `fair-lending-test-plan` and ultimately in counsel and the decision forums.

Fix: the memo states the regulatory exposure (the citations the theme touches) and the recommended cross-skill chain (e.g., escalate to `udaap-risk-review` for element-by-element analysis). It does not declare a final UDAAP determination or a fair-lending finding. The guardrail in the SKILL.md frontmatter is reflected in the memo's status line and in the recommended-actions framing.

## App-store reviews excluded for fintech themes

Symptom: a payments-fintech complaint-theme analysis pulls only the CFPB-portal extract and the firm-internal records; the app-store review channel is omitted entirely.

Why it happens: app-store reviews "are not complaints" in the firm's complaint-management taxonomy; they live in the marketing or product team.

Fix: for payments-fintech, app-store reviews are a meaningful complaint channel and the payments-fintech sector overlay flags them as such. The memo includes the app-store review pull (with the volume-bias caveat) or names the channel as excluded with a rationale.

## State-AG channel pulled mechanically across all states

Symptom: the memo pulls state-AG referrals from every state where the firm operates, treating all states as equivalent.

Why it happens: defensive completeness. The drafter pulled everything that was pullable.

Fix: state-AG channels are pulled selectively based on the firm's footprint depth in the state, the state-AG's known focal areas, and the firm's routing relationship with the state-AG offices. The memo names the states pulled and the rationale; the states excluded are also named.

## Severity rating without the rubric

Symptom: severities are assigned ("high", "medium") with no per-theme rationale and no rubric reference; the rubric is not stated in the memo.

Why it happens: severity drift is the canonical failure mode. Drafters set severity by feel.

Fix: the rubric is stated once in the memo (Critical / High / Medium / Low with explicit definitions). Each theme carries a per-theme `severity_rationale` referencing the rubric. Where multiple themes share a severity, each carries its own rationale.

## AI-flagged themes do not feed the cross-skill chain

Symptom: a theme touches algorithmic decisioning, AI agents, or AI-generated communication; `ai_flag: true` is set on the matrix; no cross-skill chain into `adverse-action-review`, `udaap-risk-review`, or `fair-lending-test-plan` is named.

Why it happens: the drafter set the flag mechanically without considering the implications.

Fix: AI-flagged themes feed at least one cross-skill chain. AAN-content themes chain to `adverse-action-review`; algorithmic-outcome themes chain to `udaap-risk-review`; protected-class-disparity themes chain to `fair-lending-test-plan`. The April 2023 Joint Statement and CFPB Circulars 2022-03 and 2023-03 are cited where applicable.

## Source trace and confidence label absent

Symptom: the memo cites no sources for material claims. Theme severity, regulatory exposure citations, and root-cause hypotheses appear without supporting references.

Why it happens: the drafter borrowed from prior memos without recording the source.

Fix: every material claim cites a source from `references/source-anchors.md` (or a loaded overlay) by file path. Source evidence (transaction data, complaint records), management assertions (first-line root-cause hypotheses), public-source obligations (regulatory anchors), generated inferences (the second-line's read of the pattern), and open legal questions stay distinguishable. The confidence label per major analytical claim reflects how well the memo supports the recommended actions.

## Sponsor-bank-fintech theme attribution unclear

Symptom: the memo covers a sponsor-bank-fintech program; themes are reported with no attribution between the bank, the fintech, and the program-agreement allocation.

Why it happens: the drafter is operating from one entity's perspective and treats the other as administrative.

Fix: per theme, the attribution names which entity holds the consumer-facing relationship, which entity owns the product / marketing / fee design at issue, and which entity owns the disclosure. The cross-skill chain into `udaap-risk-review` or `marketing-claim-review` names the bank as the accountable party per the interagency third-party guidance.

## Insurance-side theme analysed under CFPB framework

Symptom: the memo themes insurance underwriting, pricing, or claims-handling complaints under the UDAAP framework.

Why it happens: the drafter loaded the wrong sector overlay or did not load the insurance overlay.

Fix: route to the state-DOI / NAIC framework per the insurance sector overlay. The narrow exception is bank-affiliated credit-protection insurance bundled with credit, where the credit-side runs under the consumer-finance framework and the insurance-side runs under the state-DOI framework; the memo carries both reads.
