# Banking sector overlay — dora-register-builder

When the scope flags banking, load this overlay alongside `references/source-anchors.md`. It carries the banking-specific competent-authority and prior-register considerations the generic skill does not own.

## Competent-authority routing

- **ECB direct-supervised significant institutions**. The ECB acts as the competent authority via the SSM for significant institutions; the register submission flows through the SSM channel under ECB technical reporting instructions [verify exact instruction reference]. National competent authorities still play a role for less-significant institutions and for non-banking subsidiaries within the SSM perimeter.
- **EBA-coordinated approach for less-significant institutions**. Less-significant institutions submit via the national competent authority following the EBA-coordinated approach. The technical channel and validation rules vary by NCA; pin the host-state instruction.
- **Cross-border-group considerations**. EU subsidiaries of a non-EU banking group report individually to their host-state NCA; the parent group's consolidated view is informational, not a substitute for the EU subsidiary's submission.

## Pre-existing register and the EBA outsourcing register

- **EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02), §11 outsourcing register** [verify section number]. Most EU banks already maintain this register. The natural input to the DORA register is the existing outsourcing register plus the broader ICT-third-party arrangements that fall outside the EBA outsourcing definition. Map and reconcile, do not copy.
- **Mapping note**. The EBA outsourcing register is flatter and narrower than the DORA Register of Information. Critical fields that map cleanly: counterparty identity, contract reference, country of head office, sub-outsourcing flag. Fields that require new collection for DORA: ICT-service-type code (ITS taxonomy), location of data at rest and processing per service, function reference and criticality, sub-contractor visibility at deeper ranks for critical-or-important functions.

## CTPP designation and the oversight framework

- **DORA Article 31 oversight framework** [verify article number]. Designated Critical ICT Third-Party Service Providers (CTPPs) sit under direct ESA oversight (the ECB, ESMA, and EIOPA acting through the Joint Examination Team mechanism). The register's `b_03.designated_as_critical_by_competent_authority` flag captures the designation where known. Hyperscaler arrangements at significant institutions are the predictable CTPP candidate set.

## BHC and parent-group interplay

- A US BHC with EU banking subsidiaries: the EU subsidiary files the register; the BHC's own group risk-management framework consumes the register data for its consolidated third-party oversight. The BHC view is not a substitute for the EU subsidiary submission.
- A UK PRA-regulated bank with an EU subsidiary: PRA SS2/21 operational resilience and SS1/21 outsourcing and third-party risk apply at the UK entity; DORA applies at the EU entity. Two registers, two filing channels, one underlying truth in the firm's TPRM data.

## Output-template additions for banking

- ECB SSM channel and NCA channel routing flagged in the source-data-posture section.
- EBA outsourcing register reconciliation as a standing reconciliation row (almost always required for EU banks).
- CTPP designation status in the `b_03` records for any provider that meets the candidate criteria (size, criticality, concentration), even where designation has not yet occurred.
- Bank-Service-Company-Act-equivalent posture note where the EU subsidiary's parent is a US bank holding company, for the parent's own consolidated TPRM (not for the DORA submission itself).

## Common pitfalls in banking register builds

- Treating ECB Anacredit, BCBS 239 risk-data-aggregation work, or COREP/FINREP reporting as substitutes for the DORA Register of Information. Each is a separate regulatory artifact with its own schema and channel.
- Submitting the EBA outsourcing register as the DORA register because the data shapes look similar. They do not align column-for-column; the supervisor will reject.
- Missing the consolidation step for a banking group with multiple EU credit-institution subsidiaries that each have their own DORA-scoped activity.
