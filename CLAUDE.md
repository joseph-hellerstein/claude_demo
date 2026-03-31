# CLAUDE.md

This file provides guidance for Claude Code when working in this repository.

## Project Overview

**claude_demo** demonstrates Claude Code capabilities.

## Architecture

- `src/` — project modules; added to `PYTHONPATH` by `activate.sh`
- `docs/` — feature specs and style guides
- External runtime dependency: local Ollama server at `http://localhost:11434`

## Environment Setup

```bash
source activate.sh          # activate venv and set PYTHONPATH
pip install -r requirements.txt
```

## Running & Testing

1. Test files are in tests/. They have the filename test_<file>, where<file> is the file being tested.
2. Use the unittest package.

## Code Style

- Follow naming, docstring, and test conventions in [docs/find_factors.md](docs/find_factors.md)
- Use type hints on all Python functions
- Use Pydantic models (with `extra="forbid"`) for MCP tool input validation
- Function names are camelCase; variable names are `snake_case`; only lists end in `s`, arrays end in `_arr`
