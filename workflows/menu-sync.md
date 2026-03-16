---
description: Sync menu items between Google Sheets and Petpooja POS. Agent-driven workflow with human review checkpoints.
---

# /menu-sync Workflow

> **Agent-driven menu synchronization.** The agent reads data, applies rules from `@[skills/petpooja-management]`, and presents results as markdown tables for user approval before writing.

## Prerequisites
- Google Sheets API credentials at `/nara/resturant_ai/credentials.json`
- Spreadsheet shared with the Service Account
- `current sheet` tab contains the current Petpooja export
- Brand config at `/nara/resturant_ai/brands_config.json`

---

## Steps

### Step 1: Load Context
1. Read `brands_config.json` → Get sheet URL, live tab name, category rules
2. Read `@[skills/petpooja-management]` SKILL.md → Load schemas, matching rules, optimization templates
3. Read brand context from `.agent/brands/food/taste-the-heaven/context.md`

### Step 2: Read Live POS Data
1. Run the thin utility to fetch current state:
```bash
python3 menu_sync.py save-md "current sheet" "/nara/resturant_ai/menu_data/current_menu.md"
```
2. Read the generated `menu_data/current_menu.md` to understand the POS structure and Item IDs.

### Step 3: Read Update Source
1. Run the utility to fetch the update file:
```bash
python3 menu_sync.py read-local "/nara/resturant_ai/update" > "/tmp/update_source.json"
```
2. Read the source file and store it conceptually as `menu_data/update_items.md`.

### Step 4: Classify Items (Agent Does This)
For each item in the update source, the agent:
1. **Reads the matching rules** from SKILL.md § "MATCHING RULES"
2. **Compares** against `current_menu.md` items
3. **Classifies** as UPDATE (matched, price changed), SKIP (matched, same price), or CREATE (no match)
4. **Applies category mapping** from SKILL.md § "CATEGORY MAP"
5. **Generates optimized titles/descriptions** from SKILL.md § "OPTIMIZATION RULES"

### Step 5: Present Changes for Review
Generate two markdown files:

#### `proposed_updates.md`
| Item ID | POS Name | New Price | Old Price | New Online Name | New Description |
|---------|----------|-----------|-----------|-----------------|----------------|

#### `proposed_new_items.md`
| Name | Category | Price (H) | Price (F) | Online Name | Description | Dietary | Short Code |
|------|----------|-----------|-----------|-------------|-------------|---------|-----------|

**🛑 STOP HERE**: Present both tables to the user for approval via `notify_user`. Do NOT proceed until user approves.

### Step 6: Write Approved Data to Google Sheets
1. Prepare the JSON payloads for `Schema A` and `Schema B` based onapproved tables.
2. Save payloads to `/tmp/payload_update.json` and `/tmp/payload_add.json`.
3. Run the write commands:
// turbo
```bash
cat /tmp/payload_update.json | python3 menu_sync.py write "Update Existing"
cat /tmp/payload_add.json | python3 menu_sync.py write "Add New Items"
```

### Step 7: Save Local TSV Backups
Save `update_existing_FINAL.tsv` and `add_new_items_FINAL.tsv` for Petpooja dashboard upload.

---

## Guardrails (From SKILL.md — Auto-Applied)

| Guardrail | What it prevents |
|-----------|-----------------|
| **Category Lock** | Creating fake categories like "Momos" or "Chaap" |
| **Item ID Preservation** | Losing Item IDs that link to Zomato/Swiggy ratings |
| **Fuzzy Dedup** | Adding "Masala Chaap" when "Chaap Masala" already exists |
| **Semantic Safety** | Merging "Veg Manchurian" with "Chicken Manchurian" |
| **Human Review** | Agent shows `.md` tables before ANY writes |
