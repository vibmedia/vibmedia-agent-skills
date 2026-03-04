# Vibmedia Agent Skills

> 🧠 Modular AI agent toolkit — **86 skills**, **21 agents**, **26 workflows**, **3 project profiles** for Antigravity, Claude Code, and AI coding assistants.

Curated and merged from the best open-source AI skill repositories.

**[📖 Installation Guide →](INSTALL.md)** · **[🏗️ Architecture →](ARCHITECTURE.md)** · **[📋 How to Use →](GUIDE.md)** · **[🚀 Roadmap →](ROADMAP.md)**

---

## 📦 Quick Install

```bash
# Clone into your project
git clone https://github.com/vibmedia/vibmedia-agent-skills.git .agent
```

See [INSTALL.md](INSTALL.md) for detailed setup across different IDEs and CLI tools.

---

## 🏗️ Structure

```
.agent/
├── vib.md                   # Company identity (loads first)
├── ARCHITECTURE.md          # Full system map
├── structure.drawio         # Visual diagram (open in draw.io)
├── profiles/                # Project-type routing
│   ├── dev.md               # Dev skills prioritized
│   ├── marketing.md         # Marketing skills prioritized
│   └── hybrid.md            # Both (phase-based)
├── agents/                  # 21 Specialist AI personas
├── skills/                  # 77 Domain skills (tagged: dev|marketing|shared)
│   └── <skill>/
│       ├── SKILL.md         # Main instructions (required)
│       ├── references/      # Deep-dive docs (optional)
│       └── scripts/         # Automation scripts (optional)
├── workflows/               # 25 Slash command procedures
├── brands/                  # Industry → Brand context folders
│   └── <industry>/
│       ├── _common/         # Shared industry knowledge
│       └── <brand>/
│           ├── context.md   # Brand identity (profile: dev|marketing|hybrid)
│           ├── todo.md      # Progress + decisions
│           ├── structure.drawio  # Visual project map
│           ├── reference/   # Raw client data
│           ├── brand-data/  # Processed assets
│           └── artifacts/   # AI deliverables
├── docs/                    # How-to guides
├── rules/                   # Global rules
└── scripts/                 # Master validation scripts
```

---

## 🎭 Profiles

Project-type routing — controls which agents/skills are prioritized.

| Profile     | Skills                   | Use When                |
| ----------- | ------------------------ | ----------------------- |
| `dev`       | 22 dev + 27 shared       | Software development    |
| `marketing` | 29 marketing + 27 shared | Campaigns, CRO, content |
| `hybrid`    | All 79 (phase-based)     | Build product + grow it |

Set `profile:` in your brand's `context.md`.

---

## 🤖 Agents (21)

| Agent                    | Focus                      | Profile   |
| ------------------------ | -------------------------- | --------- |
| `orchestrator`           | Multi-agent coordination   | shared    |
| `project-planner`        | Discovery, task planning   | shared    |
| `frontend-specialist`    | Web UI/UX                  | shared    |
| `backend-specialist`     | API, business logic        | dev       |
| `database-architect`     | Schema, SQL                | dev       |
| `mobile-developer`       | iOS, Android, React Native | shared    |
| `game-developer`         | Game logic, mechanics      | shared    |
| `devops-engineer`        | CI/CD, Docker              | dev       |
| `security-auditor`       | Security compliance        | dev       |
| `penetration-tester`     | Offensive security         | dev       |
| `test-engineer`          | Testing strategies         | dev       |
| `debugger`               | Root cause analysis        | dev       |
| `performance-optimizer`  | Speed, Web Vitals          | shared    |
| `seo-specialist`         | Ranking, visibility        | marketing |
| `documentation-writer`   | Manuals, docs              | shared    |
| `product-manager`        | Requirements, user stories | shared    |
| `product-owner`          | Strategy, backlog, MVP     | shared    |
| `qa-automation-engineer` | E2E testing, CI pipelines  | dev       |
| `code-archaeologist`     | Legacy code, refactoring   | dev       |
| `code-reviewer`          | Code quality review        | dev       |
| `explorer-agent`         | Codebase analysis          | shared    |

---

## 🧩 Skills (79)

### Frontend & UI (7) — shared

`nextjs-react-expert` · `web-design-guidelines` · `composition-patterns` · `tailwind-patterns` · `frontend-design` · `ui-ux-pro-max` · `design-system-architecture`

### Backend & API (4) — dev

`api-patterns` · `nodejs-best-practices` · `python-patterns` · `rust-pro`

### Database (2) — dev

`database-design` · `typeorm-patterns`

### Web3 & Crypto (1) — dev

`web3-smart-contracts`

### Testing & Quality (8) — dev

`testing-patterns` · `webapp-testing` · `tdd-workflow` · `code-review-checklist` · `requesting-code-review` · `receiving-code-review` · `verification-before-completion` · `lint-and-validate`

### Architecture & Planning (10) — shared

`app-builder` · `architecture` · `plan-writing` · `brainstorming` · `executing-plans` · `subagent-driven-development` · `using-git-worktrees` · `finishing-a-development-branch` · `writing-skills` · `notebooklm-rag`

