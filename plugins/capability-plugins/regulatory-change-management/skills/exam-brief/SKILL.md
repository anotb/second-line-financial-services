---
name: exam-brief
description: |
  Drafts the engagement playbook a regulatory affairs lead, head of compliance, head of legal, or CRO chief of staff runs during a live regulator engagement. Generic across regulator type and product line. Captures the scope confirmation in writing, the named single-point-of-contact map by topic, the document-handling and privilege posture, the request-list mapping, the interview-prep posture, the supervisory-history that the engagement inherits (open MRA, MRIA, consent-order milestones, self-identified issues), the anticipated reviewer questions tied to current supervisory priorities, the exit-meeting and supervisory-letter response posture, and the post-exam follow-up. The substantive readiness sprint sits in sector-specific exam-readiness skills; this is the engagement-side scaffolding that runs during the exam window.

  Best for:
  - An exam window has opened (any regulator, any product line) and the regulatory affairs lead needs the engagement playbook before fieldwork begins.
  - A supervisory-letter response or consent-order milestone is in flight and the response posture needs a written engagement record.
  - A targeted, limited-scope, horizontal, or for-cause review where the generic engagement shape is the operative scaffolding and a sector-specific readiness package is too heavy.
  - A pre-exam mock or self-assessment exercise where the deliverable should look like the real engagement playbook.

  Not the right tool when:
  - The engagement is a full-scope OCC, FRB, or FDIC bank examination at an institution carrying the Heightened Standards. Use `sector-plugins/banking-risk-compliance/banking-supervision-readiness` for the substantive readiness sprint; that skill carries OCC, FRB, and FDIC supervisory framework, capital, liquidity, BSA/AML examination-manual, fair-lending, and CRA scaffolding. The generic exam-brief can still run as a sub-package for an engagement-side slice.
  - The engagement is an SEC investment-adviser or asset-manager exam. Use `sector-plugins/capital-markets-asset-management-compliance/adviser-exam-readiness`; that skill carries IAA Rule 206(4)-7, custody rule, marketing rule, books-and-records, and Form ADV scaffolding. The generic exam-brief can still cover, for example, a cyber-only slice within a broader adviser exam.
  - The job is to extract obligations from a published rule (use `rule-to-obligation-extraction`) or to sequence remediation milestones (use `implementation-plan`).
  - The job is impact assessment of a proposed rule, not engagement with a regulator on an existing rule (use `regulatory-impact-assessment`).

argument-hint: "[regulator, exam type, scope window, in-scope products and entities, prior-cycle posture]"
---

# Exam brief

A live regulator engagement runs on a small number of operational artifacts. Who is the regulator. What did the regulator say in writing about scope. Who on the firm side runs which topic. How documents move from custody to production, and who owns privilege. What the request list says, who owns each line, and what status each line is in today. Who interviews, on what topic, with counsel attending. What open supervisory items the engagement inherits. What the firm intends to surface proactively. What questions the team expects, grounded in current priorities and recent enforcement. What the exit conference will look like. Who owns the response when the supervisory letter lands. What the firm commits to do after the exam closes.

This skill produces that engagement playbook as a written brief and a structured record (`schemas/exam-brief.schema.json`). It is the artifact the head of regulatory affairs, head of compliance, general counsel, and CRO chief of staff carry into the engagement and update through the window. It is not the substantive readiness sprint; sector-specific exam-readiness skills (`banking-supervision-readiness`, `adviser-exam-readiness`) carry the substantive scaffolding when the engagement warrants it. When the engagement does not warrant the sector skill, or when a targeted slice inside a broader engagement needs a generic shape, this skill is the right tool.

The brief is a draft until the named lead attests. The skill stops short of speaking for the firm to the regulator.

## Ask first

Settle a handful of facts before drafting. Most engagements answer them in the first conversation; if not, default and flag.

- **Who is the regulator, which office, and what is the engagement type.** Engagement type is one of full-scope, targeted, limited-scope, horizontal, for-cause, follow-up, supervisory-letter response, consent-order response, mock, or self-assessment. Regulator office matters because the supervisory team (and the convention for the engagement) is set there: OCC Midsize and Community Bank Supervision is not Large Bank Supervision; SEC Division of Examinations regional office is not the home office; CFPB Office of Supervision Policy is not Office of Supervision Examinations.
- **What did the regulator confirm in writing as scope, and what is out of scope.** First-day letter or scope memorandum is the operative document. The out-of-scope list is the firewall against in-flight scope creep; an empty out-of-scope list is a signal that the conversation has not happened yet.
- **What does the firm inherit at the start of the engagement.** Open MRAs and MRIAs (federal banking convention, parallel CFPB Matters Requiring Attention), open consent-order milestones, in-flight supervisory-letter responses, and recent supervisory feedback. These shape both anticipated questions and the response posture.
- **Who runs the engagement on the firm side, by topic.** A single point of contact for examination correspondence (usually head of regulatory affairs or chief compliance officer) plus topic-specific primary roles (CISO for cyber, BSA officer for AML, CRO or head of model risk for model, head of TPRM for third party, head of compliance for fair lending or marketing rule, general counsel for privilege calls). One bottleneck is the failure mode; mapping topics to roles avoids it.
- **What is the source posture for this engagement.** Public-only, public-plus-firm-policy, public-plus-firm-policy-plus-evidence, or connector-aware. The brief itself is firm-confidential by convention; what it can assert at high confidence depends on the source posture.

