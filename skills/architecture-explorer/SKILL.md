---
name: architecture-explorer
description: >
  Use when the user wants to visualize or explore the architecture of a codebase.
  Triggers on "visualize architecture", "codebase map", "show node connections", 
  "architecture graph", or "Google Maps for code".
  Supports multi-level depth exploration (Server, Service, Node).
profile: shared
category: exploration
skills: []
metadata:
  version: 2.4.0
  requires: python 3.8+
---

# Architecture Explorer

> Portable, multi-level codebase visualization for any `.agent` project.

## When to Use

- Navigating complex codebases for the first time.
- Identifying circular dependencies or complex node relationships.
- Generating a visual system map for documentation or onboarding.
- Visualizing LangGraph or other state-machine based flows.

## Before Starting

1. Identify the project root directory (where `.agent/` lives).
2. Ensure Python 3.8+ is available in the environment.

## Core Framework

The explorer uses a 3-layer scanning logic:

| Level | Scope | Detection Logic |
| :--- | :--- | :--- |
| **Server** | Root directories / Apps | Top-level folders with `main.py` or `package.json` |
| **Service** | Major modules / Packages | Folders within a server (e.g., `/services`, `/graph`, `/api`) |
| **Node** | Component / File / Function | Individual `.py`, `.js`, `.ts` files or core functions |

## Outputs

The scanner produces **three** outputs:

| Output | Format | Purpose |
| :--- | :--- | :--- |
| `architecture.drawio` | Draw.io XML | Editable diagram, openable in VS Code or draw.io |
| `relationships.json` | JSON | Raw data for programmatic use |
| `map.md` | Mermaid Markdown | Inline-viewable diagram with launch link |

## Usage

### Slash Command

Run `/visualize-arch` to scan the current project and generate all outputs.

### Manual Execution

From the project root:

```bash
python3 .agent/skills/architecture-explorer/scripts/scanner.py . \
  --drawio .agent/skills/architecture-explorer/assets/architecture.drawio \
  --depth 2
```

## Installation

This skill is **already installed** if your project cloned or symlinked `vibmedia-agent-skills` as its `.agent` directory.

If your project uses a standalone `.agent` setup, install with:

```bash
# From your project root
SRC="path/to/vibmedia-agent-skills"
cp -r "$SRC/skills/architecture-explorer" .agent/skills/
cp "$SRC/workflows/visualize-arch.md" .agent/workflows/
```

> **That's it.** All paths inside the scanner and workflow are resolved dynamically at runtime using `$(pwd)/.agent`. No configuration needed.

## Related Skills

- **architecture**: Use for high-level architectural decision records (ADR).
- **clean-code**: Use for refactoring based on the visual findings.
- **app-builder**: Use for generating new structures mapped in the explorer.
