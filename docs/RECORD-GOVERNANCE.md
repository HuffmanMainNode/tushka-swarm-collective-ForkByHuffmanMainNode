# Tushka Record Governance v1

**Status:** proposed architecture and implementation contract; not yet implemented.
**Scope:** all Tushka records, including tasks, messages, files, artifacts, agent outputs, decisions, evaluations, audit events, and imported knowledge.

## 1. Purpose

Every stored item must have a defined purpose, an accountable origin, a permitted path, and a lifecycle. Tushka should preserve evidence and attribution without becoming an indiscriminate archive.

**Design rule:** preserve the integrity of necessary history; minimize the data collected, copied, exposed, and retained.

Immutable does not mean permanent retention of every payload. The event history is append-only; sensitive payloads remain subject to access controls, retention limits, correction, legal holds where applicable, and deletion workflows. A deletion or redaction event records that an action occurred without retaining the deleted content.

## 2. Record envelope

Every durable record MUST carry a small, versioned metadata envelope. The payload is stored separately when it is large, sensitive, or subject to a different retention policy.

Required fields:

| Field | Meaning |
|---|---|
| `record_id` | Random, globally unique identifier; never derived from personal data. |
| `record_type` | Controlled type such as task, message, artifact, decision, source, evaluation, checkpoint, audit_event. |
| `schema_version` | Version of the record contract. |
| `created_at` | UTC timestamp from the creating node. |
| `creator` | Agent/node/account identifier or explicit human actor category; do not infer a legal identity. |
| `origin` | Source URI/repository/commit or local-origin marker, where applicable. |
| `purpose` | One declared purpose from a controlled vocabulary. |
| `classification` | public, community, private, confidential, or restricted. |
| `license` | SPDX identifier or `NOASSERTION` / `not-applicable`; never guess. |
| `retention_class` | Declared retention rule and expiry/retention trigger. |
| `content_ref` | Optional storage locator; never an authorization token. |
| `content_digest` | Digest of the exact stored bytes when appropriate; omit for data where hashing creates a privacy/linkability risk. |
| `relationships` | Typed links such as derived_from, cites, supersedes, corrects, replies_to, attached_to. |
| `review_state` | unreviewed, validated, approved, disputed, withdrawn, superseded. |

Optional fields must be justified by the record type. Avoid collecting names, email addresses, precise location, device fingerprints, IP addresses, or model prompts unless necessary, lawful, disclosed, and access-controlled.

## 3. Identity, tags, and directional paths

Tags are navigation metadata, not permissions and not truth labels.

Use a small, namespaced vocabulary:
- `type:task`, `type:decision`, `type:source`
- `domain:orchestration`, `domain:continuity`, `domain:security`
- `state:proposed`, `state:verified`, `state:disputed`
- `scope:private`, `scope:community`
- `retention:ephemeral`, `retention:project`, `retention:legal-hold`

Tags MUST be validated against a registry; arbitrary free-form tags are discouraged. A tag MUST NOT grant access, trigger execution, or override a record's policy. Unknown tags are preserved as untrusted metadata or rejected according to schema version; they never silently gain authority.

Canonical path:

1. **Receive** — accept only through a declared connector or user action.
2. **Quarantine** — mark imported content untrusted; do not execute embedded instructions.
3. **Classify** — determine type, purpose, sensitivity, source, license, and retention.
4. **Validate** — check schema, size, malware/content policy where applicable, and provenance completeness.
5. **Review** — obtain required human or policy approval before publication or consequential action.
6. **Store** — write payload to its authorized namespace and append a minimal provenance event.
7. **Index** — index only fields allowed by classification; private content never enters public/shared indexes.
8. **Retrieve** — enforce authorization and purpose limitation before returning content to an agent.
9. **Transform** — create a new derived record with links to inputs, transformation/version, and responsible actor.
10. **Supersede, expire, or delete** — append a lifecycle event; do not silently rewrite history.

## 4. Immutability and corrections

