from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_LINE_SPACING
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.section import WD_SECTION
from pathlib import Path

OUT = Path.cwd() / "Parama_Hamsa_Vadlamudi_Java_Full_Stack_Resume_Harika_Format.docx"

def set_font(run, name="Calibri", size=9.2, bold=False, color="000000", italic=False):
    run.font.name = name
    run._element.get_or_add_rPr().rFonts.set(qn("w:ascii"), name)
    run._element.get_or_add_rPr().rFonts.set(qn("w:hAnsi"), name)
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = RGBColor.from_string(color)

def set_cell_margins(cell, top=40, start=70, bottom=40, end=70):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = tcPr.first_child_found_in("w:tcMar")
    if tcMar is None:
        tcMar = OxmlElement("w:tcMar")
        tcPr.append(tcMar)
    for m, v in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tcMar.find(qn(f"w:{m}"))
        if node is None:
            node = OxmlElement(f"w:{m}")
            tcMar.append(node)
        node.set(qn("w:w"), str(v)); node.set(qn("w:type"), "dxa")

def add_bottom_border(p, color="1F4E79", size="8"):
    pPr = p._p.get_or_add_pPr()
    pBdr = pPr.find(qn("w:pBdr"))
    if pBdr is None:
        pBdr = OxmlElement("w:pBdr"); pPr.append(pBdr)
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single"); bottom.set(qn("w:sz"), size)
    bottom.set(qn("w:space"), "1"); bottom.set(qn("w:color"), color)
    pBdr.append(bottom)

def keep_with_next(p):
    p.paragraph_format.keep_with_next = True

doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Inches(8.27), Inches(11.69)
sec.left_margin = sec.right_margin = Inches(0.75)
sec.top_margin = sec.bottom_margin = Inches(0.5)
sec.header_distance = Inches(0.2); sec.footer_distance = Inches(0.2)

styles = doc.styles
normal = styles["Normal"]
normal.font.name = "Calibri"; normal.font.size = Pt(9.2)
normal._element.rPr.rFonts.set(qn("w:ascii"), "Calibri")
normal._element.rPr.rFonts.set(qn("w:hAnsi"), "Calibri")
normal.paragraph_format.space_after = Pt(0)
normal.paragraph_format.line_spacing = 1.0

for name, size, bold in (("Resume Section", 10.5, True), ("Resume Employer", 9.4, True), ("Resume Role", 9.2, True), ("Resume Environment", 8.2, False)):
    if name not in styles:
        st = styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
    else: st = styles[name]
    st.font.name = "Calibri"; st.font.size = Pt(size); st.font.bold = bold
    st._element.rPr.rFonts.set(qn("w:ascii"), "Calibri"); st._element.rPr.rFonts.set(qn("w:hAnsi"), "Calibri")
    st.paragraph_format.space_after = Pt(0)

bullet = styles["List Bullet"]
bullet.font.name = "Calibri"; bullet.font.size = Pt(9.2)
bullet.paragraph_format.left_indent = Inches(0.18)
bullet.paragraph_format.first_line_indent = Inches(-0.14)
bullet.paragraph_format.space_after = Pt(1.2)
bullet.paragraph_format.line_spacing = 1.0

def section_heading(text):
    p = doc.add_paragraph(style="Resume Section")
    p.paragraph_format.space_before = Pt(5); p.paragraph_format.space_after = Pt(2)
    keep_with_next(p); add_bottom_border(p)
    r = p.add_run(text.upper()); set_font(r, size=10.5, bold=True, color="1F4E79")
    return p

def bullet_item(text):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.widow_control = True
    r = p.add_run(text); set_font(r, size=9.2)
    return p

def employer(company, location, dates, role, context=None):
    p = doc.add_paragraph(style="Resume Employer")
    p.paragraph_format.space_before = Pt(3); keep_with_next(p)
    p.paragraph_format.tab_stops.add_tab_stop(Inches(6.75), 2)
    r = p.add_run(f"{company} - {location}"); set_font(r, size=9.4, bold=True)
    r = p.add_run("\t" + dates); set_font(r, size=9.2, bold=True)
    p2 = doc.add_paragraph(style="Resume Role"); keep_with_next(p2)
    r = p2.add_run(role); set_font(r, size=9.2, bold=True, color="1F4E79")
    if context:
        r = p2.add_run(" | " + context); set_font(r, size=8.8, italic=True, color="404040")

def environment(text):
    p = doc.add_paragraph(style="Resume Environment")
    p.paragraph_format.space_before = Pt(1); p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_together = True
    r = p.add_run("Environment: "); set_font(r, size=8.2, bold=True, color="1F4E79")
    r = p.add_run(text); set_font(r, size=8.2, color="404040")

# Header
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_after = Pt(0)
r = p.add_run("PARAMA HAMSA VADLAMUDI"); set_font(r, size=16, bold=True, color="1F4E79")
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_after = Pt(1)
r = p.add_run("Dallas, TX | Onsite | +1 409-600-0518 | paramahamsa326@gmail.com | linkedin.com/in/paramvadlamudi")
set_font(r, size=9.2)

