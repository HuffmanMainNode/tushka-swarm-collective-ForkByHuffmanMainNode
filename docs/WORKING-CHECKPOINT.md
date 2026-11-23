# Tushka Collective — Shared Working Checkpoint

**Checkpoint:** 2026-11-23  
**Status:** Active integration checkpoint — Stage 1 alpha  
**Purpose:** Keep every participating account, fork, and contributor aligned while allowing anyone to pause, switch tasks, or resume without losing context.

This checkpoint records the shared project state. It is not a claim that every item is complete, tested, or merged. GitHub issues, pull requests, commits, and this document are the durable source of truth; individual accounts are contributors, not owners of the project's memory.

## 1. Shared north star

Build an open, model-independent, local-first and community-operated collective. People and independent nodes should be able to contribute useful work, preserve attribution and permissions, verify results, and continue even when another person, account, provider, or machine is offline.

Participation is voluntary and asynchronous. Nobody is expected to be continuously online. A task must be understandable and resumable by another authorized contributor.

## 2. Current integration board

| Workstream | Current record | Focus | Handoff condition |
|---|---|---|---|
| Protocol contracts | [PR #5](https://github.com/TushkaLoLz31337/tushka-swarm-collective/pull/5) | Versioned task/result envelopes, validation, compatibility, negative tests | Contract examples and tests are clear; CI passes; integration notes are posted |
| Local model + coordinator | [PR #4](https://github.com/TushkaLoLz31337/tushka-swarm-collective/pull/4) | Local model adapter, coordinator reliability, limits and timeout tests | Adapter behavior and limits are tested; endpoint expectations documented; CI passes |
| Communication broker | [Issue #6 — TSK-COMMS-001](https://github.com/TushkaLoLz31337/tushka-swarm-collective/issues/6) | Bounded queue, routing, admission, acknowledgements, lifecycle, retries, cancellation, fairness, idempotency | Local in-process broker design and acceptance tests agreed; build in small reviewable PRs |
| Project integration | [Roadmap](ROADMAP.md) · [Architecture](ARCHITECTURE.md) | Keep work aligned, review evidence, update checkpoint and roadmap | Every merged change updates relevant docs/tests and leaves a clear next step |

PR #4 and PR #5 are complementary foundations, not competing implementations. Keep their boundaries separate: protocol defines portable message meaning; the adapter executes work; the broker schedules and tracks work. Do not introduce remote execution until identity, authorization, isolation, privacy, and resource limits are designed and tested.

## 3. Suggested workstream stewardship

These are suggested focus areas, not exclusive ownership or permanent assignments:

- **Ryzean84:** protocol contracts, interoperability, schema evolution, fixtures and validation tests.
- **HuffmanMainNode:** local-model adapter, coordinator behavior, resource limits and reliability tests.
- **TushkaLoLz31337:** upstream integration, checkpoint maintenance, roadmap alignment, review coordination and release readiness.
- **Any participating account or contributor:** may pick up an unblocked issue, reproduce a bug, add tests/docs, review evidence, or propose a better design. Coordinate before overlapping edits to the same files.

A GitHub account is an identity for attribution, not a measure of authority or contribution value. Use least privilege; do not grant blanket administrator access merely to make collaboration possible.

## 4. The pause / resume / handoff rule

Anyone can stop at any time. Before pausing, leave a short note on the relevant issue or PR using this format:

- **Status:** exploring / in progress / blocked / ready for review / paused
- **Last completed:** specific commit, file, test, or decision
- **Next smallest step:** one actionable task
- **Current branch / PR:** link, if applicable
- **Open questions or blockers:** include evidence and what is needed
- **Risks / files being changed:** mention possible conflicts
- **Resume instructions:** exact command, test, or place to continue

A successor should be able to resume from the note without needing a private conversation. If no note exists, ask for clarification rather than overwriting uncertain work. Never force-push, discard, or replace another contributor's work without explicit coordination.

## 5. Shared task lifecycle

Every piece of work should move through visible states:

**Proposed → Ready → In progress → Review → Accepted / Merged → Verified**

It may also be **Blocked**, **Paused**, or **Needs decision**. A pause is not a failure and does not erase progress. Reopen or split work rather than silently dropping it.

For broker tasks, the runtime lifecycle will be more detailed: created → accepted → queued → assigned → running → succeeded / failed / cancelled / expired. Capacity pressure should normally produce a clear queued or deferred response, not an unexplained denial. Genuine policy, permission, or invalid-input failures remain explicit rejections.

## 6. Working agreements

1. One canonical upstream issue or PR per work item; forks are workspaces, not separate competing plans.
2. Before coding, read the linked issue, current main, and active PRs touching the same area.
3. Keep PRs small, focused, tested, and explicit about what is not implemented.
4. Never claim a test, security property, or feature is complete without evidence.
5. Preserve authorship, license, provenance, and fork/upstream history.
6. Do not commit credentials, private data, or another person's unpublished material.
7. Treat prompts and model output as untrusted data; private memory is never shared by default.
8. Prefer queue/defer and transparent recovery over silent loss or unnecessary denials.
9. When two contributions overlap, coordinate at the issue before merging; integrate by review, not by account priority.
10. Update this checkpoint whenever a meaningful milestone, blocker, ownership handoff, or integration decision changes.

## 7. Immediate checkpoint actions

- [ ] PR #4: add tests for prompt/response size limits and request timeout; clarify base URL path behavior; obtain passing CI.
- [ ] PR #5: add negative contract tests (unknown fields, unsupported version, invalid status, conditional result rules); clarify prompt-size enforcement; obtain passing CI.
- [ ] Shared: agree the broker's first local-only API and lifecycle tests in Issue #6.
- [ ] Shared: ensure the broker consumes the protocol contract and dispatches to the local agent adapter without coupling transport to model provider.
- [ ] Integration: after review and passing checks, merge in dependency order and update the roadmap/checkpoint with exact commit links.
- [ ] Participation: every contributor who pauses leaves a handoff note; every contributor who resumes posts what they picked up.

## 8. Definition of a healthy checkpoint

We are aligned when any authorized participating account can answer: what is the goal, what is already done, what is not done, what is blocked, where the source of truth lives, and what is the next safe step.

We are making progress when the work is reproducible, reviewable, and transferable—not merely when accounts are active. The collective must be able to keep moving without requiring any one account to remain online.
