---
description: Sync all system components after adding skills, agents, workflows, industries, or brands. Updates ARCHITECTURE.md and README.md counts, validates integrity.
---

# /update — System Sync Workflow

> Run this after adding or modifying any component. Ensures everything stays aligned.

---

## When to Run

- After adding a new **skill** (folder in `skills/`)
- After adding a new **agent** (file in `agents/`)
- After adding a new **workflow** (file in `workflows/`)
- After adding a new **industry** (folder in `brands/`)
- After adding a new **brand** (folder in `brands/[industry]/`)
- After adding **reference files** or **knowledge** to any component
- After any structural change to the `.agent/` directory

---

## Steps

### Step 1: Count All Components

Scan the directory structure and record current counts.

```bash
# Count skills (directories with SKILL.md)
echo "Skills: $(find skills -maxdepth 2 -name 'SKILL.md' -type f | wc -l)"

# Count agents (*.md files in agents/)
echo "Agents: $(ls agents/*.md 2>/dev/null | wc -l)"

# Count workflows (*.md files in workflows/)
echo "Workflows: $(ls workflows/*.md 2>/dev/null | wc -l)"

# Count industries (non-template directories in brands/)
echo "Industries: $(find brands -mindepth 1 -maxdepth 1 -type d ! -name '_*' | wc -l)"

# Count brands (non-template directories inside industry folders)
echo "Brands: $(find brands -mindepth 2 -maxdepth 2 -type d ! -name '_*' | wc -l)"

# Count reference files
echo "Reference files: $(find skills -path '*/references/*' -type f ! -name '.gitkeep' | wc -l)"
```

Record these numbers for the next steps.

### Step 2: Check for Duplicates

```bash
# Check duplicate skill names
grep -rh '^name:' skills/*/SKILL.md | sort | uniq -d
```

- If any duplicates found → STOP and resolve before continuing.
- Duplicate names cause routing conflicts.

### Step 3: Validate All SKILL.md Frontmatter

```bash
# Every SKILL.md must start with ---
for f in $(find skills -maxdepth 2 -name 'SKILL.md' -type f); do
  if ! head -1 "$f" | grep -q '^---'; then
    echo "MISSING FRONTMATTER: $f"
  fi
done
```

- Every SKILL.md MUST have YAML frontmatter with `name:` and `description:`.
- Fix any missing frontmatter before continuing.

### Step 4: Validate Agent Skill References

```bash
# Check every skill referenced by agents exists
for agent in agents/*.md; do
  grep -oP 'skills/[a-z0-9-]+' "$agent" 2>/dev/null | while read ref; do
    [ ! -d "$ref" ] && echo "BROKEN REF: $(basename $agent) → $ref"
  done
done
```

- Fix any broken references (typos, deleted skills).

### Step 5: Update ARCHITECTURE.md

Open `ARCHITECTURE.md` and update:

1. **Top counts** — Update the "X Skills", "Y Agents", "Z Workflows" numbers
2. **Directory structure comment** — Update the `# N Skills` / `# N Agents` comments
3. **Skills section header** — Update `## 🧩 Skills (N)`
4. **Stats table at bottom** — Update the Total Skills/Agents/Workflows rows
5. **New skills** — If any new skills were added, add them to the correct category table
6. **New agents** — If any new agents were added, add them to the agents table

### Step 6: Update README.md

Open `README.md` and update:

1. **Header line** — Update the skill/agent/workflow counts
2. **Skills section** — If new skills added, add to correct category
3. **Agents table** — If new agents added, add row
4. **Workflows table** — If new workflows added, add row
5. **Stats table** — Update counts

### Step 7: List All Industries and Brands

```bash
echo "=== Industries & Brands ==="
for industry in $(find brands -mindepth 1 -maxdepth 1 -type d ! -name '_*' | sort); do
  echo ""
  echo "📁 $(basename $industry)"
  for brand in $(find "$industry" -mindepth 1 -maxdepth 1 -type d ! -name '_*' | sort); do
    echo "   └── $(basename $brand)"
  done
done
```

- Verify the listing matches reality.
- Check that each brand has `context.md` and `todo.md`.

### Step 8: Verify Industry Common Knowledge

```bash
# Check each industry has _common/industry.md
for industry in $(find brands -mindepth 1 -maxdepth 1 -type d ! -name '_*'); do
  [ ! -f "$industry/_common/industry.md" ] && echo "MISSING: $industry/_common/industry.md"
done
```

### Step 9: Re-generate System Architecture

Ensure system diagrams reflect the latest structure:

```bash
AGENT_DIR="$(pwd)/.agent"
python3 "$AGENT_DIR/skills/architecture-explorer/scripts/scanner.py" . \
  --output "$AGENT_DIR/skills/architecture-explorer/assets/relationships.json" \
  --mermaid "$AGENT_DIR/skills/architecture-explorer/assets/map.md" \
  --drawio "$AGENT_DIR/skills/architecture-explorer/assets/architecture.drawio" \
  --depth 2
```

### Step 10: Confirm & Report

Produce a summary report:

```
📊 System Status After Update
─────────────────────────────
Skills:     [N] (was [old])
Agents:     [N] (was [old])
Workflows:  [N] (was [old])
Industries: [N]
Brands:     [N]
References: [N]

Changes:
- [What was added/modified]

Issues Found:
- [Any broken refs, missing frontmatter, etc.]
- None ✅
```
