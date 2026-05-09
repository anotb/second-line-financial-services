# Troubleshooting: exam-brief

The exam-brief is the engagement playbook the regulatory affairs lead and head of compliance run during an active examination. It sits next to the substantive readiness pack (which lives in the sector skills `banking-supervision-readiness` and `adviser-exam-readiness`); confusion between the two is the most common defect this skill produces. Other recurring defects below.

## 1. Running exam-brief when the sector readiness skill is the right tool

**Symptom**: A full-scope OCC bank exam or a substantive SEC adviser exam comes through the door, and the team produces an exam-brief artifact instead of the sector-readiness sprint. The artifact reads as a thin engagement playbook with no substantive obligation-by-obligation status mapping.

**Why it happens**: The skill description's "Best for" list got read; the "Not the right tool when" list did not.

**Resolution**:
- For a full-scope federal banking exam at a bank under Heightened Standards, route to `sector-plugins/banking-risk-compliance/banking-supervision-readiness`. That readiness sprint carries the substantive scaffolding for capital, BSA/AML, fair lending, CRA, and the Heightened Standards expectations.
- For a substantive SEC adviser, BD, or investment-company exam, route to `sector-plugins/capital-markets-asset-management-compliance/adviser-exam-readiness`. That readiness sprint carries IAA Rule 206(4)-7 cadence, marketing rule, custody rule, books-and-records, and Form ADV-specific scaffolding.
- Use exam-brief when the engagement is targeted, topic-specific, horizontal, or for-cause and the engagement-side mechanics are the operative scaffolding.
- Default to chaining: exam-brief produces the engagement playbook; the sector skill produces the substantive readiness pack. The two artifacts read together for full-scope sector engagements where both skills run.

## 2. Sector overlay defaulted to banking by reflex

**Symptom**: A CFPB non-bank exam at a fintech, a state DOI market-conduct exam at an insurer, or an SEC EXAMS adviser exam comes through, and the brief loads `references/sector-overlays/banking.md` because banking was the practitioner's home territory. The MRA / MRIA convention shows up in a context where it does not exist; the engagement-playbook section quotes federal banking response windows that do not apply.

**Why it happens**: Banking is the home territory for many financial-services practitioners; the overlay loads on autopilot.

**Resolution**:
- Sector overlay loads from the scope record's `sector_overlay_set`, not from practitioner habit.
- If `sector_overlay_set = [insurance]`, load `references/sector-overlays/insurance.md` and remove banking-specific framing (MRA / MRIA, 12 CFR Part 4 CSI regime) from the brief.
- If `sector_overlay_set = [capital-markets]`, load `references/sector-overlays/capital-markets.md`; the response-window default is 30 days from deficiency letter for SEC EXAMS and varies for FINRA, not the banking convention.
- If `sector_overlay_set = [payments-fintech]`, load `references/sector-overlays/payments-fintech.md`; CFPB non-bank uses Matters Requiring Attention by parallel convention but state money-transmitter exams use state-specific findings mechanisms.
- A multi-track engagement (e.g., a fintech with a CFPB non-bank exam and a parallel state money-transmitter cycle exam) loads two overlays and carries each engagement separately in the brief.

## 3. The out-of-scope list is empty

**Symptom**: Mid-exam, the examiner expands a request line to cover a product or business unit the firm reasonably understood to be out of scope. The firm has no written scope confirmation to point at; the engagement absorbs the expansion without challenge.

**Why it happens**: Scope confirmation went unwritten or got buried in email; the brief did not capture it.

**Resolution**:
- Capture the scope confirmation in writing in the `scope_window.scope_confirmation_source` field with a date and a pointer to the document.
- The `scope_window.out_of_scope` array carries what the regulator confirmed in writing as out of scope. An empty array signals the conversation has not happened. Force the conversation early.
- When the examiner expands scope mid-exam, request a written scope amendment. The amended scope goes in a new revision of the brief, dated, with the expansion noted. The firm gets a clean record of what changed and when.
- For SEC EXAMS engagements, the document request letter is the operative scope reference. For OCC, FRB, FDIC, and CFPB engagements, the scope memorandum or first-day letter is operative.

## 4. CSI handled like ordinary documents

