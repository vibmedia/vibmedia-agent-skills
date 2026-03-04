---
description: Find errors, broken references, stale data, and inconsistencies across the entire .agent system. Run monthly or after major changes.
---

# /system-check — Error Detection Workflow

> Comprehensive system health check. Finds broken references, missing files, stale data, and inconsistencies.

---

## When to Run

- Monthly system maintenance
- After major changes (batch additions, restructuring)
- When something isn't working as expected
- Before publishing updates to the repo

---

## Steps

### Step 1: Structural Integrity

Verify all required files exist where expected.

```bash
echo "=== SKILL.md files ==="
for dir in $(find skills -mindepth 1 -maxdepth 1 -type d); do
  [ ! -f "$dir/SKILL.md" ] && echo "❌ MISSING SKILL.md: $dir"
done

echo ""
echo "=== Agent files ==="
[ ! -d "agents" ] && echo "❌ MISSING agents/ directory"
[ $(ls agents/*.md 2>/dev/null | wc -l) -eq 0 ] && echo "❌ No agent files found"

echo ""
echo "=== Workflow files ==="
[ ! -d "workflows" ] && echo "❌ MISSING workflows/ directory"

echo ""
echo "=== Required system files ==="
[ ! -f "ARCHITECTURE.md" ] && echo "❌ MISSING ARCHITECTURE.md"
[ ! -f "GUIDE.md" ] && echo "❌ MISSING GUIDE.md"
[ ! -f "ROADMAP.md" ] && echo "❌ MISSING ROADMAP.md"
```

### Step 2: Frontmatter Validation

Every SKILL.md needs valid YAML frontmatter with required fields.

```bash
echo "=== Frontmatter Check ==="
for f in $(find skills -maxdepth 2 -name 'SKILL.md' -type f); do
  # Check starts with ---
  if ! head -1 "$f" | grep -q '^---'; then
    echo "❌ NO FRONTMATTER: $f"
    continue
  fi
  # Check has name: field
  if ! head -10 "$f" | grep -q '^name:'; then
    echo "⚠️  MISSING name: $f"
  fi
  # Check has description: field
  if ! head -10 "$f" | grep -q '^description:'; then
    echo "⚠️  MISSING description: $f"
  fi
done
```

### Step 3: Duplicate Detection

```bash
echo "=== Duplicate Skill Names ==="
dupes=$(grep -rh '^name:' skills/*/SKILL.md 2>/dev/null | sort | uniq -d)
if [ -n "$dupes" ]; then
  echo "❌ DUPLICATES FOUND:"
  echo "$dupes"
  # Find which files have the duplicates
  for name in $dupes; do
    grep -rl "^name: $name" skills/*/SKILL.md
  done
else
  echo "✅ No duplicates"
fi
```

### Step 4: Broken References

Check that skills referenced by agents and workflows actually exist.

```bash
echo "=== Agent → Skill References ==="
for agent in agents/*.md; do
  refs=$(grep -oP '(?:skills/|`)[a-z0-9-]+(?:-[a-z0-9]+)*' "$agent" 2>/dev/null | \
    sed 's/skills\///' | sed 's/`//' | sort -u)
  for ref in $refs; do
    if [ -d "skills/$ref" ]; then
      continue
    fi
    echo "⚠️  $(basename $agent) references '$ref' — not found in skills/"
  done
done

echo ""
echo "=== Workflow → Script References ==="
for wf in workflows/*.md; do
  scripts=$(grep -oP 'scripts/[a-z_]+\.py' "$wf" 2>/dev/null | sort -u)
  for script in $scripts; do
    found=$(find . -path "*/$script" -type f 2>/dev/null)
    [ -z "$found" ] && echo "⚠️  $(basename $wf) references '$script' — not found"
  done
