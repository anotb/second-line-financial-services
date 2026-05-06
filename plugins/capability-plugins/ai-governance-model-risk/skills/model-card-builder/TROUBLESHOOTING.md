# Troubleshooting: model-card-builder

Recurring failure modes when a model card looks complete but is not. The reviewer pass should catch these; the builder pass should preempt them.

## The card describes the model as it should be, not as it is

Symptom: limitations section reads aspirationally ("the model is monitored continuously for drift"), monitoring plan describes the operating intent rather than what is wired up, controls list policies rather than implemented mechanisms.

Why it happens: model owner drafted the card from the design spec, not from the operating evidence. Common at first-card stage; also common on refresh when the prior card was inherited and never re-evidenced.

Fix: every monitoring entry, control, and performance metric carries a source-trace pointer (monitoring pack, control evidence pointer, validation report, performance pack). Items without an evidence pointer go to the issue log, not into the card. If the card cannot be fully evidenced today, the gaps go to the engagement before sign-off, not after.

## Performance summary cites lab metrics, not deployed-environment metrics

Symptom: AUC, faithfulness, accuracy reported as a single number from a holdout set or vendor evaluation, no segment breakdown, no monitoring-pack pull.

Why it happens: lab numbers exist before the model goes live; deployed numbers wait on the monitoring infrastructure. Card-writing pressure beats wait-for-monitoring.

Fix: schema field `performance.deployed_environment` is required. Lab-only metrics are recorded but labelled. Production cards lean on deployed metrics. Pre-prod cards may carry lab metrics, but the card states that deployed monitoring replaces them at the first cycle, with metric, threshold, and owner named.

## Limitations section is generic platitudes

Symptom: "model may not generalise to populations outside the training data"; "performance may degrade over time"; "the model has bias that should be monitored". A reviewer learns nothing from these.

Why it happens: limitations get drafted last when card-writer fatigue is highest; the section is treated as a hedge.

Fix: schema requires `limitations[].failure_mode` and `limitations[].example`. Each limitation needs to be concrete enough that a reviewer can picture the failure and a monitoring metric to detect it. If you cannot give an example, you do not yet know the limitation. Surface it as a sign-off question instead.

## Monitoring plan does not name owners or escalation paths

Symptom: list of metrics with thresholds, no owner column, no escalation column. Monitoring lives on paper; no one is accountable when a threshold breaches.

Why it happens: the model owner does not control all the owners (consumer compliance owns complaint rate, infosec owns prompt-injection signal, vendor management owns version notice). The card-writer leaves the owner column blank rather than chasing across functions.

Fix: schema requires `monitoring[].owner` and `monitoring[].escalation_path` on every entry. Missing fields fail schema validation. Chasing the owner across functions is part of the work.

## Sign-off questions are too generic

Symptom: questions like "is the model fit for purpose?" or "are the controls adequate?". The reviewer cannot use them to challenge anything.

Why it happens: the card-writer treats sign-off questions as a closing flourish rather than a reviewer aid, or copies questions from a prior card without re-reading the new one.

Fix: each sign-off question is tagged to a section (`signoff_questions[].section_tag`) and points at a specific seam in this card. Bad: "are the controls adequate?". Good: "the agent-review gate is the only preventive control between the assistant output and the customer; what is the off-switch criterion if agent-edit rate falls below the threshold for two consecutive months?". A question that can be cut-and-pasted to any card is too generic.

## GenAI card uses the traditional-ML structure unmodified

Symptom: foundation model dependence omitted; RAG corpus not described; prompt-injection exposure absent; vendor change-of-version risk not in change management.

Why it happens: the card template was built around traditional ML and the GenAI fields look optional. The owner ticks the boxes that exist and skips the others.

Fix: when `architecture.foundation_model.provider` is set, or `architecture.uses_rag` is true, or `architecture.uses_tools` is true, the GenAI overlay block fires: foundation-model dependence (provider, name, version, pinning), RAG corpus and retrieval scoping, tool inventory and tool-boundary controls, prompt injection in robustness, vendor change-of-version trigger in change management. Builder check before submission, reviewer check before sign-off.

## Card is updated only at validation cycles

Symptom: card date is 14 months old; meanwhile the foundation model has been swapped, the RAG corpus expanded, a tool was added, the prompt template changed.

Why it happens: card refresh is treated as an annual exercise; in-flight changes are tracked in the change log but never re-flowed into the card.

Fix: the change-management table lists re-validation triggers; foundation-model swap, RAG corpus scope change, tool addition, and autonomy-level change are always triggers. Each trigger event re-validates the card section that names the changed element. The card is a living document; the annual refresh is consolidation, not sole maintenance.

## Tier and depth do not match

Symptom: tier-4 model with a 12-page card detailing every nuance; or tier-1 model with a one-pager.

Why it happens: a single template depth is being applied across the inventory.

Fix: tier drives depth. Tier-4 cards are short, focused on intended use, data, owner, monitoring. Tier-1 cards are deep, with full robustness, fairness, and sign-off coverage. The template is a maximum; the engagement scope sets how much of it to fill. When tier and depth disagree, the engagement-scope record wins.

## Sector overlay loaded but ignored

Symptom: insurance pricing model card reads in fairness/bias vocabulary but never names unfair discrimination under NAIC Model #880; banking AML model card never names FFIEC manual exposure; capital-markets surveillance card never names the Rule 15c3-5 overlap.

Why it happens: the sector overlay file exists in references/ but the card-writer treated it as background reading.

Fix: when the engagement scope names a sector, the matching `references/sector-overlays/<sector>.md` content lands as named items in the card. Sign-off questions probe the sector items. If the overlay is loaded but the card has no overlay-specific content, the loader did not run; rerun with the overlay reference in scope.

## Source trace omits the foundation-model dependency

Symptom: GenAI card has full source trace on firm-supplied evidence; the foundation-model facts (training cutoff, vendor evaluations, system card statements) are missing or claimed at high confidence without a pointer.

Why it happens: vendor system cards are external documents; the card-writer treats them as background, not as evidence.

Fix: vendor system cards and vendor evaluation reports are evidence. Cite them in source trace with confidence appropriate to vendor self-attestation (typically low to medium). Where the firm has run an independent evaluation, cite that separately at higher confidence. Do not collapse vendor and firm evidence into a single line.

## Audience and tone mismatch

Symptom: card reads like vendor marketing; or like an academic paper; or like a developer README. Practitioner reviewer cannot use it for committee or examiner review.

Why it happens: the card-writer borrowed phrasing from the vendor system card or an academic paper, or imported the development README into the card.

Fix: voice is senior model risk practitioner. The audience is the model risk committee, the validator, the examiner. Depth and formality flex with the engagement-scope `persona.role` and the lifecycle stage. A pre-prod committee card is more formal than a development working note; an exam-response card is more formal still.
