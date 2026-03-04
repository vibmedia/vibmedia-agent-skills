# Installation Guide

> Set up VibMedia Agent Skills in any IDE or CLI that supports `.agent/` or `.claude/` configuration.

---

## Quick Install (2 minutes)

```bash
# Clone into your project's .agent directory
git clone https://github.com/vibmedia/vibmedia-agent-skills.git .agent
```

That's it. Open your project in Antigravity, Claude Code, or any compatible AI IDE.

---

## Supported Environments

| Environment     | Config Path             | How It Works                 |
| --------------- | ----------------------- | ---------------------------- |
| **Antigravity** | `.agent/`               | Auto-detects on project open |
| **Claude Code** | `.agent/` or `.claude/` | Reads GEMINI.md + skills     |
| **Cursor**      | `.agent/`               | Manual reference in rules    |
| **Windsurf**    | `.agent/`               | Manual reference in rules    |
| **CLI tools**   | `.agent/`               | Point config to skill files  |

---

## 🧠 NotebookLM RAG Integration

VibMedia Agent Skills uses NotebookLM as a stable knowledge base via `notebooklm-mcp-cli`. This allows agents to query complex docs without exhausting context windows.

### 1. Install & Authenticate (Globally)

```bash
pip install notebooklm-mcp-cli
nlm login         # Authenticate in browser
nlm setup add antigravity  # Configure MCP
```

_Note: Tokens expire every few weeks. Re-run `nlm login` when authentication fails._

### Deployment Scenarios

#### Scenario A: Local Development

Install globally via `pip` on your host machine. Any local project using Antigravity will automatically use the MCP server configured in `~/.gemini/antigravity/mcp_config.json`.

#### Scenario B: Headless / SSH Servers

`nlm login` requires a browser. To install on a headless server:

1. Run `nlm login` on your local machine.
2. Copy the auth folder `~/.notebooklm/` to your server.
3. Install the pip package on the server and use it headless.

---

## Step-by-Step Setup

### 1. Clone the Repo

**Into an existing project:**

```bash
cd your-project
git clone https://github.com/vibmedia/vibmedia-agent-skills.git .agent
```

**As a standalone workspace:**

```bash
mkdir my-workspace && cd my-workspace
git clone https://github.com/vibmedia/vibmedia-agent-skills.git .agent
```

### 2. Configure Company Identity

Edit `vib.md` with your company practices:

```bash
# Open and fill in the bracketed sections
nano .agent/vib.md
```

### 3. Set Up Your First Brand

```bash
# Create an industry (if it doesn't exist)
cp -r .agent/brands/_industry-template .agent/brands/saas

# Create a brand within the industry
cp -r .agent/brands/saas/_brand-template .agent/brands/saas/my-client

# Fill in brand context
nano .agent/brands/saas/my-client/context.md
```

### 4. Start Working

```bash
# Open your IDE and start using slash commands
/plan        # Plan a feature
/create      # Build something new
/debug       # Debug an issue
```

---

## Updating

Pull the latest skills and agents:

```bash
cd .agent
git pull origin main
```

After updating, run the sync workflow:

```
/update
```

---

## Directory After Install

```
your-project/
├── .agent/                      ← This repo
│   ├── vib.md                   # Your company identity
│   ├── ARCHITECTURE.md          # System map
│   ├── structure.drawio         # Visual diagram (open in draw.io)
│   ├── profiles/                # dev.md, marketing.md, hybrid.md
│   ├── agents/                  # 21 specialist agents
│   ├── skills/                  # 77 domain skills
│   ├── workflows/               # 25 slash commands
│   ├── brands/                  # Industry → Brand folders
│   ├── docs/                    # How-to guides
│   └── scripts/                 # Validation scripts
├── src/                         ← Your project code
└── ...
```

---

## Customization

### Adding Your Own Skills

See `docs/BUILDING-SKILLS.md`

### Adding Your Own Agents

See `docs/BUILDING-AGENTS.md`

### Adding Your Own Workflows

See `docs/BUILDING-WORKFLOWS.md`

### After Any Addition

Run `/update` to sync counts and validate the system.

---

## Troubleshooting

| Problem                | Fix                                        |
| ---------------------- | ------------------------------------------ |
| AI doesn't load skills | Check `.agent/` is in project root         |
| Wrong agent selected   | Use `@agent-name` to force selection       |
| Skills not found       | Run `/system-check` to find broken refs    |
| Counts wrong           | Run `/update` to sync                      |
| Old data               | Run `git pull` in `.agent/` then `/update` |

---

## Uninstall

```bash
rm -rf .agent
```
