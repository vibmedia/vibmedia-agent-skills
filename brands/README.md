# 🏢 Brand & Industry Context System

> Persistent project context organized by industry and brand. AI reads these before working — no repeated questions, no lost context.

---

## Structure

```
brands/
├── [industry]/                       # Any industry (create as needed)
│   ├── _common/                      # Shared industry knowledge
│   │   ├── industry.md               # Industry-specific AI instructions
│   │   └── references/               # Benchmarks, frameworks, terminology
│   ├── _brand-template/              # Copy for new brands in this industry
│   │   ├── context.md           # The primary source of truth for this brand
│   │   ├── todo.md              # Active tasks and decisions made
│   │   └── reference/           # Raw client data, interview transcripts, PDFs
│   └── [brand-name]/                 # Actual brand (copy from _brand-template)
│
├── _industry-template/               # Copy when adding a new industry
│   ├── _common/
│   │   ├── industry.md
│   │   └── references/.gitkeep
│   └── _brand-template/
│       ├── context.md
│       ├── todo.md
│       └── reference/.gitkeep
│
└── README.md                         # This file
```

---

## Adding a New Industry

```bash
# 1. Copy the industry template
cp -r brands/_industry-template brands/fintech

# 2. Edit industry knowledge
#    Fill brands/fintech/_common/industry.md with:
#    - Industry terminology and concepts
#    - Key metrics and benchmarks
#    - Common workflows and patterns
#    - Regulatory/compliance notes
#    - Technical stack preferences

# 3. Run /update to sync the system
```

## Adding a New Brand

```bash
# 1. Copy the brand template from the industry
cp -r brands/fintech/_brand-template brands/fintech/acme-pay

# 2. Fill in context.md (10-15 minutes)
# 3. Drop raw client data into reference/
# 4. Add processed assets to brand-data/
# 5. Run /update to sync the system
```

---

## How AI Uses This

```
You: "Write homepage copy for acme-pay"
AI:  1. Reads brands/fintech/_common/industry.md     ← industry context
     2. Reads brands/fintech/acme-pay/context.md      ← brand context
     3. Loads copywriting skill                        ← domain expertise
     4. Writes copy using all three layers of context
```

**Three layers of context:**
1. **Skills** — domain expertise (how to write copy in general)
2. **Industry** — sector knowledge (fintech terminology, compliance, benchmarks)
3. **Brand** — client specifics (voice, audience, products, competitors)

---

## Folder Details

### `_common/industry.md` — Industry Knowledge

Must-needed knowledge for any project in this industry:

**For tech industries:** Technical standards, architecture patterns, compliance requirements, common integrations, performance benchmarks.

**For customer-facing industries:** Customer personas, buying patterns, common objections, conversion benchmarks, regulatory requirements, seasonal patterns.

### `context.md` — Brand Identity

Everything an AI needs to know about this specific brand. See the template for all fields.

### `todo.md` — Progress Tracking

Living document with: completed work, in-progress items, planned tasks, decisions log, and ideas parking lot.

### `reference/` — Raw Materials
Place raw client data here: PDF brand guidelines, old website copy, interview transcripts, meeting notes. The AI will read this to generate new context or content.

---

## Tips

1. **Industry before brand** — fill `_common/industry.md` before adding brands
2. **Context.md is king** — 30 minutes upfront saves hours of repeated questions
3. **Use `/update` after every addition** — keeps the system in sync
4. **Use `/audit-goals` weekly** — finds gaps between todo and actual progress
5. **Use `/system-check` monthly** — catches broken references and stale data
6. **Use draw.io diagrams** — each brand gets a `structure.drawio` for visual project mapping
