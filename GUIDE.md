# 📖 How to Use Guide

> Step-by-step guide to using Vibmedia Agent Skills in your projects.

---

## Quick Start (2 minutes)

```bash
# 1. Clone into your project
git clone https://github.com/vibmedia/vibmedia-agent-skills.git .agent

# 2. Open your project in Antigravity or Claude Code

# 3. Start using slash commands
/plan        # Plan a feature
/create      # Build something new
/debug       # Debug an issue
/enhance     # Improve existing code
```

That's it. The AI will automatically detect your `.agent/` directory and use the skills.

---

## Core Concepts

### Agents → Who does the work

Agents are **specialist AI personas**. Each has a focus area and knows which skills to use.

```
You: "Build a REST API for user management"
AI:  🤖 Applying knowledge of @backend-specialist...
     → Loads: api-patterns, nodejs-best-practices, database-design
```

### Skills → What they know

Skills are **knowledge modules** loaded on-demand. Each has:
- `SKILL.md` — Instructions and rules
- `references/` — Deep-dive docs, cheatsheets
- `scripts/` — Automation scripts (optional)

### Workflows → How to trigger

Workflows are **slash commands** that activate specific processes:

```
/plan     → Uses project-planner agent + plan-writing skill
/debug    → Uses debugger agent + systematic-debugging skill
/test     → Uses test-engineer agent + tdd-workflow skill
```

---

## Common Workflows

### 🏗️ Building a New Feature

```
1. /plan                    # Break down the feature into tasks
2. /create                  # Start building (agent auto-selected)
3. /test                    # Generate and run tests
4. /code-review             # Review code quality
5. /deploy                  # Deploy to production
```

### 🐛 Debugging an Issue

```
1. /debug                   # Systematic 4-phase debugging
   → Reproduce → Isolate → Understand → Fix & Verify
```

### 📝 Writing Marketing Copy

```
You: "Write homepage copy for our SaaS product"
AI:  🤖 Applying knowledge of @frontend-specialist...
     → Loads: copywriting skill
     → Asks: Page type? Audience? Product? Traffic source?
     → Outputs: Headline, subheadline, sections, CTAs with alternatives
```

### 🔍 SEO Audit

```
You: "Audit our site's SEO"
AI:  → Loads: seo-audit, schema-markup, ai-seo skills
     → Checks: Technical SEO, on-page, structured data, AI visibility
     → Outputs: Prioritized fixes with implementation steps
```

### 📊 CRO Analysis

```
You: "Our landing page isn't converting"
AI:  → Loads: page-cro skill
     → Analyzes: Value proposition, headlines, CTAs, trust signals, friction
     → Outputs: Quick wins, high-impact changes, test ideas
```

### 🚀 Product Launch

```
You: "Plan our product launch"
AI:  → Loads: launch-strategy skill
     → Asks: Launch type? Channels? Timeline?
     → Outputs: Phased launch plan with channel strategy
```

---

## Slash Commands Reference

### Development

| Command | When to Use |
|---------|-------------|
| `/create` | Build a new feature or application |
| `/plan` | Break down work into tasks before coding |
| `/enhance` | Add or update features in existing code |
| `/debug` | Systematic debugging of issues |
| `/test` | Generate and run tests |
| `/code-review` | Review code for quality and bugs |
| `/code-review-fix` | Fix issues found in code review |
| `/deploy` | Deploy to production |
| `/preview` | Start/stop local dev server |

### Planning & Analysis

| Command | When to Use |
|---------|-------------|
| `/brainstorm` | Explore ideas before building |
| `/create-prd` | Create a Product Requirements Document |
| `/piv-plan` | Deep feature plan with codebase analysis |
| `/piv-prime` | Prime AI with codebase understanding |
| `/orchestrate` | Coordinate multiple agents for complex tasks |
| `/rca` | Root cause analysis for issues |

### Verification

| Command | When to Use |
|---------|-------------|
| `/validate` | Run full validation suite |
| `/status` | Check project progress |
| `/execution-report` | Generate implementation report |
| `/system-review` | Review implementation against plan |

---

