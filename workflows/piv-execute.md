---
description: Execute an implementation plan step-by-step
argument-hint: [plan-file.md] [step-number]
---

# /piv-execute: Plan Execution Workflow

## Task
Execute a specific step from an implementation plan. 

**IMPORTANT CONTEXT LOADING RULES:**
Before executing ANY step, you MUST first read the foundational project documents if they exist:
1. Check for `PRD.md` - Product Requirements Document
2. Check for `ARCHITECTURE.md` - System Architecture and structure
3. Check for `ONBOARDING.md` - Any environment context

Read these files along with the specified `plan-file.md`.

## Arguments
- `plan-file.md`: The markdown file containing the implementation plan
- `step-number`: The specific step/task to execute from the plan

## Instructions

1. Search for the specified standard docs (`PRD.md`, `ARCHITECTURE.md`) in the workspace. Read them if they are present.
2. Read the full `{plan-file.md}` to understand the high-level context
3. Locate task `{step-number}` within the plan
4. Understand the specific goal, dependencies, and verification steps for this task
5. Write the necessary code to implement this task
6. Run validation checks for this specific code (e.g., tests, linting)
7. Report completion and explicitly instruct the user how to mark the task as done or if they should proceed to the next step

