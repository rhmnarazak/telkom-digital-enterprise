"""Build the nine shared (Tier A) capability pages from one template.

Run from the project root:  python3 tools/build_capabilities.py

Structure follows docs/kerangka-halaman-kapabilitas.md (section 4). Child capabilities per
service come from the taxonomy in build_services.py (PARENTS / CAPS). Only validated services
appear: Document Management and PrivateGPT are still estimates, and taxonomy gaps are skipped.
"""
import html
import json
from urllib.parse import quote

import site_nav
from build_services import PARENTS, CAPS, BY_KEY, FOOTER, mock, ROOT

e = html.escape
ARR = site_nav.ARR
TI = ' tabindex="-1"'
VALIDATED = ["acd", "net", "cam", "crm"]          # services whose children may appear on Tier A pages
SOON = {c[0] for caps in CAPS.values() for c in caps if len(c) > 2 and c[2] == "soon"}
HIDDEN = {"Live View & Playback"}                 # still an estimate
SHORT = {"acd": "Academic", "net": "Network", "cam": "IP Camera", "crm": "Omnichannel"}
CODE = {"acd": "ACD", "net": "NET", "cam": "CAM", "crm": "CRM"}
USAGE = {  # usage figures per service, as reported on each service website (verify before publishing)
    "acd": ("6,500+", "schools & institutions use Academic Management", "Pijar Sekolah"),
    "net": ("1,000+", "companies use Network Management", "Netmonk"),
    "cam": ("55,800", "devices connected through IP Camera Management", "Antares"),
}
SETUP = {
    "acd": ("Set up your institution", "Import classes, teachers and students, and give each role its own portal."),
    "net": ("Add what you run", "Register network devices, servers, websites and APIs."),
    "cam": ("Connect your sites", "Add IP cameras and smart devices at each location to one account."),
    "crm": ("Connect your channels", "Bring WhatsApp, chat, voice and video into one inbox."),
}

