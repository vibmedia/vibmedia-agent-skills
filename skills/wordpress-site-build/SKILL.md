---
name: wordpress-site-build
description: When the user wants to follow a complete WordPress site build process from template to launch. Also use when the user mentions "site build checklist," "WordPress checklist," "build website," "website launch checklist," "pre-launch," "site setup," or "WordPress build process." For template selection, see envato-template-selection. For MCP tools, see wordpress-mcp-bundle.
category: wordpress
profile: marketing
---

# WordPress Site Build

> End-to-end WordPress build checklist — from template import through launch. No step gets skipped.

## When to Use

- Building a new WordPress website from an Elementor kit
- Following up on a selected Envato template
- Ensuring nothing is missed before website launch
- Tracking what's done vs. what's pending client data

## Before Starting

1. Is the Envato template selected? (see `envato-template-selection`)
2. Are all required plugins sourced from Google Drive?
3. Is the WordPress site set up with hosting access?
4. Do we have client data (or know what's pending)?
5. Are MCPs checked and running? (see `wordpress-mcp-bundle`)

## Core Framework

### MCP Toggle Guide

> Enable only the MCPs needed for the current phase.

| Phase | Elementor MCP | WordPress MCP | JetEngine MCP |
|-------|:------------:|:-------------:|:-------------:|
| 1. Setup | ❌ | ✅ | ❌ |
| 2. Import | ✅ | ✅ | ❌ |
| 3. Build | ✅ | ✅ | If dynamic |
| 4. SEO | ❌ | ✅ | ❌ |
| 5. Pre-Launch | ✅ | ✅ | If dynamic |

### Phase 1: Setup (Foundation)

- [ ] 1.1 WordPress installed and accessible
- [ ] 1.2 SSL certificate active (HTTPS)
- [ ] 1.3 PHP version 8.0+ confirmed
- [ ] 1.4 WordPress updated to latest version
- [ ] 1.5 Delete default content (Hello World post, sample page)
- [ ] 1.6 Set permalink structure to "Post name"
- [ ] 1.7 Set timezone, date/time format
- [ ] 1.8 Disable search engine visibility (until launch)
- [ ] 1.9 Install required plugins from Google Drive
- [ ] 1.10 Activate Elementor Pro + required add-ons
- [ ] 1.11 Upload and activate child theme (if applicable)

### Phase 2: Template Import

- [ ] 2.1 Import Elementor Kit (ZIP or from library)
- [ ] 2.2 Verify all template pages imported correctly
- [ ] 2.3 Verify global styles applied (fonts, colors, buttons)
- [ ] 2.4 Check header template is assigned globally
- [ ] 2.5 Check footer template is assigned globally
- [ ] 2.6 Fix any broken/missing widgets or images
- [ ] 2.7 Set up menus (primary navigation, footer links)

### Phase 3: Content & Pages

- [ ] 3.1 **Home page** — Hero, services overview, CTA, testimonials
- [ ] 3.2 **About page** — Company story, team, mission, values
- [ ] 3.3 **Services pages** — One page per service (or dynamic via CPT)
- [ ] 3.4 **Contact page** — Form, map embed, address, phone, hours
- [ ] 3.5 **Blog/News** — Archive and single post templates
- [ ] 3.6 **Other pages** — Portfolio, gallery, pricing, FAQ (per project)
- [ ] 3.7 Replace all placeholder images with client images
- [ ] 3.8 Replace all Lorem Ipsum with real content
- [ ] 3.9 Set featured images for all pages
- [ ] 3.10 Configure contact form (to correct email, with confirmation)
- [ ] 3.11 Set up CTAs with correct links/phone numbers
- [ ] 3.12 Add Google Maps embed (contact page)
- [ ] 3.13 Mark PENDING items explicitly for client data not yet received

### Phase 4: SEO & Performance

- [ ] 4.1 Install SEO plugin (Yoast or Rank Math)
- [ ] 4.2 Set meta title for every page (50-60 chars)
- [ ] 4.3 Set meta description for every page (150-160 chars)
- [ ] 4.4 Set focus keyword per page
- [ ] 4.5 Verify H1-H6 heading hierarchy on each page
- [ ] 4.6 Add alt text to all images
- [ ] 4.7 Submit XML sitemap to Google Search Console
- [ ] 4.8 Configure robots.txt (allow indexing, block admin)
- [ ] 4.9 Add schema markup (LocalBusiness, Organization, BreadcrumbList)
- [ ] 4.10 Set up Google Analytics (GA4) tracking
- [ ] 4.11 Install caching plugin (WP Rocket, LiteSpeed, etc.)
- [ ] 4.12 Optimize images (WebP, lazy loading, compression)
- [ ] 4.13 Enable Gzip/Brotli compression
- [ ] 4.14 Test Core Web Vitals (LCP < 2.5s, CLS < 0.1)

### Phase 5: Pre-Launch

- [ ] 5.1 Test all forms (submission, email delivery, confirmation)
- [ ] 5.2 Test all buttons and links (no 404s)
- [ ] 5.3 Test mobile responsiveness (3 screen sizes minimum)
- [ ] 5.4 Test browser compatibility (Chrome, Firefox, Safari)
- [ ] 5.5 Add favicon (site icon)
- [ ] 5.6 Add privacy policy page
- [ ] 5.7 Add terms of service page (if applicable)
- [ ] 5.8 Add cookie consent banner (for GDPR/compliance)
- [ ] 5.9 Remove "Powered by WordPress" or theme credits
- [ ] 5.10 Secure wp-admin (limit login attempts, strong password)
- [ ] 5.11 Set up automated backups
- [ ] 5.12 Enable search engine visibility (allow indexing)
- [ ] 5.13 Final visual review of all pages (desktop + mobile)
- [ ] 5.14 Client approval via `client-coordinator`
- [ ] 5.15 🚀 LAUNCH

### Staged Delivery Protocol

> Don't wait for all client data. Build around it.

| Status | Action | Marker |
|--------|--------|--------|
| Data received | Use it immediately | ✅ |
| Data pending | Add placeholder with visible marker | `[PENDING: Company Logo]` |
| Data irrelevant | Skip section, note in build log | ⏭️ |

**Pending tracking:** Maintain a `pending-items.md` in the project root directory.
Whenever a step requires client input/approval, mark it as `[PENDING]` on the checklist and log the required item in `pending-items.md`. Proceed with other non-blocking steps.

## Output Format

### Build Progress Report
```
## Build Progress — [Client Name] — [Date]

### Completion: X%
| Phase | Status | Items Done |
|-------|--------|-----------|
| 1. Setup | ✅ Complete | 11/11 |
| 2. Import | ✅ Complete | 7/7 |
| 3. Content | 🔄 In Progress | 8/13 |
| 4. SEO | ⏳ Pending | 0/14 |
| 5. Pre-Launch | ⏳ Pending | 0/15 |

### Pending Items
- [ ] Company logo (blocks: header, favicon)
- [ ] Service descriptions (blocks: service pages)
```

## Common Mistakes

- ❌ Skipping the checklist ("I'll remember") — you won't
- ❌ Leaving Lorem Ipsum in production (check EVERY page)
- ❌ Not testing forms (most common launch-day bug)
- ❌ Launching without SEO setup (lost ranking opportunity)
- ❌ Waiting for all client data to start (use staged delivery)
- ❌ Not disabling indexing during development (Google indexes WIP content)

## Related Skills

- **envato-template-selection**: Template selection before this skill takes over
- **wordpress-mcp-bundle**: MCP tools used during build
- **seo-fundamentals**: SEO principles for Phase 4
- **schema-markup**: Structured data for Phase 4
- **client-communication**: Pending items and approval workflows
