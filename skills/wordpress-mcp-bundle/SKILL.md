---
name: wordpress-mcp-bundle
description: When using MCP tools to build or manage WordPress sites. Covers Elementor MCP (97+ tools), JetEngine MCP (native), and WordPress MCP (REST API). Also use when the user mentions "Elementor MCP," "wordpress MCP," "JetEngine MCP," "MCP page building," or "programmatic WordPress." For site build process, see wordpress-site-build. For template selection, see envato-template-selection.
category: wordpress
profile: marketing
---

# WordPress MCP Bundle

> MCP server reference for programmatic WordPress/Elementor/JetEngine management. Check availability first, toggle smartly.

## When to Use

- Building pages via Elementor MCP
- Managing WordPress content via REST API MCP
- Creating dynamic content via JetEngine MCP
- Any programmatic WordPress site management

## Before Starting

1. Are the required MCP servers running?
2. Do we have WordPress admin credentials?
3. What's the site URL and REST API endpoint?

## MCP Availability Check Protocol

> 🔴 **ALWAYS check before using. Install if missing.**

```bash
# Check if MCP servers are responding
# Elementor MCP
curl -s http://localhost:PORT/health || echo "Elementor MCP not running"

# WordPress MCP (stdio mode)
npx @node2flow/wordpress-mcp --help || npm install -g @node2flow/wordpress-mcp

# JetEngine MCP (built into JetEngine 3.8.0+)
# Verify via WordPress admin → JetEngine → Settings → MCP
```

### Auto-Install Protocol

| MCP Server | Install Command | Prerequisites |
|-----------|----------------|--------------|
| Elementor MCP | Per `msrbuilds/elementor-mcp` setup | WordPress MCP Adapter plugin |
| WordPress MCP | `npm install -g @node2flow/wordpress-mcp` | Node.js 18+ |
| JetEngine MCP | Built-in (JetEngine 3.8.0+) | JetEngine plugin active |

## Smart MCP Toggling

> Only enable MCPs for the active task. Disable when not needed.

| Task | Enable | Disable | Why |
|------|--------|---------|-----|
| Template import | Elementor + WordPress | JetEngine | No dynamic data yet |
| Page building | Elementor + WordPress | JetEngine (unless CPTs) | Most tools in Elementor |
| Content updates | WordPress only | Elementor + JetEngine | REST API sufficient |
| Dynamic data | JetEngine + Elementor | — | Need mapping tools |
| SEO setup | WordPress only | Elementor + JetEngine | Meta/settings only |
| Full verification | All | — | Need complete check |

## Components

### 1. Elementor MCP (Open Source)
**Server:** `msrbuilds/elementor-mcp`
**Tools:** 97+ specialized tools
**Connection:** HTTP Basic Auth via WordPress MCP Adapter

**Key Tool Categories:**

| Category | Tools | Common Use |
|----------|-------|-----------|
| Page building | `build-page`, `update-page` | Create/edit Elementor pages |
| Containers | `add-container`, `update-container` | Layout management |
| Widgets | `add-widget`, `update-widget` | Content elements |
| Theme templates | `create-theme-template` | Headers, footers, singles |
| Dynamic tags | `set-dynamic-tag` | JetEngine field binding |
| Global styles | `update-global-colors`, `update-global-fonts` | Site-wide styling |

### 2. JetEngine MCP (Native)
**Server:** Built into JetEngine 3.8.0+
**Tools:** Native CPT, Meta Box, Query Builder tools
**Connection:** HTTP/SSE Basic Auth

**Key Tools:**

| Tool | Purpose |
|------|---------|
| Create CPT | Define Custom Post Types |
| Create Meta Box | Define custom fields |
| Create Query | Build dynamic queries |
| Create Listing | Dynamic listing templates |

### 3. Core WordPress MCP
**Server:** `@node2flow/wordpress-mcp`
**Tools:** Standard REST API tools
**Connection:** stdio / NPX

**Key Tools:**

| Tool | Purpose |
|------|---------|
| `create-post`, `update-post` | Content management |
| `create-page`, `update-page` | Page management |
| `upload-media` | Image/file uploads |
| `get-posts`, `get-pages` | Content retrieval |
| `update-settings` | Site configuration |

## Common Workflows

### Batch Page Creation
Use `elementor-mcp/build-page` to create complex layouts using a single JSON declarative structure.

### Dynamic Mapping
Use `elementor-mcp/set-dynamic-tag` to bind JetEngine Meta Fields to Elementor elements programmatically.

### Theme Building
Use `elementor-mcp/create-theme-template` to generate headers, footers, and single-post templates.

### Content Updates
Use `wordpress-mcp/update-post` for text-only content changes (no need for Elementor MCP).

## Troubleshooting

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| MCP not responding | Server not started | Restart MCP server process |
| Auth failed | Wrong credentials | Verify WP admin user/pass in MCP config |
| Widget not found | Elementor version mismatch | Update Elementor + MCP Adapter |
| Dynamic tag empty | JetEngine field not mapped | Check field name matches exactly |
| REST API blocked | Permalink not set | Set permalink to "Post name" |

## Common Mistakes

- ❌ Leaving all 3 MCPs enabled when only one is needed (wastes tokens)
- ❌ Not checking MCP availability before starting work
- ❌ Using browser agent for tasks MCPs can handle directly
- ❌ Hardcoding page IDs instead of querying by slug
- ❌ Not verifying Elementor widget compatibility before building

## Related Skills

- **wordpress-site-build**: End-to-end build checklist
- **envato-template-selection**: Template selection before building
- **frontend-design**: Design decisions during page building
