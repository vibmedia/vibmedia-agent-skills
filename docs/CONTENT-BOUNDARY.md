# Content Boundary Rule

> **MANDATORY** — Governs what goes into framework files vs. brand/industry files.
> This rule prevents project-specific data from leaking into the generic, reusable framework.

---

## The Rule (One Line)

**Framework files are templates. Brand files are instances. Never put instance data in templates.**

---

## What Goes Where

| Content Type | Location | Example |
|-------------|----------|---------|
| **Processes** (how to do something) | `skills/`, `agents/`, `workflows/` | "Run Golden Run → Crystallize → Execute" |
| **Patterns** (reusable templates) | `skills/`, `agents/`, `workflows/` | OTP flow protocol, NAP consistency rules |
| **Placeholders** (where to plug data) | `skills/`, `agents/`, `workflows/` | `[platform]`, `[city]`, `[business license]` |
| **Platform names** (specific services) | `brands/[industry]/_common/industry.md` | Zomato, Swiggy, DoorDash, Amazon |
| **Country data** (regulations, directories) | `brands/[industry]/_common/industry.md` | FSSAI, GSTIN, Justdial, Sulekha |
| **Client data** (names, URLs, credentials) | `brands/[industry]/[brand]/context.md` | "cachandnichopra.com", "Raj's Kitchen" |
| **Project output** (code, deliverables, copy) | **Outside** `.agent/` (Project Root) | `src/`, `docs/`, `public/`, `project-copy.md` |
| **Project PRDs/Plans** | **Outside** `.agent/` (Project Root) | `.claude/`, `docs/`, root directory |
| **Executables/Utilities** (pings, checks, automations) | `scripts/` (`.py`, `.sh`) | `checklist.py`, `wordpress_checklist.py` |

---

## The Hybrid Approach (Markdown & Scripts)

> **VIBHOR'S RULE OF TRUTH:** The `.agent` system and all project logic runs on Markdown (`.md`). Python (`.py`) scripts are strictly edge-case tools, never the master plan.

1. **When to use Markdown (`.md`) - ALWAYS DEFAULT HERE**
   - Project goals, plans, and task trackers (`task.md`, `implementation_plan.md`).
   - Manual checklists and standard operating procedures (SOPs).
   - Rules, architecture, and brand definitions.
   - *If a human needs to read it to understand context, it belongs in Markdown.*

2. **When to use Scripts (`.py` / `.sh`) - EXCEPTIONS ONLY**
   - When a task requires an HTTP request, SSL ping, or API call that raw text cannot compute.
   - When running automated Regex scans across thousands of files (e.g., `verify_boundary.py`).
   - When programmatically scraping or parsing a live URL.
   - *Scripts must only execute discrete mechanical actions and report back to the AI/Human; they do not hold project truth or goals.*

---

## Framework File Rules

### ✅ ALLOWED in framework files (`agents/`, `skills/`, `workflows/`)

- Generic process steps and checklists
- Decision-making frameworks with `[placeholder]` tokens
- Category-level examples: "food delivery platforms", "e-commerce marketplaces"
- Universal tools: Google My Business, Facebook, Bing Places (global platforms)
- Delegation instructions: "load details from `brands/[industry]/_common/industry.md`"
- Template structures with `[placeholder]` values

### ❌ FORBIDDEN in framework files

- Specific platform names that are regional (Zomato, Swiggy, Justdial)
- Country-specific regulations (FSSAI, GSTIN, ABN, EIN)
- Real addresses, phone numbers, business names
- Client URLs, domain names, credentials
- Regional directories (Sulekha, IndiaMART, TradeIndia)
- Currency-specific examples (₹, prices in INR)

### ❌ FORBIDDEN in `.agent/brands/` (Brand/Industry folders)

- Deliverables meant for the project (e.g., actual source code, final website copy, compiled assets)
- These belong OUTSIDE the `.agent/` folder in the main project workspace.

### 🟡 GRAY AREA (use judgment)

- Global platforms (Amazon, Google, Facebook) → Allowed as **examples**, but frame as "e.g., Amazon" not "Amazon is required"
- Industry-generic terms (restaurant, salon, plumber) → Allowed as category examples
- Common document types (tax ID, business license) → Use generic terms, not country names

---

## Industry Template Sections

When project-specific knowledge is learned during a project, it goes here:

```
brands/[industry]/_common/industry.md
├── Industry Overview
├── Key Terminology
├── Industry Benchmarks
├── Technical Considerations
├── Platform & Listing Sources     ← NEW: Where platforms go
├── Local SEO & Citation Sources   ← NEW: Where citation sources go
├── Regulatory Requirements        ← NEW: Country-specific licenses
├── Customer Insights
├── Marketing Patterns
└── AI Instructions for This Industry
```

---

## Upgrade Workflow: Learning from Projects

When upgrading the framework based on project learnings:

```
1. IDENTIFY what was learned
   ├── Is it a PROCESS? (how to do something)     → Goes in skill/agent/workflow
   ├── Is it a PLATFORM? (specific service)        → Goes in industry.md
   ├── Is it a REGULATION? (country-specific rule)  → Goes in industry.md
   └── Is it CLIENT DATA? (specific to one brand)  → Goes in brand/context.md

2. WRITE framework changes using ONLY placeholders
   ├── Use [platform], [city], [document type], [business name]
   ├── Reference: "load from brands/[industry]/_common/industry.md"
   └── Category-level examples ONLY (e.g., "food delivery", "e-commerce")

3. VERIFY before commit
   ├── Grep for project-specific terms (client names, local platforms, addresses)
   ├── Run: grep -rl "[term]" agents/ skills/ workflows/ profiles/
   └── If any matches → fix before committing
```

---

## Pre-Commit Verification

Before committing changes to framework files, always run:

```bash
# Quick check — should return nothing for framework files
grep -rl "[PROJECT_TERMS]" agents/ skills/ workflows/ profiles/ --include="*.md"
```

Where `[PROJECT_TERMS]` are the client/project-specific names from the current engagement.

The `/update` workflow should include this check automatically.

---

## Output Generation Rule (Where to write files)

When writing or generating files for the user:

1. **Context & Knowledge → INSIDE `.agent/`**
   - Save brand guidelines, industry benchmarks, and platform rules to `brands/[industry]/[brand]/context.md` or `brands/[industry]/_common/industry.md`.
2. **Framework logic → INSIDE `.agent/`**
   - Save generic reusable skills, agents, and workflows to `skills/`, `agents/`, `workflows/`.
3. **Project Deliverables & Code → OUTSIDE `.agent/`**
   - Save actual code (`src/`), generated marketing copy, website content, PRDs, and deliverables in the **Project Root** (outside the `.agent` folder). NEVER save project outputs inside `.agent/brands/.../artifacts/`.
   - The `.agent/` folder is a framework and knowledge base, NOT a build directory.

---

## For AI Agents: Self-Check Before Writing

Before writing to ANY file in `agents/`, `skills/`, or `workflows/`:

> **Ask yourself:** "Would this sentence make sense for a different client, in a different country, in a different industry?"
>
> - If YES → write it
> - If NO → it belongs in `brands/[industry]/_common/` or `brands/[industry]/[brand]/`

---

*This rule is P0 priority — same level as GEMINI.md.*
