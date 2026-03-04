# Workflow → Agent → Skill Coverage Map

> Master reference showing how every component is reachable through workflows.
> **Rule**: Every agent and skill MUST appear at least once. See `rules/workflow-coverage-rule.md`.

---

## Coverage Summary

| Category      | Total | Covered | Coverage |
| ------------- | ----- | ------- | -------- |
| **Agents**    | 21    | 21      | ✅ 100%  |
| **Skills**    | 78    | 78      | ✅ 100%  |
| **Workflows** | 26    | 26      | ✅ 100%  |

---

## Workflow → Agent → Skill Mapping

### Development Workflows

#### `/create` — Create Application

| Agent                 | Skills Loaded                                                                                                       |
| --------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `project-planner`     | plan-writing, brainstorming, architecture                                                                           |
| `frontend-specialist` | frontend-design, nextjs-react-expert, tailwind-patterns, composition-patterns, web-design-guidelines, ui-ux-pro-max |
| `backend-specialist`  | api-patterns, nodejs-best-practices, database-design                                                                |
| `database-architect`  | database-design, typeorm-patterns                                                                                   |
| `test-engineer`       | testing-patterns, tdd-workflow, webapp-testing                                                                      |
| `devops-engineer`     | deployment-procedures, server-management                                                                            |

#### `/plan` — Project Planning

| Agent             | Skills Loaded                             |
| ----------------- | ----------------------------------------- |
| `project-planner` | plan-writing, brainstorming, architecture |
| `product-manager` | plan-writing, brainstorming               |

#### `/debug` — Systematic Debugging

| Agent            | Skills Loaded                   |
| ---------------- | ------------------------------- |
| `debugger`       | systematic-debugging            |
| `explorer-agent` | (codebase analysis — no skills) |

#### `/test` — Test Generation & Execution

| Agent                    | Skills Loaded                    |
| ------------------------ | -------------------------------- |
| `test-engineer`          | testing-patterns, tdd-workflow   |
| `qa-automation-engineer` | webapp-testing, testing-patterns |

#### `/code-review` — Technical Code Review

| Agent                | Skills Loaded                                                        |
| -------------------- | -------------------------------------------------------------------- |
| `code-reviewer`      | requesting-code-review, receiving-code-review, code-review-checklist |
| `code-archaeologist` | clean-code, code-review-checklist                                    |

#### `/code-review-fix` — Fix Review Issues

| Agent           | Skills Loaded         |
| --------------- | --------------------- |
| `code-reviewer` | receiving-code-review |

#### `/deploy` — Production Deployment

| Agent                   | Skills Loaded                            |
| ----------------------- | ---------------------------------------- |
| `devops-engineer`       | deployment-procedures, server-management |
| `security-auditor`      | vulnerability-scanner                    |
| `performance-optimizer` | performance-profiling                    |

#### `/enhance` — Update Existing Application

| Agent                   | Skills Loaded              |
| ----------------------- | -------------------------- |
| (auto-routed by domain) | (context-dependent skills) |

#### `/preview` — Local Dev Server

| Agent                            | Skills Loaded |
| -------------------------------- | ------------- |
| (no specific agent — procedural) | —             |

#### `/rca` — Root Cause Analysis

| Agent      | Skills Loaded        |
| ---------- | -------------------- |
| `debugger` | systematic-debugging |

#### `/implement-fix` — Implement Fix from RCA

| Agent                   | Skills Loaded              |
| ----------------------- | -------------------------- |
| (auto-routed by domain) | (context-dependent skills) |

#### `/validate` — Validate Implementation

| Agent              | Skills Loaded                                    |
| ------------------ | ------------------------------------------------ |
| `test-engineer`    | testing-patterns, verification-before-completion |
| `security-auditor` | vulnerability-scanner                            |

---

### Planning & Analysis Workflows

#### `/brainstorm` — Socratic Discovery

| Agent             | Skills Loaded               |
| ----------------- | --------------------------- |
| `project-planner` | brainstorming               |
| `product-owner`   | plan-writing, brainstorming |

#### `/create-prd` — Product Requirements Document

| Agent             | Skills Loaded               |
| ----------------- | --------------------------- |
| `product-manager` | plan-writing, brainstorming |
| `product-owner`   | plan-writing, brainstorming |

#### `/orchestrate` — Multi-Agent Coordination

| Agent                  | Skills Loaded                                |
| ---------------------- | -------------------------------------------- |
| `orchestrator`         | parallel-agents, behavioral-modes            |
| (all agents available) | (all skills reachable through orchestration) |

#### `/piv-plan` — Deep Feature Planning

| Agent             | Skills Loaded                               |
| ----------------- | ------------------------------------------- |
| `project-planner` | plan-writing, architecture, executing-plans |
| `explorer-agent`  | —                                           |