- Durable event records are append-only; no silent edits or destructive rewriting of provenance.
- Corrections create a new record linked with `corrects` or `supersedes`; retrieval defaults to the current approved version while preserving the authorized audit trail.
- Revocation, withdrawal, or deletion is represented by a minimal tombstone event.
- Payloads may be erased or cryptographically erased where required by retention policy or law. Do not promise that a hash alone anonymizes data.
- Do not put personal data, secrets, access tokens, raw prompts, or full source documents in the immutable event ledger.
- A hash proves byte integrity relative to a known digest; it does not prove authorship, truth, consent, or legal rights.
- Signatures, if added, require key custody, rotation, revocation, and verification rules. A signature does not make a claim true.

No blockchain is required. A local append-only event log plus content-addressed objects, signed checkpoints (when keys are available), and independently verifiable exports are sufficient for the first design.

## 5. Preventing storage and index bloat

Every record must justify its storage cost.

- Deduplicate exact payloads by content digest within the same security boundary; never deduplicate across tenants in a way that reveals whether another user has a file.
- Store large binary artifacts outside the event ledger; the ledger holds a locator and minimal metadata.
- Do not retain full agent chain-of-thought or internal hidden reasoning. Store concise task-relevant summaries, decisions, citations, test evidence, and handoff notes.
- Do not archive every polling event, token stream, transient retry, or repeated prompt. Aggregate routine telemetry and retain only bounded diagnostic windows.
- Apply per-node, per-project, and per-record size limits; reject or defer over-limit writes with a machine-readable reason.
- Use retention classes with expiry dates or explicit review triggers. Expired data is deleted or compacted according to policy.
- Compact event streams into signed/versioned snapshots while retaining the minimum audit references required by policy.
- Index only approved metadata and content. Provide re-indexing and index-deletion paths.
- Track storage by project, class, age, and owner; surface quota warnings before writes fail.

## 6. Default retention classes

These are engineering defaults, not statutory periods. A deployment must set and disclose actual periods after legal and operational review.

| Class | Example | Default behavior |
|---|---|---|
| ephemeral | transient tool output, debug trace | short TTL; never publish by default |
| task | task payload/result | retain through task completion plus configured review window |
| project | approved design, test result, decision | retain while project needs it; periodic review |
| provenance | minimal source/license/derivation event | retain while dependent artifacts rely on it, subject to law |
| security | security incident evidence | restricted access; documented incident retention schedule |
| legal_hold | records subject to preservation duty | suspend ordinary deletion only under documented authority and scope |

Do not set one universal forever-retention policy. A deployment owner is responsible for selecting, documenting, and enforcing its schedule.

## 7. Permissions and data boundaries

- Private/local is the default.
- Sharing requires an explicit, scoped action identifying the exact records, destination, purpose, and license/rights basis.
- A node's membership in a swarm does not grant access to its files, conversations, repository secrets, or local memory.
- Authorization is checked at every read, export, index, transform, and dispatch boundary.
- Agent identity and capability are not authorization. The policy engine decides whether a particular actor may perform a particular action on a particular resource.
- Never use public repository visibility as proof that code, personal data, or other content may be copied or republished.
- Minimize third-party processors and record the categories of recipients and purposes.

## 8. Required record lifecycle tests

- Stable IDs are random and contain no personal information.
- Required metadata and schema versions are validated.
- Unknown tags cannot grant privileges.
- Unauthorized reads, exports, indexes, or dispatches fail closed.
- Private content never appears in community indexes or outbound tasks without explicit permission.
- Corrections create linked successor records; old records are not silently overwritten.
- Deletion removes payloads and indexes under policy while retaining only a lawful minimal tombstone.
- Duplicate storage is prevented only within the same security boundary.
- TTL expiry, quota enforcement, compaction, and restore are tested.
- Every derived artifact identifies its source records and transformation version.
- No test fixture contains real credentials or unnecessary personal data.

## 9. Implementation sequence

1. Define JSON Schema and fixtures for the envelope and lifecycle events.
2. Implement local filesystem/object storage with private namespaces and quotas.
3. Implement append-only event metadata and content-addressed payload storage.
4. Add correction, withdrawal, expiry, deletion, export, and restore workflows.
5. Add provenance-aware retrieval and index filters.
6. Only then evaluate synchronization between two explicitly opted-in local test nodes.

## 10. Non-goals and limits

This document does not claim that Tushka currently implements immutable storage, cryptographic provenance, privacy compliance, legal retention, or deletion guarantees. It is a proposed contract for review and staged implementation. A deployment must be assessed against the laws that apply to its operator, users, data, and use cases.
