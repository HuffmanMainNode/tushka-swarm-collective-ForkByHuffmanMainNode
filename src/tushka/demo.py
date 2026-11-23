"""Run the first two-agent Tushka demonstration."""

import asyncio

from .core import AgentResult, Coordinator, Task


class DemoAgent:
    """A deterministic stand-in for a future model-backed agent."""

    def __init__(self, name: str, perspective: str):
        self.name = name
        self.perspective = perspective

    async def run(self, task: Task) -> AgentResult:
        return AgentResult(
            agent_name=self.name,
            content=f"{self.perspective}\nTask received: {task.prompt}",
        )


async def demo() -> None:
    agents = [
        DemoAgent("planner", "I will break the task into clear steps."),
        DemoAgent("reviewer", "I will check assumptions, risks, and missing evidence."),
    ]
    coordinator = Coordinator(agents)
    task = Task(
        task_id="first-swarm-task",
        prompt="Describe how two agents can collaborate on a small project.",
    )
    results = await coordinator.run(task)
    print(Coordinator.synthesize(results))


def main() -> None:
    asyncio.run(demo())


if __name__ == "__main__":
    main()