## Agent Selection

The AI **automatically selects** the best agent based on your request. You can also force a specific agent:

```
"@backend-specialist design the database schema"
"@security-auditor review this auth implementation"
"@seo-specialist audit our site"
```

### Agent Routing Cheat Sheet

| Your Request Contains | Agent Selected |
|----------------------|----------------|
| "build", "create", "implement" web UI | `frontend-specialist` |
| "API", "backend", "server" | `backend-specialist` |
| "database", "schema", "SQL" | `database-architect` |
| "mobile", "React Native", "iOS" | `mobile-developer` |
| "test", "TDD", "coverage" | `test-engineer` |
| "debug", "fix", "broken" | `debugger` |
| "security", "vulnerability", "auth" | `security-auditor` |
| "SEO", "ranking", "meta tags" | `seo-specialist` |
| "deploy", "CI/CD", "Docker" | `devops-engineer` |
| "plan", "architecture", "design" | `project-planner` |
| Marketing/CRO/copy related | Relevant marketing skills auto-loaded |

---

## Skill Categories at a Glance

### 🖥️ Development (30+ skills)

| Area | Key Skills |
|------|-----------|
| React/Next.js | `react-best-practices`, `composition-patterns` |
| Backend | `api-patterns`, `nodejs-best-practices`, `python-patterns` |
| Database | `database-design`, `prisma-expert`, `typeorm-patterns` |
| Testing | `tdd-workflow`, `testing-patterns`, `webapp-testing` |
| Code Quality | `clean-code`, `code-review-checklist` |
| Architecture | `architecture`, `plan-writing`, `app-builder` |
| Mobile | `mobile-design`, `react-native-guidelines` |

### 📈 Marketing (29 skills)

| Area | Key Skills |
|------|-----------|
| CRO | `page-cro`, `signup-flow-cro`, `form-cro`, `popup-cro` |
| Content | `copywriting`, `copy-editing`, `email-sequence`, `social-content` |
| SEO | `seo-audit`, `ai-seo`, `programmatic-seo`, `schema-markup` |
| Ads | `paid-ads`, `ad-creative` |
| Growth | `free-tool-strategy`, `referral-program`, `launch-strategy` |
| Strategy | `pricing-strategy`, `marketing-psychology`, `content-strategy` |

---

## Reference Files

Some skills include **cheatsheet reference files** for quick lookup:

```bash
# View available references for a skill
ls .agent/skills/clean-code/references/
# → solid-principles.md, design-patterns.md, code-smells.md, 
#   git-cheatsheet.sh, architecture.md, ...

ls .agent/skills/nodejs-best-practices/references/
# → node-cheatsheet.js (565 lines of Node.js patterns)

ls .agent/skills/database-design/references/
# → mysql-cheatsheet.sh, redis-cheatsheet.sh
```

---

## Validation Scripts

Run checks before deploying:

```bash
# Quick development checks (security, lint, tests, UX)
python .agent/scripts/checklist.py .

# Full pre-deploy suite (+ Lighthouse, E2E, bundle analysis)
python .agent/scripts/verify_all.py . --url http://localhost:3000
```

### Individual audit scripts

```bash
python .agent/skills/vulnerability-scanner/scripts/security_scan.py
python .agent/skills/frontend-design/scripts/ux_audit.py
python .agent/skills/seo-fundamentals/scripts/seo_checker.py
python .agent/skills/performance-profiling/scripts/lighthouse_audit.py
python .agent/skills/webapp-testing/scripts/playwright_runner.py
```

---

## Tips

1. **Be specific** — "Build a REST API with JWT auth for user management" beats "build an API"
2. **Use `/plan` first** — For complex features, plan before coding
3. **Use `/brainstorm` for vague ideas** — It'll ask the right questions
4. **Check the skill** — If output isn't great, read the relevant `SKILL.md` for what context it needs
5. **Stack skills** — Complex tasks auto-load multiple skills: "SEO audit + fix" loads `seo-audit` + `schema-markup` + `ai-seo`
6. **Reference files are gold** — Check `references/` folders for cheatsheets and deep-dive docs
