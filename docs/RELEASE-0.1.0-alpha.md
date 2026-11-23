# Tushka Swarm Collective v0.1.0-alpha — Stage 1

**Release type:** Alpha / experimental  
**Purpose:** Establish a forkable, provider-neutral orchestration foundation for the Tushka AI collective.

## Included

- Async coordinator for dispatching work to multiple agents.
- Agent protocol boundary that avoids binding the core to one model provider.
- Concurrent execution with timeout and exception isolation.
- Result attribution and explicit reporting of failed agents.
- Deterministic demonstration agents.
- Unit tests and GitHub Actions CI.
- Contribution, security, architecture, roadmap, and review guidance.

## Important limitations

This is an early orchestration prototype, not a complete decentralized AI network.

- Demo agents are deterministic placeholders, not real LLM integrations.
- No local-model adapter is included yet.
- No peer-to-peer networking, federation, shared knowledge synchronization, or distributed trust system is implemented.
- No production deployment or security audit is claimed.
- Passing CI verifies the current automated test suite, not production readiness.

## Stage 1 acceptance goals

1. Contributors can fork and install the project.
2. The automated test workflow passes.
3. The coordinator can dispatch to independent agent implementations and preserve attribution.
4. Contributors can propose adapters and improvements through pull requests.
5. Future work preserves provider independence, local-first operation, provenance, and transparent failure handling.

## Next milestone

Implement and test the first real local-model adapter behind the existing agent protocol. Track progress in issue #1.

## Forking and upstreaming

Fork this release into your participating accounts, keep each fork's identity and history intact, and use pull requests to propose improvements upstream. A fork is an independent workspace; changes are not part of the upstream project until accepted and merged.

## License

Apache License 2.0. See [LICENSE](../LICENSE).
