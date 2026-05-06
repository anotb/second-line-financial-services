# Troubleshooting — rule-to-obligation-extraction

The extraction skill produces the atomic obligation list a discrete piece of net-new regulatory rule text imposes. The recurring defects below cause the register to lose substance, lose portability across firms, or lose alignment with the downstream `obligation-mapping` skill that consumes it.

## 1. Compressing multiple obligations into one row

**Symptom**: A paragraph that says "the institution shall (i) document, (ii) test annually, and (iii) report to the board" lands in the register as one row that reads "the institution must document, test, and report annually." Downstream `obligation-mapping` cannot cleanly assign the three sub-obligations to three different owners with three different evidence shapes.

**Why it happens**: The extraction reads the paragraph as a single sentence and produces a single row. The paragraph is structurally three obligations that share a subject and a frame, not one obligation.

**Resolution**:
- Apply the atomic-obligation discipline: each enumerated sub-clause ((i), (ii), (iii); a, b, c; first, second, third) is potentially its own row. Whether to split is determined by whether the actor, frequency, action_type, or evidence shape differ.
- The default presumption is split. Combining is a deliberate decision, not a default.
- The downstream test: can `obligation-mapping` assign each row to a single owner and a single evidence shape? If not, split further.
- The defined-terms section is one place this defect hides: a row that invokes three defined terms with different scopes is often three rows in disguise.

## 2. Extracting from preamble or commentary as if it were operative text

**Symptom**: The register includes obligations drawn from the SEC adopting-release preamble that do not appear in the codified 17 CFR section. Downstream legal review pushes back on the row because the codified section does not say what the row claims.

**Why it happens**: The preamble feels load-bearing because it is interpretive and the agency uses preamble to explain what it intends the rule to require. Practitioners read the preamble as if it were the rule.

**Resolution**:
- Pin obligations to operative text: the codified CFR section for Federal Register rules; the binding article for EU regulations; the `R` paragraph for FCA Handbook rules; the operative provision for supervisory letters. Preamble or commentary is interpretive context that may inform the row but does not create the obligation.
- Use the `source_pin.preamble_context` field to capture preamble framing that changes how the operative section reads. Do not promote a preamble-only obligation to a freestanding row.
- For an EU regulation, recitals are interpretive. Article text is binding. Pin to the article.
- For an SEC adopting release, the preamble is interpretive. The closing regulatory-text amendments are what codifies. Pin to the codified section.
- For a supervisory letter (OCC bulletin, SR letter, FIL, CFPB circular), the entire instrument is interpretive supervisory guidance, not a codified rule. The pin is the section inside the instrument, and the confidence label reflects that the instrument is supervisory rather than rule-of-law.

## 3. Missing a defined term that changes scope

**Symptom**: Two extractions of the same rule by two practitioners produce different obligation lists because one captured the rule's defined term ("covered institution," "material," "senior management," "covered application," "ICT third-party service provider") and the other did not. The downstream firm-side mapping is non-portable.

**Why it happens**: Defined terms are easy to miss when the rule body uses the term as if it were ordinary English. The rule's definitions section is the only authoritative source for scope.

**Resolution**:
- Capture every defined term the body invokes in the top-level `defined_terms` section, with the rule's text of definition and the section pin where the term is defined.
- Each obligation row's `defined_terms_used` column lists the terms the row depends on.
- When a term has different definitions across rules (e.g., "cybersecurity event" in NYDFS Part 500 versus "covered cybersecurity incident" in SEC Item 1.05), the extraction captures both definitions with their pins and flags the cross-rule confusion in the open-extraction-questions section.
- Where a state has adopted a NAIC model law with material amendments to the definitions section, capture both the NAIC model definition and the state-adopted version, and pin to the state-adopted version.

## 4. Skipping the transition and phase-in language

**Symptom**: The register has a single effective date and no transition table. The downstream `implementation-plan` skill cannot sequence remediation milestones because the register doesn't capture which obligations apply when.

**Why it happens**: Effective dates feel simpler than they are. A rule with tier-by-tier compliance dates plus a deferred-effective-date provision plus a sunset clause is a different rule in month 1 than in month 25, but the register treats it as one frozen state.

