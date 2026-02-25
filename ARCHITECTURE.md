# Antigravity Kit Architecture

> Comprehensive AI Agent Capability Expansion Toolkit

---

## 📋 Overview

Antigravity Kit is a modular system consisting of:

- **21 Specialist Agents** - Role-based AI personas
- **77 Skills** - Domain-specific knowledge modules
- **11 Workflows** - Slash command procedures

---

## 🏗️ Directory Structure

```plaintext
.agent/
├── ARCHITECTURE.md          # This file
├── agents/                  # 21 Specialist Agents
├── skills/                  # 77 Skills
├── workflows/               # 11 Slash Commands
├── rules/                   # Global Rules
└── scripts/                 # Master Validation Scripts
```

---

## 🤖 Agents (21)

Specialist AI personas for different domains.

| Agent                    | Focus                      | Skills Used                                              |
| ------------------------ | -------------------------- | -------------------------------------------------------- |
| `orchestrator`           | Multi-agent coordination   | parallel-agents, behavioral-modes                        |
| `project-planner`        | Discovery, task planning   | brainstorming, plan-writing, architecture                |
| `frontend-specialist`    | Web UI/UX                  | frontend-design, react-best-practices, tailwind-patterns |
| `backend-specialist`     | API, business logic        | api-patterns, nodejs-best-practices, database-design     |
| `database-architect`     | Schema, SQL                | database-design, prisma-expert                           |
| `mobile-developer`       | iOS, Android, RN           | mobile-design                                            |
| `game-developer`         | Game logic, mechanics      | game-development                                         |
| `devops-engineer`        | CI/CD, Docker              | deployment-procedures, docker-expert                     |
| `security-auditor`       | Security compliance        | vulnerability-scanner, red-team-tactics                  |
| `penetration-tester`     | Offensive security         | red-team-tactics                                         |
| `test-engineer`          | Testing strategies         | testing-patterns, tdd-workflow, webapp-testing           |
| `debugger`               | Root cause analysis        | systematic-debugging                                     |
| `performance-optimizer`  | Speed, Web Vitals          | performance-profiling                                    |
| `seo-specialist`         | Ranking, visibility        | seo-fundamentals, geo-fundamentals                       |
| `documentation-writer`   | Manuals, docs              | documentation-templates                                  |
| `product-manager`        | Requirements, user stories | plan-writing, brainstorming                              |
| `product-owner`          | Strategy, backlog, MVP     | plan-writing, brainstorming                              |
| `qa-automation-engineer` | E2E testing, CI pipelines  | webapp-testing, testing-patterns                         |
| `code-archaeologist`     | Legacy code, refactoring   | clean-code, code-review-checklist                        |
| `code-reviewer`          | Code quality review        | requesting-code-review, receiving-code-review            |
| `explorer-agent`         | Codebase analysis          | -                                                        |

---

## 🧩 Skills (77)

Modular knowledge domains that agents can load on-demand. based on task context.

### Frontend & UI

| Skill                   | Description                                                           |
| ----------------------- | --------------------------------------------------------------------- |
| `react-best-practices`  | React & Next.js performance optimization (Vercel - 57 rules)          |
| `web-design-guidelines` | Web UI audit - 100+ rules for accessibility, UX, performance (Vercel) |
| `composition-patterns`  | React composition patterns - compound components, state lifting       |
| `tailwind-patterns`     | Tailwind CSS v4 utilities                                             |
| `frontend-design`       | UI/UX patterns, design systems                                        |
| `ui-ux-pro-max`         | 50 styles, 21 palettes, 50 fonts                                      |

### Backend & API

| Skill                   | Description                    |
| ----------------------- | ------------------------------ |
| `api-patterns`          | REST, GraphQL, tRPC            |
| `nestjs-expert`         | NestJS modules, DI, decorators |
| `nodejs-best-practices` | Node.js async, modules         |
| `python-patterns`       | Python standards, FastAPI      |

### Database

| Skill              | Description                         |
| ------------------ | ----------------------------------- |
| `database-design`  | Schema design, optimization         |
| `prisma-expert`    | Prisma ORM, migrations              |
| `typeorm-patterns` | TypeORM entities, relations, migrations, QueryBuilder |

### TypeScript/JavaScript

