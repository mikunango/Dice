"""Notebook-style SVG note builder (matches Laxminotebook Ch.23 pen style).

Inline markup:  {r:red text}  {b:blue text}  {R:bold red}  {B:bold blue}  {K:bold black}
Plain text is black.  Superscript footnote markers: write ¹ ² ³ᵃ etc.
"""
import re, html, os
from PIL import ImageFont

FONT_DIR = '/root/.fonts'
_fonts = {}
def font(size, bold=False):
    k = (size, bold)
    if k not in _fonts:
        _fonts[k] = ImageFont.truetype(os.path.join(FONT_DIR, 'Kalam-700.ttf' if bold else 'Kalam-400.ttf'), size)
    return _fonts[k]

def tw(text, size=15, bold=False):
    return font(size, bold).getlength(text)

RED, BLUE = '#D93A3A', '#2F6FDB'

# per-note line headings: LABELS[note_title] = [label, label, ...] consumed in order
LABELS = {}
DUMP = []          # (note_title, sentence) for every line that needs a heading
USE_LABELS = True
INLINE_ONLY = False   # new chapters: keywords only where written as [[kw]]
CLS = {'k': 'k', 'r': 'r', 'b': 'b', 'R': 'r', 'B': 'b', 'K': 'k', 'H': 'h'}
BOLD = set('RBKH')

def parse(markup):
    """-> list of (text, style) runs"""
    runs = []
    pos = 0
    for m in re.finditer(r'\{([rbRBKH]):(.*?)\}', markup):
        if m.start() > pos:
            runs.append((markup[pos:m.start()], 'k'))
        runs.append((m.group(2), m.group(1)))
        pos = m.end()
    if pos < len(markup):
        runs.append((markup[pos:], 'k'))
    return runs

KW_RE = re.compile(r'^\s*\[\[(.+?)\]\]\s*')
MISSING = []

def split_kw(markup):
    """'[[Keyword]] text' -> ('Keyword', 'text')"""
    m = KW_RE.match(markup)
    return (m.group(1), markup[m.end():]) if m else (None, markup)

def plain(markup):
    return ''.join(t for t, _ in parse(markup))

def wrap(markup, maxw, size=15):
    """Greedy word wrap of styled runs -> list of lines (each list of (text, style))."""
    maxw = maxw * 0.975 - 6
    words = []  # (word, style, space_before)
    sp = False
    for text, st in parse(markup):
        parts = re.split(r'(\s+)', text)
        for p in parts:
            if p == '':
                continue
            if p.isspace():
                sp = True
                continue
            words.append([p, st, sp])
            sp = False
    # first word of each run without space joins previous word (e.g. "word{r:x}")
    lines, cur, curw = [], [], 0.0
    brk = 0  # index in cur where the current (glued) word chain starts
    for i, (w, st, sp) in enumerate(words):
        glue = (not sp) and i > 0
        piece = (' ' if (sp and cur) else '') + w
        wpx = tw(piece, size, st in BOLD)
        if cur and curw + wpx > maxw and (not glue or brk > 0):
            if glue:
                tail = cur[brk:]
                lines.append(cur[:brk])
                t0, s0 = tail[0]
                tail[0] = (t0.lstrip(' '), s0)
                cur = tail + [(w, st)]
            else:
                lines.append(cur); cur = [(w, st)]
            curw = sum(tw(t, size, s in BOLD) for t, s in cur)
            brk = 0
        else:
            if not glue:
                brk = len(cur)
            cur.append((piece if cur else w, st)); curw += wpx
    if cur:
        lines.append(cur)
    # merge same-style neighbours
    out = []
    for ln in lines:
        m = []
        for t, st in ln:
            if m and m[-1][1] == st:
                m[-1] = (m[-1][0] + t, st)
            else:
                m.append((t, st))
        out.append(m)
    return out

def esc(s):
    return html.escape(s, quote=False)

def tspans(line):
    o = []
    for t, st in line:
        style = ' style="font-weight:700"' if st in BOLD else ''
        o.append(f'<tspan class="{CLS[st]}"{style}>{esc(t)}</tspan>')
    return ''.join(o)


