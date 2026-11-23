# Tushka Protocol Contracts — v1

This directory contains the first machine-readable task and result envelopes for Tushka. The contracts are intentionally transport-neutral: they can be serialized as JSON and carried by a local process, file exchange, or a future authenticated transport.

## Version 1.0

- [Task schema](../spec/v1/task.schema.json)
- [Result schema](../spec/v1/result.schema.json)
- [Task example](../spec/v1/examples/task.json)
- [Successful result example](../spec/v1/examples/result-success.json)
- [Failed result example](../spec/v1/examples/result-failure.json)

Every envelope declares `protocol_version: "1.0"` and a `message_type`. A result echoes the task identifier and includes an agent identifier and explicit status.

## Contract semantics

- `task_id` is an opaque correlation identifier. This schema does not prescribe a UUID format or global uniqueness service.
- `agent_id` is a stable logical identifier asserted by the sender. It is not authentication, a signature, or proof that the named agent produced the content.
- `succeeded` requires `content` and excludes `error`. It means the agent completed its operation, not that its claims are true.
- `failed` and `cancelled` require a structured `error` object.
- Agent content and task prompts are untrusted data. Implementations must not treat either as authority to bypass local policy, permissions, or human approval.
- Unknown fields are rejected in v1 envelopes. Additive fields require a deliberate schema revision rather than silent interpretation.

## Compatibility and evolution

The schema version is explicit so implementations can reject unsupported contracts rather than guess. A future incompatible envelope change must use a new major protocol version and retain the prior schema for readers that still support it. Clarifications that do not change validation behavior may update documentation without changing the schema.

These schemas define serialization only. They do not define transport, agent enrollment, cryptographic identity, authorization, deadlines, cancellation delivery, provenance proofs, or semantic verification. Those require separate contracts and threat modeling before networked execution is introduced.

## Validation

The repository's standard-library tests check that the schema documents and example payloads remain parseable and structurally aligned. For full JSON Schema validation, use a Draft 2020-12 validator against each example; no validator dependency is added to Tushka's runtime.