# --------------------------------------------------------------------------------------------
# Content per capability. svc[key] = (role in that service, usage moment, configure step, act step)
# --------------------------------------------------------------------------------------------
CONTENT = {
    "Real-time Dashboard & Monitoring": dict(
        h1=("Live status on one screen,", "not a report a week later."),
        sub="Real-time Dashboard & Monitoring helps teams see what is happening now, from classrooms in Academic Management to networks and connected devices.",
        challenge=("Everyone has the data.", "No one sees it in time."),
        challenge_text="In a school, the principal hears about attendance problems in a monthly recap. In an IT team, network status lives in a tool only one engineer opens. On a site, device readings sit in a spreadsheet. The pattern is the same: status is collected, but no one sees it while it still matters.",
        benefits=[
            ("Spot problems while they are small", "Status updates as data arrives, so teams act in minutes instead of waiting for a recap.",
             dict(title="Branch links · Live", chip="Network", rows=[("Jakarta", "Up", 100), ("Surabaya", "Degraded", 62)])),
            ("Give everyone the same picture", "Managers and operators look at one shared screen instead of exchanging screenshots.",
             dict(title="Institution · Today", chip="Academic", rows=[("Attendance", "96%", 96), ("Assignments due", "14", None)])),
            ("See patterns over time", "History sits next to live status, so a recurring issue stands out before it becomes routine.",
             dict(title="Sensor · Warehouse", chip="IP Camera", rows=[("Readings stored", "30 days", None), ("Dashboards", "3", None)])),
        ],
        svc={
            "net": ("Puts every network device, website, API and server on one dashboard, with history beside it.",
                    "An engineer sees a branch link slow down and checks its status history before users notice.",
                    "Choose the devices, websites and servers to watch with Network Monitoring, Web/API Monitoring and Linux Server Monitoring.",
                    "Follow live dashboards and spot patterns in Network Status History; Real-time Notifications flag outages."),
            "acd": ("Shows the whole institution, from attendance to learning outcomes, as it happens.",
                    "A principal sees which classes have low attendance before second period.",
                    "Turn on Real-time Institution Monitoring for the classes and subjects you follow.",
                    "Management watches live indicators while Real-time Attendance and Learning Performance Tracking fill in the detail."),
            "cam": ("Stores data from connected devices and shows it on dashboards or in other apps.",
                    "A facility manager follows sensor readings from every site on one screen.",
                    "Choose which device data to store and chart with Device Data Storage & Dashboard.",
                    "Watch every site on one dashboard while Multi-site Deployment keeps locations organised."),
        },
        uses=[
            ("net", "Network engineers", "Catch a slow link before the helpdesk does", "Branch latency climbs during the morning peak. The engineer sees it on the dashboard and reroutes traffic before anyone calls."),
            ("acd", "School principals", "Start the day knowing which classes need attention", "Attendance updates as students arrive. The principal checks the institution view and follows up with two homeroom teachers."),
            ("cam", "Facility managers", "Keep every site's devices in view", "Sensors across three warehouses report into one dashboard. The manager compares readings without visiting each site."),
            ("net", "IT managers", "Answer 'is the network OK?' in one glance", "Leadership asks about an outage rumour. The IT manager opens the dashboard and shares live status for every site."),
        ],
        what="Real-time Dashboard & Monitoring is the shared capability that shows live status on one screen, with history beside it, across the services that use it.",
    ),
    "Reporting & Analytics": dict(
        h1=("Reports that build themselves,", "not spreadsheets at month end."),
        sub="Reporting & Analytics helps managers turn everyday activity into reports and trends, from customer conversations to student progress and network availability.",
        challenge=("The data is already there.", "The report still takes a week."),
        challenge_text="A customer service lead copies chat numbers into a spreadsheet. A school compiles grades by hand for the term report. An IT manager screenshots dashboards for the monthly review. The pattern is the same: the activity is recorded, but turning it into a decision takes days.",
        benefits=[
            ("Decide with current numbers", "Reports draw on data teams already enter, so they are ready when the meeting starts.",
             dict(title="Report · September", chip="Network", rows=[("Availability", "99.95%", 99), ("Incidents", "3", 10)])),
            ("See what is changing", "Trends show which questions, classes or sites are moving, not only where they stand today.",
             dict(title="Top topics · This week", chip="Omnichannel", rows=[("Delivery status", "38%", 38), ("Payment", "22%", 22)])),
            ("Share one version of the truth", "Everyone works from the same report instead of their own spreadsheet.",
             dict(title="Grade 8 · Mathematics", chip="Academic", rows=[("Class average", "78", 78), ("Below 60", "5 students", 15)])),
        ],
        svc={
            "acd": ("Turns institutional data and student activity into progress per subject.",
                    "A teacher sees which students fell behind in a subject this month.",
                    "Keep records current with Institution Data Management and switch on Learning Performance Tracking per subject.",
                    "Review progress per student and subject, with Grade Management feeding the numbers."),
            "net": ("Produces availability and incident reports for any period in one click.",
                    "An IT manager exports last month's availability report for the board meeting.",
                    "Choose a period and modules for Automated Reporting.",
                    "Download the PDF report; Network Quality Analysis is coming soon for signal benchmarks."),
            "cam": ("Analyses visitor patterns and crowding from camera footage.",
                    "A store manager compares visitor counts across weekdays to plan shifts.",
                    "Turn on People Counting & Crowd Detection on entrance cameras.",
                    "Read visitor trends per site and plan staffing around the peaks."),
            "crm": ("Finds patterns in customer conversations across channels.",
                    "A customer service lead sees which topics drive most messages this week.",
                    "Label conversations so Interaction Analytics can group them.",
                    "Review the top topics and add answers to the Knowledge Base."),
        },
        uses=[
            ("crm", "Customer service leads", "Know what customers ask most", "Messages spike after a promotion. Interaction Analytics shows most are about delivery, so the lead adds a clear answer to the knowledge base."),
            ("acd", "Teachers", "See who needs help before the exam", "Progress per subject shows five students below the class average. The teacher plans a review session for them."),
            ("net", "IT managers", "Send the monthly report in minutes", "The board wants last month's availability. The IT manager picks the period and downloads the PDF."),
            ("cam", "Store managers", "Staff up for the real peaks", "Visitor counts show Saturdays peak after 4 p.m. The manager moves two shifts later."),
        ],
        what="Reporting & Analytics is the shared capability that turns everyday activity in each service into reports and trends you can act on.",
    ),
    "Notifications & Alerts": dict(
        h1=("Know the moment it matters,", "not after someone complains."),
        sub="Notifications & Alerts helps teams and customers hear about what changed straight away, from a network outage to a school arrival or a store intruder.",
        challenge=("Something changed.", "The right person heard last."),
        challenge_text="A network link fails and IT learns about it from users. A student arrives late and the parent finds out in the evening. A door opens at night and the footage is reviewed the next morning. The pattern is the same: the event is recorded, but the people who need to act are told too late.",
        benefits=[
            ("Act within minutes", "The right people are told as soon as something happens, on the device they carry.",
             dict(title="Alert · 02:14", chip="IP Camera", rows=[("Rear door", "Motion", 100)], alert=("warn", "Intruder detected · clip saved"))),
            ("Know when it is fixed", "Recovery is announced as clearly as the problem, so no one keeps checking.",
             dict(title="Link JKT–SBY", chip="Network", rows=[("Status", "Recovered", 100)], alert=("ok", "Back online at 09:42"))),
            ("Reach many people at once", "Announcements and reminders go out to every customer or parent who needs them.",
             dict(title="Broadcast · Today", chip="Omnichannel", rows=[("Sent", "4,200", 100), ("Read", "3,150", 75)])),
        ],
        svc={
            "net": ("Sends instant alerts when a network goes down and when it recovers.",
                    "The IT team is alerted when a branch link drops, and again when it comes back.",
                    "Set who receives Real-time Notifications for each device and module.",
                    "Respond to alerts while Proactive & Predictive Maintenance warns about issues before they happen."),
            "cam": ("Alerts security teams to suspicious activity as cameras detect it.",
                    "A guard receives an alert when someone enters a restricted area after hours.",
                    "Turn on Intruder Detection for the cameras that cover restricted areas.",
                    "Open the alert and its Cloud Recording clip, and dispatch someone to check."),
            "acd": ("Makes attendance visible to parents, teachers and the institution as it happens.",
                    "A parent sees their child arrive at school before first period.",
                    "Give parents access to Real-time Attendance through their portal.",
                    "Attendance appears as students check in, alongside Real-time Institution Monitoring for management."),
            "crm": ("Sends announcements and automatic reminders to customers.",
                    "Customers receive an appointment reminder the day before, and a notice when hours change.",
                    "Create audiences and messages for Broadcast (Blast) and set up Scheduling & Reminders.",
                    "Send and track delivery; replies come back to the Omnichannel Inbox."),
        },
        uses=[
            ("net", "Network engineers", "Fix outages before tickets pile up", "A branch link drops at 9 a.m. The engineer gets the alert, reroutes traffic, and sees the recovery notice twenty minutes later."),
            ("cam", "Heads of security", "Respond to a break-in while it is happening", "A door opens in a closed warehouse at 2 a.m. The security lead receives the alert with a clip and sends the night guard."),
            ("acd", "Parents", "Know your child arrived safely", "Attendance updates as students check in. A parent sees the arrival on their phone before work."),
            ("crm", "Marketing teams", "Remind customers without calling each one", "A clinic schedules reminders for tomorrow's appointments. Customers who reply land in the shared inbox."),
        ],
        what="Notifications & Alerts is the shared capability that tells the right people as soon as something changes, in every service that uses it.",
    ),
    "AI & Automation": dict(
        h1=("AI that acts on what it sees,", "not only records it."),
        sub="AI & Automation helps teams let software detect, answer and predict, from chatbots that reply at night to cameras that spot smoke and networks that warn before they fail.",
        challenge=("The signals were there.", "No one had time to read them."),
        challenge_text="A customer asks the same question at midnight and waits until morning. A camera records smoke that no one is watching. A network link creeps toward saturation unnoticed. The pattern is the same: the warning signs exist, but people cannot watch every channel, camera and link at once.",
        benefits=[
            ("Answer and act around the clock", "Routine questions and checks are handled automatically, day and night.",
             dict(title="Chatbot · Today", chip="Omnichannel", rows=[("Messages handled", "62", 62), ("Sent to an agent", "9", 14)])),
            ("Catch what people would miss", "AI watches every camera and link at once and raises only what needs attention.",
             dict(title="Loading bay", chip="IP Camera", rows=[("Smoke", "Detected", 100)], alert=("warn", "Fire & smoke alert · 14:06"))),
            ("Fix problems before they happen", "Predictions turn a coming failure into a planned task.",
             dict(title="Link JKT–SBY", chip="Network", rows=[("Utilisation", "82%", 82)], alert=("warn", "Likely saturation in ~2 hours"))),
        ],
        svc={
            "cam": ("Detects intruders, fire and smoke, crowds and staff presence from camera footage.",
                    "A store gets a smoke alert from its loading-bay camera before the alarm goes off.",
                    "Turn on Intruder Detection, Fire & Smoke Detection, People Counting & Crowd Detection or Employee Presence per camera.",
                    "Alerts arrive with the clip from Cloud Recording, for every site."),
            "net": ("Predicts network issues and raises proactive alerts on every module.",
                    "An engineer is warned that a link will saturate in two hours and reroutes traffic.",
                    "Switch on Proactive & Predictive Maintenance for the networks you monitor.",
                    "Act on predictions before users notice, and confirm with Real-time Notifications."),
            "crm": ("Runs 24/7 chatbots for frequent customer questions.",
                    "A customer asks about delivery at midnight and gets an answer straight away.",
                    "Design chatbot flows in Chatbot Builder using your Knowledge Base.",
                    "The chatbot replies and hands complex cases to agents in the Omnichannel Inbox."),
        },
        uses=[
            ("cam", "Facility managers", "Hear about smoke before the alarm", "A loading-bay camera detects smoke on a Sunday. The manager is alerted and calls the site team within minutes."),
            ("net", "Network engineers", "Plan around failures instead of reacting", "Predictive maintenance flags a link heading for saturation. The engineer reroutes traffic before the afternoon peak."),
            ("crm", "Customer service managers", "Cover nights and weekends", "The chatbot answers delivery questions overnight. Agents start the day with only the cases that need a person."),
            ("cam", "HR teams", "Record presence without a queue", "Employee Presence logs staff as they arrive at each site. HR reviews attendance without collecting paper sheets."),
        ],
        what="AI & Automation is the shared capability that lets software detect, answer and predict on your behalf in the services that use it.",
        security=[("AI runs inside your tenant", "Detections and chatbot conversations stay in your company's own tenant."),
                  ("People stay in control", "Alerts go to people to act on, and chatbots hand complex cases to agents."),
                  ("Protected under UU PDP", "Personal data is handled under Indonesia's Personal Data Protection Law (No. 27/2022).")],
    ),
    "Cloud Storage": dict(
        h1=("Files you can reach from anywhere,", "not boxes in a back office."),
        sub="Cloud Storage helps teams keep important footage and content safe and reachable, from camera recordings in IP Camera Management to learning content in Academic Management.",
        challenge=("It was recorded.", "It is just not where you are."),
        challenge_text="Camera footage sits on a recorder in a store's back room. Learning materials live on one teacher's laptop. When someone needs them from somewhere else, they wait or do without. The pattern is the same: the content exists, but it is stuck in one place.",
        benefits=[
            ("Open what you need from any device", "Content lives in the cloud, so a phone or laptop is enough to reach it.",
             dict(title="Recordings · Store 12", chip="IP Camera", rows=[("Entrance · 14:02", "02:31", None), ("Cashier · 13:47", "01:10", None)])),
            ("Stop losing files to broken hardware", "Automatic backup means a failed device does not take the content with it.",
             dict(title="Backup", chip="IP Camera", rows=[("Last backup", "2 min ago", None)], alert=("ok", "Backed up automatically"))),
            ("Share without copying", "Students and colleagues open the same material instead of passing files around.",
             dict(title="Learning content · Grade 8", chip="Academic", rows=[("Fractions · Video", "Shared", None), ("Quiz practice", "Shared", None)])),
        ],
        svc={
            "cam": ("Stores footage securely in the cloud with automatic backup, shareable from any device.",
                    "A manager opens yesterday's entrance clip on a phone and shares it with security.",
                    "Turn on Cloud Recording for the cameras you want to keep footage from.",
                    "Find, play and share clips from any device; detections link straight to the recording."),
            "acd": ("Hosts interactive learning materials that students open from school or home.",
                    "A student reviews a lesson video at home the night before a quiz.",
                    "Upload materials to Learning Content and attach them to subjects.",
                    "Students open materials on the web or Mobile Apps, and teachers follow up with assignments."),
        },
        uses=[
            ("cam", "Business owners", "Check an incident from wherever you are", "A customer complaint comes in while the owner is travelling. They open the clip on their phone and share it with the store manager."),
            ("cam", "Heads of security", "Keep evidence safe", "A camera recorder at one site fails. The footage is already in the cloud, so nothing is lost."),
            ("acd", "Teachers", "Prepare lessons once and reuse them", "A teacher uploads a lesson set for Grade 8. Every class uses the same materials, updated in one place."),
            ("acd", "Students", "Study from home with the same materials", "A student reopens the lesson video before a quiz. No files need to be copied or sent."),
        ],
        what="Cloud Storage is the shared capability that keeps footage and content in the cloud, safe and reachable from any device.",
        security=[("Access per role", "Only the people you choose can open recordings or materials."),
                  ("Encrypted device data", "IP Camera Management encrypts device data through Security & Access Management."),
                  ("Automatic backup", "Cloud Recording backs footage up automatically.")],
    ),
    "User & Access Management": dict(
        h1=("The right access for every role,", "not one login for everyone."),
        sub="User & Access Management helps organisations decide who sees what, from portals for each school role to encrypted, controlled access for cameras and devices.",
        challenge=("Everyone can see everything.", "Or no one can see enough."),
        challenge_text="A school shares one admin login between staff. A security team gives every guard access to every camera. When someone leaves, no one is sure what they could still open. The pattern is the same: access is either too wide or too narrow, and never quite right.",
        benefits=[
            ("Give each role its own view", "People see the data that fits their job, and nothing else.",
             dict(title="Portals", chip="Academic", rows=[("Teachers", "Class view", None), ("Parents", "Child view", None)])),
            ("Protect sensitive data by default", "Data is encrypted and access is checked every time someone opens it.",
             dict(title="Access · Warehouse cameras", chip="IP Camera", rows=[("Security team", "Allowed", 100), ("Store staff", "Denied", 0)])),
            ("Change access in one place", "Adding or removing someone is one change, not a list of passwords to reset.",
             dict(title="Users", chip="Access", rows=[("New teacher", "Added", None), ("Former guard", "Removed", None)])),
        ],
        svc={
            "acd": ("Gives management, teachers, students, parents, admins and education offices their own portal.",
                    "A parent sees only their child's attendance and grades.",
                    "Assign each person a role in Role-based Portals.",
                    "Every role sees its own view of the same data, from Real-time Attendance to Grade Management."),
            "cam": ("Encrypts device data and controls who can access each device.",
                    "Store staff can view the shop floor but not the warehouse cameras.",
                    "Set permissions per user and site in Security & Access Management.",
                    "Teams see only the cameras they look after, across Multi-site Deployment."),
        },
        uses=[
            ("acd", "School admins", "Stop sharing one admin password", "Each staff member gets their own role. When a teacher leaves, the admin removes one account."),
            ("acd", "Education offices", "See every school without seeing every student", "A district office uses its own portal to compare institutions, without opening individual student records."),
            ("cam", "Heads of security", "Give each guard the cameras they need", "Night guards see the warehouse cameras; store staff see the shop floor. Access follows the role."),
            ("cam", "Business owners", "Keep device data private", "Device data is encrypted and access is controlled, so footage is only opened by the people allowed to."),
        ],
        what="User & Access Management is the shared capability that decides who can see and do what in each service.",
        security=[("Single sign-on", "One account per person across the platform, with roles that decide who sees what."),
                  ("Encrypted devices and data", "IP Camera Management encrypts device data and controls access to it."),
                  ("Isolated tenants", "Each partner's users and data stay in their own tenant."),
                  ("Protected under UU PDP", "Personal data is handled under Indonesia's Personal Data Protection Law (No. 27/2022).")],
    ),
    "API Integration": dict(
        h1=("Connect what you already use,", "not another system to retype into."),
        sub="API Integration helps teams link the platform to the channels and devices they rely on, from the official WhatsApp API to IoT networks and smart devices.",
        challenge=("The tools work.", "They just do not talk to each other."),
        challenge_text="Customers write on WhatsApp but agents answer from a separate system. Sensors and smart lamps each need their own app. The pattern is the same: every tool does its job, but people become the link between them.",
        benefits=[
            ("Meet customers on their channel", "Conversations start where customers already are, and land in your workflow.",
             dict(title="WhatsApp · Official API", chip="Omnichannel", rows=[("Messages today", "1,240", 80), ("Answered", "1,198", 96)])),
            ("Run devices from one app", "Cameras, lamps, plugs and door sensors are controlled together.",
             dict(title="Store 12 · Devices", chip="IP Camera", rows=[("Smart lamps", "On", None), ("Door sensor", "Closed", None)])),
            ("Connect sites without new cabling", "Wireless IoT networks bring remote locations online.",
             dict(title="Connectivity", chip="IP Camera", rows=[("LoRaWAN", "12 devices", None), ("NB-IoT", "8 devices", None)])),
        ],
        svc={
            "crm": ("Connects to WhatsApp through the official API for personal, two-way conversations.",
                    "A customer replies to an order update on WhatsApp and an agent answers from the shared inbox.",
                    "Connect your WhatsApp Business account through WhatsApp API.",
                    "Conversations flow into the Omnichannel Inbox, where Chatbot Builder can answer the routine ones."),
            "cam": ("Links cameras and smart devices, over LoRaWAN, NB-IoT or GPRS.",
                    "A store turns its lights off and checks the door sensor from the same app as its cameras.",
                    "Pair devices with Smart Device Integration and pick a network with IoT Connectivity.",
                    "Control devices and store their data with Device Data Storage & Dashboard."),
        },
        uses=[
            ("crm", "Customer service agents", "Answer WhatsApp without switching apps", "A customer replies to an order notice on WhatsApp. The agent sees it in the shared inbox with the order history."),
            ("crm", "Marketing teams", "Send updates customers actually read", "Marketing sends a personal WhatsApp update to opted-in customers. Replies come back to the team."),
            ("cam", "Facility managers", "Run lights and sensors with your cameras", "At closing, the manager switches off smart lamps and checks door sensors in the camera app."),
            ("cam", "Operations teams", "Bring remote sites online", "A warehouse without fixed internet connects its sensors over NB-IoT and reports into the same dashboard."),
        ],
        integrations=[("Official WhatsApp API", "Reach customers on the app they already use, with conversations kept in one inbox."),
                      ("LoRaWAN, NB-IoT and GPRS", "Connect devices at sites where fixed internet is hard to reach."),
                      ("Smart lamps, plugs and door sensors", "Control the building and the cameras from one app.")],
        what="API Integration is the shared capability that connects each service to the channels, networks and devices you already use.",
        security=[("Official channels", "WhatsApp conversations run on the official WhatsApp API."),
                  ("Encrypted device data", "Data from connected devices is encrypted and access-controlled."),
                  ("Isolated tenants", "Data from your integrations stays in your company's own tenant.")],
    ),
    "Communication & Chatbot": dict(
        h1=("Every conversation in one place,", "not scattered across apps."),
        sub="Communication & Chatbot helps teams hold every customer conversation in one place, labelled, answered and tracked, today in Omnichannel Management.",
        challenge=("Customers moved to chat.", "Teams still switch between apps."),
        challenge_text="A customer writes on WhatsApp, calls the next day, then chats on the website. Each message lands somewhere else, so agents ask the same questions again and complaints slip through. The problem is not the number of channels; it is that the conversation is split across them.",
        benefits=[
            ("Keep the whole thread together", "Every message, call and chat with a customer sits in one history.",
             dict(title="Budi S. · 3 channels", chip="Omnichannel", rows=[("WhatsApp · Mon", "Order", None), ("Voice · Tue", "Delivery", None), ("Chat · Today", "Address", None)])),
            ("Answer consistently", "A shared answer library keeps every agent's reply the same.",
             dict(title="Knowledge base", chip="Omnichannel", rows=[("Delivery times", "Used 84×", None), ("Returns", "Used 41×", None)])),
            ("Never lose a complaint", "Requests become tracked tickets until they are resolved.",
             dict(title="Ticket #2041 · Refund", chip="Resolved", rows=[("Opened", "Mon 09:12", None), ("Resolved", "Tue 15:40", None)])),
        ],
        svc={
            "crm": ("Brings chat, voice and video into one inbox, with labels, a knowledge base and ticketing.",
                    "An agent sees a customer's WhatsApp, call and chat history before replying.",
                    "Set up the Omnichannel Inbox, Conversation Labeling and a Knowledge Base.",
                    "Agents reply from one place and turn complaints into Ticketing cases; Interaction Analytics shows the trends."),
        },
        uses=[
            ("crm", "Customer service agents", "Reply with the full history in front of you", "A customer follows up on yesterday's call by chat. The agent sees the call notes and answers without asking again."),
            ("crm", "Customer service managers", "Know where every complaint stands", "Each morning the manager reviews open tickets by label and assigns the oldest first."),
            ("crm", "Business owners", "Serve every channel without extra hires", "One small team answers WhatsApp, web chat and calls from the same inbox."),
            ("crm", "Public service offices", "Give citizens consistent answers", "Staff use the shared knowledge base, so every citizen gets the same answer about opening hours and documents."),
        ],
        integrations=[("WhatsApp API", "Bring WhatsApp conversations into the same inbox as every other channel."),
                      ("Chatbot Builder", "Let a chatbot answer frequent questions and hand the rest to agents.")],
        what="Communication & Chatbot is the shared capability that keeps every customer conversation in one place, labelled, answered and tracked.",
    ),
    "Mobile App": dict(
        h1=("The service in your pocket,", "not only on a school computer."),
        sub="Mobile App helps students and teachers use Academic Management on their phones, with separate apps for students on iOS and Android and for teachers.",
        challenge=("Learning happens everywhere.", "The system stayed on a desk."),
        challenge_text="A student wants to check tomorrow's assignment on the bus. A teacher wants to see who submitted while away from school. When the system only works on a school computer, both wait. The problem is not access to data; it is access from where people actually are.",
        benefits=[
            ("Check in from anywhere", "Assignments, grades and attendance are a tap away.",
             dict(title="Today", chip="Academic", rows=[("Fractions quiz", "Due 10:00", None), ("Grade · Science", "84", 84)])),
            ("Get the right app for your role", "Students and teachers each get an app designed for what they do.",
             dict(title="Apps", chip="Academic", rows=[("Student app", "iOS · Android", None), ("Teacher app", "Available", None)])),
            ("Stay in sync with school", "What happens in the app updates the same records the school sees.",
             dict(title="Sync", chip="Academic", rows=[("Submitted", "28 / 32", 88)], alert=("ok", "Teacher notified"))),
        ],
        svc={
            "acd": ("Provides separate apps for students (iOS and Android) and for teachers.",
                    "A student submits an assignment from their phone and the teacher sees it straight away.",
                    "Invite students and teachers to the Mobile Apps from their portals.",
                    "Students follow Assignment Management and grades; teachers check Real-time Attendance on the go."),
        },
        uses=[
            ("acd", "Students", "Submit on time, wherever you are", "A student finishes an assignment on the way home and submits it from the app before the deadline."),
            ("acd", "Teachers", "Check the class without a laptop", "Between lessons, a teacher sees who has submitted and who is absent today."),
            ("acd", "Parents", "Follow progress on your phone", "A parent checks the week's attendance and new grades from the same phone they use every day."),
            ("acd", "Institution management", "Reach every student, not only those with a computer", "Students without a laptop at home still receive assignments and materials on their phones."),
        ],
        what="Mobile App is the shared capability that brings each service to iOS and Android, today with separate student and teacher apps in Academic Management.",
    ),
}


