# Troubleshooting: criticality-assessment

Recurring pitfalls. Read before producing the assessment and again before sign-off.

## Tier-setting pitfalls

### Using vendor spend or vendor headcount as a proxy for criticality

Spend is not impact. A low-spend vendor on the customer-facing path can be critical. A high-spend vendor that runs a non-IBS internal process can be not-critical. The IBS dependency, customer-impact severity, and substitutability read drive the tier.

### Setting RTO and RPO to the vendor's commitment rather than the firm's tolerance

The vendor's commitment is the ceiling on what the vendor delivers. The firm's tolerance comes from the IBS impact analysis and is the test the vendor must meet. `recovery_meets_firm_tolerance = yes` only when the vendor's commitment meets the tolerance. A gap is itself a finding for `contract-gap-review` and a precondition for `vendor-diligence` to evidence operational-resilience posture.

### Letting the procurement category drive the tier

"IT services" is not a tier. "Cloud" is not a tier. "Professional services" is not a tier. The tier is set by impact on the IBS, customer, and regulator. The procurement category may correlate with tier; it does not determine it.

### Skipping the manual-workaround viability test

The criticality call depends on whether the firm can keep the supported process running without the vendor for the full tolerance window. Without this test the substitutability read is incomplete and the tier is unreliable. `manual_workaround_viable = true` is a high bar and uncommon for vendors on the IBS chain.

## DORA and jurisdictional pitfalls

### Treating "DORA critical or important function" and the firm's own tier as identical

The criteria differ. The firm's tier reflects the firm's IBS map, customer-impact framework, and substitutability read. The DORA critical-or-important-function call applies the EBA-defined criteria. Where DORA applies, record both calls separately with rationale on each. Collapsing them is a documentation defect that propagates to the DORA register.

### Confusing "in scope of the DORA register" with "DORA critical or important function"

An ICT service to a financial entity in the DORA perimeter belongs in the register regardless of criticality. The critical-or-important-function flag is a separate field on the register entry. Many register entries are ICT services that are not critical or important functions; the flag is `no` and the rationale is recorded.

### Defaulting the DORA call to "not-in-scope" without checking entity perimeter

Where the firm or its EU subsidiary is in DORA scope, every ICT arrangement gets the call (`yes`, `no`, or both calls separately if multiple entities are affected). `not-in-scope` is reserved for entities outside the DORA perimeter.

### Missing the UK PRA SS2/21 overlay for UK-licensed firms

If the firm is UK-licensed, the IBS framing and impact-tolerance test are UK-overlay items. `uk_ibs_flag = yes | no` per the firm's UK IBS map; `not-in-scope` only for firms outside the UK perimeter.

## Engagement-scope pitfalls

### Running without scope

If the scope record is missing, ask the four questions (institution type, primary regulator(s), persona/audience, source posture) and default to public posture if the practitioner declines. Note in the artifact that scope was not formalised. Do not silently apply a default sector overlay.

### Loading the wrong sector overlay

Institution type and primary regulator constellation determine the sector overlay set. Banking is not insurance is not capital markets is not payments-fintech. A dual-registrant or a fintech with a sponsor bank may need two overlays.

### Setting the tier and walking away

The criticality call is revisited on contract renewal, on material change to the service, on material change to the IBS, and on annual recertification per the firm's policy. Record the next-review trigger explicitly. A criticality call without a next-review trigger is incomplete.

## Output discipline

### Citing without sections

Every regulator citation in the assessment carries a section reference or a `[verify section]` placeholder. URL alone fails the source-anchor depth check. Use `references/source-anchors.md` for the canonical citation set; do not restate excerpts in the assessment body.

### Marking unsupported claims silently

Use `[evidence needed]` explicitly. An inferred claim presented as evidenced is the failure mode. Tier rationale that reads as authoritative without a cited source is the most common version of this defect.

### Treating the assessment as the decision

The assessment stops at the recommendation. The named approver decides under the firm's third-party-risk policy for the proposed tier. The skill outputs a `tier` and `tier_rationale`; the formal sign-off lives downstream.

### Closing with too much certainty

The confidence label is `high` only when the IBS map, the impact tolerance, and the customer-impact and regulatory-impact reads are all anchored in firm-of-record evidence. `medium` and `low` are normal for early-stage assessments and for arrangements where the firm has not yet formalised an IBS map. `unknown` is honest where the criteria are unresolved.
