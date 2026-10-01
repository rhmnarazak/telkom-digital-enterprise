"""Build customer-stories.html (the story hub) from the STORIES data below.

Run from the project root:  python3 tools/build_stories.py

Structure follows docs/kerangka-halaman-customer-stories.md. Sections follow the product stage
(section 1 of the kerangka): with 1–5 stories the page shows hero, featured story, story cards,
logos, testimonials and CTA. At 6+ stories the "I need…" paths and the service/capability filter
appear automatically; at 20+ the industry filter joins them.

IMPORTANT: every story and quote below is a PLACEHOLDER for layout review. Replace them with real,
approved partner stories (quote, metrics, permission to use the name/logo) before publishing.
"""
import html
import json
from collections import Counter

import site_nav
from build_services import PARENTS, BY_KEY, FOOTER, mock, ROOT

e = html.escape
ARR = site_nav.ARR
CODE = {"crm": "CRM", "acd": "ACD", "net": "NET", "cam": "CAM", "doc": "DOC", "gai": "GAI"}
VALIDATED = {"acd", "net", "cam", "crm"}   # DOC and GAI capabilities are estimates: not used as public tags

# --------------------------------------------------------------------------------------------
# Hero: strongest partner quote + aggregate figures
# --------------------------------------------------------------------------------------------
HERO_QUOTE = dict(
    text="We stopped finding problems the next morning. Now we hear about them while there is still time to act.",
    role="Regional Operations Manager", org="National retail chain", service="cam", placeholder=True)
AGGREGATES = [  # as reported on each service website (Pijar Sekolah, Netmonk, Antares): verify and date
    ("6,500+", "schools & institutions"),
    ("1,000+", "companies"),
    ("55,800", "connected devices"),
]

# --------------------------------------------------------------------------------------------
# Stories — fields mirror the use-case identification card (kerangka section 4.1)
# --------------------------------------------------------------------------------------------
STORIES = [
    dict(
        slug="national-retail-chain", placeholder=True, named=False,
        org="National retail chain", industry="Retail", size="Enterprise",
        service_primary="cam", services_supporting=["net"],
        capabilities_core=["People Counting & Crowd Detection", "Multi-site Deployment", "Cloud Recording"],
        use_case="Track shelf availability and store traffic across every branch from one app.",
        title="How a national retail chain cut out-of-stock time by 30% with computer vision",
        summary="Store teams used to discover empty shelves at closing time. With cameras that count visitors and flag gaps, they now restock during the day and plan staff around real peaks.",
        metrics=[("30%", "less out-of-stock time"), ("120", "stores on one app"), ("24/7", "shelf and crowd monitoring")],
        quote="We used to find empty shelves at the end of the day. Now the store team gets an alert while there is still time to restock.",
        role="Regional Operations Manager",
        image="assets/landing/story-retail-v2.png", image_alt="Professional woman under a clear sky among city buildings", mirror=True, pos="66% 50%",
    ),
    dict(
        slug="school-foundation", placeholder=True, named=False,
        org="Private school foundation", industry="Education", size="Mid-size",
        service_primary="acd", services_supporting=[],
        capabilities_core=["Real-time Attendance", "Computer-based Assessment", "Role-based Portals"],
        use_case="Run attendance, assessments and grades for a group of schools on one platform.",
        title="How a school foundation brought 12 campuses onto one academic platform",
        summary="Each campus kept its own registers and spreadsheets. One platform now gives parents live attendance and teachers online assessments, and the foundation one view of every school.",
        metrics=[("12", "campuses on one platform"), ("2×", "faster term reports"), ("6", "roles with their own portal")],
        quote="Parents see attendance before first period, and our teachers stopped retyping grades for the term report.",
        role="Head of Academic Affairs",
        mock=dict(title="Foundation · Today", chip="12 campuses", rows=[("Attendance", "95%", 95), ("Assessments scored", "1,240", 80)], alert=("ok", "Parents notified at 07:45")),
    ),
    dict(
        slug="regional-isp", placeholder=True, named=False,
        org="Regional internet service provider", industry="Telecommunications", size="Mid-size",
        service_primary="net", services_supporting=[],
        capabilities_core=["Proactive & Predictive Maintenance", "Network Monitoring", "Automated Reporting"],
        use_case="Monitor networks, servers and APIs, and get predictive alerts before customers notice.",
        title="How a regional ISP caught 4 in 5 incidents before customers called",
        summary="The operations team used to learn about outages from complaints. Predictive alerts now flag links heading for trouble, and SLA reports go out in one click.",
        metrics=[("80%", "of incidents flagged before complaints"), ("300+", "devices monitored"), ("1 click", "monthly SLA report")],
        quote="We see a link heading for trouble hours ahead, so we fix it in a maintenance window instead of on the phone with customers.",
        role="Network Operations Lead",
        image="assets/services/network.jpg", image_alt="Network operations wall showing throughput, system health and threat maps", pos="50% 50%",
    ),
    dict(
        slug="consumer-finance", placeholder=True, named=False,
        org="Consumer finance company", industry="Financial services", size="Enterprise",
        service_primary="crm", services_supporting=[],
        capabilities_core=["Omnichannel Inbox", "Chatbot Builder", "WhatsApp API"],
        use_case="Answer customers on WhatsApp, chat and voice from one inbox, with a 24/7 chatbot.",
        title="How a consumer finance company answered 60% of questions with a chatbot",
        summary="Agents were switching between apps for every channel. One inbox now holds each customer's whole conversation, and a chatbot covers routine questions around the clock.",
        metrics=[("60%", "of questions answered by the chatbot"), ("3", "channels in one inbox"), ("2×", "faster first response")],
        quote="Our agents no longer jump between apps. The whole conversation is in one place, and the chatbot handles routine questions at night.",
        role="Customer Service Manager",
        image="assets/services/omnichannel.jpg", image_alt="Customer support dashboard with live metrics and a ticket queue", pos="50% 50%",
    ),
]

