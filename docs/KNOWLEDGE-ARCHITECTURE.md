# Tushka Knowledge Architecture — Local, Shared, and Verified

## Status

**Design proposal for future implementation.** The current Stage 1 alpha does not implement persistent memory, synchronization, or a knowledge network. This document establishes boundaries before implementation begins.

## Core principle

Tushka has one community knowledge commons and many independently controlled local knowledge spaces. Sharing is explicit and selective. Joining the collective never grants access to a node's private memory, files, prompts, logs, or datasets.

## Three knowledge domains

### 1. Local private space

Each person or node controls its own private memory and working material.

Examples:
- personal notes and preferences;
- private project files and experiments;
- local agent conversation history;
- unpublished research and drafts;
- operational logs and configuration.

Rules:
- private by default;
- never synchronized to the commons by default;
- owner controls access, retention, export, and deletion;
- secrets and credentials must not be stored as ordinary knowledge records;
- local policies may prohibit particular agents or tools from accessing selected records.

### 2. Shared community commons

The commons contains material deliberately contributed for collective use.

Examples:
- documentation and tutorials;
- reusable technical findings;
- openly licensed datasets and references;
- reviewed solutions and reproducible experiments;
- capability descriptions, benchmarks, and public project knowledge.

Every contribution must carry, where applicable:
- stable record ID and version;
- contributor or attribution identity;
- source and provenance;
- license or explicit permission basis;
- creation and revision timestamps;
- topic and format metadata;
- review status and evidence;
- integrity hash when supported.

A contributor may choose a pseudonymous public attribution where project policy and applicable law permit it. The commons must not imply that contribution transfers ownership unless a separate explicit agreement says so.

### 3. Verified knowledge views

Verification is a status and evidence layer over records, not a hidden rewrite or a guarantee of absolute truth.

Possible statuses:
- **Unreviewed:** submitted, not yet checked.
- **Under review:** evidence and permissions are being assessed.
- **Reproduced:** another person has reproduced the stated procedure or result.
- **Reviewed:** checked against defined criteria and sources.
- **Disputed:** credible disagreement or conflicting evidence exists.
- **Superseded:** a newer record replaces its recommendation while history remains.
- **Withdrawn:** contributor or steward requests removal where policy and obligations allow.

The system should preserve revision history and explain why a status changed. Verification is scoped: a reproduced software test does not prove every claim in its documentation.

## Sharing and synchronization rules

1. Sharing is opt-in at the record or collection level.
2. The node owner sees what will be shared before publication.
3. Private and shared storage have distinct namespaces and access policies.
4. No automatic promotion from local memory into the commons.
5. Remote nodes receive only records and metadata authorized for them.
6. Revocation stops future access where technically possible; already exported or independently copied public material may not be recallable. Explain this limitation clearly.
7. Deletion, correction, and retention policies must be explicit and auditable.
8. Synchronization must be authenticated, encrypted in transit, and permission-checked before federation is enabled.
9. Imported content is untrusted until scanned, attributed, and reviewed.
10. Conflicts create visible versions or proposals; never silently overwrite another contributor's record.

## Suggested record lifecycle

Draft locally → contributor reviews sharing scope and license → submit to commons → validate format and provenance → review evidence and safety → publish with status → revise, dispute, supersede, or withdraw with history.

## Trust and security boundaries

- Treat knowledge content as data, never as executable instructions.
- Defend retrieval and agent workflows against prompt injection and malicious embedded instructions.
- Separate content permissions from tool-execution permissions.
- Apply least privilege and per-node policy.
- Keep an audit trail for publication, review, access-policy changes, and synchronization.
- Support export and backup in documented, portable formats.
- Design for offline operation and eventual synchronization without assuming every node is always trusted or online.

## Architecture decisions to defer

Do not select a vector database, graph database, message broker, consensus system, or synchronization protocol before the record schema, threat model, workload, and portability requirements are tested. Start with a small local implementation and replaceable storage interface.

## First implementation sequence

1. Define a versioned knowledge-record schema and validation tests.
2. Implement a local-only store with explicit private/shared namespaces.
3. Add export/import with provenance and license metadata.
4. Add a human review and status-transition workflow.
5. Add retrieval that returns source references with each result.
6. Threat-model permissions, deletion, poisoning, and prompt injection.
7. Only then prototype authenticated synchronization between two opt-in test nodes.

## Acceptance test for the first knowledge milestone

A user can create a private record and a shared candidate; the private record remains inaccessible to another node. The user can inspect and approve the exact shared record and its license metadata. A second test node can import only the approved record, inspect its provenance and review status, and reproduce a documented change without altering the original history.