class Note:
    W = 680
    L = 40          # left margin
    R = 640         # right edge
    LH = 22         # line height

    def __init__(self, title, desc=''):
        self.title = title
        self.desc = desc or title
        self.el = []
        self.y = 26
        self.src = []      # book text registered for the completeness check
        self.fsrc = []     # footnote text
        self._li = 0
        self._title(title)

    def label(self, sentence):
        """Next heading for a non-original line (None if labels off / not provided)."""
        DUMP.append((self.title, plain(sentence)))
        labs = LABELS.get(self.title)
        if not USE_LABELS or labs is None:
            MISSING.append((self.title, plain(sentence)[:70]))
            return None
        i = self._li
        self._li += 1
        return labs[i] if i < len(labs) else '??'

    # ---------- registration ----------
    def reg(self, markup):
        self.src.append(plain(markup))

    # ---------- primitives ----------
    def _title(self, t):
        w = tw(t, 17, True) + 60
        x = (self.W - w) / 2
        self.el.append(f'<rect x="{x:.0f}" y="26" width="{w:.0f}" height="40" rx="3" fill="none" stroke="{RED}" stroke-width="1.5"/>')
        self.el.append(f'<text class="r hd" x="340" y="53" text-anchor="middle">{esc(t)}</text>')
        self.y = 66

    def gap(self, h=10):
        self.y += h

    def rule(self):
        self.y += 14
        self.el.append(f'<line x1="30" y1="{self.y}" x2="650" y2="{self.y}" stroke="var(--text-secondary)" stroke-width="0.8"/>')
        self.y += 6

    def section(self, t, src=True):
        """Major red heading with red underline (e.g. LEGISLATIVE RELATIONS)."""
        self.y += 34
        self.el.append(f'<text class="r hd" x="{self.L}" y="{self.y}">{esc(t)}</text>')
        self.el.append(f'<line x1="{self.L}" y1="{self.y+6}" x2="{self.L + tw(t,17,True):.0f}" y2="{self.y+6}" stroke="{RED}" stroke-width="1"/>')
        self.y += 6
        if src: self.reg(t)

    def sub(self, t, src=True):
        """Black bold underlined sub-heading (e.g. 1. Territorial Extent ...)."""
        self.y += 32
        self.el.append(f'<text class="lb" x="{self.L}" y="{self.y}">{esc(t)}</text>')
        self.y += 2
        if src: self.reg(t)

    def subsub(self, t, src=True):
        """Red bold sub-sub heading (e.g. A. When Rajya Sabha Passes a Resolution)."""
        self.y += 28
        for i, ln in enumerate(wrap('{R:' + t + '}', self.R - self.L, 16)):
            if i: self.y += 20
            self.el.append(f'<text class="sh" x="{self.L}" y="{self.y}">{tspans(ln)}</text>')
        self.y += 2
        if src: self.reg(t)

    def text(self, markup, x=None, size=15, src=True, maxw=None, lh=None):
        x = self.L if x is None else x
        maxw = maxw or (self.R - x)
        lh = lh or self.LH
        for i, ln in enumerate(wrap(markup, maxw, size)):
            self.y += lh
            cls = ' class="sm"' if size == 14 else (' class="xs"' if size == 13 else '')
            self.el.append(f'<text{cls} x="{x:.0f}" y="{self.y}">{tspans(ln)}</text>')
        if src: self.reg(markup)

    def bullets(self, items, level=0, src=True, sym='•', size=15, orig=False):
        """orig=True: Laxmikanth's own bullet list (kept as •).
        Otherwise every line starts with its own short heading 'Label:' instead of a bullet."""
        bx = self.L + 4 + level * 26
        lh = self.LH if size == 15 else 20
        cls = ' class="sm"' if size == 14 else ''
        for it in items:
            self.y += 6
            kw, it = split_kw(it)
            pre = ''
            if kw and kw.startswith('!'):
                kw = kw[1:]; pre = kw + ' '
            lab = None if orig else (kw or self.label(it))
            if lab:
                lines = wrap('{H:' + lab.rstrip(':') + ':} ' + it, self.R - bx, size)
                for i, ln in enumerate(lines):
                    self.y += lh
                    self.el.append(f'<text{cls} x="{bx + (0 if i == 0 else 12)}" y="{self.y}">{tspans(ln)}</text>')
            else:
                tx = bx + 14
                for i, ln in enumerate(wrap(it, self.R - tx, size)):
                    self.y += lh
                    if i == 0:
                        col = RED if level == 0 else BLUE
                        self.el.append(f'<text x="{bx}" y="{self.y}" style="fill:{col};font-weight:700">{sym}</text>')
                    self.el.append(f'<text{cls} x="{tx}" y="{self.y}">{tspans(ln)}</text>')
            if src: self.reg(pre + it)

    def para(self, markup, level=0, src=True):
        """A book paragraph -> kept whole, one keyword bulletpoint at its start."""
        self.bullets([markup], level, src)

    def items(self, items, src=True, bracket=True, indent=0, size=15, kw=True):
        """Enumerated list: items are (label, markup). Red bracket on the left."""
        x0 = self.L + 4 + indent
        lw = max(tw(l + ' ', size, True) for l, _ in items) + 4
        tx = x0 + 12 + lw
        top = self.y + 6
        lh = self.LH if size == 15 else 20
        cls = ' class="sm"' if size == 14 else ''
        avg_words = sum(len(plain(split_kw(it)[1]).split()) for _, it in items) / max(len(items), 1)
        for lab, it in items:
            self.y += 4
            ikw, it = split_kw(it)
            pre = ''
            if ikw and ikw.startswith('!'):
                ikw = ikw[1:]; pre = ikw + ' '
            sents = [it]
            if ikw:
                sents = ['{H:' + ikw.rstrip(':') + ':} ' + it]
            elif kw and avg_words >= 10 and INLINE_ONLY:
                MISSING.append((self.title, 'ITEM ' + lab + ' ' + plain(it)[:62]))
            elif kw and avg_words >= 10 and not INLINE_ONLY:
                kl = self.label(it)
                if kl:
                    sents = ['{H:' + kl + ':} ' + it]
            for s_i, s in enumerate(sents):
                sx = tx
                if s_i:
                    self.y += 3
                    hl = self.label(s)
                    s = ('{H:' + hl.rstrip(':') + ':} ' + s) if hl else s
                for i, ln in enumerate(wrap(s, self.R - sx - (12 if s_i else 0), size)):
                    self.y += lh
                    if i == 0 and s_i == 0:
                        self.el.append(f'<text x="{x0+12}" y="{self.y}" class="r" style="font-weight:700">{esc(lab)}</text>')
                    self.el.append(f'<text{cls} x="{sx + (12 if (s_i and i) else 0):.0f}" y="{self.y}">{tspans(ln)}</text>')
            if src: self.reg(lab + ' ' + pre + it)
        bot = self.y + 6
        if bracket:
            self.el.append(f'<path d="M{x0+6} {top} L{x0} {top} L{x0} {bot} L{x0+6} {bot}" fill="none" stroke="{RED}" stroke-width="1.6"/>')

    def cont(self, markup):
        """Continuation of the same paragraph (no new keyword bulletpoint)."""
        self.y += 2
        self.text(markup, x=self.L + 16)

    def listpara(self, intro, items, outro=None, cont=False, kw=True):
        """Paragraph containing an inline (i)/(ii) list -> intro + item list (+ closing words)."""
        if cont:
            self.cont(intro)
        else:
            self.bullets([intro])
        self.items(items, indent=14, kw=kw)
        if outro:
            self.text(outro, x=self.L + 18)

    def quote(self, markup, src=True, by=None):
        """Quotation: blue bar on the left, one bullet per sentence."""
        top = self.y + 8
        sents = [markup]
        self.y += 2
        x = self.L + 16
        for s in sents:
            self.y += 4
            qkw, s = split_kw(s)
            hl = qkw or self.label(s)
            s2 = ('{H:' + hl.rstrip(':') + ':} ' + s) if hl else s
            for i, ln in enumerate(wrap(s2, self.R - x - 14, 15)):
                self.y += self.LH
                self.el.append(f'<text x="{x + (12 if i else 0)}" y="{self.y}">{tspans(ln)}</text>')
        bot = self.y + 8
        self.el.append(f'<line x1="{self.L+4}" y1="{top}" x2="{self.L+4}" y2="{bot}" stroke="{BLUE}" stroke-width="3" stroke-linecap="round"/>')
        self.y = bot
        if src: self.reg(split_kw(markup)[1])

    def arrow(self, markup, x=None, src=False, size=14):
        """Down arrow from previous line, then a short note beside its tip."""
        x = (self.L + 20) if x is None else x
        y0 = self.y + 6
        self.el.append(f'<line class="ln" x1="{x}" y1="{y0}" x2="{x}" y2="{y0+16}" marker-end="url(#ah)"/>')
        self.y = y0 + 16
        right = x > 420
        maxw = (x - 12 - self.L) if right else (self.R - x - 14)
        lines = wrap(markup, maxw, size)
        cls = ' class="sm"' if size == 14 else ''
        for i, ln in enumerate(lines):
            yy = self.y + 16 + i * 19
            if right:
                self.el.append(f'<text{cls} x="{x-10}" y="{yy}" text-anchor="end">{tspans(ln)}</text>')
            else:
                self.el.append(f'<text{cls} x="{x+12}" y="{yy}">{tspans(ln)}</text>')
        self.y += 16 + (len(lines) - 1) * 19 + 4
        if src: self.reg(markup)

    def tree(self, labels, root_x=None, size=14, src=False, lw=None):
        """Branching arrows from a point down to N labels (centred)."""
        n = len(labels)
        span = self.R - self.L
        cw = span / n
        xs = [self.L + cw * (i + 0.5) for i in range(n)]
        rx = (self.L + self.R) / 2 if root_x is None else root_x
        y0 = self.y + 6
        y1 = y0 + 12
        self.el.append(f'<line class="ln" x1="{rx:.0f}" y1="{y0}" x2="{rx:.0f}" y2="{y1}"/>')
        if n > 1:
            self.el.append(f'<line class="ln" x1="{min(xs+[rx]):.0f}" y1="{y1}" x2="{max(xs+[rx]):.0f}" y2="{y1}"/>')
        for x in xs:
            self.el.append(f'<line class="ln" x1="{x:.0f}" y1="{y1}" x2="{x:.0f}" y2="{y1+16}" marker-end="url(#ah)"/>')
        maxl = 0
        for x, lab in zip(xs, labels):
            lines = wrap(lab, (lw or cw) - 8, size)
            for i, ln in enumerate(lines):
                yy = y1 + 36 + i * 18
                self.el.append(f'<text class="{"sm" if size==14 else "xs"}" x="{x:.0f}" y="{yy}" text-anchor="middle">{tspans(ln)}</text>')
            maxl = max(maxl, len(lines))
            if src: self.reg(lab)
        self.y = y1 + 36 + (maxl - 1) * 18 + 4

    def boxes(self, boxes, size=14, src=False, h=None, gap=10, color=RED, x0=None, x1=None):
        """Row of red-outlined boxes; each box is a list of markup lines (wrapped)."""
        x0 = self.L if x0 is None else x0
        x1 = self.R if x1 is None else x1
        n = len(boxes)
        bw = (x1 - x0 - gap * (n - 1)) / n
        wrapped = []
        for b in boxes:
            lines = []
            for m in b:
                lines += wrap(m, bw - 12, size)
            wrapped.append(lines)
        maxl = max(len(l) for l in wrapped)
        bh = h or (maxl * 18 + 14)
        top = self.y + 12
        for i, lines in enumerate(wrapped):
            x = x0 + i * (bw + gap)
            self.el.append(f'<rect class="bx" x="{x:.0f}" y="{top}" width="{bw:.0f}" height="{bh}" rx="3" style="stroke:{color}"/>')
            start = top + (bh - len(lines) * 18) / 2 + 13
            for j, ln in enumerate(lines):
                self.el.append(f'<text class="{"sm" if size==14 else "xs"}" x="{x+bw/2:.0f}" y="{start + j*18:.0f}" text-anchor="middle">{tspans(ln)}</text>')
            if src:
                for m in boxes[i]: self.reg(m)
        self.y = top + bh
        return [(x0 + i * (bw + gap), bw) for i in range(n)]

    def flow(self, labels, size=14, src=False, sep='arrow'):
        """Boxes linked left->right with arrows (wraps to next row if too wide)."""
        pad, ag = 14, 26
        widths = [min(tw(plain(l), size) + pad * 2, 260) for l in labels]
        rows, cur, cw = [], [], 0
        for l, w in zip(labels, widths):
            if cur and cw + ag + w > self.R - self.L:
                rows.append(cur); cur, cw = [], 0
            cur.append((l, w)); cw += (ag if len(cur) > 1 else 0) + w
        rows.append(cur)
        for r_i, row in enumerate(rows):
            total = sum(w for _, w in row) + ag * (len(row) - 1)
            x = self.L + (self.R - self.L - total) / 2
            wr = [wrap(l, w - 10, size) for l, w in row]
            bh = max(len(w) for w in wr) * 18 + 12
            top = self.y + 12
            if r_i:
                cx = (self.L + self.R) / 2
                self.el.append(f'<line class="ln" x1="{cx:.0f}" y1="{self.y+1}" x2="{cx:.0f}" y2="{self.y+22}" marker-end="url(#ah)"/>')
                top = self.y + 24
            for k, ((l, w), lines) in enumerate(zip(row, wr)):
                self.el.append(f'<rect class="bx" x="{x:.0f}" y="{top}" width="{w:.0f}" height="{bh}" rx="3"/>')
                st = top + (bh - len(lines) * 18) / 2 + 13
                for j, ln in enumerate(lines):
                    self.el.append(f'<text class="sm" x="{x+w/2:.0f}" y="{st+j*18:.0f}" text-anchor="middle">{tspans(ln)}</text>')
                if k < len(row) - 1:
                    if sep == 'arrow':
                        self.el.append(f'<line class="ln" x1="{x+w+3:.0f}" y1="{top+bh/2:.0f}" x2="{x+w+ag-3:.0f}" y2="{top+bh/2:.0f}" marker-end="url(#ah)"/>')
                    else:
                        self.el.append(f'<text class="r" x="{x+w+ag/2:.0f}" y="{top+bh/2+5:.0f}" text-anchor="middle" style="font-weight:700">{esc(sep)}</text>')
                x += w + ag
                if src: self.reg(l)
            self.y = top + bh

    def compare(self, cols, size=14, src=False, heads_color=RED):
        """Side-by-side columns: cols = [(head_markup, [line_markup,...]), ...] with divider lines."""
        n = len(cols)
        cw = (self.R - self.L) / n
        top = self.y + 14
        maxy = top
        for i, (head, lines) in enumerate(cols):
            x = self.L + i * cw
            hl = wrap(head, cw - 20, 14)
            hh = len(hl) * 18 + 10
            self.el.append(f'<rect class="bx" x="{x+6:.0f}" y="{top}" width="{cw-12:.0f}" height="{hh}" rx="3"/>')
            for j, ln in enumerate(hl):
                self.el.append(f'<text class="sm" x="{x+cw/2:.0f}" y="{top+18+j*18}" text-anchor="middle">{tspans(ln)}</text>')
            yy = top + hh + 4
            self.el.append(f'<line class="ln" x1="{x+cw/2:.0f}" y1="{top+hh}" x2="{x+cw/2:.0f}" y2="{yy+10}" marker-end="url(#ah)"/>')
            yy += 12
            for m in lines:
                for k, ln in enumerate(wrap(m, cw - 20, size)):
                    yy += 19
                    self.el.append(f'<text class="sm" x="{x+cw/2:.0f}" y="{yy}" text-anchor="middle">{tspans(ln)}</text>')
                yy += 3
                if src: self.reg(m)
            maxy = max(maxy, yy)
            if i:
                self.el.append(f'<line x1="{x:.0f}" y1="{top}" x2="{x:.0f}" y2="{maxy}" stroke="var(--text-secondary)" stroke-width="0.6" stroke-dasharray="4 3"/>')
        self.y = maxy + 6

    def table(self, head, rows, widths, src=True, size=14, caption=None, group_rows=()):
        """Grid table. rows: list of lists of markup. group_rows: indexes rendered as full-width red band."""
        if caption:
            self.y += 30
            for i, ln in enumerate(wrap('{R:' + caption + '}', self.R - self.L, 15)):
                if i: self.y += 20
                self.el.append(f'<text x="{self.L}" y="{self.y}">{tspans(ln)}</text>')
            if src: self.reg(caption)
        top = self.y + 10
        xs = [self.L]
        for w in widths: xs.append(xs[-1] + w)
        y = top
        def row(cells, hdr=False):
            nonlocal y
            wr = [wrap(c, w - 14, size) for c, w in zip(cells, widths)]
            h = max(len(w) for w in wr) * 19 + 12
            for c, lines in enumerate(wr):
                for j, ln in enumerate(lines):
                    anchor = ' text-anchor="middle"' if hdr else ''
                    xx = (xs[c] + xs[c+1]) / 2 if hdr else xs[c] + 7
                    self.el.append(f'<text class="sm" x="{xx:.0f}" y="{y+20+j*19}"{anchor}>{tspans(ln)}</text>')
            y += h
            self.el.append(f'<line class="gx" x1="{xs[0]}" y1="{y}" x2="{xs[-1]}" y2="{y}"/>')
            return h
        row(head, True)
        if src: self.reg(' '.join(head))
        vstarts = []
        for i, r in enumerate(rows):
            if i in group_rows:
                h = 30
                self.el.append(f'<rect x="{xs[0]}" y="{y}" width="{xs[-1]-xs[0]}" height="{h}" fill="#D93A3A" fill-opacity="0.08"/>')
                self.el.append(f'<text class="sm" x="{(xs[0]+xs[-1])/2:.0f}" y="{y+20}" text-anchor="middle">{tspans([(plain(r[0]), "R")])}</text>')
                y += h
                self.el.append(f'<line class="gx" x1="{xs[0]}" y1="{y}" x2="{xs[-1]}" y2="{y}"/>')
                vstarts.append(('g', y - h, y))
            else:
                y0 = y
                row(r)
                vstarts.append(('r', y0, y))
            if src: self.reg(' '.join(r))
        self.el.append(f'<rect class="gx" x="{xs[0]}" y="{top}" width="{xs[-1]-xs[0]}" height="{y-top}"/>')
        # vertical dividers (skip through group bands)
        segs = [(top, vstarts[0][1] if vstarts else y)]
        for kind, a, b in vstarts:
            if kind == 'r':
                segs.append((a, b))
        for x in xs[1:-1]:
            for a, b in segs:
                self.el.append(f'<line class="gx" x1="{x}" y1="{a}" x2="{x}" y2="{b}"/>')
        self.y = y

    def footnote(self, num, markup):
        """Book footnote, boxed, small blue text (registered separately)."""
        x = self.L
        top = self.y + 14
        lines = wrap('{R:' + num + '} ' + markup, self.R - x - 20, 13)
        yy = top + 4
        for ln in lines:
            yy += 18
            self.el.append(f'<text class="xs" x="{x+10}" y="{yy}">{tspans(ln)}</text>')
        bot = yy + 9
        self.el.append(f'<rect x="{x}" y="{top}" width="{self.R-x}" height="{bot-top}" rx="3" fill="none" stroke="var(--text-secondary)" stroke-width="0.8" stroke-dasharray="4 3"/>')
        self.y = bot
        self.fsrc.append((num, plain(markup)))

    def raw(self, svg, dy=0):
        self.el.append(svg)
        self.y += dy

    # ---------- output ----------
    def svg(self):
        H = int(self.y + 30)
        defs = ('<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" '
                'orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" '
                'stroke-width="1.6" stroke-linecap="round"/></marker></defs>')
        return (f'<svg class="n" width="100%" viewBox="0 0 680 {H}" role="img"><title>{esc(self.title)}</title>'
                f'<desc>{esc(self.desc)}</desc>\n{defs}\n' + '\n'.join(self.el) + '\n</svg>')

    def html(self):
        return HTML_TMPL.replace('%TITLE%', esc(self.title)).replace('%DESC%', esc(self.desc)).replace('%SVG%', self.svg())


