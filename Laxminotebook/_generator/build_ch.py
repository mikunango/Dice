"""Build one chapter and run the word-by-word check.
usage: python3 build_ch.py <chapter_no>     (content module: c<ch>.py with notes(), OUT, SKIP)
"""
import sys, re, os, difflib, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nb
nb.INLINE_ONLY = True
SCR = '/tmp/claude-0/-home-user-Dice/2a2c16e4-87a0-5601-91af-b35abdcd531c/scratchpad'
ch = sys.argv[1]
mod = importlib.import_module('c' + ch)
OUT = mod.OUT

SUP = str.maketrans('¹²³⁴⁵⁶⁷⁸⁹⁰ᵃᵇᶜ', '1234567890abc')
def toks(s):
    s = s.translate(SUP).replace('’', "'").replace('‘', "'")
    s = s.replace('–', ' ').replace('—', ' ').replace('-', ' ')
    return [t.lower() for t in re.findall(r"[A-Za-z0-9₹]+", s)]

notes = mod.notes()
os.makedirs(OUT, exist_ok=True)
body, foot = [], {}
for name, n in notes:
    open(os.path.join(OUT, name + '.html'), 'w').write(n.html())
    body += n.src
    for k, v in n.fsrc: foot[k] = v
open(os.path.join(OUT, '99_note_check_tables.html'), 'w').write(nb.final_note_html())

raw = open(f'{SCR}/ch{ch}.txt').read()
m = list(re.finditer(r'\n1\n\n(?=\S)', raw))
fi = m[-1].start() if m else len(raw)
main, fn = raw[:fi], raw[fi:]
for a, b in mod.SKIP:          # skipped tables (cut from the source before comparing)
    i = main.index(a); j = main.index(b, i) if b else len(main)
    main = main[:i] + main[j:]
lines = [l for l in main.split('\n') if l.strip() not in ('•', '') and not re.fullmatch(r'\s*\d{3}\s*', l)]
S = toks(' '.join(lines)); M = toks(' '.join(body))
sm = difflib.SequenceMatcher(None, S, M, autojunk=False)
print(f'notes={len(notes)} source_tokens={len(S)} note_tokens={len(M)} matched={sum(b.size for b in sm.get_matching_blocks())}')
for t, a, b, c, d in sm.get_opcodes():
    if t != 'equal':
        print(f'  {t:8s} SRC:{" ".join(S[max(a-3,0):b+3])!r:.170}\n           NOTE:{" ".join(M[max(c-3,0):d+3])!r:.170}')
fparts = re.split(r'\n(\d+[abc]?)\n', fn)
src_f = {}
for i in range(1, len(fparts) - 1, 2):
    src_f[fparts[i]] = '\n'.join(l for l in fparts[i+1].split('\n') if not re.fullmatch(r'\s*\d{3}\s*', l))
for k, v in foot.items():
    if toks(src_f.get(k, '')) != toks(v):
        a, b = toks(src_f.get(k, '')), toks(v)
        print(f'  FOOTNOTE {k} differs:', [(o, a[i1:i2], b[j1:j2]) for o, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b).get_opcodes() if o != 'equal'][:3])
print('footnotes in notes:', len(foot), '| missing:', [k for k in src_f if k not in foot and len(k) < 3])
print('paragraphs without keyword:', len(nb.MISSING))
for t, s in nb.MISSING[:80]: print('   ', t[:30], '|', s)
