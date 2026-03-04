---
description: Visualize project architecture with /visualize-arch
---

# /visualize-arch — Architecture Explorer

Generates a Draw.io diagram, Mermaid inline diagram, and raw JSON data for any `.agent` project.

> All paths are resolved dynamically. This workflow is portable across projects.

## Steps

1. Detect the `.agent` directory relative to the current project root.

2. Run the architecture scanner with all output formats:
// turbo
```bash
AGENT_DIR="$(pwd)/.agent"
python3 "$AGENT_DIR/skills/architecture-explorer/scripts/scanner.py" . \
  --output "$AGENT_DIR/skills/architecture-explorer/assets/relationships.json" \
  --mermaid "$AGENT_DIR/skills/architecture-explorer/assets/map.md" \
  --drawio "$AGENT_DIR/skills/architecture-explorer/assets/architecture.drawio" \
  --depth 2
```

3. Present results to user:
// turbo
```bash
AGENT_DIR="$(pwd)/.agent"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Architecture Explorer — Scan Complete!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📐 Draw.io:  $AGENT_DIR/skills/architecture-explorer/assets/architecture.drawio"
echo "📊 Mermaid:  $AGENT_DIR/skills/architecture-explorer/assets/map.md"
echo "📦 JSON:     $AGENT_DIR/skills/architecture-explorer/assets/relationships.json"
echo ""
echo "💡 Open the .drawio file in VS Code (Draw.io extension) or at https://app.diagrams.net"
echo ""
```

4. After running, read `map.md` and display its Mermaid diagram inline to the user.
