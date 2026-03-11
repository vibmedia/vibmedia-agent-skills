#!/usr/bin/env python3

import os
import sys
import re
from pathlib import Path

# The specific terms to search for (learned from CA Chandni Chopra project and others)
# This list can be appended to in the future.
PROJECT_TERMS = [
    # Platforms/Regional Services
    r'\bZomato\b', r'\bSwiggy\b', r'\bJustdial\b', r'\bSulekha\b', r'\bIndiaMART\b', r'\bTradeIndia\b',
    # Documents/Licenses
    r'\bFSSAI\b', r'\bGSTIN\b', r'\bGST\b',
    # Locations
    r'\bNoida\b', r'\bDelhi\b', r'\bIndia\b',
    # Client specifics
    r"Raj's Kitchen", r'chandnichopra', r'cachandnichopra'
]

# Directories that must be PURE FRAMEWORK (no project data)
TARGET_DIRS = ['agents', 'skills', 'workflows', 'profiles']

def check_framework_boundaries(base_path: str) -> bool:
    """Scan framework files for strictly forbidden project/brand-specific terms and check for artifacts."""
    root_dir = Path(base_path) / '.agent'
    if not root_dir.exists():
        print("❌ Please run this script from the project root (where .agent lives).")
        sys.exit(1)

    failures = 0

    # 1. Check framework boundary (no brand info in framework)
    print("📋 Checking Framework Boundary (No instance data in templates)...")
    regex = re.compile('|'.join(PROJECT_TERMS), re.IGNORECASE)

    for target in TARGET_DIRS:
        target_path = root_dir / target
        if not target_path.exists():
            continue

        for filepath in target_path.rglob('*.md'):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    matches = regex.findall(content)
                    if matches:
                        failures += 1
                        print(f"❌ VIOLATION in {filepath}")
                        print(f"   Found project-specific terms: {set(matches)}")
                        print(f"   Fix: Move this to brands/[industry]/_common/ or replace with generic [placeholder].")
                        print(f"   See docs/CONTENT-BOUNDARY.md for rules.\n")
            except Exception as e:
                print(f"Error reading {filepath}: {e}")

    if failures > 0:
        print("🚨 Content Boundary Check FAILED. Do not commit these files until fixed.")
        # Do not exit yet, continue to the next check

    # 2. Check output boundary (no project deliverables in .agent/brands)
    print("\n📋 Checking Output Boundary (No project deliverables inside .agent)...")
    brands_dir = root_dir / "brands"
    if brands_dir.is_dir():
        for root, dirs, files in os.walk(brands_dir):
            if "artifacts" in dirs:
                rel_path = Path(root) / "artifacts"
                print(f"❌ ERROR: Project deliverables inside framework detected: {rel_path}")
                print(f"      Rule: Project artifacts (code, copy) must be saved OUTSIDE the .agent folder.")
                failures += 1

    if failures == 0:
        print("\n✅ Verification Passed: Framework remains generic and boundaries respected.")
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == '__main__':
    check_framework_boundaries(os.getcwd())
