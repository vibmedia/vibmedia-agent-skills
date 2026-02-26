---
description: Analyze todo.md goals against current system state. Finds gaps, missing skills, and blockers preventing achievement of planned objectives.
---

# /audit-goals — Gap Analysis Workflow

> Find what's missing, what's blocking progress, and what loopholes exist between where you are and where you want to be.

---

## When to Run

- Weekly review of project progress
- After completing a sprint or milestone
- When a brand's todo.md feels stalled
- When planning the next phase of work
- Before client status meetings

---

## Steps

### Step 1: Identify the Target

Ask: **Which brand are we auditing?** or **Is this a system-level audit?**

- **Brand-level:** Read `brands/[industry]/[brand]/todo.md` and `context.md`
- **System-level:** Read `ARCHITECTURE.md` and `ROADMAP.md`

### Step 2: Extract Goals

From `todo.md`, extract:

1. **Planned items** — tasks with `[ ]` checkboxes
2. **In-progress items** — tasks with `[/]`
3. **Completed items** — tasks with `[x]`
4. **Stalled items** — in-progress for too long (check decision log dates)

From `context.md`, extract:

1. **Key metrics** — current vs target
2. **Stated objectives** — what the brand is trying to achieve

### Step 3: Gap Analysis

For each planned/in-progress goal, answer:

| Question | Finding |
|----------|---------|
| **Do we have the skills for this?** | List required skills and check if they exist in `skills/` |
| **Do we have the agent for this?** | Which agent owns this goal? Does it exist? |
| **Do we have the workflow for this?** | Is there a repeatable process, or manual every time? |
| **Do we have the data for this?** | Does `_common/` and `context.md` have enough context? |
| **What's blocking this?** | Dependencies, missing info, unclear requirements? |

### Step 4: Skill Gap Check

```bash
# List all available skills
find skills -maxdepth 2 -name 'SKILL.md' -type f -exec grep -l 'name:' {} \; | \
  xargs grep '^name:' | sed 's/.*name: //' | sort
```

Compare against goals:
- Goal requires copywriting → Do we have `copywriting` skill? ✅
- Goal requires video marketing → Do we have a video skill? ❌ **GAP**

### Step 5: Resource Assessment

For each gap found:

| Gap Type | Resolution |
|----------|-----------|
| **Missing skill** | Create new skill or find external source |
| **Missing agent** | Create new agent with correct skill bindings |
| **Missing workflow** | Create workflow to make the process repeatable |
| **Missing data** | Fill `_common/` or `context.md` with required info |
| **Missing integration** | Identify tool/API needed and plan implementation |
| **Unclear requirement** | Flag for client/stakeholder clarification |

### Step 6: Priority Matrix

Rank all gaps by impact and effort:

```
            HIGH IMPACT
                │
    Quick Wins  │  Major Projects
   (Do First)   │  (Plan Carefully)
────────────────┼────────────────
    Fill Later  │  Reconsider
   (Low Priority)│  (Maybe Not Needed)
                │
            LOW IMPACT
```

### Step 7: Update Todo

Based on findings, update `todo.md`:

1. **Add new tasks** for identified gaps
2. **Re-prioritize** existing tasks based on gap analysis
3. **Add blockers** to in-progress items that need unblocking
4. **Log decisions** in the decisions table
5. **Move stalled items** to planned with clear next steps

### Step 8: Report

Produce a summary:

```
🎯 Goal Audit Report — [Brand/System]
──────────────────────────────────────
Progress: [X] completed / [Y] in-progress / [Z] planned

Gaps Found:
1. [Gap] → [Resolution] → [Priority]
2. [Gap] → [Resolution] → [Priority]
3. [Gap] → [Resolution] → [Priority]

Stalled Items:
- [Item] — Blocked by: [Reason] — Next step: [Action]

Recommendations:
1. [Quick win to tackle first]
2. [Major project to plan]
3. [Data to gather before next session]
```