| Skill               | Description                         |
| ------------------- | ----------------------------------- |
| `typescript-expert` | Type-level programming, performance |

### Cloud & Infrastructure

| Skill                   | Description               |
| ----------------------- | ------------------------- |
| `docker-expert`         | Containerization, Compose |
| `deployment-procedures` | CI/CD, deploy workflows   |
| `server-management`     | Infrastructure management |

### Testing & Quality

| Skill                   | Description              |
| ----------------------- | ------------------------ |
| `testing-patterns`      | Jest, Vitest, strategies                     |
| `webapp-testing`        | E2E, Playwright                              |
| `tdd-workflow`          | Test-driven development (+ Superpowers TDD)  |
| `code-review-checklist` | Code review standards                        |
| `requesting-code-review`| When/how to dispatch code reviewer           |
| `receiving-code-review` | Evaluating feedback, pushback protocol       |
| `verification-before-completion` | Evidence before claims, iron law    |
| `lint-and-validate`     | Linting, validation                          |

### Security

| Skill                   | Description              |
| ----------------------- | ------------------------ |
| `vulnerability-scanner` | Security auditing, OWASP |
| `red-team-tactics`      | Offensive security       |

### Architecture & Planning

| Skill           | Description                                    |
| --------------- | ---------------------------------------------- |
| `app-builder`   | Full-stack app scaffolding                     |
| `architecture`  | System design patterns                         |
| `plan-writing`  | Task planning, breakdown (+ Superpowers plans) |
| `brainstorming` | Socratic questioning (+ Superpowers gate)      |
| `executing-plans` | Batch execution with checkpoints             |
| `subagent-driven-development` | Subagent per task + 2-stage review |
| `using-git-worktrees` | Isolated workspace setup                 |
| `finishing-a-development-branch` | Merge/PR/keep/discard workflow  |
| `writing-skills` | TDD for skill creation, CSO                   |

### Mobile

| Skill                    | Description                                        |
| ------------------------ | -------------------------------------------------- |
| `mobile-design`          | Mobile UI/UX patterns                              |
| `react-native-guidelines`| React Native & Expo best practices (Vercel - 30+ rules) |

### Game Development

| Skill              | Description           |
| ------------------ | --------------------- |
| `game-development` | Game logic, mechanics |

### SEO & Growth

| Skill              | Description                   |
| ------------------ | ----------------------------- |
| `seo-fundamentals` | SEO, E-E-A-T, Core Web Vitals |
| `geo-fundamentals` | GenAI optimization            |
| `seo-audit`        | Technical and on-page SEO     |
| `ai-seo`           | AI search optimization (AEO, GEO, LLMO) |
| `programmatic-seo` | Scaled page generation        |
| `schema-markup`    | Structured data / JSON-LD     |

### Marketing & CRO

| Skill                     | Description                                  |
| ------------------------- | -------------------------------------------- |
| `page-cro`                | Marketing page conversion optimization       |
| `signup-flow-cro`         | Registration flow optimization               |
| `onboarding-cro`          | Post-signup activation                       |
| `form-cro`                | Lead capture form optimization               |
| `popup-cro`               | Modals and overlays                          |
| `paywall-upgrade-cro`     | In-app upgrade moments                       |
| `copywriting`             | Marketing page copy                          |
| `copy-editing`            | Edit and polish existing copy                |
| `cold-email`              | B2B cold outreach emails                     |
| `email-sequence`          | Automated email flows                        |
| `social-content`          | Social media content                         |
| `content-strategy`        | Content planning and strategy                |
| `paid-ads`                | Google, Meta, LinkedIn ad campaigns          |
| `ad-creative`             | Bulk ad creative generation                  |
| `analytics-tracking`      | Event tracking setup (GA4, GTM)              |
| `ab-test-setup`           | Experiment design                            |
| `churn-prevention`        | Cancel flows, save offers, dunning           |
| `free-tool-strategy`      | Marketing tools and calculators              |
| `referral-program`        | Referral and affiliate programs              |
| `marketing-ideas`         | 140 SaaS marketing ideas                     |
| `marketing-psychology`    | Mental models and psychology                 |
| `launch-strategy`         | Product launches and announcements           |
| `pricing-strategy`        | Pricing, packaging, monetization             |
| `competitor-alternatives` | Comparison and alternative pages             |
| `product-marketing-context` | Product marketing context setup            |

