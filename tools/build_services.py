"""Build the six service detail pages from one template.

Run from the project root:  python3 tools/build_services.py

Content follows docs/kerangka-halaman-layanan.md; capability names and descriptions come from
docs/service-capability-breakdown.md. Edit the SERVICES data below, then re-run to regenerate
every service-*.html page. The nav logo and partner logo strip are copied from index.html.
"""
import html
import json
import re
from pathlib import Path

import site_nav

ROOT = Path(__file__).resolve().parent.parent
e = html.escape

# --------------------------------------------------------------------------------------------
# Shared taxonomy: parent (shared) capabilities and which service capabilities sit under them
# --------------------------------------------------------------------------------------------
PARENTS = {
    "Real-time Dashboard & Monitoring": {
        "acd": ["Real-time Institution Monitoring"],
        "net": ["Network Monitoring", "Web/API Monitoring", "Linux Server Monitoring", "Network Status History", "Traffic & Bandwidth Monitoring"],
        "cam": ["Device Data Storage & Dashboard"],
        "gai": ["Usage & Cost Monitoring"],
    },
    "Reporting & Analytics": {
        "crm": ["Interaction Analytics"],
        "acd": ["Institution Data Management", "Learning Performance Tracking"],
        "net": ["Automated Reporting", "Network Quality Analysis"],
        "cam": ["People Counting & Crowd Detection"],
        "doc": ["Audit Trail"],
        "gai": ["Usage & Cost Monitoring"],
    },
    "Notifications & Alerts": {
        "crm": ["Broadcast (Blast)", "Scheduling & Reminders"],
        "acd": ["Real-time Attendance"],
        "net": ["Real-time Notifications"],
        "cam": ["Intruder Detection"],
        "doc": ["Approval Workflow"],
    },
    "AI & Automation": {
        "crm": ["Chatbot Builder"],
        "net": ["Proactive & Predictive Maintenance"],
        "cam": ["Intruder Detection", "Fire & Smoke Detection", "People Counting & Crowd Detection", "Employee Presence"],
        "doc": ["AI Document Assistant"],
        "gai": ["Model Management", "Knowledge Base (RAG)", "AI Agent & Workflow Builder"],
    },
    "Cloud Storage": {
        "acd": ["Learning Content"],
        "cam": ["Cloud Recording"],
        "doc": ["Central Repository", "Version Control", "Retention & Archiving"],
        "gai": ["Knowledge Base (RAG)"],
    },
    "User & Access Management": {
        "acd": ["Role-based Portals"],
        "cam": ["Security & Access Management"],
        "doc": ["Access Control & Sharing", "Audit Trail"],
        "gai": ["Access Control", "Guardrails & Data Privacy"],
    },
    "API Integration": {
        "crm": ["WhatsApp API"],
        "cam": ["IoT Connectivity", "Smart Device Integration"],
        "doc": ["Electronic Signature"],
        "gai": ["API & SDK"],
    },
    "Communication & Chatbot": {
        "crm": ["Omnichannel Inbox", "Conversation Labeling", "Knowledge Base", "Ticketing"],
        "gai": ["AI Chat Assistant"],
    },
    "Mobile App": {"acd": ["Mobile Apps"]},
}
# Group titles for the "all capabilities" grid, keyed by parent capability
GROUP_TITLE = {
    "Communication & Chatbot": "Conversations",
    "Real-time Dashboard & Monitoring": "Monitoring & dashboards",
    "Reporting & Analytics": "Reports & analytics",
    "Notifications & Alerts": "Alerts & reminders",
    "AI & Automation": "AI & automation",
    "Cloud Storage": "Storage & content",
    "User & Access Management": "Access & security",
    "API Integration": "Integrations",
    "Mobile App": "Mobile",
}

