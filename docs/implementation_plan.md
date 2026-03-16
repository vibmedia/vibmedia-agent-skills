# Menu Engineering & Zomato SEO — MD-First Architecture

## Goal

Transform the menu sync from a simple data transfer into a **Menu Engineering & SEO Engine**. This involves deeper categorization, variation handling (Half/Full), addon management, and Zomato-optimized copy.

## User Review Required

> [!IMPORTANT]
> - **ID Preservation**: We will prioritize matching existing POS items to retain historical `Item ID` data. The Parent row's ID will ALWAYS be preserved with Price 0.
> - **Robust Multi-Index Matching**: We use Token Sets, Clean Names, and Short Codes to match existing items and prevent duplicates.
> - **No Pieces Rule**: Strictly removes `(8 Pcs)` or any piece count from `Item Name` and `Online Display Name` columns.
> - **Safety Guard**: Automatic cross-check of all `Adds` against POS to move existing items to `Updates` list.
> - **3-Row Architecture**: Every item with portions will have a Parent (item), a Full (variation), and a Half (variation).
> - **Hierarchical Linking**: In the "Add New Items" tab, we will use the **Blank-Name Column A** technique to link variations to their parent.

---

## Proposed Changes

### [MODIFY] [SKILL.md](file:///nara/resturant_ai/.agent/skills/petpooja-management/SKILL.md)

**New Sections to Implement:**

1.  **Zomato SEO Masterclass**:
    - **Keyword Architecture**: Title templates using `{Protein} + {Preparation} + {Quantity}`.
    - **Sensory Descriptions**: A library of "mouth-watering" adjectives mapped to cuisine types.
    - **SEO Badges**: Rules for auto-applying "Bestseller" and "New" tags.
2.  **3-Row Variation Logic**:
    - **Row 1**: Parent (Item ID preserved, Price 0, Online Name = Core Name).
    - **Row 2**: Full Portion (ID preserved if exists, Online Name = Core Name + " (Full)").
    - **Row 3**: Half Portion (ID preserved if exists, Online Name = Core Name + " (Half)").
    - Price calculation logic (Premium on half portions).
3.  **Addon Group Management**:
    - Schema for linking items to "Customisation" or "Addon" groups.

### [MODIFY] [/menu-sync Workflow](file:///nara/resturant_ai/.agent/workflows/menu-sync.md)

**Updated Steps:**

1.  **Step 4 (Enriched)**: The agent classifies items AND performs "SEO Audit" — checking if the title and description meet the new high-standard rules.
2.  **Step 5 (Approval)**: The review table will now include a "SEO Status" column to show what was optimized.

---

## Verification Plan

### Automated Verification
- Run `python .agent/scripts/lint_runner.py` to ensure .md files are valid.

### Manual Verification
1. Run `/menu-sync` with the new update file.
2. Verify that "Half" and "Full" items are correctly grouped in `proposed_new_items.md` with blank names for children.
3. Check that the "Update Existing" sheet contains the Parent ID with Price 0 for every variation-ready item.
4. Verify the generated "Online Display Names" against the SEO rules in SKILL.md.
