---
name: workflow-coverage-rule
description: Enforces that every agent and skill is reachable through at least one workflow. Prevents dead or forgotten components.
enforcement: strict
---

# Workflow Coverage Rule

> **STRICT ENFORCEMENT**: The AI MUST block and report if orphaned agents or skills are detected.

---

## Purpose

Every agent and every skill in this framework MUST be reachable through at least one workflow chain:

```
Workflow → invokes Agent → loads Skill
```

This guarantees: **learn the workflows → access the entire system**. No dead components.

---

## The Rule

### R1: Every Agent Must Be Workflow-Reachable

Every `.md` file in `agents/` must appear as a usable agent in at least one workflow defined in `workflows/`.

**Check**: An agent is "covered" if:

- It is explicitly named in a workflow's steps, OR
- It is invokable through the `orchestrator` via `/orchestrate`, OR
- It is auto-selected via `intelligent-routing` for a workflow-triggerable task category

### R2: Every Skill Must Be Agent-Reachable

Every directory in `skills/` must be listed in the `skills:` frontmatter of at least one agent.

**Check**: A skill is "covered" if:

- It appears in at least one agent's `skills:` list, OR
- It is a `profile: shared` universal skill (clean-code, intelligent-routing, etc.)

### R3: Coverage Chain Integrity

The full chain must be valid:

```
Workflow → Agent → Skill
   ↓         ↓        ↓
  exists   exists   exists
```

Broken links at any point = violation.

---

## Enforcement

### When to Check

- On every `/update` run
- On every `/system-check` run
- Before any `/deploy`

### What Happens on Violation

```
🔴 WORKFLOW COVERAGE VIOLATION

Orphaned Agents (not reachable via any workflow):
  ❌ agent-name — Add to a workflow or remove

Orphaned Skills (not loaded by any agent):
  ❌ skill-name — Add to an agent's skills: list or remove

ACTION REQUIRED: Fix violations before proceeding.
The system cannot have dead components.
```

### Auto-Resolution Suggestions

When an orphan is detected, the AI should suggest:

| Type           | Suggestion                                                  |
| -------------- | ----------------------------------------------------------- |
| Orphaned Agent | "Add `agent-name` to `/orchestrate` agent matrix"           |
| Orphaned Skill | "Add `skill-name` to `agent-name`'s skills: frontmatter"    |
| Dead Workflow  | "This workflow invokes no agents — connect it or remove it" |

---

## Reference

See [docs/workflow-coverage-map.md](../docs/workflow-coverage-map.md) for the full mapping of:

- Which workflows invoke which agents
- Which agents load which skills
- Coverage percentage per category

---

## Maintenance

After adding a new agent, skill, or workflow:

1. Run `/update` — it will check coverage
2. If violation detected → fix immediately
3. Update `docs/workflow-coverage-map.md` if needed