done
```

### Step 5: Count Consistency

Check that counts in ARCHITECTURE.md and README.md match reality.

```bash
actual_skills=$(find skills -maxdepth 2 -name 'SKILL.md' -type f | wc -l)
actual_agents=$(ls agents/*.md 2>/dev/null | wc -l)
actual_workflows=$(ls workflows/*.md 2>/dev/null | wc -l)

echo "=== Count Check ==="
echo "Actual: $actual_skills skills, $actual_agents agents, $actual_workflows workflows"

# Check ARCHITECTURE.md
arch_skills=$(grep -oP 'Skills \(\K\d+' ARCHITECTURE.md 2>/dev/null)
if [ "$arch_skills" != "$actual_skills" ]; then
  echo "❌ ARCHITECTURE.md says $arch_skills skills, actual is $actual_skills"
else
  echo "✅ ARCHITECTURE.md skill count matches"
fi
```

### Step 6: Brand Structure Validation

```bash
echo "=== Brand Structure ==="
for industry in $(find brands -mindepth 1 -maxdepth 1 -type d ! -name '_*'); do
  echo ""
  echo "📁 $(basename $industry)"

  # Check _common exists
  [ ! -d "$industry/_common" ] && echo "  ❌ Missing _common/"
  [ ! -f "$industry/_common/industry.md" ] && echo "  ⚠️  Missing _common/industry.md"

  # Check each brand
  for brand in $(find "$industry" -mindepth 1 -maxdepth 1 -type d ! -name '_*'); do
    echo "  └── $(basename $brand)"
    [ ! -f "$brand/context.md" ] && echo "     ❌ Missing context.md"
    [ ! -f "$brand/todo.md" ] && echo "     ⚠️  Missing todo.md"
  done
done
```

### Step 7: Stale Content Detection

Check for files that haven't been updated recently.

```bash
echo "=== Files Not Updated in 90+ Days ==="
find . -name '*.md' -mtime +90 -not -path './.git/*' | head -20
```

Check for empty or near-empty template files that were never filled:

```bash
echo ""
echo "=== Unfilled Templates (still contain placeholder text) ==="
grep -rl '\[Brand Name\]\|\[Industry Name\]\|\[Name\]\|\[URL\]' brands/ 2>/dev/null | \
  grep -v '_template\|_industry-template'
```

### Step 8: Cross-Reference Check

Verify that every skill category in ARCHITECTURE.md has matching directories:

```bash
echo "=== Skills in ARCHITECTURE.md vs Actual ==="
# Extract skill names from ARCHITECTURE.md backtick references
grep -oP '`[a-z0-9-]+`' ARCHITECTURE.md | tr -d '`' | sort -u | while read skill; do
  [ -d "skills/$skill" ] || echo "⚠️  ARCHITECTURE.md lists '$skill' but no directory exists"
done

# Check for skills that exist but aren't in ARCHITECTURE.md
for dir in $(find skills -mindepth 1 -maxdepth 1 -type d -exec basename {} \;); do
  grep -q "\`$dir\`" ARCHITECTURE.md 2>/dev/null || \
    echo "⚠️  skills/$dir exists but not listed in ARCHITECTURE.md"
done
```

### Step 9: Workflow Coverage Audit (STRICT)

Enforce the workflow-coverage-rule: every agent and skill must be reachable.

```bash
echo "=== Workflow Coverage Audit ==="

# Check every agent is mentioned in at least one workflow
echo ""
echo "--- Agent Coverage ---"
for agent_file in agents/*.md; do
  agent=$(basename "$agent_file" .md)
  found=$(grep -rl "$agent" workflows/ 2>/dev/null | head -1)
  if [ -z "$found" ]; then
    # Check if reachable via orchestrate
    found=$(grep -l "$agent" workflows/orchestrate.md 2>/dev/null)
  fi
  if [ -z "$found" ]; then
    echo "🔴 ORPHANED AGENT: $agent — not reachable via any workflow"
  fi
done

# Check every skill is in at least one agent's frontmatter
echo ""
echo "--- Skill Coverage ---"
for skill_dir in $(find skills -mindepth 1 -maxdepth 1 -type d -exec basename {} \;); do
  found=$(grep -rl "$skill_dir" agents/ 2>/dev/null | head -1)
  if [ -z "$found" ]; then
    echo "🔴 ORPHANED SKILL: $skill_dir — not loaded by any agent"
  fi
done

echo ""
echo "If any 🔴 ORPHANED items found: FIX BEFORE PROCEEDING."
echo "See rules/workflow-coverage-rule.md for resolution steps."
```

### Step 10: Telos Validation

Check that brand folders use Telos context files.

```bash
echo "=== Telos Validation ==="
for industry in $(find brands -mindepth 1 -maxdepth 1 -type d ! -name '_*'); do
  for brand in $(find "$industry" -mindepth 1 -maxdepth 1 -type d ! -name '_*'); do
    echo "  └── $(basename $brand)"
    [ ! -f "$brand/telos.md" ] && echo "     ❌ Missing telos.md (required — replaces todo.md)"
    # Check telos.md has been filled in (not still template)
    if [ -f "$brand/telos.md" ]; then
      grep -q '\[Brand Name\]' "$brand/telos.md" && \
        echo "     ⚠️  telos.md still contains template placeholders"
    fi
  done
done
```

### Step 11: Report

Produce a health report:

```
🏥 System Health Report
────────────────────────
Date: [Date]

Components:
  Skills:     [N] ✅/❌
  Agents:     [N] ✅/❌
  Workflows:  [N] ✅/❌
  Industries: [N]
  Brands:     [N]

Coverage:
  Agent Coverage:  [N]/[Total] ✅/❌
  Skill Coverage:  [N]/[Total] ✅/❌

Errors (must fix):
  ❌ [Error 1]
  ❌ [Error 2]

Warnings (should fix):
  ⚠️  [Warning 1]
  ⚠️  [Warning 2]

Health Score: [Good / Needs Attention / Critical]
```

### Step 12: Fix or Flag

For each issue found:

- **Errors (❌)** → Fix immediately (broken refs, missing files, orphaned components)
- **Warnings (⚠️)** → Add to `telos.md` Activity Log for next session
- **Info** → Note for awareness, no action needed