# --------------------------------------------------------------------------------------------
# Service content
# --------------------------------------------------------------------------------------------
SERVICES = [
    # ======================================================================================
    dict(
        key="acd", slug="academic-management", name="Academic Management", taxonomy="Academic Management",
        icon="academic-management.png", photo=None,
        estimated=False,
        seo_title="Academic Management | Attendance to learning progress for schools — Telkom Digital",
        seo_desc="Academic Management brings attendance, assessments and learning progress into one place for 6,500+ schools and institutions, with Computer-based Assessment and Real-time Attendance.",
        core="from attendance to learning progress, in one place",
        h1=("Paper registers record attendance.", "Academic Management shows how students learn."),
        sub="Academic Management helps schools and institutions run classes, assessments and grades, and see each student's progress <strong>from attendance to learning progress, in one place</strong>.",
        nums=[("6,500+", "schools and institutions")],
        mock=dict(title="Class 8B · Today", chip="Live", rows=[("Attendance", "31 / 32", 97), ("Fractions quiz submitted", "28", 88), ("Class average", "84", 84)], alert=("ok", "Attendance sent to parents at 07:45")),
        connects=["iOS app", "Android app", "Teacher app", "Web portal", "Parent access", "Education office view"],
        problem_title=("Attendance is recorded.", "Learning is not."),
        problem=["Today, many schools keep attendance on paper, grades in spreadsheets and assignments in chat groups. By the time a teacher sees that a student is falling behind, the term is half over.",
                 "The problem is no longer collecting data. It is that <strong>attendance, assignments and grades live in different places</strong>, so no one sees the whole picture in time."],
        steps=[("Set up your institution", "Import classes, teachers and students, and give each role its own portal."),
               ("Plan the term", "Add learning content, assignments and assessments to each subject."),
               ("Follow progress", "Attendance, grades and activity update in real time for teachers, students and parents.")],
        effort="Works in a browser and on iOS and Android: no servers to install at school.",
        featured=[
            dict(cap="Computer-based Assessment", title="Run a test and see the scores the same day",
                 body="When a teacher sets a quiz, students answer online and scores arrive as soon as they finish, without stacks of paper to mark.",
                 mock=dict(title="Fractions quiz · 8B", chip="Scored", rows=[("Submitted", "28 / 32", 88), ("Average score", "81", 81), ("Needs review", "4 students", 12)])),
            dict(cap="Real-time Attendance", title="Parents know their child arrived before first period",
                 body="As students check in, attendance is visible to teachers, parents and the institution at the same moment.",
                 mock=dict(title="Attendance · 07:40", chip="Live", rows=[("Present", "31", 97), ("Late", "1", 3)], alert=("ok", "Parents notified"))),
            dict(cap="Learning Performance Tracking", title="Spot a student falling behind in week three, not week ten",
                 body="Teachers follow progress and activity per subject, <strong>from attendance to learning progress, in one place</strong>, and step in early.",
                 mock=dict(title="Rani · Mathematics", chip="Trend", rows=[("Assignments done", "9 / 12", 75), ("Average grade", "68", 68)], alert=("warn", "Below class average for 3 weeks"))),
            dict(cap="Role-based Portals", title="Every role sees only what it needs",
                 body="Management, teachers, students, parents, admins and education offices each get their own view of the same data.",
                 mock=dict(title="Portals", chip="6 roles", rows=[("Management", "Institution view", None), ("Teachers", "Class view", None), ("Parents", "Child view", None)])),
        ],
        proof=dict(kind="usage", value="6,500", unit="schools & institutions", text="Schools and institutions across Indonesia already run attendance, assessments and grades on Academic Management.", source="Figure as reported on the service website (Pijar Sekolah)."),
        roles=[
            ("Institution management", "See the whole school at a glance", "A principal checks attendance and grade trends across classes before the weekly meeting.", ["Real-time Institution Monitoring", "Institution Data Management"]),
            ("Teachers", "Mark less, teach more", "A teacher sets an online quiz in the morning and reviews the scores at lunch.", ["Computer-based Assessment", "Assignment Management"]),
            ("Students & parents", "Follow progress from home", "A parent sees attendance and new grades on their phone the same day.", ["Real-time Attendance", "Mobile Apps"]),
            ("School admins", "Keep records in one place", "An admin updates class lists and grades once, and every portal stays in sync.", ["Institution Data Management", "Grade Management"]),
            ("Education offices", "Compare institutions with live data", "A district office follows attendance across schools without waiting for monthly reports.", ["Role-based Portals", "Real-time Institution Monitoring"]),
        ],
        security=[("Role-based access", "Each portal shows only the data that role is allowed to see."),
                  ("Student data protected", "Personal data is handled under Indonesia's Personal Data Protection Law (UU PDP No. 27/2022).")],
        related=[("ip-camera-management", "Pair campus cameras with attendance: Employee Presence and crowd detection keep sites safe."),
                 ("document-management", "Keep school letters, decrees and reports in one repository with approvals.")],
        pack=dict(title="Sized to your institution", text="Packages depend on the number of students and the portals you need. Tell us about your school and we will propose a package.", items=["Portals for every role", "Mobile apps for students and teachers", "Support in Bahasa Indonesia"]),
        faq_extra=[],
        faq=dict(
            what="Academic Management is a platform for schools and institutions to run attendance, assignments, assessments and grades, and to follow each student's progress, from attendance to learning progress, in one place.",
            who="Schools, madrasah, universities and training institutions, from a single campus to a group of institutions, plus education offices that oversee them.",
            diff="Paper registers and spreadsheets record data but do not connect it. Academic Management links attendance, assignments and grades so teachers and parents see progress as it happens.",
            need="Class lists, teacher and student data, and an internet connection. Teachers and students can use a browser or the mobile apps.",
            time="It depends on the number of classes and the data you bring. After a consultation, our team shares a rollout plan for your institution.",
            connect="Students and teachers use the iOS and Android apps or the web portal. Ask us about connecting other systems you already run.",
            security="Each role sees only its own data, and personal data is protected under UU PDP No. 27/2022.",
            price="Pricing depends on the number of students and modules. Contact us for a package proposal.",
        ),
    ),
    # ======================================================================================
    dict(
        key="doc", slug="document-management", name="Document Management", taxonomy="Document Management",
        icon="document-management.png", photo="document.jpg",
        estimated=True,
        seo_title="Document Management | Find, approve and sign documents for legal and finance teams — Telkom Digital",
        seo_desc="Document Management keeps every document found, approved and signed in one place, with Central Repository, Search & OCR and Electronic Signature.",
        core="every document found, approved and signed in one place",
        h1=("Documents scattered across folders and email.", "Find, approve and sign them in one place."),
        sub="Document Management helps legal, finance and secretariat teams store, review and sign documents, with <strong>every document found, approved and signed in one place</strong>.",
        nums=[("10", "document capabilities in one service")],
        mock=dict(title="PKS_Mitra_2026.pdf · v4", chip="In review", rows=[("Legal", "Approved", 100), ("Finance", "Approved", 100), ("Director", "Waiting", 40)], alert=("warn", "Signature due today, 17:00")),
        connects=["Electronic signature", "e-Stamp", "Scanned documents (OCR)", "Shared links"],
        problem_title=("The document exists.", "Finding the right version does not."),
        problem=["Today, contracts and letters move as email attachments and shared folders. Someone signs the wrong version, an approval sits in an inbox for days, and an audit means searching through years of files.",
                 "The problem is not storage. It is that <strong>documents, approvals and signatures happen in different places</strong>, so no one can see where a document stands."],
        steps=[("Bring your documents in", "Upload files and scans into folders with metadata and tags."),
               ("Set the flow", "Define who reviews, who approves and who signs each document type."),
               ("Work from one place", "Search, approve and sign, with every action recorded.")],
        effort="Runs in the cloud: no document server to maintain.",
        featured=[
            dict(cap="Central Repository", title="One home for every contract and letter",
                 body="When a new agreement arrives, it goes into one organised repository with <strong>every document found, approved and signed in one place</strong>.",
                 mock=dict(title="Legal / Contracts / 2026", chip="128 files", rows=[("PKS_Mitra_2026.pdf", "v4", None), ("NDA_Vendor_A.pdf", "v2", None), ("SK_Direksi_014.pdf", "v1", None)])),
            dict(cap="Search & OCR", title="Find a clause in a scanned contract in seconds",
                 body="Full-text search reads scanned documents too, so a team can find a clause without opening every file.",
                 mock=dict(title="Search: \"force majeure\"", chip="OCR", rows=[("PKS_Mitra_2026.pdf", "p. 12", None), ("Kontrak_2019_scan.pdf", "p. 7", None)])),
            dict(cap="Approval Workflow", title="Know exactly who is holding an approval",
                 body="Multi-level review shows each step, so a director sees what is waiting and a requester sees why.",
                 mock=dict(title="Approval · PKS_Mitra_2026", chip="Step 3 / 3", rows=[("Legal", "Approved", 100), ("Finance", "Approved", 100), ("Director", "Waiting", 40)])),
            dict(cap="Electronic Signature", title="Sign without printing",
                 body="Once approved, documents are signed digitally, with e-stamp integration, and filed back automatically.",
                 mock=dict(title="Ready to sign", chip="e-Sign", rows=[("Signer", "Director", None), ("e-Stamp", "Attached", None)], alert=("ok", "Signed copy filed to Contracts / 2026"))),
        ],
        proof=dict(kind="logos"),
        roles=[
            ("Legal", "Find the latest signed version every time", "A legal officer pulls up the signed contract and its history during a negotiation.", ["Version Control", "Search & OCR"]),
            ("Corporate secretariat", "Send decrees for approval without chasing", "The secretariat routes a board decree and sees each approval as it happens.", ["Approval Workflow", "Electronic Signature"]),
            ("Finance", "Close the month with every invoice on file", "Finance finds supporting documents for an expense in one search.", ["Central Repository", "Search & OCR"]),
            ("Compliance & audit", "Answer an audit request in an afternoon", "An auditor sees who viewed, edited or shared a document and when.", ["Audit Trail", "Retention & Archiving"]),
        ],
        security=[("Access per document", "Role-based permissions and expiring share links control who sees each file."),
                  ("Full audit trail", "Every view, edit and share is logged for supervision and audit.")],
        related=[("privategpt", "Ask questions of your documents in plain language, with answers that cite the source file."),
                 ("omnichannel-management", "Send approved letters and notices to customers from the same platform.")],
        pack=dict(title="Start with your busiest documents", text="Packages depend on users, storage and the workflows you need. We usually start with one document type, such as contracts.", items=["Repository, search and version control", "Approval workflows per document type", "Electronic signature add-on"]),
        faq_extra=[],
        faq=dict(
            what="Document Management is a platform to store, search, approve and sign documents, with every document found, approved and signed in one place.",
            who="Legal, corporate secretariat, finance and compliance teams in organisations that handle contracts, decrees and letters every day.",
            diff="Shared folders and email store files but do not track versions, approvals or signatures. Document Management keeps all three with the document.",
            need="The documents you want to bring in and a list of who approves each document type. Scans can be uploaded as they are.",
            time="It depends on the volume of documents and the workflows you need. Our team shares a plan after a consultation.",
            connect="Documents can be signed electronically with e-stamp integration. Ask us about connecting other systems you run.",
            security="Access is set per document and role, share links can expire, and every action is logged in the audit trail.",
            price="Pricing depends on users, storage and workflows. Contact us for a proposal.",
        ),
    ),
    # ======================================================================================
    dict(
        key="cam", slug="ip-camera-management", name="IP Camera Management", taxonomy="IP Cam Management",
        icon="ip-cam-management.png", photo="ip-camera.jpg",
        estimated=False,
        seo_title="IP Camera Management | Live AI alerts for stores, sites and offices — Telkom Digital",
        seo_desc="IP Camera Management turns cameras into alerts while it happens, with Cloud Recording and Intruder Detection, used by 100 enterprise partners with 55,800 connected devices.",
        core="cameras that alert you while it happens, not after",
        h1=("Ordinary CCTV records what happened.", "IP Camera Management tells you as it happens."),
        sub="IP Camera Management helps business owners and security teams watch every site from one app, with AI detection and cloud recording: <strong>cameras that alert you while it happens, not after</strong>.",
        nums=[("100", "enterprise partners"), ("55,800", "connected devices")],
        mock=dict(title="Warehouse · Rear door", chip="AI", rows=[("Cameras online", "48 / 48", 100), ("Visitors today", "1,284", 64)], alert=("warn", "Intruder detected · 02:14 · clip saved")),
        connects=["IP cameras", "Smart lamps", "Smart plugs", "Door sensors", "LoRaWAN", "NB-IoT", "GPRS"],
        problem_title=("The footage exists.", "The alert came too late."),
        problem=["Today, most CCTV records to a box in the back office. When something goes wrong, someone scrolls through hours of video the next morning, and the moment to act has passed.",
                 "The problem is not recording. It is that <strong>no one is told while it is happening</strong>."],
        steps=[("Connect your cameras", "Add IP cameras and smart devices at each site to one account."),
               ("Choose what to detect", "Turn on intruder, fire and smoke, crowd or presence detection per camera."),
               ("Get alerted", "Alerts and recordings arrive on any device, for every site.")],
        effort="Footage is stored in the cloud: no local recorder to manage at each site.",
        featured=[
            dict(cap="Cloud Recording", title="Footage you can open from anywhere",
                 body="When an incident is reported, a manager opens the clip on a phone and shares it, with automatic backup in the cloud.",
                 mock=dict(title="Recordings · Store 12", chip="Cloud", rows=[("Entrance · 14:02", "02:31", None), ("Cashier · 13:47", "01:10", None)], alert=("ok", "Backed up automatically"))),
            dict(cap="Intruder Detection", title="Know about a break-in while it is happening",
                 body="AI flags suspicious activity and sends an alert straight away: <strong>cameras that alert you while it happens, not after</strong>.",
                 mock=dict(title="Warehouse · Rear door", chip="AI", rows=[("Motion after hours", "Detected", 100)], alert=("warn", "Intruder detected · 02:14"))),
            dict(cap="People Counting & Crowd Detection", title="See when a store gets crowded",
                 body="Visitor counts and crowd alerts help a store manager open another cashier before the queue grows.",
                 mock=dict(title="Store 12 · Entrance", chip="Today", rows=[("Visitors", "1,284", 64), ("Crowd level", "High", 86)])),
            dict(cap="Multi-site Deployment", title="Every location in one view",
                 body="Security teams manage large numbers of cameras across branches from one place, instead of one recorder per site.",
                 mock=dict(title="All sites", chip="12 sites", rows=[("Jakarta", "18 cameras", None), ("Surabaya", "14 cameras", None), ("Medan", "16 cameras", None)])),
        ],
        proof=dict(kind="story", stat=("55,800", "connected devices", "Across 100 enterprise partners. Figure as reported on the service website (Antares).")),
        roles=[
            ("Business owners", "Check every branch from your phone", "An owner opens the live view of three stores while travelling.", ["Multi-site Deployment", "Cloud Recording"]),
            ("Head of security", "Act on alerts, not on footage", "The security lead receives an intruder alert at night and dispatches a guard.", ["Intruder Detection", "Fire & Smoke Detection"]),
            ("Facility managers", "Keep buildings safe and efficient", "A facility manager controls smart lamps and door sensors from the same app.", ["Smart Device Integration", "IoT Connectivity"]),
            ("HR teams", "Record staff presence without a queue", "HR sees who has arrived at each site from camera-based presence.", ["Employee Presence"]),
            ("Store managers", "Staff up before the rush", "A manager opens another cashier when crowd levels rise.", ["People Counting & Crowd Detection"]),
        ],
        security=[("Encrypted devices and data", "Security & Access Management encrypts device data and controls who can view each camera."),
                  ("Access per site", "Grant each team access only to the locations they look after.")],
        related=[("network-management", "Keep the networks your cameras depend on online, with alerts before they fail."),
                 ("academic-management", "Bring camera-based presence to campuses alongside student attendance.")],
        pack=dict(title="Scale from one store to hundreds", text="Packages depend on the number of cameras, sites and AI detections you switch on.", items=["Cloud recording with auto-backup", "AI detections per camera", "IoT connectivity options"]),
        faq_extra=[],
        faq=dict(
            what="IP Camera Management connects your IP cameras and smart devices to one app with AI detection and cloud recording: cameras that alert you while it happens, not after.",
            who="Retail chains, warehouses, offices, campuses and facilities, from a single site to many locations.",
            diff="Ordinary CCTV records to a local box for review later. IP Camera Management detects intruders, fire, smoke and crowds as they happen and stores footage in the cloud.",
            need="IP cameras and an internet connection at each site. Our team can advise if your existing cameras are compatible.",
            time="It depends on the number of sites and cameras. After a site survey and consultation, our team shares a rollout plan.",
            connect="Yes: smart lamps, plugs and door sensors work in the same app, with LoRaWAN, NB-IoT and GPRS connectivity options.",
            security="Device data is encrypted and access is controlled per user and site through Security & Access Management.",
            price="Pricing depends on cameras, sites and detections. Contact us for a quote.",
        ),
    ),
    # ======================================================================================
    dict(
        key="net", slug="network-management", name="Network Management", taxonomy="Network Monitoring Management",
        icon="network-monitoring.png", photo="network.jpg",
        estimated=False,
        seo_title="Network Management | Predictive network monitoring for IT teams — Telkom Digital",
        seo_desc="Network Management lets IT teams know about network issues before users do, with Network Monitoring and Proactive & Predictive Maintenance, used by 1,000+ companies.",
        core="know about network issues before your users do",
        h1=("Most monitoring tells you the network is down.", "We tell you before it happens."),
        sub="Network Management helps IT teams watch networks, servers, websites and APIs from one dashboard, with predictive alerts, so you <strong>know about network issues before your users do</strong>.",
        nums=[("1,000+", "companies")],
        mock=dict(title="Core router · Jakarta", chip="Live", rows=[("Latency", "4 ms", 18), ("Packet loss", "0.01%", 4), ("Link utilisation", "82%", 82)], alert=("warn", "Utilisation trending up · check within 2 h")),
        connects=["Network devices", "Websites", "HTTP APIs", "Linux servers", "PDF reports"],
        problem_title=("Your users found the outage.", "Your dashboard found it second."),
        problem=["Today, many IT teams learn about an outage from a complaint. They log in, find the failed link and start fixing, while the business waits.",
                 "The problem is not seeing that something broke. It is that <strong>warning signs were there before it broke</strong>, and no one was told."],
        steps=[("Add what you run", "Register network devices, servers, websites and APIs to monitor."),
               ("Set thresholds", "Choose who is alerted, for which device, and when."),
               ("Stay ahead", "Dashboards, predictive alerts and reports keep the team ahead of outages.")],
        effort="Monitoring is tailored to your company with Customization.",
        featured=[
            dict(cap="Network Monitoring", title="See every device on one dashboard",
                 body="Data from network devices flows into analytics dashboards, so an engineer sees the health of every site at a glance.",
                 mock=dict(title="Network · All sites", chip="Live", rows=[("Devices up", "412 / 414", 99), ("Avg latency", "6 ms", 20)])),
            dict(cap="Web/API Monitoring", title="Know your website is reachable before customers try",
                 body="Websites and HTTP APIs are checked continuously, so a failed endpoint is caught before checkout breaks.",
                 mock=dict(title="api.partner.co.id/orders", chip="HTTP 200", rows=[("Uptime (30 days)", "99.97%", 99), ("Response time", "182 ms", 30)])),
            dict(cap="Proactive & Predictive Maintenance", title="Fix the link before it fails",
                 body="Proactive alerts on every module and predictive maintenance for networks mean you <strong>know about network issues before your users do</strong>.",
                 mock=dict(title="Link JKT–SBY", chip="Predictive", rows=[("Utilisation", "82%", 82)], alert=("warn", "Likely saturation in ~2 hours"))),
            dict(cap="Automated Reporting", title="Send the monthly report in one click",
                 body="Choose a period and export a PDF report for management, without building slides by hand.",
                 mock=dict(title="Report · September 2026", chip="PDF", rows=[("Availability", "99.95%", 99), ("Incidents", "3", 10)], alert=("ok", "Report ready to download"))),
        ],
        proof=dict(kind="usage", value="1,000", unit="companies", text="Companies across Indonesia monitor their networks, servers and APIs with Network Management.", source="Figure as reported on the service website (Netmonk)."),
        roles=[
            ("IT managers", "Report uptime without chasing data", "An IT manager exports last month's availability report for the board.", ["Automated Reporting", "Network Status History"]),
            ("Network engineers", "Fix problems before tickets arrive", "An engineer gets a predictive alert and reroutes traffic before peak hours.", ["Proactive & Predictive Maintenance", "Real-time Notifications"]),
            ("DevOps teams", "Watch servers and APIs together", "A DevOps engineer sees a Linux server and the API it serves on one screen.", ["Linux Server Monitoring", "Web/API Monitoring"]),
            ("Business owners", "Know the network is fine without asking", "An owner checks one dashboard instead of calling IT.", ["Network Monitoring"]),
        ],
        security=[("Monitoring scoped to your tenant", "Each company sees only its own devices, servers and reports.")],
        related=[("ip-camera-management", "Cameras and IoT devices depend on the network: monitor both from the same platform."),
                 ("omnichannel-management", "Tell customers about planned maintenance across every channel.")],
        pack=dict(title="Pick the modules you monitor", text="Packages depend on the number of devices and the modules you need: network, web/API or Linux server.", items=["Network, web/API and server modules", "Real-time and predictive alerts", "One-click PDF reports"]),
        faq_extra=[("What is coming soon?", "Traffic & Bandwidth Monitoring and Network Quality Analysis are coming soon. They are marked as such in the capability list.")],
        faq=dict(
            what="Network Management monitors your networks, servers, websites and APIs from one dashboard, with predictive alerts, so you know about network issues before your users do.",
            who="IT managers, network engineers and DevOps teams in companies of any size, plus owners who want one view of their network.",
            diff="Basic monitoring tools tell you when something is already down. Network Management adds proactive and predictive alerts so you can act before users notice.",
            need="Access to the devices, servers, websites and APIs you want to monitor.",
            time="It depends on how many devices and modules you monitor. Our team shares a plan after a consultation.",
            connect="It monitors network devices, websites, HTTP APIs and Linux servers, and exports reports as PDF.",
            security="Each company's monitoring data stays in its own tenant, with access through single sign-on.",
            price="Pricing depends on devices and modules. Contact us for a quote.",
        ),
    ),
    # ======================================================================================
    dict(
        key="crm", slug="omnichannel-management", name="Omnichannel Management", taxonomy="Customer Relationship Management",
        icon="crm.png", photo="omnichannel.jpg",
        estimated=False,
        seo_title="Omnichannel Management | One inbox for every customer channel — Telkom Digital",
        seo_desc="Omnichannel Management puts every customer conversation in one inbox, with Omnichannel Inbox, Chatbot Builder and WhatsApp API.",
        core="every customer conversation in one inbox",
        h1=("Customer messages come from everywhere.", "Answer them all from one place."),
        sub="Omnichannel Management helps customer service and marketing teams handle chat, voice and video, run chatbots and send broadcasts, with <strong>every customer conversation in one inbox</strong>.",
        nums=[("11", "customer service capabilities in one inbox")],
        mock=dict(title="Inbox · 14 open", chip="Live", rows=[("WhatsApp · \"Is my order shipped?\"", "2m", None), ("Web chat · \"Change my address\"", "5m", None), ("Ticket #2041 · Refund", "Resolved", None)], alert=("ok", "Chatbot answered 62 messages today")),
        connects=["WhatsApp API", "Chat", "Voice", "Video", "Broadcast"],
        problem_title=("Customers moved to chat.", "Your team is still switching apps."),
        problem=["Today, a customer writes on WhatsApp, calls the next day and chats on the website after that. Each message lands in a different place, so agents ask the same questions again.",
                 "The problem is not the number of channels. It is that <strong>the conversation and the customer's history are split across them</strong>."],
        steps=[("Connect your channels", "Bring WhatsApp, chat, voice and video into one inbox."),
               ("Set up answers", "Build a knowledge base, chatbot flows and labels for your team."),
               ("Serve and learn", "Agents reply from one place while analytics show what customers ask.")],
        effort="Start with the core inbox and add modules as you grow, with Modular Packages.",
        featured=[
            dict(cap="Omnichannel Inbox", title="Every conversation in one inbox",
                 body="When a customer switches from WhatsApp to a call, the agent sees the whole thread, with <strong>every customer conversation in one inbox</strong>.",
                 mock=dict(title="Budi S. · 3 channels", chip="History", rows=[("WhatsApp · Mon", "Order question", None), ("Voice · Tue", "Delivery date", None), ("Chat · Today", "Address change", None)])),
            dict(cap="Chatbot Builder", title="Answer common questions at 2 a.m.",
                 body="Build a 24/7 chatbot for frequent questions, with reports on message volume and response time.",
                 mock=dict(title="Chatbot · Today", chip="24/7", rows=[("Messages handled", "62", 62), ("Handed to an agent", "9", 14)])),
            dict(cap="Ticketing", title="No complaint gets lost",
                 body="Complaints and requests become tickets that are logged, tracked and resolved, so a customer never has to repeat themselves.",
                 mock=dict(title="Ticket #2041 · Refund", chip="Resolved", rows=[("Opened", "Mon 09:12", None), ("Assigned", "Finance", None), ("Resolved", "Tue 15:40", None)])),
            dict(cap="Interaction Analytics", title="See what customers ask most",
                 body="Patterns across conversations show which questions to answer in the knowledge base next.",
                 mock=dict(title="Top topics · This week", chip="Analytics", rows=[("Delivery status", "38%", 38), ("Payment", "22%", 22), ("Returns", "14%", 14)])),
        ],
        proof=dict(kind="logos"),
        roles=[
            ("Business owners", "Serve customers without hiring for every channel", "An owner answers WhatsApp and web chat from one inbox.", ["Omnichannel Inbox", "Modular Packages"]),
            ("Customer service managers", "Know where every complaint stands", "A manager tracks open tickets and response times each morning.", ["Ticketing", "Interaction Analytics"]),
            ("Customer service agents", "Reply with the full history in front of you", "An agent sees past orders and conversations before answering.", ["Customer Data & History", "Knowledge Base"]),
            ("Marketing teams", "Reach customers on the channel they use", "Marketing sends a promotion by broadcast and schedules reminders.", ["Broadcast (Blast)", "Scheduling & Reminders"]),
            ("Public service offices", "Answer citizens around the clock", "A public office runs a chatbot for common questions and hands the rest to staff.", ["Chatbot Builder", "WhatsApp API"]),
        ],
        security=[("Official WhatsApp integration", "Conversations run on the official WhatsApp API."),
                  ("Customer data in one tenant", "Contacts and interaction history stay in your company's own tenant.")],
        related=[("privategpt", "Ground chatbot answers in your company knowledge, with sources."),
                 ("document-management", "Attach approved documents and letters to customer conversations.")],
        pack=dict(title="Start small, add modules", text="Modular Packages let you start with the core inbox and add features as the business grows.", items=["Core: Omnichannel Inbox and Ticketing", "Add: Chatbot Builder and Broadcast (Blast)", "Add: WhatsApp API and Interaction Analytics"]),
        faq_extra=[],
        faq=dict(
            what="Omnichannel Management is a customer service platform that brings chat, voice, video and WhatsApp together, with every customer conversation in one inbox.",
            who="Businesses and public service offices of any size that talk to customers on more than one channel.",
            diff="Separate apps per channel split the conversation. Omnichannel Management keeps one thread and one customer history across channels.",
            need="The channels you want to connect. WhatsApp API needs a WhatsApp Business account; our team helps with the setup.",
            time="It depends on the channels and modules you start with. Our team shares a plan after a consultation.",
            connect="Yes: WhatsApp through the official API, plus chat, voice and video channels in the same inbox.",
            security="Contacts and conversations stay in your company's tenant, with access through single sign-on and roles.",
            price="Start with core features and add modules as you grow. Contact us for a package.",
        ),
    ),
    # ======================================================================================
    dict(
        key="gai", slug="privategpt", name="PrivateGPT", taxonomy="Generative AI Management",
        icon="program-lifecycle.png", photo="privategpt.jpg",
        estimated=True,
        seo_title="PrivateGPT | AI answers from your company data for enterprise teams — Telkom Digital",
        seo_desc="PrivateGPT gives AI answers grounded in your own data, with sources, kept private, with Knowledge Base (RAG) and Guardrails & Data Privacy.",
        core="AI answers grounded in your own data, with sources, kept private",
        h1=("Public AI guesses the answer.", "PrivateGPT answers from your data, with sources."),
        sub="PrivateGPT helps employees and IT teams use AI on internal documents and data, with <strong>AI answers grounded in your own data, with sources, kept private</strong>.",
        nums=[("9", "AI capabilities managed in one place")],
        mock=dict(title="PrivateGPT", chip="Private", rows=[("Q · Leave policy for contract staff?", "", None), ("A · 12 days per year, pro-rated", "", None), ("Source · HR Policy 2026, p. 4", "", None)], alert=("ok", "No personal data left your tenant")),
        connects=["Internal documents", "Company knowledge base", "API & SDK", "Multiple AI models"],
        problem_title=("Your team already uses AI.", "Your data should not leave to do it."),
        problem=["Today, employees paste internal documents into public chatbots to get quick answers. The answers sound confident but cite nothing, and company data leaves the building.",
                 "The problem is not whether to use AI. It is that <strong>answers need to come from your own data, and stay there</strong>."],
        steps=[("Connect your knowledge", "Add internal documents and data sources to the knowledge base."),
               ("Set the guardrails", "Choose models, who can use them, and what data is masked."),
               ("Ask and automate", "Employees ask questions and build agents, with usage tracked per team.")],
        effort="Managed in one place: models, prompts, access and costs.",
        featured=[
            dict(cap="Knowledge Base (RAG)", title="Answers that cite the document they came from",
                 body="When an employee asks about a policy, the answer comes from your own files, <strong>AI answers grounded in your own data, with sources, kept private</strong>.",
                 mock=dict(title="Ask PrivateGPT", chip="RAG", rows=[("Q · Reimbursement limit for travel?", "", None), ("Source · Travel Policy 2026, §3", "", None)])),
            dict(cap="AI Agent & Workflow Builder", title="Automate a repetitive task without code",
                 body="Teams build agents that summarise reports or draft replies, without waiting for a development project.",
                 mock=dict(title="Agent · Weekly summary", chip="Workflow", rows=[("Collect reports", "Done", 100), ("Summarise", "Done", 100), ("Send to managers", "Mon 08:00", 40)])),
            dict(cap="Guardrails & Data Privacy", title="Personal data stays masked",
                 body="Content filters and PII masking keep sensitive information out of prompts and answers, in line with data protection rules.",
                 mock=dict(title="Guardrails", chip="On", rows=[("PII masking", "Enabled", 100), ("Blocked topics", "4 rules", None)], alert=("ok", "2 ID numbers masked in this answer"))),
            dict(cap="Usage & Cost Monitoring", title="Know what AI costs, per team",
                 body="Token quotas, per-team costs and activity logs show IT where AI is used and keep spending predictable.",
                 mock=dict(title="Usage · September", chip="Quota", rows=[("Legal", "62%", 62), ("Finance", "41%", 41), ("Customer service", "78%", 78)])),
        ],
        proof=dict(kind="logos"),
        roles=[
            ("CIO & IT teams", "Offer AI without losing control of data", "IT gives every department AI access, with quotas and logs per team.", ["Usage & Cost Monitoring", "Access Control"]),
            ("Data & AI teams", "Switch models without rebuilding", "The data team compares models for a use case from one place.", ["Model Management", "API & SDK"]),
            ("Employees", "Get answers from company documents", "An employee asks about a policy and gets the paragraph that answers it.", ["Knowledge Base (RAG)", "AI Chat Assistant"]),
            ("Compliance", "Prove that sensitive data stays protected", "Compliance reviews guardrail rules and masked data in the logs.", ["Guardrails & Data Privacy"]),
        ],
        security=[("Guardrails & PII masking", "Content filtering and personal-data masking apply to every prompt and answer."),
                  ("Access per user and team", "Decide who can use which models and knowledge sources.")],
        related=[("document-management", "Keep the documents PrivateGPT answers from organised, versioned and approved."),
                 ("omnichannel-management", "Use AI answers to help agents reply to customers faster.")],
        pack=dict(title="Pay for what teams use", text="Packages depend on users, models and usage quotas. We help you start with one department and expand.", items=["Knowledge base on your documents", "Guardrails and access control", "Usage and cost dashboards"]),
        faq_extra=[],
        faq=dict(
            what="PrivateGPT is a managed generative AI service for companies: AI answers grounded in your own data, with sources, kept private.",
            who="Enterprises and public institutions that want employees to use AI on internal knowledge without sending data to public tools.",
            diff="Public AI chatbots answer from general training data and keep what you paste. PrivateGPT answers from your documents, cites the source and applies your guardrails.",
            need="The documents or data sources you want AI to answer from, and a list of teams who will use it.",
            time="It depends on the knowledge sources and teams you start with. Our team shares a plan after a consultation.",
            connect="Yes: other applications can use PrivateGPT through its API & SDK.",
            security="Guardrails mask personal data, access is set per user and team, and activity is logged.",
            price="Pricing depends on users, models and usage. Contact us for a proposal.",
        ),
    ),
]

