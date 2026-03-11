---
name: business-listing
description: When the user wants to create, manage, or automate business listings on external marketplace platforms. Also use when the user mentions "listing," "marketplace listing," "product listing," "restaurant listing," "platform listing," "listing automation," or any specific marketplace platform name. For Google My Business, see google-my-business. For local SEO citations, see local-seo.
category: marketing
profile: marketing
---

# Business Listing

> Create and manage business listings on external platforms using the harness pattern for repeatability and token savings.

## When to Use

- Creating a new business listing on any platform
- Setting up a restaurant on food delivery platforms
- Listing products on e-commerce marketplaces
- Managing existing listings across platforms
- Automating repetitive listing creation

## Before Starting

1. Which platform(s) does this business need?
2. Do we have login credentials or will we need OTP flow?
3. What documents are required? (business license, tax ID, brand auth, etc.)
4. Are images ready in Google Drive? Meeting platform specs?
5. Is the listing data verified by the client?
6. Do we have a crystallized script for this platform, or is this a Golden Run?

## Core Framework

### The Harness Pattern (MANDATORY)

> 🔴 **Every new platform goes through 3 phases. No exceptions.**

| Phase | Name | What Happens | Output |
|-------|------|-------------|--------|
| 1 | **Golden Run** | Browser agent processes one listing manually, maps all UI elements | `golden-run-notes.md` |
| 2 | **Crystallize** | Agent writes Playwright script + rules file | `listing_script.py` + `listing_rules.md` |
| 3 | **Execute** | Run script with variable data, near-zero token cost | Listing confirmation + screenshot |

### Phase 1: Golden Run Checklist

During the Golden Run, document:
- [ ] Login URL and authentication flow
- [ ] Every form field with its selector (ID, name, class)
- [ ] Required vs. optional fields
- [ ] File upload mechanisms (images, documents)
- [ ] Character limits for text fields
- [ ] Any CAPTCHA or bot detection
- [ ] OTP/verification triggers and timing
- [ ] Submit button and confirmation page
- [ ] Error messages and validation rules

### Phase 2: Crystallize Template

```python
# listing_script.py — Template structure
from playwright.sync_api import sync_playwright

def create_listing(data: dict):
    """
    data = {
        "business_name": "...",
        "address": "...",
        "phone": "...",
        "category": "...",
        "images": ["path1.jpg", "path2.jpg"],
        "description": "...",
        # ... platform-specific fields
    }
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        # ... scripted steps from Golden Run
```

### Phase 3: Rules File Template

```markdown
# listing_rules.md — [Platform Name]

## Field Constraints
| Field | Max Length | Required | Format |
|-------|-----------|----------|--------|
| Name | 60 chars | Yes | Title Case |
| Description | 500 chars | Yes | No HTML |
| Phone | 10 digits | Yes | No country code |

## Image Requirements
| Type | Size | Format | Required |
|------|------|--------|----------|
| Logo | 400x400 | PNG/JPG | Yes |
| Cover | 1200x628 | JPG | Yes |
| Menu | Any | JPG/PDF | Yes (restaurants) |

## Verification
- [ ] Screenshot final preview before submitting
- [ ] Human approves screenshot
- [ ] Submit only after approval
```

### Platform Quick Reference

> 📌 **Platform-specific requirements should be documented in `brands/[industry]/_common/industry.md`.**
> Below is a generic template — populate per platform during the Golden Run.

| Platform Type | Examples | Typical Documents | OTP Required |
|---------------|----------|------------------|--------------|
| Food delivery | DoorDash, UberEats, regional apps | Food license, menu photos, bank details | Usually yes |
| E-commerce | Amazon, regional marketplaces | Tax ID, product images, brand auth | Usually yes |
| Local directory | Yelp, regional directories | Business proof, address proof | Varies |

### OTP Flow Integration

```
Browser Agent → "OTP sent to client"
    ↓
Client Coordinator → WhatsApp: "OTP sent to your phone for [Platform]. Please share."
    ↓
Client → Replies with OTP
    ↓
Client Coordinator → Relays to Browser Agent
    ↓
Browser Agent → Enters OTP, completes login
```

**Timeouts:**
- Wait 5 minutes for OTP response
- Send 1 reminder after 3 minutes
- After 5 minutes → flag as BLOCKED
- After 24 hours → escalate to human

## Data Collection via Google Sheets

For bulk listings, use Google Sheets with standardized columns:

| Column | Example |
|--------|---------|
| Business Name | [Client business name] |
| Address | [Full formatted address] |
| Phone | [Phone with country code] |
| Category | [Platform category path] |
| License/Tax ID | [Country-specific business license] |
| Description | [Business description] |
| Images Folder | [Google Drive link] |
| Status | PENDING / SUBMITTED / VERIFIED |

## Output Format

### Per Listing
```
## Listing Created — [Platform] — [Business Name]

- Platform: [Platform name]
- Status: SUBMITTED ✅
- URL: [listing URL]
- Submitted: 2026-03-11
- Screenshot: [path]
- Verified by: [human name]
```

## Common Mistakes

- ❌ Doing a second listing manually instead of crystallizing after Golden Run
- ❌ Submitting listings without human verification
- ❌ Ignoring platform-specific character limits (causes rejections)
- ❌ Using wrong image dimensions (each platform has different specs)
- ❌ Not handling OTP timeout gracefully (blocks entire workflow)
- ❌ Hardcoding business data in scripts (use variables/JSON)

## Related Skills

- **google-my-business**: For GMB profile management (not a marketplace listing)
- **local-seo**: For citation building across directories
- **client-communication**: For OTP relay and data collection
- **copywriting**: For listing descriptions and product copy
