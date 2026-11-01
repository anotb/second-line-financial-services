# cross-cutting

One section per topic. Read only the sections the scope calls for.

## conduct

### Conduct cross-cutting overlay for fair-lending-test-plan

When the scope record flags `conduct` for the fair-lending test plan, this overlay adds conduct-risk content to named test-plan sections. Conduct in second-line vocabulary is not the same as fairness as a model property; it is the customer-outcome lens, the named-manager accountability lens, and the regulatory-engagement lens. The overlap with fair lending is real but not total: every fair-lending defect is potentially a conduct defect, but not every conduct defect is a fair-lending defect.

Loaded by: `fair-lending-test-plan/SKILL.md` when `scope.cross_cutting_set` includes `conduct`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What changes for conduct-flagged fair-lending test plans

##### 1. UDAAP overlap is named explicitly

The CFPB UDAAP framework (sections 1031 and 1036 of the Consumer Financial Protection Act) overlaps fair-lending review on themes such as:

- Marketing claims and dark-pattern design (deception or unfairness prong).
- Steering practices that channel customers into less-favorable products (unfairness or abusiveness prong).
- Adverse-action notices that obscure the actual reason (deception prong, on top of the Reg B §1002.9 specificity obligation).
- Servicing and loss-mitigation conduct that produces materially-different outcomes for similarly-situated customers (unfairness prong).

Where the fair-lending test plan covers any of these decision points, the conduct overlay records the UDAAP prong in scope alongside the fair-lending hypothesis. The two regimes can be tested together; the test memos should separate the findings cleanly.

##### 2. Customer-outcome lens supplements the protected-class lens

Conduct framing extends the test population beyond the protected-class lens. Customer-outcome disparity across policy-relevant segments (rural, low-balance, digital-only, English-as-second-language, recent-immigrant cohorts where lawful to consider) is a conduct concern even where the protected-class disparity tests pass. The fair-lending test plan with a conduct overlay typically adds:

- A customer-outcome subsection in scope that names the policy-relevant segments under review.
- A customer-outcome regression alongside the protected-class regression (same model, different segment indicators).
- A complaint-theme cross-reference where complaint signals indicate customer-outcome harm in segments that the protected-class lens does not catch.

##### 3. Complaint linkage is load-bearing

Complaint themes are a recurring scope-trigger for the fair-lending test plan. The conduct overlay makes the linkage explicit: the test plan records the upstream complaint-theme-analysis output as a scope trigger and records the downstream complaint-rate-monitoring posture as a controls-hypothesis item. Drift in complaint rates and complaint codes is a leading indicator of customer-outcome harm.

Cross-reference complaint-theme-analysis explicitly in `tests[].cross_reference_skills` and in the assumptions block.

##### 4. Named conduct-accountable manager

For UK-licensed firms in SMCR scope, the senior manager with the prescribed responsibility for the relevant business is a named sign-off audience. For non-UK firms, the firm's conduct framework names a manager (often the head of the relevant business or the head of consumer / customer); the plan names the role, not the individual. The fair-lending committee approval and the conduct-accountable manager sign-off are separable items; the plan is explicit about which is which.

##### 5. Regulatory-engagement events as plan triggers

A regulatory-engagement event (CFPB inquiry, FCA Section 166 review, state DOI inquiry, fair-lending exam finding) is a conduct re-validation trigger. The plan records:

- The event that triggered the plan refresh.
- The regulator-engagement counsel posture (privilege, work-product, response-file management).
- The reporting-plan field for `regulator_ready_summary` is typically true under this trigger.

#### Conduct-specific test-plan template additions

- `scope.policy_relevant_segments[]` — list of policy-relevant segments under conduct review (rural, low-balance, English-as-second-language, etc.) where lawful to consider.
- `tests[].udaap_prong` — enum (`unfairness`, `deception`, `abusiveness`, `n_a`) where the test addresses a UDAAP prong alongside fair-lending.
- `tests[].cross_reference_skills[]` — list of related skills (complaint-theme-analysis, marketing-claim-review, adverse-action-review).
- `controls_hypothesis[]` — complaint-rate monitoring control listed where the conduct overlay is loaded.
- `committee_approval_gate.conduct_accountable_manager_role` — role under SMCR or the firm's conduct framework, distinct from the fair-lending committee chair.
- `reporting_plan.conduct_committee_read` — boolean; if true, the conduct or customer-outcome committee gets a read alongside the fair-lending committee.

#### Common pitfalls in conduct-flagged fair-lending test plans

- Conflating fair-lending review with UDAAP review and producing a test memo that does not separate the findings cleanly; counsel and the regulator both need the seams visible.
- Extending the protected-class lens into customer-outcome segments without recording the test-framing change; the vocabulary matters because the legal regime differs.
- Treating complaint themes as a noisy input rather than as a leading indicator; complaint-rate and complaint-code drift are signal, not noise.
- Missing the named conduct-accountable manager on the sign-off audience list; the conduct framework names a role separate from the model owner and separate from the fair-lending committee chair.
- Writing the plan without recording the regulator-engagement trigger where one exists; the response-file posture and the privilege posture both turn on whether the plan is responding to engagement or running on the routine cycle.

## privacy

### Privacy cross-cutting overlay for fair-lending-test-plan

