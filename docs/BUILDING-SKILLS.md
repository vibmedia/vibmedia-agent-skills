# Building Skills

> How to create a domain skill that any agent can load.

---

## What is a Skill?

A skill is a **knowledge module** — a folder containing instructions, references, and optional scripts. Skills are loaded on-demand when the AI detects a matching task.

```
.agent/skills/
├── your-skill/
│   ├── SKILL.md           # Required — main instructions
│   ├── references/        # Optional — deep-dive docs, cheatsheets
│   └── scripts/           # Optional — automation scripts
```

---

## SKILL.md Format

```markdown
---
name: skill-name
description: When to use this skill. Include trigger phrases the user might say. Mention related skills for clarity. Keep under 200 chars.
metadata:
  version: 1.0.0
---

# Skill Title

> One-line purpose statement.

## When to Use

- [Trigger condition 1]
- [Trigger condition 2]
- [Trigger condition 3]

## Before Starting

[Context gathering — what questions to ask, what to check first]

## Core Framework

[The main knowledge, principles, rules, patterns]

### Section 1: [Topic]

[Instructions, tables, examples]

### Section 2: [Topic]

[Instructions, tables, examples]

## Output Format

[How the skill structures its output]

## Common Mistakes

- ❌ [Mistake to avoid]
- ❌ [Mistake to avoid]

## Related Skills

- **skill-name**: [When to use that instead]
- **skill-name**: [How it complements this skill]
```

---

## Step-by-Step Creation

### 1. Define the Trigger

The `description` field is how the AI finds your skill. Make it rich with trigger phrases:

```yaml
# BAD — too vague
description: SEO stuff

# GOOD — rich with triggers
description: >
  When the user wants to audit, review, or diagnose SEO issues.
  Also use when the user mentions "SEO audit," "technical SEO,"
  "why am I not ranking," "on-page SEO," or "meta tags review."
  For building pages at scale, see programmatic-seo.
```

### 2. Structure the Knowledge

Good skills follow this pattern:

```
1. Context Gathering   — What to ask before starting
2. Framework           — The core methodology (tables, steps, principles)
3. Specific Guidance   — Detailed rules for sub-topics
4. Output Format       — How to structure deliverables
5. Common Mistakes     — Anti-patterns to avoid
6. Related Skills      — Where to hand off
```

### 3. Use Tables Over Prose

Tables are faster for AI to parse and apply:

```markdown
## ❌ Prose (harder to apply)
When writing headlines, make sure they are specific and outcome-focused.
Avoid being too clever at the expense of clarity.

## ✅ Table (easier to apply)
| Element | Do | Don't |
|---------|-----|-------|
| Headlines | Specific, outcome-focused | Clever at expense of clarity |
| CTAs | Action verb + what they get | "Submit", "Click Here" |
```

### 4. Add References (Optional)

Deep-dive docs that the skill can load when needed:

```
your-skill/
├── SKILL.md
└── references/
    ├── detailed-framework.md
    ├── industry-benchmarks.md
    └── cheatsheet.sh
```

Reference from SKILL.md:
```markdown
See: [references/detailed-framework.md](references/detailed-framework.md)
```

### 5. Add Scripts (Optional)

Automation scripts the AI can run:

```
your-skill/
├── SKILL.md
└── scripts/
    ├── audit.py
    └── validate.sh
```

---

## Skill Quality Checklist

Before shipping a skill:

1. Did I include the YAML frontmatter?
2. Is the `description` specific with exact trigger phrases?
3. Did I use tables for structured data?
4. Did I remove all project-specific data and use generic placeholders? **(Review `docs/CONTENT-BOUNDARY.md` - this is P0 priority!)**
5. Are the examples illustrative but generic (e.g., `[Company Name]`)?
6. Is the skill actionable (tells *how* to do it) rather than just theoretical?
- [ ] Includes "Before Starting" context-gathering section
- [ ] Has "Output Format" section (so output is consistent)
- [ ] Has "Common Mistakes" section
- [ ] Has "Related Skills" section (prevents confusion between similar skills)
- [ ] Content is actionable (tells AI what to DO, not just what to know)

---

## Naming Conventions

| Element | Convention | Example |
|---------|-----------|---------|
| Folder name | `kebab-case` | `page-cro` |
| Skill name | `kebab-case` | `page-cro` |
| SKILL.md | Always uppercase `SKILL.md` | `SKILL.md` |
| References | `kebab-case.md` | `copy-frameworks.md` |
| Scripts | `snake_case.py` | `seo_checker.py` |

---

## Skill Sizing Guide

| Size | Lines | When |
|------|-------|------|
| **Small** | 50-100 | Single focused task (e.g., `schema-markup`) |
| **Medium** | 100-250 | Domain with multiple sub-topics (e.g., `copywriting`) |
| **Large** | 250-500 | Comprehensive methodology (e.g., `ai-seo`, `clean-code`) |
| **Too Large** | 500+ | Split into multiple skills or use references |

---

## Examples

### Minimal Skill (~60 lines)

```markdown
---
name: my-skill
description: When the user wants to [do X]. Trigger on "[phrase 1]", "[phrase 2]", "[phrase 3]".
---

# My Skill

## When to Use

- Doing X
- Fixing Y
- Building Z

## Framework

| Step | Action |
|------|--------|
| 1 | Assess the situation |
| 2 | Identify options |
| 3 | Execute best option |
| 4 | Verify results |

## Output Format

Provide:
1. Analysis summary
2. Recommendations (prioritized)
3. Implementation steps

## Related Skills

- **other-skill**: For [different aspect]
```
