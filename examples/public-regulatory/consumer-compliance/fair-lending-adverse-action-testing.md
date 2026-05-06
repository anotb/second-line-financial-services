# Fair lending and adverse action testing scenario

## Source anchors

- CFPB Section 1071 materials address collection and reporting of small business lending application data, privacy interests, shielding certain demographic data, and recordkeeping.
- CFPB Regulation B section 1002.107 describes compilation and maintenance of reportable covered-application data.

## Scenario

A small business lending platform uses automated reason-code suggestions for declined applications. Compliance testing wants to review reason-code traceability, data completeness, protected demographic data firewall, and complaint themes.

## Test focus

| Control area | Test procedure |
|---|---|
| Data completeness | Compare application register fields to source application and decision records |
| Reason-code traceability | Trace adverse action reasons to underwriting criteria and source facts |
| Protected data firewall | Inspect role access and exception approvals |
| Complaint feedback | Compare complaint themes to denial reasons and remediation records |
| Change governance | Review changes to automated reason-code logic and approval evidence |

## Human-review gate

Fair lending counsel should review testing design, statistical limitations, exceptions, and remediation language.
