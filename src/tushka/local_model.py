"""Local model adapter using the Ollama-compatible chat HTTP API.

The adapter is deliberately outside core.py: the coordinator remains provider-neutral.
It performs no automatic model installation, discovery, or remote execution.
"""

from __future__ import annotations

import asyncio
import json
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

from .core import AgentResult, Task


class LocalModelAgent:
    """An Agent backed by an explicitly configured local chat endpoint.

    The default endpoint is loopback. A non-loopback endpoint must be supplied
    explicitly by the operator. The endpoint receives task prompts as data.
    """

    def __init__(
        self,
        name: str,
        model: str,
        base_url: str = "http://127.0.0.1:11434",
        request_timeout_seconds: float = 120.0,
    ) -> None:
        if not name.strip():
            raise ValueError("Agent name must not be empty.")
        if not model.strip():
            raise ValueError("Model name must not be empty.")
        if request_timeout_seconds <= 0:
            raise ValueError("request_timeout_seconds must be greater than zero.")

        parsed = urlsplit(base_url)
        if parsed.scheme not in {"http", "https"} or not parsed.hostname:
            raise ValueError("base_url must be an absolute HTTP or HTTPS URL.")
        if parsed.username or parsed.password or parsed.query or parsed.fragment:
            raise ValueError("base_url must not contain credentials, query, or fragment.")

        self.name = name
        self.model = model
        self.base_url = base_url.rstrip("/")
        self.request_timeout_seconds = request_timeout_seconds

    async def run(self, task: Task) -> AgentResult:
        """Send a non-streaming chat request without blocking the event loop."""
        content = await asyncio.to_thread(self._request, task.prompt)
        return AgentResult(agent_name=self.name, content=content)

    def _request(self, prompt: str) -> str:
        payload = json.dumps(
            {
                "model": self.model,
                "messages": [{"role": "user", "content": prompt}],
                "stream": False,
            }
        ).encode("utf-8")
        request = Request(
            f"{self.base_url}/api/chat",
            data=payload,
            headers={"Content-Type": "application/json", "Accept": "application/json"},
            method="POST",
        )

        try:
            with urlopen(request, timeout=self.request_timeout_seconds) as response:
                raw = response.read(4 * 1024 * 1024 + 1)
        except HTTPError as exc:
            raise RuntimeError(f"Local model endpoint returned HTTP {exc.code}.") from None
        except URLError as exc:
            reason_type = type(exc.reason).__name__
            raise RuntimeError(
                f"Could not reach the configured local model endpoint ({reason_type})."
            ) from None
        except TimeoutError:
            raise RuntimeError("Local model request timed out.") from None

        if len(raw) > 4 * 1024 * 1024:
            raise RuntimeError("Local model response exceeded the 4 MiB limit.")

        try:
            response_data = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            raise RuntimeError("Local model endpoint returned invalid JSON.") from None

        if not isinstance(response_data, dict):
            raise RuntimeError("Local model endpoint returned an unexpected response.")
        message = response_data.get("message")
        content = message.get("content") if isinstance(message, dict) else None
        if not isinstance(content, str) or not content.strip():
            raise RuntimeError("Local model endpoint returned no usable message content.")
        return content.strip()
