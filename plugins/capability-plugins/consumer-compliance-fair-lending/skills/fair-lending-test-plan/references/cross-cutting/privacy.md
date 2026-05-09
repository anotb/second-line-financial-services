# Privacy cross-cutting overlay for fair-lending-test-plan

When the scope record flags `privacy` for the fair-lending test plan, this overlay addresses how customer data used in fair-lending testing is handled. Fair-lending testing pulls applicant data, model features, and demographic-proxy inputs out of systems of record, moves the data to an analytics environment, and processes it for statistical analysis. That movement and processing sits inside the firm's privacy program; the overlay names the seams.

Loaded by: `fair-lending-test-plan/SKILL.md` when `scope.cross_cutting_set` includes `privacy`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- GLBA Safeguards Rule (16 CFR Part 314 for FTC-supervised; 12 CFR Part 30 Appendix B for OCC; 12 CFR Part 364 Appendix B for FDIC) — non-public personal information (NPI) handled in fair-lending testing.
- Federal banking regulator guidance on customer data use in compliance testing.
- State privacy laws (CCPA / CPRA, VCDPA, CTDPA, and the rolling roster of state laws) where the institution operates in those jurisdictions.
- ECOA Reg B §1002.5 limits on requests for protected-basis information; §1002.13 monitoring information rules.
- The firm's privacy program (privacy notice, internal data-use policy, data-classification scheme, data-loss-prevention posture).

## What changes for privacy-flagged fair-lending test plans

### 1. Data-handling posture is recorded per data requirement

Each data requirement in the test plan carries a privacy-handling subsection:

- Sensitivity classification (NPI under GLBA, public, confidential, internal-only).
- Movement posture (does the data move to an analytics environment, and if so, which one and under what controls).
- Retention period for the test-execution artifacts (raw extract, analytic dataset, test memo).
- Re-identification posture (is the data tokenised or pseudonymised before analysis, and what is the re-identification path for follow-up).

The data-required block in the test plan template extends to include these fields under the privacy overlay.

### 2. BISG inputs and demographic proxy data

The BISG proxy method requires applicant name and address. Both are NPI under GLBA. The test plan records:

- The system of record for name and address (typically the application or origination platform).
- The mechanism for joining the BISG proxy assignment back to the test population (typically a hashed identifier).
- The retention posture on the BISG-proxy-assignment table; it is itself sensitive (associates the institution's customers with race-ethnicity probability distributions).
- The access control on the BISG-proxy-assignment table; restricted to fair-lending-analytics roles.

Where the test plan uses geocoded proxy or surname-only proxy as a sensitivity analysis, the same handling applies.

### 3. HMDA self-reported demographics

HMDA monitoring data collected under §1002.13 is in the LAR. The LAR is a regulatory submission with established access and handling expectations. The test plan inherits the LAR-handling posture; no incremental data-movement question typically arises for mortgage tests beyond what the HMDA program already addresses.

### 4. Counsel-direction and privilege intersection

Where outside counsel directs the fair-lending review for privilege, the privacy program and the privilege program intersect. The data-handling artifacts (extracts, analytic datasets, test memos) typically carry attorney-client-privileged or attorney-work-product designation; the data-handling posture must accommodate the privilege framework (limited access, marked artifacts, restricted distribution lists).

### 5. Vendor analytics environments

Where the institution uses a vendor analytics environment (cloud-based statistical-analysis platform, fair-lending-analytics SaaS) for test execution, the privacy posture extends to the vendor:

- DPA or BAA posture with the vendor (whichever applies).
- Vendor-side data-residency and data-deletion confirmation.
- Vendor-side access-control posture.
- Vendor-side incident-response integration with the institution.

### 6. Customer-rights workflow

Where the institution operates in a state-privacy-law footprint (CCPA / CPRA, VCDPA, etc.), the customer-rights workflow (right to know, right to delete) reaches the data used in fair-lending testing. The test plan records:

- Whether the test population is subject to a customer-rights request received during the test cycle.
- The handling posture for a customer-rights-request affecting test data (the test data is typically retained under the regulatory-recordkeeping exception or the legal-process exception during the test cycle).

## Privacy-specific test-plan template additions

- `tests[].data_required[].sensitivity_classification` — NPI / public / confidential / internal-only.
- `tests[].data_required[].movement_posture` — string describing where the data moves and under what controls.
- `tests[].data_required[].retention_period` — string per the test-execution lifecycle.
- `tests[].data_required[].vendor_dpa_or_baa_reference` — pointer where a vendor environment is in scope.
- `committee_approval_gate.privacy_office_coordination` — boolean; if true, the privacy office is a coordinating reviewer on the plan.
- `assumptions_and_dependencies` — privacy-handling assumptions (analytic environment posture, retention, re-identification path) recorded explicitly.

## Common pitfalls in privacy-flagged fair-lending test plans

- Treating the BISG-proxy-assignment table as routine analytics output; it is itself sensitive and access-controlled.
- Moving applicant-level data to a vendor analytics environment without a current DPA in place; the test execution sits on shaky ground.
- Conflating the privilege posture with the privacy posture; the two regimes overlap but they are separate frameworks and the artifacts carry separate marks.
- Missing the customer-rights-workflow integration where state privacy laws apply; the firm's privacy operations need to know about the test population to handle in-flight requests.
- Defaulting to "the data is anonymised" without recording the actual de-identification or pseudonymisation method; ECOA monitoring data and BISG-derived proxies are sensitive even when account-identifier-stripped.
- Treating the test memo as a routine document with the rest of the analytics output; the test memo typically carries privilege and is handled accordingly.