**Resolution**:
- Capture every staged date in the `transition_table` array. One row per stage.
- Distinguish effective date (rule joins the CFR or OJ) from compliance date (regulated party must comply). They are typically different.
- For tier-by-tier compliance (1071, DORA, CSRD), each tier is a row in the transition table; the obligations applicable in each tier go in the `applicable_obligation_ids` column.
- For phased compliance within a single tier (e.g., assurance requirements phased in for the SEC climate rule), each phase is a row.
- Where a rule has been the subject of post-publication litigation that has stayed or modified the effective dates, capture the dates as of the extraction date and flag the litigation status in the open-extraction-questions section.

## 5. Mixing extraction with firm-side mapping

**Symptom**: Rows in the register name firm-specific control owners (e.g., "Head of TPRM at the bank"; "Compliance Officer for the credit-card line"), firm-specific evidence systems ("captured in the bank's GRC platform"; "evidenced in JIRA ticket"), or firm-specific policy text ("the bank's existing CDD policy already requires ..."). Downstream `obligation-mapping` cannot cleanly overlay firm context because the register is already half-firm-specific.

**Why it happens**: The practitioner is familiar with the firm and reaches for firm-specific labels by reflex. The extraction collapses into a firm-side mapping.

**Resolution**:
- The skill produces a firm-agnostic register. The actor is whoever the rule names (board; senior management; CISO; covered institution; ICT third-party service provider). The evidence shape is shape, not system (board minute; attestation; log; periodic report; not "captured in GRC platform"). The owner is the regulator-defined party, not a firm-side role.
- If the firm-side mapping is needed, the skill is `risk-compliance-core/obligation-mapping`, not this one. The two chain.
- Where the engagement scope record has firm context, this skill ignores it for register content; firm context is consumed by `obligation-mapping`.
- Run the portability test: would the register read the same for a different firm of the same type? If not, the register is over-specified.

## 6. Confidence label that hides the defects

**Symptom**: The register carries a single overall confidence of "high" while several rows are pinned to `[verify section]` or carry interpretive readings of preamble. Downstream legal review pushes back because the register's confidence label does not reflect the rows.

**Why it happens**: Practitioners are reluctant to label a register low-confidence because it implies the work is incomplete; the overall label aggregates away the per-row variability.

**Resolution**:
- Confidence is per-row: high where the operative text is unambiguous; medium where interpretation is involved; low where reading between the lines or relying on preamble alone.
- The overall `confidence_label` is `mixed` when rows vary; do not collapse to a single label that hides the variability.
- Each `[verify section]` row is automatically not-high; use medium where the section is genuinely uncertain and the practitioner has read the surrounding text, or low where the section is fabricated or guessed.
- The reviewer reads the per-row confidence first. Hiding low-confidence rows under a high-overall label fails the next read.

## 7. Treating supervisory letters as if they were rules

**Symptom**: The register pins obligations to OCC Bulletin 2013-29, SR 11-7, or a CFPB circular and labels them with the same confidence as obligations pinned to a Federal Register final rule. Downstream legal review notes that the bulletin is interpretive supervisory guidance, not a rule of law.

**Why it happens**: Supervisory letters operate as if they were rules in practice (examiners apply them; firms comply). The legal status (interpretive supervisory guidance) is different from the operational status (binding for examination purposes).

**Resolution**:
- Use the `instrument_type` enum precisely: `final-rule` for codified rules; `supervisory-letter`, `bulletin`, `circular`, `fil`, `letter-to-credit-unions`, `industry-letter`, `interagency-statement`, `advisory` for the various supervisory instruments.
- Confidence label: high for clearly stated supervisory expectations even where the instrument is interpretive; the operational status is what matters for the firm's compliance posture, but the legal status influences how the firm frames its response if the supervisory expectation is contested.
- For an interagency statement (FFIEC, three-agency banking statement), pin to the statement and note that it carries the joint position of the named agencies.
- For a CFPB circular, pin to the circular and the underlying statute the circular interprets.

## 8. Treating consent-order articles as the operative source

**Symptom**: A firm not named in a consent order extracts the order's articles into its own register and treats the articles as obligations the firm must satisfy. Downstream legal review notes that the firm has no contractual or statutory obligation to satisfy the articles; the articles bind only the named defendant.

**Why it happens**: Public consent orders are useful supervisory signals. A non-defendant firm with similar exposure may treat the articles as obligations the firm should satisfy as a posture decision. The extraction blurs "should satisfy as posture" with "must satisfy as legal obligation."

