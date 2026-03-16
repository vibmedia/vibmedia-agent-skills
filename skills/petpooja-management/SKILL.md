---
name: petpooja-management
description: Manage Petpooja POS billing dashboard, menu schemas, and TSV exports
profile: hybrid
category: operations
---

# Petpooja Management Skill

This skill defines how agents should interact with the Petpooja Restaurant POS ecosystem. The agent reads these rules and applies them directly — **no intermediate Python scripts for logic**.

> 🔴 **MD-FIRST RULE**: All classification, matching, and optimization logic lives HERE. Python is only used as a thin utility for Google Sheets auth/read/write. The agent IS the engine.

---

## 🚀 ZOMATO SEO MASTERCLASS (Agent-Enforced)

Every item synchronized MUST pass this SEO audit. If an item fails, the agent creates an optimized version in the `Online Display Name` and `Description` columns.

### 1. Title Keywords (The "Search Magnet")
- **Formula**: `{Core Item} + {Preparation} + {Protein} + {Quantity/Size}`
- **Forbidden**: Generic names like "Veg Momo", "Noodles".
- **Required**: Use sensory adjectives (Smoky, Crispy, Juicy, Wok-tossed).

### 2. Description Sensory Mapping

| Cuisine | Sensory Adjectives | Preparation Keywords |
|---------|-------------------|----------------------|
| Momo | Himalayan, Thin-wrapped, Juicy | Steamed, Pan-fried, Tandoor-grilled |
| Chinese | Wok-tossed, Fiery, Aromatic | Stir-fried, Deep-fried, Braised |
| Tandoor | Smoky, Charred, Succulent | Marinated, Clay-oven baked |
| Continental | Creamy, Hand-tossed, Al dente | Sautéed, Baked, Infused |

### 3. Portion Meta-Data
- **Quantity**: Always specify piece counts for starters/momos (e.g., "8 Pcs").
- **Size**: Always append "(Half)" or "(Full)" to the `Online Display Name` to clarify for the customer, even if it's in the variation column.
- **NO PIECES IN ITEM NAME**: Per user mandate, the `Item Name` and `Online Display Name` MUST NOT contain piece counts like `(8 Pcs)`. These are scrubbed during sync. Piece counts should only be handled via Category or Description if needed.

---

## 🔴 CRITICAL SAFETY HARNESSES

1. **Never Lose Item IDs**: Petpooja uses `Item ID` to map sales, ratings, and analytics. If a menu update is pushed without an `Item ID` for an existing item, Petpooja creates a duplicate, destroying historical data and live platform mapping (Zomato/Swiggy).
2. **Datacenter IP Block**: `billing.petpooja.com` sits behind an AWS ELB WAF that drops traffic from cloud IPs (403 Forbidden).
3. **Human Verification**: Always show proposed changes as markdown tables for user approval BEFORE writing to Google Sheets.
4. **WhatsApp Notification**: Send screenshots of changes to the owner (`9718204968`) for final confirmation before uploading to Petpooja dashboard.

---

## 📋 PETPOOJA SCHEMAS (Exact Column Order)

### Schema A: "Update Existing Items" (23 Columns)

Use this when updating items that ALREADY have an Item ID in the POS.

| # | Column Name | Default | Notes |
|---|------------|---------|-------|
| 1 | Item ID | *(from POS)* | 🔴 NEVER blank for existing items |
| 2 | Category | *(from POS)* | Use exact POS category name |
| 3 | Item Name | *(from POS)* | Keep original POS name |
| 4 | Variation | *(from POS)* | e.g., "Half", "Full", or blank |
| 5 | Online Display Name | *(optimized)* | Agent generates this |
| 6 | Item Type | `item` | `item` for parent, `variation` for child |
| 7 | Price | *(updated)* | New price if changed |
| 8 | Description | *(optimized)* | Agent generates this |
| 9 | Dietary | *(inferred)* | `veg`, `non-veg`, or `egg` |
| 10 | Short Code | *(from POS)* | Keep original |
| 11 | Sap Code | | Leave blank |
| 12 | HSN Code | | Leave blank |
| 13 | Weight | | Leave blank |
| 14 | Weight Unit | | Leave blank |
| 15 | Rank | `1` | |
| 16 | Packing Charges | `0` | |
| 17 | Expose in Captain | `Yes` | |
| 18 | Goods/Services | `services` | |
| 19 | Short Code Two | | Leave blank |
| 20 | Allow Decimal Qty | `Yes` | |
| 21 | Manufacturing Date (DD-MM-YYYY) | | Leave blank |
| 22 | Expiry Date (DD-MM-YYYY) | | Leave blank |
| 23 | Dine-In QR | `Yes` | |

### Schema B: "Add New Items" (30 Columns)