# Descriptions from docs/service-capability-breakdown.md (exact names). Status: soon = coming soon
CAPS = {
    "crm": [("Omnichannel Inbox", "Manage conversations from multiple channels (chat, voice, video) in one inbox"),
            ("Customer Data & History", "Store contacts and the full history of every customer interaction"),
            ("Conversation Labeling", "Tag conversations by category for easier handling"),
            ("Knowledge Base", "Central answer library for fast, consistent responses"),
            ("Ticketing", "Log, track, and resolve customer complaints and requests"),
            ("Chatbot Builder", "Build 24/7 chatbots, with reports on message volume and response time"),
            ("Broadcast (Blast)", "Send mass announcements across channels"),
            ("WhatsApp API", "Official WhatsApp integration for personalized communication"),
            ("Scheduling & Reminders", "Sync meetings with customer contacts and send automatic reminders"),
            ("Interaction Analytics", "Analyze patterns in customer interactions"),
            ("Modular Packages", "Start with core features, add modules as the business grows")],
    "acd": [("Role-based Portals", "Dedicated views for institution management, teachers, students, parents, admins, and education offices"),
            ("Real-time Institution Monitoring", "Track attendance through learning outcomes in real time"),
            ("Computer-based Assessment", "Fast, interactive online assessments with scoring"),
            ("Assignment Management", "Assign online tasks, set deadlines, and grade directly"),
            ("Real-time Attendance", "Attendance data accessible to parents, teachers, and institutions"),
            ("Institution Data Management", "Manage institutional data to support decision-making"),
            ("Learning Content", "Interactive learning materials for students"),
            ("Grade Management", "Input and manage student grades"),
            ("Learning Performance Tracking", "Monitor student progress and activity per subject"),
            ("Mobile Apps", "Separate apps for students (iOS/Android) and teachers")],
    "net": [("Network Monitoring", "Collect data from network devices and visualize it in analytics dashboards"),
            ("Web/API Monitoring", "Ensure websites and HTTP APIs stay available and accessible"),
            ("Linux Server Monitoring", "Track visibility and performance of physical and virtual servers"),
            ("Automated Reporting", "One-click PDF reports for any selected period"),
            ("Proactive & Predictive Maintenance", "Proactive alerts on all modules; predictive maintenance for network monitoring"),
            ("Real-time Notifications", "Instant alerts on outages and recovery"),
            ("Network Status History", "Historical status graphs to spot patterns and potential issues"),
            ("Traffic & Bandwidth Monitoring", "Track data sent and received over time", "soon"),
            ("Network Quality Analysis", "Measure signal attenuation as a quality benchmark", "soon"),
            ("Customization", "Tailor monitoring to specific company needs")],
    # Live View & Playback is still an estimate, so it stays off the page until validated
    "cam": [("Cloud Recording", "Store footage securely in the cloud, accessible and shareable from any device, with auto-backup"),
            ("Intruder Detection", "AI detection of suspicious activity"),
            ("Fire & Smoke Detection", "AI detection of fire and smoke"),
            ("People Counting & Crowd Detection", "Analyze visitor patterns and detect crowding"),
            ("Employee Presence", "AI-based staff attendance monitoring"),
            ("Smart Device Integration", "Control cameras, smart lamps, plugs, and door sensors in one app"),
            ("Multi-site Deployment", "Manage large numbers of cameras across locations"),
            ("IoT Connectivity", "LoRaWAN, NB-IoT, and GPRS connectivity options"),
            ("Device Data Storage & Dashboard", "Store device data and display it in dashboards or other apps"),
            ("Security & Access Management", "Encryption and access control for devices and data")],
    "doc": [("Central Repository", "Upload and organize documents with folders, metadata, and tags"),
            ("Search & OCR", "Full-text search, including scanned documents"),
            ("Version Control", "Track revisions and restore previous versions"),
            ("Access Control & Sharing", "Role-based permissions and expiring share links"),
            ("Approval Workflow", "Multi-level review and approval flows"),
            ("Electronic Signature", "Digital signature and e-stamp integration"),
            ("Retention & Archiving", "Retention policies and automatic archiving"),
            ("Audit Trail", "Log who viewed, edited, or shared each document"),
            ("Document Templates", "Reusable templates for common documents"),
            ("AI Document Assistant", "Summaries, Q&A on document content, auto-classification")],
    "gai": [("Model Management", "Access and switch between multiple AI models in one place"),
            ("Knowledge Base (RAG)", "Ground AI answers in internal documents and data"),
            ("AI Chat Assistant", "Conversational assistant for employees or customers"),
            ("AI Agent & Workflow Builder", "Automate repetitive tasks without code"),
            ("Prompt Management", "Shared, reusable prompt templates"),
            ("Guardrails & Data Privacy", "Content filtering, PII masking, data protection compliance"),
            ("Usage & Cost Monitoring", "Token quotas, per-team costs, activity logs"),
            ("Access Control", "Permissions per user and team"),
            ("API & SDK", "Integrate AI capabilities into other applications")],
}