**Symptom**: Prior-cycle supervisory letters, examination reports, or MRA correspondence get circulated inside the firm to a wide population for "context." A subsequent records subpoena or M&A diligence ask sweeps in the CSI; the firm is in violation of the regulator's CSI regime.

**Why it happens**: CSI looks like a normal firm document until you read the rule. The regulator's CSI rules (12 CFR Part 4 Subpart C for OCC, Part 261 for FRB, Part 309 for FDIC, Part 1070 Subpart D for CFPB) restrict the firm's onward sharing.

**Resolution**:
- `document_handling.confidential_supervisory_information_handled = true` triggers a controlled CSI-handling protocol: need-to-know population, access logging, no onward sharing without regulator authorisation.
- Where the engagement references a prior cycle's CSI, the brief notes the source and the access-logging posture.
- Where the firm believes a legitimate need-to-know person outside the standard population must see CSI (outside counsel, board members, M&A counterparty under NDA), counsel evaluates whether regulator authorisation is required under the applicable CSI rule.
- Train the engagement team on CSI handling at engagement kickoff. CSI handling is the most common quiet-but-serious posture failure on bank-side engagements.

## 5. Privilege posture set per-document at the last minute

**Symptom**: The production wave is due in 24 hours; counsel is reviewing 400 documents for privilege; redactions are inconsistent; the privilege log is hand-built; the team works through the weekend.

**Why it happens**: Privilege posture got set per-document at the last minute rather than per-topic in advance.

**Resolution**:
- `document_handling.privilege_review_lead_role` names the responsible role; `privilege_log_required` and `redaction_workflow` set the posture in advance.
- For each request-list item, set `privilege_posture` at the item level (`producible`, `redacted-and-producible`, `privileged-withhold`, `csi-held-by-regulator`, `under-review`). Items in `under-review` get counsel attention early, not late.
- Recurring privileged-territory categories: internal-investigation work product, root-cause-analysis materials counsel-supervised, attorney-client communications on regulatory questions, work-product on litigation-adjacent matters. Pre-categorise.
- For SEC EXAMS engagements, the privilege log accompanies any redacted production; build the log inline as redactions happen, not retrospectively.
- For FINRA Rule 8210 production, the privilege posture is contestable; counsel posture is the operative driver.

## 6. Anticipated reviewer questions that read as FAQs

**Symptom**: The `anticipated_reviewer_questions` section reads as a generic FAQ pulled from a vendor template. Each question is plausible but not grounded; talking points are generic.

**Why it happens**: The questions were drafted from "what an examiner would probably ask" rather than from current supervisory priorities and recent enforcement themes.

**Resolution**:
- Each question carries `source_pattern` naming the basis: a specific examination priorities letter, a specific risk alert, a specific Supervisory Highlights edition, a specific public consent order, a peer-firm experience.
- For OCC, FRB, FDIC engagements, the most recent semi-annual operating plan or supervisory priorities communication drives the topic mix.
- For CFPB engagements (bank or non-bank), the most recent Supervisory Highlights edition is the operative source.
- For SEC EXAMS engagements, the most recent annual examination priorities letter and the recent risk alerts drive the topic mix; the off-channel-communications enforcement pattern since 2021 has its own gravity.
- For FINRA engagements, the most recent annual Regulatory Oversight Report drives the topic mix.
- Talking points are firm-side response postures, not scripts. A talking point of one or two sentences is enough; longer is over-engineered.

## 7. Self-identified issues suppressed because they look bad

**Symptom**: The team strips known gaps from the brief because they would "give the examiner ammunition." The examiner finds the gaps anyway; the firm loses the credibility it would have had from self-identification.

**Why it happens**: The instinct to minimise findings overrides the discipline of self-identification.

**Resolution**:
- Self-identification is generally a credibility signal with examiners across regulators (OCC, FRB, FDIC, CFPB, SEC, FINRA, state DOIs all reward it). Suppressing material gaps backfires.
- `supervisory_history.self_identified_issues` captures the gaps the firm intends to surface proactively. Each issue carries a topic, a remediation status with a date, and an owner role.
- The brief's executive summary references the self-identified issues as a credibility item; the response-posture section pre-positions the firm's path to closure.
- Where a gap is genuinely sensitive (privileged investigation in flight, M&A-restricted), counsel sets the posture; surface the existence of the work, not the privileged details.

