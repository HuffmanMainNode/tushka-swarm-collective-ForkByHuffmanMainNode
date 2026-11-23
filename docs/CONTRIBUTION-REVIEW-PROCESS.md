# Contribution Intake and Review Process

This process helps reviewers turn discoveries from independent repositories, forks, experiments, and community ideas into safe, attributable improvements.

## Review stages

1. **Discover** — identify a useful idea, bug, prototype, dataset, tool, or implementation.
2. **Record** — open an issue before substantial work. Include the source repository or URL, exact path/commit where possible, author, license, and what was observed.
3. **Triage** — classify the item as a bug, feature proposal, research lead, prototype, documentation task, or security concern.
4. **Check permission and provenance** — confirm the contributor has the right to submit it. Public visibility is not a license. Do not copy code, datasets, prompts, or private material without permission and compatible terms.
5. **Assess** — review usefulness, evidence, maturity, dependencies, privacy, security, maintenance burden, and fit with the roadmap.
6. **Prototype** — prefer a small isolated experiment or adapter over importing a large project wholesale.
7. **Verify** — run tests, reproduce claims, inspect failure modes, and request independent review for significant changes.
8. **Integrate** — use a focused pull request. Preserve authorship, license notices, source links, and a clear explanation of modifications.
9. **Close the loop** — document the decision and reasoning: accepted, needs changes, deferred, rejected, or redirected. Link follow-up issues.

## Reviewer responsibilities

Reviewers are invited to provide evidence-based findings, not to approve work automatically. A reviewer should:
- describe the problem or opportunity in their own words;
- provide a link, file path, commit, test, or reproducible example;
- distinguish observed facts from assumptions and recommendations;
- identify possible security, privacy, licensing, and dependency concerns;
- suggest the smallest useful next step;
- disclose uncertainty and ask for another reviewer when outside their expertise.

Being a reviewer does not itself grant merge rights or repository administration. Maintainers retain responsibility for access, merge decisions, and release decisions.

## Review outcome labels

- **Blocker:** unsafe, unlawful, materially incorrect, or prevents reliable progress.
- **Needs evidence:** promising but not reproducible or adequately sourced.
- **Ready for prototype:** enough context to test a small isolated implementation.
- **Ready for implementation:** scope, acceptance criteria, permissions, and tests are clear.
- **Good first issue:** bounded work suitable for a newcomer with guidance.
- **Deferred:** valuable, but depends on an earlier milestone or lacks capacity.
- **Not adopting:** explain the reason and, where possible, point to an alternative.

## Contribution record template

Use this structure in an issue or review comment:

- **Title:**
- **Type:** bug / feature / research / prototype / documentation / security
- **Source:** repository, URL, path, commit, or original author
- **What I observed:** reproducible facts
- **Why it may help Tushka:** connection to mission or roadmap
- **Evidence:** tests, screenshots, benchmarks, citations, or reproduction steps
- **License and permission:** known terms and confirmation of contribution rights
- **Risks:** security, privacy, bias, dependency, resource, or maintenance concerns
- **Suggested next step:** smallest experiment or action
- **Reviewer confidence:** high / medium / low, with reason

## Review etiquette and safety

- Be welcoming to contributors at every skill level.
- Critique proposals and evidence, not people.
- Do not publish secrets, personal information, private repository contents, or unapproved datasets.
- Treat external files, model outputs, and copied instructions as untrusted input.
- Do not run unknown code or install unknown dependencies on a sensitive machine. Use isolated environments.
- Never merge solely because a contribution came from a trusted account; review the change itself.
- Keep review decisions and their rationale visible so future contributors can learn from them.