BY_KEY = {s["key"]: s for s in SERVICES}
BY_SLUG = {s["slug"]: s for s in SERVICES}
CODE = {"crm": "Omnichannel", "acd": "Academic", "net": "Network", "cam": "IP Camera", "doc": "Document", "gai": "PrivateGPT"}


def href(s):
    return f"service-{s['slug']}.html"


def parent_of(key, cap):
    """First parent capability that lists this service capability (the grouping parent)."""
    for p, m in PARENTS.items():
        if cap in m.get(key, []):
            return p
    return None


def also_in(key, cap):
    """Other services sharing a parent capability with this one."""
    others = []
    for p, m in PARENTS.items():
        if cap in m.get(key, []):
            others += [k for k in m if k != key and k not in others]
    order = ["acd", "doc", "cam", "net", "crm", "gai"]
    return [k for k in order if k in others]


# --------------------------------------------------------------------------------------------
# Rendering helpers
# --------------------------------------------------------------------------------------------
CUR = ' aria-current="page"'
ARR = '<svg aria-hidden="true"><use href="#arr"/></svg>'
CHEV = '<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M3 4.5l3 3 3-3" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
DCHEV = CHEV.replace('1.6', '1.4')


def mock(m, label):
    rows = []
    for lab, val, pct in m["rows"]:
        bar = f'<span class="mock-bar"><i style="--pct:{pct}%"></i></span>' if pct is not None else ''
        val_html = f'<em>{e(val)}</em>' if val else '<em></em>'
        rows.append(f'<li><span>{e(lab)}</span>{val_html}{bar}</li>')
    alert = ''
    if m.get("alert"):
        kind, text = m["alert"]
        alert = f'<div class="mock-alert{" ok" if kind == "ok" else ""}">{e(text)}</div>'
    return (f'<div class="mock" role="img" aria-label="{e(label)}">'
            f'<div class="mock-head"><span class="mock-dot"></span><b>{e(m["title"])}</b><span class="mock-chip">{e(m["chip"])}</span></div>'
            f'<ul class="mock-rows">{"".join(rows)}</ul>{alert}</div>')


