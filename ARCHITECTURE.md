# Antigravity Kit Architecture

> Comprehensive AI Agent Capability Expansion Toolkit

---

## 📋 Overview

Antigravity Kit is a modular system consisting of:

- **26 Specialist Agents** - Role-based AI personas
- **93 Skills** - Domain-specific knowledge modules
- **30 Slash Commands** - Slash command procedures

---

## 🏗️ Directory Structure

```plaintext
.agent/
├── vib.md                   # Company identity (loads first)
├── telos.md                 # Framework-level Telos tracker
├── ARCHITECTURE.md          # This file
├── structure.drawio          # Visual system map (draw.io)
├── profiles/                # Project-type routing (3 profiles)
├── agents/                  # 26 Specialist Agents
├── skills/                  # 93 Skills (tagged: dev|marketing|shared)
├── workflows/               # 26 Slash Commands
├── brands/                  # Industry → Brand context folders
├── docs/                    # Authoring guides (5 files)
├── rules/                   # Global Rules (inc. coverage rule)
└── scripts/                 # Master Validation Scripts
```

---

## 🤖 Agents (26)

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
| `wordpress-site-builder` | WordPress site builds      | wordpress-mcp-bundle, wordpress-site-build, envato-template-selection |
| `local-seo-manager`      | Local SEO, GMB, citations  | local-seo, google-my-business, seo-fundamentals          |
| `listing-automation`     | Platform listings          | business-listing, client-communication, copywriting      |
| `client-coordinator`     | Client comms, approvals    | client-communication, brainstorming                      |
| `crocoblock-specialist`  | Dynamic data, JetEngine    | frontend-design                                          |

---

## 🧩 Skills (93)

Modular knowledge domains that agents can load on-demand based on task context.

### Frontend & UI

| Skill                        | Profile | Description                                                           |
| ---------------------------- | ------- | --------------------------------------------------------------------- |
| `nextjs-react-expert`        | shared  | React & Next.js performance optimization (Vercel - 57 rules)          |
| `web-design-guidelines`      | shared  | Web UI audit - 100+ rules for accessibility, UX, performance (Vercel) |
| `composition-patterns`       | shared  | React composition patterns - compound components, state lifting       |
| `tailwind-patterns`          | shared  | Tailwind CSS v4 utilities                                             |
| `frontend-design`            | shared  | UI/UX patterns, design systems                                        |
| `ui-ux-pro-max`              | shared  | 50 styles, 21 palettes, 50 fonts                                      |
| `design-system-architecture` | dev     | Figma sync, React/Tailwind token strategy                             |

### Backend & API

| Skill                   | Profile | Description                   |
| ----------------------- | ------- | ----------------------------- |
| `api-patterns`          | dev     | REST, GraphQL, tRPC           |
| `nodejs-best-practices` | dev     | Node.js async, modules        |
| `python-patterns`       | dev     | Python standards, FastAPI     |
| `rust-pro`              | dev     | Rust 1.75+ async, type system |

### Database & Web3

| Skill                  | Profile | Description                                           |
| ---------------------- | ------- | ----------------------------------------------------- |
| `database-design`      | dev     | Schema design, optimization                           |
| `typeorm-patterns`     | dev     | TypeORM entities, relations, migrations, QueryBuilder |
| `web3-smart-contracts` | dev     | Solidity, CEI patterns, Hardhat/Foundry testing       |

### Cloud & Infrastructure

| Skill                   | Profile | Description                               |
| ----------------------- | ------- | ----------------------------------------- |
| `deployment-procedures` | dev     | CI/CD, deploy workflows                   |
| `server-management`     | dev     | Infrastructure management                 |
| `cloud-infrastructure`  | dev     | Terraform, AWS/GCP architecture, security |

### Testing & Quality