section_heading("Professional Summary")
for t in [
    "Senior Software Engineer and Java Full Stack Lead with 10+ years of experience building high-availability enterprise applications, event-driven services, and cloud-native platforms.",
    "Strong backend expertise in Java 11/17, Spring Boot, Spring MVC, Spring Data JPA, Spring Security, Spring Batch, Hibernate, REST APIs, Kafka, and distributed microservice patterns.",
    "Full-stack delivery experience with Angular 14/16, TypeScript, HTML5, CSS3/SASS, Bootstrap, PostgreSQL, Oracle, MySQL, MongoDB, and Redis.",
    "Hands-on cloud and DevSecOps background across AWS, Kubernetes, Red Hat OpenShift, Docker, GitHub Actions, Harness, Jenkins, observability, and vulnerability remediation.",
    "Technical leader who owns architecture through production operations, mentors engineers, improves delivery workflows, and applies AI-assisted development tools to accelerate engineering quality."
]: bullet_item(t)

section_heading("Technical Skills")
skills = [
    ("Languages", "Java 8/11/17/21, Python, Go, TypeScript, JavaScript, SQL, PL/SQL, Bash, PowerShell"),
    ("Java & Frameworks", "Core Java, Collections, Streams, Lambdas, Multithreading, Spring Boot, Spring MVC, Spring Batch, Spring Security, Spring Data JPA, Spring AOP, Hibernate"),
    ("Front End", "Angular 12/14/16, React, Redux, HTML5, CSS3/SASS, Bootstrap, AJAX, JSON, jQuery"),
    ("APIs & Messaging", "REST, SOAP, OpenAPI/Swagger, Kafka, ActiveMQ, JMS, API Gateway, Eureka, Resilience4j, SAGA"),
    ("Cloud & Containers", "AWS EKS, EC2, RDS, S3, Lambda, ECR, IAM, CloudWatch; Kubernetes, OpenShift, Docker, Helm, Nginx, PCF"),
    ("Data", "PostgreSQL, Oracle, MySQL, SQL Server, MongoDB, Redis, Cassandra, Sybase; data modeling, indexing, query tuning"),
    ("CI/CD & Build", "GitHub Actions, Harness, Jenkins, Git, Bitbucket, Maven, Gradle, Ant, Nexus"),
    ("Testing", "JUnit, Mockito, Postman, integration testing, TDD, automated regression testing"),
    ("Observability", "Splunk, AppDynamics, Prometheus, Grafana, PagerDuty, Log4j, SLF4J"),
    ("Security", "OAuth 2.0, JWT, AWS IAM, ACLs, secrets management, CSRF protection, SAST/DAST, CVE remediation"),
    ("AI & Tooling", "GitHub Copilot, LLM APIs/SDKs, RAG, AI agents, Codex, Moveworks, Windsurf; JIRA, Confluence")
]
table = doc.add_table(rows=0, cols=2)
table.autofit = False
table.columns[0].width = Inches(1.45); table.columns[1].width = Inches(5.32)
tblPr = table._tbl.tblPr
tblW = tblPr.find(qn("w:tblW")); tblW.set(qn("w:w"), "9749"); tblW.set(qn("w:type"), "dxa")
grid = table._tbl.tblGrid
for child in list(grid): grid.remove(child)
for width in (2088, 7661):
    c = OxmlElement("w:gridCol"); c.set(qn("w:w"), str(width)); grid.append(c)
for i, (cat, val) in enumerate(skills):
    cells = table.add_row().cells
    for cell, width in zip(cells, (2088, 7661)):
        cell.width = Inches(width/1440); cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        set_cell_margins(cell)
        tcW = cell._tc.get_or_add_tcPr().find(qn("w:tcW")); tcW.set(qn("w:w"), str(width)); tcW.set(qn("w:type"), "dxa")
    if i % 2 == 0:
        for cell in cells:
            shd = OxmlElement("w:shd"); shd.set(qn("w:fill"), "F3F6F8"); cell._tc.get_or_add_tcPr().append(shd)
    p0, p1 = cells[0].paragraphs[0], cells[1].paragraphs[0]
    p0.paragraph_format.space_after = p1.paragraph_format.space_after = Pt(0)
    set_font(p0.add_run(cat), size=8.7, bold=True, color="1F4E79")
    set_font(p1.add_run(val), size=8.7)