def children(cap):
    """{service: [validated child capabilities]} in VALIDATED order, skipping gaps and estimates."""
    out = {}
    for k in VALIDATED:
        kids = [c for c in PARENTS[cap].get(k, []) if c not in HIDDEN]
        if kids:
            out[k] = kids
    # most children first, as a stand-in for "most partner stories" until stories are tagged
    return dict(sorted(out.items(), key=lambda kv: -len(kv[1])))


def page(slug, cap, desc):
    c = CONTENT[cap]
    kids = children(cap)
    svcs = list(kids)
    nav_html, drawer_html = site_nav.nav(slug)

    badges = "".join(f'<a class="avail" href="{site_nav.SERVICE_HREF[k]}"><span class="code">{CODE[k]}</span>{e(BY_KEY[k]["name"])}</a>' for k in svcs)
    nums = [f'<div><b>{len(svcs)}</b><span>service{"s" if len(svcs) > 1 else ""} use it today</span></div>']
    for k in svcs:
        if k in USAGE:
            nums.append(f'<div><b>{e(USAGE[k][0])}</b><span>{e(USAGE[k][1])}</span></div>')
            break

    hero_mock = c["benefits"][0][2]
    benefits = "\n".join(f'''        <li class="benefit rv" style="--d:{i}">
          <div class="benefit-visual">{mock(m, t + " preview")}</div>
          <h3>{e(t)}</h3>
          <p>{e(d)}</p>
        </li>''' for i, (t, d, m) in enumerate(c["benefits"]))

    def kid(k, name):
        soon = ' <span class="status soon">Coming soon</span>' if name in SOON else ''
        return f'<li><b>{e(name)}</b>{soon}</li>'

    avail = "\n".join(f'''        <li class="av-card rv" style="--d:{i}">
          <div class="av-head"><img src="assets/capabilities/{BY_KEY[k]["icon"]}" alt=""><div><span class="code">{CODE[k]}</span><h3>{e(BY_KEY[k]["name"])}</h3></div></div>
          <p class="av-role">{e(c["svc"][k][0])}</p>
          <small>Capabilities</small>
          <ul class="av-kids">{"".join(kid(k, n) for n in kids[k])}</ul>
          <p class="av-moment"><em>Example</em>{e(c["svc"][k][1])}</p>
          <a class="link-arrow" href="{site_nav.SERVICE_HREF[k]}">See {e(BY_KEY[k]["name"])} {ARR}</a>
        </li>''' for i, k in enumerate(svcs))

    tabs = "\n".join(f'          <button class="tab" role="tab" id="t-{k}" aria-controls="p-{k}" aria-selected="{"true" if i == 0 else "false"}"{"" if i == 0 else TI}>{e(BY_KEY[k]["name"])}</button>'
                     for i, k in enumerate(svcs))
    panels = []
    for i, k in enumerate(svcs):
        _, _, conf, act = c["svc"][k]
        steps = [SETUP[k], ("Set it up", conf), ("Put it to work", act)]
        li = "".join(f'<li class="step"><h3>{e(t)}</h3><p>{e(d)}</p></li>' for t, d in steps)
        panels.append(f'''        <div class="how-panel" role="tabpanel" id="p-{k}" aria-labelledby="t-{k}"{"" if i == 0 else " hidden"}>
          <ol class="steps">{li}</ol>
        </div>''')
    tabs_html = f'''      <div class="tabs rv" role="tablist" aria-label="How it works in each service">
{tabs}
      </div>''' if len(svcs) > 1 else ''

    uses = "\n".join(f'''        <li class="role rv" style="--d:{i % 3}">
          <span class="code">{CODE[k]} · {e(SHORT[k])}</span>
          <small>{e(r)}</small>
          <h3>{e(h)}</h3>
          <p>{e(sc)}</p>
          <a class="link-arrow" href="index.html#open">Schedule a demo {ARR}</a>
        </li>''' for i, (k, r, h, sc) in enumerate(c["uses"]))

    integ = ''
    if c.get("integrations"):
        items = "".join(f'<li><b>{e(t)}</b><p>{e(d)}</p></li>' for t, d in c["integrations"])
        integ = f'''
  <!-- ================= Integrations ================= -->
  <section class="sec" id="integrations" aria-labelledby="int-title">
    <div class="inner">
      <p class="eyebrow rv"><i class="dm"></i>Integrations</p>
      <h2 id="int-title" class="rv" style="--d:1">What it connects to, <b>and why it helps.</b></h2>
      <ul class="integrations rv" style="--d:2">{items}</ul>
    </div>
  </section>
'''

    # partner proof: the retail story is tagged People Counting & Crowd Detection (CAM)
    story = ''
    if "cam" in kids and "People Counting & Crowd Detection" in kids["cam"]:
        story = f'''      <div class="svc-story rv">
        <a class="story" href="story-national-retail-chain.html">
          <div class="story-img leaf"><img class="mirror" src="assets/landing/story-retail-v2.png" alt="Professional woman under a clear sky among city buildings" loading="lazy" style="object-position:66% 50%"></div>
          <div class="story-body">
            <div class="story-meta"><span class="chip">CAM · IP Camera Management</span><span class="tag">People Counting &amp; Crowd Detection</span></div>
            <h3>Retail supply chains, seen by computer vision</h3>
            <p>How a retailer uses IP Camera Management to track shelf availability in its stores, live, instead of waiting for manual stock checks.</p>
            <span class="link-arrow">Read the story {ARR}</span>
          </div>
        </a>
      </div>'''
    usage = [k for k in svcs if k in USAGE]
    usage_html = ''
    if usage:
        tiles = "".join(f'<li><span class="code">{CODE[k]} · {e(SHORT[k])}</span><b>{e(USAGE[k][0])}</b><p>{e(USAGE[k][1])}</p></li>' for k in usage)
        src = ", ".join(USAGE[k][2] for k in usage)
        usage_html = f'''      <!-- Fallback (no stories tagged with this capability yet): usage figures per service. TODO: verify and date -->
      <ul class="usage-tiles rv">{tiles}</ul>
      <p class="ph-source rv">Figures as reported on each service website ({e(src)}).</p>'''
    if not story and not usage:
        usage_html = '      <!-- TODO: no partner story or usage figure for this capability yet — evidence priority -->\n      <p class="lede rv">Partner stories for this capability are coming soon.</p>'

    sec_html = ''
    if c.get("security"):
        icons = ["icon-user-key.svg", "icon-cloud.svg", "icon-layout-dashboard.svg", "../form/ic-shield.svg"]
        pts = "\n".join(f'        <li class="rv" style="--d:{i}"><span class="pi"><img src="assets/landing/{icons[i % 4]}" width="22" height="22" alt=""></span><div><h3>{e(t)}</h3><p>{e(d)}</p></div></li>' for i, (t, d) in enumerate(c["security"]))
        sec_html = f'''
  <!-- ================= Security & control (required for this capability) ================= -->
  <section class="sec" id="security" aria-labelledby="sec-title">
    <div class="inner trust">
      <div>
        <p class="eyebrow rv"><i class="dm"></i>Security &amp; control</p>
        <h2 id="sec-title" class="rv" style="--d:1">Built in, <b>not bolted on.</b></h2>
        <p class="lede rv" style="--d:2">What your IT and legal teams will want to know about {e(cap)}.</p>
      </div>
      <ul class="eco-points trust-points">
{pts}
      </ul>
    </div>
  </section>
'''

    names = [BY_KEY[k]["name"] for k in svcs]
    listed = names[0] if len(names) == 1 else ", ".join(names[:-1]) + " and " + names[-1]
    per = " ".join(f'In {BY_KEY[k]["name"]}, it covers {", ".join(kids[k])}.' for k in svcs)
    faqs = [
        (f"What is {cap}?", c["what"]),
        (f"Which services include {cap}?", f"Today it is available in {listed}. {per}"),
        ("Do I need a particular service to use it?", f"Yes. {cap} comes with the services that include it, so you use it through {listed}. Ask us which package fits your needs."),
        (f"How does {cap} differ between services?", " ".join(f'In {BY_KEY[k]["name"]}, it {c["svc"][k][0][0].lower()}{c["svc"][k][0][1:]}' for k in svcs)),
        ("How is our data kept secure?", f"{cap} runs inside each service's tenant, with single sign-on and role-based access. Personal data is handled under Indonesia's Personal Data Protection Law (UU PDP No. 27/2022)."),
        ("How do packages and pricing work?", "Pricing follows the service and package you choose. Contact us and we will propose a package for your team."),
    ]
    faq_html = "\n".join(f'        <details{" open" if i == 0 else ""}>\n          <summary>{e(q)}</summary>\n          <p>{e(a)}</p>\n        </details>' for i, (q, a) in enumerate(faqs))
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "index.html"},
            {"@type": "ListItem", "position": 2, "name": "Capabilities"},
            {"@type": "ListItem", "position": 3, "name": cap}]}]}
    ctx = ", ".join(SHORT[k] for k in svcs)
    picker = "\n".join(f'          <li><a class="rel" href="{site_nav.SERVICE_HREF[k]}"><img src="assets/capabilities/{BY_KEY[k]["icon"]}" alt=""><h3>{e(BY_KEY[k]["name"])}</h3><p>{e(", ".join(kids[k]))}</p><span class="link-arrow">See the service {ARR}</span></a></li>' for k in svcs)

    single = '' if len(svcs) > 1 else f'''
<!-- Only one validated service uses {e(cap)} today (others are estimates or taxonomy gaps).
     The page stays Tier A so it is ready when more services are validated. -->'''

    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(cap)} for {e(ctx)} | Telkom Digital</title>
