#!/usr/bin/env python3
"""
Extensive WordPress Launch Checklist - Antigravity Kit
======================================================
Automated pre-flight checks specifically designed for WordPress sites.
Validates SEO, Security, Configuration, and UX standards without failing
on standard software dev metrics (like missing linters).

> **HYBRID APPROACH CONTEXT (Vibhor Rule):**
> `.py` scripts in the Antigravity Kit are ONLY used for tasks that 
> Markdown files cannot perform natively — like making HTTP requests, 
> pinging URLs, checking SSL certificates, and hitting APIs.
> 
> The *source of truth* for project objectives, plans, and manual 
> checklists must ALWAYS remain in the `.md` format (e.g., `task.md`,
> `requirements.md`). These `.py` files are strictly utilitarian tools 
> to assist the Markdown workflows, never to replace them.

Usage:
    python3 scripts/wordpress_checklist.py https://example.com
"""

import sys
import argparse
import urllib.request
import urllib.error
from urllib.parse import urlparse, urljoin
import ssl
from html.parser import HTMLParser

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class WPHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.has_viewport = False
        self.title = ""
        self.in_title = False
        self.meta_desc = ""
        self.h1_count = 0
        self.forms = 0
        self.has_favicon = False
        self.links = []
        self.mixed_content = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        # Check for mixed content
        src = attrs_dict.get('src', '')
        href = attrs_dict.get('href', '')
        if str(src).startswith("http://") or str(href).startswith("http://"):
            self.mixed_content = True

        if tag == "meta":
            if attrs_dict.get("name") == "viewport":
                self.has_viewport = True
            if attrs_dict.get("name", "").lower() == "description":
                self.meta_desc = attrs_dict.get("content", "")
        elif tag == "title":
            self.in_title = True
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "form":
            self.forms += 1
        elif tag == "link":
            if "icon" in attrs_dict.get("rel", "").lower():
                self.has_favicon = True
            if "href" in attrs_dict:
                self.links.append(attrs_dict["href"])
        elif tag == "a":
            if "href" in attrs_dict:
                self.links.append(attrs_dict["href"])

    def handle_data(self, data):
        if self.in_title:
            self.title += data

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

def print_header(text: str):
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{text.center(60)}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.ENDC}\n")

def print_result(name: str, passed: bool, message: str = "", critical: bool = True):
    if passed:
        print(f"{Colors.GREEN}✅ PASSED: {name}{Colors.ENDC}")
        if message: print(f"   ↳ {message}")
        return True
    else:
        if critical:
            print(f"{Colors.RED}❌ FAILED: {name}{Colors.ENDC}")
            if message: print(f"   ↳ {Colors.RED}{message}{Colors.ENDC}")
            return False
        else:
            print(f"{Colors.YELLOW}⚠️ WARNING: {name}{Colors.ENDC}")
            if message: print(f"   ↳ {Colors.YELLOW}{message}{Colors.ENDC}")
            return True

def check_url(url: str, timeout=10):
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as response:
            return response.getcode(), response.read().decode('utf-8', errors='ignore')
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:
        return 0, str(e)

