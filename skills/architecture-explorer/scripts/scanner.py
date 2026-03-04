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

def generate_drawio(data, max_level=2):
    filtered = [n for n in data["nodes"] if n["level"] <= max_level]
    node_ids = {n["id"] for n in filtered}
    
    root_node = next((n for n in filtered if n["level"] == 0), None)
    if not root_node: return ""
    
    children = {}
    for link in data["links"]:
        if link["type"] == "hierarchy" and link["source"] in node_ids and link["target"] in node_ids:
            children.setdefault(link["source"], []).append(link["target"])
            
    subtree_widths = {}
    h_gap, v_gap = 260, 280
    
    def calc_w(nid):
        kids = children.get(nid, [])
        if not kids: 
            subtree_widths[nid] = h_gap
            return h_gap
        w = sum(calc_w(k) for k in kids)
        subtree_widths[nid] = max(w, h_gap)
        return subtree_widths[nid]
        
    calc_w(root_node["id"])
    
    raw_pos = {}
    def do_layout(nid, x, y):
        raw_pos[nid] = (x, y)
        kids = children.get(nid, [])
        if not kids: return
        cx = x - (subtree_widths[nid] // 2)
        for k in kids:
            kw = subtree_widths[k]
            do_layout(k, cx + (kw // 2), y + v_gap)
            cx += kw
            
    do_layout(root_node["id"], 0, 150)
    
    min_x = min(p[0] for p in raw_pos.values())
    margin = 100
    for nid in raw_pos:
        x, y = raw_pos[nid]
        raw_pos[nid] = (x - min_x + margin, y)
        
    max_x = max(p[0] for p in raw_pos.values())
    layer_width = max(1400, max_x + margin + 100)
    
    levels = {}
    for n in filtered:
        lvl = n["level"]
        if lvl not in levels:
            levels[lvl] = {
                "y": raw_pos[n["id"]][1],
                "nodes": []
            }
        levels[lvl]["nodes"].append(n)
        
    box_styles = {
        "server": "rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=14;fontStyle=1;fontColor=#000000;",
        "service": "rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12;fontStyle=1;fontColor=#000000;",
        "node": "rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;fontSize=11;fontStyle=0;fontColor=#000000;"
    }
    
    layer_bg_colors = ["#f8f9fa", "#f1f3f5", "#e9ecef", "#dee2e6", "#ced4da"]
    
    cells = []
    
    title = f"{root_node['name'].upper()} — Architecture Topology"
    cells.append(f'''        <mxCell id="title" value="{title}" style="text;html=1;fontSize=24;fontStyle=1;align=center;fillColor=none;strokeColor=none;fontColor=#000000;" parent="1" vertex="1">
            <mxGeometry x="50" y="20" width="1000" height="40" as="geometry"/>
        </mxCell>''')

    for lvl in sorted(levels.keys()):
        y = levels[lvl]["y"]
        bg_color = layer_bg_colors[lvl % len(layer_bg_colors)]
        
        if lvl == 0: layer_name = "ROOT PROJECT"
        elif lvl == 1: layer_name = "MODULES &amp; SERVICES"
        elif lvl == 2: layer_name = "COMPONENTS"
        else: layer_name = f"DEPTH {lvl}"
        
        cells.append(f'''        <mxCell id="layer_{lvl}_bg" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor={bg_color};strokeColor=#dee2e6;dashed=1;" parent="1" vertex="1">
            <mxGeometry x="50" y="{y - 60}" width="{layer_width}" height="{200}" as="geometry"/>
        </mxCell>''')
        
        cells.append(f'''        <mxCell id="layer_{lvl}_label" value="LAYER {lvl+1}: {layer_name}" style="text;html=1;fontSize=14;fontStyle=1;fontColor=#495057;" parent="1" vertex="1">
            <mxGeometry x="60" y="{y - 50}" width="400" height="30" as="geometry"/>
        </mxCell>''')
        
    id_map = {}
    for i, n in enumerate(filtered):
        sid = f"node_{i}"
        id_map[n["id"]] = sid
        
        cx, cy = raw_pos[n["id"]]
        w, h = 220, 80
        nx = cx - (w // 2)
        ny = cy
        
        style = box_styles.get(n["type"], box_styles["node"])
        
        icon = "📁" if n["type"] in ("server", "service") else "📄"
        safe_name = xml_escape(n["name"])
        doc = n.get("content", "").strip()
        
        if doc:
            if len(doc) > 60: doc = doc[:57] + "..."
            val = f"{icon} {safe_name}&#10;{xml_escape(doc)}"
        else:
            val = f"{icon} {safe_name}"
            
        file_uri = f"file://{n.get('path', '')}"
        
        cells.append(f'''        <UserObject label="{val}" link="{file_uri}" id="{sid}">
            <mxCell style="{style}" parent="1" vertex="1">
                <mxGeometry x="{nx}" y="{ny}" width="{w}" height="{h}" as="geometry"/>
            </mxCell>
        </UserObject>''')
        
    for i, link in enumerate(data["links"]):
        if link["source"] in id_map and link["target"] in id_map:
            eid = f"edge_{i}"
            target_node = next((n for n in filtered if n["id"] == link["target"]), None)
            link_uri = f"file://{target_node['path']}" if target_node and "path" in target_node else ""
            cells.append(f'''        <UserObject label="" link="{link_uri}" id="{eid}">
            <mxCell style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#222222;strokeWidth=2;" parent="1" source="{id_map[link["source"]]}" target="{id_map[link["target"]]}" edge="1">
                <mxGeometry relative="1" as="geometry"/>
            </mxCell>
        </UserObject>''')

    pw = int(layer_width + 100)
    ph = int(max((raw_pos[nid][1] for nid in raw_pos), default=0) + 300)

    return f'''<mxfile host="65bd71144e">
    <diagram id="layered-tree" name="Layered Tree Architecture">
        <mxGraphModel dx="1200" dy="1200" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{pw}" pageHeight="{ph}" math="0" shadow="0">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
{chr(10).join(cells)}
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>'''

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("--drawio", default=None)
    parser.add_argument("--output", default=None)
    parser.add_argument("--mermaid", default=None)
    parser.add_argument("--depth", type=int, default=2)
    args = parser.parse_args(); root = Path(args.path).resolve()
    data = scan_project(args.path, args.depth)
    if args.drawio:
        os.makedirs(os.path.dirname(os.path.abspath(args.drawio)), exist_ok=True)
        with open(args.drawio, "w", encoding="utf-8") as f: f.write(generate_drawio(data, args.depth))
    if args.output:
        os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as f: json.dump(data, f, indent=2)
    if args.mermaid:
        os.makedirs(os.path.dirname(os.path.abspath(args.mermaid)), exist_ok=True)
        filtered = [n for n in data["nodes"] if n["level"] <= args.depth]
        node_ids = {n["id"] for n in filtered}
        m_lines = ["# Architecture Map\n", "```mermaid", "graph TD"]
        for n in filtered:
            safe_name = n["name"].replace('"', '')
            # Ensure valid mermaid node ID
            node_id_safe = re.sub(r'[^a-zA-Z0-9_]', '_', n["id"])
            m_lines.append(f'  {node_id_safe}["{safe_name}"]')
        for link in data["links"]:
            if link["source"] in node_ids and link["target"] in node_ids:
                src_safe = re.sub(r'[^a-zA-Z0-9_]', '_', link["source"])
                tgt_safe = re.sub(r'[^a-zA-Z0-9_]', '_', link["target"])
                m_lines.append(f'  {src_safe} --> {tgt_safe}')
        for n in filtered:
            node_id_safe = re.sub(r'[^a-zA-Z0-9_]', '_', n["id"])
            if n.get("path"):
                m_lines.append(f'  click {node_id_safe} "file://{n["path"]}" "Open {n["name"]}"')
        m_lines.append("```\n")
        with open(args.mermaid, "w", encoding="utf-8") as f: f.write("\n".join(m_lines))
    print(f"✅ Scan complete ({len(data['nodes'])} nodes).")
