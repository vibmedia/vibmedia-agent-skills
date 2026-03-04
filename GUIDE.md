# 📖 How to Use Guide

> Step-by-step guide to using Vibmedia Agent Skills in your projects.

---

## Quick Start (2 minutes)

```bash
# 1. Clone into your project
git clone https://github.com/vibmedia/vibmedia-agent-skills.git .agent

# 2. Edit vib.md with your company practices
nano .agent/vib.md

# 3. Open your project in Antigravity or Claude Code

# 4. Start using slash commands
/plan        # Plan a feature
/create      # Build something new
/debug       # Debug an issue
```

See [INSTALL.md](INSTALL.md) for detailed setup.

---

## System Hierarchy

The system has a clear hierarchy. The AI loads context top-down:

```
vib.md                          ← Company identity (ALWAYS loads first)
  └── profiles/[profile].md    ← Project type routing (dev|marketing|hybrid)
        └── agents/            ← Specialist personas (tagged: profile)
              └── skills/      ← Domain knowledge (tagged: profile)
                    └── workflows/  ← Slash command procedures
                          └── brands/[industry]/[brand]/  ← Client context
                                └── _common/industry.md   ← Industry knowledge
```

### What Each Layer Does

| Layer        | File                         | Purpose                                                    |
| ------------ | ---------------------------- | ---------------------------------------------------------- |
| **Company**  | `vib.md`                     | Your practices, standards, routing rules                   |
| **Profile**  | `profiles/*.md`              | Which agents/skills to prioritize                          |
| **Agent**    | `agents/*.md`                | Specialist persona + principles                            |
| **Skill**    | `skills/*/SKILL.md`          | Domain expertise (has `profile:` and `category:` metadata) |
| **Workflow** | `workflows/*.md`             | Step-by-step procedures                                    |
| **Industry** | `brands/[industry]/_common/` | Shared industry knowledge                                  |
| **Brand**    | `brands/[industry]/[brand]/` | Client-specific context                                    |

---

## Profiles — Dev vs Marketing vs Hybrid

Every project has a **profile** that determines which agents and skills are prioritized:

| Profile     | Set In `context.md`  | What Loads                             |
| ----------- | -------------------- | -------------------------------------- |
| `dev`       | `profile: dev`       | 26 dev skills + 10 dev agents          |
| `marketing` | `profile: marketing` | 29 marketing skills + marketing agents |
| `hybrid`    | `profile: hybrid`    | All skills, phase-based priority       |

### How Profiles Work

```
profile: dev       → AI prioritizes: backend, database, testing, security skills
profile: marketing → AI prioritizes: copywriting, SEO, CRO, ads skills
profile: hybrid    → AI uses both, switches by phase (Build → Grow)
```

Shared skills (clean-code, brainstorming, architecture, frontend) load for ALL profiles.

---

## Core Concepts

### Agents → Who does the work

Agents are **specialist AI personas**. Each has a focus area, a profile tag, and skills.

```
You: "Build a REST API for user management"
AI:  🤖 Applying knowledge of @backend-specialist...
     → Profile: dev
     → Loads: api-patterns, nodejs-best-practices, database-design
```

### Skills → What they know

Skills are **knowledge modules** loaded on-demand. Each has metadata:

- `SKILL.md` — Instructions and rules
- `profile:` — dev, marketing, or shared
- `category:` — Hierarchy grouping (backend, content, core, etc.)
- `references/` — Deep-dive docs, cheatsheets
- `scripts/` — Automation scripts (optional)

### Workflows → How to trigger

Workflows are **slash commands** that activate specific processes:

```
/plan     → Uses project-planner agent + plan-writing skill
/debug    → Uses debugger agent + systematic-debugging skill
/update   → Scans system, validates, syncs counts
```

---

## Working with Brands

### Setting Up a New Client

```bash
# 1. Create industry (if new)
cp -r .agent/brands/_industry-template .agent/brands/saas

# 2. Fill industry knowledge
nano .agent/brands/saas/_common/industry.md

# 3. Create brand
cp -r .agent/brands/saas/_brand-template .agent/brands/saas/acme-corp

# 4. Fill brand context (set profile: dev | marketing | hybrid)
nano .agent/brands/saas/acme-corp/context.md

# 5. Drop raw client data into reference/
# 6. Add logos, guidelines to brand-data/
```

### Brand Folder Contents

```
brands/saas/acme-corp/
├── context.md          # Brand identity + profile: marketing
├── todo.md             # Progress, decisions, ideas
├── structure.drawio    # Visual project map (draw.io)
├── reference/          # Raw client data (inbox)
├── brand-data/         # Processed assets (logos, guidelines)
└── artifacts/          # AI-generated deliverables
```

### Switching Brands

```
You: "Switch to acme-corp. Write their Q2 email sequence."
AI:  → Reads brands/saas/acme-corp/context.md
     → Detects profile: marketing
     → Loads marketing skills
     → Uses acme-corp's voice, audience, products
```

---

## Common Workflows

### 🏗️ Building a New Feature (Dev Profile)

```
1. /plan                    # Break down the feature into tasks
2. /create                  # Start building (agent auto-selected)
3. /test                    # Generate and run tests
4. /code-review             # Review code quality
5. /deploy                  # Deploy to production
```

### 📝 Marketing Campaign (Marketing Profile)

```
1. Set profile: marketing in context.md
2. "Write homepage copy for acme-corp"
   → Loads: copywriting skill + brand context
3. "Audit SEO for acme-corp.com"
   → Loads: seo-audit, schema-markup, ai-seo
4. "Set up Google Ads campaign"
   → Loads: paid-ads, ad-creative
```

### 🔀 Hybrid Project (Build + Grow)

