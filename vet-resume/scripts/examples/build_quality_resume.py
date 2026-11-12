from pathlib import Path

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

OUT = Path.cwd() / "Parama Hamsa Vadlamudi Resume Quality Engineer - Full QA.docx"
FONT = "Charter"
BLACK = RGBColor(0, 0, 0)
CM = 0.3937007874

doc = Document()
sec = doc.sections[0]
sec.page_width = Inches(8.5)
sec.page_height = Inches(11)
sec.top_margin = Inches(2 * CM)
sec.bottom_margin = Inches(2 * CM)
sec.left_margin = Inches(2 * CM)
sec.right_margin = Inches(2 * CM)
sec.header_distance = Inches(.39)
sec.footer_distance = Inches(.39)

def set_font(run, size=10, bold=False, italic=False):
    run.font.name = FONT
    run._element.get_or_add_rPr().rFonts.set(qn('w:ascii'), FONT)
    run._element.get_or_add_rPr().rFonts.set(qn('w:hAnsi'), FONT)
    run._element.get_or_add_rPr().rFonts.set(qn('w:eastAsia'), FONT)
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = BLACK

normal = doc.styles['Normal']
normal.font.name = FONT
normal._element.rPr.rFonts.set(qn('w:ascii'), FONT)
normal._element.rPr.rFonts.set(qn('w:hAnsi'), FONT)
normal.font.size = Pt(10.3)
normal.font.color.rgb = BLACK
normal.paragraph_format.space_before = Pt(0)
normal.paragraph_format.space_after = Pt(0)
normal.paragraph_format.line_spacing = 1.0

def add_bottom_rule(p):
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '4')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), '000000')
    pBdr.append(bottom)
    pPr.append(pBdr)

def heading(text, first=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4 if first else 8)
    p.paragraph_format.space_after = Pt(5)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    set_font(r, 12.5, True)
    add_bottom_rule(p)

def paragraph(text, size=10, after=0):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.line_spacing = 1.0
    r = p.add_run(text)
    set_font(r, size)
    return p

def experience_header(title, company, location, dates, note=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(5)
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.tab_stops.add_tab_stop(Inches(3.82), WD_TAB_ALIGNMENT.CENTER)
    p.paragraph_format.tab_stops.add_tab_stop(Inches(6.92), WD_TAB_ALIGNMENT.RIGHT)
    r = p.add_run(title); set_font(r, 10.3, True)
    r = p.add_run('\t' + company + ' - ' + location); set_font(r, 10.3, True)
    r = p.add_run('\t' + dates); set_font(r, 10.3, True)
    if note:
        p2 = doc.add_paragraph()
        p2.paragraph_format.space_after = Pt(1)
        p2.paragraph_format.keep_with_next = True
        r = p2.add_run(note); set_font(r, 9.7, False, True)

def bullet(text):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.left_indent = Inches(.14)
    p.paragraph_format.first_line_indent = Inches(-.14)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2.1)
    p.paragraph_format.line_spacing = 1.03
    p.paragraph_format.keep_together = True
    r = p.add_run(text); set_font(r, 10.05)

def labeled_line(label, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2.2)
    p.paragraph_format.line_spacing = 1.03
    r = p.add_run(label + ': '); set_font(r, 10.05, True)
    r = p.add_run(text); set_font(r, 10.05)

# Canonical centered header.
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_after = Pt(5)
r = p.add_run('Parama Hamsa Vadlamudi'); set_font(r, 25)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_after = Pt(2)
r = p.add_run('San Jose, CA | paramahamsa326@gmail.com | +1 409 600 0518'); set_font(r, 10)

heading('Professional Summary', first=True)
paragraph('Senior Software Quality Engineer with 11+ years of experience owning quality strategy, test automation, and release readiness across cloud platforms, mobile ecosystems, and AI/ML workflows. At ServiceNow, led end-to-end quality initiatives across high-impact product portfolios, including Asset Management, Safe Workplace Apps, Workplace Service Delivery, and HR Service Delivery. Experienced in building scalable automation frameworks, strengthening CI/CD pipelines, and designing evaluation coverage for modern AI applications. Known for a proactive, engineering-minded approach to finding risk early and delivering reliable, high-performing software.', 10.3, 1)

