---
category: industry-knowledge
industry: food-delivery
region: india
---

# Indian Food Delivery Industry Rules

This document outlines the standard operating procedures, rules, and best practices for running a cloud kitchen on Indian food delivery aggregators (Zomato, Swiggy) and managing it via Petpooja POS.

## 1. Compliance & Licensing
- **FSSAI (Food Safety and Standards Authority of India)**: Mandatory for every food business. Must be displayed on all packaging. A single FSSAI license covers the kitchen address but must be linked to ALL sub-brands operating from that kitchen on Zomato/Swiggy.
- **GST (Goods and Services Tax)**: Usually 5% for restaurants without ITC (Input Tax Credit), but aggregator commissions carry 18% GST. All menus must explicitly state if prices are inclusive or exclusive of taxes.

## 2. Multi-Brand Cloud Kitchen Strategy
- **Concept**: Operating multiple virtual restaurant storefronts (brands) from a single physical kitchen to maximize discovery and target specific niches (e.g., one brand for Momos, one for Combos, one for Chinese meals).
- **Zomato/Swiggy Rules**: Aggregators allow multiple brands from the same address, but they usually require distinct FSSAI registrations or a clear NOC tying the brands to the parent kitchen. The menus must be differentiated (at least 30-40% different items or distinct naming) to avoid shadow-banning for duplicate listings.
- **Packaging Hack**: To save costs, use generic unbranded containers with brand-specific stickers printed in-house.

## 3. Platform Rules (Zomato & Swiggy)
- **Menu Taxonomy**: Follow strict category hierarchies (e.g., Starters, Main Course, Breads, Beverages). 
- **Dietary Tags**: EVERY item must be explicitly tagged as Veg, Non-Veg, or Egg. Missing tags will cause the item to be rejected or hidden.
- **Image Specs**: 1:1 aspect ratio, high resolution, no text overlay, no watermarks. White or wooden backgrounds preferred.
- **Character Limits**: Item names usually max out at 60 characters. Descriptions max out at 140-200 characters.

## 4. Pricing Strategy (The 30% Rule)
- **Aggregator Commissions**: Zomato and Swiggy charge between 22% to 28% commission + GST on platform orders.
- **Pricing Parity vs. Markup**: To maintain margins, food delivery menus must have a strict **30% markup** over physical dine-in/takeaway prices. 
  - *Example*: Offline price ₹100 → Online base price ₹130.

## 5. Petpooja POS Ecosystem
Petpooja is the central nerve system bridging the physical kitchen and the aggregators.
- **Menu Master**: The Petpooja menu must be the EXCLUSIVE source of truth. Changes made directly on Zomato/Swiggy dashboards will get overwritten by Petpooja syncs.
- **TSV Import Schema**: Petpooja bulk menu imports strictly require a 23-column TSV format. 
  - **Crucial Rule**: The `Item ID` column must NEVER be lost. If an item is re-uploaded without its Petpooja ID, it generates a duplicate, breaking sales tracking and potentially losing Zomato item ratings.
  - Variations (Half/Full) must be listed on separate rows directly below their parent item, with the parent item having a price of `0` in the TSV.
