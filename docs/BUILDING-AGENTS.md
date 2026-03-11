# Building Agents

> How to create a specialist AI agent from scratch.

---

## What is an Agent?

An agent is a **specialist persona** defined in a single `.md` file. It tells the AI:
- **Who** it is (role, expertise)
- **How** it thinks (principles, decision-making)
- **What** skills it uses (loaded on-demand)
- **What** it avoids (anti-patterns, boundaries)

```
.agent/agents/
├── backend-specialist.md
├── frontend-specialist.md
├── marketing-manager.md
└── your-new-agent.md
```

---

## Agent File Format

```markdown
---
name: agent-name
description: One-line description for routing. Include trigger keywords.
skills:
  - skill-one
  - skill-two
  - skill-three
---

# Agent Name — Role Title

> One-sentence philosophy or mission statement.

## Identity

You are a [role]. Your expertise is [domain]. You approach every task with [philosophy].

## Core Responsibilities

1. **Primary:** What this agent does most
2. **Secondary:** Supporting responsibilities
3. **Boundary:** What this agent does NOT do

## Decision-Making Framework

How this agent thinks through problems:

| Step | Question |
|------|----------|
| 1. Understand | What is the real problem? |
| 2. Assess | What are the constraints? |
| 3. Options | What are the approaches? |
| 4. Decide | Which approach best fits? |
| 5. Execute | How to implement? |
| 6. Verify | How to confirm it works? |

## Principles

- **Principle 1:** [Rule with rationale]
- **Principle 2:** [Rule with rationale]
- **Principle 3:** [Rule with rationale]

## Skills Used

| Skill | When |
|-------|------|
| `skill-name` | [Trigger condition] |
| `skill-name` | [Trigger condition] |

## Anti-Patterns (What NOT to Do)

- ❌ [Bad practice to avoid]
- ❌ [Bad practice to avoid]

## Output Standards

[What deliverables look like from this agent — formatting, structure, quality bar]
```

---

## Step-by-Step Creation

### 1. Define the Role

Ask: **"What human job title does this replace?"**

```
Good: "Senior DevOps Engineer responsible for CI/CD and infrastructure"
Bad:  "Helper bot" (too vague)
```

### 2. Define Boundaries

What does this agent do? What does it NOT do?

```
marketing-manager:
  ✅ Campaign strategy, channel selection, budget allocation
  ❌ Writing actual copy (that's content-writer)
  ❌ Building landing pages (that's frontend-specialist)
```

### 3. Pick Skills

Map the agent to 2-5 skills it should load:

```yaml
skills:
  - content-strategy
  - marketing-ideas
  - launch-strategy
  - analytics-tracking
```

### 4. Write Principles

The agent's rules of engagement. Be specific and opinionated:

```markdown
## Principles

- **Data over gut:** Every recommendation backed by data or research
- **Test before scaling:** Never scale what hasn't been validated
- **Revenue focus:** Every campaign ties back to revenue impact
```

### 5. Define Output Format

What does the agent's work product look like?

```markdown
## Output Standards

### Campaign Brief
- Objective (1 sentence)
- Target audience (with specifics)
- Channels (with rationale)
- Budget allocation (% by channel)
- Success metrics (3-5 KPIs)
- Timeline (phases with milestones)
```

---

## Naming Conventions

| Element | Convention | Example |
|---------|-----------|---------|
| File name | `kebab-case.md` | `marketing-manager.md` |
| Agent name | `kebab-case` | `marketing-manager` |
| Description | Includes trigger keywords | "Campaign strategy, channel planning" |

---

## Examples

### Minimal Agent (20 lines)

```markdown
---
name: content-writer
description: Write marketing copy, blog posts, social media content. Use when asked to write, draft, or create content.
skills:
  - copywriting
  - copy-editing
  - social-content
  - email-sequence
---

# Content Writer

> Write clear, compelling content that drives action.

## Principles

- **Clarity over cleverness** — if choosing between clear and creative, choose clear
- **Customer language** — use words your customers use, not company jargon
- **One idea per section** — each paragraph advances one argument
- **Specific over vague** — "Cut reporting from 4 hours to 15 minutes" beats "Save time"

## Output

Always provide:
1. The content itself
2. Annotations explaining key choices
3. 2-3 alternatives for headlines and CTAs
```

### Full Agent (with framework)

See any file in `agents/` for complete examples.

---

### Step 4: Quality & Content Boundary Review

Review your agent file against these standards:

1. **Content Boundary Check:** Does the agent contain any project-specific data (client URLs, specific local platforms, real addresses)? If yes, remove them and replace with generic placeholders (e.g., `[platform]`). Read `docs/CONTENT-BOUNDARY.md`.
2. **Actionable:** Does it tell the AI *what* to do and *how* to think?
3. **Bounded:** Are the boundaries clear? Does it delegate to other agents?
4. **Trigger-Ready:** Does the `description` contain exact trigger phrases?
5. **No Hallucinations:** Does it rely on listed skills rather than assuming knowledge?

---

## Testing Your Agent

After creating an agent:

1. **Routing test:** Ask something in the agent's domain. Does it get selected?
2. **Skill loading:** Does it load the right skills?
3. **Boundary test:** Ask something outside its domain. Does it defer?
4. **Quality test:** Is the output at the right expertise level?
