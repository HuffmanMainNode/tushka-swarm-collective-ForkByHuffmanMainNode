# Roadmap

This roadmap is staged so each phase leaves a runnable, reviewable result.

## Phase 0 — Executable foundation

- [x] Repository purpose and initial architecture
- [x] Provider-neutral agent interface
- [x] Async coordinator with timeout and failure isolation
- [x] Two-agent demonstration
- [x] Unit tests for collection, failure, timeout, and synthesis

## Phase 1 — Useful local swarm

- [ ] Structured task/result schemas and JSON serialization
- [ ] Agent capability registry and task routing
- [ ] Local model adapter behind the Agent interface
- [ ] Configurable agent roles and prompts
- [ ] Independent verifier agent and task-specific evaluation
- [ ] CLI for submitting and inspecting tasks

## Phase 2 — Knowledge and provenance

- [ ] Versioned knowledge records with source references
- [ ] Retrieval interface independent of storage backend
- [ ] Citation/provenance propagation into agent results
- [ ] Human review and correction workflow
- [ ] Export and backup format

## Phase 3 — Federated nodes

- [ ] Node identity and enrollment
- [ ] Authenticated transport and authorization policy
- [ ] Remote task execution with quotas and cancellation
- [ ] Node health, observability, and recovery
- [ ] Threat model and security review before public deployment

## Phase 4 — Community collective

- [ ] Contribution and capability registry
- [ ] Interoperability tests for independent implementations
- [ ] Governance and maintainership succession
- [ ] Reproducible evaluation suite
- [ ] Portable deployment and documentation

## Definition of done for the first milestone

A developer can clone the repository, run the tests, execute the demo, and observe two separately identified agents responding to the same task. A failed or timed-out agent is reported without discarding another agent's usable result.
