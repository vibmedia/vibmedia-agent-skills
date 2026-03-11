# VibMedia — Company Identity

> This file loads at the start of every conversation. It defines who we are, how we work, and our standards.

---

## Company Overview

- **Company:** [VibMedia]
- **What we do:** [Brief — e.g., "We build products and run marketing for startups and SMBs"]
- **Industries served:** [All — tech, ecommerce, healthcare, hospitality, etc.]
- **Role:** Forward deployed engineer — automating workflows with AI agents
- **Team:** Solo operator (expanding)

### 🧹 Clean Code (Global Mandatory)

**ALL code MUST follow `@[skills/clean-code]` rules. No exceptions.**

- **Code**: Concise, direct, no over-engineering. Self-documenting.
- **Testing**: Mandatory. Pyramid (Unit > Int > E2E) + AAA Pattern.
- **Performance**: Measure first. Adhere to 2025 standards (Core Web Vitals).
- **Infra/Safety**: 5-Phase Deployment. Verify secrets security.

### 🛡️ CONTENT BOUNDARY RULE (Global Mandatory)

**MANDATORY: You MUST abide by `.agent/docs/CONTENT-BOUNDARY.md` at all times.**

- **Generic Framework:** `agents/`, `skills/`, `workflows/` MUST BE 100% GENERIC.
  - ❌ **Forbidden:** Client names, real URLs, specific country platforms (e.g., Zomato, Swiggy), local addresses, real documents (FSSAI).
  - ✅ **Allowed:** `[platform]`, `[marketplace]`, `e-commerce apps`, `[tax_id]`.
- **Project Specific:** Real names, data, and country-specific rules go in:
  - `brands/[industry]/_common/industry.md` (for country/industry rules)
  - `brands/[industry]/[brand]/context.md` (for client data)

---

## How We Work

### Project Types

We handle two types of projects, sometimes both for the same client:

| Type | Input | Output | Profile |
|------|-------|--------|---------|
| **Software Development** | PRD (Product Requirements Doc) | Code, deploys, features | `profiles/dev.md` |
| **Marketing** | Brand Guidelines | Campaigns, content, ads, growth | `profiles/marketing.md` |
| **Hybrid** | PRD + Brand Guidelines | Full product + growth | `profiles/hybrid.md` |

### Project Initiation

**For dev projects:**
1. Gather requirements → Create PRD (`/create-prd`)
2. Set up brand folder with `profile: dev`
3. Architecture planning → Build → Test → Deploy

**For marketing projects:**
1. Gather brand data → Fill `context.md` with `profile: marketing`
2. Fill industry `_common/` knowledge
3. Strategy → Create → Optimize → Report

**For hybrid:**
1. Start with dev (build the product)
2. Transition to marketing (grow it)
3. Use `profile: hybrid` — both agent teams available

---

## Client Onboarding Process

1. [ ] Identify industry → create/use industry folder
2. [ ] Create brand folder from `_brand-template/`
3. [ ] Fill `context.md` completely (30 min)
4. [ ] Drop raw client data into `reference/`
5. [ ] Set `profile:` type (dev / marketing / hybrid)
6. [ ] Define goals in `todo.md`
7. [ ] Start first task

---

## Communication Style

- [e.g., "Direct and clear — no fluff"]
- [e.g., "Explain technical decisions in plain language"]
- [e.g., "Always provide options, not just one answer"]
- [e.g., "Weekly status updates for clients"]

---

## Quality Standards

- [e.g., "No placeholder content in deliverables"]
- [e.g., "Every page must be mobile-responsive"]
- [e.g., "All copy must match brand voice from context.md"]
- [e.g., "Code must pass lint + tests before deploy"]

---

## Hard Rules (Always / Never)

### Always
- [ ] Read brand `context.md` before starting any work
- [ ] Check industry `_common/` for sector-specific rules
- [ ] Update `todo.md` after completing work
- [ ] Date-stamp artifacts in `artifacts/`

### Never
- [ ] Never skip the brand context — assumptions lead to rework
- [ ] Never deploy without testing
- [ ] Never publish content without matching brand voice

---

## Tool Preferences

- **IDE:** Antigravity
- **Diagrams:** draw.io (`.drawio` files)
- **Docs:** Markdown (`.md`) — AI-readable, version-controlled
- **Version control:** Git
- **Design:** [Your preferred tools]

---

## Routing Instructions

When starting work on a brand:

```
1. Load this file (vib.md) → company context
2. Read brands/[industry]/[brand]/context.md → check profile: field
3. Load matching profile:
   - profile: dev       → read profiles/dev.md
   - profile: marketing → read profiles/marketing.md
   - profile: hybrid    → read profiles/hybrid.md
4. Prioritize agents/skills listed in that profile
5. Read brands/[industry]/_common/industry.md → industry context
6. Begin work
```

---

*Fill in the bracketed sections with your actual practices. This is YOUR file — customize it fully.*
