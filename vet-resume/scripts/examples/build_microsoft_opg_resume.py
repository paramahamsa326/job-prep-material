from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

OUT = r"Job_Applications\Parama_Hamsa_Vadlamudi_Microsoft_OPG_Data_Platform.docx"

doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Inches(8.5), Inches(11)
sec.top_margin, sec.bottom_margin = Inches(.43), Inches(.43)
sec.left_margin, sec.right_margin = Inches(.58), Inches(.58)
sec.header_distance, sec.footer_distance = Inches(.2), Inches(.2)

styles = doc.styles
normal = styles['Normal']
normal.font.name = 'Arial'
normal.font.size = Pt(8.7)
normal.font.color.rgb = RGBColor(0, 0, 0)
normal.paragraph_format.space_after = Pt(0)
normal.paragraph_format.line_spacing = 1.0
normal._element.rPr.rFonts.set(qn('w:ascii'), 'Arial')
normal._element.rPr.rFonts.set(qn('w:hAnsi'), 'Arial')

for sname in ['Title', 'Heading 1']:
    s = styles[sname]
    s.font.name = 'Arial'
    s.font.color.rgb = RGBColor(0, 0, 0)
    s._element.rPr.rFonts.set(qn('w:ascii'), 'Arial')
    s._element.rPr.rFonts.set(qn('w:hAnsi'), 'Arial')

styles['Title'].font.size = Pt(17)
styles['Title'].font.bold = True
styles['Title'].paragraph_format.space_after = Pt(1)
styles['Title'].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
styles['Heading 1'].font.size = Pt(10)
styles['Heading 1'].font.bold = True
styles['Heading 1'].paragraph_format.space_before = Pt(3.5)
styles['Heading 1'].paragraph_format.space_after = Pt(1.5)
styles['Heading 1'].paragraph_format.keep_with_next = True

def set_bottom_border(p):
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '6')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), '000000')
    pBdr.append(bottom)
    pPr.append(pBdr)

def heading(text):
    p = doc.add_paragraph(text.upper(), style='Heading 1')
    set_bottom_border(p)
    return p

def add_text(text, size=8.7, bold=False, italic=False, align=None):
    p = doc.add_paragraph()
    if align is not None:
        p.alignment = align
    r = p.add_run(text)
    r.bold, r.italic, r.font.size = bold, italic, Pt(size)
    r.font.name = 'Arial'
    return p

def add_labeled(lines):
    for label, value in lines:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(.4)
        a = p.add_run(label + ': ')
        a.bold = True
        b = p.add_run(value)
        for r in (a, b):
            r.font.name = 'Arial'
            r.font.size = Pt(8.25)

def job(company, location, title, dates, bullets):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.keep_with_next = True
    left = p.add_run(company)
    left.bold = True
    right = p.add_run('  |  ' + location)
    right.italic = True
    for r in (left, right): r.font.size = Pt(8.7)
    p2 = doc.add_paragraph()
    p2.paragraph_format.space_after = Pt(.5)
    p2.paragraph_format.keep_with_next = True
    a = p2.add_run(title)
    a.bold = True
    b = p2.add_run('  |  ' + dates)
    b.italic = True
    for r in (a, b): r.font.size = Pt(8.4)
    for bullet in bullets:
        q = doc.add_paragraph(style='List Bullet')
        q.paragraph_format.left_indent = Inches(.15)
        q.paragraph_format.first_line_indent = Inches(-.11)
        q.paragraph_format.space_after = Pt(.7)
        q.paragraph_format.line_spacing = .96
        q.add_run(bullet)

p = doc.add_paragraph('Parama Hamsa Vadlamudi', style='Title')
add_text('Seattle, WA | Open to Relocation | +1 409 600 0518 | paramahamsa326@gmail.com', 8.5, align=WD_ALIGN_PARAGRAPH.CENTER)

