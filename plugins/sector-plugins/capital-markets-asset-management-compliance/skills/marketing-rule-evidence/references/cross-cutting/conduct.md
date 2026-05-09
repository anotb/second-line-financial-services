# Conduct cross-cutting overlay for marketing-rule-evidence

This overlay loads where the substantiation gap, the testimonial framing, the third-party-rating presentation, or the performance-presentation choices cross the antifraud "fair and balanced" threshold. The Marketing Rule's general prohibitions in Rule 206(4)-1(b) are the antifraud backbone of the rule; the conduct overlay is where the technical-compliance read meets the antifraud read.

Loaded by: `marketing-rule-evidence/SKILL.md` when `scope.cross_cutting_set` includes `conduct` or when the per-claim or per-statement-type analysis surfaces a finding that may be technically compliant on the disclosure mechanics but materially misleading in context.

Cited and section-referenced anchors live in `references/source-anchors.md`.

## What the overlay catches that disclosure-mechanic review misses

The disclosure-mechanic review reads what the rule explicitly requires: the trigger words, the prescribed time periods, the testimonial disclosure clauses, the third-party-rating disclosure clauses, the recordkeeping fields. The fair-and-balanced overlay reads what those mechanics, taken together, say in context to a reasonable recipient. A representation that ticks the disclosure boxes can still be:

- *Cherry-picked.* A performance series that includes the strong years and excludes the weak years (or that includes a particular composite snapshot but not the actual investor experience) is not fair and balanced even where the gross-and-net pairing is present and the time periods are stated.
- *Materially misleading by implication.* A claim that the firm "manages $X billion in assets" can imply discretionary advisory assets when the figure includes non-discretionary or sub-advised assets; a claim about a "flagship" strategy can imply track-record continuity that the personnel changes do not support.
- *Implicit endorsement.* A logo or association mark (a publication, an industry award, a fiduciary-conduct framework) presented in a way that implies endorsement or selection where none was made.
- *Unbalanced disclosure of risks.* A disclosure that mentions the standard risk factors but omits a risk specific to the strategy that materially shaped the period's results.

The overlay records each conduct read on its own line and pins the (b) general prohibition that operates against it.

## The general prohibitions in operation

Rule 206(4)-1(b) sets seven general prohibitions. The overlay maps the per-claim and per-statement-type findings against each prohibition where it operates:

- *(b)(1) Untrue statement of material fact.* The strongest read; a finding here is a fact the firm asserts that is not true.
- *(b)(2) Material claim presented without substantiation.* The substantiation-file finding ties here; the claim is on the page without the source-and-date trail.
- *(b)(3) Untrue or misleading implication or inference.* The cherry-picked-performance and materially-misleading-by-implication reads tie here; the words may be true but the inference is not.
- *(b)(4) Reference to specific investment advice that is not fair and balanced.* The case-study and the named-position-discussion reads tie here.
- *(b)(5) Performance results presented in a manner that is not fair and balanced.* The cherry-picked-period read, the unbalanced gross-only presentation outside the narrow exception, and the misleading-benchmark read tie here.
- *(b)(6) Otherwise materially misleading.* The catch-all; the overlay records findings that do not fit (b)(1) through (b)(5) cleanly but are nonetheless misleading.
- *(b)(7) Specific provisions on third-party-rating use* [verify exact paragraph number — the rule's general-prohibition list and the third-party-rating-specific provisions interact; pin the operative paragraph at pack date].

The overlay records the operative (b) paragraph alongside each finding so that a counsel-led review can map the antifraud reach.

## Conduct-risk taxonomy tie-back (where the firm operates one)

Many advisers and asset managers operate a conduct-risk taxonomy alongside the regulatory program. Common taxonomy entries that map to Marketing Rule findings:

- *Communication and disclosure.* The dominant taxonomy entry for marketing findings.
- *Performance representation.* The named entry for performance-presentation findings.
- *Sales practice.* Where the marketing finding is part of an acquisition-funnel design or a particular client-segment targeting.
- *Conflicts of interest.* Where a testimonial or third-party-rating use omits a material conflict.
- *Customer outcome.* Where the finding feeds a recurring complaint pattern or a redress-eligible loss.

The overlay records the firm's taxonomy tie-back per finding; the conduct-risk function classifies any conduct-event candidacy.

## Named conduct-accountable manager (where the firm operates an SMCR-equivalent regime)

For UK-licensed adviser entities or US adviser groups operating a senior-manager accountability regime, the senior manager with the prescribed responsibility for marketing or for the relevant business is a named sign-off audience. The pack records the role (not the individual) and the routing.

## Chained-finding posture

Where the Marketing Rule pack surfaces a recurring finding (the same substantiation gap across multiple advertisements; the same testimonial-disclosure failure pattern across the firm's website; the same hypothetical-performance condition unmet across a strategy's deck library), the overlay flags the chained-finding posture and routes:

- The Rule 206(4)-7 annual review picks up the recurring finding for the firm's written-compliance-program adequacy assessment.
- The CCO determines whether to escalate to the firm's audit committee or board (where applicable) under the firm's escalation framework.
- The firm's enterprise-conduct-risk function picks up the conduct-event candidacy for classification under its taxonomy.

## Conduct-specific pack template additions

The following fields are added where the conduct overlay loads:

- `finding.fair_and_balanced_read[]` — list of fair-and-balanced findings beyond the disclosure-mechanic read.
- `finding.operative_general_prohibition_paragraph` — string; the (b) paragraph the finding maps to.
- `finding.conduct_risk_taxonomy_tie_back[]` — list of conduct-risk taxonomy categories the finding touches.
- `finding.conduct_event_candidate` — boolean; if true, the finding is recommended for classification by the conduct-risk function.
- `finding.chained_finding_posture` — string; description of the recurring-finding read and the routing.
- `finding.smcr_or_equivalent_role` — string; where applicable, the role with the prescribed responsibility.

## Common pitfalls in conduct-flagged Marketing-Rule packs

- Treating "the disclosure mechanics tick the boxes" as the end of the analysis. The fair-and-balanced overlay is the antifraud backbone; technical compliance does not foreclose an antifraud finding.
- Treating cherry-picked performance as a presentation choice rather than a (b)(5) violation. Where the period selected materially affects the read, the cherry-picking is an antifraud finding.
- Missing implicit endorsements (logos, association marks, fiduciary-conduct-framework badges) because they are not labelled as endorsements. The overlay reads the visual and the placement, not just the text.
- Treating an isolated finding as one-off when the same pattern recurs across the firm's marketing inventory. The chained-finding posture is the operative read; route the recurring finding to the annual review.
- Naming the marketing-review committee as the only sign-off audience and missing the conduct-accountable manager role where the firm operates an SMCR-equivalent regime.