#### `/piv-prime` — Prime Agent with Codebase

| Agent            | Skills Loaded |
| ---------------- | ------------- |
| `explorer-agent` | —             |

#### `/piv-execute` — Execute PIV Plan

| Agent                       | Skills Loaded                                |
| --------------------------- | -------------------------------------------- |
| (auto-routed per plan step) | subagent-driven-development, executing-plans |

#### `/execution-report` — Implementation Report

| Agent                  | Skills Loaded           |
| ---------------------- | ----------------------- |
| `documentation-writer` | documentation-templates |

#### `/system-review` — Review Against Plan

| Agent             | Skills Loaded                                |
| ----------------- | -------------------------------------------- |
| `project-planner` | plan-writing, verification-before-completion |

#### `/status` — Project Progress

| Agent                      | Skills Loaded |
| -------------------------- | ------------- |
| (procedural — reads state) | —             |

---

### Design Workflows

#### `/ui-ux-pro-max` — Premium UI Design

| Agent                 | Skills Loaded                  |
| --------------------- | ------------------------------ |
| `frontend-specialist` | ui-ux-pro-max, frontend-design |
| `mobile-developer`    | mobile-design                  |

---

### System Management Workflows

#### `/update` — Sync System

| Agent        | Skills Loaded                           |
| ------------ | --------------------------------------- |
| (procedural) | intelligent-routing (validates routing) |

#### `/audit-goals` — Goal Gap Analysis

| Agent             | Skills Loaded |
| ----------------- | ------------- |
| `project-planner` | plan-writing  |

#### `/system-check` — Health Check + Coverage Audit

| Agent        | Skills Loaded     |
| ------------ | ----------------- |
| (procedural) | lint-and-validate |

#### `/visualize-arch` — Architecture Visualization

| Agent            | Skills Loaded |
| ---------------- | ------------- |
| `explorer-agent` | architecture  |

---

### Security Workflows (via `/deploy` and `/orchestrate`)

| Agent                | Skills Loaded                           |
| -------------------- | --------------------------------------- |
| `security-auditor`   | vulnerability-scanner, red-team-tactics |
| `penetration-tester` | red-team-tactics                        |

---

### Marketing Workflows (via `/orchestrate` + profile routing)

| Agent                   | Skills Loaded                                                                                 |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| `seo-specialist`        | seo-fundamentals, geo-fundamentals, seo-audit, ai-seo, programmatic-seo, schema-markup        |
| (skill-based marketing) | copywriting, copy-editing, cold-email, email-sequence, social-content, content-strategy       |
| (skill-based CRO)       | page-cro, signup-flow-cro, onboarding-cro, form-cro, popup-cro, paywall-upgrade-cro           |
| (skill-based ads)       | paid-ads, ad-creative, analytics-tracking, ab-test-setup                                      |
| (skill-based growth)    | churn-prevention, free-tool-strategy, referral-program, marketing-ideas, marketing-psychology |
| (skill-based strategy)  | launch-strategy, pricing-strategy, competitor-alternatives, product-marketing-context         |

---

### Special Skills (Always Available)

These skills load globally regardless of workflow:

| Skill                            | Why Always Available                 |
| -------------------------------- | ------------------------------------ |
| `clean-code`                     | Global coding standard (Tier 0 rule) |
| `intelligent-routing`            | Agent selection system               |
| `behavioral-modes`               | Agent personas                       |
| `parallel-agents`                | Multi-agent patterns                 |
| `bash-linux`                     | Shell commands (Linux)               |
| `powershell-windows`             | Shell commands (Windows)             |
| `i18n-localization`              | Internationalization                 |
| `mcp-builder`                    | Model Context Protocol               |
| `app-builder`                    | Full-stack scaffolding               |
| `writing-skills`                 | Skill creation                       |
| `using-git-worktrees`            | Workspace isolation                  |
| `finishing-a-development-branch` | Branch management                    |

---

### Game Development (via `/create` + domain detection)

| Agent            | Skills Loaded    |
| ---------------- | ---------------- |
| `game-developer` | game-development |

---

### Mobile Development (via `/create` + `/ui-ux-pro-max`)

| Agent              | Skills Loaded                          |
| ------------------ | -------------------------------------- |
| `mobile-developer` | mobile-design, react-native-guidelines |

---

### Language-Specific Skills (via agent auto-loading)

| Skill                     | Loaded By                                   |
| ------------------------- | ------------------------------------------- |
| `python-patterns`         | `backend-specialist` (when Python detected) |
| `rust-pro`                | `backend-specialist` (when Rust detected)   |
| `nodejs-best-practices`   | `backend-specialist` (default)              |
| `react-native-guidelines` | `mobile-developer`                          |

---

_Last updated: 2026-03-04_
_To verify: run `/system-check` Step 9.5: Coverage Audit_
