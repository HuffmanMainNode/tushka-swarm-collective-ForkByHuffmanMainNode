# Tushka Protocol Contracts — v1

This directory contains the first machine-readable task and result envelopes for Tushka. The contracts are transport-neutral: they can be serialized as JSON and carried by a local process, file exchange, or a future authenticated transport.

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
- `failed` and `cancelled` require a structured `error` object and must not include success `content`.
- Error objects require non-empty string `code` and `message` fields; `retryable`, when present, must be boolean. Unknown error fields are rejected.
- Unknown envelope fields are rejected in v1. Additive fields require a deliberate schema revision rather than silent interpretation.
- Agent content and task prompts are untrusted data. Implementations must not treat either as authority to bypass local policy, permissions, or human approval.

## Prompt size limit

A v1 task prompt MUST be no larger than **65,536 UTF-8 bytes (64 KiB)** after UTF-8 encoding. The limit is measured in bytes, not Unicode characters; multi-byte characters count according to their encoded length. Exactly 65,536 bytes is accepted; 65,537 bytes is rejected.

JSON Schema's `maxLength` counts characters, not UTF-8 bytes, so this byte limit is an additional protocol-level validation rule and is intentionally not represented as `maxLength`. A receiver MUST enforce the byte limit at the protocol-ingress/validation boundary before queueing or dispatching the task. Adapter-specific transport limits may be lower, but must not be treated as changing this protocol maximum.

## Compatibility and evolution

The schema version is explicit so implementations can reject unsupported contracts rather than guess. A future incompatible envelope change must use a new major protocol version and retain the prior schema for readers that still support it. Clarifications that do not change validation behavior may update documentation without changing the schema.

These schemas define serialization only. They do not define transport, agent enrollment, cryptographic identity, authorization, deadlines, cancellation delivery, provenance proofs, or semantic verification. Those require separate contracts and threat modeling before networked execution is introduced.

## Validation

The protocol tests use the `jsonschema` package's `Draft202012Validator` to meta-validate both schemas and validate all example fixtures. They also exercise invalid payloads and the UTF-8 byte limit. Install the test dependency with `python -m pip install -r requirements-test.txt`. This is a test-only dependency; it is not added to Tushka's runtime dependencies.
