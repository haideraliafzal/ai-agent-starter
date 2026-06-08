
"""
AI Agent Starter — an autonomous agent that plans, calls tools, and answers.
Built with LangGraph's ReAct loop. Add a @tool function and the agent can use it.

Usage:
    python agent.py "your question or task here"
"""
import os
import sys

from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

load_dotenv()

# ---------------------------------------------------------------------------
# Tools — add your own here. Each becomes available to the agent automatically.
# ---------------------------------------------------------------------------

@tool
def calculator(expression: str) -> str:
    """Evaluate a basic arithmetic expression, e.g. '18/100 * 2450'."""
    allowed = set("0123456789+-*/(). %")
    if not set(expression) <= allowed:
        return "Error: only basic arithmetic is allowed."
    try:
        return str(eval(expression.replace("%", "/100")))  # noqa: S307 (sandboxed by allow-list)
    except Exception as exc:  # noqa: BLE001
        return f"Error: {exc}"


@tool
def knowledge(topic: str) -> str:
    """Return a one-line definition for a small set of known topics."""
    facts = {
        "langgraph": "LangGraph is a framework for building stateful, multi-step AI agents as graphs.",
        "mcp": "MCP (Model Context Protocol) is an open standard for connecting AI agents to tools and data.",
        "rag": "RAG (Retrieval-Augmented Generation) grounds an LLM's answers in your own data.",
    }
    return facts.get(topic.lower().strip(), "No entry found. (Wire this tool to a real source.)")


TOOLS = [calculator, knowledge]

# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = (
    "You are a capable, concise assistant. Use the available tools when they help, "
    "show your reasoning briefly, and give a clear final answer. "
    "Never loop unnecessarily — finish as soon as you can answer."
)


def build_agent(model: str = "gpt-4o-mini"):
    llm = ChatOpenAI(model=model, temperature=0)
    # recursion_limit acts as a simple guardrail against runaway loops.
    return create_react_agent(llm, TOOLS, state_modifier=SYSTEM_PROMPT)


def run(task: str) -> str:
    if not os.getenv("OPENAI_API_KEY"):
        return "Set OPENAI_API_KEY in your .env file first."
    agent = build_agent()
    result = agent.invoke(
        {"messages": [("user", task)]},
        config={"recursion_limit": 12},
    )
    return result["messages"][-1].content


if __name__ == "__main__":
    task = " ".join(sys.argv[1:]) or "What is 18% of 2,450, and what is MCP in one line?"
    print("\n🤖", run(task), "\n")