**Resolution**:
- Use `instrument_type: consent-order-as-obligation-source` to mark the source as a consent order whose articles are extracted for posture, not because the firm is the named defendant.
- The register's source-trace and the open-extraction-questions section flag that the firm is not the named defendant; the obligations are extracted as posture and require firm-management decision on adoption.
- Confidence labels run lower for consent-order-derived rows (medium at best for non-defendants).
- Where the firm later becomes subject to a similar enforcement matter, the register's posture-derived rows are upgraded to obligations under the firm's own order.

## 9. Stopping at the rule and missing the implementing technical standards

**Symptom**: Extraction of an EU regulation captures the article-level obligations but misses the implementing or regulatory technical standards (RTS / ITS) adopted as Commission Delegated Regulations. Downstream implementation work surfaces the missing detail late.

**Why it happens**: EU regulations frequently delegate operational detail to RTS and ITS issued by ESMA, EBA, or EIOPA and adopted as Commission Delegated Regulations. The regulation cites the delegation; the practitioner reads the regulation but not the delegated regulation.

**Resolution**:
- For EU regulations, list the cross-referenced RTS and ITS in the source list and extract obligations from the delegated regulations as separate registers (one extraction per Commission Delegated Regulation).
- The rule's article text is the binding obligation; the RTS / ITS provide operational detail. The extraction may pin some obligations to the regulation article and others to the RTS, depending on which carries the operative requirement.
- For DORA specifically, there are multiple RTS and ITS (e.g., RTS on the policy on the use of ICT services supporting critical or important functions; RTS on subcontracting of ICT services supporting critical or important functions; ITS on the templates for incident reporting). Extraction should capture each as a separate source.

## 10. Not flagging litigation or revision risk

**Symptom**: A rule that has been the subject of post-publication litigation (vacated; stayed; remanded for further proceedings) lands in the register as if the rule were operative as published. Downstream implementation-plan work proceeds on stale dates.

**Why it happens**: Practitioners extract from the rule as published and do not check operational status at extraction time. The register lacks an operational-status flag.

**Resolution**:
- At extraction time, check the operational status: is the rule effective? Has any provision been stayed or vacated? Are compliance dates as published, or have they been adjusted?
- The `source_citation.compliance_dates` array captures the dates in effect at the extraction date, with notes on the post-publication adjustment history.
- The open-extraction-questions section flags any provision under live litigation or under regulator-announced amendment.
- Confidence labels on rows that depend on the litigated provision run lower.
- Re-extract on material change: if the rule is amended or the litigation resolves, the register is re-emitted with a revision-log entry.

## 11. Engagement-scope record stale or missing

**Symptom**: The extraction was drafted from yesterday's understanding of the engagement; today the regulator has issued an interim final rule that supersedes the source under extraction, or the firm has changed its sector posture in a way that changes the overlay set. The register no longer matches the engagement.

**Why it happens**: The engagement-scope record was treated as a kickoff artifact rather than a living record. The extraction consumed an old version.

**Resolution**:
- Engagement-scope is a status, not a fixed truth. Re-emit the scope record after any material change; re-emit the extraction consuming the updated scope.
- Where the extraction is run without an engagement-scope record at all, ask the four questions (regulator and instrument; publication / effective / compliance dates; source posture; firm boundary) and default to public-only posture if the practitioner declines. Note in the register that scope was not formalised.

## 12. Boundary with `obligation-mapping` not respected

**Symptom**: The extraction register and the firm-side obligation register (produced by `risk-compliance-core/obligation-mapping`) duplicate substantive content. Subtle inconsistencies appear at the row level: this register names the rule's actor as "covered institution"; the firm-side register names the actor as "the bank's BSA officer." Downstream consumers cannot tell which is operative.

**Why it happens**: The boundary between extraction and mapping was not respected; both skills produced overlapping content for the same row.

**Resolution**:
- The two skills chain; they do not duplicate. Extraction produces the regulator-side, firm-agnostic obligation list. Mapping overlays firm-side context on top.
- The shared key is `obligation_id`. The mapping skill's register references the extraction's `obligation_id` and adds firm-side columns (named owner; firm-side control objective; named evidence system; firm policy reference; risk taxonomy tag; review-gate posture). It does not restate the extraction's regulator-side columns.
- Where the firm-side register and the extraction register diverge on the regulator-side columns (actor name; requirement statement; deadline; exception; defined-term scope), the extraction register is operative; the mapping register has drifted and needs revision.
- The schema contract (the cross-skill `obligation_id` plus the extraction's regulator-side columns) is additive. Breaking changes to the schema ship as a versioned migration with downstream skills told in advance.