Use this for creating brand-new items that don't exist in the POS.

| # | Column Name | Default | Notes |
|---|------------|---------|-------|
| 1 | Name | *(item name)* | 🔴 First row = parent item name |
| 2 | Online_Name | *(optimized)* | Agent generates this |
| 3 | Description | *(optimized)* | Agent generates this |
| 4 | Short_Code | *(generated)* | First letters of each word, unique |
| 5 | Short_Code_2 | | Leave blank |
| 6 | Sap_Code | | Leave blank |
| 7 | HSN_Code | | Leave blank |
| 8 | Parent_Category | `Chinese` | From brand config |
| 9 | Category | *(mapped)* | Use Category Map below |
| 10 | Category_online_display | *(same as Name)* | |
| 11 | Price | *(price)* | Set to `0` if item has variations |
| 12 | Attributes | *(inferred)* | `veg`, `non-veg`, or `egg` |
| 13 | Goods_Services | `services` | |
| 14 | Unit | `dish` | |
| 15 | is_Self_Item_Recipe | `0` | |
| 16 | minimum_stock_level | `0` | |
| 17 | at_par_stock_level | `0` | |
| 18 | Rank | `1` | |
| 19 | Packing_Charges | `0` | |
| 20 | Allow_Decimal_Qty | `No` | |
| 21-24 | Addon_Group_* | | Leave blank |
| 25 | Variation_group_name | `Size` | Only if item has Half/Full |
| 26 | Variation | `Half` or `Full` | |
| 27 | Variation_Price | *(actual price)* | |
| 28 | Variation_Sap_Code | | Leave blank |
| 29 | Variation_Packing_Charges | `0` | |
| 30 | # addon in variation | | Leave blank |

---

## 🔄 VARIATION LOGIC (Portion Engineering)

When an item has multiple portions or types (e.g., Half/Full, Dry/Gravy), apply these structural rules to link them correctly.

### 1. The 3-Row Architecture (Parent-First)
To maintain POS data integrity and correctly link variations on Zomato:
- **Structure**: Every item with portions MUST have:
    1. **Parent Row**: `Item Type` = `item`, `Price` = `0`. `Item Name` = `{Core Name}`.
    2. **Variation Row (Full)**: `Item Type` = `variation`, `Price` = `Full_Price`. `Item Name` = `{Core Name} (Full)`.
    3. **Variation Row (Half)**: `Item Type` = `variation`, `Price` = `Half_Price`. `Item Name` = `{Core Name} (Half)`.

### 2. ID Preservation Logic
- **Existing Items**:
    - If the POS has an `Item ID` for the parent or any variation, that row MUST go to the **Update Existing Items** sheet.
    - Match existing `Variation_Price` to the new price from the update source.
- **New Variations**:
    - If a portion (e.g., Half) is missing from the POS, it goes to the **Add New Items** sheet.
    - **Linking in Add New**: List the **Parent Name** in the first row, then the **Variation Rows** below it. For new variations, the `Name` column MUST be `{Parent Name} ({Variation})`.

### 3. Online Name & SEO
- **Parent Row**: `Online Display Name` = `{Item Name}`.
- **Variation Rows**: `Online Display Name` = `{Item Name} ({Variation})`. Include SEO badges like `(8 Pcs)`.

### 2. Variation Types
1. **Portion Size**: Half, Full.
2. **Preparation**: Dry, Gravy.
3. **Quantity**: 6 Pcs, 10 Pcs.

---

## ➕ ADDON & GROUP MANAGEMENT

Addons are managed via "Addon Groups" mapped in columns 21-24 of Schema B.

### Standard Groups:
- **Customisation**: Extra Cheese, No Onion/Garlic, Extra Spicy.
- **Dips**: Spicy Red Chutney, Mint Mayo, Soy Sauce.
- **Portion Size**: (Used as a variation group, but can be a selection if prices are flat).

---

## 🗂️ CATEGORY MAP (Agent MUST Use This)

When classifying items into categories, the agent matches keywords in the item name to the correct Petpooja category:

| Keywords in Item Name | Real Petpooja Category |
|----------------------|----------------------|
| momo, steam, firestix, kurkure (momo context), tandoori (momo context), afgani (momo context), chilli momo | `Momo'S Pagluu (8 Pcs)` |
| chaap, malai chaap, tandoori chaap, kurkure chaap, achaari chaap, afgani chaap, haryali chaap, masala chaap | `Tandoor Se` |
| pasta, alfredo, arrabiata, sauce pasta, white sauce, red sauce, mix sauce, mushroom sauce | `Continental` |
| noodle, noodles, rice, hakka, schezwann, singapore, fried rice, egg rice | `Noodles & Rice` |
| box | `Wok Boxes` |
| platter, mania, feast | `Signature Platters` |
| soup, fries, spring roll, manchurian, chilli (non-momo context), drums, pepper corn | `Starters` |
| *(no match / default)* | `Starters` |