section_heading("Professional Experience")
employer("ServiceNow Inc.", "Seattle, WA", "Jan 2018 - Present", "Senior Software Engineer / Java Full Stack Lead", "Enterprise workflow automation and cloud asset lifecycle platform")
for t in [
    "Lead full-stack architecture, technical design, and delivery for high-throughput enterprise automation services supporting multi-region deployments and millions of operational transactions.",
    "Design cloud-native microservices with Java 11/17, Spring Boot, Spring Batch, Spring Data JPA, and Spring Security for transaction processing, background jobs, and enterprise data ingestion.",
    "Build responsive administration and analytics experiences with Angular 14/16, TypeScript, HTML5, SASS, and Bootstrap.",
    "Define REST API contracts with OpenAPI/Swagger and enforce OAuth 2.0, JWT, AWS IAM, validation, and authorization controls.",
    "Optimize PostgreSQL and MongoDB persistence layers through data modeling, query tuning, spatial indexing, and elimination of N+1 query patterns.",
    "Deploy and scale containerized services on Red Hat OpenShift, Kubernetes, and AWS EKS using ingress rules, health probes, and horizontal pod autoscaling.",
    "Engineer GitHub Actions, Harness, and Jenkins pipelines for automated testing, security scanning, and zero-downtime canary deployments.",
    "Implement observability with Splunk, AppDynamics, Prometheus, Grafana, and PagerDuty; lead incident response and remediate high-severity dependency and application vulnerabilities.",
    "Automate developer setup, proxy configuration, and operational workflows with Bash, Python, and PowerShell, reducing environment setup and onboarding time by 50%.",
    "Introduce GitHub Copilot, LLM APIs/SDKs, and agent-based engineering workflows, accelerating feature delivery by 35% and automating test generation."
]: bullet_item(t)
environment("Java 11/17, Spring Boot, Spring Batch, Spring Data JPA, Spring Security, Microservices, Angular 14/16, TypeScript, PostgreSQL, MongoDB, Redis, Kafka, AWS EKS/RDS, OpenShift, Kubernetes, Docker, GitHub Actions, Harness, Jenkins, Splunk, AppDynamics, Prometheus, Grafana, Python, Bash")

employer("8x8, Inc.", "San Jose, CA", "Sep 2016 - Dec 2017", "Software Developer - Java Full Stack", "Communication, messaging, and content moderation platform")
for t in [
    "Delivered full-stack features using Java 8/11, Spring Boot, Spring MVC, Hibernate, Angular, TypeScript, and Bootstrap in an Agile Scrum environment.",
    "Built secure REST services and third-party integrations, documenting contracts and validating integrations with Postman and mock services.",
    "Implemented Kafka and JMS messaging to decouple services and added retry processing with offset tracking for failed events.",
    "Created moderation workflows and analytics dashboards for policy review and real-time approval and rejection metrics.",
    "Optimized Oracle and MySQL queries, joins, stored procedures, connection pools, and persistence mappings.",
    "Containerized Java services with Docker and maintained Jenkins/Maven delivery pipelines with JUnit and Mockito test suites.",
    "Used Splunk and Log4j telemetry to diagnose production issues, coordinate fixes, and deliver hotfixes."
]: bullet_item(t)
environment("Java 8/11, Spring Boot, Spring MVC, Spring Security, Hibernate, Angular, TypeScript, HTML5, CSS3, Oracle, MySQL, Kafka, Docker, Kubernetes, Jenkins, Maven, REST APIs, JUnit, Mockito, Splunk, JIRA, Git")

employer("OpenText Pvt. Ltd.", "Hyderabad, India", "Feb 2013 - Dec 2014", "Software Engineer")
for t in [
    "Contributed across analysis, design, development, unit testing, and defect resolution for enterprise web applications.",
    "Developed server-side components with Java, Spring MVC/Core/JDBC, Servlets, Hibernate, and layered MVC patterns.",
    "Improved peak-load response time by 10% by eliminating Hibernate N+1 queries, tuning indexes, and optimizing JDBC connection pools.",
    "Built responsive interfaces with JSP, custom tags, HTML, CSS, JavaScript, and AJAX.",
    "Exposed and consumed SOAP services with Apache CXF and REST APIs with JAX-RS; created Oracle and MySQL tables, views, procedures, and triggers.",
    "Automated Maven and Ant builds, used Git and SVN workflows, and wrote JUnit tests with Log4j-based diagnostics."
]: bullet_item(t)
environment("Java, Spring MVC, Spring JDBC, Hibernate, JSP, Servlets, HTML, JavaScript, AJAX, Oracle, MySQL, SQL, PL/SQL, SOAP, REST, JUnit, Log4j, Maven, Ant, Git, Eclipse, Apache Tomcat")

section_heading("Education")
for degree, school, dates in [
    ("Master of Science in Computer Science", "Lamar University, USA", "2015 - 2016"),
    ("Bachelor of Technology in Electronics & Communication Engineering", "Vignan University, India", "2009 - 2013")
]:
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.tab_stops.add_tab_stop(Inches(6.75), 2)
    set_font(p.add_run(degree), size=9.2, bold=True)
    set_font(p.add_run(f" | {school}"), size=9.2)
    set_font(p.add_run("\t" + dates), size=9.2, bold=True)

# Footer page number field
footer = sec.footer
fp = footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = fp.add_run("Page "); set_font(r, size=8, color="666666")
fld = OxmlElement("w:fldSimple"); fld.set(qn("w:instr"), "PAGE")
rr = OxmlElement("w:r"); tt = OxmlElement("w:t"); tt.text = "1"; rr.append(tt); fld.append(rr); fp._p.append(fld)

doc.core_properties.title = "Parama Hamsa Vadlamudi - Java Full Stack Resume"
doc.core_properties.subject = "Senior Software Engineer / Java Full Stack Lead"
doc.core_properties.author = "Parama Hamsa Vadlamudi"
doc.save(OUT)
print(OUT)
