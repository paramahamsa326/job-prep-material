from pathlib import Path
import subprocess
import sys

ROOT = Path.cwd()
EXAMPLES_DIR = Path(__file__).resolve().parent
BASE = ROOT / "Parama_Hamsa_Vadlamudi_Quality_Engineer_Resume.tex"
OUT = ROOT / "Parama_Hamsa_Vadlamudi_Quality_Engineer_Resume_Updated.tex"

# Regenerate the known-good canonical-template version first.
subprocess.run([sys.executable, str(EXAMPLES_DIR / "build_quality_latex.py")], check=True)
text = BASE.read_text(encoding="utf-8")

# Move Core Skills after the complete Work Experience section.
skills_start = text.index(r"    \section{Core Skills}")
work_start = text.index(r"    \section{Work Experience}")
awards_start = text.index(r"    \section{Awards}")
skills_block = text[skills_start:work_start]
work_block = text[work_start:awards_start]
text = text[:skills_start] + work_block + skills_block + text[awards_start:]

# Strengthen ServiceNow engineering/tool-development coverage.
needle = r"""            \item Developed Java and JavaScript automation that eliminated repetitive manual testing, reduced total test effort by 75\%, and accelerated Jenkins CI/CD runs.
"""
replacement = needle + r"""            \item Built a Node.js and Nginx proxy-server tool to automate developer-instance configuration and deployment, reducing environment setup and onboarding time by 50\%.
            \item Developed reusable Java and JavaScript test utilities for data setup, UI validation, REST API checks, and Jenkins reporting, giving teams faster and more consistent release feedback.
"""
if needle not in text:
    raise RuntimeError("ServiceNow insertion point was not found")
text = text.replace(needle, replacement, 1)

# Elevate older roles to show quality-engineering ownership, architecture, and release accountability.
old_8x8 = r"""            \item Built and maintained automated test suites for Salesforce-integrated back-office systems using Java, Selenium WebDriver, and TestNG.
            \item Automated REST API checks with Postman and integrated them into daily regression builds.
            \item Performed end-to-end functional, UAT, boundary, cross-browser, and integration testing across web applications.
            \item Owned features from early requirement discussions through production rollout and internal user training.
"""
new_8x8 = r"""            \item Designed and maintained a Java, Selenium WebDriver, and TestNG automation suite for Salesforce-integrated back-office systems, improving repeatability across daily regression cycles.
            \item Built Postman collections for REST API validation, including positive, negative, boundary, and integration scenarios, and embedded them in daily regression builds.
            \item Owned end-to-end quality for web features through requirements analysis, test design, functional and UAT execution, defect triage, cross-browser validation, and production readiness.
            \item Partnered with developers and business stakeholders through rollout, root-cause analysis, and internal user training to resolve release risks early.
"""
if old_8x8 not in text:
    raise RuntimeError("8x8 block was not found")
text = text.replace(old_8x8, new_8x8, 1)

old_ot = r"""            \item Designed and built a keyword-driven automation framework using Java, Selenium WebDriver, and TestNG for OpenText Tempo Social.
            \item Executed comprehensive web and mobile test scenarios across Android, iOS, Windows, Linux, and OS X.
            \item Managed nightly Jenkins automation runs, repaired failed test scripts, and provided fast feedback to development teams.
"""
new_ot = r"""            \item Architected and built a keyword-driven automation framework using Java, Selenium WebDriver, and TestNG for OpenText Tempo Social, creating reusable components for maintainable regression coverage.
            \item Defined and executed functional, integration, compatibility, and end-to-end scenarios across web and mobile platforms, including Android, iOS, Windows, Linux, and OS X.
            \item Owned nightly Jenkins automation health, investigated failures, repaired unstable scripts, and worked with developers to distinguish product defects from test and environment issues.
            \item Reported release-quality status and actionable defect findings to development teams, shortening feedback cycles and improving build confidence.
"""
if old_ot not in text:
    raise RuntimeError("OpenText block was not found")
text = text.replace(old_ot, new_ot, 1)

OUT.write_text(text, encoding="utf-8")
print(OUT)
