"""Refresh the nav, mobile drawer and footer in hand-written pages (index.html, who-we-are.html)
from site_nav.py, so every page shares the same menus. Run: python3 tools/update_nav.py"""
import re

import site_nav

PAGES = {"index.html": "home", "who-we-are.html": "who"}

for name, current in PAGES.items():
    path = site_nav.ROOT / name
    s = path.read_text(encoding="utf-8")
    desktop, drawer = site_nav.nav(current, home_logo=(current == "home"))
    s, n1 = re.subn(r'  <nav class="nav in" style="--i:0" aria-label="Main">.*?\n  </nav>', lambda m: desktop, s, count=1, flags=re.S)
    s, n2 = re.subn(r'<div class="drawer" id="drawer" aria-hidden="true">.*?\n  </nav>\n</div>', lambda m: drawer, s, count=1, flags=re.S)
    s, n3 = re.subn(r'<footer class="foot">.*?</footer>', lambda m: site_nav.footer(), s, count=1, flags=re.S)
    assert n1 == 1 and n2 == 1 and n3 == 1, name
    s = site_nav.with_icons(s)
    path.write_text(s, encoding="utf-8")
    print("updated", name)
