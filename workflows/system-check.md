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

### Step 9: Report

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

Errors (must fix):
  ❌ [Error 1]
  ❌ [Error 2]

Warnings (should fix):
  ⚠️  [Warning 1]
  ⚠️  [Warning 2]

Health Score: [Good / Needs Attention / Critical]
```

### Step 10: Fix or Flag

For each issue found:
- **Errors (❌)** → Fix immediately (broken refs, missing files, duplicate names)
- **Warnings (⚠️)** → Add to `todo.md` for next session
- **Info** → Note for awareness, no action needed
