# Contributing to Tushka

Tushka is built in the open by people with different skills, experience, hardware, and time. You do not need to be an expert, a professional developer, or an AI researcher to make a useful contribution.

## Start at your level

- **Just curious?** Read the README, run the demo if you can, ask a question, or tell us what is unclear.
- **Learning to code?** Reproduce a bug, improve an example, add a small test, or document a setup step.
- **Not a programmer?** Help with writing, diagrams, accessibility, translation, usability testing, research summaries, and issue triage.
- **Experienced builder?** Work on orchestration, model adapters, evaluation, storage, interfaces, deployment, and security.
- **Researcher or subject expert?** Contribute reproducible evaluations, carefully sourced knowledge, threat analysis, or domain-specific test cases.
- **Operating a node?** Share deployment results, resource measurements, reliability findings, and interoperability feedback.

Small contributions count. Explain what you observed and how someone else can reproduce it.

## Good first contributions

- Clarify confusing documentation or add a beginner-friendly example.
- Add a test for an edge case or reproduce an existing failure.
- Improve error messages, logging, or accessibility.
- Propose a typed task/result schema.
- Implement an adapter behind the existing provider-neutral Agent interface.
- Add local-model setup instructions and reproducible evaluation cases.
- Improve provenance, export, privacy, or security documentation.

For substantial proposals and external project discoveries, use the contribution intake and review process. Open a structured contribution proposal to give reviewers the source, evidence, permissions, risks, and suggested next step.

## Contribution workflow

1. Search existing issues and discussions before opening a duplicate.
2. For substantial changes, open an issue describing the problem and proposed approach.
3. Keep changes focused and explain trade-offs, limitations, and risks.
4. Include tests or reproducible evidence for behavior changes.
5. Request review; respond constructively and revise when needed.
6. Keep prototypes clearly labeled. A pull request is not upstream until it is reviewed and merged.

## Shared standards

- Never commit credentials, private user data, or material you do not have rights to contribute.
- Respect each project's license, authorship, attribution, and contribution terms. Public visibility alone is not permission to copy or redistribute.
- Cite sources for factual knowledge contributions and distinguish evidence from opinion or model-generated text.
- Treat model output and external content as untrusted until checked.
- Do not claim security, accuracy, autonomy, or production readiness without evidence.
- Prefer small, reversible changes with tests, review notes, and a rollback path.
- Be welcoming. Critique ideas and code, not the worth or background of contributors.

## Development

- Python 3.11+
- Runtime dependencies: Python standard library only
- Run tests: python -m unittest discover -s tests -v
- Run demo: python -m tushka.demo

## License

The project is licensed under the Apache License 2.0. By submitting a contribution, you agree that it may be distributed under the repository's applicable contribution and licensing terms. If you are unsure whether you have permission to contribute material, ask before submitting it.