HTML_TMPL = """<!doctype html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>%TITLE%</title>
<link href="https://fonts.googleapis.com/css2?family=Kalam:wght@400;700&amp;display=swap" rel="stylesheet">
<style>
:root{--text-primary:#1f1e1d;--text-secondary:#73726c}
html,body{margin:0;padding:0;background:#ffffff}
#vis-container{max-width:680px;margin:0 auto;padding:12px 0}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0,0,0)}
.n{display:block}
.n text{font-family:'Kalam',cursive;font-size:15px}.r{fill:#D93A3A}.b{fill:#2F6FDB}.k{fill:var(--text-primary)}.h{fill:#7A1F1F;text-decoration:underline}.hd{font-weight:700;font-size:17px!important}.sh{font-weight:700;font-size:16px!important}.ln{stroke:var(--text-secondary);stroke-width:1.2;fill:none}.lb{fill:var(--text-primary);font-weight:700;text-decoration:underline}.sm{font-size:14px!important}.xs{font-size:13px!important}.bx{fill:none;stroke:#D93A3A;stroke-width:1.2}.gx{fill:none;stroke:var(--text-secondary);stroke-width:1}
@media print{#vis-container{padding:0}}
</style></head><body>
<div id="vis-container"><h2 class="sr-only">%DESC%</h2>
%SVG%
</div></body></html>
"""

