"""Minimal asynchronous coordinator for independent task agents.

This module deliberately knows nothing about a particular model provider.
Adapters implement the Agent protocol and can call local or hosted systems.
"""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import Protocol, Sequence


@dataclass(frozen=True, slots=True)
class Task:
    """A unit of work sent to participating agents."""

    task_id: str
    prompt: str


@dataclass(frozen=True, slots=True)
class AgentResult:
    """An attributable result returned by one agent."""

    agent_name: str
    content: str
    success: bool = True
    error: str | None = None


class Agent(Protocol):
    """Interface implemented by every model, tool, or human-backed agent."""

    name: str

    async def run(self, task: Task) -> AgentResult:
        """Execute a task and return an attributable result."""
        ...


class Coordinator:
    """Dispatch tasks concurrently and combine successful agent responses."""

    def __init__(self, agents: Sequence[Agent], timeout_seconds: float = 60.0):
        if not agents:
            raise ValueError("Coordinator requires at least one agent.")
        if timeout_seconds <= 0:
            raise ValueError("timeout_seconds must be greater than zero.")
        self.agents = tuple(agents)
        self.timeout_seconds = timeout_seconds

    async def run(self, task: Task) -> list[AgentResult]:
        """Run all agents concurrently, isolating individual failures."""
        async def invoke(agent: Agent) -> AgentResult:
            try:
                result = await asyncio.wait_for(
                    agent.run(task), timeout=self.timeout_seconds
                )
                if result.agent_name != agent.name:
                    return AgentResult(
                        agent_name=agent.name,
                        content="",
                        success=False,
                        error="Agent identity mismatch in returned result.",
                    )
                return result
            except asyncio.TimeoutError:
                return AgentResult(
                    agent_name=agent.name,
                    content="",
                    success=False,
                    error=f"Timed out after {self.timeout_seconds:g} seconds.",
                )
            except Exception as exc:  # isolate a failed participant
                return AgentResult(
                    agent_name=agent.name,
                    content="",
                    success=False,
                    error=f"{type(exc).__name__}: {exc}",
                )

        return list(await asyncio.gather(*(invoke(agent) for agent in self.agents)))

    @staticmethod
    def synthesize(results: Sequence[AgentResult]) -> str:
        """Create a transparent first-pass synthesis without hiding attribution."""
        usable = [r for r in results if r.success and r.content.strip()]
        if not usable:
            failures = "; ".join(
                f"{r.agent_name}: {r.error or 'empty response'}" for r in results
            )
            raise RuntimeError(f"No usable agent results. {failures}")

        sections = ["# Combined agent results"]
        for result in usable:
            sections.append(f"## {result.agent_name}\n{result.content.strip()}")

        failed = [r for r in results if not r.success]
        if failed:
            sections.append("## Agent failures")
            sections.extend(
                f"- {r.agent_name}: {r.error or 'unsuccessful'}" for r in failed
            )
        return "\n\n".join(sections)