When an `scope` record is supplied, the skill consumes it for institution, persona, source posture, sector overlay set, and cross-cutting overlay set. When it is not supplied, ask the few questions and default; flag the defaults in the brief.

## How the brief gets built

The brief has the same spine across regulators. The order below is the spine; in practice, sections fill in as the engagement and the regulator surface evidence. The structured record sorts itself.

**Cover and scope confirmation.** Regulator, regulator office, engagement type, trigger (routine cycle, risk-based selection, supervisory-letter follow-up, consent-order monitoring, complaint-driven for-cause, horizontal, M&A-driven). Scope window is the dated fieldwork window plus the dated review period; in-scope products, business units, legal entities, geographies; the out-of-scope list as confirmed by the regulator in writing; pointer to the first-day letter or scope memorandum that confirmed scope. If scope was confirmed verbally only, that is itself a brief entry; ask for written confirmation.

**Named points of contact.** A single-point-of-contact map by topic, roles only (never named individuals). Examination correspondence has a primary; each substantive topic in scope has a primary and a backup; outside counsel engagement is flagged per topic. The map is the answer to "who do I route this regulator question to" without a single bottleneck. Where the regulator runs an examiner-in-charge model (federal banking, CFPB) or a lead-examiner model (SEC, FINRA, NYDFS), the firm-side single point mirrors that structure.

**Document-handling and privilege posture.** Production channel (regulator portal, secure file transfer, on-site reading-room, examiner laptop, paper). Privilege-review lead role (typically inside counsel; outside counsel for higher-stakes engagements or topics carrying internal-investigation work product). Privilege-log requirement (true when the regulator has indicated a log will be requested or where firm policy requires one). Redaction workflow as a named process: counsel-supervised, burned-in redactions only, metadata stripped, reviewer named per document. Deduplication method across waves, hash-based at the production-package level being the convention. Production-log location, the canonical record of every document, hash, date sent, date received, custodian role. CSI-handled flag, true when the regulator's prior supervisory letters, MRAs, or examination reports are referenced (CSI cannot leave the firm without the regulator's written authorisation under 12 CFR Part 4 Subpart C for OCC, Part 261 for FRB, Part 309 for FDIC; CFPB CSI runs under 12 CFR Part 1070 Subpart D; SEC and FINRA each have their own posture).

**Request-list mapping.** The first-day letter or follow-up request items, each mapped to verbatim or paraphrased text, owner role, status (`ready`, `partial`, `not-started`, `escalated`, `produced`, `withdrawn`), due date, produced date, artifact pointers (system-of-record paths, not screenshots), privilege posture (`producible`, `redacted-and-producible`, `privileged-withhold`, `csi-held-by-regulator`, `under-review`), confidence label, and notes. The mapping is the operative production tracker; the engagement lead runs the daily standup against it.

**Interview-prep posture.** Schedule by interviewee role and topic, with prep-session date, counsel-attending flag, key documents the interviewee should re-read before the session, anticipated topics, and off-limits topics. Off-limits topics are the privileged territory or out-of-scope material the interviewee redirects to counsel if raised; naming them avoids the in-meeting failure mode of an interviewee waiving privilege under pressure. Roles only, never named individuals.

**Supervisory history.** Open MRAs, open MRIAs, open consent orders with milestone status, and self-identified issues the firm intends to surface proactively. Each open item names topic, owner role, due date, and status. Self-identification is generally a credibility signal with examiners; suppressing material issues is a worse posture than disclosing them. Where prior CSI is referenced, the access-population for the brief itself is constrained accordingly.

**Anticipated reviewer questions.** Each question ties to a current supervisory priority or a public enforcement theme: SEC Division of Examinations annual priorities, FINRA Annual Regulatory Oversight Report, CFPB Supervisory Highlights, OCC semiannual operating plan, FFIEC inter-agency communications, NYDFS Industry Letters, NAIC focus areas, recent published consent orders. The talking-point field carries the firm-side response posture, brief, not a script. Questions that read like generic FAQs are the failure mode; each anticipated question references a concrete source pattern.

**Exit-meeting prep.** Scheduled date; firm attendees by role; anticipated findings drawn from in-flight examiner signals; disagreement posture (where the firm intends to push back, on what basis, via what channel: verbal at exit, written response, escalation to office director or supervisory committee); expected response window in days. The exit conference is where the engagement turns from data-collection to negotiation; the brief pre-positions the disagreement posture so counsel is not surprised in the room.

**Response posture.** Named response owner role (typically head of compliance or chief compliance officer for the cover letter, with substantive ownership by the topic primary). Response-due calculation basis: receipt of the supervisory letter, exit memo, or final examination report (federal banking convention is generally 30 days from receipt of the supervisory letter; CFPB and SEC vary; agency-specific). Remediation-plan template pointer, chaining to `implementation-plan` for the milestone build-out. Board or committee reporting required (almost always for MRIAs and consent orders; often for material MRAs). External-counsel-for-response flag.

