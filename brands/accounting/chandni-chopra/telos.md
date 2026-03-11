# Telos Context File — Chandni Chopra and Associates

> Replaces `todo.md`. Captures mission, goals, strategies, current state, and streaming activity log.

---

## Document Purpose

This Telos Context File (TCF) captures the full context for **Chandni Chopra and Associates**. It is used by the AI to:

- Shape all recommendations and deliverables
- Track goals, KPIs, and project progress
- Maintain a streaming activity log (past → present → future)
- Make informed decisions based on current state, not just initial context

---

## Entity Overview

- **Name:** Chandni Chopra and Associates
- **Industry:** Accounting & Finance
- **Profile:** hybrid
- **Founded:** N/A
- **Team Size:** 3 Partners
- **Stage:** Established

---

## Mission

To deliver a high-quality, fully functional, 40+ page website for the CA firm within a strict 1-hour deadline by eliminating manual data entry and using dynamic templates.

---

## Goals (G1 is highest priority; each subsequent goal is half as important)

- G1: Launch 40+ page website within the 1-hour deadline.
- G2: Complete JetEngine/Crocoblock CPT integration for Services and map to the Counter template manually.
- G3: Import bulk content via CSV to populate Services pages.
- G4: Optimize content for Delhi CA local SEO ("CA firm in Delhi", "Tax consultant near me", "GST registration Delhi", etc.).
- G5: Future-proof the build for a domain change ensuring all paths are relative/dynamic.

---

## KPIs (How We Measure Progress)

| ID  | Metric        | Target         | Current         | Status   |
| --- | ------------- | -------------- | --------------- | -------- |
| K1  | Pages created | 40+            | 0               |        |
| K2  | Time elapsed  | < 1 hour       | Active          |        |
| K3  | CPTs imported | 100%           | 0%              |        |

---

## Strategies

- S1: Generate content programmatically inside a CSV matched exactly to Elementor template dummy text lengths.
- S2: Utilize the new `@crocoblock-specialist` agent methodology to set up the Custom Post Type (CPT) and Meta Fields.
- S3: Import CSV into WordPress using WP All Import to automatically generate the pages.
- S4: Target local Delhi keywords (e.g., "Best CA in Delhi", "Accounting services Delhi", "Income tax filing East Krishna Nagar") in headings and content.
- S5: Implement dynamic mapping (Elementor Dynamic Tags) so changing the domain name doesn't break internal text or button links.

---

## Risk Register (What We're Most Worried About)

| Risk     | Impact       | Likelihood   | Mitigation |
| -------- | ------------ | ------------ | ---------- |
| Missed 1-hr deadline | High | Med | Pre-generate all precise content in Python directly to CSV. |
| Text overflows in UI | Med  | Med | Character and word counts strictly match the provided template limits. |
| CSV import failure   | High | Low | Use standard WP All Import mapping with clear column headers. |

---

## Tech Stack / Infrastructure

- **Frontend:** Elementor (WordPress)
- **Backend:** WordPress
- **Database:** JetEngine Custom Meta Fields
- **Auth:** WP Admin
- **Integrations:** WP All Import

---

## Team

| Name   | Role   | Skills       | Focus Area         |
| ------ | ------ | ------------ | ------------------ |
| Chandni Chopra | Managing Partner | Audits, Compliance | Firm leadership |
| AI Agent | Developer/Marketer | Python, Elementor, Copywriting | Web dev, data import, SEO |

---

## Active Projects

| Project     | Priority    | Owner  | Start  | End    | Status      | Notes   |
| ----------- | ----------- | ------ | ------ | ------ | ----------- | ------- |
| Website Setup | 🔴 Critical | AI Agent | Today | Today | In Progress | 1-hour deadline |

---

## Current State — Activity Log

> **Streaming updates.** Newest entries at the top. These override any conflicting information above.
> Format: `- [YYYY-MM-DD]: [Update]`

- 2026-03-10: User manually configured and finalized the Elementor Single Service template mapping.
- 2026-03-10: Saved premium plugins Google Drive link to context.md for future use.
- 2026-03-10: User paused WP All Import. Updated strategy: We must build the Elementor Single Service Template and manually populate ONE service post to verify the design before returning to bulk generation.
- 2026-03-10: JetEngine `Services` Custom Post Type has been created with all 17 required meta fields for the template.
- 2026-03-10: Created `@crocoblock-specialist` agent to assist with JetEngine dynamic mapping based on the Counter template.
- 2026-03-10: Audited `cachandnichopra.com`. Found it has template data ("Counter" theme) with all nav links pointing to `#` or `/`. All 40+ service pages and core pages (About, Contact) are pending mapping.
- 2026-03-10: Added local SEO target keywords targeting Delhi and the East Krishna Nagar area.
- 2026-03-10: Added Future Domain Change prevention strategy to ensure no hardcoded URLs are used in the build.
- 2026-03-10: Brand setup and Telos initialization in `.agent/brands/accounting/chandni-chopra`.
- 2026-03-10: Generated 40-row `services_import.csv` with dynamically sized content via Python script `generate_services_csv.py`.

---

*Last updated: 2026-03-10*
