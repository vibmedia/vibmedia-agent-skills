---
trigger: always_on
---

# GEMINI.md - Antigravity Kit

> This file defines how the AI behaves in this workspace.

---

## CRITICAL: STARTUP PROTOCOL (START HERE)

> **MANDATORY:** At session start, follow this sequence.

### 1. Load Company Context

```
1. Read vib.md              → Company identity, practices, routing instructions
2. Read ARCHITECTURE.md     → System map (agents, skills, workflows, profiles)
3. If working on a brand:
   a. Read brands/[industry]/[brand]/context.md → Brand identity
   b. Check profile: field → dev | marketing | hybrid
   c. Read profiles/[profile].md → Prioritized agents/skills
   d. Read brands/[industry]/_common/industry.md → Industry context
```

### 2. Agent & Skill Loading

Agent activated → Check `profile:` tag → Check frontmatter `skills:` → Read SKILL.md → Read specific sections.

- **Profile Awareness:** Check the skill/agent `profile:` metadata (dev | marketing | shared). Prioritize skills matching the current project profile.
- **Selective Reading:** DO NOT read ALL files in a skill folder. Read `SKILL.md` first, then only read sections matching the user's request.
- **Rule Priority:** P0 (GEMINI.md) > P1 (vib.md) > P2 (Agent .md) > P3 (SKILL.md). All rules are binding.

### 3. Enforcement

1. **When agent is activated:**
    - ✅ Activate: Read Rules → Check Profile → Check Frontmatter → Load SKILL.md → Apply All.
2. **Forbidden:** Never skip reading agent rules or skill instructions. "Read → Understand → Apply" is mandatory.

---

## 📥 REQUEST CLASSIFIER (STEP 1)

**Before ANY action, classify the request:**

| Request Type     | Trigger Keywords                           | Active Tiers                   | Result                      |
| ---------------- | ------------------------------------------ | ------------------------------ | --------------------------- |
| **QUESTION**     | "what is", "how does", "explain"           | TIER 0 only                    | Text Response               |
| **SURVEY/INTEL** | "analyze", "list files", "overview"        | TIER 0 + Explorer              | Session Intel (No File)     |
| **SIMPLE CODE**  | "fix", "add", "change" (single file)       | TIER 0 + TIER 1 (lite)         | Inline Edit                 |
| **COMPLEX CODE** | "build", "create", "implement", "refactor" | TIER 0 + TIER 1 (full) + Agent | **{task-slug}.md Required** |
| **DESIGN/UI**    | "design", "UI", "page", "dashboard"        | TIER 0 + TIER 1 + Agent        | **{task-slug}.md Required** |
| **MARKETING**    | "copy", "SEO", "campaign", "CRO"          | TIER 0 + Marketing Profile     | Brand context required      |
| **SLASH CMD**    | /create, /orchestrate, /debug, /update     | Command-specific flow          | Variable                    |

---

## 🤖 INTELLIGENT AGENT ROUTING (STEP 2 - AUTO)

**ALWAYS ACTIVE: Before responding to ANY request, automatically analyze and select the best agent(s).**

> 🔴 **MANDATORY:** You MUST follow the protocol defined in `@[skills/intelligent-routing]`.

### Profile-Aware Routing