When the scope record flags `privacy` for the fair-lending test plan, this overlay addresses how customer data used in fair-lending testing is handled. Fair-lending testing pulls applicant data, model features, and demographic-proxy inputs out of systems of record, moves the data to an analytics environment, and processes it for statistical analysis. That movement and processing sits inside the firm's privacy program; the overlay names the seams.

Loaded by: `fair-lending-test-plan/SKILL.md` when `scope.cross_cutting_set` includes `privacy`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- GLBA Safeguards Rule (16 CFR Part 314 for FTC-supervised; 12 CFR Part 30 Appendix B for OCC; 12 CFR Part 364 Appendix B for FDIC) — non-public personal information (NPI) handled in fair-lending testing.
- Federal banking regulator guidance on customer data use in compliance testing.
- State privacy laws (CCPA / CPRA, VCDPA, CTDPA, and the rolling roster of state laws) where the institution operates in those jurisdictions.
- ECOA Reg B §1002.5 limits on requests for protected-basis information; §1002.13 monitoring information rules.
- The firm's privacy program (privacy notice, internal data-use policy, data-classification scheme, data-loss-prevention posture).

#### What changes for privacy-flagged fair-lending test plans

##### 1. Data-handling posture is recorded per data requirement

Each data requirement in the test plan carries a privacy-handling subsection:

- Sensitivity classification (NPI under GLBA, public, confidential, internal-only).
- Movement posture (does the data move to an analytics environment, and if so, which one and under what controls).
- Retention period for the test-execution artifacts (raw extract, analytic dataset, test memo).
- Re-identification posture (is the data tokenised or pseudonymised before analysis, and what is the re-identification path for follow-up).

The data-required block in the test plan template extends to include these fields under the privacy overlay.

##### 2. BISG inputs and demographic proxy data

The BISG proxy method requires applicant name and address. Both are NPI under GLBA. The test plan records:

- The system of record for name and address (typically the application or origination platform).
- The mechanism for joining the BISG proxy assignment back to the test population (typically a hashed identifier).
- The retention posture on the BISG-proxy-assignment table; it is itself sensitive (associates the institution's customers with race-ethnicity probability distributions).
- The access control on the BISG-proxy-assignment table; restricted to fair-lending-analytics roles.

Where the test plan uses geocoded proxy or surname-only proxy as a sensitivity analysis, the same handling applies.

##### 3. HMDA self-reported demographics

HMDA monitoring data collected under §1002.13 is in the LAR. The LAR is a regulatory submission with established access and handling expectations. The test plan inherits the LAR-handling posture; no incremental data-movement question typically arises for mortgage tests beyond what the HMDA program already addresses.

##### 4. Counsel-direction and privilege intersection

Where outside counsel directs the fair-lending review for privilege, the privacy program and the privilege program intersect. The data-handling artifacts (extracts, analytic datasets, test memos) typically carry attorney-client-privileged or attorney-work-product designation; the data-handling posture must accommodate the privilege framework (limited access, marked artifacts, restricted distribution lists).

##### 5. Vendor analytics environments

Where the institution uses a vendor analytics environment (cloud-based statistical-analysis platform, fair-lending-analytics SaaS) for test execution, the privacy posture extends to the vendor:

- DPA or BAA posture with the vendor (whichever applies).
- Vendor-side data-residency and data-deletion confirmation.
- Vendor-side access-control posture.
- Vendor-side incident-response integration with the institution.

##### 6. Customer-rights workflow

Where the institution operates in a state-privacy-law footprint (CCPA / CPRA, VCDPA, etc.), the customer-rights workflow (right to know, right to delete) reaches the data used in fair-lending testing. The test plan records:

- Whether the test population is subject to a customer-rights request received during the test cycle.
- The handling posture for a customer-rights-request affecting test data (the test data is typically retained under the regulatory-recordkeeping exception or the legal-process exception during the test cycle).

#### Privacy-specific test-plan template additions

- `tests[].data_required[].sensitivity_classification` — NPI / public / confidential / internal-only.
- `tests[].data_required[].movement_posture` — string describing where the data moves and under what controls.
- `tests[].data_required[].retention_period` — string per the test-execution lifecycle.
- `tests[].data_required[].vendor_dpa_or_baa_reference` — pointer where a vendor environment is in scope.
- `committee_approval_gate.privacy_office_coordination` — boolean; if true, the privacy office is a coordinating reviewer on the plan.
- `assumptions_and_dependencies` — privacy-handling assumptions (analytic environment posture, retention, re-identification path) recorded explicitly.

#### Common pitfalls in privacy-flagged fair-lending test plans

- Treating the BISG-proxy-assignment table as routine analytics output; it is itself sensitive and access-controlled.
- Moving applicant-level data to a vendor analytics environment without a current DPA in place; the test execution sits on shaky ground.
- Conflating the privilege posture with the privacy posture; the two regimes overlap but they are separate frameworks and the artifacts carry separate marks.
- Missing the customer-rights-workflow integration where state privacy laws apply; the firm's privacy operations need to know about the test population to handle in-flight requests.
- Defaulting to "the data is anonymised" without recording the actual de-identification or pseudonymisation method; ECOA monitoring data and BISG-derived proxies are sensitive even when account-identifier-stripped.
- Treating the test memo as a routine document with the rest of the analytics output; the test memo typically carries privilege and is handled accordingly.