| Skill                            | Description                                 |
| -------------------------------- | ------------------------------------------- |
| `testing-patterns`               | Jest, Vitest, strategies                    |
| `webapp-testing`                 | E2E, Playwright                             |
| `tdd-workflow`                   | Test-driven development (+ Superpowers TDD) |
| `code-review-checklist`          | Code review standards                       |
| `requesting-code-review`         | When/how to dispatch code reviewer          |
| `receiving-code-review`          | Evaluating feedback, pushback protocol      |
| `verification-before-completion` | Evidence before claims, iron law            |
| `lint-and-validate`              | Linting, validation                         |

### Security

| Skill                   | Description              |
| ----------------------- | ------------------------ |
| `vulnerability-scanner` | Security auditing, OWASP |
| `red-team-tactics`      | Offensive security       |

### Architecture & Planning

| Skill                            | Description                                    |
| -------------------------------- | ---------------------------------------------- |
| `app-builder`                    | Full-stack app scaffolding                     |
| `architecture`                   | System design patterns                         |
| `plan-writing`                   | Task planning, breakdown (+ Superpowers plans) |
| `brainstorming`                  | Socratic questioning (+ Superpowers gate)      |
| `executing-plans`                | Batch execution with checkpoints               |
| `subagent-driven-development`    | Subagent per task + 2-stage review             |
| `using-git-worktrees`            | Isolated workspace setup                       |
| `finishing-a-development-branch` | Merge/PR/keep/discard workflow                 |
| `writing-skills`                 | TDD for skill creation, CSO                    |
| `notebooklm-rag`                 | Connect to NotebookLM for stable RAG knowledge |

### Mobile

| Skill                     | Description                                             |
| ------------------------- | ------------------------------------------------------- |
| `mobile-design`           | Mobile UI/UX patterns                                   |
| `react-native-guidelines` | React Native & Expo best practices (Vercel - 30+ rules) |

### Game Development

| Skill              | Description           |
| ------------------ | --------------------- |
| `game-development` | Game logic, mechanics |

### SEO & Growth

| Skill              | Description                             |
| ------------------ | --------------------------------------- |
| `seo-fundamentals` | SEO, E-E-A-T, Core Web Vitals           |
| `geo-fundamentals` | GenAI optimization                      |
| `seo-audit`        | Technical and on-page SEO               |
| `ai-seo`           | AI search optimization (AEO, GEO, LLMO) |
| `programmatic-seo` | Scaled page generation                  |
| `schema-markup`    | Structured data / JSON-LD               |

### WordPress & Site Building

| Skill                        | Profile   | Description                                           |
| ---------------------------- | --------- | ----------------------------------------------------- |
| `wordpress-mcp-bundle`       | marketing | MCP tools for Elementor, JetEngine, WordPress REST    |
| `wordpress-site-build`       | marketing | End-to-end WordPress build checklist (5 phases)       |
| `envato-template-selection`  | marketing | Envato Elementor Kit search, evaluation, plugin mgmt  |

### Local SEO & Listings

| Skill                  | Profile   | Description                                           |
| ---------------------- | --------- | ----------------------------------------------------- |
| `local-seo`            | marketing | NAP consistency, citations, local pack optimization   |
| `google-my-business`   | marketing | GMB profiles, reviews, Google Posts, API integration   |
| `business-listing`     | marketing | Platform listings with harness pattern (Zomato, etc.) |

### Client Communication

| Skill                  | Profile   | Description                                           |
| ---------------------- | --------- | ----------------------------------------------------- |
| `client-communication` | marketing | WhatsApp/Evolution API, OTP relay, approvals, pending |

### Marketing & CRO

