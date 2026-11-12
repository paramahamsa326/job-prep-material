from docx import Document
from pathlib import Path
import sys

p = Path(sys.argv[1])
d = Document(p)
print(f'paragraphs={len(d.paragraphs)} tables={len(d.tables)} sections={len(d.sections)}')
for i, para in enumerate(d.paragraphs):
    text = para.text.replace('\t', ' <TAB> ').strip()
    if text:
        pf = para.paragraph_format
        print(f'P{i:03d}|style={para.style.name}|align={para.alignment}|before={pf.space_before}|after={pf.space_after}|line={pf.line_spacing}|{text[:240]}')
for ti, table in enumerate(d.tables):
    print(f'TABLE {ti} rows={len(table.rows)} cols={len(table.columns)}')
    for ri, row in enumerate(table.rows[:20]):
        print('  R%02d: %s' % (ri, ' || '.join(c.text.replace('\n',' / ')[:180] for c in row.cells)))