## 8. Open MRA or MRIA without an owner and a date

**Symptom**: The `supervisory_history.open_mras` array carries entries with `status: open` but no `due_date`, no `owner_role`. The brief reads as drift; the examiner reads it the same way.

**Why it happens**: The closure path was not set when the MRA was issued; the issue lived in an issue tracker without firm-side ownership.

**Resolution**:
- Every open MRA, MRIA, or consent-order milestone carries an owner role and a due date in the brief. Missing either is a defect.
- The closure-submission path runs through the firm's issue-management process; the brief references the closure submission timing.
- Where the closure is in flight and the exam window straddles the closure submission, the brief notes the timing in the `anticipated_reviewer_questions` section.
- For consent orders, the milestone status reads against the order's articles; the brief carries the article-by-article status.

## 9. Response window calculated from the wrong clock

**Symptom**: The team calculates the response window from the exit-meeting date rather than from the receipt of the supervisory letter or deficiency letter; the response is filed late, or the team scrambles to make a deadline that never applied.

**Why it happens**: The exit meeting feels like the close of the exam; in fact, the formal record-of-examination or supervisory letter is the operative trigger.

**Resolution**:
- `response_posture.response_due_calculation_basis` names the operative clock: receipt of supervisory letter (federal banking convention); receipt of deficiency letter (SEC EXAMS); receipt of exam report (FINRA cycle); receipt of CFPB supervisory letter (CFPB non-bank); receipt of state DOI examination report (insurance).
- Where the regulator has stated otherwise in writing, follow the written statement and update the field.
- For consent orders and stipulations, the clock is set by the order's articles, not by general response convention.

## 10. Engagement-scope record stale or missing

**Symptom**: The brief was drafted from yesterday's understanding; today the regulator has confirmed an expanded scope or a participant office has joined the team. The brief no longer matches the engagement.

**Why it happens**: The scope record was treated as a kickoff artifact rather than a living record. The brief consumed an old version.

**Resolution**:
- Engagement-scope is a status, not a fixed truth. Re-emit the scope record after any material change; re-emit the exam-brief consuming the updated scope.
- Standing scope review in the engagement steering cadence (daily during fieldwork, weekly otherwise).
- Where the brief is run without an scope record at all, ask the four questions (regulator, exam type, scope window, source posture) and default to public posture if the practitioner declines. Note in the brief that scope was not formalised.

## 11. The brief is treated as the deliverable, not the working artifact

**Symptom**: The brief gets drafted, signed off, and then sits unread for the duration of the exam. The team runs the exam from email, calendar, and informal notes.

**Why it happens**: The brief was treated as a one-time artifact for the kickoff meeting rather than as the operative working artifact for the exam window.

**Resolution**:
- The brief is the operative working artifact. The request-list mapping is the daily standup; the interview-prep section is the prep brief for each interview; the response-posture section is the contingency plan for the close.
- Update the brief continuously: status changes on request-list items, additions to the production log, lessons learned from in-flight examiner signals, additions to anticipated reviewer questions as new themes emerge.
- The post-exam after-action record consumes the final state of the brief; the next cycle's brief starts from the previous cycle's after-action.

## 12. Boundary with sector-specific exam-readiness skills not respected

**Symptom**: The brief duplicates substantive obligation-by-obligation status mapping that the sector readiness skill is producing in parallel. Two artifacts say almost the same thing with subtle inconsistencies; the examiner notices.

**Why it happens**: The boundary between exam-brief and the sector readiness skills was not respected; both skills produced overlapping content.

**Resolution**:
- exam-brief is the engagement playbook: regulator, scope confirmation, document handling, points of contact, request-list mapping, interview prep, supervisory history, response posture, post-exam follow-up.
- The sector readiness skill is the substantive readiness pack: obligation-by-obligation status, control-by-control evidence, gap analysis against the rule, remediation roadmap.
- The two artifacts cross-reference; they do not duplicate.
- Where a sector readiness skill has produced the substantive pack, the brief's request-list mapping points at the pack's evidence inventory rather than restating it.
- Where exam-brief is run alongside `scoping`, `regulatory-impact-assessment`, `rule-to-obligation-map`, `implementation-plan`, or `policy-diff` in the same plugin, the brief consumes the upstream artifacts and does not restate them.
