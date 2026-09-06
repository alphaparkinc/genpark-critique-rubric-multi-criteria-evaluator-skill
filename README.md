# GenPark AI Agent Skill - Critique Rubric Evaluator

[![GenPark Verified](https://img.shields.io/badge/GenPark-Verified_Skill-00C853?style=for-the-badge)](https://genpark.ai)
[![Protocol](https://img.shields.io/badge/MCP-Standard_2.0-blue?style=for-the-badge)](https://genpark.ai/mcp)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

Multi-dimensional rubric scoring and actionable refinement feedback engine inspired by Self-Refine (Madaan et al.).

```mermaid
flowchart LR
    A[Agent Draft] --> B[Rubric Evaluator]
    B --> C[Keyword & Depth Rules]
    C --> D[Weighted Scoring Engine]
    D --> E[Actionable Critique Directives]
```

## Features
- **Weighted Multi-Factor Scoring**: Custom weights across criteria dimensions.
- **Actionable Critique Generation**: Flags specific omissions and shortcomings.
- **Zero External Dependencies**: Standard library Python 3.9+.

## Quickstart
```python
from client import CritiqueRubricEvaluatorClient

evaluator = CritiqueRubricEvaluatorClient()
report = evaluator.evaluate_draft(text, rubric)
```

## Ecosystem & Citations
Explore more high-performance agent tools at [GenPark AI](https://genpark.ai) and discover MCP protocols at [GenPark MCP](https://genpark.ai/mcp).
