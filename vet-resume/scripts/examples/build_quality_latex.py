from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[2]
TEMPLATE = SKILL_ROOT / "assets" / "templates" / "Canonical_Overleaf_Resume_Template.tex"
OUTPUT = Path.cwd() / "Parama_Hamsa_Vadlamudi_Quality_Engineer_Resume.tex"

template = TEMPLATE.read_text(encoding="utf-8")
preamble = template.split(r"\begin{document}", 1)[0]

body = r'''\begin{document}
    \newcommand{\AND}{\unskip
        \cleaders\copy\ANDbox\hskip\wd\ANDbox
        \ignorespaces
    }
    \newsavebox\ANDbox
    \sbox\ANDbox{$|$}

    \begin{header}
        \fontsize{25 pt}{25 pt}\selectfont Parama Hamsa Vadlamudi

        \vspace{5 pt}

        \normalsize
        \mbox{San Jose, CA}%
        \kern 5.0 pt%
        \AND%
        \kern 5.0 pt%
        \mbox{\hrefWithoutArrow{mailto:paramahamsa326@gmail.com}{paramahamsa326@gmail.com}}%
        \kern 5.0 pt%
        \AND%
        \kern 5.0 pt%
        \mbox{\hrefWithoutArrow{tel:+14096000518}{+1 409 600 0518}}%
    \end{header}

    \vspace{5 pt - 0.3 cm}

    \section{Professional Summary}
    \begin{onecolentry}
        Senior Software Quality Engineer with 11+ years of experience owning quality strategy, test automation, and release readiness across cloud platforms, mobile ecosystems, and AI/ML workflows. At ServiceNow, led end-to-end quality initiatives across Asset Management, Safe Workplace Apps, Workplace Service Delivery, and HR Service Delivery. Experienced in building scalable automation frameworks, strengthening CI/CD pipelines, and designing evaluation coverage for modern AI applications. Known for a proactive, engineering-minded approach to identifying risk early and delivering reliable, high-performing software.
    \end{onecolentry}

    \section{Core Skills}
    \begin{onecolentry}
        \textbf{Quality Leadership \& Strategy:} Test architecture, AI model and agent evaluation, release-risk assessment, defect triage, cross-team quality standards, Agile/Scrum
    \end{onecolentry}
    \vspace{0.1 cm}
    \begin{onecolentry}
        \textbf{Automation \& Tools:} Selenium WebDriver, JUnit, TestNG, Cypress, Playwright, Postman, Jenkins CI/CD pipelines, REST API testing
    \end{onecolentry}
    \vspace{0.1 cm}
    \begin{onecolentry}
        \textbf{Testing Scope:} AI/LLM workflows, RAG system validation, Android, Windows, web, mobile, and cloud testing; functional, regression, integration, performance, and reliability testing
    \end{onecolentry}
    \vspace{0.1 cm}
    \begin{onecolentry}
        \textbf{Languages \& Technologies:} Java, Python, JavaScript, SQL, Glide API, Node.js, React, HTML5/CSS3, Git/GitHub
    \end{onecolentry}

    \section{Work Experience}
    \begin{twocolentry}{
        \textbf{Jan 2018 -- Present}
    }
        \textbf{Senior Software Quality Engineer} \hspace{1.3cm}\textbf{ServiceNow Inc. -- San Jose, CA}
    \end{twocolentry}
    \vspace{0.05 cm}
    \begin{onecolentry}
        \textit{Promoted from Associate Software Quality Engineer}
    \end{onecolentry}
    \vspace{0.05 cm}
    \begin{onecolentry}
        \begin{highlights}
            \item Took ownership of quality strategy across multiple business units, leading test planning, release-risk evaluations, defect triage, and cross-team quality standards to support stable, predictable production releases.
            \item Designed and maintained test suites for complex workflows, multi-step agent actions, and contextual logic across HR Service Delivery and Safe Workplace Apps, including evaluation of accuracy, grounding, hallucination, latency, and safety behavior.
            \item Led quality strategy for HR Service Delivery products including Journey Designer, Life Cycle Events, HR Case Management, Opportunity Management, Talent Insights, Career Hub, Succession Planning, and EmployeeWorks, reducing post-launch issues by more than 40\%.
            \item Served as lead quality engineer for critical Safe Workplace applications, including Emergency Outreach, Contact Tracing, Vaccination Status, Safe Workplace Dashboard, Employee Readiness Survey, Health Screening, Travel Safety, Health and Safety Testing, and PPE Inventory, validating stability under heavy concurrent usage.
            \item Created cross-device and cloud integration plans for Indoor Mapping and Workplace Reservation \& Scheduling, ensuring reliable real-time data synchronization across web and mobile platforms.
            \item Built scalable automation suites for Software Asset Management, Hardware Asset Management, Subscriptions Management, and Software Spend Analysis using Java, Selenium, JUnit, and Glide API.
            \item Developed Java and JavaScript automation that eliminated repetitive manual testing, reduced total test effort by 75\%, and accelerated Jenkins CI/CD runs.
        \end{highlights}
    \end{onecolentry}

    \vspace{0.2 cm}
    \begin{twocolentry}{
        \textbf{Oct 2016 -- Dec 2018}
    }
        \textbf{Software Quality Assurance Engineer} \hspace{0.65cm}\textbf{8x8, Inc. -- San Jose, CA}
    \end{twocolentry}
    \vspace{0.05 cm}
    \begin{onecolentry}
        \begin{highlights}
            \item Built and maintained automated test suites for Salesforce-integrated back-office systems using Java, Selenium WebDriver, and TestNG.
            \item Automated REST API checks with Postman and integrated them into daily regression builds.
            \item Performed end-to-end functional, UAT, boundary, cross-browser, and integration testing across web applications.
            \item Owned features from early requirement discussions through production rollout and internal user training.
        \end{highlights}
    \end{onecolentry}

    \vspace{0.2 cm}
    \begin{twocolentry}{
        \textbf{Sep 2015 -- Aug 2016}
    }
        \textbf{Graduate Assistant} \hspace{3.0cm}\textbf{Lamar University -- Beaumont, TX}
    \end{twocolentry}
    \vspace{0.05 cm}
    \begin{onecolentry}
        \begin{highlights}
            \item Guided undergraduate students through coursework and labs in Java programming, data structures, and Android application development.
        \end{highlights}
    \end{onecolentry}

    \vspace{0.2 cm}
    \begin{twocolentry}{
        \textbf{Feb 2013 -- Jan 2015}
    }
        \textbf{Software Development Engineer in Test (SDET)} \hspace{0.35cm}\textbf{OpenText Technologies -- India}
    \end{twocolentry}
    \vspace{0.05 cm}
    \begin{onecolentry}
        \begin{highlights}
            \item Designed and built a keyword-driven automation framework using Java, Selenium WebDriver, and TestNG for OpenText Tempo Social.
            \item Executed comprehensive web and mobile test scenarios across Android, iOS, Windows, Linux, and OS X.
            \item Managed nightly Jenkins automation runs, repaired failed test scripts, and provided fast feedback to development teams.
        \end{highlights}
    \end{onecolentry}

    \section{Awards}
    \begin{twocolentry}{Mar 2022}
        \textbf{Customer Success Award} -- ServiceNow
    \end{twocolentry}
    \vspace{0.1 cm}
    \begin{twocolentry}{Oct 2020}
        \textbf{Innovation and Execution} -- ServiceNow
    \end{twocolentry}
    \vspace{0.1 cm}
    \begin{twocolentry}{Jul 2020}
        \textbf{Return to Work Apps} -- ServiceNow
    \end{twocolentry}
    \vspace{0.1 cm}
    \begin{twocolentry}{Jun 2020}
        \textbf{Win as a Team Award} -- ServiceNow
    \end{twocolentry}
    \vspace{0.1 cm}
    \begin{twocolentry}{Jan 2020}
        \textbf{Innovation Award} -- ServiceNow
    \end{twocolentry}

    \section{Education}
    \begin{twocolentry}{2015--2016}
        \textbf{M.S. -- Computer Science} (Lamar University, GPA: 3.75/4.0)
    \end{twocolentry}
    \begin{twocolentry}{2009--2013}
        \textbf{B.Tech. -- Electronics \& Communication Engineering} (Vignan's University)
    \end{twocolentry}

\end{document}
'''

OUTPUT.write_text(preamble + body, encoding="utf-8")
print(OUTPUT)