def run_wordpress_audit(base_url: str):
    base_url = base_url.rstrip("/")
    results = []
    critical_errors = 0

    print_header(f"🚀 WORDPRESS PRE-FLIGHT AUDIT: {base_url}")
    print_header("🔒 SECURITY & CONFIGURATION CHECKS")
    
    # 1. SSL Check
    ssl_passed = base_url.startswith("https://")
    res = print_result("HTTPS Enabled", ssl_passed, "Site should use HTTPS securely.")
    results.append(res); critical_errors += not res
    
    # 2. Readme.html Check (Should be 404/403 or deleted)
    code, _ = check_url(f"{base_url}/readme.html")
    res = print_result("Default Readme Hidden", code in [404, 403, 0], "Default WP readme.html should be removed or blocked.", critical=False)
    results.append(res)
    
    # 3. XML-RPC Check (Often blocked or secured)
    code, _ = check_url(f"{base_url}/xmlrpc.php")
    res = print_result("XML-RPC Secured/Blocked", code in [405, 403, 404], "xmlrpc.php should be secured to prevent brute-force.", critical=False)
    results.append(res)

    print_header("🔌 SEO & PERFORMANCE CHECKS")

    # 4. Robots.txt Check
    code, text = check_url(f"{base_url}/robots.txt")
    res = print_result("Robots.txt Indexable", code == 200 and "Disallow: /" not in text.replace("Disallow: /wp-admin/", ""), "Ensure robots.txt is not blocking search engines.")
    results.append(res); critical_errors += not res

    # 5. Sitemap Check
    sitemap_code, _ = check_url(f"{base_url}/sitemap_index.xml")
    if sitemap_code != 200:
        sitemap_code, _ = check_url(f"{base_url}/sitemap.xml")
    res = print_result("XML Sitemap Exists", sitemap_code == 200, "Yoast, RankMath, or WP Core sitemap should respond.", critical=False)
    results.append(res)

    print_header("👁️ FRONTEND & UX CHECKS (HOMEPAGE)")

    # 6. Parse Homepage
    hp_code, hp_html = check_url(base_url)
    if hp_code != 200:
        print_result("Homepage Loaded", False, f"Could not load {base_url} (HTTP {hp_code})")
        sys.exit(1)
        
    parser = WPHTMLParser()
    parser.feed(hp_html)

    # 7. Viewport
    res = print_result("Mobile Viewport Meta Tag", parser.has_viewport, "Crucial for mobile responsiveness.")
    results.append(res); critical_errors += not res

    # 8. Mixed Content
    res = print_result("No Mixed Content (HTTP on HTTPS)", not parser.mixed_content, "Found HTTP linked assets on the HTTPS page.")
    results.append(res); critical_errors += not res

    # 9. Title & Meta Desc
    title_text = parser.title.strip()
    res = print_result("SEO Title Tag Exists", bool(title_text), f"Title: {title_text[:60]}")
    results.append(res); critical_errors += not res
    
    res = print_result("SEO Meta Description Exists", bool(parser.meta_desc.strip()), "Crucial for CTR in search results.")
    results.append(res); critical_errors += not res

    # 10. Single H1
    h1_passed = parser.h1_count == 1
    res = print_result("Single H1 Header", h1_passed, f"Found {parser.h1_count} H1 tags. There should be exactly one.", critical=False)
    results.append(res)

    # 11. Favicon
    res = print_result("Favicon Configured", parser.has_favicon, "Provides brand identity in browser tabs.", critical=False)
    results.append(res)

    # 12. Forms Present
    res = print_result("Lead/Contact Forms Detected", parser.forms > 0, f"Found {parser.forms} form(s). Make sure SMTP is tested manually.", critical=False)
    results.append(res)

    # 13. Legal Links Check
    links_text = " ".join(parser.links).lower()
    has_privacy = "privacy" in links_text
    has_terms = "terms" in links_text
    res = print_result("Privacy Policy Linked", has_privacy, "A Privacy Policy link should be in the footer.", critical=False)
    results.append(res)
    
    res = print_result("Terms/Disclaimer Linked", has_terms or "disclaimer" in links_text, "Terms or Legal Disclaimer link.", critical=False)
    results.append(res)

    print_header("📊 EXTENSIVE WP AUDIT SUMMARY")
    total = len(results)
    passed = sum(1 for r in results if r)
    
    print(f"Total Checks: {total}")
    print(f"{Colors.GREEN}✅ Passed/Warnings: {passed}{Colors.ENDC}")
    print(f"{Colors.RED}❌ Failed (Critical): {critical_errors}{Colors.ENDC}")
    print()
    if critical_errors == 0:
        print(f"{Colors.BOLD}{Colors.GREEN}Excellent! Website meets critical WordPress automated standards.{Colors.ENDC}")
        sys.exit(0)
    else:
        print(f"{Colors.BOLD}{Colors.RED}Please address the {critical_errors} critical failure(s) before launch.{Colors.ENDC}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extensive WordPress Launch Checklist")
    parser.add_argument("url", help="The base URL of the WordPress site (e.g., https://example.com)")
    args = parser.parse_args()
    
    if not args.url.startswith("http"):
        print("Error: URL must start with http:// or https://")
        sys.exit(1)
        
    run_wordpress_audit(args.url)