---

## 🔍 MATCHING RULES (Agent Applies These)

When comparing a new/update item name against existing POS items:

### Step 1: Token-Set Normalization
- Lowercase both names.
- Normalize synonyms: `momo` = `momos`, `steamed` = `steam`, `chilly` = `chilli`, `patoto` = `potato`, `noodles` = `noodle`.
- Remove piece counts: `\s*\(\s*\d+\s*pcs\s*\)`.
- Extract unique tokens: `set(re.findall(r'\w+', name))`.
- Match if tokens are a subset or identical.

### Step 2: Multi-pronged Search
The agent performs matching in this order:
1. **Direct Match**: Cleaned Name + Variation.
2. **Token Match**: Comparing normalized token sets.
3. **Short Code Match**: First letters of each word + Variation.
4. **ID Lookup**: Direct match by Item ID if available.

### Step 3: Safety Guard
Every item identified as an "Add" MUST be cross-checked against the POS using the above logic. If a match is found, it MUST be re-routed to the "Update" list to prevent "Already Assigned" errors.

---

## ✨ OPTIMIZATION RULES (Agent Applies These)

### Title Optimization
Generate an `Online Display Name` that is search-friendly and descriptive:

| Item Type | Template | Example |
|-----------|----------|---------|
| Steamed Momo | `{Protein} Steamed Momos (8 Pcs)` | Veg Steamed Momos (8 Pcs) |
| Fried Momo | `{Protein} Crispy Fried Momos (8 Pcs)` | Chicken Crispy Fried Momos (8 Pcs) |
| Kurkure Momo | `{Protein} Crunchy Kurkure Momos (8 Pcs)` | Paneer Crunchy Kurkure Momos (8 Pcs) |
| Tandoori Momo | `{Protein} Smoky Tandoori Momos (8 Pcs)` | Chicken Smoky Tandoori Momos (8 Pcs) |
| Afghani Momo | `{Protein} Creamy Afghani Momos (8 Pcs)` | Paneer Creamy Afghani Momos (8 Pcs) |
| Chilli Momo | `{Protein} Pan-Fried Chilli Momos (8 Pcs)` | Veg Pan-Fried Chilli Momos (8 Pcs) |
| Noodle | `{Protein} {Style} Noodles` | Chicken Singapore Noodles |
| Rice | `{Protein} {Style} Rice` | Egg Schezwann Rice |
| Chaap | `{Style} Chaap` | Afghani Chaap |
| Pasta | `{Protein} {Sauce} Pasta` | Chicken Red Sauce Pasta |
| Soup | `{Name} Soup` | Hot & Sour Soup |
| Starter | Keep original name | Peri Peri Fries |

### Description Templates

| Category | Description |
|----------|------------|
| Steamed Momo | Traditional Himalayan style steamed momos, thin-wrapped and stuffed with fresh fillings. Served with our signature spicy red chutney. |
| Fried Momo | Golden-fried to perfection! These crispy momos offer a satisfying crunch with every bite. Served with spicy dip. |
| Kurkure Momo | Our best-seller! Momos coated in a secret crunchy batter and deep-fried for the ultimate crunch experience. |
| Tandoori Momo | Momos marinated in authentic tandoori masala and charred in the clay oven for that perfect smoky flavor. |
| Afghani Momo | Tandoor-grilled momos smothered in a rich, creamy Afghani sauce with aromatic spices. |
| Chilli Momo | Tossed in a fiery Schezwan sauce with crunchy bell peppers and onions. A spicy lover's dream! |
| Noodle | Freshly prepared {style} noodles made with wok-tossed vegetables and aromatic spices. |
| Rice | Freshly prepared {style} rice made with fragrant long-grain rice and premium ingredients. |
| Chaap | Smoky and tender soya chaap prepared with {style} marinade. A vegetarian delight! |
| Pasta | Freshly prepared {sauce} pasta made with imported Italian penne and rich sauce. |
| Soup | A warm, comforting bowl of {name} prepared fresh with every order. |
| Default | Freshly prepared {name} made with premium ingredients. A Taste The Heaven signature dish. |

---

## 🛠️ Utility Script (Thin Layer Only)

The Python utility at `/nara/resturant_ai/menu_sync.py` provides ONLY:
- `connect_sheets()` — Google Sheets API authentication
- `read_sheet(tab_name)` → Returns list of dicts
- `write_sheet(tab_name, data)` → Writes rows to sheet

---

## 📝 Workflow

Use `/menu-sync` to run the full sync workflow. See `.agent/workflows/menu-sync.md`.