### Security (2) — dev

`vulnerability-scanner` · `red-team-tactics`

### SEO & Discovery (6) — marketing

`seo-fundamentals` · `geo-fundamentals` · `seo-audit` · `ai-seo` · `programmatic-seo` · `schema-markup`

### Marketing & CRO (25) — marketing

`page-cro` · `signup-flow-cro` · `onboarding-cro` · `form-cro` · `popup-cro` · `paywall-upgrade-cro` · `copywriting` · `copy-editing` · `cold-email` · `email-sequence` · `social-content` · `content-strategy` · `paid-ads` · `ad-creative` · `analytics-tracking` · `ab-test-setup` · `churn-prevention` · `free-tool-strategy` · `referral-program` · `marketing-ideas` · `marketing-psychology` · `launch-strategy` · `pricing-strategy` · `competitor-alternatives` · `product-marketing-context`

### Mobile (2) — shared

`mobile-design` · `react-native-guidelines`

### Infrastructure (3) — dev

`deployment-procedures` · `server-management` · `cloud-infrastructure`

### Shell & CLI (2) — shared

`bash-linux` · `powershell-windows`

### AI & Data (4) — dev/shared

`notebooklm-rag` · `ml-engineer` · `data-analysis` · `github-mcp`

### Other (10) — shared/dev

`clean-code` · `behavioral-modes` · `parallel-agents` · `intelligent-routing` · `prompt-engineering` · `mcp-builder` · `documentation-templates` · `i18n-localization` · `performance-profiling` · `systematic-debugging`

### Game (1) — shared

`game-development`

---

## 🔄 Workflows (26)

| Command             | Description                   |
| ------------------- | ----------------------------- |
| `/brainstorm`       | Socratic discovery            |
| `/create`           | Create new features           |
| `/create-prd`       | Product Requirements Document |
| `/debug`            | Debug issues                  |
| `/deploy`           | Deploy application            |
| `/enhance`          | Improve existing code         |
| `/orchestrate`      | Multi-agent coordination      |
| `/plan`             | Task breakdown                |
| `/preview`          | Preview changes               |
| `/status`           | Check project status          |
| `/test`             | Run tests                     |
| `/ui-ux-pro-max`    | Design with 50 styles         |
| `/code-review`      | Technical code review         |
| `/code-review-fix`  | Fix code review issues        |
| `/implement-fix`    | Implement fix from RCA        |
| `/rca`              | Root cause analysis           |
| `/execution-report` | Implementation report         |
| `/system-review`    | Analyze against plan          |
| `/piv-plan`         | Feature plan with analysis    |
| `/piv-prime`        | Prime agent with codebase     |
| `/validate`         | Validate implementation       |
| `/update`           | Sync system after changes     |
| `/audit-goals`      | Goal gap analysis             |
| `/system-check`     | System health check           |

---

## 📖 Documentation

| Document                                                     | Purpose                                 |
| ------------------------------------------------------------ | --------------------------------------- |
| [INSTALL.md](INSTALL.md)                                     | Installation guide for all environments |
| [GUIDE.md](GUIDE.md)                                         | How to use — workflows, commands, tips  |
| [ARCHITECTURE.md](ARCHITECTURE.md)                           | Full system map with all components     |
| [ROADMAP.md](ROADMAP.md)                                     | Enterprise AI workforce roadmap         |
| [docs/BUILDING-AGENTS.md](docs/BUILDING-AGENTS.md)           | How to create agents                    |
| [docs/BUILDING-SKILLS.md](docs/BUILDING-SKILLS.md)           | How to create skills                    |
| [docs/BUILDING-WORKFLOWS.md](docs/BUILDING-WORKFLOWS.md)     | How to create workflows                 |
| [docs/COMBINING-COMPONENTS.md](docs/COMBINING-COMPONENTS.md) | How they work together                  |
| [brands/README.md](brands/README.md)                         | Brand & industry context system         |

---

## 📊 Stats

| Metric             | Count |
| ------------------ | ----- |
| Agents             | 21    |
| Skills             | 86    |
| Workflows          | 26    |
| Profiles           | 3     |
| Reference Files    | 60+   |
| Validation Scripts | 20    |

---

## 🙌 Sources & Credits

| Source                                                                                        | What It Contributed                                                  |
| --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| [obra/superpowers](https://github.com/obra/superpowers)                                       | TDD, debugging, plan execution, parallel agents, code review         |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)                       | React best practices, composition patterns, React Native, web design |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)             | 29 marketing skills (CRO, copywriting, SEO, ads, analytics, growth)  |
| [LeCoupa/awesome-cheatsheets](https://github.com/LeCoupa/awesome-cheatsheets)                 | Language & tool cheatsheets (Node, Bash, Python, React, Docker, Git) |
| [ramziddin/solid-skills](https://github.com/ramziddin/solid-skills)                           | SOLID principles, design patterns, code smells                       |
| [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | Karpathy's 4 coding principles                                       |

---

## 📄 License

MIT