<meta name="description" content="{e(c["sub"])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,200..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<link rel="stylesheet" href="css/service.css">
<link rel="stylesheet" href="css/capability.css">
<script type="application/ld+json">
{json.dumps(ld, indent=2, ensure_ascii=False)}
</script>
</head>
<body>
<!-- Generated by tools/build_capabilities.py — edit the data there and re-run instead of editing this file -->{single}
<!--
  Page data (Kerangka Halaman Kapabilitas, Tier A)
  - Shared capability: {e(cap)}
  - Services shown (validated children only): {", ".join(CODE[k] for k in svcs)}
  - TODO before publishing: verify figures and tag partner stories with this capability
-->

<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
  <symbol id="arr" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></symbol>
</svg>

<section class="hero phero" id="hero">
{nav_html}

  <div class="inner ph-grid">
    <header class="ph-copy">
      <p class="eyebrow in" style="--i:1"><i class="dm"></i>Capability</p>
      <h1 class="ph-title in" style="--i:2">{e(c["h1"][0])} <b>{e(c["h1"][1])}</b></h1>
      <p class="lede in" style="--i:3">{e(c["sub"])}</p>
      <div class="avail-row in" style="--i:4"><small>Available in</small>{badges}</div>
      <div class="hero-nums in" style="--i:4">{"".join(nums)}</div>
      <div class="hero-cta in" style="--i:5">
        <a class="pricing" href="#find">Find the right service</a>
        <a class="link-arrow" href="index.html#open">Schedule a demo {ARR}</a>
      </div>
    </header>
    <div class="svc-visual in" style="--i:3">
      <figure class="ph-photo leaf blank" aria-hidden="true"></figure>
      {mock(hero_mock, cap + " preview")}
    </div>
  </div>
