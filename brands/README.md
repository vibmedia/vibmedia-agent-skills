# 🏢 Brand Context System

> Persistent project context that AI agents use across sessions. One folder per brand/client.

---

## Why This Exists

AI agents lose context between sessions. This system solves that by keeping **everything an agent needs to know** about a brand/client in a structured folder. When an agent starts working, it reads the brand folder first — no repeat questions, no lost context.

---

## Structure

```
brands/
├── _template/                    # Copy this for new brands
│   ├── context.md                # Brand identity + AI instructions
│   ├── todo.md                   # Progress tracking
│   ├── reference/                # Raw client inputs
│   │   └── .gitkeep
│   ├── brand-data/               # Processed brand assets
│   │   └── .gitkeep
│   └── artifacts/                # AI-generated deliverables
│       └── .gitkeep
│
├── acme-corp/                    # Example: SaaS client
│   ├── context.md
│   ├── todo.md
│   ├── reference/
│   │   ├── client-brief.pdf
│   │   ├── competitor-screenshots/
│   │   └── meeting-notes-2026-02.md
│   ├── brand-data/
│   │   ├── logo.svg
│   │   ├── brand-guidelines.md
│   │   ├── services.md
│   │   └── contacts.md
│   └── artifacts/
│       ├── landing-page-v1/
│       ├── seo-audit-2026-02.md
│       └── campaign-brief-q1.md
│
└── README.md                     # This file
```

---

## Quick Start

### 1. Create a brand folder

```bash
cp -r brands/_template brands/your-client-name
```

### 2. Fill in `context.md`

Answer the prompts in the template. Takes 10-15 minutes.

### 3. Start working

```
You: "Write homepage copy for acme-corp"
AI:  → Reads brands/acme-corp/context.md
     → Loads copywriting skill
     → Writes copy using brand voice, audience, and product details
     → No repeated questions needed
```

---

## Folder Breakdown

### `context.md` — Brand Identity + AI Instructions

The **single most important file**. Contains everything an agent needs:
- What the company does
- Who the customers are
- Brand voice and positioning
- Products/services and pricing
- Competitive landscape

### `reference/` — Raw Client Data

Unprocessed inputs from the client:
- Client briefs, SOWs, meeting notes
- Competitor screenshots, market research
- Raw data, spreadsheets
- Email threads, requirements docs

**Rule:** Drop files here as-is. Don't spend time organizing — this is the "inbox".

### `brand-data/` — Processed Brand Assets

Cleaned, organized brand materials:
- Logos (SVG, PNG)
- Brand guidelines (colors, fonts, do/don'ts)
- Product/service descriptions
- Contact information
- Team structure

**Rule:** These should be AI-readable (markdown preferred, not just PDFs).

### `todo.md` — Progress Tracking

Living document tracking:
- What's been done
- What's in progress
- What's planned next
- Decisions made + rationale

### `artifacts/` — AI-Generated Deliverables

Everything the AI has produced for this brand:
- Landing pages, email campaigns
- SEO audits, CRO analyses
- Campaign briefs, content plans
- Code, designs, reports

**Rule:** Organize by project or date. Never delete — keep the history.

---

## Industry Templates

The `context.md` template works for any industry. Here's how the same structure adapts:

### SaaS Company

```markdown
## Product
- Core product: Project management SaaS
- Pricing: Free / Pro $29/mo / Enterprise custom
- Key differentiator: AI-powered task estimation
- Value metric: Per user/month
```

### E-commerce Brand

```markdown
## Product
- Product type: Sustainable fashion
- Price range: $50-$200
- Key differentiator: Carbon-neutral supply chain
- Fulfillment: Shopify + 3PL
```

### Service Agency

```markdown
## Services
- Core services: Web development, SEO, paid ads
- Pricing model: Retainer ($5k-$20k/mo)
- Key differentiator: Performance guarantees
- Team size: 15 people
```

### Startup (Pre-revenue)

```markdown
## Product
- Stage: MVP / Beta
- Core product: [Description]
- Target launch: Q2 2026
- Funding: Bootstrapped / Seed
- Key hypothesis: [What you're testing]
```

---

## Multi-Brand Workflow

When working across brands in the same project:

```bash
# Structure
project/
├── .agent/           # AI skills and agents (shared)
└── brands/           # Per-brand context (isolated)
    ├── brand-a/
    ├── brand-b/
    └── brand-c/
```

**Switching brands:**
```
You: "Switch to acme-corp. Write their Q2 email sequence."
AI:  → Reads brands/acme-corp/context.md
     → Loads email-sequence skill
     → Uses acme-corp's voice, audience, products
```

**Cross-brand work:**
```
You: "Compare SEO performance across all brands"
AI:  → Reads context.md from each brand folder
     → Loads seo-audit skill
     → Produces comparative analysis
```

---

## Tips

1. **Fill `context.md` thoroughly** — 30 minutes upfront saves hours of repeated questions
2. **Keep `reference/` messy, `brand-data/` clean** — reference is raw input, brand-data is processed
3. **Update `todo.md` after every session** — your future self (and AI) will thank you
4. **Store artifacts with dates** — `seo-audit-2026-02.md` not just `seo-audit.md`
5. **Use markdown over PDFs** — AI reads markdown 10x better than PDFs
6. **One brand = one folder** — never mix brand contexts
