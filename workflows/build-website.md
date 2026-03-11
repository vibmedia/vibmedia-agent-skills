---
description: Build a complete WordPress website from template selection to launch. Orchestrates template selection, MCP setup, page building, SEO, and pre-launch checklist.
---

# /build-website — WordPress Site Build

## Prerequisites
- Client brand folder set up with `profile: marketing`
- Client requirements gathered (pages, content, design preferences)

## Steps

1. **Check MCP availability**
   - Verify Elementor MCP, WordPress MCP, and JetEngine MCP are running
   - If any are missing, install using system instructions
   - Test connection with a simple API call
   - Expected: All required MCPs responding

2. **Select template**
   - Load `envato-template-selection` skill
   - Search Envato Elements → WordPress → Filter: Elementor Kits
   - Evaluate top 3-5 with scorecard (industry fit, design, pages, plugins)
   - Present recommendation to user for approval
   - Expected: Template selected with plugin list

3. **Install plugins**
   - Cross-reference required plugins with Google Drive repository
   - Upload pro/paid plugins from Google Drive
   - Install free plugins from WordPress.org via WordPress MCP
   - Activate all plugins
   - Expected: All plugins active, no conflicts

4. **Import template kit**
   - Import Elementor kit via Elementor MCP
   - Verify all pages, headers, footers imported
   - Check global styles (fonts, colors, buttons)
   - Expected: Kit imported with global styles applied

5. **Build pages**
   - Follow `wordpress-site-build` Phase 3 checklist
   - Use Elementor MCP for page building
   - Replace placeholder content with client data
   - Mark PENDING items for missing client data
   - If dynamic content needed → delegate to `@crocoblock-specialist`
   - Expected: All pages built (or marked PENDING)

6. **SEO setup**
   - Follow `wordpress-site-build` Phase 4 checklist
   - Install SEO plugin, set meta tags, add schema
   - Submit sitemap, configure robots.txt
   - Set up GA4 tracking
   - Expected: All SEO items checked

7. **Performance optimization**
   - Enable caching, image optimization
   - Test Core Web Vitals
   - Expected: LCP < 2.5s, CLS < 0.1

8. **Pre-launch checklist**
   - Follow `wordpress-site-build` Phase 5 checklist
   - Test forms, links, mobile, browsers
   - Add favicon, privacy policy, cookie consent
   - Expected: All 15 pre-launch items checked

9. **Client approval**
   - Use `@client-coordinator` to send screenshots for approval
   - Wait for client response
   - Apply any requested changes
   - Expected: Client approves

10. **Launch**
    - Enable search engine visibility
    - Remove any "under construction" pages
    - Send launch confirmation to client
    - Expected: Site live and indexed