</section>

{drawer_html}

<main>
  <!-- ================= Challenge ================= -->
  <section class="sec mist" id="challenge" aria-labelledby="ch-title">
    <div class="inner problem">
      <header>
        <p class="eyebrow rv"><i class="dm"></i>The challenge</p>
        <h2 id="ch-title" class="rv" style="--d:1">{e(c["challenge"][0])} <b>{e(c["challenge"][1])}</b></h2>
      </header>
      <div class="problem-copy rv" style="--d:2"><p>{e(c["challenge_text"])}</p></div>
    </div>
  </section>

  <!-- ================= Benefits (no feature names) ================= -->
  <section class="sec" id="benefits" aria-labelledby="ben-title">
    <div class="inner">
      <p class="eyebrow rv"><i class="dm"></i>What changes</p>
      <h2 id="ben-title" class="rv" style="--d:1">What your teams <b>get from it.</b></h2>
      <ul class="benefits">
{benefits}
      </ul>
    </div>
  </section>

  <!-- ================= Available in services (core section) ================= -->
  <section class="sec mist" id="find" aria-labelledby="av-title">
    <div class="inner">
      <div class="sec-head">
        <div>
          <p class="eyebrow rv"><i class="dm"></i>Available in</p>
          <h2 id="av-title" class="rv" style="--d:1">One capability, <b>{"in " + str(len(svcs)) + " services." if len(svcs) > 1 else "inside " + e(names[0]) + "."}</b></h2>
        </div>
        <p class="lede rv" style="--d:2">{"Each service uses " + e(cap) + " in its own way. Pick the one that matches your work." if len(svcs) > 1 else "Today " + e(cap) + " is part of " + e(names[0]) + "; more services will follow as they are validated."}</p>
      </div>
      <ul class="av-grid av-{len(svcs)}">
{avail}
      </ul>
    </div>
  </section>

  <!-- ================= How it works per service ================= -->
  <section class="sec" id="how" aria-labelledby="how-title">
    <div class="inner">
      <p class="eyebrow rv"><i class="dm"></i>How it works</p>
      <h2 id="how-title" class="rv" style="--d:1">Three steps <b>{"in each service." if len(svcs) > 1 else "to get started."}</b></h2>
{tabs_html}
      <div class="how-panels rv" style="--d:2">
{chr(10).join(panels)}
      </div>
    </div>
  </section>

  <!-- ================= Use cases ================= -->
  <section class="sec mist" id="uses" aria-labelledby="uses-title">
    <div class="inner">
      <p class="eyebrow rv"><i class="dm"></i>Use cases</p>
      <h2 id="uses-title" class="rv" style="--d:1">Where it makes <b>a difference.</b></h2>
      <ul class="roles uses">
{uses}
      </ul>
    </div>
  </section>
{integ}
  <!-- ================= Partner proof ================= -->
  <section class="sec{" mist" if integ else ""}" id="proof" aria-labelledby="proof-title">
    <div class="inner">
      <div class="sec-head">
        <div>
          <p class="eyebrow rv"><i class="dm"></i>Partner proof</p>
          <h2 id="proof-title" class="rv" style="--d:1">Already at work <b>with our partners.</b></h2>
        </div>
        <a class="link-arrow rv" style="--d:2" href="customer-stories.html?capability={quote(cap)}">All partner stories {ARR}</a>
      </div>
{story}
{usage_html}
    </div>
  </section>
{sec_html}
  <!-- ================= FAQ ================= -->
  <section class="sec mist" id="faq" aria-labelledby="faq-title">
    <div class="inner faq-wrap">
      <div>
        <p class="eyebrow rv"><i class="dm"></i>FAQ</p>
        <h2 id="faq-title" class="rv" style="--d:1">Questions about <b>{e(cap)}.</b></h2>
      </div>
      <div class="faq rv" style="--d:2">
{faq_html}
      </div>
    </div>
  </section>

  <!-- ================= Service picker + CTA ================= -->
  <section class="sec" id="pick" aria-labelledby="pick-title">
    <div class="inner">
      <p class="eyebrow rv"><i class="dm"></i>Find the right service</p>
      <h2 id="pick-title" class="rv" style="--d:1">Start with the service <b>that fits your work.</b></h2>
      <ul class="rel-list picker picker-{len(svcs)}">
{picker}
      </ul>
    </div>
  </section>

  <section class="sec cta" id="open" aria-labelledby="cta-title">
    <div class="inner cta-grid">
      <div class="bigdoor" aria-hidden="true">
        <span class="floor"></span><span class="frame"></span><span class="light"></span><span class="panel-d"></span>
      </div>
      <div>
        <p class="eyebrow rv"><i class="dm"></i>Get started</p>
        <h2 id="cta-title" class="rv" style="--d:1">See it <b>with your own data.</b></h2>
        <p class="lede rv" style="--d:2">Book a demo and we will show you {e(cap)} in the service that fits your team.</p>
        <div class="cta-actions rv" style="--d:3">
          <a class="pricing" href="index.html#open">Schedule a demo</a>
          <a class="link-arrow on-dark" href="#find">Find the right service {ARR}</a>
        </div>
      </div>
    </div>
  </section>
</main>

{FOOTER}

<script src="js/site.js"></script>
<script src="js/services-menu.js"></script>
<script src="js/capability.js"></script>
</body>
</html>
'''


def main():
    for slug, cap, desc, _ in site_nav.CAPS_MENU:
        out = ROOT / f"capability-{slug}.html"
        out.write_text(site_nav.with_icons(page(slug, cap, desc)), encoding="utf-8")
        print("wrote", out.name)


if __name__ == "__main__":
    main()