**Post-exam follow-up.** Lessons-learned session date, after-action record pointer, next-cycle preparation owner role. The engagement does not end at the exit conference; the firm carries the follow-up commitments and the after-action record into the next cycle.

**Source trace and confidence.** Every material claim about regulator process, supervisory-cycle convention, document-handling expectation, or response-window calculation cites a source from `references/source-anchors.md`. Unsupported items are marked `[evidence needed]`. Section references that cannot be confirmed get `[verify section]` rather than fabricated. The brief carries an overall `confidence_label`; medium is the honest read when request-list items are still partial or escalated, regardless of how clean the rest of the brief looks.

## Sector and cross-cutting overlays

When the scope names a sector, load the matching overlay in `references/sector-overlays/{banking,insurance,capital-markets,payments-fintech}.md`. The overlay carries the regulator-specific engagement convention, examiner-in-charge model, document-handling posture, MRA/MRIA/consent-order convention, and response-window calculation for that sector. Same pattern for cross-cutting overlays where present (cyber, privacy, conduct).

The boundary the overlay enforces: a banking sector overlay loaded inside this skill covers the engagement-side scaffolding for a non-full-scope engagement at a bank (a CFPB exam at a bank, an NYDFS cyber exam at a state-chartered bank, a coordinated trust exam, an IT-focused exam, a topic-targeted OCC review). For a full-scope federal banking exam at a bank carrying the Heightened Standards, the overlay routes to `banking-supervision-readiness` instead. Same pattern for capital-markets: the overlay covers a niche review (cyber-only at an adviser, an exchange-rule examination, a transfer-agent review) where `adviser-exam-readiness` is too broad.

Loading an overlay the engagement does not implicate adds noise without challenge value. Loading none when one applies is the more common failure mode.

## Quality bar

Holds across every brief. Every material claim about regulator process cites a source from `references/source-anchors.md` (or a loaded overlay) by path. Unsupported items carry `[evidence needed]`. Section references that cannot be confirmed get `[verify section]`. Source evidence, vendor or firm management assertion, public-source obligation, generated inference, and open legal question stay distinguishable. Roles only, never named individuals, in every section. No named institutions in narrative beyond a public defendant in a finalised consent order, and only for structural pattern. The brief stops short of speaking for the firm to the regulator. The named lead attests.

## Adaptation

Brief depth scales to engagement type and stakes: a horizontal review brief reads short and operational; a consent-order-response brief reads longer with a milestone tracker and named monitor role; a for-cause brief reads tighter on the precipitating event with counsel-shaped sections. Audience drives shape: regulatory affairs and head of compliance run the operational version; CRO chief of staff and general counsel pull the response-posture and disagreement sections forward; a board pre-read distills to executive summary plus open MRA/MRIA status. Source posture (public-only through connector-aware) drives what the brief can assert at high confidence and what carries `[evidence needed]`. Sector and cross-cutting overlays load from the scope. Where firm-specific policy or named review machinery applies, it lives in `references/firm-overlay.md` and is consumed when present; the brief itself stays generic.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors (federal banking, CFPB, SEC and FINRA, NYDFS and state DOIs, privilege and CSI, MRA/MRIA/consent-order convention, AI-and-cyber-targeted anchors).
- `references/sector-overlays/{banking,insurance,capital-markets,payments-fintech}.md` — sector overlays loaded from scope.
- `references/firm-overlay.md` — firm-installed regulator-relationship history, named privilege-review counsel, approved redaction tools, internal CSI-handling SOP, response-letter style guide; consumed when present.
- `templates/default-output.md` — brief template.
- `schemas/exam-brief.schema.json` — structured-output contract for downstream consumption.
- `examples/` — public-source-derived scenarios (OCC targeted exam at a regional bank covering third-party risk and cyber; further scenarios as overlays land).

## Output

Two artifacts: the brief per `templates/default-output.md`, and the structured record per `schemas/exam-brief.schema.json`. The named lead attests; the brief is a draft until that step.

Downstream consumers: `implementation-plan` reads the response-posture section and any open MRA, MRIA, or consent-order milestones for the remediation build-out. `policy-diff` is called when the engagement uncovers policy gaps surfaced by request-list items. `regulatory-impact-assessment` is called when the engagement implicates a published rule whose impact has not been formally assessed. The schema is the cross-skill contract; additive changes only, never silent renames. Breaking changes ship as a versioned migration with downstream skills told in advance.

## Human review and AI disclosure

Open the deliverable with this line, and remove it only after the review below: `AI-assisted draft. Requires review by a qualified person before use.`

A qualified person with authority to change the output reviews it before it is delivered or relied on, and stays accountable for it. Where the output supports advice to an individual or a decision about an individual (credit, insurance underwriting, pricing or claims, employment, legal rights, or similar), that individual must be told AI was used to produce it. This skill does not make final decisions, file with a regulator, notify customers, execute transactions, or move money or other financial assets.
