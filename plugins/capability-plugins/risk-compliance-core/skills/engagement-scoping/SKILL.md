---
name: engagement-scoping
description: |
  Produces an engagement charter and a structured engagement-scope record that downstream second-line skills consume. The charter sets institution, engagement, persona, source posture, risk lens, and overlay context so other skills do not reinvent these facts each time they are called.

  Best for:
  - An advisory engagement starting up and the lead needs a written scope before review work begins.
  - An internal review being charted (annual model risk review, periodic third-party risk review, audit support, exam-readiness sprint, regulatory-change implementation, board-pack cycle).
  - A practitioner joining an engagement mid-flight and needing the context in one place.
  - A downstream skill called with contested or unclear scope.

  Not the right tool when:
  - A current scope is already on file and the downstream skill is engagement-scope-aware (pass the existing record).
  - The work is a one-off question rather than an engagement.
  - The institution and persona are already encoded in a `references/firm-overlay.md` the firm has installed.

  Anchored to: IIA International Standards, AICPA AU-C 300, COSO ERM, SR 11-7, OCC Bulletin 2026-13, the interagency third-party-risk guidance (2023), FFIEC IT Examination Handbook, NAIC ORSA, and standard consulting engagement-letter convention. Citations and excerpts live in `references/source-anchors.md`.
argument-hint: "[institution and engagement type, or pointer to existing scope]"
---

# Engagement scoping

The first thing a senior reviewer does on any non-trivial second-line engagement is set the scope. Who is the institution. What is the engagement. Who is the persona running it. What evidence is actually available. Which risks are in scope. Which sector and cross-cutting overlays apply. What is excluded. What is being assumed. What is left to clarify.

This skill produces that scope as a written charter for the engagement to carry, and as a structured record (`schemas/engagement-scope.schema.json`) that downstream skills consume. Both 1.5-line embedded teams and 2-line independent reviewers benefit; advisory engagements run the charter formally, internal teams run it lighter.

Engagement-scoping runs in two situations. At kickoff, the engagement lead calls it to set the charter before any review work begins. Mid-flight, another skill calls it because that skill has hit contested or unclear scope (the source posture is too low for the evidence ask, the persona review gates are unnamed, the sector overlay is ambiguous). Both entries produce the same artifact; the mid-flight version focuses the revision on the contested section and hands back to the calling skill.

## Ask first

Before drafting, get plain answers to a few things. Most engagements answer them in the first conversation; if not, default and flag.

- Who reads the deliverable. The audience drives tone, depth, and which review gates matter.
- What this engagement is not covering. Naming exclusions up front prevents drift; an empty list usually means the conversation has not happened yet.
- What evidence the engagement actually has access to today, not aspirationally. Source posture is what you can deliver against, not what you wish you had.
- What decision the engagement supports and who owns the sign-off. The persona and review machinery flow from this.
- What the time horizon is. An eight-week exam-readiness sprint and an open-ended program review need different pacing.

## What goes in the charter

The charter has the same spine across engagement types. Walk it in the order that fits the conversation; the structured record sorts itself.

The institution profile names the type, asset size band, charter, registrations, geographic footprint, and the regulators this engagement is actually addressing. Asset size matters because the regulatory expectations binding on a $50B regional bank differ from those on a $700B GSIB or a $5B insurer. Recent supervisory posture (open MRAs, MRIAs, consent orders, examination outcomes) goes here when it is known and the source posture allows; private items stay out of any artifact that will read at a lower posture than the engagement.

The engagement profile names the type, sponsor (a role, not a person), audience, timeframe with milestones, and the deliverable shape. Type drives which downstream skills the engagement will use; deliverable shape drives how the artifacts roll up.

The persona profile names the role running the engagement and the line of defense it sits in. 1.5-line is the embedded business risk officer, the regional risk lead, the BU controls tester (accountable to the business, but with a risk mandate). 2-line is the independent function: CRO, head of model risk, head of TPRM, head of operational resilience, CCO, BSA officer, AI governance lead, head of regulatory affairs. Audit support and advisory engagements layer their own review machinery on top, including partner approval, independent QA, internal audit sign-off. CRO-led engagements run on ERM machinery, CCO-led on compliance committee, AI-governance-led on AI risk committee. Capture which line and which review gates; downstream skills key off both.

Source posture is one of public-only, public-plus-firm-policy, public-plus-firm-policy-plus-evidence, or connector-aware. Set it at what the engagement has today. The same engagement may run at public-only for an early scoping conversation and shift up once firm access lands; that shift goes in the revision log.

Risk lens is the list of risk types in scope, drawn from the firm's taxonomy when the firm has one or from the named risks the engagement targets when it does not. Match the lens to the engagement; an exam-readiness sprint covering credit and BSA does not need the full enterprise taxonomy.

Sector overlay set is which of {banking, insurance, capital-markets, payments-fintech} apply. Usually one. Multi-entity engagements may need two; flag the choice. Cross-cutting overlay set is which of {cyber, privacy, climate, conduct} apply, driven mostly by the risk lens. Both sets are directives to downstream skills, telling them which `references/sector-overlays/<sector>.md` and `references/cross-cutting/<topic>.md` to load.

Out of scope, assumptions, and open questions close the spine. Out of scope is what the engagement explicitly will not cover and is the firewall against drift. Assumptions are facts being treated as fixed; open questions are items flagged for sponsor or counsel.

The revision log is append-only. The first row is the initial scope, every material change adds a row, and the log is the audit trail when scope is later contested in steering, in court, or with a regulator.

## Working with what you have

The skill does not block on missing input. If the practitioner has only partial context (institution type, perhaps the engagement type, no persona yet), draft the charter against what is given, default the rest using the institution profile and engagement type, and flag the defaults in `assumptions_and_dependencies`. The first charter is a working draft. Revisions are normal and expected.

## What not to do

- Do not invent regulatory facts. When a section reference is not known, leave it for verification; do not fabricate.
- Do not encode firm-specific facts (firm risk taxonomy, internal review machinery, named owners, system-of-record paths) in the charter directly. Those live in a `references/firm-overlay.md` the firm installs; the charter consumes them.
- Do not mix engagements. A holding-company review and a subsidiary review need separate charters even if the same practitioner runs both.
- Do not include private supervisory content in a charter that will read at a lower source posture than the content. Privileged or regulator-confidential material has implications for what downstream artifacts can include; flag it where it lands.
- Do not over-list primary regulators. Primary regulators is who this engagement is actually addressing, not every regulator that touches the institution. Conceivable-but-secondary regulators go in `assumptions_and_dependencies`.

## Output

Two artifacts: the charter in `templates/default-output.md` shape, and the structured record conforming to `schemas/engagement-scope.schema.json`. The sponsor signs the charter; downstream skills consume the record. The schema is the cross-skill contract; additive changes only, never silent edits. Add fields, do not rename or repurpose them. A breaking change is a versioned migration with the downstream skills told in advance.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/firm-overlay.md` — firm-installed taxonomy, machinery, and policy pointers (consumed when present).
- `templates/default-output.md` — charter template.
- `schemas/engagement-scope.schema.json` — structured-output contract.
- `examples/` — advisory exam-readiness sprint at a regional bank; internal AI use-case intake review at a registered investment adviser.
- `TROUBLESHOOTING.md` — recurring defects in scope records.
