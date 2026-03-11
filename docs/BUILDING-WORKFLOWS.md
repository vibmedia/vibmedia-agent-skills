# Building Workflows

> How to create slash-command workflows.

---

## What is a Workflow?

A workflow is a **step-by-step procedure** triggered by a `/command`. It orchestrates agents and skills into a repeatable process.

```
.agent/workflows/
├── deploy.md
├── debug.md
├── your-workflow.md
```

---

## Workflow File Format

```markdown
---
description: Short description of what this workflow does
---

## Steps

1. **Step name**
   - What to do
   - Expected output

2. **Step name**
   - What to do
   - Expected output

3. **Step name**
   - What to do
   - Expected output
```

---

## Step-by-Step Creation

### 1. Define the Trigger

The filename becomes the slash command: `deploy.md` → `/deploy`

### 2. Write the Description

```yaml
---
description: Deploy application to production with pre-flight checks
---
```

### 3. Write Sequential Steps

Each step should be:
- **Specific** — exactly what to do
- **Verifiable** — how to know it's done
- **Independent** — can be retried without repeating prior steps

```markdown
1. **Run pre-deploy checks**
   - Execute: `python .agent/scripts/checklist.py .`
   - All checks must pass before proceeding
   - If any critical failures, stop and fix first

2. **Build production bundle**
   - Execute: `npm run build`
   - Verify no build errors

3. **Deploy to staging**
   - Execute: `npm run deploy:staging`
   - Verify staging URL is accessible

4. **Run E2E tests against staging**
   - Execute: `python .agent/skills/webapp-testing/scripts/playwright_runner.py`
   - All tests must pass

5. **Deploy to production**
   - Execute: `npm run deploy:prod`
   - Verify production URL
   - Monitor for errors (5 min)
```

### 4. Add Auto-Run Annotations (Optional)

Mark safe steps with `// turbo` for auto-execution:

```markdown
1. **Check git status**
   - Execute: `git status`
// turbo
2. **Run linter**
   - Execute: `npm run lint`
```

Use `// turbo-all` at the top to auto-run ALL steps.

---

## Workflow Design Patterns

### Linear (Steps in Order)

```
Step 1 → Step 2 → Step 3 → Done
```

Best for: deploys, audits, setup procedures.

### Branching (Decision Points)

```markdown
1. **Analyze the issue**

2. **Determine type**
   - If performance issue → Go to Performance section
   - If logic bug → Go to Debugging section
   - If UI issue → Go to Frontend section

### Performance
3a. Run profiler...

### Debugging
3b. Reproduce issue...
```

Best for: debugging, triage, routing.

### Loop (Iterate Until Done)

```markdown
1. **Write test** (RED)
2. **Write code** (GREEN)
3. **Refactor** (BLUE)
4. **Repeat** from step 1 for next feature
```

Best for: TDD, iterative development.

---

## Naming Conventions

| Element | Convention | Example |
|---------|-----------|---------|
| File name | `kebab-case.md` | `code-review.md` |
| Slash command | `/filename` | `/code-review` |
| Description | Imperative, concise | "Review code for quality and bugs" |

---

## Workflow Quality Checklist

Before shipping a workflow:

1. Did I include the YAML frontmatter with `description`?
2. Is the workflow mapping to a slash command?
3. Is it deterministic (numbered list)?
4. Did I remove all project-specific data? **(Review `docs/CONTENT-BOUNDARY.md` - P0 priority!)**
5. Does it delegate specialized work to agents?
6. Are the exit criteria clear?

---

## Examples

### Minimal Workflow

```markdown
---
description: Run all tests and report results
---

1. **Run unit tests**
   - Execute: `npm test`

2. **Run E2E tests**
   - Execute: `npx playwright test`

3. **Report results**
   - Summarize pass/fail counts
   - List any failures with file:line
```

### Complex Workflow

See `workflows/deploy.md` or `workflows/code-review.md` for full examples.
