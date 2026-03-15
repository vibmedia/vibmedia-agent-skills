# Telos Context File — VibMedia Agent Skills Framework

> Deep context for the framework itself. Tracks mission, goals, evolution, and streaming activity log.

---

## Document Purpose

This is the master Telos file for the **VibMedia Agent Skills** framework. It tracks:

- Framework mission and goals
- Current capabilities and coverage
- Active development priorities
- Streaming activity log for all changes

---

## Entity Overview

- **Name:** VibMedia Agent Skills (Antigravity Kit)
- **Type:** AI Agent Capability Expansion Toolkit
- **Profile:** hybrid (builds product + serves marketing)
- **Maintainer:** VibMedia
- **License:** MIT

---

## Mission

Provide a modular, extensible AI agent toolkit where every component (agent, skill, workflow) is discoverable, documented, and reachable — enabling a single operator to do the work of multiple specialists.

---

## Goals

- G1: Achieve 100% workflow coverage — every agent/skill reachable via workflows
- G2: Maintain clear documentation — any new user can be productive in < 30 minutes
- G3: Scale to 100+ skills covering all dev/marketing/ops domains
- G4: Implement Phase 1 of Roadmap — add 6 high-priority agents
- G5: Build infrastructure layer (task router, persistent memory)

---

## KPIs

| ID  | Metric                        | Target       | Current | Status |
| --- | ----------------------------- | ------------ | ------- | ------ |
| K1  | Total Agents                  | 34 (Roadmap) | 21      | 🟡     |
| K2  | Total Skills                  | 100+         | 85      | 🟡     |
| K3  | Total Workflows               | 30+          | 26      | 🟡     |
| K4  | Workflow Coverage             | 100%         | 100%    | 🟢     |
| K5  | Doc Quality (self-assessment) | Complete     | Good    | 🟡     |

---

## Strategies

- S1: Use workflow-coverage-rule to prevent dead components
- S2: Use Telos for all project tracking (framework + brands)
- S3: Add agents in priority order per ROADMAP.md
- S4: Community contributions via GitHub Issues/PRs

---

## Risk Register

| Risk                                | Impact | Likelihood | Mitigation                                  |
| ----------------------------------- | ------ | ---------- | ------------------------------------------- |
| Skill bloat (too many, low quality) | High   | Medium     | Quality checklist in BUILDING-SKILLS.md     |
| Agent overlap (confusing routing)   | Medium | Medium     | Strict boundary enforcement in orchestrator |
| Documentation drift                 | High   | High       | /system-check monthly + /update on changes  |

---

## Current State — Activity Log

> Newest entries first. These override any conflicting information above.

- 2026-03-15: Formalized "Vibhor Rule" (Markdown Truth) in `ARCHITECTURE.md` and `CONTENT-BOUNDARY.md`. Added `wordpress_checklist.py` and updated infrastructure to use `python3`.
- 2026-03-04: Integrated GitHub MCP using provided PAT and created `github-mcp` skill.
- 2026-03-04: Built the 6 missing enterprise skills (`data-analysis`, `prompt-engineering`, `cloud-infrastructure`, `web3-smart-contracts`, `design-system-architecture`, `ml-engineer`).
- 2026-03-04: Documented missing skill domains for future development and removed temporary local `.agent/GEMINI.md` junction to fix IDE rule duplication.
- 2026-03-04: Integrated NotebookLM as a stable RAG source using `notebooklm-mcp-cli`
- 2026-03-04: Created `notebooklm-rag` skill to teach agents how to use the RAG tools
- 2026-03-04: Updated `INSTALL.md` with instructions for SSH, New, and Ongoing project deployments
- 2026-03-04: Created framework-level telos.md- 2026-02-26: ROADMAP.md created — 4-phase enterprise AI workforce plan
- 2026-02-26: Initial framework release — 77 skills, 21 agents, 25 workflows

---

_Update this file after every significant framework change. Run `/update` to sync._
