import glob, sys, os, subprocess, textwrap
from PIL import Image
import numpy as np
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from playwright.sync_api import sync_playwright
# usage: make_pdf.py <Laxminotebook subfolder> "<footer label>" <out.pdf>
FOLDER, LABEL, OUTPDF = sys.argv[1], sys.argv[2], sys.argv[3]
WD = 'work_' + FOLDER
os.makedirs(WD + '/notes', exist_ok=True); os.makedirs(WD + '/ras', exist_ok=True)
SRC = '/home/user/Dice/Laxminotebook/' + FOLDER
CSS = """html,body{margin:0!important;padding:0!important;background:#fff!important;width:680px!important}
#vis-container{margin:0!important;padding:0!important;max-width:none!important;width:680px!important}
svg.n{display:block;width:680px!important;height:auto!important;margin:0!important}@page{margin:0}"""
htmls = [f for f in sorted(glob.glob(SRC + '/[0-9][0-9]_*.html')) if not os.path.basename(f).startswith('99_')]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    pg = b.new_page(viewport={'width': 680, 'height': 1000})
    for f in htmls:
        pg.goto('file://' + f, wait_until='networkidle'); pg.add_style_tag(content=CSS); pg.evaluate("document.fonts.ready")
        r = pg.evaluate("(()=>{const s=document.querySelector('svg.n').getBoundingClientRect();return [s.y,s.height]})()")
        out = WD + '/notes/' + os.path.basename(f)[:-5] + '.pdf'
        pg.pdf(path=out, width='680px', height=f'{r[0]+r[1]+1:.0f}px', print_background=True, margin={'top':'0','bottom':'0','left':'0','right':'0'})
        subprocess.run(['pdftoppm', '-r', '144', '-gray', '-png', '-singlefile', out, WD + '/ras/' + os.path.basename(out)[:-4]], check=True)
W,H = 595.28, 841.89
M=14.0; G=12; FOOT=12; MINSLICE=60
colw=(W-2*M-G)/2; colh=H-2*M-FOOT
files=sorted(glob.glob(WD+'/notes/*.pdf'))
notes=[]
for f in files:
    x=pagexobj(PdfReader(f).pages[0]); w=float(x.BBox[2]); h=float(x.BBox[3])
    a=np.asarray(Image.open(WD+'/ras/'+os.path.basename(f)[:-4]+'.png').convert('L')).astype(int)
    rpp=a.shape[0]/h  # raster rows per pt
    blank=(a.max(1)-a.min(1))<25   # uniform row
    # a cut row (in pt) is safe if a band of +-3pt around it is blank
    safe=np.zeros(int(h)+1,bool)
    for y in range(int(h)+1):
        r0=int(max(0,(y-3)*rpp)); r1=int(min(a.shape[0],(y+3)*rpp))
        safe[y]=blank[r0:r1].all()
    notes.append((x,w,h,safe))
s=colw/510
pieces=[]; page=0; col=0; y=0  # y = used height in column (page pt)
def advance():
    global page,col,y
    col+=1; y=0
    if col==2: col=0; page+=1
for idx,(x,w,h,safe) in enumerate(notes):
    top=0.0
    if y>0: y+=8  # gap between notes
    while True:
        rem=colh-y
        need=(h-top)*s
        if need<=rem:
            pieces.append((page,col,y,idx,top,h)); y+=need; break
        # find safe cut <= top+rem/s
        lim=int(top+rem/s)
        cut=None
        for c in range(lim, int(top+MINSLICE/s), -1):
            if c<len(safe) and safe[c]: cut=c; break
        if cut is None:
            advance(); continue
        pieces.append((page,col,y,idx,top,cut)); top=cut; advance()
npages=page+2   # + final reminder page
print('pages',npages,'scale',round(s*0.75*680/680/0.75,3))
c=canvas.Canvas(OUTPDF,pagesize=(W,H))
c.setTitle('Laxmikanth '+LABEL+' Notes')
for p in range(npages-1):
    for (pg,col,y,idx,t,b) in pieces:
        if pg!=p: continue
        x,w,h,_=notes[idx]
        X=M+col*(colw+G); Ytop=H-M-y
        c.saveState()
        p_=c.beginPath(); p_.rect(X, Ytop-(b-t)*s, colw, (b-t)*s); c.clipPath(p_,stroke=0,fill=0)
        c.translate(X, Ytop-(h-t)*s); c.scale(s,s); c.doForm(makerl(c,x))
        c.restoreState()
    c.setStrokeGray(0.75); c.setLineWidth(0.5); c.line(W/2, M+FOOT, W/2, H-M)
    c.setFont('Helvetica',7.5); c.setFillGray(0.45)
    c.drawCentredString(W/2, M-2, f'Laxmikanth {LABEL}   |   Page {p+1} of {npages}')
    c.showPage()


# ---- final page: reminder about tables, large text ----
pdfmetrics.registerFont(TTFont('KalamB', '/root/.fonts/Kalam-700.ttf'))
NOTE = ('Please check the tables of this chapter once. If a table looks important, study it directly '
        'from Laxmikanth, or take a screenshot of it and add it to this page as needed.')
lines = textwrap.wrap(NOTE, 30)
c.setStrokeColorRGB(0.85, 0.23, 0.23); c.setLineWidth(1.5); c.setDash(8, 5)
c.roundRect(40, 60, W-80, H-120, 10, stroke=1, fill=0); c.setDash()
c.setFillColorRGB(0.85, 0.23, 0.23); c.setFont('KalamB', 30)
y = H - 150
for ln in lines:
    c.drawCentredString(W/2, y, ln); y -= 44
c.setFont('Helvetica', 7.5); c.setFillGray(0.45)
c.drawCentredString(W/2, M-2, f'Laxmikanth {LABEL}   |   Page {npages} of {npages}')
c.showPage()
c.save()