def cap_link(key, cap):
    """Featured capability link: to its shared (Tier A) capability page, when it has one."""
    p = parent_of(key, cap)
    if not p or BY_KEY[key]["estimated"]:  # Tier A pages list validated services only
        return ''
    return f'<a class="link-arrow" href="{site_nav.CAP_HREF[p]}">Part of {e(p)} {ARR}</a>'


def faq_items(s):
    n, f = s["name"], s["faq"]
    alt = {"acd": "paper registers and spreadsheets", "doc": "shared folders and email", "cam": "ordinary CCTV",
           "net": "basic monitoring tools", "crm": "separate apps for each channel", "gai": "public AI chatbots"}[s["key"]]
    common = {"acd": "the mobile apps", "doc": "electronic signature", "cam": "smart devices and IoT networks",
              "net": "our servers, websites and APIs", "crm": "WhatsApp", "gai": "our other applications"}[s["key"]]
    qa = [(f"What is {n}?", f["what"]),
          (f"Who is {n} for?", f["who"]),
          (f"How is {n} different from {alt}?", f["diff"]),
          ("What do we need before we start?", f["need"]),
          ("How long does implementation take?", f["time"]),
          (f"Can it connect with {common}?", f["connect"]),
          ("How is our data kept secure?", f["security"]),
          ("How do packages and pricing work?", f["price"])]
    return qa + s["faq_extra"]