# Curated testimonials — must not repeat a card quote (kerangka 3.7)
TESTIMONIALS = [
    dict(text="I set the quiz in the morning and the scores are waiting at lunch. That alone gives me an hour back each week.",
         role="Mathematics Teacher", org="Private school foundation", service="acd", cap="Computer-based Assessment", placeholder=True),
    dict(text="The intruder alert reached me before the alarm company called. I already had the clip open.",
         role="Head of Security", org="Logistics company", service="cam", cap="Intruder Detection", placeholder=True),
    dict(text="The board asks for uptime every month. Now it is one click and a PDF.",
         role="IT Manager", org="Manufacturing group", service="net", cap="Automated Reporting", placeholder=True),
    dict(text="When a customer writes on WhatsApp after a call, I can see the call notes right there.",
         role="Customer Service Agent", org="Consumer finance company", service="crm", cap="Omnichannel Inbox", placeholder=True),
]

NEED = {  # "I need…" path per service (kerangka 3.3)
    "crm": "to serve customers from every channel in one place",
    "acd": "to run schools, classes and grades digitally",
    "net": "to catch network issues before users complain",
    "cam": "to watch many sites from one app",
    "doc": "to store, find and approve documents quickly",
    "gai": "to use AI safely on company data",
}


def parents_of(key, cap):
    return [p for p, m in PARENTS.items() if cap in m.get(key, [])]


def shared_of(story):
    out = []
    for c in story["capabilities_core"]:
        for p in parents_of(story["service_primary"], c):
            if p not in out:
                out.append(p)
    return out


def tag(key, cap):
    """Capability tag: links to its shared (Tier A) capability page when it has one."""
    ps = parents_of(key, cap)
    if ps and key in VALIDATED:
        return f'<a class="tag" href="{site_nav.CAP_HREF[ps[0]]}">{e(cap)}</a>'
    return f'<span class="tag">{e(cap)}</span>'


def svc_label(s):
    k = s["service_primary"]
    extra = f' <em>+{len(s["services_supporting"])}</em>' if s["services_supporting"] else ''
    return f'<a class="svc-label" href="{site_nav.SERVICE_HREF[k]}"><span class="code">{CODE[k]}</span>{e(BY_KEY[k]["name"])}{extra}</a>'


