
<h1 align="center">🤖 AI Agent Starter</h1>
<h3 align="center">A clean, production-minded starter for autonomous AI agents — LangGraph + tool calling + MCP-ready</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/LangGraph-FF6F61?style=for-the-badge&logo=chainlink&logoColor=white">
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white">
  <img src="https://img.shields.io/badge/MCP-000000?style=for-the-badge&logo=modelcontextprotocol&logoColor=white">
</p>

---

A minimal but **production-minded** template for building autonomous AI agents that actually *do* things — plan, call tools, and complete multi-step tasks — instead of just chatting. Built the way I ship them for clients: clear structure, typed tools, guardrails, and easy to extend with MCP servers.

## ✨ What it does

- 🧠 **Reasoning loop** — the agent plans, picks tools, acts, and reflects (ReAct-style) via LangGraph
- 🔧 **Typed tools** — add a function, decorate it, and the agent can use it (calculator + web-search examples included)
- 🛡️ **Guardrails** — step limits and safe-completion so the agent can't loop forever
- 🔌 **MCP-ready** — structured so external tools/data can be added via the Model Context Protocol
- 📦 **Zero-magic** — readable, commented code you can actually maintain

## 🚀 Quickstart

```bash
git clone https://github.com/haideraliafzal/ai-agent-starter.git
cd ai-agent-starter
pip install -r requirements.txt
cp .env.example .env        # add your OPENAI_API_KEY
python agent.py "What's 18% of 2,450, and what is LangGraph in one line?"
```

## 🧩 Add your own tool

```python
@tool
def get_weather(city: str) -> str:
    """Return the current weather for a city."""
    return weather_api.lookup(city)
```
Register it in `TOOLS` and the agent can use it automatically.

## 🗺️ Where this goes next

This starter is the foundation for the agent systems I build in production: multi-agent orchestration, memory, human-in-the-loop approval, monitoring, and MCP integrations across a client's full stack.

---

<p align="center"><i>Built by <a href="https://www.haideraliafzal.com">Haider Ali Afzal</a> — AI Integration & Full-Stack Engineer · Lead Architect of <a href="https://studio98.ai">Studio98AI</a></i></p>
