---
description: "Create a new MCP tool in mcp/ollama_mcp.py with validated inputs, clear annotations, and robust error handling."
name: "Add MCP Tool"
argument-hint: "Describe the new tool's purpose, inputs, and output schema"
agent: "agent"
---
Add one new MCP tool based on this request: $ARGUMENTS

Requirements:
- Modify [mcp/ollama_mcp.py](../../mcp/ollama_mcp.py).
- Reuse existing patterns for Pydantic input models, annotations, and async error handling.
- Reuse lifespan-managed HTTP/client resources where applicable.
- If new behavior requires extra documentation, add a concise update in [README.md](../../README.md) instead of duplicating docs elsewhere.
- Keep changes minimal and consistent with project conventions in [.github/copilot-instructions.md](../copilot-instructions.md).

Deliverables:
- The exact code changes.
- A short summary of behavior and edge cases.
- Any follow-up command(s) needed to run or validate the update.
