---
name: local-seo
description: When the user wants to optimize for local search, build citations, improve local pack rankings, or audit NAP consistency. Also use when the user mentions "local SEO," "local rankings," "citation building," "NAP audit," "local pack," "map pack," "local search optimization," "service area," or "local content." For Google My Business profile management, see google-my-business. For technical/on-page SEO, see seo-audit.
category: seo
profile: marketing
---

# Local SEO

> Dominate local search results through citations, NAP consistency, and local content strategy.

## When to Use

- Setting up local SEO for a new business
- Auditing existing local search presence
- Building or fixing citation profiles
- Improving local pack (map pack) rankings
- Creating location-specific content strategy

## Before Starting

1. What is the business type? (single location, multi-location, service area)
2. What's the primary service area / target geography?
3. Is the GMB profile claimed and verified?
4. Do we have the correct NAP (Name, Address, Phone)?
5. What are the target local keywords?

## Core Framework

### Local Ranking Factors

| Factor | Weight | Action |
|--------|--------|--------|
| Google My Business signals | 36% | Optimize profile (see `google-my-business` skill) |
| On-page signals | 34% | Local keywords in title, H1, content, schema |
| Citation signals | 7% | NAP consistency across top sources |
| Review signals | 17% | Volume, velocity, diversity, response rate |
| Link signals | 13% | Local backlinks, chamber of commerce, sponsors |
| Behavioral signals | 11% | CTR, mobile clicks-to-call, driving directions |
| Personalization | 6% | Proximity, search history |

### NAP Consistency Protocol

> 🔴 NAP must be IDENTICAL everywhere. Even small differences hurt rankings.

| Element | Rule | Example |
|---------|------|---------|
| Name | Exact legal business name, no keyword stuffing | "[Business]" not "[Business] - Best [Service] in [City]" |
| Address | Exact same format everywhere | "42, Main Road, Suite 12" not "42 Main Rd, Ste 12" |
| Phone | Include country code, consistent format | "+[code] [number]" everywhere |

### Citation Building

> 📌 **Country-specific citation sources should be defined in `brands/[industry]/_common/industry.md`.**
> The framework below shows priority tiers — populate with sources from the brand/industry context.

| Priority | Source | Type |
|----------|--------|------|
| P0 | Google My Business | Must have |
| P0 | Google My Business | Must have (all regions) |
| P0 | [Country directory 1] | Must have (from industry context) |
| P0 | [Country directory 2] | Must have (from industry context) |
| P1 | [Industry directory] | Industry-specific |
| P1 | Yelp / [Regional equivalent] | Reviews |
| P1 | Facebook Business | Social |
| P2 | Bing Places | Search |
| P2 | Apple Maps | Maps |
| P2 | [Country yellow pages] | Directory |
| P2 | Foursquare | Location |
| P3 | Industry-specific directories | Varies |

### Local Content Strategy

| Content Type | Purpose | Example |
|--------------|---------|---------|
| Location pages | Rank for "[service] in [city]" | "[Service] in [City Name]" |
| Service area pages | Cover each service area | One page per city/neighborhood |
| Local blog posts | Local events, community | "Best [Services] Near [Landmark]" |
| FAQ pages | Answer local queries | "How much does [service] cost in [City]?" |

### Local SEO Audit Checklist

- [ ] GMB profile complete and verified
- [ ] NAP consistent across top 30 citations
- [ ] Local keywords in page titles and H1s
- [ ] Local schema markup (LocalBusiness, Service)
- [ ] Location pages for each service area
- [ ] Embedded Google Map on contact page
- [ ] Local backlinks from relevant sources
- [ ] Review strategy in place (see `google-my-business`)
- [ ] Mobile-optimized (click-to-call, directions)
- [ ] Local content published regularly

## Output Format

### Local SEO Audit Report
```
## Local SEO Audit — [Business Name]

### NAP Score: X/10
- Name consistency: ✅/❌
- Address consistency: ✅/❌
- Phone consistency: ✅/❌

### Citation Score: X/30
- Found on: [list of sources]
- Missing from: [list of sources]
- Inconsistencies: [list]

### Recommendations (Prioritized)
1. [P0] Fix NAP on [source]
2. [P1] Create listing on [missing source]
3. [P2] Create location pages for [areas]
```

## Common Mistakes

- ❌ Different NAP on different platforms
- ❌ Keyword stuffing in GMB business name
- ❌ Creating one page for all locations (need separate pages)
- ❌ Ignoring reviews (both getting them and responding)
- ❌ Not including local schema markup on pages
- ❌ Using a virtual address instead of real business address

## Related Skills

- **google-my-business**: For GMB profile management, reviews, posts
- **seo-audit**: For technical/on-page SEO issues
- **schema-markup**: For LocalBusiness structured data
- **copywriting**: For location page content
