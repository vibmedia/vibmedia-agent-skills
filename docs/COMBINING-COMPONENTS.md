# Combining Components

> How agents, skills, and workflows work together — and how to design new combinations.

---

## The System Model

```
                    ┌─────────────┐
User Request ──────►│ Agent Router│
                    └──────┬──────┘
                           │ selects
                    ┌──────▼──────┐
                    │    Agent    │ (persona + principles)
                    └──────┬──────┘
                           │ loads
              ┌────────────┼────────────┐
              ▼            ▼            ▼
          ┌───────┐   ┌───────┐   ┌───────┐
          │Skill 1│   │Skill 2│   │Skill 3│
          └───┬───┘   └───┬───┘   └───┬───┘
              │           │           │
         references/  references/  scripts/
```

### Flow

1. **Router** reads the request and picks the best agent
2. **Agent** provides persona, principles, and decision-making framework
3. **Skills** provide domain knowledge — loaded based on what the task needs
4. **References** give deep-dive docs when the skill needs extra detail
5. **Scripts** automate validation, audits, and checks

---

## How Routing Works

The router matches requests to agents using the `description` field:

```
"Build a landing page" → matches frontend-specialist (has "UI", "web", "page")
                       → loads: react-best-practices, frontend-design, copywriting
```

Multiple skills can load simultaneously. The agent decides which apply.

---

## Designing a New Combination

### Example: "Launch a Product"

**Step 1 — What human team would do this?**

```
Marketing Manager → owns the strategy
Content Writer    → creates copy
Frontend Dev      → builds pages
SEO Specialist    → optimizes discovery
Ads Manager       → runs paid campaigns
```

**Step 2 — Map to agents + skills:**

| Role | Agent | Skills |
|------|-------|--------|
| Strategy | `marketing-manager` | content-strategy, launch-strategy |
| Copy | `content-writer` | copywriting, email-sequence |
| Pages | `frontend-specialist` | react-best-practices, frontend-design |
| SEO | `seo-specialist` | seo-audit, ai-seo, schema-markup |
| Ads | `paid-ads-manager` | paid-ads, ad-creative |

**Step 3 — Create a workflow:** `/launch`

```markdown
---
description: Execute a product launch across content, pages, SEO, and ads
---

1. **Create launch brief**
   - Agent: marketing-manager
   - Output: Campaign brief with objectives, audience, channels, timeline

2. **Write landing page copy**
   - Agent: content-writer
   - Input: Launch brief
   - Output: Headline, sections, CTAs

3. **Build landing page**
   - Agent: frontend-specialist
   - Input: Copy + brand guidelines
   - Output: Deployed page

4. **Optimize for SEO**
   - Agent: seo-specialist
   - Input: Landing page URL
   - Output: SEO fixes applied

5. **Set up ad campaigns**
   - Agent: paid-ads-manager
   - Input: Launch brief + landing page URL
   - Output: Campaign configuration
```

---

## Combination Patterns

### Pattern 1: Sequential Pipeline

```
Agent A → output → Agent B → output → Agent C → deliverable
```

**Use when:** Each step's output is the next step's input.
**Examples:** Content pipeline, deploy pipeline, onboarding flow.

### Pattern 2: Parallel Fan-Out

```
                ┌→ Agent A → output ─┐
Request ────────┼→ Agent B → output ─┼→ Synthesis
                └→ Agent C → output ─┘
```

**Use when:** Independent analyses needed from different perspectives.
**Examples:** Code review (security + quality + performance), competitive analysis.

Use the `orchestrator` agent with `/orchestrate` for this pattern.

### Pattern 3: Expert Consultation

```
Primary Agent works on task
   → Hits uncertainty
   → Loads specialist skill
   → Continues with new knowledge
```

**Use when:** Main agent needs domain expertise mid-task.
**Examples:** Frontend dev needs SEO advice, backend dev needs security review.

### Pattern 4: Iterative Loop

```
Agent → output → Review → feedback → Agent → output → Review → ✅
```

**Use when:** Quality improves through iteration.
**Examples:** Copy editing, code review, design iteration.

---

## Best Practices

### 1. One Agent Per Responsibility

```
❌ One agent that does everything
✅ Focused agents that collaborate
```

### 2. Skills Are the Knowledge, Agents Are the Judgment

```
Skill:  "Here are the CRO principles and frameworks"
Agent:  "Based on these principles, HERE is what we should do for THIS page"
```

### 3. Workflows Are the Glue

```
Without workflow: User manually chains agent → agent → agent
With workflow:    /launch triggers the entire chain automatically
```

### 4. Reference Files Prevent Bloat

```
❌ 500-line SKILL.md with everything
✅ 150-line SKILL.md + references/ for deep dives
```

---

## Creating Your Own Stack

### For a Marketing Agency

```
Agents:  marketing-manager, content-writer, seo-specialist, paid-ads-manager
Skills:  copywriting, page-cro, seo-audit, paid-ads, analytics-tracking
Workflow: /campaign → strategy → copy → page → SEO → ads → tracking
```

### For a Dev Shop

```
Agents:  project-planner, backend-specialist, frontend-specialist, test-engineer
Skills:  plan-writing, api-patterns, react-best-practices, tdd-workflow
Workflow: /feature → plan → backend → frontend → test → review → deploy
```

### For a Full-Service Company

```
Agents:  All 21+ agents
Skills:  All 77 skills
Workflows: /campaign, /feature, /launch, /onboard-client, /sprint
```
