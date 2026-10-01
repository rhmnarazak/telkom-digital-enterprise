"""Shared nav (desktop links + Services/Capabilities mega menus + mobile drawer) for every page.

Used by build_services.py and build_capabilities.py, and by update_nav.py to refresh the nav
in index.html and who-we-are.html. `current` is "home", "who", "stories", a service key ("acd", …) or a
capability slug ("notifications-alerts", …).
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
e = html.escape

# Services in menu order: key, page slug, menu name, icon, short description
SERVICES_MENU = [
    ("acd", "academic-management", "Academic Management", "academic-management.png", "Run classes, attendance and grades for every school in one place."),
    ("doc", "document-management", "Document Management", "document-management.png", "Store, find and sign documents, with every version on record."),
    ("cam", "ip-camera-management", "IP Camera Management", "ip-cam-management.png", "Turn cameras into live alerts for intruders, fire and crowds."),
    ("net", "network-management", "Network Management", "network-monitoring.png", "Watch networks, servers and APIs before issues reach your users."),
    ("crm", "omnichannel-management", "Omnichannel Management", "crm.png", "Answer customers on WhatsApp and every channel from one inbox."),
    ("gai", "privategpt", "PrivateGPT", "program-lifecycle.png", "Ask questions of your company data, kept private inside your tenant."),
]
SERVICE_HREF = {k: f"service-{slug}.html" for k, slug, *_ in SERVICES_MENU}

# Shared (Tier A) capabilities: slug, exact taxonomy name, short description, menu column
CAPS_MENU = [
    ("realtime-dashboard-monitoring", "Real-time Dashboard & Monitoring", "See schools, networks and devices live on one screen", "Monitor & decide"),
    ("reporting-analytics", "Reporting & Analytics", "Turn daily activity into reports you can act on", "Monitor & decide"),
    ("notifications-alerts", "Notifications & Alerts", "Tell the right people the moment something changes", "Monitor & decide"),
    ("ai-automation", "AI & Automation", "Let AI detect, answer and predict so teams act sooner", "Automate & connect"),
    ("api-integration", "API Integration", "Connect WhatsApp, IoT networks and smart devices", "Automate & connect"),
    ("communication-chatbot", "Communication & Chatbot", "Hold every customer conversation in one place", "Automate & connect"),
    ("cloud-storage", "Cloud Storage", "Keep footage and learning content safe and reachable", "Store & secure"),
    ("user-access-management", "User & Access Management", "Give every role exactly the access it needs", "Store & secure"),
    ("mobile-app", "Mobile App", "Take the service with you on iOS and Android", "Store & secure"),
]
CAP_HREF = {name: f"capability-{slug}.html" for slug, name, *_ in CAPS_MENU}
CAP_SLUGS = {slug for slug, *_ in CAPS_MENU}

CUR = ' aria-current="page"'

# Existing partners sign in on the Workspace app
LOGIN_URL = "https://staging-enterprise.telkomdigital.id/login"
USER_ICO = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="4" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M4 20c1.5-4 4.5-6 8-6s6.5 2 8 6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>'
ARR = '<svg aria-hidden="true"><use href="#arr"/></svg>'
CHEV = '<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M3 4.5l3 3 3-3" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
DCHEV = CHEV.replace('1.6', '1.4')


def logo_from_index():
    idx = (ROOT / "index.html").read_text(encoding="utf-8")
    m = re.search(r'<a class="logo" href="(?:index\.html|#hero)"[^>]*>.*?</svg></a>', idx, re.S)
    return m.group(0)


def nav(current, logo=None, home_logo=False):
    """Return (desktop nav html, mobile drawer html)."""
    logo = logo or logo_from_index()
    href = "#hero" if home_logo else "index.html"
    logo = re.sub(r'^<a class="logo"[^>]*>', f'<a class="logo" href="{href}" aria-label="Telkom Digital, home">', logo)
    in_svc = current in SERVICE_HREF
    in_cap = current in CAP_SLUGS

    svc_items = "\n".join(
        f'          <li><a class="mega-item" href="{SERVICE_HREF[k]}"{CUR if k == current else ""}><span class="mega-ico"><img src="assets/capabilities/{ic}" alt=""></span><span><b>{e(n)}</b><small>{e(d)}</small></span></a></li>'
        for k, _, n, ic, d in SERVICES_MENU)
    cols = {}
    for slug, n, d, col in CAPS_MENU:
        cols.setdefault(col, []).append(
            f'            <li><a class="mega-cap" href="capability-{slug}.html"{CUR if slug == current else ""}><b>{e(n)}</b><small>{e(d)}</small></a></li>')
    cap_cols = "\n".join(
        f'        <div class="mega-col">\n          <p class="mega-label">{e(c)}</p>\n          <ul>\n{chr(10).join(items)}\n          </ul>\n        </div>'
        for c, items in cols.items())

    def top(label, page, key):
        return f'<li><a href="{page}"{CUR if current == key else ""}>{label}</a></li>'

    desktop = f'''  <nav class="nav in" style="--i:0" aria-label="Main">
    {logo}
    <ul class="links">
      {top("Home", "index.html", "home")}
      <li>
        <button class="links-btn{" current" if in_svc else ""}" type="button" aria-expanded="false" aria-controls="svc-menu">Services {CHEV}</button>
      </li>
      <li>
        <button class="links-btn{" current" if in_cap else ""}" type="button" aria-expanded="false" aria-controls="cap-menu">Capabilities {CHEV}</button>
      </li>
      {top("Customer Stories", "customer-stories.html", "stories")}
      {top("Who We Are", "who-we-are.html", "who")}
    </ul>
    <div class="mega" id="svc-menu">
      <div class="mega-main">
        <p class="mega-label">Services</p>
        <ul class="mega-grid">
{svc_items}
        </ul>
      </div>
      <a class="mega-feature" href="#">
        <span class="mega-label">One platform</span>
        <span class="mf-door" aria-hidden="true"><i class="fr"></i><i class="lt"></i><i class="pn"></i></span>
        <span class="mf-title">One login. <b>Six services.</b></span>
        <span class="link-arrow">Explore all services {ARR}</span>
      </a>
      <a class="mega-bar" href="#"><b>API &amp; Integrations</b><span>Connect partner systems through one gateway: data in, insight out.</span>{ARR}</a>
    </div>
    <div class="mega mega-caps" id="cap-menu">
      <div class="mega-cols">
{cap_cols}
      </div>
      <a class="mega-bar" href="who-we-are.html#ecosystem"><b>How it fits together</b><span>Every service is built on the same shared capabilities.</span>{ARR}</a>
    </div>
    <a class="nav-login" href="{LOGIN_URL}">Log in</a>
    <a class="pricing" href="{"#open" if current == "home" else "index.html#open"}">Schedule a Demo</a>
    <a class="nav-login-ico" href="{LOGIN_URL}" aria-label="Log in to Workspace">{USER_ICO}</a>
    <button class="menu" type="button" aria-label="Open menu" aria-controls="drawer"><span></span><span></span></button>
  </nav>'''

    d_svc = "\n".join(f'        <a href="{SERVICE_HREF[k]}"{CUR if k == current else ""}><img src="assets/capabilities/{ic}" alt="">{e(n)}</a>' for k, _, n, ic, _d in SERVICES_MENU)
    d_cap = "\n".join(f'        <a href="capability-{slug}.html"{CUR if slug == current else ""}>{e(n)}</a>' for slug, n, *_ in CAPS_MENU)
    drawer = f'''<div class="drawer" id="drawer" aria-hidden="true">
  <nav class="drawer-panel" aria-label="Mobile">
    <button class="drawer-close" type="button" aria-label="Close menu">×</button>
    <a href="index.html"{CUR if current == "home" else ""}>Home</a>
    <details class="drawer-sub"{" open" if in_svc else ""}>
      <summary>Services {DCHEV}</summary>
      <div>
{d_svc}
      </div>
    </details>
    <details class="drawer-sub"{" open" if in_cap else ""}>
      <summary>Capabilities {DCHEV}</summary>
      <div>
{d_cap}
      </div>
    </details>
    <a href="customer-stories.html"{CUR if current == "stories" else ""}>Customer Stories</a>
    <a href="who-we-are.html"{CUR if current == "who" else ""}>Who We Are</a>
    <a class="pricing" href="{"#open" if current == "home" else "index.html#open"}">Schedule a Demo</a>
    <a class="drawer-login" href="{LOGIN_URL}">Log in to Workspace</a>
  </nav>
</div>'''
    return desktop, drawer


def footer():
    """Shared footer for every page: services and shared capabilities from the taxonomy."""
    svc = "".join(f'<li><a href="{SERVICE_HREF[k]}">{e(n)}</a></li>' for k, _, n, _ic, _d in SERVICES_MENU)
    caps = "".join(f'<li><a href="capability-{slug}.html">{e(n)}</a></li>' for slug, n, *_ in CAPS_MENU[:6])
    return f'''<footer class="foot">
  <div class="inner">
    <div class="foot-top">
      <div class="foot-brand">
        <a class="logo" href="index.html" aria-label="Telkom Digital, home" data-logo></a>
        <p>Telkom Digital brings Telkom's enterprise services together on one secure, multi-tenant platform: one door for every partner.</p>
      </div>
      <nav class="foot-cols foot-cols-4" aria-label="Footer">
        <div><h4>Services</h4><ul>{svc}</ul></div>
        <div><h4>Capabilities</h4><ul>{caps}<li><a href="who-we-are.html#ecosystem">How it fits together</a></li></ul></div>
        <div><h4>Company</h4><ul><li><a href="who-we-are.html">Who We Are</a></li><li><a href="customer-stories.html">Customer Stories</a></li><li><a href="index.html#open">Contact us</a></li></ul></div>
        <div><h4>Support</h4><ul><li><a href="{LOGIN_URL}">Log in to Workspace</a></li><li><a href="#">Help centre</a></li><li><a href="#">API documentation</a></li><li><a href="#">SLA status</a></li></ul></div>
      </nav>
    </div>
    <div class="foot-legal">
      <p>© 2026 PT Telkom Indonesia (Persero) Tbk. All rights reserved.</p>
      <ul><li><a href="#">Privacy policy</a></li><li><a href="#">Terms &amp; conditions</a></li><li><a href="#">Data security</a></li></ul>
    </div>
  </div>
</footer>'''


ICONS = ('<link rel="icon" href="assets/favicon/favicon.svg" type="image/svg+xml">\n'
         '<link rel="icon" href="assets/favicon/icon-32.png" sizes="32x32" type="image/png">\n'
         '<link rel="apple-touch-icon" href="assets/favicon/apple-touch-icon.png">\n')


def with_icons(page):
    """Add the favicon links to a page's <head> (idempotent)."""
    page = re.sub(r'<link rel="(?:icon|apple-touch-icon)"[^>]*>\n', '', page)
    anchor = '<link rel="preconnect" href="https://fonts.googleapis.com">'
    return page.replace(anchor, ICONS + anchor, 1)
