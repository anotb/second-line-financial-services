# Troubleshooting: regulatory-impact-assessment

The impact assessment is the second line's first read on a regulatory item; mistakes at this stage shape every downstream skill (rule-to-obligation-extraction, policy-diff, implementation-plan, exam-brief). The defects below recur across teams and across regulators.

## 1. Treating the assessment as a legal interpretation

**Symptom**: The assessment opines on whether the rule applies to the firm as a matter of law, characterises a regulator's interpretive position as binding, or settles an ambiguous-applicability question without legal review. Counsel reads the assessment and rewrites the in-scope-determination section to remove the legal conclusion.

**Why it happens**: The line between scoping the rule and interpreting it is thin under time pressure; the practitioner reaches for a conclusion when the question warrants a routed open question.

**Resolution**:
- The skill names obligations and routes open questions; it does not opine on whether the rule applies as a matter of law.
- Where applicability is ambiguous (a threshold question, an activity-classification question, a state-by-state-adoption question, an AI-system definitional question), the assessment carries an `open_questions` entry routed to legal with a due date.
- The `in_scope_rationale` field cites the source pin and names the firm-side facts; it does not interpret the rule's text beyond what the source itself says.
- Where the rule's interpretive position is the question (a CFPB Circular, a regulator speech, a consent-order-pattern theme), the assessment characterises the regulator's position with quoted or paraphrased language and routes interpretive questions to qualified review.

## 2. Loading every sector and cross-cutting overlay for completeness

**Symptom**: The assessment loads all four sector overlays and all four cross-cutting overlays; the assessment reads as a generic compendium with no operative direction. The strategy lens is diluted across sectors that do not apply to the firm; the implementation lens carries cyber-and-conduct-and-climate-and-privacy threads when the rule is privacy-only.

**Why it happens**: The instinct toward completeness overrides the discipline of loading what the scope flags.

**Resolution**:
- Sector overlay loads from the scope record's `sector_overlay_set`, not from practitioner habit.
- Cross-cutting overlay loads from the scope record's `cross_cutting_overlay_set`, not from "every cross-cutting topic the rule could plausibly touch."
- A multi-sector firm (e.g., a bank holding company with a registered broker-dealer subsidiary and a state-chartered insurer) loads sector overlays for the legal entities the rule actually scopes. A rule scoping advisers loads capital-markets only; a rule scoping bank-holding-company-level requirements loads banking; a rule scoping insurer subsidiaries loads insurance.
- Cross-cutting overlay sets are typically a single overlay or two overlays at most. A privacy-anchored rule loads privacy. A cyber-anchored rule loads cyber. A rule that is both AI-and-cyber loads cyber plus the AI-related sections of the conduct or other relevant overlay where the rule has a fair-lending or conduct intersection.

## 3. The strategy lens is missing or pro-forma

**Symptom**: The assessment's strategy section reads as boilerplate ("the firm will engage through industry-association channels"; "no public position"; "comment letter to be drafted"). The CRO chief of staff reads it for an actual posture and finds none.

**Why it happens**: The implementation lens is the practitioner's home territory; the strategy lens requires industry-association coordination, examiner-posture reading, and litigation-and-engagement-history awareness that the practitioner may not have at hand.

**Resolution**:
- The strategy section reads against named industry associations the firm engages with on the rule (BPI, ABA, ICBA, SIFMA, ICI, IAA, ACLI, NAFCU, MBA, FTA, AFC, others); the assessment names which association(s) the firm is on, and where peer alignment runs.
- Examiner-posture-shift signal reads against named, dated regulator speeches, supervisory-priorities communications, and Supervisory Highlights editions; not "the regulator has emphasised X" without a citation.
- Comment-period posture is dated and routed: if the rule is proposed and the comment period closes on a specific date, the comment posture has an internal owner, a draft pathway, an approval gate, and a submission target date.
- Escalation triggers read against firm-specific thresholds: cost-to-comply, board-reporting expectation, material-risk-management-framework implication, consent-order-pattern peer reference. Escalation triggers without thresholds drift.

## 4. Cost-to-comply with precision but no basis

**Symptom**: The financial-impact section presents a precise dollar range ("$3M to $5M one-time, $400K annual") without naming the basis. Finance reads it; the partner asks where the numbers came from; the practitioner cannot answer.

**Why it happens**: Cost-to-comply ranges are often the headline number CRO and CFO read first, and the pull toward precision is strong; the basis discipline is harder.