def page(s, logo, mitra):
    key, name = s["key"], s["name"]
    top = {f["cap"] for f in s["featured"]}
    nav_html, drawer_html = site_nav.nav(key, logo)

    # hero visual
    if s["photo"]:
        photo = f'<figure class="ph-photo leaf"><img src="assets/services/{s["photo"]}" alt="{e(PHOTO_ALT[key])}" width="1376" height="768"></figure>'
    else:
        photo = '<figure class="ph-photo leaf blank" aria-hidden="true"></figure>'
    nums = "".join(f'<div><b>{e(v)}</b><span>{e(u)}</span></div>' for v, u in s["nums"])

    connects = "".join(f"<li>{e(c)}</li>" for c in s["connects"])
    problem = "".join(f"<p>{p}</p>" for p in s["problem"])
    steps = "\n".join(f'        <li class="step rv" style="--d:{i}"><h3>{e(t)}</h3><p>{e(d)}</p></li>' for i, (t, d) in enumerate(s["steps"]))

    feats = []
    for i, f in enumerate(s["featured"], 1):
        proof = f'<div class="f-proof"><b>{e(f["proof"][0])}</b><span>{e(f["proof"][1])}</span></div>' if f.get("proof") else \
            f'<!-- TODO: evidence priority — add a partner quote or figure for {e(f["cap"])} -->'
        feats.append(f'''        <li class="feature rv">
          <div>
            <div class="f-top"><span class="f-no">0{i}</span><span class="tag">{e(f["cap"])}</span></div>
            <h3>{e(f["title"])}</h3>
            <p>{f["body"]}</p>
            {proof}
            {cap_link(key, f["cap"])}
          </div>
          <div class="feature-visual">{mock(f["mock"], f["cap"] + " preview")}</div>
        </li>''')

    # all capabilities grouped by parent
    groups = {}
    for c in CAPS[key]:
        cap, desc = c[0], c[1]
        soon = len(c) > 2 and c[2] == "soon"
        p = parent_of(key, cap)
        groups.setdefault(p, []).append((cap, desc, soon))
    order = [p for p in GROUP_TITLE if p in groups] + ([None] if None in groups else [])
    cards = []
    for p in order:
        title = GROUP_TITLE.get(p, f"Built for {name}")
        for cap, desc, soon in groups[p]:
            also = also_in(key, cap)
            also_html = f'<span class="also">Also in {", ".join(CODE[k] for k in also)}</span>' if also else ''
            status = '<span class="status soon">Coming soon</span>' if soon else '<span class="status">Available</span>'
            cards.append(f'          <li class="rv"><a class="cap-card{" top" if cap in top else ""}" href="{"#capabilities" if s["estimated"] else site_nav.CAP_HREF.get(p, "#capabilities")}"><small>{e(title)}</small><b>{e(cap)}</b><p>{e(desc)}</p><span class="cap-meta">{status}{also_html}</span></a></li>')
    gtxt = ['        <ul class="cap-grid">', *cards, '        </ul>']

    roles = "\n".join(f'''        <li class="role rv" style="--d:{i % 3}">
          <small>{e(r)}</small>
          <h3>{e(h)}</h3>
          <p>{e(sc)}</p>
          <div class="m-tags">{"".join(f'<span class="tag">{e(t)}</span>' for t in tags)}</div>
          <a class="link-arrow" href="index.html#open">Schedule a demo {ARR}</a>
        </li>''' for i, (r, h, sc, tags) in enumerate(s["roles"]))

    # partner proof (story if one exists for this service, else the kerangka fallbacks)
    pr = s["proof"]
    if pr["kind"] == "story":
        v, u, src = pr["stat"]
        proof_html = f'''      <div class="svc-story rv">
        <a class="story" href="story-national-retail-chain.html">
          <div class="story-img leaf"><img class="mirror" src="assets/landing/story-retail-v2.png" alt="Professional woman under a clear sky among city buildings" loading="lazy" style="object-position:66% 50%"></div>
          <div class="story-body">
            <div class="story-meta"><span class="chip">Retail · Case study</span><span class="tag">People Counting &amp; Crowd Detection</span></div>
            <h3>Retail supply chains, seen by computer vision</h3>
            <p>How a retailer uses IP Camera Management to track shelf availability in its stores, live, instead of waiting for manual stock checks.</p>
            <span class="link-arrow">Read the story {ARR}</span>
          </div>
        </a>
      </div>
      <div class="usage rv">
        <div><b>{e(v)}</b><span>{e(u)}</span></div>
        <div><p>Devices connected through IP Camera Management and IoT connectivity.</p><small>{e(src)}</small></div>
      </div>'''
    elif pr["kind"] == "usage":
        proof_html = f'''      <!-- Fallback 2 (no published story yet): usage figure. TODO: verify and date the figure -->
      <div class="usage rv">
        <div><b>{e(pr["value"])}<i>+</i></b><span>{e(pr["unit"])}</span></div>
        <div><p>{e(pr["text"])}</p><small>{e(pr["source"])}</small></div>
      </div>'''
    else:
        proof_html = f'''      <!-- Fallback 3 (no story or usage figure yet): partner logos. TODO: replace dummy logos with real {e(name)} partners -->
      <div class="mitra-strip proof-logos rv" aria-label="Partner logos">
        {mitra}
      </div>'''

    base_sec = [("Isolated tenants", "Your data stays apart from every other partner in its own tenant layer."),
                ("Single sign-on", "One account per person, with roles that decide who sees what."),
                ("Protected under UU PDP", "Personal data is handled under Indonesia's Personal Data Protection Law (No. 27/2022).")]
    sec = s["security"] + [b for b in base_sec if b[0] not in {x[0] for x in s["security"]}]
    if s["key"] == "acd":
        sec = [x for x in sec if x[0] != "Protected under UU PDP"]
    icons = ["icon-cloud.svg", "icon-user-key.svg", "icon-layout-dashboard.svg", "../form/ic-shield.svg", "icon-chart-network.svg"]
    sec_html = "\n".join(f'        <li class="rv" style="--d:{i}"><span class="pi"><img src="assets/landing/{icons[i % len(icons)]}" width="22" height="22" alt=""></span><div><h3>{e(t)}</h3><p>{e(d)}</p></div></li>' for i, (t, d) in enumerate(sec[:5]))

    rel = "\n".join(f'''          <li><a class="rel rv" href="{href(BY_SLUG[sl])}" style="--d:{i}"><img src="assets/capabilities/{BY_SLUG[sl]["icon"]}" alt=""><h3>{e(BY_SLUG[sl]["name"])}</h3><p>{e(t)}</p><span class="link-arrow">See the service {ARR}</span></a></li>''' for i, (sl, t) in enumerate(s["related"]))
    pk = s["pack"]
    pack_items = "".join(f"<li>{e(x)}</li>" for x in pk["items"])

    faqs = faq_items(s)
    faq_html = "\n".join(f'        <details{" open" if i == 0 else ""}>\n          <summary>{e(q)}</summary>\n          <p>{e(a)}</p>\n        </details>' for i, (q, a) in enumerate(faqs))
    ld = {"@context": "https://schema.org", "@type": "FAQPage",
          "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

    draft = f'''
<!--
  DRAFT CONTENT: every {e(s["taxonomy"])} capability is still an estimate in docs/service-capability-breakdown.md.
  Validate capabilities, integrations and claims with the product team before publishing.
-->''' if s["estimated"] else ''

    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(s["seo_title"])}</title>
