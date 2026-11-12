from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether

OUT = r"Job_Applications\Parama_Hamsa_Vadlamudi_Visa_Senior_Software_Engineer.pdf"

navy = colors.HexColor("#17365D")
dark = colors.HexColor("#222222")
muted = colors.HexColor("#555555")
styles = getSampleStyleSheet()

name = ParagraphStyle("Name", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=20,
                      leading=23, textColor=navy, alignment=TA_CENTER, spaceAfter=4)
contact = ParagraphStyle("Contact", parent=styles["Normal"], fontName="Helvetica", fontSize=9,
                         leading=11, textColor=muted, alignment=TA_CENTER, spaceAfter=9)
section = ParagraphStyle("Section", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=11,
                         leading=13, textColor=navy, spaceBefore=7, spaceAfter=3,
                         borderWidth=0, borderPadding=0)
body = ParagraphStyle("Body", parent=styles["Normal"], fontName="Helvetica", fontSize=9.25,
                      leading=11.6, textColor=dark, spaceAfter=2.5)
role = ParagraphStyle("Role", parent=body, fontName="Helvetica-Bold", fontSize=9.65, leading=11.8,
                      spaceBefore=3.5, spaceAfter=1.8)
bullet = ParagraphStyle("Bullet", parent=body, leftIndent=12, firstLineIndent=-7, bulletIndent=2,
                        leading=11.5, spaceAfter=2.2)


def b(text):
    return Paragraph(text, bullet, bulletText="•")


story = [
    Paragraph("Parama Hamsa Vadlamudi", name),
    Paragraph(
        'Seattle, WA | Open to relocate | (409) 600-0518 | '
        '<link href="mailto:paramahamsa326@gmail.com" color="#17365D">paramahamsa326@gmail.com</link> | '
        '<link href="https://www.linkedin.com/in/paramvadlamudi" color="#17365D">linkedin.com/in/paramvadlamudi</link>',
        contact,
    ),
    Paragraph("PROFESSIONAL SUMMARY", section),
    Paragraph(
        "Senior Software Engineer with 10+ years of experience designing and operating highly available, "
        "secure enterprise platforms and event-driven microservices. Experienced in Java, Python, Go, AWS, "
        "Kubernetes, REST APIs, Kafka, SQL/NoSQL, observability, and AI-assisted development, with a record of "
        "leading architecture, delivery, and production reliability initiatives.", body),
    Paragraph("PROFESSIONAL EXPERIENCE", section),
    Paragraph("Senior Software Engineer | ServiceNow Inc. - Seattle, WA | Jan 2018-Present", role),
    b("Designed and delivered a cloud-native software asset lifecycle platform on AWS EKS using React, REST APIs, and AWS RDS, maintaining 99.95% uptime."),
    b("Built AI-assisted actions and contextual workflows backed by enterprise APIs and operational data, reducing manual HR case resolution turnaround time by 30%."),
    b("Led development of an ML-powered software-spend analytics system that classified transaction data, improved spend visibility, and identified license-optimization opportunities."),
    b("Designed the data model and workflow for hardware asset onboarding and reconciliation, improving inventory accuracy and supporting compliance reporting and spend optimization."),
    b("Developed secure service integrations using OAuth 2.0, AWS IAM, ACLs, and secrets management to protect sensitive data across enterprise and cloud boundaries."),
    b("Established incident-response practices and production monitoring with Prometheus, Grafana, Splunk, and PagerDuty; led design and code reviews to improve engineering quality."),
    b("Automated deployment and proxy configuration with Node.js and Nginx, cutting developer environment setup and onboarding time by 50%."),
    Paragraph("Software Developer | 8x8, Inc. - San Jose, CA | Sep 2016-Dec 2017", role),
    b("Built secure REST integrations across internal services and third-party platforms, and automated testing and delivery using JUnit, Mockito, Spring Test, Jenkins, Docker, and Kubernetes."),
    b("Developed content-moderation workflows and dashboards for policy review, approvals, rejections, and operational metrics."),
    Paragraph("Software Engineer | OpenText Pvt. Ltd. - Hyderabad, India | Feb 2013-Dec 2014", role),
    b("Improved peak-load response time by 10% by eliminating Hibernate N+1 queries and tuning SQL indexes and JDBC connection pools."),
    b("Developed moderation systems and dashboards to review content, enforce policy controls, and track approval and rejection metrics."),
    Paragraph("TECHNICAL SKILLS", section),
    Paragraph("<b>Languages:</b> Java, Python, Go, JavaScript, TypeScript", body),
    Paragraph("<b>Architecture & APIs:</b> Microservices, event-driven architecture, REST APIs, Spring Boot, Spring MVC, Spring Security, Hibernate", body),
    Paragraph("<b>Cloud & DevOps:</b> AWS, Amazon EKS, Docker, Kubernetes, Helm, Jenkins, CI/CD, Nginx", body),
    Paragraph("<b>Data & Messaging:</b> SQL, PostgreSQL, MongoDB, Redis, Pinecone, Apache Kafka", body),
    Paragraph("<b>Observability & Security:</b> Prometheus, Grafana, Splunk, OAuth 2.0, JWT, AWS IAM, ACLs, secrets management", body),
    Paragraph("<b>AI & Front End:</b> RAG, AI agents, Moveworks, Agent Studio, Codex, Copilot, Windsurf, React, Redux, Angular", body),
    Paragraph("EDUCATION", section),
    Paragraph("<b>M.S., Computer Science</b> - Lamar University | 2015-2016 &nbsp;&nbsp; <b>B.Tech., Electronics and Communication Engineering</b> - Vignan University | 2009-2013", body),
]

doc = SimpleDocTemplate(
    OUT, pagesize=letter, rightMargin=0.55*inch, leftMargin=0.55*inch,
    topMargin=0.42*inch, bottomMargin=0.40*inch,
    title="Parama Hamsa Vadlamudi - Senior Software Engineer",
    author="Parama Hamsa Vadlamudi",
)
doc.build(story)
print(OUT)