| Skill                       | Description                            |
| --------------------------- | -------------------------------------- |
| `page-cro`                  | Marketing page conversion optimization |
| `signup-flow-cro`           | Registration flow optimization         |
| `onboarding-cro`            | Post-signup activation                 |
| `form-cro`                  | Lead capture form optimization         |
| `popup-cro`                 | Modals and overlays                    |
| `paywall-upgrade-cro`       | In-app upgrade moments                 |
| `copywriting`               | Marketing page copy                    |
| `copy-editing`              | Edit and polish existing copy          |
| `cold-email`                | B2B cold outreach emails               |
| `email-sequence`            | Automated email flows                  |
| `social-content`            | Social media content                   |
| `content-strategy`          | Content planning and strategy          |
| `paid-ads`                  | Google, Meta, LinkedIn ad campaigns    |
| `ad-creative`               | Bulk ad creative generation            |
| `analytics-tracking`        | Event tracking setup (GA4, GTM)        |
| `ab-test-setup`             | Experiment design                      |
| `churn-prevention`          | Cancel flows, save offers, dunning     |
| `free-tool-strategy`        | Marketing tools and calculators        |
| `referral-program`          | Referral and affiliate programs        |
| `marketing-ideas`           | 140 SaaS marketing ideas               |
| `marketing-psychology`      | Mental models and psychology           |
| `launch-strategy`           | Product launches and announcements     |
| `pricing-strategy`          | Pricing, packaging, monetization       |
| `competitor-alternatives`   | Comparison and alternative pages       |
| `product-marketing-context` | Product marketing context setup        |

### Shell/CLI

| Skill                | Description               |
| -------------------- | ------------------------- |
| `bash-linux`         | Linux commands, scripting |
| `powershell-windows` | Windows PowerShell        |

### AI & Data

| Skill            | Profile | Description                                 |
| ---------------- | ------- | ------------------------------------------- |
| `notebooklm-rag` | shared  | Using NotebookLM for stable project context |
| `ml-engineer`    | dev     | LLM evals, RAG tuning, and LoRA fine-tuning |
| `data-analysis`  | shared  | SQL reporting, pandas, enterprise charting  |

### Other

| Skill                     | Profile | Description                                  |
| ------------------------- | ------- | -------------------------------------------- |
| `clean-code`              | shared  | Coding standards + SOLID + Karpathy (Global) |
| `behavioral-modes`        | shared  | Agent personas                               |
| `parallel-agents`         | shared  | Multi-agent patterns                         |
| `intelligent-routing`     | shared  | Auto agent selection                         |
| `prompt-engineering`      | shared  | System prompts, few-shot structures, LLMO    |
| `github-mcp`              | shared  | GitHub repository automation via MCP         |
| `mcp-builder`             | dev     | Model Context Protocol                       |
| `documentation-templates` | shared  | Doc formats                                  |
| `i18n-localization`       | dev     | Internationalization                         |
| `performance-profiling`   | shared  | Web Vitals, optimization                     |
| `systematic-debugging`    | shared  | Troubleshooting                              |

---

## 🎭 Profiles (3)

Project-type routing — determines which agents/skills are prioritized per project.

| Profile     | Agents         | Skills              | Use When                          |
| ----------- | -------------- | ------------------- | --------------------------------- |
| `dev`       | 10 engineering | 22 dev skills       | Software development projects     |
| `marketing` | 1 + shared     | 29 marketing skills | Marketing campaigns, CRO, content |
| `hybrid`    | All            | All (phase-based)   | Build product + grow it           |

Set `profile:` in brand's `context.md`. See `profiles/` for full listings.

---

## 🔄 Workflows (25)

Slash command procedures. Invoke with `/command`.

