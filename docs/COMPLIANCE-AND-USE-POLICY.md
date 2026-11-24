# Tushka Compliance and Use Policy

**Status:** proposed project-wide engineering policy; not legal advice or a certification.
**Applies to:** core software, agents, tools, adapters, repositories, community nodes, datasets, integrations, demos, and deployments.

## 1. Operating principle

Tushka is intended to support lawful, permissioned, accountable collaboration. No feature, agent, connector, or use case is exempt from this policy. Each deployment operator remains responsible for determining which laws, contracts, platform terms, and sector-specific rules apply.

Tushka cannot guarantee that every possible use is lawful. It must make lawful use easier to identify, unsafe or unauthorized use harder to perform, and evidence of decisions available for review.

## 2. GitHub platform requirements

When Tushka or its contributors interact with GitHub:

- Follow the current GitHub Terms of Service, Acceptable Use Policies, API terms, privacy statement, product-specific terms, and applicable repository license.
- Use official APIs and supported authentication flows where practical. Respect rate limits, secondary limits, abuse controls, and Retry-After responses.
- Never share personal access tokens between accounts or use multiple tokens/accounts to evade rate limits, suspensions, or platform restrictions.
- Do not scrape or collect personal information for unsolicited contact, profiling, sale, or unrelated purposes. Respect removal, complaint, and do-not-contact requests.
- Do not use GitHub as infrastructure for unauthorized access, malware, command-and-control, spam, disruption, or other prohibited activity.
- Automated accounts must act transparently, use credentials owned/authorized for that integration, follow least privilege, and leave attributable commits, comments, and pull requests. Do not impersonate people or misrepresent human review.
- Do not mass-create issues, comments, PRs, forks, stars, or other engagement. Require deduplication, rate limiting, bounded retries, and human review for broad or externally visible actions.
- Never use an agent to bypass repository rules, branch protections, required reviews, Actions approval, or account restrictions.
- Keep credentials in GitHub Actions secrets or an appropriate secret manager; never commit tokens, private keys, session cookies, or secrets to issues, logs, artifacts, or prompts.
- Use GitHub-hosted compute and Actions within the applicable product terms, fair-use constraints, quotas, and billing controls.

Public repository content is publicly accessible, but this does not erase copyright, license, privacy, confidentiality, or other legal obligations. Before reuse, inspect the exact source revision, per-file notices, license, dependencies, and upstream lineage. Preserve copyright and license notices and identify modifications. If rights are unclear, do not copy; link and request clarification.

## 3. Colorado and United States privacy baseline

For deployments operated from Colorado or processing Colorado residents' data, assess applicability of the Colorado Privacy Act (CPA), its rules, Colorado data-security and breach-notification statutes, and applicable federal and other state laws.

Engineering baseline:
- State the purpose before collecting personal data.
- Collect only what is adequate, relevant, and reasonably necessary for that purpose.
- Do not repurpose personal data for a materially different purpose without a valid legal basis and required notice/consent.
- Provide clear privacy notices, access/correction/deletion/portability mechanisms where applicable, and a contact path for privacy requests.
- Use reasonable administrative, technical, and physical safeguards appropriate to data sensitivity and risk.
- Establish documented retention and secure disposal rules.
- Review processors and service providers; contractually require appropriate safeguards where required.
- Conduct and document a data protection assessment when required, including processing of sensitive data, sale, targeted advertising, or qualifying high-risk profiling.
- Provide required opt-out mechanisms for targeted advertising, sale, or certain profiling, including applicable universal opt-out signals.
- Do not assume the CPA applies to every person or project: statutory thresholds, exemptions, controller/processor roles, and context matter. Have qualified counsel assess applicability.

Colorado breach response must be designed before an incident. The operator should preserve evidence, contain the incident, investigate promptly, determine affected data and residents, and obtain legal advice on notice obligations and deadlines. Colorado's official guidance describes a 30-day outer deadline in covered circumstances and Attorney General notice for breaches affecting 500 or more Colorado residents; applicability and the trigger must be confirmed by counsel.

## 4. Colorado AI and automated decision systems

Tushka is a general-purpose collaboration framework, but downstream deployments may enter regulated use cases. A general-purpose label does not exempt a particular deployment.

Before use in employment, education, housing, lending, financial services, insurance, healthcare, essential government services, public benefits, or another consequential domain:
- Identify whether the deployment is a covered AI system, high-risk system, or automated decision-making technology under the law in force at the time.
- Document intended use, prohibited/unsupported uses, model and data limitations, known risks, human oversight, testing, monitoring, and incident response.
- Assess discrimination, accessibility, privacy, security, and disparate impact risks.
- Provide disclosures and consumer rights required by the applicable law.
- Keep a qualified human accountable for consequential decisions; provide meaningful review and appeal where required.
- Do not make a consequential decision solely from an unverified model output.
- Re-check law and effective dates before release; Colorado's AI statutes were amended in 2026 and obligations may phase in.

The project must not claim compliance merely because a model card, risk checklist, or audit log exists.

## 5. Universal prohibited-use baseline