ABBR = re.compile(r'(?:\b(?:Dr|Mr|Mrs|Ms|St|No|Nos|vs|Vol|pp|p|viz|Ibid|Prof|etc|i\.e|e\.g|Govt|Art|cf)\.|\b(?:[A-Z]\.)+|\bi\.e\.,?|\be\.g\.,?)$')

def split_sentences(markup):
    """Split markup text into sentences without breaking {x:...} spans incorrectly."""
    # work on positions in the plain string, map back to markup
    out, start, depth = [], 0, 0
    i = 0
    n = len(markup)
    while i < n:
        c = markup[i]
        if c == '{' and i + 2 < n and markup[i+2] == ':':
            depth += 1
        elif c == '}' and depth:
            depth -= 1
        if c in '.?!' or (c in '”"’' and i > 0 and markup[i-1] in '.?!'):
            j = i + 1
            d = depth
            # include closing quote/brace/superscripts/footnote digits after punctuation
            while j < n and (markup[j] in '”"’}' or markup[j] in '¹²³⁴⁵⁶⁷⁸⁹⁰ᵃᵇ'):
                if markup[j] == '}' and d: d -= 1
                j += 1
            if j < n and markup[j] == ' ' and d == 0:
                depth = 0
                k = j + 1
                nxt = markup[k:k+4]
                nxt_plain = re.sub(r'^\{[rbRBKH]:', '', markup[k:k+6])
                if nxt_plain[:1] and (nxt_plain[:1].isupper() or nxt_plain[:1] in '“‘("(' or nxt_plain[:1].isdigit()):
                    prev = plain(markup[start:i+1]).split()[-1] if plain(markup[start:i+1]).split() else ''
                    if not ABBR.search(prev):
                        out.append(markup[start:j].strip())
                        start = k
                        i = k
                        continue
        i += 1
    tail = markup[start:].strip()
    if tail:
        out.append(tail)
    return out


FINAL_NOTE = ('Please check the tables of this chapter once. If a table looks important, '
              'study it directly from Laxmikanth, or take a screenshot of it and add it '
              'to this page as needed.')

def final_note_html():
    """Last page: the reminder about tables, in large text."""
    import textwrap
    lines = textwrap.wrap(FINAL_NOTE, 34)
    y0 = 140
    t = ''.join(f'<text class="r" x="340" y="{y0 + i*46}" text-anchor="middle" style="font-size:32px;font-weight:700">{esc(l)}</text>' for i, l in enumerate(lines))
    H = y0 + len(lines) * 46 + 60
    svg = (f'<svg class="n" width="100%" viewBox="0 0 680 {H}" role="img"><title>Check the tables</title><desc>Reminder</desc>'
           f'<rect x="30" y="40" width="620" height="{H-70}" rx="6" fill="none" stroke="#D93A3A" stroke-width="2" stroke-dasharray="8 5"/>{t}</svg>')
    return HTML_TMPL.replace('%TITLE%', 'Check the tables').replace('%DESC%', 'Reminder').replace('%SVG%', svg)