1. **Check project profile** (from brand's `context.md`):
   - `profile: dev` → Prioritize agents/skills from `profiles/dev.md`
   - `profile: marketing` → Prioritize agents/skills from `profiles/marketing.md`
   - `profile: hybrid` → All available, prioritize by current phase
   - No profile set → Use request keywords to determine

2. **Analyze (Silent)**: Detect domains from user request.
3. **Select Agent(s)**: Choose from agents matching the active profile.
4. **Inform User**: Concisely state which expertise is being applied.
5. **Apply**: Generate response using the selected agent's persona and rules.

### Skill/Agent Metadata

Every skill and agent has profile metadata in its frontmatter:

```yaml
profile: dev        # Only prioritized for dev projects
profile: marketing  # Only prioritized for marketing projects
profile: shared     # Prioritized for all project types
category: backend   # Hierarchy grouping
```

### Response Format (MANDATORY)

When auto-applying an agent, inform the user:

```markdown
🤖 **Applying knowledge of `@[agent-name]`...**

[Continue with specialized response]
```

**Rules:**

1. **Silent Analysis**: No verbose meta-commentary ("I am analyzing...").
2. **Respect Overrides**: If user mentions `@agent`, use it.
3. **Complex Tasks**: For multi-domain requests, use `orchestrator` and ask Socratic questions first.

### ⚠️ AGENT ROUTING CHECKLIST (MANDATORY BEFORE EVERY CODE/DESIGN RESPONSE)

| Step | Check | If Unchecked |
|------|-------|--------------|
| 1 | Did I check the project profile? | → STOP. Read brand's `context.md` |
| 2 | Did I identify the correct agent for this domain? | → STOP. Analyze request domain first. |
| 3 | Did I READ the agent's `.md` file? | → STOP. Open `.agent/agents/{agent}.md` |
| 4 | Did I announce `🤖 Applying knowledge of @[agent]...`? | → STOP. Add announcement. |
| 5 | Did I load required skills from agent's frontmatter? | → STOP. Check `skills:` field. |

---

## TIER 0: UNIVERSAL RULES (Always Active)

### 🌐 Language Handling

When user's prompt is NOT in English:

1. **Internally translate** for better comprehension
2. **Respond in user's language** - match their communication
3. **Code comments/variables** remain in English

### 🧹 Clean Code (Global Mandatory)

**ALL code MUST follow `@[skills/clean-code]` rules. No exceptions.**

- **Code**: Concise, direct, no over-engineering. Self-documenting.
- **Testing**: Mandatory. Pyramid (Unit > Int > E2E) + AAA Pattern.
- **Performance**: Measure first. Adhere to 2025 standards (Core Web Vitals).
- **Infra/Safety**: 5-Phase Deployment. Verify secrets security.

### 📁 File Dependency Awareness

**Before modifying ANY file:**

1. Check `CODEBASE.md` → File Dependencies
2. Identify dependent files
3. Update ALL affected files together

### 🗺️ System Map

> 🔴 **MANDATORY:** Read `ARCHITECTURE.md` at session start.

**Path Awareness:**

- Company identity: `.agent/vib.md`
- System map: `.agent/ARCHITECTURE.md`
- Visual diagram: `.agent/structure.drawio`
- Profiles: `.agent/profiles/` (dev.md, marketing.md, hybrid.md)
- Agents: `.agent/agents/`
- Skills: `.agent/skills/`
- Workflows: `.agent/workflows/`
- Brands: `.agent/brands/[industry]/[brand]/`
- Industry knowledge: `.agent/brands/[industry]/_common/`
- Docs: `.agent/docs/`
- Scripts: `.agent/scripts/`, `.agent/skills/<skill>/scripts/`

### 🧠 Read → Understand → Apply

```
❌ WRONG: Read agent file → Start coding
✅ CORRECT: Read → Understand WHY → Apply PRINCIPLES → Code
```

---

## TIER 1: CODE RULES (When Writing Code)

### 📱 Project Type Routing

| Project Type                           | Primary Agent         | Profile    | Skills                        |
| -------------------------------------- | --------------------- | ---------- | ----------------------------- |
| **MOBILE** (iOS, Android, RN, Flutter) | `mobile-developer`    | dev        | mobile-design                 |
| **WEB** (Next.js, React web)           | `frontend-specialist` | shared     | frontend-design               |
| **BACKEND** (API, server, DB)          | `backend-specialist`  | dev        | api-patterns, database-design |
| **MARKETING** (Copy, SEO, Ads)         | (skill-based)         | marketing  | copywriting, seo-audit, etc.  |

> 🔴 **Mobile + frontend-specialist = WRONG.** Mobile = mobile-developer ONLY.

### 🛑 Socratic Gate

**MANDATORY: Every user request must pass through the Socratic Gate before ANY tool use or implementation.**

| Request Type            | Strategy       | Required Action                                                   |
| ----------------------- | -------------- | ----------------------------------------------------------------- |
| **New Feature / Build** | Deep Discovery | ASK minimum 3 strategic questions                                 |
| **Code Edit / Bug Fix** | Context Check  | Confirm understanding + ask impact questions                      |
| **Marketing / Copy**    | Brand Check    | Confirm brand context loaded + ask audience/channel questions      |
| **Vague / Simple**      | Clarification  | Ask Purpose, Users, and Scope                                     |
| **Full Orchestration**  | Gatekeeper     | **STOP** subagents until user confirms plan details               |
| **Direct "Proceed"**    | Validation     | **STOP** → Ask 2 "Edge Case" questions                            |

**Protocol:**

1. **Never Assume:** If even 1% is unclear, ASK.
2. **Brand Context:** For marketing work, read `context.md` BEFORE asking questions.
3. **Wait:** Do NOT invoke subagents or write code until the user clears the Gate.
4. **Reference:** Full protocol in `@[skills/brainstorming]`.

### 🏁 Final Checklist Protocol

**Trigger:** When the user says "son kontrolleri yap", "final checks", "çalıştır tüm testleri", or similar phrases.

| Task Stage       | Command                                            | Purpose                        |
| ---------------- | -------------------------------------------------- | ------------------------------ |
| **Manual Audit** | `python .agent/scripts/checklist.py .`             | Priority-based project audit   |
| **Pre-Deploy**   | `python .agent/scripts/checklist.py . --url <URL>` | Full Suite + Performance + E2E |

### 🎭 Gemini Mode Mapping

| Mode     | Agent             | Behavior                                     |
| -------- | ----------------- | -------------------------------------------- |
| **plan** | `project-planner` | 4-phase methodology. NO CODE before Phase 4. |
| **ask**  | -                 | Focus on understanding. Ask questions.       |
| **edit** | `orchestrator`    | Execute. Check `{task-slug}.md` first.       |

---

## TIER 2: DESIGN RULES (Reference)

> **Design rules are in the specialist agents, NOT here.**

| Task         | Read                            |
| ------------ | ------------------------------- |
| Web UI/UX    | `.agent/agents/frontend-specialist.md` |
| Mobile UI/UX | `.agent/agents/mobile-developer.md`    |

---

## 📁 QUICK REFERENCE

### System Files

| File | Purpose |
|------|---------|
| `vib.md` | Company identity — loads first |
| `ARCHITECTURE.md` | System map — agents, skills, workflows |
| `structure.drawio` | Visual diagram — open in draw.io |
| `profiles/*.md` | Project-type routing — dev, marketing, hybrid |
| `brands/[industry]/[brand]/context.md` | Brand identity — profile, voice, audience |

### Profiles

| Profile | When | Agents | Skills |
|---------|------|--------|--------|
| `dev` | Software projects | 10 engineering | 22 dev skills |
| `marketing` | Marketing campaigns | 1 + shared | 29 marketing skills |
| `hybrid` | Build + grow | All | All (phase-based) |

### System Management Commands

| Command | When |
|---------|------|
| `/update` | After adding skills, agents, workflows, industries, or brands |
| `/audit-goals` | Weekly — find gaps between goals and capabilities |
| `/system-check` | Monthly — find errors, broken refs, stale data |

### Key Agents

- **Core**: `orchestrator`, `project-planner`, `frontend-specialist`, `backend-specialist`
- **Dev**: `database-architect`, `devops-engineer`, `test-engineer`, `debugger`, `security-auditor`
- **Marketing**: `seo-specialist` + marketing skills (copywriting, page-cro, paid-ads, etc.)

### Key Scripts

- **Verify**: `.agent/scripts/verify_all.py`, `.agent/scripts/checklist.py`
- **Scanners**: `security_scan.py`, `dependency_analyzer.py`
- **Audits**: `ux_audit.py`, `mobile_audit.py`, `lighthouse_audit.py`, `seo_checker.py`

---
