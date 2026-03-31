---
description: "Use when adding or editing MCP tools in mcp Python files, including tool signatures, Pydantic input models, async HTTP calls, and user-facing error handling."
name: "MCP Python Tool Guidelines"
applyTo: "mcp/**/*.py"
---
# MCP Python Tool Guidelines

- Prefer one Pydantic input model per tool for non-trivial input instead of raw dicts.
- Keep model validation strict (`extra=\"forbid\"`) and define clear field constraints.
- Reuse shared resources via FastMCP lifespan state for clients and connections.
- Keep async network calls explicit about timeout behavior and failure modes.
- Return clear user-facing errors for connection failures, timeouts, and HTTP status errors.
- Add/maintain MCP annotations (`readOnlyHint`, `idempotentHint`, `destructiveHint`, `openWorldHint`) to match tool behavior.
- Use type hints consistently for function arguments and return values.
- Follow project-wide guidance in [.github/copilot-instructions.md](../copilot-instructions.md) and link detailed feature rules from [docs/find_factors.md](../../docs/find_factors.md) instead of duplicating them.