heading('Core Skills')
labeled_line('Quality Leadership & Strategy', 'Test architecture, AI model and agent evaluation, release-risk assessment, defect triage, cross-team quality standards, Agile/Scrum')
labeled_line('Automation & Tools', 'Selenium WebDriver, JUnit, TestNG, Cypress, Playwright, Postman, Jenkins CI/CD pipelines, REST API testing')
labeled_line('Testing Scope', 'AI/LLM workflows, RAG system validation, cross-device testing across Android, Windows, web, mobile, and cloud; functional, regression, integration, performance, and reliability testing')
labeled_line('Languages & Technologies', 'Java, Python, JavaScript, SQL, Glide API, Node.js, React, HTML5/CSS3, Git/GitHub')

heading('Work Experience')
experience_header('Senior Software Quality Engineer', 'ServiceNow Inc.', 'San Jose, CA', 'Jan 2018 - Present', 'Promoted from Associate Software Quality Engineer')
for text in [
    'Took ownership of quality strategy across multiple business units, leading test planning, release-risk evaluations, defect triage, and cross-team quality standards to support stable, predictable production releases.',
    'Designed and maintained test suites for complex workflows, multi-step agent actions, and contextual logic across HR Service Delivery and Safe Workplace Apps, including evaluation of accuracy, grounding, hallucination, latency, and safety behavior.',
    'Led quality strategy for HR Service Delivery products including Journey Designer, Life Cycle Events, HR Case Management, Opportunity Management, Talent Insights, Career Hub, Succession Planning, and EmployeeWorks, reducing post-launch issues by more than 40%.',
    'Served as lead quality engineer for critical Safe Workplace applications, including Emergency Outreach, Contact Tracing, Vaccination Status, Safe Workplace Dashboard, Employee Readiness Survey, Health Screening, Travel Safety, Health and Safety Testing, and PPE Inventory, validating stability under heavy concurrent usage.',
    'Created cross-device and cloud integration plans for Indoor Mapping and Workplace Reservation & Scheduling, ensuring reliable real-time data synchronization across web and mobile platforms.',
    'Built scalable automation suites for Software Asset Management, Hardware Asset Management, Subscriptions Management, and Software Spend Analysis using Java, Selenium, JUnit, and Glide API.',
    'Developed Java and JavaScript automation that eliminated repetitive manual testing, reduced total test effort by 75%, and accelerated Jenkins CI/CD runs.'
]: bullet(text)

experience_header('Software Quality Assurance Engineer', '8x8, Inc.', 'San Jose, CA', 'Oct 2016 - Dec 2018')
for text in [
    'Built and maintained automated test suites for Salesforce-integrated back-office systems using Java, Selenium WebDriver, and TestNG.',
    'Automated REST API checks with Postman and integrated them into daily regression builds.',
    'Performed end-to-end functional, UAT, boundary, cross-browser, and integration testing across web applications.',
    'Owned features from early requirement discussions through production rollout and internal user training.'
]: bullet(text)

experience_header('Graduate Assistant', 'Lamar University', 'Beaumont, TX', 'Sep 2015 - Aug 2016')
bullet('Guided undergraduate students through coursework and labs in Java programming, data structures, and Android application development.')

experience_header('Software Development Engineer in Test (SDET)', 'OpenText Technologies', 'India', 'Feb 2013 - Jan 2015')
for text in [
    'Designed and built a keyword-driven automation framework using Java, Selenium WebDriver, and TestNG for OpenText Tempo Social.',
    'Executed comprehensive web and mobile test scenarios across Android, iOS, Windows, Linux, and OS X.',
    'Managed nightly Jenkins automation runs, repaired failed test scripts, and provided fast feedback to development teams.'
]: bullet(text)

heading('Education')
for degree, school, years in [
    ('M.S. - Computer Science', 'Lamar University | GPA: 3.75/4.0', '2015-2016'),
    ('B.Tech. - Electronics & Communication Engineering', "Vignan's University", '2009-2013')
]:
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.tab_stops.add_tab_stop(Inches(6.92), WD_TAB_ALIGNMENT.RIGHT)
    r = p.add_run(degree); set_font(r, 9.7, True)
    r = p.add_run(' (' + school + ')'); set_font(r, 9.7)
    r = p.add_run('\t' + years); set_font(r, 9.7)

# No page numbers, headers, footers, colors, or decorative furniture.
doc.core_properties.title = 'Parama Hamsa Vadlamudi - Quality Assurance Resume'
doc.core_properties.author = 'Parama Hamsa Vadlamudi'
doc.core_properties.subject = 'Software Quality Assurance Engineering'
doc.save(OUT)
print(OUT)
