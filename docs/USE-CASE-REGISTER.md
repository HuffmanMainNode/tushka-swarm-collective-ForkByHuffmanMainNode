# Tushka Use-Case Register

**Status:** template and initial project-level entries; deployments must add their own entries.
**Rule:** no new capability or deployment goes live without a completed use-case record and assigned reviewer.

## Use-case lifecycle

`proposed → assessed → approved-with-controls → enabled → monitored → suspended/retired`

Approval is scoped to a purpose, dataset, operator, environment, and version. It is not transferable to a different context without reassessment.

## Register

| ID | Use case | Data scope | Risk tier | Current status | Required gate |
|---|---|---|---:|---|---|
| TSK-UC-001 | Local development and test orchestration | repository files explicitly made available; synthetic test data | 1 | proposed | sandbox, secret scanning, test limits, user-controlled repository permissions |
| TSK-UC-002 | Local model inference adapter | task text supplied by operator; local endpoint configuration | 1–2 | experimental | endpoint allowlist, size/time limits, no secret logging, model output treated as untrusted |
| TSK-UC-003 | Agent-to-agent task dispatch | task/result envelopes; private payload only with explicit grant | 2 | proposed | bounded broker, identity, per-task authorization, quotas, idempotency, audit metadata |
| TSK-UC-004 | Persistent knowledge and continuity | private local records by default; explicit shared records | 2–3 | proposed | record governance, retention, correction/deletion, provenance, access controls |
| TSK-UC-005 | GitHub issue/PR automation | repository metadata and code in authorized repositories | 2 | operator-authorized only | GitHub terms, official API, least privilege, rate limits, human approval for external writes |
| TSK-UC-006 | Federated node cooperation | explicitly selected task and metadata; no default private-memory sync | 3 | not enabled | identity, authenticated transport, authorization, isolation, privacy assessment, incident plan |
| TSK-UC-007 | Consequential decisions about people | personal data and decision inputs | 3 | prohibited by default / legal review required | jurisdiction-specific legal assessment, required disclosures/rights, validated system, human accountability |

## Required entry template

Copy this template for each new use case:

### TSK-UC-XXX — [name]

- **Owner/operator:**
- **Purpose and intended users:**
- **Deployment location/jurisdictions:**
- **People affected:**
- **Data categories and sources:**
- **Sensitive data / minors involved:**
- **Controller / processor roles (if applicable):**
- **Legal basis, notices, consents, and permissions:**
- **Recipients, subprocessors, and transfers:**
- **Model, tools, and version:**
- **Known limitations and prohibited uses:**
- **Risk tier and rationale:**
- **Human approval / oversight:**
- **Retention and deletion schedule:**
- **GitHub/platform terms and licenses reviewed:**
- **Security, privacy, bias, and accessibility tests:**
- **Incident response and rollback:**
- **Approval evidence / reviewer:**
- **Review date and change triggers:**

## Important boundary

The project-level entries above describe intended engineering controls, not a legal determination or authorization to deploy. Each node operator must complete the template for its actual use, data, users, and jurisdiction.
