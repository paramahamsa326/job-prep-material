---
name: vet-resume
description: Evaluate, tailor, format, and generate evidence-based resumes for Java/JavaScript full-time roles, Java contract roles, ServiceNow Developer roles, and software quality/SDET roles. Use when reviewing a resume, matching it to a job posting, selecting defensible bullets and technical skills, producing ATS-friendly LaTeX or Word output, or maintaining Parama Hamsa Vadlamudi's resume evidence without mixing role tracks or borrowing facts from reference resumes.
---

# Vet and Build Resumes

Keep context small. Read only the core reference plus the target track and task-specific guidance.

## Route the task

1. Read [references/review-rubric.md](references/review-rubric.md) for every review or rewrite.
2. For candidate-specific work, read [references/candidate/core-profile.md](references/candidate/core-profile.md).
3. Read exactly one primary track unless the user requests a comparison:
   - Java/JavaScript full-time: [references/candidate/java-full-time.md](references/candidate/java-full-time.md)
   - Java contract: [references/candidate/java-contract.md](references/candidate/java-contract.md)
   - ServiceNow Developer: [references/candidate/servicenow.md](references/candidate/servicenow.md)
   - Software quality/SDET: [references/candidate/quality-engineering.md](references/candidate/quality-engineering.md)
4. Read [references/java-engineering-patterns.md](references/java-engineering-patterns.md) only when evaluating or rewriting technical bullets.
5. Read [references/formatting.md](references/formatting.md) only when generating or checking a formatted resume.

Do not load job-application history, rendered pages, or store-room resumes unless the current task specifically needs them.

## Work from evidence

- Separate confirmed facts, draft claims, explicit exclusions, and verification questions.
- Preserve employers, titles, dates, education, ownership, technology versions, metrics, and tense.
- Do not infer ServiceNow platform expertise solely from employment at ServiceNow Inc.
- Do not promote a market keyword, proposed architecture, or friend's accomplishment into candidate experience.
- Resolve conflicting dates or titles with the user before producing a final resume.
- Use placeholders for missing metrics; never manufacture scale or results.

## Tailor the content

1. Classify requirements as must-have, preferred, or inferred.
2. Map each material requirement to strong, partial, absent, or unclear evidence.
3. Select the smallest set of bullets that proves role fit and seniority.
4. Connect tools to systems, decisions, constraints, and outcomes; avoid keyword chains.
5. Keep full-time resumes to one page through content selection. Allow contract resumes up to three pages when project detail is verified and useful.
6. Keep ServiceNow, Java/JavaScript, contract, and quality narratives separate.

## Generate files

- Use [assets/templates/Canonical_Overleaf_Resume_Template.tex](assets/templates/Canonical_Overleaf_Resume_Template.tex) as the authority for LaTeX formatting.
- Change body content only unless the user explicitly authorizes a redesign.
- Use `scripts/inspect_docx.py` for quick DOCX structure inspection.
- Treat `scripts/examples/` as prior builders to adapt, not canonical content or portable commands. Review hard-coded paths and candidate claims before running them.
- For DOCX or PDF creation and final layout checks, use the corresponding document or PDF skill and complete its render-and-inspect gate.

## Deliver

Provide the fit assessment, highest-impact changes, evidence gaps, and copy-ready revisions requested. For targeted work, include a concise requirement-to-evidence table. Before finalizing, verify every claim against the loaded candidate references and confirm the output uses the selected track only.