def visual(s, cls="story-img leaf"):
    if s.get("image"):
        mir = ' class="mirror"' if s.get("mirror") else ''
        return f'<div class="{cls}"><img{mir} src="{s["image"]}" alt="{e(s["image_alt"])}" loading="lazy" style="object-position:{s.get("pos", "50% 50%")}"></div>'
    return f'<div class="{cls} story-mock">{mock(s["mock"], s["org"] + " preview")}</div>'


def card(s, i):
    k = s["service_primary"]
    services = " ".join([k] + s["services_supporting"])
    caps = "|".join(s["capabilities_core"])
    shared = "|".join(shared_of(s))
    tags = "".join(tag(k, c) for c in s["capabilities_core"][:3])
    return f'''        <li class="sc rv" style="--d:{i % 3}" data-services="{services}" data-caps="{e(caps)}" data-shared="{e(shared)}" data-industry="{e(s["industry"])}">
          <article class="story sc-card">
            {visual(s)}
            <div class="story-body">
              <div class="sc-top">{svc_label(s)}<span class="sc-org">{e(s["org"])}</span></div>
              <blockquote class="sc-quote"><p>{e(s["quote"])}</p><footer>{e(s["role"])}, {e(s["org"])}</footer></blockquote>
              <h3><a href="story-{s["slug"]}.html">{e(s["title"])}</a></h3>
              <p class="sc-use">{e(s["use_case"])}</p>
              <div class="m-tags">{tags}</div>
              <a class="link-arrow" href="story-{s["slug"]}.html">Read the story {ARR}</a>
            </div>
          </article>
        </li>'''


def filters(stories):
    """Service + capability filter (kerangka 3.4); only options with results, with counts."""
    svc = Counter(k for s in stories for k in [s["service_primary"]] + s["services_supporting"])
    shared = Counter(p for s in stories for p in shared_of(s))
    svc_btns = "".join(f'<button class="fchip" type="button" data-f="service" data-v="{k}" aria-pressed="false">{e(BY_KEY[k]["name"])} <span>({n})</span></button>'
                       for k, n in svc.most_common())
    cap_opts = "".join(f'<option value="{e(p)}">{e(p)} ({n})</option>' for p, n in shared.most_common())
    # service-specific capabilities, revealed once a service is chosen
    child = {}
    for s in stories:
        for c in s["capabilities_core"]:
            child.setdefault(s["service_primary"], Counter())[c] += 1
    child_json = json.dumps({k: [[c, n] for c, n in v.most_common()] for k, v in child.items()})
    industry = ''
    if len(stories) >= 20:
        ind = Counter(s["industry"] for s in stories)
        industry = '<label class="fsel"><span>Industry</span><select data-f="industry"><option value="">All industries</option>' + \
            "".join(f'<option value="{e(i)}">{e(i)} ({n})</option>' for i, n in ind.most_common()) + '</select></label>'
    return f'''      <div class="filters rv" role="group" aria-label="Filter stories">
        <div class="frow"><span class="flabel">Service</span><button class="fchip" type="button" data-f="service" data-v="" aria-pressed="true">All <span>({len(stories)})</span></button>{svc_btns}</div>
        <div class="frow">
          <label class="fsel"><span>Capability</span><select data-f="capability"><option value="">All capabilities</option><optgroup label="Shared capabilities">{cap_opts}</optgroup><optgroup label="In this service" hidden></optgroup></select></label>
          {industry}
          <p class="fcount" aria-live="polite"><b>{len(stories)}</b> stories</p>
        </div>
      </div>
      <script type="application/json" id="child-caps">{child_json}</script>'''


def paths(stories):
    out = []
    for k in ["crm", "acd", "net", "cam", "doc", "gai"]:
        mine = [s for s in stories if k == s["service_primary"] or k in s["services_supporting"]]
        if not mine:
            continue
        pop = [c for c, _ in Counter(c for s in mine for c in s["capabilities_core"]).most_common(2)]
        out.append(f'''        <li><a class="path rv" href="?service={k}" data-path="{k}">
          <b>I need {e(NEED[k])}</b>
          <span class="path-svc">{e(BY_KEY[k]["name"])} · {len(mine)} {"story" if len(mine) == 1 else "stories"}</span>
          <small>Popular: {e(" · ".join(pop))}</small>
          <span class="link-arrow">See stories {ARR}</span>
        </a></li>''')
    return "\n".join(out)


