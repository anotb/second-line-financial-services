# Conduct cross-cutting overlay for fair-lending-test-plan

When the engagement-scope record flags `conduct` for the fair-lending test plan, this overlay adds conduct-risk content to named test-plan sections. Conduct in second-line vocabulary is not the same as fairness as a model property; it is the customer-outcome lens, the named-manager accountability lens, and the regulatory-engagement lens. The overlap with fair lending is real but not total: every fair-lending defect is potentially a conduct defect, but not every conduct defect is a fair-lending defect.

Loaded by: `fair-lending-test-plan/SKILL.md` when `engagement_scope.cross_cutting_set` includes `conduct`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for conduct-flagged fair-lending test plans

### 1. UDAAP overlap is named explicitly

The CFPB UDAAP framework (sections 1031 and 1036 of the Consumer Financial Protection Act) overlaps fair-lending review on themes such as:

- Marketing claims and dark-pattern design (deception or unfairness prong).
- Steering practices that channel customers into less-favorable products (unfairness or abusiveness prong).
- Adverse-action notices that obscure the actual reason (deception prong, on top of the Reg B §1002.9 specificity obligation).
- Servicing and loss-mitigation conduct that produces materially-different outcomes for similarly-situated customers (unfairness prong).

Where the fair-lending test plan covers any of these decision points, the conduct overlay records the UDAAP prong in scope alongside the fair-lending hypothesis. The two regimes can be tested together; the test memos should separate the findings cleanly.

### 2. Customer-outcome lens supplements the protected-class lens

Conduct framing extends the test population beyond the protected-class lens. Customer-outcome disparity across policy-relevant segments (rural, low-balance, digital-only, English-as-second-language, recent-immigrant cohorts where lawful to consider) is a conduct concern even where the protected-class disparity tests pass. The fair-lending test plan with a conduct overlay typically adds:

- A customer-outcome subsection in scope that names the policy-relevant segments under review.
- A customer-outcome regression alongside the protected-class regression (same model, different segment indicators).
- A complaint-theme cross-reference where complaint signals indicate customer-outcome harm in segments that the protected-class lens does not catch.

### 3. Complaint linkage is load-bearing

Complaint themes are a recurring scope-trigger for the fair-lending test plan. The conduct overlay makes the linkage explicit: the test plan records the upstream complaint-theme-analysis output as a scope trigger and records the downstream complaint-rate-monitoring posture as a controls-hypothesis item. Drift in complaint rates and complaint codes is a leading indicator of customer-outcome harm.

Cross-reference complaint-theme-analysis explicitly in `tests[].cross_reference_skills` and in the assumptions block.

### 4. Named conduct-accountable manager

For UK-licensed firms in SMCR scope, the senior manager with the prescribed responsibility for the relevant business is a named sign-off audience. For non-UK firms, the firm's conduct framework names a manager (often the head of the relevant business or the head of consumer / customer); the plan names the role, not the individual. The fair-lending committee approval and the conduct-accountable manager sign-off are separable items; the plan is explicit about which is which.

### 5. Regulatory-engagement events as plan triggers

A regulatory-engagement event (CFPB inquiry, FCA Section 166 review, state DOI inquiry, fair-lending exam finding) is a conduct re-validation trigger. The plan records:

- The event that triggered the plan refresh.
- The regulator-engagement counsel posture (privilege, work-product, response-file management).
- The reporting-plan field for `regulator_ready_summary` is typically true under this trigger.

## Conduct-specific test-plan template additions

- `scope.policy_relevant_segments[]` — list of policy-relevant segments under conduct review (rural, low-balance, English-as-second-language, etc.) where lawful to consider.
- `tests[].udaap_prong` — enum (`unfairness`, `deception`, `abusiveness`, `n_a`) where the test addresses a UDAAP prong alongside fair-lending.
- `tests[].cross_reference_skills[]` — list of related skills (complaint-theme-analysis, marketing-claim-review, adverse-action-review).
- `controls_hypothesis[]` — complaint-rate monitoring control listed where the conduct overlay is loaded.
- `committee_approval_gate.conduct_accountable_manager_role` — role under SMCR or the firm's conduct framework, distinct from the fair-lending committee chair.
- `reporting_plan.conduct_committee_read` — boolean; if true, the conduct or customer-outcome committee gets a read alongside the fair-lending committee.

## Common pitfalls in conduct-flagged fair-lending test plans

- Conflating fair-lending review with UDAAP review and producing a test memo that does not separate the findings cleanly; counsel and the regulator both need the seams visible.
- Extending the protected-class lens into customer-outcome segments without recording the test-framing change; the vocabulary matters because the legal regime differs.
- Treating complaint themes as a noisy input rather than as a leading indicator; complaint-rate and complaint-code drift are signal, not noise.
- Missing the named conduct-accountable manager on the sign-off audience list; the conduct framework names a role separate from the model owner and separate from the fair-lending committee chair.
- Writing the plan without recording the regulator-engagement trigger where one exists; the response-file posture and the privilege posture both turn on whether the plan is responding to engagement or running on the routine cycle.
