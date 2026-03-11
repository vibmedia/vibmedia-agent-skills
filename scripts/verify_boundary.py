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

def check_files():
    root_dir = Path('.agent')
    if not root_dir.exists():
        print("❌ Please run this script from the project root (where .agent lives).")
        sys.exit(1)

    has_violations = False
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
                        has_violations = True
                        print(f"❌ VIOLATION in {filepath}")
                        print(f"   Found project-specific terms: {set(matches)}")
                        print(f"   Fix: Move this to brands/[industry]/_common/ or replace with generic [placeholder].")
                        print(f"   See docs/CONTENT-BOUNDARY.md for rules.\n")
            except Exception as e:
                print(f"Error reading {filepath}: {e}")

    if has_violations:
        print("🚨 Content Boundary Check FAILED. Do not commit these files until fixed.")
        sys.exit(1)
    else:
        print("✅ Content Boundary Check PASSED. All framework files are generic.")
        sys.exit(0)

if __name__ == '__main__':
    check_files()
