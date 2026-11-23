# Security policy

Tushka is an early prototype and is not yet suitable for untrusted public network deployment.

## Reporting a vulnerability

Please do not publish exploitable details in a public issue. Use GitHub's private vulnerability reporting feature if it is enabled for this repository, or contact the repository owner through a private channel.

Include:
- affected component and version/commit;
- impact and realistic attack conditions;
- reproduction steps or a proof of concept that does not expose real secrets or data;
- suggested mitigation, if known.

## Current security limitations

- The initial coordinator executes agents in-process.
- There is no remote node authentication or authorization yet.
- There is no sandbox for model-generated code or tool execution.
- The demo agents are not a security boundary.
- Do not provide the prototype with secrets or sensitive data.

Security controls for remote execution must be designed and reviewed before federation is enabled.
