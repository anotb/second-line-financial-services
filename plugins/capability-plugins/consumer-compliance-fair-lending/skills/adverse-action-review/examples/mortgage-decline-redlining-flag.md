# Example: HMDA-reportable mortgage decline review with redlining flag

## Input description

A national bank's mortgage origination platform issued adverse-action notices on 1,400 declined HMDA-reportable applications in the prior quarter. The fair-lending lead asks for a §1002.9 review of the population, with the disparate-impact panel using HMDA self-reported demographics rather than BISG (mortgage product, self-reported demographics available under §1002.13). Sector overlay: banking. Cross-cutting overlay: privacy.

## Output sketch

Population panel records 1,400 declines, prior quarter, HMDA-reportable mortgage (first-lien purchase, refi, junior-lien refi, home-improvement, HELOC), with the §1002.2(c) action category split (1,180 outright denials, 145 counteroffers not accepted, 75 incomplete-application notices). Sample frame is 100% review on counteroffers and incompletes (smaller populations, higher defect rate historically), 200-decision random sample on outright denials.

The §1002.9 timing-compliance panel surfaces nine decisions where the notice was sent on day 33 from the completed-application date — clean breach of the 30-day clock under §1002.9(a)(1). Evidence trail traces the breach to an LOS routing defect that occurred during a system upgrade. All nine are in the review's outright-denial subset.

The §1002.9 content-compliance panel surfaces a recurring "credit application incomplete" reason cited on 22 decisions where the application was actually complete (notice template defect; the §1002.9(c) incomplete-application clock was applied where it should not have been). The Staff Commentary on specificity treats this as a content defect because the cited reason is not accurate. Notices for those 22 decisions are non-compliant.

The disparate-impact panel uses HMDA self-reported demographics directly. The decline-rate disparity for one MSA is 4.2x the institution's footprint average for the protected-class cohort, with marketing-distribution evidence showing thin branch coverage and minimal direct-mail volume to majority-minority census tracts within the MSA. The pattern matches DOJ Combatting Redlining Initiative consent-order patterns; the panel surfaces this as a redlining red flag, applies the BISG caveat where BISG-only segments were also analyzed, and routes the finding-grade work to `fair-lending-test-plan` and the bank's CRA officer (the MSA overlaps the bank's CRA assessment area).

The AI / complex-model findings section is short — the underlying mortgage AUS uses Desktop Underwriter, not an internal AI / ML model, so the Circulars 2022-03 / 2023-03 framing applies narrowly to the AUS-deny pass-through pattern (which the bureau has flagged supervisorily) and to the bank's own override layer. The memo records the AUS-recommendation field as a control covariate for any subsequent regression but flags that AUS-recommendation is itself in the fair-lending perimeter per the banking sector overlay.

Recommended actions:

1. Notice re-issuance on the nine timing breaches with counsel-reviewed language. Owner: consumer compliance second-line. Control: notice issuance control. Due: 14 days.
2. Notice re-issuance on the 22 content defects (incomplete-application reason cited on complete applications) with counsel-reviewed language. Owner: consumer compliance second-line. Due: 30 days.
3. LOS routing-defect remediation that produced the timing breaches. Owner: mortgage operations. Control: LOS notice-trigger control. Due: per IT release cycle, with interim manual control.
4. Fair-lending escalation on the 4.2x MSA disparity to `fair-lending-test-plan` for regression and comparative file review; CRA officer coordination given assessment-area overlap. Owner: fair-lending lead + CRA officer. Cross-route: fair-lending committee.
5. Comparative file review on the override layer where the AUS-recommendation pass-through pattern is in scope. Owner: fair-lending statistician.

The memo closes with two open questions for counsel (DOJ Combatting Redlining Initiative posture given the MSA disparity; whether voluntary regulator engagement is appropriate in advance of formal testing) and the source-trace table tying each claim to §1002.9, the Staff Commentary, FHA §3605, the FFIEC Interagency Fair Lending Examination Procedures, and the DOJ initiative.

## Why this scenario matters

It exercises the dwelling-secured perimeter (FHA + ECOA) where HMDA self-reported demographics are the right proxy choice rather than BISG. It produces the timing-breach pattern (most common §1002.9 defect) and the inaccurate-reason pattern (where the §1002.9(c) clock was misapplied). It also shows how the disparate-impact panel surfaces a redlining red flag that routes to fair-lending testing and CRA coordination — the adverse-action review is the most common entry point to a redlining finding, but the finding follows the formal test.

Pattern derived from public CFPB / DOJ redlining consent-order themes. No named institution.
