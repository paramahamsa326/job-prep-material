from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

OUT = Path.cwd() / "Parama_Hamsa_Generic_ServiceNow_Developer_Resume.docx"

NAVY = RGBColor(24, 55, 86)
GRAY = RGBColor(85, 93, 102)
BLACK = RGBColor(0, 0, 0)


def font(run, size=9.4, bold=False, color=BLACK, italic=False):
    run.font.name = "Arial"
    run._element.get_or_add_rPr().rFonts.set(qn("w:ascii"), "Arial")
    run._element.get_or_add_rPr().rFonts.set(qn("w:hAnsi"), "Arial")
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = color


def set_cell_margins(cell, top=60, start=90, bottom=60, end=90):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcMar = tcPr.first_child_found_in("w:tcMar")
    if tcMar is None:
        tcMar = OxmlElement("w:tcMar")
        tcPr.append(tcMar)
    for m, v in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tcMar.find(qn(f"w:{m}"))
        if node is None:
            node = OxmlElement(f"w:{m}")
            tcMar.append(node)
        node.set(qn("w:w"), str(v))
        node.set(qn("w:type"), "dxa")


def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    tcPr.append(shd)


def add_section_heading(doc, text):
    p = doc.add_paragraph(style="Heading 1")
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.space_before = Pt(7)
    p.paragraph_format.space_after = Pt(3)
    r = p.add_run(text.upper())
    font(r, 11, True, NAVY)
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "183756")
    pBdr.append(bottom)
    pPr.append(pBdr)


def add_bullet(doc, text, size=9.2, after=1.5):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.left_indent = Inches(0.18)
    p.paragraph_format.first_line_indent = Inches(-0.14)
    p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.keep_together = True
    r = p.add_run(text)
    font(r, size)
    return p


def add_role(doc, company, location, title, dates):
    table = doc.add_table(rows=2, cols=2)
    table.autofit = False
    table.columns[0].width = Inches(4.8)
    table.columns[1].width = Inches(1.7)
    for row in table.rows:
        row.cells[0].width = Inches(4.8)
        row.cells[1].width = Inches(1.7)
        for c in row.cells:
            set_cell_margins(c, 0, 0, 0, 0)
    p = table.cell(0, 0).paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    font(p.add_run(company), 10, True, NAVY)
    p = table.cell(0, 1).paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    font(p.add_run(location), 9, False, GRAY)
    p = table.cell(1, 0).paragraphs[0]
    p.paragraph_format.space_after = Pt(1)
    font(p.add_run(title), 9.5, True)
    p = table.cell(1, 1).paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    font(p.add_run(dates), 9, False, GRAY)


doc = Document()
sec = doc.sections[0]
sec.top_margin = Inches(0.48)
sec.bottom_margin = Inches(0.48)
sec.left_margin = Inches(0.62)
sec.right_margin = Inches(0.62)
sec.header_distance = Inches(0.25)
sec.footer_distance = Inches(0.25)

styles = doc.styles
normal = styles["Normal"]
normal.font.name = "Arial"
normal.font.size = Pt(9.4)
normal.paragraph_format.space_after = Pt(2)
normal.paragraph_format.line_spacing = 1.0
for style_name in ("List Bullet", "List Number"):
    s = styles[style_name]
    s.font.name = "Arial"
    s.font.size = Pt(9.2)

# Header
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_after = Pt(1)
font(p.add_run("PARAMA HAMSA VADLAMUDI"), 18, True, NAVY)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_after = Pt(1)
font(p.add_run("Senior ServiceNow Developer | Platform Engineering | Integrations | AI Automation"), 10.5, True, GRAY)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_after = Pt(4)
font(p.add_run("Seattle, WA | Open to Relocation | +1 409 600 0518 | paramahamsa326@gmail.com"), 9)