**Resolution**:
- `cost_to_comply.implementation_one_time.basis` and `cost_to_comply.ongoing_run_rate.basis` name the basis: peer benchmark, vendor estimate, similar prior project, agency RIA, firm-side estimate.
- `cost_to_comply.implementation_one_time.confidence` and `cost_to_comply.ongoing_run_rate.confidence` carry an honest confidence label (`high` / `medium` / `low` / `unknown`); for first-week assessments on a new rule, `low` or `medium` are usually the honest read.
- Where the firm's read diverges from the agency's RIA estimate (which it routinely does), the assessment names the divergence and the basis. The strategy lens often picks up that divergence as a comment-letter input.
- A range is fine where it reflects genuine uncertainty (e.g., "$1M to $3M" because the vendor-quote variance is real). A precision-without-basis number ("$2.4M") is a false signal.

## 5. The two-lens assessment collapses into a single lens

**Symptom**: The assessment reads as a pure implementation document (in-scope, policy impact, control impact, cost-to-comply) with no strategy section, or as a pure strategy document (firm position, comment-period posture, peer alignment) with no implementation detail. Audience confusion follows: regulatory affairs reads the strategy version and asks where the policy impact is; CRO chief of staff reads the implementation version and asks where the engagement posture is.

**Why it happens**: The practitioner anchors on the audience they spend most time with and lets the other lens drift.

**Resolution**:
- Both lenses run; the assessment audience is the union of regulatory affairs, head of compliance, head of legal, CRO chief of staff, and head of business affected, not any single role.
- Where the assessment is being prepared for a board pre-read, the board pre-read distils to executive summary, strategy posture, financial impact, and decision request, but the underlying assessment carries both lenses.
- The implementation lens flexes to the source type: an interpretive circular has shorter implementation sections than a 600-page final rule; the strategy lens has shorter comment-period content for a final rule than for a proposed rule.
- The two lenses cross-reference: the cost-to-comply read informs the strategy posture (a high cost-to-comply may shift the firm position from neutral to opposition); the strategy posture informs the implementation pathway (an opposition posture may delay the implementation kickoff pending litigation).

## 6. The source-identification block is thin

**Symptom**: The source-citation field carries a regulator and a topic ("CFPB on adverse-action notices") but no release number, no publication date, no Federal Register citation. The downstream rule-to-obligation-extraction skill receives an ambiguous handoff and re-identifies the source.

**Why it happens**: The practitioner has the source open in a browser tab and writes the assessment from that context; the precise citation does not make it onto the page.

**Resolution**:
- `source_citation.regulator`, `source_citation.instrument_type`, `source_citation.citation`, `source_citation.publication_date`, and `source_citation.url` are populated in every assessment.
- Where the section reference is unknown, `source_citation.section` carries `[verify section]` rather than fabricated detail.
- Related instruments (the proposed rule that preceded the final, the FAQ that updated the bulletin, the speech that signalled the priority) read in `source_citation.related_instruments`. Downstream skills consume them.
- For a regulator speech or an enforcement-pattern theme, the citation is the speech URL and date or the published consent-order ID; the source-citation block is honest about the soft-source nature of the trigger.

## 7. Open questions without a routed owner or a due date

**Symptom**: The `open_questions` array carries questions without `owner_role` or `due_date`; the questions sit in the assessment without movement; downstream skills wait for resolution that does not come.

**Why it happens**: Open questions are easy to surface and harder to route; the practitioner adds them to the assessment as a list and moves on.

**Resolution**:
- Every open question carries `owner_role` (legal, compliance, business-head, sponsor, model-risk, TPRM, CISO, BSA-officer, fair-lending-officer, privacy-officer, data-protection-officer) and `blocker_for` (rule-to-obligation-extraction-kickoff, policy-diff-scope, implementation-plan-sequencing, comment-letter-signature, strategy-posture-finalisation, exam-brief-handoff).
- `due_date` is set; an open question without a due date is a question that drifts.
- The assessment's executive summary references the open-question count and the highest-impact blocker; the named lead reads the executive summary and routes the questions before attesting.

## 8. The transition-period posture is missed

**Symptom**: The assessment names the effective date but says nothing about phase-in stages, transition relief, or sunset clauses. Implementation-plan inherits the assessment and discovers mid-sequencing that a phase-in stage shifts a milestone by 12 months.