### Shell/CLI

| Skill                | Description               |
| -------------------- | ------------------------- |
| `bash-linux`         | Linux commands, scripting |
| `powershell-windows` | Windows PowerShell        |

### Other

| Skill                     | Description               |
| ------------------------- | ------------------------- |
| `clean-code`              | Coding standards + SOLID + Karpathy (Global) |
| `behavioral-modes`        | Agent personas            |
| `parallel-agents`         | Multi-agent patterns      |
| `mcp-builder`             | Model Context Protocol    |
| `documentation-templates` | Doc formats               |
| `i18n-localization`       | Internationalization      |
| `performance-profiling`   | Web Vitals, optimization  |
| `systematic-debugging`    | Troubleshooting           |

---

## 🔄 Workflows (11)

Slash command procedures. Invoke with `/command`.

| Command          | Description              |
| ---------------- | ------------------------ |
| `/brainstorm`    | Socratic discovery       |
| `/create`        | Create new features      |
| `/debug`         | Debug issues             |
| `/deploy`        | Deploy application       |
| `/enhance`       | Improve existing code    |
| `/orchestrate`   | Multi-agent coordination |
| `/plan`          | Task breakdown           |
| `/preview`       | Preview changes          |
| `/status`        | Check project status     |
| `/test`          | Run tests                |
| `/ui-ux-pro-max` | Design with 50 styles    |

---

## 🎯 Skill Loading Protocol

```plaintext
User Request → Skill Description Match → Load SKILL.md
                                            ↓
                                    Read references/
                                            ↓
                                    Read scripts/
```

### Skill Structure

```plaintext
skill-name/
├── SKILL.md           # (Required) Metadata & instructions
├── scripts/           # (Optional) Python/Bash scripts
├── references/        # (Optional) Templates, docs
└── assets/            # (Optional) Images, logos
```

### Enhanced Skills (with scripts/references)

| Skill               | Files | Coverage                            |
| ------------------- | ----- | ----------------------------------- |
| `ui-ux-pro-max`     | 27    | 50 styles, 21 palettes, 50 fonts    |
| `app-builder`       | 20    | Full-stack scaffolding              |

---

## � Scripts (2)

Master validation scripts that orchestrate skill-level scripts.

### Master Scripts

| Script          | Purpose                                 | When to Use              |
| --------------- | --------------------------------------- | ------------------------ |
| `checklist.py`  | Priority-based validation (Core checks) | Development, pre-commit  |
| `verify_all.py` | Comprehensive verification (All checks) | Pre-deployment, releases |

### Usage

```bash
# Quick validation during development
python .agent/scripts/checklist.py .

# Full verification before deployment
python .agent/scripts/verify_all.py . --url http://localhost:3000
```

### What They Check

**checklist.py** (Core checks):

- Security (vulnerabilities, secrets)
- Code Quality (lint, types)
- Schema Validation
- Test Suite
- UX Audit
- SEO Check

**verify_all.py** (Full suite):

- Everything in checklist.py PLUS:
- Lighthouse (Core Web Vitals)
- Playwright E2E
- Bundle Analysis
- Mobile Audit
- i18n Check

For details, see [scripts/README.md](scripts/README.md)

---

## 📊 Statistics

| Metric              | Value                         |
| ------------------- | ----------------------------- |
| **Total Agents**    | 21                            |
| **Total Skills**    | 77                            |
| **Total Workflows** | 11                            |
| **Total Scripts**   | 2 (master) + 18 (skill-level) |
| **Coverage**        | ~98% web/mobile/marketing     |

---

## 🔗 Quick Reference

| Need     | Agent                 | Skills                                |
| -------- | --------------------- | ------------------------------------- |
| Web App  | `frontend-specialist` | react-best-practices, frontend-design |
| API      | `backend-specialist`  | api-patterns, nodejs-best-practices   |
| Mobile   | `mobile-developer`    | mobile-design                         |
| Database | `database-architect`  | database-design, prisma-expert        |
| Security | `security-auditor`    | vulnerability-scanner                 |
| Testing  | `test-engineer`       | testing-patterns, webapp-testing      |
| Debug    | `debugger`            | systematic-debugging                  |
| Plan     | `project-planner`     | brainstorming, plan-writing           |