heading('Software Engineer - Agentic AI & Data Platforms')
add_text('Software Engineer with 11+ years of experience building and operating production software, agentic AI workflows, distributed data services, and enterprise integrations. Hands-on experience creating AI agents and skills with large language models, orchestrating API-driven actions, processing streaming and relational data, and implementing validation, observability, CI/CD, and fault-tolerance guardrails. Strong foundation in Java, JavaScript, SQL, Kafka, REST APIs, cloud-native systems, data modeling, and production operations.', 8.45)

heading('Technical Skills')
add_labeled([
    ('Agentic AI', 'AI Agents, Agent Skills, Agent Orchestration, Now LLM, Now Assist, Prompt Engineering, AI-Assisted Summarization, Deterministic API Grounding'),
    ('Data Engineering', 'SQL, Data Modeling, Data Ingestion, Data Transformation, Kafka, Event-Driven Processing, Data Validation, MySQL, PostgreSQL, MongoDB, DynamoDB, Redis'),
    ('Software & APIs', 'Java 17/21, JavaScript, Spring Boot, REST APIs, Microservices, OpenAPI, JSON, Shell Scripting'),
    ('Reliability', 'Idempotency, Retries, Dead-Letter Queues, Fault Tolerance, Monitoring, Grafana, Prometheus, Splunk, Incident Response, Postmortems'),
    ('Cloud & Delivery', 'AWS, Docker, Kubernetes, Helm, Maven, Git, Jenkins, CI/CD, JUnit, Mockito, Postman'),
])

heading('Professional Experience')
job('ServiceNow Inc.', 'Seattle, WA', 'Senior Software Engineer', 'January 2018-Present', [
    'Built and operated production AI agents and agent skills using AI Agent Studio, Now Assist, and Now LLM to orchestrate case resolution, enterprise-data summarization, contextual assistance, and API-driven employee workflows.',
    'Developed agent actions and multi-step workflows that grounded model output in structured ServiceNow data and deterministic REST API responses, enabling assistants to execute governed business tasks without inventing system-of-record values.',
    'Designed ingestion, transformation, and integration services using Java 17/21, Spring Boot, Kafka, REST APIs, SQL/NoSQL data stores, and data mapping to connect enterprise systems and support analytics-ready workflows.',
    'Implemented operational guardrails with schema-aware processing, idempotency, retries, dead-letter queues, automated tests, monitoring, tracing, and incident response to improve correctness, freshness, and recoverability of distributed data operations.',
    'Improved application and query performance through SQL optimization, indexing, lazy loading, caching, JVM diagnostics, and profiling; supported production health with Grafana, Prometheus, Splunk, postmortems, and on-call ownership.',
    'Led design and code reviews, CI/CD automation, and developer mentoring; delivered workflow automation that reduced case-task volume and weekly inflow by 30%.',
])
job('8x8, Inc.', 'San Jose, CA', 'Software Developer', 'September 2016-December 2017', [
    'Developed cloud-native Java 8 and Spring Boot microservices and real-time Kafka pipelines for scalable ingestion, asynchronous processing, and data exchange across distributed services.',
    'Built secure REST integrations and reusable transformation flows connecting internal and third-party systems; improved release reliability with JUnit, Mockito, Spring Test, Jenkins, Docker, and Kubernetes.',
])
job('OpenText Pvt. Ltd.', 'Hyderabad, India', 'Software Engineer', 'February 2013-December 2014', [
    'Developed reliable backend data-processing services for an enterprise collaboration platform and validated business logic, database interactions, and end-to-end behavior with automated tests.',
    'Improved peak-load response time by 10% by eliminating Hibernate N+1 queries, tuning SQL indexes and JDBC connection pools, and reducing JVM heap pressure and garbage-collection pauses.',
])

heading('Education')
add_text('M.S., Computer Science, Lamar University, Beaumont, TX | 2016', 8.3, bold=True)
add_text('B.Tech., Electronics and Communication Engineering, Vignan University, India | 2013', 8.3, bold=True)

props = doc.core_properties
props.title = 'Parama Hamsa Vadlamudi - Software Engineer, Agentic AI and Data Platforms'
props.subject = 'Microsoft OPG Office Analytics and Experimentation'
props.author = 'Parama Hamsa Vadlamudi'
doc.save(OUT)
print(OUT)