def page(mitra):
    stories = STORIES
    n = len(stories)
    stage = "early" if n <= 5 else "growing" if n < 20 else "mature"
    # order: named + metric, named, anonymous (kerangka 3.4)
    ordered = sorted(stories, key=lambda s: (not s["named"], not s["metrics"]))
    featured, rest = ordered[0], ordered[1:]
    nav_html, drawer_html = site_nav.nav("stories")

    fk = featured["service_primary"]
    f_metrics = "".join(f'<li><b>{e(v)}</b><span>{e(u)}</span></li>' for v, u in featured["metrics"][:3])
    f_tags = "".join(tag(fk, c) for c in featured["capabilities_core"])
    hq = HERO_QUOTE
    aggs = "".join(f'<div class="bigstat rv" style="--d:{i}"><b>{e(v)}</b><span>{e(u)}</span></div>' for i, (v, u) in enumerate(AGGREGATES))

    growing = stage != "early"
    paths_html = f'''
  <!-- ================= Paths by need (6+ stories) ================= -->
  <section class="sec mist" id="needs" aria-labelledby="needs-title">
    <div class="inner">
      <p class="eyebrow rv"><i class="dm"></i>Start from your need</p>
      <h2 id="needs-title" class="rv" style="--d:1">What are you <b>trying to solve?</b></h2>
      <ul class="paths">
{paths(stories)}
      </ul>
    </div>
  </section>
''' if growing else ''
    grid_cards = "\n".join(card(s, i) for i, s in enumerate(rest if not growing else ordered))
    filter_html = filters(ordered) if growing else ''
    more = '<div class="more-wrap"><button class="more" type="button" hidden>Load more stories</button></div>' if n > 12 else ''

    testi = "\n".join(f'''        <li class="tq rv" style="--d:{i % 2}">
          <blockquote><p>{e(t["text"])}</p></blockquote>
          <footer><b>{e(t["role"])}</b><span>{e(t["org"])}</span></footer>
          <div class="m-tags"><a class="svc-label" href="{site_nav.SERVICE_HREF[t["service"]]}"><span class="code">{CODE[t["service"]]}</span>{e(BY_KEY[t["service"]]["name"])}</a>{tag(t["service"], t["cap"])}</div>
        </li>''' for i, t in enumerate(TESTIMONIALS))

    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Customer Stories | Telkom Digital",
          "hasPart": [{"@type": "Article", "headline": s["title"]} for s in ordered]}
    placeholder_note = '''
<!--
  PLACEHOLDER CONTENT: every story, quote and impact figure on this page is a placeholder for layout
  review (anonymous partners, no real names). Replace with approved partner stories in
  tools/build_stories.py before publishing, and confirm permission for names, logos and quotes.
  The aggregate figures in the hero come from the service websites and still need verifying.
-->''' if any(s["placeholder"] for s in stories) else ''

    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Customer Stories | Telkom Digital — Academic, Network, IP Camera and Omnichannel Management</title>
<meta name="description" content="How partners across Indonesia use Telkom Digital: 6,500+ schools, 1,000+ companies and 55,800 connected devices, across academic, network, IP camera and omnichannel services.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,200..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<link rel="stylesheet" href="css/service.css">
<link rel="stylesheet" href="css/stories.css">
<script type="application/ld+json">
{json.dumps(ld, indent=2, ensure_ascii=False)}
</script>
</head>
<body data-stage="{stage}">
<!-- Generated by tools/build_stories.py — edit the data there and re-run instead of editing this file -->{placeholder_note}
<!-- Stage: {stage} ({n} stories). Paths and filters appear at 6+ stories, the industry filter at 20+. -->

<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
  <symbol id="arr" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></symbol>
</svg>

