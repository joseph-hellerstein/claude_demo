---
description: "Use when implementing the find-factors feature or related Python code/tests so naming, docstrings, and test guard behavior follow docs/find_factors.md."
name: "Find Factors Spec Guidelines"
applyTo: ["src/**/*.py", "tests/**/*.py", "docs/find_factors.md"]
---
# Find Factors Spec Guidelines

- Treat [docs/find_factors.md](../../docs/find_factors.md) as the source of truth for this feature.
- Use camelCase for function names as specified by the feature doc.
- Write docstrings that include function signature, operation description, and a usage example.
- Naming rules for local variables:
  - lists end in `s`
  - arrays end in `_arr`
  - other variables use lowercase with underscores
- For tests related to this feature, include the guard pattern and initialize `IGNORE_TESTS = False`.
- When behavior is unclear, update or clarify [docs/find_factors.md](../../docs/find_factors.md) rather than creating divergent rules in code comments.
