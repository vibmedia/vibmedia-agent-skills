---
name: google-my-business
description: When the user wants to create, optimize, or manage a Google My Business (GMB) profile, respond to Google reviews, publish Google Posts, or optimize Google Maps presence. Also use when the user mentions "Google My Business," "GMB," "Google Business Profile," "Google reviews," "Google Maps listing," "Google Posts," "business profile," or "review management." For broader local SEO strategy, see local-seo. For structured data, see schema-markup.
category: seo
profile: marketing
---

# Google My Business

> Optimize GMB profiles for maximum local visibility, manage reviews, and maintain active presence with Google Posts.

## When to Use

- Setting up a new Google My Business profile
- Optimizing an existing GMB profile for completeness
- Managing and responding to Google reviews
- Publishing Google Posts for engagement
- Setting up automated review replies via Google API

## Before Starting

1. Do we have access to the client's GMB profile? (via their email)
2. Is the profile claimed and verified?
3. What's the current profile completeness percentage?
4. What's the current review count and rating?
5. Is Google API access available for automation?

## Core Framework

### Profile Optimization Checklist

#### Basic Info (P0 — Complete First)
- [ ] Business name (exact legal name, NO keyword stuffing)
- [ ] Primary category (most impactful ranking factor)
- [ ] Secondary categories (up to 9 additional)
- [ ] Address (exact, consistent with all citations)
- [ ] Phone number (local number preferred over toll-free)
- [ ] Website URL
- [ ] Business hours (including special hours for holidays)
- [ ] Business description (750 chars max, include keywords naturally)

#### Media (P1 — Visual Trust)
- [ ] Logo (minimum 250x250px)
- [ ] Cover photo (1080x608px)
- [ ] Interior photos (3-5 minimum)
- [ ] Exterior photo (helps customers find the location)
- [ ] Team photos (builds trust)
- [ ] Product/service photos (5-10 minimum)
- [ ] Video (30 seconds, optional but impactful)

| Photo Type | Min Count | Specs | Purpose |
|-----------|-----------|-------|---------|
| Logo | 1 | 250x250 | Brand recognition |
| Cover | 1 | 1080x608 | First impression |
| Interior | 3+ | 720p+ | Space feel |
| Exterior | 1 | 720p+ | Wayfinding |
| Team | 2+ | 720p+ | Human trust |
| Products | 5+ | 720p+ | Showcase offering |

#### Extended Info (P2 — Completeness Score)
- [ ] Service list with descriptions
- [ ] Products/menu items (if applicable)
- [ ] Attributes (wheelchair accessible, Wi-Fi, etc.)
- [ ] Booking link (if applicable)
- [ ] Appointment URL (if applicable)
- [ ] From the business description (direct response area)

### Category Selection Guide

| Business Type | Primary Category | secondaries |
|--------------|-----------------|-------------|
| Restaurant | Restaurant | [Cuisine] Restaurant, Delivery Restaurant |
| Plumber | Plumber | Emergency Plumber, Water Heater Repair |
| Accountant | Accounting Firm | Tax Preparation, Bookkeeper |
| Salon | Beauty Salon | Hair Salon, Nail Salon |

> **Rule:** Primary category drives 90% of local ranking. Choose the most specific one.

### Review Management

#### Response Templates

**Positive Review (4-5 stars):**
```
Thank you so much, [Name]! We're glad you enjoyed [specific thing they mentioned].
Looking forward to seeing you again. 😊
```

**Neutral Review (3 stars):**
```
Thank you for your feedback, [Name]. We appreciate you taking the time.
We'd love to know how we can improve — feel free to reach out at [email].
```

**Negative Review (1-2 stars):**
```
We're sorry to hear about your experience, [Name].
This isn't the standard we aim for. Please contact us at [email/phone]
so we can make this right. We take all feedback seriously.
```

#### Response Rules

| Rule | Rationale |
|------|-----------|
| Respond within 24 hours | Shows you care, Google rewards responsiveness |
| Mention something specific | Proves you actually read the review |
| Keep it professional | Future customers read your responses |
| Never argue publicly | Take disputes offline |
| Thank every reviewer | Even negative ones — shows maturity |
| Include business name/keyword naturally | Subtle SEO benefit |

### Google Posts Strategy

| Post Type | Frequency | Content |
|-----------|-----------|---------|
| What's New | Weekly | Business updates, news, tips |
| Event | As needed | Upcoming events with dates |
| Offer | Monthly | Special deals, coupons (with expiry) |
| Product | Bi-weekly | Highlight products/services |

**Post Best Practices:**
- Include a CTA button (Learn More, Call Now, Book)
- Use high-quality images (1200x900px ideal)
- Keep text under 300 words (100-200 words ideal)
- Include relevant keywords naturally
- Posts expire after 7 days — maintain regular schedule

### Google API Integration (When Available)

If the client has shared Google API credentials, automate:

| Task | API Endpoint | Automation Level |
|------|-------------|-----------------|
| Read reviews | `accounts.locations.reviews.list` | Full auto |
| Reply to reviews | `accounts.locations.reviews.updateReply` | Semi-auto (template + human verify) |
| Update business info | `accounts.locations.patch` | Full auto |
| Create posts | `accounts.locations.localPosts.create` | Semi-auto |
| Get insights | `accounts.locations.reportInsights` | Full auto |

> **Note:** If no API access, use browser agent with harness pattern from `local-seo-manager`.

## Output Format

### GMB Audit Report
```
## GMB Audit — [Business Name]

### Profile Completeness: X%
| Section | Status | Action |
|---------|--------|--------|
| Basic Info | ✅ Complete | — |
| Photos | ⚠️ 3/10 | Upload 7 more |
| Reviews | 23 (4.2★) | Need response template |
| Posts | None | Start weekly schedule |

### Priority Actions
1. [P0] Upload exterior and team photos
2. [P1] Respond to 5 unresponded reviews
3. [P2] Start weekly Google Posts
```

## Common Mistakes

- ❌ Keyword stuffing in business name (Google penalizes this)
- ❌ Using a PO Box or virtual address
- ❌ Not responding to reviews (kills trust + ranking signal)
- ❌ Using stock photos instead of real business photos
- ❌ Setting up and forgetting — GMB needs ongoing maintenance
- ❌ Inconsistent business hours (especially holidays)

## Related Skills

- **local-seo**: Broader local SEO strategy, citation building
- **seo-fundamentals**: Technical SEO principles
- **copywriting**: Business descriptions, review responses
- **schema-markup**: LocalBusiness structured data on website
