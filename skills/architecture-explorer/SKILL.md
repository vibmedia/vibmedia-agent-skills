---
name: architecture-explorer
description: Use when the user wants to visualize or explore the codebase structure, identify dependencies, map system patterns, or generate visual documentation of how components connect.
profile: shared
category: exploration
---

# Architecture Explorer

## Overview
Generates layered architecture diagrams, connection maps, and hierarchy data for any `.agent` project. It provides visual clarity on complex codebases, dependencies, and state-machine flows by parsing code and generating structured graph outputs (Draw.io, Mermaid, JSON).

## When to Use

- When navigating a complex or unfamiliar codebase for the first time
- When identifying circular dependencies, tight coupling, or complex node relationships 
- When generating visual system maps for documentation or onboarding
- When visualizing LangGraph or other state-machine based flows
- When preparing an architectural decision record (ADR)
- **Do not use** for standard text-based file searches (use standard search tools).

## Core Pattern

Run the `scanner.py` script to generate a three-layered structural mapping (Server, Service, Node) and output visual artifacts. 

The explorer categorizes files logically rather than just mirroring the filesystem:
- **Server:** Root directories / Apps containing entry points (`main.py`, `package.json`)
- **Service:** Major modules / Packages within a server (e.g., `/services`, `/graph`, `/api`)
- **Node:** Individual components, files, or core functions (`.py`, `.js`, `.ts`)

## Quick Reference

| Action | Path/Command | Description |
|---|---|---|
| **Run Scanner (via command)** | `/visualize-arch` | Runs the full scanner and generates all required outputs inside `.agent/skills/architecture-explorer/assets/`. |
| **Run Scanner (manual bash)** | `python3 [scanner_path] [target_path] --drawio [out] --mermaid [out]` | Directly invoke the scanner script for precise output targeting. |
| **View Editable Topology** | `assets/architecture.drawio` | Layered XML tree diagram with clickable node links, openable in VS Code. |
| **View Inline Map** | `assets/map.md` | Mermaid graph designed for quick Markdown previewing. |

## Implementation

Always ensure the target project is using the `.agent` directory structure. 

To execute manually via the terminal, run the following script:

```bash
AGENT_DIR="$(pwd)/.agent"
python3 "$AGENT_DIR/skills/architecture-explorer/scripts/scanner.py" . \
  --output "$AGENT_DIR/skills/architecture-explorer/assets/relationships.json" \
  --mermaid "$AGENT_DIR/skills/architecture-explorer/assets/map.md" \
  --drawio "$AGENT_DIR/skills/architecture-explorer/assets/architecture.drawio" \
  --depth 2
```

## Common Mistakes

| Mistake | Fix |
|---|---|
| Running parser on the `.agent` folder itself | The scanner logic ignores the `.agent` and other cache directories by default to prevent visual noise. Point the parser at the root `.` directory instead. |
| Expecting every function to be mapped | The scanner maps up to the file (Node) level by default. It parses Python docstrings for descriptions, but does not explode every single function into a separate block unless explicitly configured. |
| Opening raw XML | The `architecture.drawio` file is XML. Use the Draw.io extension for VS Code or upload it to app.diagrams.net to interact with the visualization cleanly. |