<meta name="description" content="{e(s["seo_desc"])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,200..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<link rel="stylesheet" href="css/service.css">
<script type="application/ld+json">
{json.dumps(ld, indent=2, ensure_ascii=False)}
</script>
</head>
<body>
<!-- Generated by tools/build_services.py — edit the data there and re-run instead of editing this file -->{draft}
<!--
  Page data (Kerangka Halaman Layanan, 3.0)
  - Service: {e(s["taxonomy"])} (menu name: {e(name)})
  - Core message, repeated in hero, one featured capability and FAQ: "{e(s["core"])}"
  - TODO before publishing: verify every figure with the service team and add the update date
-->

<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
  <symbol id="arr" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></symbol>
</svg>

<section class="hero phero" id="hero">
{nav_html}

  <div class="inner ph-grid">
    <header class="ph-copy">
      <p class="eyebrow svc-crumb in" style="--i:1"><i class="dm"></i>Services <span class="sep">/</span> {e(name)}</p>
      <h1 class="ph-title in" style="--i:2">{e(s["h1"][0])} <b>{e(s["h1"][1])}</b></h1>
      <p class="lede in" style="--i:3">{s["sub"]}</p>
      <div class="hero-nums in" style="--i:4">{nums}</div>
      <div class="hero-cta in" style="--i:5">
        <a class="pricing" href="index.html#open">Schedule a demo</a>
        <a class="link-arrow" href="index.html#open">Talk to sales {ARR}</a>
      </div>
    </header>
    <div class="svc-visual in" style="--i:3">
      {photo}
      {mock(s["mock"], name + " preview")}
    </div>
  </div>
