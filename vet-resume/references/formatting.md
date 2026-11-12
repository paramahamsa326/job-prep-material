# Resume Formatting

## Canonical format

Use `../assets/templates/Canonical_Overleaf_Resume_Template.tex` for full-time LaTeX resumes.

- 10 pt US Letter; Charter font; 2 cm margins.
- Centered 25 pt name and single-line contact block.
- Preserve section rules, `twocolentry`, `onecolentry`, `highlights`, alignment, spacing, and black-only color.
- Preserve ATS support: T1 encoding, `glyphtounicode`, and `\pdfgentounicode=1`.
- No page numbers, headers, or footers.
- Keep full-time resumes to one page by selecting concise content, not changing geometry or typography.
- Contract resumes may use up to three pages but should retain the same visual system unless instructed otherwise.

## Allowed changes

Change summary wording, skills selection and order, experience bullet selection and wording, and target-role terminology. Keep all changes inside the document body.

## Prohibited without approval

Do not change the preamble, document class, packages, margins, fonts, header structure, section styling, bullet geometry, column widths, employer/date alignment, education layout, or technology layout.

## Validation

1. Compare the tailored `.tex` with the canonical template.
2. Treat formatting differences outside body content as errors.
3. Compile to PDF when a LaTeX compiler is available.
4. Inspect every rendered page for overflow, clipping, broken characters, and unintended layout drift.
5. When Word output is requested, reproduce the canonical appearance as closely as possible and identify the `.tex` version as authoritative.