Tushka deployments must not be configured to facilitate:
- unauthorized access, credential theft, malware, destructive actions, or evasion of security controls;
- harassment, stalking, doxxing, targeted intimidation, or non-consensual surveillance;
- unlawful discrimination, deceptive impersonation, fraud, scams, or identity misuse;
- unlawful collection, sale, disclosure, or profiling of personal data;
- copyright/license circumvention or removal of attribution and provenance;
- prohibited weapons, violent wrongdoing, or other unlawful harmful activity;
- spam, platform manipulation, artificial engagement, or evasion of platform enforcement.

This list is a minimum project policy, not a complete statement of law. Use cases must also follow applicable export controls, sanctions, consumer-protection, employment, accessibility, health, financial, child-safety, and sector-specific requirements.

## 6. Risk-tiered action permissions

| Tier | Examples | Default control |
|---|---|---|
| 0 — Read-only | read authorized docs, inspect local tests | allowed within granted scope |
| 1 — Local reversible | edit a working branch, run tests, create local artifacts | sandbox, resource limits, audit event |
| 2 — External side effect | open issue/PR, send message, publish package, deploy | explicit authorization, preview, rate limit, attributable actor |
| 3 — Sensitive/high impact | access personal/sensitive data, make consequential recommendation, change permissions, production changes | documented legal/risk assessment, least privilege, human approval and oversight |
| 4 — Prohibited | unauthorized access, evasion, unlawful surveillance, harmful or illegal conduct | deny, log minimal policy event, escalate where appropriate |

A tool capability is not a permission. Every action is checked against identity, resource, purpose, scope, risk tier, and current authorization.

## 7. Required use-case record

Before a new feature, integration, or deployment is enabled, record:
- intended purpose and users;
- operator/controller/processor roles where applicable;
- data categories, sources, sensitivity, and affected people;
- lawful/permission basis and notices/consents;
- recipients, subprocessors, and cross-border transfers;
- model/tool capabilities and known limitations;
- prohibited uses and abuse scenarios;
- risk tier and required human approvals;
- retention, deletion, and user-rights workflow;
- GitHub/platform terms and license review where relevant;
- tests, monitoring, incident response, and rollback plan;
- accountable maintainer and review date.

No use case may bypass this record because it is a prototype, open-source, local, or agent-operated.

## 8. Open-source provenance and authorship

- Preserve upstream copyright, license, NOTICE, and attribution requirements.
- Record repository, exact commit, source path, author/copyright notice, license, modifications, and destination path for reused code.
- Do not infer individual authorship from repository ownership.
- Keep dependency and license inventories; review transitive dependencies.
- If origin or license is uncertain, keep the work as a linked reference only.
- Contributions must be submitted by people/accounts with authority to license them; do not submit copied private, confidential, or employer-owned materials without permission.

## 9. Review and enforcement workflow

Every feature follows:
**Propose → classify → assess → implement behind limits → test → review → approve → monitor → retire.**

The reviewer checks legal/terms applicability, privacy, security, provenance, accessibility, reliability, and cost. A failed or incomplete assessment blocks release or keeps the feature disabled. Material changes to purpose, data, model, recipient, or deployment context trigger reassessment.

## 10. Governance and limitations

This is an engineering policy, not a legal opinion, privacy notice, data-processing agreement, or guarantee of compliance. Legal obligations depend on the operator, organizational status, data subjects, data types, location, and actual deployment. Obtain Colorado and relevant federal counsel before processing sensitive personal data or deploying systems in regulated or consequential domains. Review this policy at least quarterly and whenever law, GitHub terms, or system behavior changes.


## 11. Primary references checked for this draft

These links are starting points, not a complete legal inventory. Re-check the current text and rules before each release or deployment.

- [GitHub Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service) — includes account, content, acceptable-use, API, and product terms.
- [GitHub Acceptable Use Policies](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies) — lawfulness, safety, IP, authenticity, spam, information use, privacy, and service limits.
- [Colorado Attorney General — Colorado Privacy Act](https://coag.gov/resources/colorado-privacy-act/) — consumer rights, transparency, minimization, safeguards, assessments, sensitive-data consent, and universal opt-out mechanism.
- [Colorado Attorney General — Consumer Data Protection Laws FAQ](https://coag.gov/resources/data-protection-laws/) — Colorado PII disposal, reasonable security, processor safeguards, and breach response. The AG's current guidance describes resident notice within 30 days after determination and AG notice within 30 days where 500 or more Colorado residents are affected, subject to statutory conditions and exceptions.
- [Colorado General Assembly — SB26-189, Automated Decision-Making Technology](https://leg.colorado.gov/bills/sb26-189) — signed May 14, 2026. The enacted summary describes covered consequential domains, developer documentation beginning January 1, 2027, a three-year compliance-record retention requirement, consumer notice, correction rights, and meaningful human review/reconsideration after adverse outcomes.

**Colorado ADMT caution:** SB26-189 applies to covered automated decision-making technology used in consequential decisions concerning education, employment, housing, financial/lending services, insurance, health care, and essential government services/public benefits. Tushka must not assume every model or task is covered—or exempt—without analyzing the actual deployment. Obtain legal review of the enacted text, implementing rules, and effective-date provisions before enabling such a use.
