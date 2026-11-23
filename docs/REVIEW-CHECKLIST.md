# Founding review checklist

This checklist is for independent technical review of the initial public foundation.

## Review the project direction

- [ ] Does the mission describe the intended community-built, decentralized, model-independent system?
- [ ] Are the boundaries between coordinator, agents, adapters, knowledge, and nodes clear?
- [ ] Are prototype capabilities distinguished from planned capabilities?
- [ ] Are there hidden assumptions that would force a proprietary provider or paid API?

## Review the implementation

- [ ] Is the Agent interface small and usable by independent implementations?
- [ ] Does the coordinator preserve agent attribution?
- [ ] Are timeouts and individual failures isolated?
- [ ] Does synthesis expose failures instead of hiding them?
- [ ] Are tests sufficient for the first milestone?
- [ ] What should be changed before adding a real local model adapter?

## Review security and stewardship

- [ ] Are secrets and private data excluded?
- [ ] Are remote execution and tool execution correctly treated as future security work?
- [ ] Are ownership, licensing, and provenance expectations clear?
- [ ] Can independent contributors participate without transferring ownership of their repositories?

## Submit findings

Please open separate issues for actionable defects or proposals. For general feedback, comment on the repository's first milestone issue. Identify findings as:
- **Blocker** — unsafe or incorrect to proceed.
- **Important** — should be addressed before the next milestone.
- **Suggestion** — useful improvement that does not block progress.

Do not treat account names as assigned technical roles until their owners explicitly agree to them.
