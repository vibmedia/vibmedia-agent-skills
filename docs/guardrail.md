# Petpooja Menu Sync Guardrails

These rules are derived from manual corrections made by the owner and MUST be followed by the agent to ensure POS data integrity and correct grouping in Petpooja/Zomato.

## 1. Variation Architecture (The 3-Row Rule)
- Every item with portions (Half/Full) MUST have 3 rows in the sync:
  1. **Parent**: `Item Type = item`, `Price = 0`.
  2. **Full**: `Item Type = variation`, `Price = 289 (sample)`.
  3. **Half**: `Item Type = variation`, `Price = 179 (sample)`.

## 2. Naming Convention (Full Name with Parentheses)
- **Variation Item Name**: The `Item Name` column for variation rows MUST include the variation in parentheses.
  - ✅ `Spring Roll Veg (Full)`
  - ✅ `Spring Roll Veg (Half)`
  - ❌ `Spring Roll Veg` (only allowed for parent row)
- **Online Display Name**: Should strictly match the `Item Name` format: `{Parent Name} ({Variation})`. 
- **NO PIECES RULE**: Per user mandate, piece counts like `(8 Pcs)` or `(10 Pcs)` MUST NOT appear in the `Item Name` or `Online Display Name` columns. These are scrubbed during synchronization to maintain clean naming.

## 2.1. Block Alignment (Add New Items Only)
- **First Variation Rule**: The very first variation row of an item block in the "Add New Items" sheet MUST have the **Parent Name** in Column A.
- **Linking**: Subsequent variation rows in the same block MUST leave Column A **blank** to correctly link to the parent.
- **Existing Parents**: Even if the parent already exists in POS, if you are adding its first new variation to the "Add New" sheet, you MUST provide the parent name in Column A for that variation row.

## 3. ID Preservation & Deduplication
- **ID-First**: If an `Item ID` exists in the POS for a row, that ID MUST be used.
- **No Duplicates**: Before adding an item, search for it using canonical tokens (e.g., "HCP" for Honey Chilli Potato) to see if it already exists with a different name.

## 4. Price Logic
- Parent rows MUST have `Price = 0` if variations exist.
- Prices must be extracted from the latest `update` source provided by the user.

## 5. Schema Alignment
- **Update Existing**: 23 columns. Every row must have a full name.
- **Add New Items**: 30 columns. Variations can be linked to the parent in the same block.