| Command             | Description               |
| ------------------- | ------------------------- |
| `/brainstorm`       | Socratic discovery        |
| `/create`           | Create new features       |
| `/create-prd`       | Product Requirements Doc  |
| `/debug`            | Debug issues              |
| `/deploy`           | Deploy application        |
| `/enhance`          | Improve existing code     |
| `/orchestrate`      | Multi-agent coordination  |
| `/plan`             | Task breakdown            |
| `/preview`          | Preview changes           |
| `/status`           | Check project status      |
| `/test`             | Run tests                 |
| `/ui-ux-pro-max`    | Design with 50 styles     |
| `/code-review`      | Technical code review     |
| `/code-review-fix`  | Fix review issues         |
| `/rca`              | Root cause analysis       |
| `/implement-fix`    | Implement fix from RCA    |
| `/piv-plan`         | Feature plan + analysis   |
| `/piv-prime`        | Prime codebase            |
| `/piv-execute`      | Execute PIV plan          |
| `/validate`         | Validate implementation   |
| `/execution-report` | Implementation report     |
| `/system-review`    | Review against plan       |
| `/update`           | Sync system after changes |
| `/audit-goals`      | Goal gap analysis         |
| `/system-check`     | System health check       |
| `/build-website`    | WordPress site build      |
| `/setup-listing`    | Platform listing setup    |
| `/local-seo-setup`  | Local SEO + GMB setup     |
| `/client-verify`    | Client data verification  |

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

| Skill           | Files | Coverage                         |
| --------------- | ----- | -------------------------------- |
| `ui-ux-pro-max` | 27    | 50 styles, 21 palettes, 50 fonts |
| `app-builder`   | 20    | Full-stack scaffolding           |

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

## 🏢 Brands & Industries

```plaintext
brands/
├── _industry-template/          # Copy for new industry
│   ├── _common/industry.md      # Industry knowledge
│   └── _brand-template/         # Copy for new brand
│       ├── context.md            # Brand identity (has profile: field)
│       ├── telos.md              # Telos tracker  (replaces todo.md)
│       ├── reference/            # Raw client data
│       └── brand-data/           # Processed assets
└── [industry]/[brand]/          # Actual brand folders
```

---

## 📖 Docs

| Document                        | Purpose                           |
| ------------------------------- | --------------------------------- |
| `docs/BUILDING-AGENTS.md`       | How to create agents              |
| `docs/BUILDING-SKILLS.md`       | How to create skills              |
| `docs/BUILDING-WORKFLOWS.md`    | How to create workflows           |
| `docs/COMBINING-COMPONENTS.md`  | How they work together            |
| `docs/workflow-coverage-map.md` | Full workflow→agent→skill mapping |

---

## 📊 Statistics

| Metric              | Value                         |
| ------------------- | ----------------------------- |
| **Total Agents**    | 26                            |
| **Total Skills**    | 93                            |
| **Total Workflows** | 30                            |
| **Profiles**        | 3 (dev, marketing, hybrid)    |
| **Total Scripts**   | 2 (master) + 18 (skill-level) |
| **Coverage**        | ~99% web/mobile/marketing     |

---

## 🔗 Quick Reference

| Need     | Agent                 | Skills                                 |
| -------- | --------------------- | -------------------------------------- |
| Web App  | `frontend-specialist` | nextjs-react-expert, frontend-design   |
| API      | `backend-specialist`  | api-patterns, nodejs-best-practices    |
| Mobile   | `mobile-developer`    | mobile-design, react-native-guidelines |
| Database | `database-architect`  | database-design, typeorm-patterns      |
| Security | `security-auditor`    | vulnerability-scanner                  |
| Testing  | `test-engineer`       | testing-patterns, webapp-testing       |
| Debug    | `debugger`            | systematic-debugging                   |
| Plan     | `project-planner`     | brainstorming, plan-writing            |
| SEO      | `seo-specialist`      | seo-audit, ai-seo, schema-markup       |
| Local SEO| `local-seo-manager`   | local-seo, google-my-business          |
| WordPress| `wordpress-site-builder` | wordpress-mcp-bundle, wordpress-site-build |
| Listings | `listing-automation`  | business-listing, client-communication |
| Client   | `client-coordinator`  | client-communication                   |
| Copy     | (skill-based)         | copywriting, copy-editing              |
| CRO      | (skill-based)         | page-cro, signup-flow-cro              |
| Ads      | (skill-based)         | paid-ads, ad-creative                  |