```
Phase 1 — Build:
1. /create-prd              # Product Requirements Document
2. /plan                    # Architecture + tasks
3. /create                  # Build the product

Phase 2 — Grow:
4. "Write launch copy"      # → copywriting, launch-strategy
5. "Set up tracking"        # → analytics-tracking
6. "Run SEO audit"          # → seo-audit
```

### 🐛 Debugging

```
1. /debug                   # Systematic 4-phase debugging
   → Reproduce → Isolate → Understand → Fix & Verify
```

---

## Slash Commands Reference

### Development

| Command        | When to Use                              |
| -------------- | ---------------------------------------- |
| `/create`      | Build a new feature or application       |
| `/plan`        | Break down work into tasks before coding |
| `/enhance`     | Add or update features in existing code  |
| `/debug`       | Systematic debugging of issues           |
| `/test`        | Generate and run tests                   |
| `/code-review` | Review code for quality and bugs         |
| `/deploy`      | Deploy to production                     |
| `/preview`     | Start/stop local dev server              |

### Planning & Analysis

| Command        | When to Use                                  |
| -------------- | -------------------------------------------- |
| `/brainstorm`  | Explore ideas before building                |
| `/create-prd`  | Create a Product Requirements Document       |
| `/piv-plan`    | Deep feature plan with codebase analysis     |
| `/orchestrate` | Coordinate multiple agents for complex tasks |
| `/rca`         | Root cause analysis for issues               |

### System Management

| Command         | When to Use                                                   |
| --------------- | ------------------------------------------------------------- |
| `/update`       | After adding skills, agents, workflows, industries, or brands |
| `/audit-goals`  | Weekly — find gaps between goals and capabilities             |
| `/system-check` | Monthly — find errors, broken refs, stale data                |
| `/status`       | Check project progress                                        |

---

## Agent Selection

The AI **automatically selects** the best agent based on your request and the active profile.

Force a specific agent with `@`:

```
"@backend-specialist design the database schema"
"@security-auditor review this auth implementation"
"@seo-specialist audit our site"
```

### Agent Routing (Profile-Aware)

| Your Request         | Profile   | Agent                               |
| -------------------- | --------- | ----------------------------------- |
| "build API"          | dev       | `backend-specialist`                |
| "write copy"         | marketing | (copywriting skill)                 |
| "build landing page" | hybrid    | `frontend-specialist` + copywriting |
| "debug"              | any       | `debugger`                          |
| "plan"               | any       | `project-planner`                   |

---

## Skill Categories

### 🔧 Dev Skills (26) — `profile: dev`

`api-patterns` · `nodejs-best-practices` · `python-patterns` · `rust-pro` · `database-design` · `typeorm-patterns` · `testing-patterns` · `webapp-testing` · `tdd-workflow` · `code-review-checklist` · `requesting-code-review` · `receiving-code-review` · `verification-before-completion` · `lint-and-validate` · `vulnerability-scanner` · `red-team-tactics` · `deployment-procedures` · `server-management` · `mobile-design` · `react-native-guidelines` · `mcp-builder` · `i18n-localization` · `cloud-infrastructure` · `web3-smart-contracts` · `design-system-architecture` · `ml-engineer`

### 📈 Marketing Skills (29) — `profile: marketing`

`copywriting` · `copy-editing` · `cold-email` · `email-sequence` · `social-content` · `content-strategy` · `seo-audit` · `ai-seo` · `programmatic-seo` · `schema-markup` · `competitor-alternatives` · `page-cro` · `signup-flow-cro` · `onboarding-cro` · `form-cro` · `popup-cro` · `paywall-upgrade-cro` · `paid-ads` · `ad-creative` · `analytics-tracking` · `ab-test-setup` · `churn-prevention` · `free-tool-strategy` · `referral-program` · `marketing-ideas` · `marketing-psychology` · `launch-strategy` · `pricing-strategy` · `product-marketing-context`

### ⚡ Shared Skills (30) — `profile: shared`

`clean-code` · `brainstorming` · `plan-writing` · `architecture` · `app-builder` · `nextjs-react-expert` · `web-design-guidelines` · `composition-patterns` · `tailwind-patterns` · `frontend-design` · `behavioral-modes` · `parallel-agents` · `intelligent-routing` · `performance-profiling` · `systematic-debugging` · `documentation-templates` · `seo-fundamentals` · `geo-fundamentals` · `executing-plans` · `subagent-driven-development` · `using-git-worktrees` · `finishing-a-development-branch` · `writing-skills` · `bash-linux` · `powershell-windows` · `game-development` · `data-analysis` · `prompt-engineering` · `notebooklm-rag` · `github-mcp`

---

## Extending the System

| Want to add... | How                                      | After adding  |
| -------------- | ---------------------------------------- | ------------- |
| New skill      | See `docs/BUILDING-SKILLS.md`            | Run `/update` |
| New agent      | See `docs/BUILDING-AGENTS.md`            | Run `/update` |
| New workflow   | See `docs/BUILDING-WORKFLOWS.md`         | Run `/update` |
| New industry   | Copy `brands/_industry-template`         | Run `/update` |
| New brand      | Copy `brands/[industry]/_brand-template` | Run `/update` |

---

## Tips

1. **Fill `vib.md` first** — your company identity shapes all AI responses
2. **Set the profile** — `profile: dev` or `profile: marketing` in `context.md` saves tokens
3. **Use `/plan` first** — for complex features, plan before coding
4. **Use `/brainstorm` for vague ideas** — it asks the right questions
5. **Read brand context** — the AI is better when it knows the brand
6. **Run `/update` after changes** — keeps counts and references in sync
7. **Run `/system-check` monthly** — catches drift and broken references
8. **Use draw.io** — each brand gets a `structure.drawio` for visual mapping
