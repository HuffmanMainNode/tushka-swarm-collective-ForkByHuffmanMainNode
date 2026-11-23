# Local model adapter

The first model-backed adapter implements the existing Agent interface and
uses the non-streaming Ollama-compatible POST /api/chat endpoint. It uses
Python's standard library and adds no runtime dependency to the project.

## Requirements

- Python 3.11+
- A locally operated inference service exposing the Ollama chat API
- A model already available to that service

The adapter does not install models, start a model server, discover endpoints,
or require an account or hosted API.

## Example

    import asyncio

    from tushka.core import Coordinator, Task
    from tushka.local_model import LocalModelAgent

    async def main():
        agents = [
            LocalModelAgent("local-planner", "qwen2.5:7b"),
            LocalModelAgent("local-reviewer", "llama3.2:3b"),
        ]
        coordinator = Coordinator(agents, timeout_seconds=180)
        results = await coordinator.run(
            Task("example-001", "Identify the risks in a small local-first project.")
        )
        print(Coordinator.synthesize(results))

    if __name__ == "__main__":
        asyncio.run(main())

## Endpoint URL

The default endpoint is http://127.0.0.1:11434. The base_url argument accepts
either the service root or a URL path prefix. The adapter appends /api/chat to
the configured URL after removing trailing slashes:

- http://127.0.0.1:11434 becomes
  http://127.0.0.1:11434/api/chat.
- http://127.0.0.1:11434/ollama/v1/ becomes
  http://127.0.0.1:11434/ollama/v1/api/chat.

The configured path prefix is preserved. The adapter does not detect or
rewrite an existing /api/chat suffix, so configure the service root or
prefix rather than the final chat endpoint URL.

Non-loopback endpoints must use HTTPS. Operators must understand and trust
the configured destination because task prompts are sent to that endpoint.

## Behavior and limits

- Requests are non-streaming JSON chat requests.
- Blocking HTTP work runs in a worker thread so the asyncio event loop remains responsive.
- Task prompts are limited to 1 MiB and responses to 4 MiB.
- HTTP failures, unreachable endpoints, malformed JSON, and empty responses
  become explicit agent failures when invoked through the coordinator.
- The adapter does not validate model claims, provide independent verification,
  sandbox the model server, or authenticate an arbitrary remote endpoint.
- The coordinator's timeout and the adapter's request timeout are separate.
  Configure the adapter timeout no higher than the coordinator timeout if the
  coordinator should enforce the full request deadline.
- Cancellation of the asyncio task does not forcibly terminate an HTTP request
  already running in its worker thread; the adapter request timeout bounds that
  underlying operation.

This is a first local integration boundary, not a production security review
or a claim of model quality. See the project security policy before exposing
an inference endpoint to a network.
