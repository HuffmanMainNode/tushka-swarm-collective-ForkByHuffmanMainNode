"""Tushka: a small, model-independent agent coordination core."""

from .core import Agent, AgentResult, Coordinator, Task
from .local_model import LocalModelAgent

__all__ = ["Agent", "AgentResult", "Coordinator", "LocalModelAgent", "Task"]
