---
name: systematic-debugging
description: 4-phase systematic debugging methodology with root cause analysis and evidence-based verification. Use when debugging complex issues.
category: core
profile: shared
allowed-tools: Read, Glob, Grep
---

# Systematic Debugging

> Source: obra/superpowers

## Overview
This skill provides a structured approach to debugging that prevents random guessing and ensures problems are properly understood before solving.

## 4-Phase Debugging Process

### Phase 1: Reproduce
Before fixing, reliably reproduce the issue.

```markdown
## Reproduction Steps
1. [Exact step to reproduce]
2. [Next step]
3. [Expected vs actual result]

## Reproduction Rate
- [ ] Always (100%)
- [ ] Often (50-90%)
- [ ] Sometimes (10-50%)
- [ ] Rare (<10%)
```

### Phase 2: Isolate
Narrow down the source.

```markdown
## Isolation Questions
- When did this start happening?
- What changed recently?
- Does it happen in all environments?
- Can we reproduce with minimal code?
- What's the smallest change that triggers it?
```

### Phase 3: Understand
Find the root cause, not just symptoms.

```markdown
## Root Cause Analysis
### The 5 Whys
1. Why: [First observation]
2. Why: [Deeper reason]
3. Why: [Still deeper]
4. Why: [Getting closer]
5. Why: [Root cause]
```

### Phase 4: Fix & Verify
Fix and verify it's truly fixed.

```markdown
## Fix Verification
- [ ] Bug no longer reproduces
- [ ] Related functionality still works
- [ ] No new issues introduced
- [ ] Test added to prevent regression
```

## Debugging Checklist

```markdown
## Before Starting
- [ ] Can reproduce consistently
- [ ] Have minimal reproduction case
- [ ] Understand expected behavior

## During Investigation
- [ ] Check recent changes (git log)
- [ ] Check logs for errors
- [ ] Add logging if needed
- [ ] Use debugger/breakpoints

## After Fix
- [ ] Root cause documented
- [ ] Fix verified
- [ ] Regression test added
- [ ] Similar code checked
```

## Common Debugging Commands

```bash
# Recent changes
git log --oneline -20
git diff HEAD~5

# Search for pattern
grep -r "errorPattern" --include="*.ts"

# Check logs
pm2 logs app-name --err --lines 100
```

## Anti-Patterns

❌ **Random changes** — "Maybe if I change this..."
❌ **Ignoring evidence** — "That can't be the cause"
❌ **Assuming** — "It must be X" without proof
❌ **Not reproducing first** — Fixing blindly
❌ **Stopping at symptoms** — Not finding root cause

---

## Advanced Techniques (from Superpowers)

### Root Cause Tracing

When error is deep in call stack:
- Where does the bad value originate?
- Trace backward from symptom to source
- At each step: "Is this the cause, or a consequence?"
- Stop when you find something that explains ALL symptoms

### Multi-Component Diagnostics

When system has multiple components (CI → build → deploy, API → service → DB):

**BEFORE proposing fixes, add diagnostic instrumentation:**
```
For EACH component boundary:
  1. Log inputs entering the component
  2. Log outputs leaving the component
  3. Compare expected vs actual at each boundary
```

This reveals: Which layer fails (secrets → workflow ✓, workflow → build ✗)

### Hypothesis Testing (Phase 3)

1. **Form hypothesis** — State clearly: "I think X is the root cause because Y"
2. **Test minimally** — Make the SMALLEST possible change to test hypothesis
3. **One variable at a time** — Don't fix multiple things at once
4. **Verify** — Did it work? Yes → Phase 4. No → Form NEW hypothesis, DON'T add more fixes on top

### The 3+ Fixes Escalation Rule

If you've tried 3+ fixes and none work:
- **STOP** — Count how many fixes you've attempted
- If < 3: Return to Phase 1, re-analyze with new information
- **If ≥ 3: STOP and question the architecture**
- Pattern indicating architectural problem: Each fix reveals new shared state/coupling in different places, or fixes require "massive refactoring"

### Quick Reference

| Phase | Key Activities | Success Criteria |
|-------|---------------|------------------|
| **1. Reproduce** | Reproduce, check changes, gather evidence | Understand WHAT and WHERE |
| **2. Isolate** | Find working examples, compare | Identify differences |
| **3. Understand** | Form hypothesis, test minimally | Confirmed root cause |
| **4. Fix & Verify** | Create test, fix, verify | Bug resolved, tests pass |

### Human Partner Signals You're Doing It Wrong

Watch for these redirections:
- "Is that not happening?" — You assumed without verifying
- "Stop guessing" — You're proposing fixes without understanding
- "We're stuck?" (frustrated) — Your approach isn't working
