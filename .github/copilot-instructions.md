# Project Guidelines

## Code Style
- Follow the style rules in `docs/find_factors.md` for naming, docstrings, and test guard conventions.
- Prefer type hints for Python functions and Pydantic models for request/input validation.
- Keep async network code explicit about timeouts and user-facing errors (see `mcp/ollama_mcp.py`).

## Architecture
- Main production code is the MCP server in `mcp/ollama_mcp.py`.
- `src/` is reserved for project modules and is added to `PYTHONPATH` by `activate.sh`.
- External runtime dependency: a local Ollama server at `http://localhost:11434`.

## Build and Test
- Environment setup: `source activate.sh`.
- Install/update dependencies: `pip install -r requirements.txt`.
- Run MCP server: `python mcp/ollama_mcp.py`.
- Testing tools are installed (`pytest`, `nose2`), but no test suite is currently checked in.

## Conventions
- When adding MCP tools, use structured input models and clear error paths.
- Reuse shared clients/resources via server lifespan rather than creating per-request clients.
- For detailed feature requirements and style expectations, link to existing docs instead of restating them: `docs/find_factors.md`.