<section class="hero phero" id="hero">
{nav_html}

  <div class="inner cs-hero">
    <p class="eyebrow in" style="--i:1"><i class="dm"></i>Customer stories</p>
    <blockquote class="cs-quote in" style="--i:2">
      <h1>{e(hq["text"])}</h1>
      <footer><b>{e(hq["role"])}</b>, {e(hq["org"])} · <a href="{site_nav.SERVICE_HREF[hq["service"]]}">{e(BY_KEY[hq["service"]]["name"])}</a></footer>
    </blockquote>
    <p class="lede in" style="--i:3">In our partners' words, not ours: how schools, companies and stores across Indonesia run on Telkom Digital.</p>
    <div class="stats cs-stats">{aggs}</div>
    <p class="ph-source rv">Aggregate figures as reported on each service website (Pijar Sekolah, Netmonk, Antares).</p>
  </div>
</section>

{drawer_html}

<main>
  <!-- ================= Featured story ================= -->
  <section class="sec mist" id="featured" aria-labelledby="feat-title">
    <div class="inner">
      <p class="eyebrow rv"><i class="dm"></i>Featured story</p>
      <article class="feat rv" style="--d:1" aria-labelledby="feat-title">
        {visual(featured, "feat-img leaf")}
        <div class="feat-body">
          <div class="sc-top">{svc_label(featured)}<span class="sc-org">{e(featured["org"])}</span></div>
          <h2 id="feat-title" class="feat-title"><a href="story-{featured["slug"]}.html">{e(featured["title"])}</a></h2>
          <p>{e(featured["summary"])}</p>
          <ul class="feat-metrics">{f_metrics}</ul>
          <div class="m-tags">{f_tags}</div>
          <a class="pricing" href="story-{featured["slug"]}.html">Read the story</a>
        </div>
      </article>
    </div>
  </section>
{paths_html}
  <!-- ================= Stories ================= -->
  <section class="sec" id="stories" aria-labelledby="grid-title">
    <div class="inner">
      <div class="sec-head">
        <div>
          <p class="eyebrow rv"><i class="dm"></i>{"All stories" if growing else "More stories"}</p>
          <h2 id="grid-title" class="rv" style="--d:1">Proof from <b>every kind of partner.</b></h2>
        </div>
        <p class="lede rv" style="--d:2">Each story is tagged with the service and capabilities the partner uses.</p>
      </div>
{filter_html}
      <ul class="sc-grid">
{grid_cards}
      </ul>
      <p class="sc-empty" hidden>No stories match these filters yet. <button type="button" class="link-arrow" data-reset>Clear filters</button></p>
      {more}
    </div>
  </section>

  <!-- ================= Logos ================= -->
  <!-- TODO: replace the dummy marks with real partner logos (one colour, permission confirmed) -->
  <section class="logo-band" aria-label="Partner logos">
    <div class="inner">
      <p class="eyebrow"><i class="dm"></i>Trusted by partners across Indonesia</p>
      <div class="mitra-strip">
        {mitra}
      </div>
    </div>
  </section>

  <!-- Third-party proof (certifications, awards, reviews) is left out until there is verified content -->

  <!-- ================= Testimonials ================= -->
  <section class="sec mist" id="voices" aria-labelledby="voices-title">
    <div class="inner">
      <p class="eyebrow rv"><i class="dm"></i>In their words</p>
      <h2 id="voices-title" class="rv" style="--d:1">From the people <b>who use it every day.</b></h2>
      <ul class="tq-grid">
{testi}
      </ul>
    </div>
  </section>

  <!-- ================= CTA ================= -->
  <section class="sec cta" id="open" aria-labelledby="cta-title">
    <div class="inner cta-grid">
      <div class="bigdoor" aria-hidden="true">
        <span class="floor"></span><span class="frame"></span><span class="light"></span><span class="panel-d"></span>
      </div>
      <div>
        <p class="eyebrow rv"><i class="dm"></i>Your story next</p>
        <h2 id="cta-title" class="rv" style="--d:1">Write the next one <b>with us.</b></h2>
        <p class="lede rv" style="--d:2">Book a demo with your own use case, or tell us what you need and we will point you to the right service.</p>
        <div class="cta-actions rv" style="--d:3">
          <a class="pricing" href="index.html#open">Schedule a demo</a>
          <a class="link-arrow on-dark" href="index.html#open">Tell us what you need {ARR}</a>
        </div>
      </div>
    </div>
  </section>
