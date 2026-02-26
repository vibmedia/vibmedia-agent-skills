# Vibmedia Agent Skills

> 🧠 Modular AI agent toolkit — **77 skills**, **21 agents**, **25 workflows** for Antigravity, Claude Code, and AI coding assistants.

Curated and merged from the best open-source AI skill repositories.

---

## 📦 Installation

### Option 1: Copy into your project (Recommended)

```bash
git clone https://github.com/vibmedia/vibmedia-agent-skills.git
cp -r vibmedia-agent-skills/* /path/to/your/project/.agent/
rm -rf vibmedia-agent-skills
```

### Option 2: Git Submodule

```bash
git submodule add https://github.com/vibmedia/vibmedia-agent-skills.git .agent
git submodule update --remote  # to update later
```

### Option 3: Symlink

```bash
git clone https://github.com/vibmedia/vibmedia-agent-skills.git ~/agent-skills
ln -s ~/agent-skills /path/to/your/project/.agent
```

### For Antigravity IDE

Place the contents at the root of your project as `.agent/`:

```bash
git clone https://github.com/vibmedia/vibmedia-agent-skills.git .agent
```

Antigravity will automatically detect and use the skills, agents, and workflows.

---

## 🏗️ Structure

```
.agent/
├── ARCHITECTURE.md          # Full system map
├── agents/                  # 21 Specialist AI personas
├── skills/                  # 77 Domain-specific skills
│   └── <skill>/
│       ├── SKILL.md         # Main instructions (required)
│       ├── references/      # Deep-dive docs (optional)
│       └── scripts/         # Automation scripts (optional)
├── workflows/               # 25 Slash command procedures
├── rules/                   # Global rules
└── scripts/                 # Master validation scripts
```

---

## 🤖 Agents (21)

| Agent | Focus |
|-------|-------|
| `orchestrator` | Multi-agent coordination |
| `project-planner` | Discovery, task planning |
| `frontend-specialist` | Web UI/UX |
| `backend-specialist` | API, business logic |
| `database-architect` | Schema, SQL |
| `mobile-developer` | iOS, Android, React Native |
| `game-developer` | Game logic, mechanics |
| `devops-engineer` | CI/CD, Docker |
| `security-auditor` | Security compliance |
| `penetration-tester` | Offensive security |
| `test-engineer` | Testing strategies |
| `debugger` | Root cause analysis |
| `performance-optimizer` | Speed, Web Vitals |
| `seo-specialist` | Ranking, visibility |
| `documentation-writer` | Manuals, docs |
| `product-manager` | Requirements, user stories |
| `product-owner` | Strategy, backlog, MVP |
| `qa-automation-engineer` | E2E testing, CI pipelines |
| `code-archaeologist` | Legacy code, refactoring |
| `code-reviewer` | Code quality review |
| `explorer-agent` | Codebase analysis |

---

## 🧩 Skills (77)

### Frontend & UI (6)
`react-best-practices` · `web-design-guidelines` · `composition-patterns` · `tailwind-patterns` · `frontend-design` · `ui-ux-pro-max`

### Backend & API (4)
`api-patterns` · `nestjs-expert` · `nodejs-best-practices` · `python-patterns`

### Database (3)
`database-design` · `prisma-expert` · `typeorm-patterns`

### Testing & Quality (8)
`testing-patterns` · `webapp-testing` · `tdd-workflow` · `code-review-checklist` · `requesting-code-review` · `receiving-code-review` · `verification-before-completion` · `lint-and-validate`

### Architecture & Planning (9)
`app-builder` · `architecture` · `plan-writing` · `brainstorming` · `executing-plans` · `subagent-driven-development` · `using-git-worktrees` · `finishing-a-development-branch` · `writing-skills`

### Security (2)
`vulnerability-scanner` · `red-team-tactics`

### SEO & Discovery (6)
`seo-fundamentals` · `geo-fundamentals` · `seo-audit` · `ai-seo` · `programmatic-seo` · `schema-markup`

### Marketing & CRO (25)
`page-cro` · `signup-flow-cro` · `onboarding-cro` · `form-cro` · `popup-cro` · `paywall-upgrade-cro` · `copywriting` · `copy-editing` · `cold-email` · `email-sequence` · `social-content` · `content-strategy` · `paid-ads` · `ad-creative` · `analytics-tracking` · `ab-test-setup` · `churn-prevention` · `free-tool-strategy` · `referral-program` · `marketing-ideas` · `marketing-psychology` · `launch-strategy` · `pricing-strategy` · `competitor-alternatives` · `product-marketing-context`

### Mobile (2)
`mobile-design` · `react-native-guidelines`

### Infrastructure (3)
`deployment-procedures` · `server-management` · `docker-expert`

### Shell & CLI (2)
`bash-linux` · `powershell-windows`

### Other (11)
`clean-code` · `behavioral-modes` · `parallel-agents` · `mcp-builder` · `documentation-templates` · `i18n-localization` · `performance-profiling` · `systematic-debugging` · `game-development` · `typescript-expert` · `intelligent-routing`

---

## 🔄 Workflows (25)

Invoke with `/command` in your AI assistant:

| Command | Description |
|---------|-------------|
| `/brainstorm` | Socratic discovery |
| `/create` | Create new features |
| `/create-prd` | Create Product Requirements Document |
| `/debug` | Debug issues |
| `/deploy` | Deploy application |
| `/enhance` | Improve existing code |
| `/orchestrate` | Multi-agent coordination |
| `/plan` | Task breakdown |
| `/preview` | Preview changes |
| `/status` | Check project status |
| `/test` | Run tests |
| `/ui-ux-pro-max` | Design with 50 styles |
| `/code-review` | Technical code review |
| `/code-review-fix` | Fix code review issues |
| `/implement-fix` | Implement fix from RCA |
| `/rca` | Root cause analysis |
| `/execution-report` | Implementation report |
| `/system-review` | Analyze against plan |
| `/piv-plan` | Feature plan with analysis |
| `/piv-prime` | Prime agent with codebase |
| `/piv-execute` | Execute PIV plan |
| `/validate` | Validate implementation |
| `/update` | Sync system after changes |
| `/audit-goals` | Find gaps in goals vs capabilities |
| `/system-check` | System health check |

---

## 🚀 How Skills Work

```
User Request → Match skill by description → Load SKILL.md
                                               ↓
                                        Read references/
                                               ↓
                                        Execute scripts/
```

1. **Agent routing** — Your AI assistant matches the request to the best agent
2. **Skill loading** — The agent loads relevant skills based on frontmatter descriptions
3. **Reference docs** — Deep-dive references are loaded on-demand
4. **Scripts** — Validation and audit scripts run when needed

---

## 📊 Stats

| Metric | Count |
|--------|-------|
| Agents | 21 |
| Skills | 77 |
| Workflows | 25 |
| Reference Files | 20+ |
| Validation Scripts | 20 |

---

## 🙌 Sources & Credits

| Source | What It Contributed |
|--------|-------------------|
| [obra/superpowers](https://github.com/obra/superpowers) | TDD, debugging, plan execution, parallel agents, code review |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | React best practices, composition patterns, React Native, web design |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | 29 marketing skills (CRO, copywriting, SEO, ads, analytics, growth) |
| [LeCoupa/awesome-cheatsheets](https://github.com/LeCoupa/awesome-cheatsheets) | Language & tool cheatsheets (Node, Bash, Python, React, Docker, Git) |
| [ramziddin/solid-skills](https://github.com/ramziddin/solid-skills) | SOLID principles, design patterns, code smells |
| [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | Karpathy's 4 coding principles |

---

## 📄 License

MIT
