"""Long-form content for each single story page (docs/kerangka-success-story.md).

Keyed by the story slug in build_stories.STORIES. Inline markup in paragraphs:
  [[Capability name]]  -> link to its shared capability page (exact taxonomy name)
  {{svc:cam}}          -> link to the service page
  **bold**             -> bold (used for the customer's goal)

PLACEHOLDER: all content below is illustrative, written for layout review. Replace it with the
real interview (see Lampiran A in the kerangka) and get approval before publishing.
"""

CONTENT = {
    # ==========================================================================================
    "national-retail-chain": dict(
        location="Java and Sumatra", since="2025", size_detail="120 stores, 3,000+ store staff",
        capabilities_supporting=["Intruder Detection", "Real-time Notifications"],
        hero_image="assets/services/ip-camera.jpg", hero_alt="Supermarket aisle with an automated inventory monitoring display",
        sub="A national retail chain with 120 stores now restocks shelves during the day instead of at closing, using IP Camera Management to count visitors and flag gaps across every branch.",
        context=[
            "The chain runs 120 supermarkets and convenience stores across Java and Sumatra, serving neighbourhoods where it is often the closest place to buy daily groceries. Fresh produce and fast-moving goods make up most of its sales, so a shelf that stays empty for an afternoon is a sale that goes to the shop next door.",
            "Regional operations managers look after 15 to 20 stores each. Their job is to keep shelves full and queues short, with store teams that change shifts twice a day and a head office that wants the same standard in every branch.",
        ],
        bridge="The network kept growing. But keeping every shelf and every queue in view got harder with each new store.",
        challenge=[
            "Before the change, shelf checks happened on foot. Staff walked the aisles three times a day with a paper checklist, and most gaps were spotted at the evening count, when it was too late to restock from the back room. CCTV recorded every aisle, but the footage sat on a recorder in each store and was only opened after an incident.",
            "The problem was not a lack of cameras. It was that no one could watch 120 stores at once, so the data the cameras captured never reached the people who could act on it. Out-of-stock items and long queues showed up in the sales report a week later.",
        ],
        challenge_quote=("By the time we saw the empty shelf in the report, the customer had already gone somewhere else.", "Regional Operations Manager"),
        goal="Know about empty shelves and crowded tills while there is still time to fix them, in every store.",
        solution=[
            "The chain chose {{svc:cam}} because it worked with the IP cameras most stores already had and kept footage in the cloud instead of on local recorders. A pilot in 10 stores ran for six weeks before the rollout to the rest of the network.",
            "The biggest change came from [[People Counting & Crowd Detection]]. Entrance and aisle cameras now count visitors and flag when an area gets crowded, so a store manager opens another till before the queue grows, and plans shifts around the real peaks instead of guesses.",
            "[[Multi-site Deployment]] put all 120 stores in one view. Regional managers compare branches side by side and see which stores fall behind during the day, not at the end of the month.",
            "When something looks wrong, [[Cloud Recording]] means the clip is already there. A manager opens it on a phone and shares it with the store team, without driving to the branch to pull footage off a recorder.",
        ],
        solution_quote=("We used to find empty shelves at the end of the day. Now the store team gets an alert while there is still time to restock.", "Regional Operations Manager"),
        solution_quote2=("I check the crowd level on my phone before lunch and move one person to the tills. It takes a minute.", "Store Manager"),
        connected="The stores' connections are watched by {{svc:net}} as a supporting service: when a branch link drops, [[Real-time Notifications]] reach IT before cameras go offline, so recordings and counts are not lost.",
        screenshot=dict(mock=dict(title="Store 12 · Entrance", chip="Today", rows=[("Visitors", "1,284", 64), ("Crowd level", "High", 86)], alert=("warn", "Open another till · queue building")),
                        caption="People Counting & Crowd Detection on a store entrance: the store manager sees the crowd level rise and opens another till."),
        results_table=[("Out-of-stock time per store", "Baseline", "30% less"), ("Stores watched from one app", "0", "120"), ("Shelf and crowd monitoring", "3 walk-throughs a day", "24/7")],
        results=[
            "The result was not only fewer empty shelves. Store meetings changed: instead of reviewing last week's sales, teams start the day with yesterday's visitor peaks and plan who restocks when.",
            "Head office now compares stores on the same live numbers, and new branches are added to the same view on their first day.",
        ],
        decision_quote=("We stopped managing stores from last week's report. Every regional manager now sees the same picture, at the same time.", "Director of Retail Operations"),
        next="Next, the chain plans to bring smart lamps and door sensors into the same app with Smart Device Integration, and to extend Intruder Detection to its distribution centres. The goal is one view of every site it runs, which is what IP Camera Management is built for: cameras that alert you while it happens, not after.",
        faq=[
            ("How does IP Camera Management help retail stores?", "It turns existing IP cameras into live signals: People Counting & Crowd Detection shows visitor peaks and crowding, and Cloud Recording keeps footage reachable from any device. In this story, the chain cut out-of-stock time by 30%."),
            ("Can it run across many stores?", "Yes. Multi-site Deployment puts every location in one view. This chain manages 120 stores from one app."),
            ("Do we need new cameras?", "Not always. The chain used the IP cameras most stores already had. Our team checks compatibility during a site survey."),
            ("How long does a rollout take?", "It depends on the number of sites. This chain ran a six-week pilot in 10 stores before rolling out to the rest."),
        ],
    ),
    # ==========================================================================================
    "school-foundation": dict(
        location="West Java", since="2024", size_detail="12 campuses, 9,000 students, 600 teachers",
        capabilities_supporting=["Grade Management", "Learning Performance Tracking", "Mobile Apps"],
        hero_image=None,
        sub="A private school foundation with 12 campuses now gives parents live attendance and teachers online assessments, with one view of every school on Academic Management.",
        context=[
            "The foundation runs 12 campuses in West Java, from primary to senior high school, with around 9,000 students and 600 teachers. Parents choose its schools for close follow-up on every child, so they expect to know how their children are doing without waiting for the end of term.",
            "The Head of Academic Affairs is responsible for academic standards across all campuses: attendance, assessments and term reports, with a small central team and a principal at each school.",
        ],
        bridge="The foundation kept adding campuses. But each new school brought its own registers, spreadsheets and chat groups.",
        challenge=[
            "Before the change, every campus kept attendance on paper and grades in its own spreadsheets. At the end of each term, teachers retyped grades into report templates, and the central team spent weeks collecting files from 12 schools to compare results.",
            "The problem was not effort; teachers worked hard. It was that attendance, assessments and grades lived in different places, so no one could see a student falling behind until the term report.",
        ],
        challenge_quote=("Every term we spent two weeks copying grades from one file to another. It was time we should have spent with students.", "Head of Academic Affairs"),
        goal="Give every campus the same platform, so parents, teachers and the foundation see progress as it happens.",
        solution=[
            "The foundation chose {{svc:acd}} because one platform covered attendance, assessments and grades, with a portal for every role. Two campuses started in the first semester; the remaining ten joined the next.",
            "The first change parents noticed was [[Real-time Attendance]]. As students check in, attendance is visible to the homeroom teacher, the parent and the principal at the same time.",
            "For teachers, [[Computer-based Assessment]] replaced most paper quizzes. Students answer online, scores arrive as soon as they finish, and the results flow straight into the term report.",
            "[[Role-based Portals]] gave each group its own view of the same data: management sees the whole foundation, teachers see their classes, parents see their child, and admins keep the records in one place.",
        ],
        solution_quote=("Parents see attendance before first period, and our teachers stopped retyping grades for the term report.", "Head of Academic Affairs"),
        solution_quote2=("I set a quiz in the morning and review the scores at lunch. I know who needs help before the next lesson.", "Mathematics Teacher"),
        connected="",
        screenshot=dict(mock=dict(title="Foundation · Today", chip="12 campuses", rows=[("Attendance", "95%", 95), ("Assessments scored", "1,240", 80)], alert=("ok", "Parents notified at 07:45")),
                        caption="The foundation view in Academic Management: attendance and scored assessments across all 12 campuses, updated through the day."),
        results_table=[("Campuses on one platform", "0", "12"), ("Time to prepare term reports", "About 2 weeks", "2× faster"), ("Roles with their own portal", "None", "6")],
        results=[
            "The result was not only faster reports. Teachers now use assessment results during the term to plan review sessions, and principals bring live attendance to weekly meetings instead of last month's recap.",
            "Parents ask fewer 'how is my child doing?' questions at school gates, because they already see attendance and new grades on their phones.",
        ],
        decision_quote=("For the first time, the foundation looks at all twelve schools with the same numbers, on the same day.", "Chair of the Foundation"),
        next="Next, the foundation plans to add Learning Content so teachers can share lesson materials across campuses, and to open the education office view to its district partners. The aim is one platform for the whole school community, from attendance to learning progress, in one place.",
        faq=[
            ("How does Academic Management help a group of schools?", "Every campus runs on the same platform, so attendance, assessments and grades are comparable across schools. This foundation brought 12 campuses together."),
            ("Can parents see attendance?", "Yes. Real-time Attendance shows arrivals to parents, teachers and the institution at the same time."),
            ("Is there a mobile app?", "Yes. Mobile Apps provide separate apps for students (iOS and Android) and for teachers."),
            ("How long does it take to move a campus over?", "It depends on the data you bring. This foundation started with two campuses in one semester and added the rest the next."),
        ],
    ),
    # ==========================================================================================
    "regional-isp": dict(
        location="Central Java", since="2025", size_detail="300+ network devices, 40,000 subscribers",
        capabilities_supporting=["Real-time Notifications", "Network Status History", "Web/API Monitoring"],
        hero_image="assets/services/network.jpg", hero_alt="Network operations wall showing throughput, system health and threat maps",
        sub="A regional internet service provider now flags 4 in 5 incidents before customers call, using Network Management for predictive alerts and one-click SLA reports.",
        context=[
            "The provider connects around 40,000 homes and small businesses across Central Java, many in towns where it is the main fibre provider. Its reputation rests on staying online: one long outage brings a wave of complaints and cancellations.",
            "A network operations team of eight engineers watches more than 300 devices, from core routers to last-mile switches, on shifts that cover the whole day.",
        ],
        bridge="Subscribers kept growing. But the team kept learning about problems from the people they were meant to protect.",
        challenge=[
            "Before the change, monitoring was split across several tools that only reported when something was already down. Most incidents reached the team as customer calls, and engineers spent the first part of every outage working out where the problem was.",
            "Monthly SLA reports took two days to assemble from screenshots and spreadsheets, so management saw availability long after the fact.",
        ],
        challenge_quote=("Our customers were our alarm system. That is not how you want to run a network.", "Network Operations Lead"),
        goal="Find problems before customers do, and report availability without building it by hand.",
        solution=[
            "The provider chose {{svc:net}} to bring devices, servers and APIs into one dashboard with alerts that look ahead. The team added its core and distribution layer first, then the rest of the network over the following month.",
            "The biggest change came from [[Proactive & Predictive Maintenance]]. Instead of waiting for a link to fail, engineers are warned when a link is heading for saturation and can reroute traffic in a planned window.",
            "[[Network Monitoring]] put every device on one dashboard, and Network Status History shows recurring patterns, such as a switch that degrades every evening peak.",
            "At the end of each month, [[Automated Reporting]] produces the SLA report as a PDF in one click.",
        ],
        solution_quote=("We see a link heading for trouble hours ahead, so we fix it in a maintenance window instead of on the phone with customers.", "Network Operations Lead"),
        solution_quote2=("The alert tells me which device and why. I start fixing instead of searching.", "Network Engineer"),
        connected="",
        screenshot=dict(mock=dict(title="Link SMG–SLO", chip="Predictive", rows=[("Utilisation", "82%", 82), ("Latency", "6 ms", 20)], alert=("warn", "Likely saturation in ~2 hours")),
                        caption="A predictive alert in Network Management: the team sees a link heading for saturation and reroutes traffic before the evening peak."),
        results_table=[("Incidents flagged before complaints", "Few", "80%"), ("Devices on one dashboard", "Split across tools", "300+"), ("Time to produce the monthly SLA report", "2 days", "1 click")],
        results=[
            "The result was not only fewer complaints. The team's rhythm changed: most fixes now happen in planned maintenance windows, and the morning stand-up starts with predicted risks rather than last night's outages.",
            "Management receives the SLA report on the first working day of the month, with the same numbers the engineers see.",
        ],
        decision_quote=("We used to measure the team by how fast they fixed outages. Now we measure how many never reached a customer.", "Chief Technology Officer"),
        next="Next, the provider plans to add Web/API Monitoring for its customer portal and payment API, and to adopt Traffic & Bandwidth Monitoring when it becomes available. The goal is simple: know about network issues before your users do.",
        faq=[
            ("How does Network Management help an ISP?", "It brings devices, servers and APIs into one dashboard and adds predictive alerts. This provider now flags 80% of incidents before customers call."),
            ("Can it produce SLA reports?", "Yes. Automated Reporting creates a PDF report for any period in one click."),
            ("What is predictive maintenance?", "Proactive & Predictive Maintenance warns about issues, such as a link heading for saturation, before they cause an outage."),
            ("How long does onboarding take?", "It depends on the size of the network. This provider added its core layer first and the rest over the following month."),
        ],
    ),
    # ==========================================================================================
    "consumer-finance": dict(
        location="Jakarta", since="2025", size_detail="80 agents, 1.2 million customers",
        capabilities_supporting=["Ticketing", "Knowledge Base", "Interaction Analytics"],
        hero_image="assets/services/omnichannel.jpg", hero_alt="Customer support dashboard with live metrics and a ticket queue",
        sub="A consumer finance company now answers 60% of customer questions with a chatbot and keeps every conversation in one inbox with Omnichannel Management.",
        context=[
            "The company provides consumer loans and instalment plans to more than a million customers, most of whom contact it on WhatsApp. Questions about payment dates, balances and documents arrive at all hours, and a slow answer can mean a missed payment.",
            "A customer service team of 80 agents handles chat, voice and video, led by a customer service manager who reports response times to the board every month.",
        ],
        bridge="The customer base kept growing. But every new channel added another app for agents to watch.",
        challenge=[
            "Before the change, agents switched between a WhatsApp tool, a call system and a web chat. A customer who wrote in the morning and called in the afternoon had to explain everything twice, and complaints were tracked in a shared spreadsheet.",
            "Most questions were routine, such as payment dates and how to upload documents, yet they waited in the same queue as urgent cases.",
        ],
        challenge_quote=("Half our day went on questions a well-written answer could handle, while the hard cases waited.", "Customer Service Manager"),
        goal="Keep every customer conversation in one place, and let the routine questions answer themselves.",
        solution=[
            "The company chose {{svc:crm}} for its official WhatsApp integration and modular packages. It started with the core inbox and ticketing, then added the chatbot two months later.",
            "The biggest change came from the [[Omnichannel Inbox]]. WhatsApp, chat and voice now land in one place, with the customer's history beside every message.",
            "[[Chatbot Builder]] took on the routine questions. The chatbot draws on a shared Knowledge Base, answers around the clock and hands anything complex to an agent with the context attached.",
            "Through the official [[WhatsApp API]], the company sends payment reminders and receives replies in the same inbox, instead of from a separate number.",
        ],
        solution_quote=("Our agents no longer jump between apps. The whole conversation is in one place, and the chatbot handles routine questions at night.", "Customer Service Manager"),
        solution_quote2=("When a customer writes after a call, I can see the call notes right there. I do not have to ask again.", "Customer Service Agent"),
        connected="",
        screenshot=dict(mock=dict(title="Chatbot · Today", chip="24/7", rows=[("Questions answered by chatbot", "60%", 60), ("Handed to an agent", "9%", 9)], alert=("ok", "Average first response under 1 minute")),
                        caption="The chatbot report in Omnichannel Management: routine questions are answered automatically and complex cases go to agents."),
        results_table=[("Questions answered by the chatbot", "0%", "60%"), ("Channels in one inbox", "3 separate tools", "3 in one"), ("First response time", "Baseline", "2× faster")],
        results=[
            "The result was not only faster replies. Agents now spend their time on complaints and restructuring requests, and the team reviews Interaction Analytics each week to decide which answers to add to the knowledge base next.",
            "Complaints are tracked as tickets, so the manager reports open cases and resolution times from the same system the agents use.",
        ],
        decision_quote=("We grew our customer base without growing the queue. That changed how we plan the team.", "Head of Customer Experience"),
        next="Next, the company plans to use Broadcast (Blast) for payment reminders and to explore grounding chatbot answers in its policy documents. The aim is every customer conversation in one inbox, answered quickly and consistently.",
        faq=[
            ("How does Omnichannel Management help a finance company?", "It brings WhatsApp, chat and voice into one inbox and adds a 24/7 chatbot. This company now answers 60% of questions automatically."),
            ("Does it work with WhatsApp?", "Yes, through the official WhatsApp API, with replies landing in the same inbox as other channels."),
            ("Can we start small?", "Yes. Modular Packages let you start with the core inbox and add the chatbot or broadcast later, as this company did."),
            ("What happens to questions the chatbot cannot answer?", "They go to an agent in the Omnichannel Inbox with the conversation attached, so the customer does not repeat themselves."),
        ],
    ),
}
