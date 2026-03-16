# Task Plan — MD-First Menu Sync Restructure

## Phase 1: Restructure SKILL.md ✅
- [x] Add complete Petpooja schemas (23-col Update, 30-col Add) with exact headers
- [x] Convert matching rules from Python to agent-readable instructions
- [x] Add optimization templates (title/description rules)
- [x] Add brand-specific data references

## Phase 2: Rewrite Workflow ✅
- [x] Convert `/menu-sync` from "run script" to step-by-step agent instructions
- [x] Add review checkpoint (agent shows `.md` tables before writing)
- [x] Add Google Sheets read/write steps using agent tools

## Phase 3: Create Data Layer ✅
- [x] Create `menu_data/` directory for .md tables
- [x] Verify `save-md` command generates markdown from live data

## Phase 4: Demote Python ✅
- [x] Strip `menu_sync.py` to only auth + read/write functions (845 → 150 lines)
- [x] Remove all classification, matching, and optimization logic from Python
- [x] Delete `menu_watcher.py`

## Phase 5: Align GEMINI.md ✅
- [x] Add "📄 MD-First Operations" rule to TIER 0 Universal Rules
- [x] Update `HOW_TO_USE.md` for new workflow

## Phase 6: Sync Execution 🏗️
- [x] Read live POS data and update source
- [x] Classify items and generate .md tables
- [x] Present initial changes for human review
- [x] Research & Structure Zomato SEO & Variation Logic
- [x] Update SKILL.md with advanced matching and SEO templates
- [x] Regenerate `proposed_updates.md` and `proposed_new_items.md` with deep SEO
- [x] Write approved updates to "Update Existing" tab
- [x] Write approved new items to "Add New Items" tab
- [x] Save local TSV backups

## Phase 7: Correction & Final Sync 🏗️
- [x] Verify with final walkthrough

## Phase 10: Parent-Child Sync Consolidation ✅
- [x] Research existing variations in POS
- [x] Keep related rows (Parent/Vary) together in Update sheet

## Phase 11: Transition to MD-First Architecture ✅
- [x] Create `pos-operations-manager` agent
- [x] Refactor `/menu-sync` workflow to remove Python logic
- [x] Execute Sync via Agent Reasoning (Pure MD-First)
- [x] Final Validation of POS Integrity

## Phase 12: Sync with User-Updated POS 🏗️
- [x] Read new "current sheet" from POS
- [x] Audit user manual changes for new rules
- [x] Update `SKILL.md` and `guardrail.md`
- [x] Regenerate sync payloads
- [x] Debug 'Already Assigned' errors (Multi-Index Matching)
- [x] Execute Final Sync