**Why it happens**: Effective dates are scanned for the first compliance date; transition-period detail is buried in a later section of the rule and gets skipped.

**Resolution**:
- `effective_date_posture.phase_in_stages` is populated where the rule has tier-by-tier phase-in (1071, DORA, CRA modernisation, Basel III Endgame).
- `effective_date_posture.transition_period` carries the transition-relief description with the citation.
- `effective_date_posture.sunset_or_contingency` carries Congressional Review Act dependency, judicial review status, or agency-rulemaking-implementation contingency.
- `effective_date_posture.early_adoption_posture` is named where the firm is considering early compliance.
- Where the rule's effective date is itself uncertain (litigation-stay; vacatur; CRA disapproval), the assessment says so and names what the firm's compliance posture is in the meantime.

## 9. Customer impact named in technical jargon

**Symptom**: The customer-impact section reads in regulatory-and-system-of-record language ("customer adverse-action notification timing extends from 30 to 45 days; UDAAP-risk surface broadens"). The head of consumer banking reads it and asks what the customer experience actually changes.

**Why it happens**: The practitioner writes the assessment in second-line vocabulary; customer-impact is not the practitioner's natural register.

**Resolution**:
- `customer_impact[*].implication` reads in plain language: what the customer sees, hears, or experiences differently.
- Where the rule introduces a new customer right, the implication names the right ("customer can request data deletion within 45 days; firm responds within 30 days") rather than the regulatory-categorical name.
- Where the rule alters the customer's evidence burden, the implication names the additional burden ("customer at account opening must produce additional KYC documentation including X").
- The customer-impact section reads alongside the operating-model implication; the head of business affected uses both.

## 10. The assessment is treated as the deliverable, not the kickoff artifact

**Symptom**: The assessment gets drafted, signed off, and then sits unread for the duration of the regulatory item. The downstream skills run from email and ad-hoc steering items; the assessment is not consulted again.

**Why it happens**: The assessment was treated as a one-time document for the regulatory-change-committee rather than as the kickoff artifact for the downstream skills and the inventory record.

**Resolution**:
- The assessment is the kickoff artifact for the chain. `rule-to-obligation-extraction` reads `affected_obligation_domains` and `source_citation`. `policy-diff` reads `policy_impact`. `implementation-plan` reads `affected_obligation_domains`, `effective_date_posture`, and `cost_to_comply`. `exam-brief` reads the assessment when the item enters an exam window.
- The assessment is updated as open questions resolve; a revision log captures the deltas.
- Where a regulator amends the rule (a finalised version of a proposed rule, an FAQ update, a litigation-driven implementation-date change), the assessment is re-emitted with the updated source-citation block and the downstream skills are re-run with the revised handoff.

## 11. Engagement-scope record stale or missing

**Symptom**: The assessment was drafted from yesterday's understanding; today the firm's footprint has expanded (an acquisition closes; a new state license issues; a registered fund launches), and the in-scope determination no longer matches the firm.

**Why it happens**: The scope record was treated as a kickoff artifact rather than a living record. The assessment consumed an old version.

**Resolution**:
- Engagement-scope is a status, not a fixed truth. Re-emit the scope record after any material change; re-emit the assessment consuming the updated scope.
- Standing scope review at the regulatory-change-committee cadence; for high-impact items, weekly or bi-weekly scope check.
- Where the assessment is run without an scope record at all, ask the questions (institution, primary regulators, persona, source posture, time pressure) and default to public posture if the practitioner declines. Note in the assessment that scope was not formalised.

## 12. Boundary with downstream skills not respected

**Symptom**: The assessment duplicates rule-to-obligation-extraction (decomposing the rule into atomic obligations row by row), policy-diff (drafting policy language), or implementation-plan (sequencing milestones with dates and owners). Two artifacts say almost the same thing with subtle inconsistencies.

**Why it happens**: The boundary between the impact assessment and the downstream skills was not respected; the practitioner pulled work forward.

**Resolution**:
- The impact assessment names the surface area and routes the handoffs; it does not decompose obligations row by row, draft policy language, or sequence milestones.
- `affected_obligation_domains` are high-level domains, not atomic obligations.
- `policy_impact[*].rationale` is a sentence on why the policy area is affected; it is not a draft of the policy amendment.
- `cost_to_comply` is an indicative range with a basis; it is not a milestone-level cost-and-resource plan.
- Where the assessment has been pulled too far forward, the named lead routes the work back to the appropriate downstream skill.