add_section_heading(doc, "Professional Summary")
p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(3)
p.paragraph_format.line_spacing = 1.03
font(p.add_run(
    "Senior ServiceNow developer and platform engineer with 8+ years at ServiceNow and 13+ years in software engineering. "
    "Hands-on experience delivering enterprise applications, reusable user experiences, workflow automation, secure integrations, "
    "AI-assisted service capabilities, automated testing, and production-ready platform services. Strong in JavaScript-based ServiceNow "
    "development, UI Builder/Next Experience, Flow Designer, Integration Hub, MID Server, REST APIs, ACLs, ATF, Java/Spring, cloud-native "
    "engineering, performance tuning, and technical leadership."
), 9.4)

add_section_heading(doc, "ServiceNow Technical Expertise")
skill_rows = [
    ("Platform Development", "ServiceNow Platform, ServiceNow Studio, scoped/enterprise applications, Business Rules, Client Scripts, ACLs, Flow Designer, Workflow Editor, reusable application components"),
    ("User Experience", "UI Builder, Next Experience UI Framework, Service Portal, CMS, Angular, jQuery, JavaScript, HTML5, CSS3, responsive design, reusable UI components, WCAG accessibility"),
    ("Integrations", "Integration Hub, REST APIs, MID Server, OAuth 2.0, Basic Authentication, data mapping, Workday, SCCM, Azure AD, JAMF, Moveworks Agent Studio, APIthon Script Actions, HTTP/Script/Compound Actions"),
    ("AI and Automation", "AI Agent Studio, AI Agents, Agent Skills, Now Assist, Now LLM, contextual assistance, case-resolution automation, summarization, workflow/action orchestration, shell automation"),
    ("Quality and Delivery", "Automated Test Framework (ATF), Git, Jenkins, Maven, Postman, CI/CD, Agile delivery, code reviews, testing strategy, release automation"),
    ("Supporting Engineering", "Java 17/21, Spring Boot, Spring MVC, Spring Data JPA, Hibernate, Spring Security, Kafka, REST/OpenAPI, Docker, Kubernetes, AWS, SQL/NoSQL, Grafana, Prometheus, Splunk"),
]
t = doc.add_table(rows=0, cols=2)
t.autofit = False
for label, detail in skill_rows:
    cells = t.add_row().cells
    cells[0].width = Inches(1.45)
    cells[1].width = Inches(5.75)
    set_cell_margins(cells[0]); set_cell_margins(cells[1])
    shade(cells[0], "E9EFF5")
    p = cells[0].paragraphs[0]; p.paragraph_format.space_after = Pt(0)
    font(p.add_run(label), 8.7, True, NAVY)
    p = cells[1].paragraphs[0]; p.paragraph_format.space_after = Pt(0)
    font(p.add_run(detail), 8.7)

