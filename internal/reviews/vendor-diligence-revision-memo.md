# Vendor-diligence revision review memo

Date: 2026-05-06
Reviewer: phase-2 reviewer subagent
Subject: revised `plugins/capability-plugins/third-party-operational-resilience/skills/vendor-diligence/SKILL.md`
Compared against: spec sheet (`docs/specs/third-party-operational-resilience/vendor-diligence.md`), boundary spec (`docs/specs/ai-governance-model-risk/llm-vendor-evidence-review.md`), chained specs (`contract-gap-review.md`, `exit-plan.md`, `concentration-risk-review.md`), build contract, anti-AI-tells memory (updated), practitioner-lens memory, scoping review memo for shape reference.

## 1. Top-line judgment

About right, leaning slightly under-cut in three places. The prose carries the work. AI tells are mostly gone. The four "Ask first" questions are intact. The `ai_vendor` boolean is a real branch with the `llm-vendor-evidence-review` chain wired in. Risk-based evidence ask is intact. AI-overlay pitfalls are folded into a working paragraph. Lifecycle cross-links are all there with their named field handles. Recommendation enum is complete. The 6-phase spine reads in prose without numbering and a runtime reader can follow it without ladder structure — the named opening clauses ("The frame opens with...", "Evidence collection is risk-based...", "Reading the evidence is where...", "The AI overlay...", "The lifecycle cross-links close...", "The pack ends with...") give Claude the handles it needs.