</main>

{FOOTER}

<script src="js/site.js"></script>
<script src="js/services-menu.js"></script>
<script src="js/stories.js"></script>
</body>
</html>
'''



# --------------------------------------------------------------------------------------------
# Single story pages (docs/kerangka-success-story.md)
# --------------------------------------------------------------------------------------------
import re as _re
from story_content import CONTENT as STORY_CONTENT


def rich(text, key):
    """[[Capability]] -> capability link, {{svc:x}} -> service link, **b** -> <strong>."""
    t = e(text)
    def cap(m):
        name = html.unescape(m.group(1))
        ps = parents_of(key, name)
        if ps and key in VALIDATED:
            return f'<a class="cap-link" href="{site_nav.CAP_HREF[ps[0]]}">{e(name)}</a>'
        return f'<strong>{e(name)}</strong>'
    def svc(m):
        k = m.group(1)
        return f'<a class="cap-link" href="{site_nav.SERVICE_HREF[k]}">{e(BY_KEY[k]["name"])}</a>'
    t = _re.sub(r'\[\[(.+?)\]\]', cap, t)
    t = _re.sub(r'\{\{svc:(\w+)\}\}', svc, t)
    t = _re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    return t


def pull(q, cls=""):
    return f'<blockquote class="pull{cls}"><p>{e(q[0])}</p><footer>{e(q[1])}, {e(STORY_ORG)}</footer></blockquote>'


def story_page(s, mitra):
    global STORY_ORG
    c = STORY_CONTENT[s["slug"]]
    k = s["service_primary"]
    STORY_ORG = s["org"]
    nav_html, drawer_html = site_nav.nav("stories")
    tags = "".join(tag(k, x) for x in s["capabilities_core"])
    svcs = [k] + s["services_supporting"]
    svc_list = " + ".join(f'<a href="{site_nav.SERVICE_HREF[x]}">{e(BY_KEY[x]["name"])}</a>' for x in svcs)
    shared = shared_of(s)

    if c["hero_image"]:
        visual_html = f'<figure class="ph-photo leaf"><img src="{c["hero_image"]}" alt="{e(c["hero_alt"])}" width="1376" height="768"></figure>'
    else:
        visual_html = f'<figure class="ph-photo leaf blank" aria-hidden="true"></figure>\n      {mock(s["mock"], s["org"] + " preview")}'

    summary_rows = [("Industry", e(s["industry"])), ("Size", e(c["size_detail"])), ("Location", e(c["location"])),
                    ("Use case", e(s["use_case"])), ("Services", svc_list),
                    ("Capabilities used", ", ".join(e(x) for x in s["capabilities_core"])), ("Partner since", e(c["since"]))]
    summary = "".join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in summary_rows)
    stats = "".join(f'<li><b>{e(v)}</b><span>{e(u)}</span></li>' for v, u in s["metrics"])

    para = lambda ps: "\n".join(f'          <p>{rich(x, k)}</p>' for x in ps)
    sol = c["solution"]
    shot = c["screenshot"]
    table = "".join(f'<tr><th scope="row">{e(m)}</th><td>{e(b)}</td><td>{e(a)}</td></tr>' for m, b, a in c["results_table"])
    connected = f'\n          <p class="connected">{rich(c["connected"], k)}</p>' if c["connected"] else ''

    others = [o for o in STORIES if o["slug"] != s["slug"]]
    others.sort(key=lambda o: (o["service_primary"] == k, o["industry"] == s["industry"]))
    others_html = "\n".join(card(o, i) for i, o in enumerate(others[:3]))

    faq_html = "\n".join(f'        <details{" open" if i == 0 else ""}>\n          <summary>{e(q)}</summary>\n          <p>{e(a)}</p>\n        </details>' for i, (q, a) in enumerate(c["faq"]))
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": s["title"], "about": BY_KEY[k]["name"]},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in c["faq"]]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Customer Stories", "item": "customer-stories.html"},
            {"@type": "ListItem", "position": 2, "name": s["org"]}]}]}
    words = len(_re.sub(r'<[^>]+>', ' ', " ".join(c["context"] + c["challenge"] + sol + c["results"] + [c["next"], c["bridge"], c["goal"]])).split())

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(s["title"])} | {e(BY_KEY[k]["name"])} for {e(s["industry"])} — Telkom Digital</title>
<meta name="description" content="{e(c["sub"])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,200..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<link rel="stylesheet" href="css/service.css">
<link rel="stylesheet" href="css/stories.css">
<link rel="stylesheet" href="css/story.css">
<script type="application/ld+json">
{json.dumps(ld, indent=2, ensure_ascii=False)}
</script>
</head>
<body>
<!-- Generated by tools/build_stories.py (content in tools/story_content.py) — edit there and re-run -->
<!--
  PLACEHOLDER STORY for layout review: partner, quotes and figures are illustrative.
  Use-case card: {e(s["use_case"])} | primary {CODE[k]}{" | supporting " + ", ".join(CODE[x] for x in s["services_supporting"]) if s["services_supporting"] else ""}
  | core: {e(", ".join(s["capabilities_core"]))} | supporting: {e(", ".join(c["capabilities_supporting"]))}
  | shared: {e(", ".join(shared))} | industry: {e(s["industry"])} | size: {e(s["size"])} | impact: {e(s["metrics"][0][0] + " " + s["metrics"][0][1])}
  Story body: ~{words} words.
-->

<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
  <symbol id="arr" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></symbol>
</svg>

<section class="hero phero" id="hero">
{nav_html}

  <div class="inner ph-grid">
    <header class="ph-copy">
      <p class="eyebrow svc-crumb in" style="--i:1"><i class="dm"></i><a href="customer-stories.html">Customers</a> <span class="sep">/</span> {e(s["industry"])}</p>
      <div class="story-labels in" style="--i:2">{svc_label(s)}<span class="m-tags">{tags}</span></div>
      <h1 class="ph-title st-title in" style="--i:2">{e(s["title"])}</h1>
      <p class="lede in" style="--i:3">{e(c["sub"])}</p>
      <div class="hero-cta in" style="--i:4">
        <a class="pricing" href="index.html#open">Schedule a demo</a>
        <a class="link-arrow" href="{site_nav.SERVICE_HREF[k]}">See {e(BY_KEY[k]["name"])} {ARR}</a>
      </div>
    </header>
    <div class="svc-visual in" style="--i:3">
      {visual_html}
    </div>
  </div>
</section>

{drawer_html}

<main>
  <!-- ================= Summary card + 3 numbers ================= -->
  <section class="st-summary" aria-label="Story at a glance">
    <div class="inner st-sum-grid">
      <ul class="st-stats rv">{stats}</ul>
      <dl class="st-card rv" style="--d:1">{summary}</dl>
    </div>
  </section>

  <article class="sec st-body" aria-labelledby="ctx-title">
    <div class="inner st-cols">
      <div class="st-text">
        <section aria-labelledby="ctx-title">
          <p class="eyebrow rv"><i class="dm"></i>Context</p>
          <h2 id="ctx-title" class="rv">Who they are</h2>
{para(c["context"])}
          <p class="bridge">{e(c["bridge"])}</p>
        </section>

        <section aria-labelledby="ch-title">
          <p class="eyebrow rv"><i class="dm"></i>The challenge</p>
          <h2 id="ch-title" class="rv">Why the old way stopped working</h2>
{para(c["challenge"])}
          {pull(c["challenge_quote"])}
          <p>Their goal was clear: <strong>{e(c["goal"])}</strong></p>
        </section>

        <section aria-labelledby="sol-title">
          <p class="eyebrow rv"><i class="dm"></i>The solution</p>
          <h2 id="sol-title" class="rv">How {e(BY_KEY[k]["name"])} changed the work</h2>
{para(sol[:2])}
          {pull(c["solution_quote"], " big")}
{para(sol[2:])}
          {pull(c["solution_quote2"])}{connected}
          <figure class="st-shot">
            <div class="st-shot-frame">{mock(shot["mock"], "Product screenshot")}</div>
            <figcaption>{e(shot["caption"])}</figcaption>
          </figure>
        </section>

        <section aria-labelledby="res-title">
          <p class="eyebrow rv"><i class="dm"></i>The results</p>
          <h2 id="res-title" class="rv">What changed, in numbers</h2>
          <table class="st-table">
            <thead><tr><th scope="col">Metric</th><th scope="col">Before</th><th scope="col">After</th></tr></thead>
            <tbody>{table}</tbody>
          </table>
{para(c["results"])}
          {pull(c["decision_quote"], " big")}
        </section>

        <section aria-labelledby="next-title">
          <p class="eyebrow rv"><i class="dm"></i>What's next</p>
          <h2 id="next-title" class="rv">Where they go from here</h2>
          <p>{rich(c["next"], k)}</p>
        </section>
      </div>

      <aside class="st-aside" aria-label="Story details">
        <div class="st-aside-in">
          <p class="eyebrow"><i class="dm"></i>In this story</p>
          <ul class="st-toc">
            <li><a href="#ctx-title">Context</a></li><li><a href="#ch-title">The challenge</a></li><li><a href="#sol-title">The solution</a></li><li><a href="#res-title">The results</a></li><li><a href="#next-title">What's next</a></li>
          </ul>
          <p class="eyebrow"><i class="dm"></i>Capabilities used</p>
          <div class="m-tags">{tags}</div>
          <a class="pricing" href="index.html#open">Schedule a demo</a>
        </div>
      </aside>
    </div>
  </article>

  <!-- ================= Closing: CTA, more stories, FAQ ================= -->
  <section class="sec mist" id="more" aria-labelledby="more-title">
    <div class="inner">
      <div class="sec-head">
        <div>
          <p class="eyebrow rv"><i class="dm"></i>More stories</p>
          <h2 id="more-title" class="rv" style="--d:1">From other services <b>and industries.</b></h2>
        </div>
        <a class="link-arrow rv" style="--d:2" href="customer-stories.html">All customer stories {ARR}</a>
      </div>
      <ul class="sc-grid">
{others_html}
      </ul>
    </div>
  </section>

  <section class="sec" id="faq" aria-labelledby="faq-title">
    <div class="inner faq-wrap">
      <div>
        <p class="eyebrow rv"><i class="dm"></i>FAQ</p>
        <h2 id="faq-title" class="rv" style="--d:1">Questions about <b>{e(BY_KEY[k]["name"])}.</b></h2>
      </div>
      <div class="faq rv" style="--d:2">
{faq_html}
      </div>
    </div>
  </section>

  <section class="sec cta" id="open" aria-labelledby="cta-title">
    <div class="inner cta-grid">
      <div class="bigdoor" aria-hidden="true">
        <span class="floor"></span><span class="frame"></span><span class="light"></span><span class="panel-d"></span>
      </div>
      <div>
        <p class="eyebrow rv"><i class="dm"></i>Your story next</p>
        <h2 id="cta-title" class="rv" style="--d:1">Get results <b>like these.</b></h2>
        <p class="lede rv" style="--d:2">Book a demo of {e(BY_KEY[k]["name"])} with your own use case.</p>
        <div class="cta-actions rv" style="--d:3">
          <a class="pricing" href="index.html#open">Schedule a demo</a>
          <a class="link-arrow on-dark" href="index.html#open">Request a free consultation {ARR}</a>
        </div>
      </div>
    </div>
  </section>
</main>

{FOOTER}

<script src="js/site.js"></script>
<script src="js/services-menu.js"></script>
</body>
</html>
"""

def main():
    idx = (ROOT / "index.html").read_text(encoding="utf-8")
    import re
    mitra = re.search(r'<ul class="mitra-track">.*?</ul>', idx, re.S).group(0)
    out = ROOT / "customer-stories.html"
    out.write_text(site_nav.with_icons(page(mitra)), encoding="utf-8")
    print("wrote", out.name, f"({len(STORIES)} stories)")
    for st in STORIES:
        if st["slug"] in STORY_CONTENT:
            p = ROOT / f"story-{st['slug']}.html"
            p.write_text(site_nav.with_icons(story_page(st, mitra)), encoding="utf-8")
            print("wrote", p.name)


if __name__ == "__main__":
    main()