add_section_heading(doc, "Professional Experience")
add_role(doc, "ServiceNow Inc.", "Seattle, WA", "Senior Software Engineer", "Jan 2018 - Present")
bullets = [
    "Designed and developed enterprise applications on the ServiceNow Platform using JavaScript, ServiceNow Studio, Business Rules, Client Scripts, ACLs, Flow Designer, Workflow Editor, REST APIs, Java, and microservices.",
    "Built modular, responsive, WCAG-compliant user experiences and reusable components with UI Builder, Next Experience UI Framework, Service Portal, CMS, Angular, jQuery, HTML, and CSS.",
    "Developed AI Agents and Agent Skills in AI Agent Studio, integrating Now Assist and Now LLM to automate case resolution, summarize employee data, and provide contextual assistance.",
    "Integrated ServiceNow with Workday, SCCM, Azure AD, and JAMF using Integration Hub, REST APIs, MID Servers, OAuth 2.0, Basic Authentication, and secure data-mapping patterns.",
    "Created Moveworks actions and orchestrations using Agent Studio, APIthon Script Actions, HTTP/Script/Compound Actions, and ServiceNow REST APIs so conversational assistants could complete employee tasks.",
    "Engineered Java 17/21 and Spring services supporting platform applications and integrations, applying Spring Boot, MVC, Data JPA, Hibernate, Spring Security, transaction management, API versioning, JWT, and secrets-management practices.",
    "Designed Kafka-based asynchronous processing with partitioning, consumer groups, offset management, delivery semantics, idempotency, retries, dead-letter queues, and schema evolution for resilient distributed workflows.",
    "Applied fault tolerance, eventual consistency, circuit breakers, back-pressure, sagas, high availability, disaster recovery, caching, concurrency, JVM profiling, garbage-collection diagnostics, and database tuning to production services.",
    "Supported AWS-hosted and containerized workloads using EC2, EKS/ECS, Lambda, S3, RDS, DynamoDB, SQS, SNS, API Gateway, IAM, CloudWatch, Docker, Kubernetes, Helm, probes, autoscaling, Secrets, ConfigMaps, Ingress, canary delivery, and GitOps practices.",
    "Implemented automated validation and delivery with ATF, Git, Maven, Jenkins, Postman, unit/integration testing, and CI/CD; mentored developers on scalable scripting, testing strategy, code quality, and application architecture.",
    "Used Grafana, Prometheus, Splunk, metrics, tracing, on-call practices, incident response, and postmortems to improve operability and reduce recovery time across production services.",
    "Optimized queries, indexes, payloads, and lazy-loading behavior to improve application responsiveness; contributed automation that reduced case-task volume and weekly inflow by 30%."
]
for b in bullets: add_bullet(doc, b, 9.05, 1.2)

add_role(doc, "8x8, Inc.", "San Jose, CA", "Software Developer", "Sep 2016 - Dec 2017")
for b in [
    "Developed high-performance Java 8 and Spring Boot microservices with Maven for scalable distributed backend systems in a cloud-native environment.",
    "Built real-time, event-driven applications with Apache Kafka for asynchronous service communication and data streaming.",
    "Designed secure REST integrations using Dell Boomi to connect internal systems with third-party platforms.",
    "Supported quality and release automation with JUnit, Mockito, Spring Test, Jenkins, Docker, and Kubernetes."
]: add_bullet(doc, b)

add_role(doc, "OpenText Pvt. Ltd.", "Hyderabad, India", "Software Engineer", "Feb 2013 - Dec 2014")
for b in [
    "Implemented backend logic and secure data processing for a corporate social-networking platform, maintaining reliability during high-activity periods.",
    "Developed unit, integration, and end-to-end tests using JUnit 4, Mockito, and Selenium across business logic and database interactions.",
    "Improved peak-load response time by 10% by eliminating Hibernate N+1 queries, tuning SQL indexes and JDBC connection pools, and reducing JVM heap pressure and garbage-collection pauses."
]: add_bullet(doc, b)

add_section_heading(doc, "Education")
for degree in [
    "M.S., Computer Science - Lamar University, Beaumont, TX | 2015 - 2016",
    "B.Tech., Electronics and Communication Engineering - Vignan University, Guntur, India | 2009 - 2013",
]:
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(1)
    font(p.add_run(degree), 9.2, True if degree.startswith("M.S.") else False)

# Quiet footer
footer = sec.footer.paragraphs[0]
footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
font(footer.add_run("Parama Hamsa Vadlamudi | ServiceNow Developer Resume"), 8, False, GRAY)

# Keep rows together and reduce table borders for ATS-friendly rendering.
for table in doc.tables:
    for row in table.rows:
        trPr = row._tr.get_or_add_trPr()
        cant_split = OxmlElement("w:cantSplit")
        trPr.append(cant_split)

doc.core_properties.title = "Parama Hamsa Vadlamudi - Generic ServiceNow Developer Resume"
doc.core_properties.subject = "ATS-friendly ServiceNow Developer resume"
doc.core_properties.author = "Parama Hamsa Vadlamudi"
doc.save(OUT)
print(OUT)