The revision over-cut in three small but load-bearing spots: the impact-tolerance test against vendor RTO/RPO claims (the second half of spec pitfall #5), the schema-stability discipline (one slogan-line, same as scoping), and a missing explicit reviewer-question-clusters-by-forum cue in the recommendation paragraph. One smaller cleanup on `load-bearing` overuse and one on naming the agent-tool / agentic posture explicitly in the AI overlay.

Net: five proposed edits, all small. None reintroduce numbered ladders or rigidity tells.

## 2. What got dropped or weakened

### 2.1 Impact-tolerance test against vendor RTO/RPO claims

The spec sheet's pitfall #5 has two halves:

> Setting RTO/RPO to the vendor's claim instead of the firm's tolerance. The vendor's claim is the ceiling on what the vendor delivers. The firm's impact-tolerance for the supported important business service is the test the vendor must meet.

The revision keeps the first half:

> Vendor RTO/RPO claims are claims; evidenced recovery objectives are facts.

That is the claims-vs-evidence cut. Good, but it does not address the second half — that the test is the firm's impact tolerance for the supported important business service, not the vendor's number. The PRA SS1/21 / SS2/21 frame, BCBS principles, and the interagency guidance all expect the firm's tolerance to be the test. Without this, a vendor that publishes a 4-hour RTO with airtight evidence still passes the read even if the firm's impact tolerance for the IBS is 2 hours. Practitioner senior reviewers test the vendor against the firm's tolerance, not the vendor's commitment.

This belongs in the "Reading the evidence" paragraph, one short clause.

### 2.2 Schema-stability discipline

The revision has one sentence:

> The schema is the cross-skill contract; additive changes only.

Same gap as scoping. Vendor-diligence's schema is consumed by `contract-gap-review`, `exit-plan`, `concentration-risk-review`, `dora-register-builder`, and `llm-vendor-evidence-review`, which makes the cross-skill-contract claim more, not less, load-bearing here. One added sentence brings the rule from slogan to operational guidance without ballooning it.

### 2.3 Reviewer questions by forum is named earlier but not at the recommendation point

The revision names the forum-clustering point in "Ask first":

> ...a critical vendor gets full depth with reviewer questions clustered for the relevant forums.

And in the "Flexes" paragraph:

> A TPRM-forum pack reads short and operational. A risk-committee pack for a critical vendor reads longer with reviewer questions clustered for the forum. A fund-board pack reads differently again; lead with the decision the audience must make.

That is good. But the recommendation paragraph itself just says:

> Reviewer questions tie to the decision.

The forum-cluster cue is two paragraphs upstream. At runtime when Claude is composing the reviewer-questions block, the forum hint should be next to the action. One short clause in the recommendation paragraph does it.

### 2.4 Agent-tool / agentic posture missing from the AI overlay narrative

Spec sheet, output template section 14:

> ...agent-tool-use posture if the vendor offers agentic capabilities.

Spec sheet, structured-output `ai_specific_findings.agent_tool_posture` is a named sub-field.

The revision's AI-overlay paragraph names: system card fit to deployment, eval coverage on the deployed system, training-data posture, shared-responsibility clarity, prompt-as-customer-data, model-version pin / deprecation clock. It does not name agent-tool posture. The "Flexes" paragraph mentions "agentic system" as a use-case category. That is a design-surface mention, not a finding-surface mention. A senior practitioner reviewing an agentic AI vendor (tool use, browser use, code execution, multi-step planning) treats agent-scope, agent-tool whitelisting, sandboxing, and prompt-injection-via-tool-output as load-bearing AI-specific findings. Add one short clause to the AI-overlay paragraph naming it.

### 2.5 `load-bearing` appears twice

> ...the load-bearing design point for this skill.
> Load-bearing across every pack: ...

`load-bearing` is a fine practitioner term but using it twice in adjacent sections is engineer-voice repetition. The first instance ("the load-bearing design point") is the more disposable of the two — the paragraph itself reads as design-point without the meta-label. Trim one.

## 3. What survived correctly and should not be undone

In case the orchestrator over-corrects:

- **The four "Ask first" prompts.** Tier (from criticality-assessment), AI-vendor boolean, regulatory profile, engagement type. All four present, in plain bullets, not numbered. Right call.
- **The `ai_vendor` boolean is a real branch, not a side-note.** "The AI-vendor branch is a real branch, not a side-note: it conditionally surfaces `ai_specific_findings` and pulls the cyber and privacy overlays in by default." Right call. The default-on cyber/privacy for AI vendors is the right enforcement.
- **Boundary chain to `llm-vendor-evidence-review` with `eval_evidence_status = deferred-to-evidence-review` and the linked record ID.** Surgically named. Right call. Closer to spec than spec — the spec hand-waves "use llm-vendor-evidence-review for that narrower question"; the revision wires the actual schema field that triggers the chain.
- **The 6-phase spine in prose, not numbered ladder.** "The pack has the same spine across vendor types. A senior reviewer fills it in roughly in the order the engagement and the vendor offer evidence, not in a lockstep sequence." Then six prose paragraphs each opening with the named phase. The order is recoverable at runtime; the dependency chain (frame sets AI flag → AI flag drives overlay defaults → overlay drives evidence ask → evidence read drives AI-overlay findings → findings drive cross-links → all of it drives the recommendation) is implicit but linguistically marked. Per the updated anti-AI-tells memory, this is the right call. Do not renumber.
- **Risk-based evidence ask list intact.** Audited financials, SOC 2 Type II (full report not summary), ISO/IEC 27001 with SoA, pen-test summary, vulnerability-management evidence with cadence and MTTR, BCDR test reports with evidenced recovery objectives, privacy program with sub-processor list and incident history, sub-contractor and fourth-party register, regulatory and legal posture. All present. AI-specific add-on (system card, eval report, red-team summary, trust-and-safety pages, contract addenda) present.
- **Evidence-reading discipline intact.** Status enum `sufficient | partial | missing | not-applicable`; SOC 2 scope and CUEC; vendor RTO/RPO claims vs evidenced recovery objectives; region-pin promises vs data-residency reports; "RFP narrative is not evidence". Right.
- **Lifecycle cross-links all present with named field handles.** `contract_gap_summary` → `contract-gap-review`; `exit_plan_status` → `exit-plan`; `concentration_flag` → `concentration-risk-review`; `ai_specific_findings.llm_vendor_evidence_review_record_id` → `llm-vendor-evidence-review`. The "diligence pack without a contract-gap pointer is incomplete" and "critical or important vendor without a current exit plan is itself a finding" carry through. Right.
- **Recommendation enum complete.** `approve`, `approve-with-conditions`, `defer`, `decline`, `escalate`. "Conditions are specific and verifiable." Right. The named review gates (scope, evidence, authority, impact, decision) reference is correct.
- **The "Best for" expansion to four entries (added exit-triggered or post-incident re-review).** Right. Practitioner-recognized.
- **Forum-clustering naming.** TPRM forum, risk committee, fund board are all named in the "Flexes" paragraph. Right. Edit 3 below moves a hint closer to the recommendation paragraph but does not duplicate.
- **One section "What's load-bearing and what flexes", not parallel rigidities/adaptation pair.** Right. Per anti-AI-tells.
- **"Pointers" section short, file-path-only.** Right.
- **The boundary line — "RFP narrative is not evidence, anywhere."** Carried in the load-bearing list. Right.
- **No `[verify section]` markers in SKILL.md or the description's "Anchored to" line.** Right. Those live in `references/source-anchors.md`.
- **The "schema is the cross-skill contract" line lives.** Slogan needs one more sentence (Edit 2) but the line itself stays.
- **No marketing adjectives, no hedge tics, no repeated must/mandatory stack.** Right.

## 4. Proposed edits

Five edits, all small. None reintroduce numbered-step rigidity, AI-tell prose, or fake-precision ranges.

### Edit 1 — add the impact-tolerance test alongside claims-vs-evidence

**Location**: third paragraph of "How the pack gets built" (the "Reading the evidence is where the pack earns its keep" paragraph). After the existing sentence:

> Vendor RTO/RPO claims are claims; evidenced recovery objectives are facts.

**Proposed addition** (one sentence inserted immediately after):

> Both are read against the firm's impact tolerance for the supported important business service, not against the vendor's published commitment; the vendor's number is the ceiling, not the test.

**Why**: spec pitfall #5's second half is the sharpest cut in the spec sheet on resilience-evidence reading. PRA SS1/21 and BCBS Principles for Operational Resilience (March 2021) frame impact tolerance as the firm's test of vendor performance. Without this clause, the pack risks reading the vendor's evidence against the vendor's commitment instead of the firm's IBS tolerance, which is exactly the diligence failure regulators flag.

### Edit 2 — one more sentence on schema stability

**Location**: "Output" section, after the existing sentence "The schema is the cross-skill contract; additive changes only."

**Proposed text**:

> Add fields, do not rename or repurpose them. A breaking change is a versioned migration with the downstream skills told in advance.

**Why**: vendor-diligence's schema is consumed by `contract-gap-review`, `exit-plan`, `concentration-risk-review`, `dora-register-builder`, and `llm-vendor-evidence-review`. The cross-skill-contract claim is the load-bearing one. One slogan-line is not enough operational guidance for a schema with five downstream consumers.

### Edit 3 — name the forum cluster at the recommendation paragraph

**Location**: last paragraph of "How the pack gets built" (the "The pack ends with the recommendation" paragraph). Replace the existing line:

> Reviewer questions tie to the decision.

**Proposed text** (replacing the existing sentence):

> Reviewer questions tie to the decision and cluster for the forum that decides — TPRM forum for an operational arrangement, risk committee for a critical vendor, AI risk committee for an AI vendor, fund board where the arrangement sits inside a registered fund.

**Why**: at runtime, the forum hint should be next to the action that uses it. The "Flexes" paragraph names the forums correctly but is several paragraphs upstream of the reviewer-questions composition step. This brings the cue local without duplicating substance.

### Edit 4 — name agent-tool / agentic posture in the AI overlay

**Location**: the AI-overlay paragraph in "How the pack gets built". After the existing clause on model-version pin and deprecation clock and before the chained `llm-vendor-evidence-review` clause. Currently:

> ...and the model-version pin and deprecation-notice clock, because the deployed checkpoint is a moving target. Where the question becomes...

**Proposed insertion** (one clause inserted immediately after the deprecation-clock clause and before "Where the question becomes"):

> Agent-tool posture sits next to these for any agentic vendor: agent scope, tool whitelisting, sandbox guarantees, prompt-injection-via-tool-output, and the firm-side guardrails the deployment must add are read here even when the vendor's published evidence pretends the controls are vendor-side.

**Why**: spec sheet's `ai_specific_findings` schema includes `agent_tool_posture` and the spec example calls it out. The "Flexes" paragraph mentions agentic system as a use-case category but the AI overlay's actual finding-surface narrative does not name agent-tool posture as a load-bearing item. Senior AI-vendor reviewers in 2026 treat agentic capability as a top-three concern alongside system-card fit and eval coverage. Naming it puts the finding in the right paragraph.

### Edit 5 — trim one of the two `load-bearing` instances

**Location**: AI-overlay paragraph. Currently opens:

> The AI overlay, when `ai_vendor=true`, populates `ai_specific_findings` and is the load-bearing design point for this skill. The high-leverage items: ...

**Proposed edit** (replace the first sentence):

> The AI overlay, when `ai_vendor=true`, populates `ai_specific_findings`. The high-leverage items: ...

**Why**: `load-bearing` is a fine practitioner term but appears twice in adjacent sections (here and in the "What's load-bearing and what flexes" header opening line). Cutting the meta-label here is no loss — the paragraph is the design-point by composition, and the heading two paragraphs down owns the term cleanly.

## 5. Closing

The revision is good and lands close to the scoping pattern. The 6-phase spine works in prose because each phase opens with a named handle. The four "Ask first" questions are intact. The AI-vendor branch is wired correctly with the `llm-vendor-evidence-review` chain. The five edits proposed are surgical: one resilience-test substance restoration, one schema-stability sentence, one runtime locality fix on forum clustering, one agentic-posture naming, one stylistic trim. None restore numbered ladders, fake-precision ranges, repeated must/mandatory stacking, or AI-tell prose.

If the orchestrator can only land one edit, land Edit 1 (impact-tolerance test). It is the single piece of substance whose absence a senior op-resilience reviewer would notice on first read.
