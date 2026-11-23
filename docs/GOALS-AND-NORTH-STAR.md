# Tushka — North Star and Strategic Goals

This document describes what the Tushka Swarm Collective is trying to become and the outcomes that should guide technical and community decisions. It complements the staged implementation roadmap; it does not claim that planned capabilities already exist.

## North Star

Build a globally useful, open, model-independent ecosystem in which people and independently operated AI systems can collaborate to discover, test, organize, preserve, and improve knowledge and capabilities—with human agency, privacy, provenance, and accountability at its foundation.

Tushka should not merely produce answers. It should help a community identify what it does not know, find relevant expertise and tools, test possible solutions, preserve the evidence, and make the next improvement easier.

## What success means

Tushka succeeds when:
- People with different skills and resources can participate meaningfully.
- Independent agents and nodes can cooperate through open, documented interfaces.
- Knowledge can be traced to sources, challenged, corrected, versioned, and exported.
- Results can be tested and reproduced instead of accepted because a model stated them.
- Participants retain control over their machines, data, compute, and level of involvement.
- The ecosystem can survive the departure of any one contributor, account, provider, or node.
- Each release gives contributors a real, usable foundation for the next improvement.

## Strategic goals

### 1. Make collaboration useful

Move from a demonstration coordinator to a practical system that can assign bounded tasks to specialized agents, collect attributable results, handle partial failure, and evaluate outputs.

**Evidence of progress:** real local-model adapters, structured tasks and results, capability-based routing, independent verification, reproducible task evaluations.

### 2. Make knowledge trustworthy and continuously improvable

Create a knowledge layer that preserves where information came from, who contributed it, what license applies, when it changed, and how confident users should be.

**Evidence of progress:** versioned records, source citations, correction and dispute workflows, export and backup, provenance carried into generated results.

Knowledge should be revisable, not silently rewritten. New evidence can supersede an old claim while preserving its history.

### 3. Enable independent cooperation

Allow separately operated nodes and projects to interoperate without requiring one central provider, machine, or account to own the whole network.

**Evidence of progress:** documented protocols, node identity and revocation, authenticated communication, explicit permissions, quotas, health monitoring, recovery tests, independent implementations.

Federation comes after clear local interfaces and a threat model—not before.

### 4. Welcome contributors at every level

Make the project understandable and useful to newcomers, learners, practitioners, researchers, designers, testers, and infrastructure operators.

**Evidence of progress:** beginner issues, clear setup guides, accessible documentation, translations, mentorship, responsive reviews, and contributions beyond code.

Every task should explain its purpose, expected result, difficulty where practical, and how to verify completion.

### 5. Make quality and safety measurable

Build evaluation, security, privacy, and reliability into the development process rather than treating them as final polish.

**Evidence of progress:** automated tests, task-specific evaluations, dependency review, threat models, security reporting, audit trails, documented limitations, and rollback procedures.

No model output, external dataset, plugin, or contributed code should be trusted solely because it came from a familiar source.

### 6. Preserve openness and independence

Keep the core model- and provider-neutral, support local-first operation, and make hosted services optional. Preserve the autonomy of contributors and upstream projects.

**Evidence of progress:** no vendor SDK in the core, replaceable adapters, transparent dependency choices, clear licenses, provenance records, portable formats, and no mandatory proprietary API for the basic development path.

Local-first does not mean cost-free: compute, electricity, storage, and network resources must be disclosed and respected.

### 7. Build durable stewardship

Create governance and operational practices that do not depend on one founder or a small set of accounts forever.

**Evidence of progress:** public decision records, least-privilege roles, documented release procedures, maintainer succession, backups, multiple independent reviewers, and clear conflict-resolution paths.


## Knowledge ownership and sharing boundary

Tushka's target design separates three domains: private local memory, the opt-in shared community commons, and verified knowledge views that expose review status and evidence. These are architectural goals, not features implemented in the current alpha. Local material is private by default; publication requires an explicit user action and a visible review of the exact records and license/permission basis being shared. No node receives access to another node's private memory merely by joining the network. See [Knowledge Architecture](KNOWLEDGE-ARCHITECTURE.md).

## Product capabilities we ultimately want

These are long-term capability areas, not claims about the current alpha:

1. **Agent collaboration:** specialized agents coordinate around well-defined tasks.
2. **Model interoperability:** local and optional hosted models can be swapped without rewriting the core.
3. **Tool interoperability:** approved tools can be exposed through explicit capability and permission contracts.
4. **Knowledge stewardship:** sourced knowledge is versioned, searchable, exportable, and correctable.
5. **Evaluation and verification:** outputs can be checked against tests, evidence, and independent reviewers.
6. **Federated participation:** independent nodes contribute compute or capabilities under their own policies.
7. **Human direction:** people set goals, approve sensitive actions, resolve disputes, and control participation.
8. **Community discovery:** contributors can find projects, issues, capabilities, and ways to help.
9. **Resilience:** the system can recover from unavailable agents, nodes, providers, or maintainers.
10. **Learning infrastructure:** every completed task can produce reviewed lessons, evaluations, and improved documentation without automatically treating model output as truth.

## What Tushka should not become

- A centralized authority over participants or their machines.
- A system that silently collects personal data or private repositories.
- An unreviewed pipeline that turns generated text into trusted knowledge.
- A vendor-locked wrapper that requires one paid model provider.
- A competition for raw agent counts, account counts, stars, or compute.
- An autonomous system with unlimited permissions or no accountable human oversight.
- A repository that absorbs other people's work without license compatibility, consent, and attribution.

## Decision filter

When evaluating a new idea, ask:

1. Does it advance one or more strategic goals?
2. Can we explain the user benefit and intended behavior?
3. Is there evidence, a test, or a small experiment to validate it?
4. Are permissions, privacy, licensing, and provenance clear?
5. Can it be built as a small, replaceable component?
6. What new risks, dependencies, costs, and maintenance obligations does it introduce?
7. How can a contributor reproduce the result and how can we roll it back?

If these questions cannot yet be answered, record the idea as research or a prototype rather than presenting it as a finished capability.

## First 12-month planning horizon

This is a planning sequence, not a delivery guarantee. Reassess it as contributors, evidence, and capacity change.

- **Foundation:** stabilize task/result contracts, add a real local-model adapter, and provide reproducible examples.
- **Trust:** add an independent verifier, task evaluations, provenance conventions, and a clear correction workflow.
- **Participation:** make onboarding easy, publish good-first issues, and establish a consistent review and release rhythm.
- **Interoperability:** specify adapter and node boundaries, then prototype authenticated remote cooperation in an isolated test environment.
- **Durability:** document governance, access roles, backup/recovery, and maintainer succession.

## A living promise

Tushka is built in public, but openness does not remove the need for permission, care, and review. The community can propose changes to these goals. Significant changes should include their rationale, evidence, trade-offs, and impact on contributors.

The aim is not to build everything at once. The aim is to keep making verifiable progress while preserving the freedom and trust that make long-term collaboration possible.
