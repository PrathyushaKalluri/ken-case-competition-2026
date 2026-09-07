from pathlib import Path
import re, html, json
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Flowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/pdf'
OUT.mkdir(parents=True, exist_ok=True)
FONT = Path('/System/Library/Fonts/Supplemental')
pdfmetrics.registerFont(TTFont('ReportSans', str(FONT/'Arial.ttf')))
pdfmetrics.registerFont(TTFont('ReportSansBold', str(FONT/'Arial Bold.ttf')))
pdfmetrics.registerFontFamily('ReportSans', normal='ReportSans', bold='ReportSansBold', italic='ReportSans', boldItalic='ReportSansBold')
ink = HexColor('#16302e'); teal = HexColor('#176f67'); muted = HexColor('#516665')
styles = {
 'body': ParagraphStyle('body', fontName='ReportSans', fontSize=10.2, leading=13.5, textColor=ink, spaceAfter=7),
 'h1': ParagraphStyle('h1', fontName='ReportSansBold', fontSize=23, leading=27, textColor=ink, spaceAfter=17),
 'h2': ParagraphStyle('h2', fontName='ReportSansBold', fontSize=13, leading=17, textColor=teal, spaceAfter=12),
 'h3': ParagraphStyle('h3', fontName='ReportSansBold', fontSize=12, leading=16, textColor=teal, spaceBefore=5, spaceAfter=8),
}

def fmt(s):
 s = html.escape(s)
 s = re.sub(r'\[([^\]]+)\]\((https?://[^\s)]+)\)', r'<link href="\2" color="#176f67"><u>\1</u></link>', s)
 s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
 return s

class Sprint(Flowable):
 def __init__(self):
  Flowable.__init__(self); self.width=487; self.height=78
 def draw(self):
  c=self.canv
  labels=[('DAY 1','Evidence','Answers 01 + 02'),('DAY 2','Design','Loop + rail ask'),('DAY 3','Submit','Verify + receipt')]
  for i,(day,title,sub) in enumerate(labels):
   x=i*166
   c.setFillColor(HexColor('#edf5f1')); c.roundRect(x,6,155,68,6,fill=1,stroke=0)
   c.setFillColor(teal); c.setFont('ReportSansBold',9); c.drawString(x+11,59,day)
   c.setFillColor(ink); c.setFont('ReportSansBold',13); c.drawString(x+11,39,title)
   c.setFont('ReportSans',9); c.drawString(x+11,21,sub)

def footer(c,doc):
 c.saveState(); c.setFillColor(muted); c.setFont('ReportSans',8)
 c.drawString(54,30,'THE KEN 2026  /  TEAM RESEARCH PLAYBOOK  /  7 SEP 2026')
 c.drawRightString(A4[0]-54,30,str(doc.page)); c.restoreState()

source=(ROOT/'research/report-source.md').read_text()
story=[]
for section_i,section in enumerate(source.split('---PAGE---')):
 if section_i: story.append(PageBreak())
 for block in re.split(r'\n\s*\n',section.strip()):
  if block.startswith('# '):
   # First section has consecutive title/subtitle lines.
   for line in block.splitlines():
    level='h2' if line.startswith('## ') else 'h1'
    story.append(Paragraph(fmt(line.lstrip('# ')),styles[level]))
  elif block.startswith('### '): story.append(Paragraph(fmt(block[4:]),styles['h3']))
  elif block.startswith('## '): story.append(Paragraph(fmt(block[3:]),styles['h2']))
  else:
   lines=block.splitlines()
   if len(lines)>1 and all(re.match(r'^\d+\.',l) for l in lines):
    for l in lines: story.append(Paragraph(fmt(l),styles['body']))
   else: story.append(Paragraph(fmt(' '.join(lines)),styles['body']))
  if section_i==0 and block.startswith('### The three-day'):
   story.append(Sprint()); story.append(Spacer(1,8))

target=OUT/'Ken_2026_Research_and_Submission_Playbook.pdf'
doc=SimpleDocTemplate(str(target),pagesize=A4,rightMargin=54,leftMargin=54,topMargin=47,bottomMargin=49,
 title='The Ken 2026 - Keeping the machines running: research and submission playbook',author='Team research workspace')
doc.build(story,onFirstPage=footer,onLaterPages=footer)

# Internal provenance ledger: URLs with their immediate claim context.
records=[]
for block in re.split(r'\n\s*\n',source):
 for title,url in re.findall(r'\[([^\]]+)\]\((https?://[^\s)]+)\)',block):
  records.append({'source_title':title,'url':url,'accessed':'2026-09-07','publication_date':'not always stated; see original',
    'claim_context':block,'access_notes':'Direct public HTML or web retrieval; no sandbox execution. Prototype content read, not interactively tested.'})
(ROOT/'research/claim-source-ledger.json').write_text(json.dumps(records,indent=2))
print(target)
