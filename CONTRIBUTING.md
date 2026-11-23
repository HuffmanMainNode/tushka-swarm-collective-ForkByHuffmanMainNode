# Contributing to Tushka

Tushka is intended to be built by independent contributors and interoperable projects. You do not need to adopt one model provider, framework, or account structure to participate.

## Good first contributions

- Add tests or improve error handling in the coordinator.
- Propose a typed task/result schema.
- Implement an agent adapter behind the existing interface.
- Add a local-model integration with setup instructions.
- Build evaluation cases that expose failure modes.
- Improve provenance, documentation, accessibility, or reproducibility.

## Contribution expectations

1. Open an issue for substantial changes so the problem and intended scope are visible.
2. Keep pull requests focused and explain the design trade-offs.
3. Include tests for behavior changes.
4. Never commit credentials, private user data, or material you do not have rights to contribute.
5. Preserve original authorship, license notices, and upstream attribution.
6. Identify prototypes and unverified claims clearly.
7. Do not describe a pull request as accepted upstream until it has been merged.

## Development

- Python 3.11+
- Runtime dependencies: Python standard library only
- Run tests: `python -m unittest discover -s tests -v`
- Run demo: `python -m tushka.demo`

## License

A repository license has not yet been selected. Until the owner adds one, do not assume that public visibility grants permission to copy, modify, or redistribute this code.