</section>

<div class="connects" aria-label="Connects with">
  <div class="inner">
    <p class="eyebrow"><i class="dm"></i>Connects with</p>
    <ul>{connects}</ul>
  </div>
</div>

{drawer_html}

<main>
  <!-- ================= Problem ================= -->
  <section class="sec mist" id="problem" aria-labelledby="problem-title">
    <div class="inner problem">
      <header>
        <p class="eyebrow rv"><i class="dm"></i>Why it matters</p>
        <h2 id="problem-title" class="rv" style="--d:1">{e(s["problem_title"][0])} <b>{e(s["problem_title"][1])}</b></h2>
      </header>
      <div class="problem-copy rv" style="--d:2">{problem}</div>
    </div>
  </section>

  <!-- ================= How it works ================= -->
  <section class="sec" id="how" aria-labelledby="how-title">
    <div class="inner">
      <p class="eyebrow rv"><i class="dm"></i>How it works</p>
      <h2 id="how-title" class="rv" style="--d:1">Three steps <b>to get started.</b></h2>
      <ol class="steps">
{steps}
      </ol>
      <p class="effort rv">{e(s["effort"])}</p>
    </div>
  </section>

  <!-- ================= Featured capabilities ================= -->
  <section class="sec mist" id="features" aria-labelledby="feat-title">
    <div class="inner">
      <div class="sec-head">
        <div>
          <p class="eyebrow rv"><i class="dm"></i>Featured capabilities</p>
          <h2 id="feat-title" class="rv" style="--d:1">What {e(name)} <b>does for you.</b></h2>
        </div>
      </div>
      <ol class="features">
{chr(10).join(feats)}
      </ol>
      <div class="features-cta rv"><a class="pricing" href="index.html#open">Schedule a demo</a></div>
    </div>
  </section>

  <!-- ================= All capabilities ================= -->
  <section class="sec" id="capabilities" aria-labelledby="caps-title">
    <div class="inner">
      <div class="sec-head">
        <div>
          <p class="eyebrow rv"><i class="dm"></i>All capabilities</p>
          <h2 id="caps-title" class="rv" style="--d:1">Everything in <b>{e(name)}.</b></h2>
        </div>
        <p class="lede rv" style="--d:2">Shared capabilities work the same way across services, so partners learn them once.</p>
      </div>
      <div class="cap-groups">
{chr(10).join(gtxt)}
      </div>
    </div>
  </section>

  <!-- ================= Use cases by role ================= -->
  <section class="sec mist" id="roles" aria-labelledby="roles-title">
    <div class="inner">
      <p class="eyebrow rv"><i class="dm"></i>Use cases by role</p>
      <h2 id="roles-title" class="rv" style="--d:1">Find your role, <b>see your day.</b></h2>
      <ul class="roles">
{roles}
      </ul>
    </div>
  </section>

  <!-- ================= Partner proof ================= -->
  <section class="sec" id="proof" aria-labelledby="proof-title">
    <div class="inner">
      <div class="sec-head">
        <div>
          <p class="eyebrow rv"><i class="dm"></i>Partner stories</p>
          <h2 id="proof-title" class="rv" style="--d:1">Already at work <b>with our partners.</b></h2>
        </div>
        <a class="link-arrow rv" style="--d:2" href="customer-stories.html?service={key}">All {e(name)} stories {ARR}</a>
      </div>
{proof_html}
    </div>
  </section>

  <!-- ================= Security ================= -->
  <section class="sec mist" id="security" aria-labelledby="sec-title">
    <div class="inner trust">
      <div>
        <p class="eyebrow rv"><i class="dm"></i>Security &amp; control</p>
        <h2 id="sec-title" class="rv" style="--d:1">Your data, <b>under your control.</b></h2>
        <p class="lede rv" style="--d:2">The answers your IT and legal teams will ask for.</p>
        <a class="link-arrow rv" style="--d:3" href="#">How we protect data {ARR}</a>
      </div>
      <!-- Only controls the service has today; add certifications once verified -->
      <ul class="eco-points trust-points">
{sec_html}
      </ul>
    </div>
  </section>

  <!-- ================= Related services + packages ================= -->
  <section class="sec" id="related" aria-labelledby="rel-title">
    <div class="inner">
      <p class="eyebrow rv"><i class="dm"></i>Works well with</p>
      <h2 id="rel-title" class="rv" style="--d:1">Better together <b>on one platform.</b></h2>
      <div class="related">
        <ul class="rel-list">
{rel}
        </ul>
        <div class="pack rv" style="--d:2">
          <small>Packages</small>
          <h3>{e(pk["title"])}</h3>
          <p>{e(pk["text"])}</p>
          <ul>{pack_items}</ul>
          <a class="link-arrow" href="index.html#open">Request a package proposal {ARR}</a>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= FAQ ================= -->
  <section class="sec mist" id="faq" aria-labelledby="faq-title">
    <div class="inner faq-wrap">
      <div>
        <p class="eyebrow rv"><i class="dm"></i>FAQ</p>
        <h2 id="faq-title" class="rv" style="--d:1">Questions about <b>{e(name)}.</b></h2>
      </div>
      <div class="faq rv" style="--d:2">
{faq_html}
      </div>
    </div>
  </section>

  <!-- ================= Closing CTA ================= -->
  <section class="sec cta" id="open" aria-labelledby="cta-title">
    <div class="inner cta-grid">
      <div class="bigdoor" aria-hidden="true">
        <span class="floor"></span><span class="frame"></span><span class="light"></span><span class="panel-d"></span>
      </div>
      <div>
        <p class="eyebrow rv"><i class="dm"></i>Get started</p>
        <h2 id="cta-title" class="rv" style="--d:1">See it <b>with your own data.</b></h2>
        <p class="lede rv" style="--d:2">{e(s["h1"][0])} {e(s["h1"][1])} Book a demo and we will show you how it works for your team.</p>
        <div class="cta-actions rv" style="--d:3">
          <a class="pricing" href="index.html#open">Schedule a demo</a>
          <a class="link-arrow on-dark" href="index.html#open">Request a consultation {ARR}</a>
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
'''


PHOTO_ALT = {
    "doc": "Office desk with a monitor showing a business dashboard",
    "cam": "Supermarket aisle with an automated inventory monitoring display",
    "net": "Network operations wall showing throughput, system health and threat maps",
    "crm": "Customer support dashboard with live metrics and a ticket queue",
    "gai": "Secure server racks glowing in a data centre",
}

FOOTER = site_nav.footer()


def main():
    idx = (ROOT / "index.html").read_text(encoding="utf-8")
    logo = site_nav.logo_from_index()
    mitra = re.search(r'<ul class="mitra-track">.*?</ul>', idx, re.S).group(0)
    for s in SERVICES:
        out = ROOT / href(s)
        out.write_text(site_nav.with_icons(page(s, logo, mitra)), encoding="utf-8")
        print("wrote", out.name)


if __name__ == "__main__":
    main()
