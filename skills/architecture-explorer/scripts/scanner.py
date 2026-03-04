import os
import json
import ast
import argparse
import re
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

# ===========================================================================
# Architecture Explorer Scanner v2.4
# Portable across any .agent project.
# Standardized XML for maximum compatibility.
# ===========================================================================

IGNORE_DIRS = {
    '.git', '.agent', '__pycache__', 'node_modules', '.venv', 'venv',
    'brain', 'logs', '.next', 'dist', 'build', '.cache', '.turbo',
    'coverage', '.nyc_output', 'egg-info'
}

SUPPORTED_EXTENSIONS = ('.py', '.js', '.ts', '.tsx', '.jsx', '.go', '.rs', '.java')

def get_docstring(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            tree = ast.parse(f.read())
            doc = ast.get_docstring(tree) or ""
            doc = re.sub(r'\s+', ' ', doc).strip()
            return doc
    except Exception: return ""

def get_readme(dir_path):
    for name in ("README.md", "readme.md", "Readme.md"):
        readme = Path(dir_path) / name
        if readme.exists():
            try:
                content = readme.read_text(encoding='utf-8', errors='ignore')
                content = content.split('\n\n')[0] if '\n\n' in content else content
                content = re.sub(r'#+\s.*', '', content)
                content = re.sub(r'\n', ' ', content).strip()
                return content[:200]
            except Exception: pass
    return ""

def scan_project(root_dir, max_depth=3):
    nodes, links = [], []
    root_path = Path(root_dir).resolve()
    project_name = root_path.name
    path_to_id = {}
    def make_id(p):
        rel = os.path.relpath(p, str(root_path))
        return rel.replace(os.sep, '/') if rel != '.' else 'root'

    root_id = "root"
    path_to_id[str(root_path)] = root_id
    nodes.append({
        "id": root_id, "name": project_name, "type": "server",
        "level": 0, "path": str(root_path), "content": get_readme(root_path)
    })

    for current_dir, dirs, files in os.walk(str(root_path)):
        dirs[:] = sorted([d for d in dirs if d not in IGNORE_DIRS])
        rel_dir = os.path.relpath(current_dir, str(root_path))
        depth = 0 if rel_dir == "." else rel_dir.count(os.sep) + 1
        if depth > max_depth: continue

        if depth > 0:
            dir_path = Path(current_dir).resolve()
            dir_id = make_id(str(dir_path))
            path_to_id[str(dir_path)] = dir_id
            nodes.append({
                "id": dir_id, "name": dir_path.name, "type": "service",
                "level": min(depth, max_depth), "path": str(dir_path),
                "content": get_readme(current_dir)
            })
            parent_id = path_to_id.get(str(dir_path.parent))
            if parent_id: links.append({"source": parent_id, "target": dir_id, "type": "hierarchy"})

        for f in sorted(files):
            if not f.endswith(SUPPORTED_EXTENSIONS) or f.lower().startswith('readme'): continue
            file_path = Path(current_dir) / f
            file_abs = str(file_path.resolve())
            file_id = make_id(file_abs)
            path_to_id[file_abs] = file_id
            content = get_docstring(file_path) if f.endswith('.py') else ""
            nodes.append({
                "id": file_id, "name": f, "type": "node",
                "level": min(depth + 1, max_depth), "path": file_abs, "content": content
            })
            parent_id = path_to_id.get(str(Path(current_dir).resolve()))
            if parent_id: links.append({"source": parent_id, "target": file_id, "type": "hierarchy"})
    return {"nodes": nodes, "links": links}

# Simplified Styles
DRAWIO_STYLES = {
    "server": "rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=14;fontStyle=1;arcSize=20;fontColor=#000000;",
    "service": "rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12;fontStyle=1;fontColor=#000000;",
    "node": "rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;fontSize=11;fontColor=#000000;",
}
NODE_WIDTH = {"server": 240, "service": 200, "node": 180}
NODE_HEIGHT = {"server": 60, "service": 50, "node": 40}

def generate_drawio(data, max_level=2):
    filtered = [n for n in data["nodes"] if n["level"] <= max_level]
    node_ids = {n["id"] for n in filtered}
    children = {}
    for link in data["links"]:
        if link["type"] == "hierarchy" and link["source"] in node_ids and link["target"] in node_ids:
            children.setdefault(link["source"], []).append(link["target"])

    subtree_widths = {}
    h_gap, v_gap = 220, 150
    def calc_w(nid):
        kids = children.get(nid, [])
        if not kids: subtree_widths[nid] = h_gap; return h_gap
        w = sum(calc_w(k) for k in kids)
        subtree_widths[nid] = max(w, h_gap); return subtree_widths[nid]
    calc_w("root")
    
    raw_pos = {}
    def layout(nid, x, y):
        raw_pos[nid] = (x, y)
        kids = children.get(nid, [])
        if not kids: return
        cx = x - (subtree_widths[nid] // 2)
        for k in kids:
            kw = subtree_widths[k]
            layout(k, cx + (kw // 2), y + v_gap)
            cx += kw
    layout("root", 0, 80)
    
    # Normalize: shift all coords so minimum x is at margin
    all_xs = []
    id_to_node = {n["id"]: n for n in filtered}
    for nid, (rx, ry) in raw_pos.items():
        w = NODE_WIDTH.get(id_to_node[nid]["type"], 180)
        all_xs.append(rx - w // 2)
    min_x = min(all_xs) if all_xs else 0
    margin = 80
    
    cells = []
    id_map = {}
    for i, n in enumerate(filtered):
        sid = f"node_{i}"
        id_map[n["id"]] = sid
        w, h = NODE_WIDTH.get(n["type"], 180), NODE_HEIGHT.get(n["type"], 50)
        rx, ry = raw_pos[n["id"]]
        nx = rx - (w // 2) - min_x + margin
        val = xml_escape(n["name"])
        cells.append(f'        <mxCell id="{sid}" value="{val}" style="{DRAWIO_STYLES.get(n["type"])}" parent="1" vertex="1"><mxGeometry x="{nx}" y="{ry}" width="{w}" height="{h}" as="geometry"/></mxCell>')

    for i, link in enumerate(data["links"]):
        if link["source"] in id_map and link["target"] in id_map:
            eid = f"edge_{i}"
            cells.append(f'        <mxCell id="{eid}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;" parent="1" source="{id_map[link["source"]]}" target="{id_map[link["target"]]}" edge="1"><mxGeometry relative="1" as="geometry"/></mxCell>')

    pw = int(max(raw_pos[nid][0] + 400 for nid in raw_pos) - min_x + margin)
    ph = int(max(raw_pos[nid][1] + 400 for nid in raw_pos))

    return f'''<mxfile host="65bd71144e">
    <diagram id="arch" name="Architecture">
        <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{pw}" pageHeight="{ph}" math="0" shadow="0">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
{chr(10).join(cells)}
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>'''

def generate_mermaid(data, max_level=2):
    lines = ["graph TD"]
    lines.append("    classDef server fill:#ef4444,stroke:#b91c1c,color:#fff,font-weight:bold")
    lines.append("    classDef service fill:#3b82f6,stroke:#2563eb,color:#fff")
    lines.append("    classDef node_file fill:#10b981,stroke:#059669,color:#fff,font-size:10px")
    filtered = [n for n in data["nodes"] if n["level"] <= max_level]
    node_ids = {n["id"] for n in filtered}
    mermaid_ids = {}
    for i, n in enumerate(filtered):
        mid = f"n{i}"
        mermaid_ids[n["id"]] = mid
        label = n["name"]
        if n["type"] == "server":   lines.append(f'    {mid}["{label}"]:::server')
        elif n["type"] == "service": lines.append(f'    {mid}["{label}/"]:::service')
        else:                       lines.append(f'    {mid}["{label}"]:::node_file')
    for link in data["links"]:
        if link["type"] == "hierarchy" and link["source"] in mermaid_ids and link["target"] in mermaid_ids:
            lines.append(f"    {mermaid_ids[link['source']]} --> {mermaid_ids[link['target']]}")
    return "\n".join(lines)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Architecture Explorer Scanner — Portable codebase mapper")
    parser.add_argument("path", help="Project root to scan (use '.' for cwd)")
    parser.add_argument("--output", default=None, help="Output JSON path")
    parser.add_argument("--mermaid", default=None, help="Output Mermaid .md path")
    parser.add_argument("--drawio", default=None, help="Output Draw.io .drawio path")
    parser.add_argument("--depth", type=int, default=2, help="Scan depth (default: 2)")
    args = parser.parse_args()
    root = Path(args.path).resolve()
    data = scan_project(str(root), max_depth=args.depth)
    if args.output:
        os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
        with open(args.output, "w") as f: json.dump(data, f, indent=2)
    if args.mermaid:
        os.makedirs(os.path.dirname(os.path.abspath(args.mermaid)), exist_ok=True)
        with open(args.mermaid, "w") as f:
            f.write(f"# Map — {root.name}\n\n```mermaid\n{generate_mermaid(data, args.depth)}\n```\n")
    if args.drawio:
        os.makedirs(os.path.dirname(os.path.abspath(args.drawio)), exist_ok=True)
        with open(args.drawio, "w") as f: f.write(generate_drawio(data, args.depth))
    print(f"✅ Scan complete ({len(data['nodes'])} nodes).")
