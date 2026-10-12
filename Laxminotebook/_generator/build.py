import sys, re, os, difflib, importlib
sys.path.insert(0, os.path.dirname(__file__))
OUT = '/home/user/Dice/Laxminotebook/Ch15_Centre_State_Relations'
SRC = '/tmp/claude-0/-home-user-Dice/2a2c16e4-87a0-5601-91af-b35abdcd531c/scratchpad/ch15.txt'
parts = [p for p in sys.argv[1:] if not p.startswith('-')] or ['p1']

SUP = str.maketrans('¹²³⁴⁵⁶⁷⁸⁹⁰ᵃᵇ', '1234567890ab')
def toks(s):
    s = s.translate(SUP).replace('’', "'").replace('‘', "'")
    s = s.replace('–', ' ').replace('—', ' ').replace('-', ' ')
    return [t.lower() for t in re.findall(r"[A-Za-z0-9₹]+", s)]

notes = []
for p in parts:
    notes += importlib.import_module(p).notes()

os.makedirs(OUT, exist_ok=True)
body, foot = [], {}
for name, n in notes:
    open(os.path.join(OUT, name + '.html'), 'w').write(n.html())
    body += n.src
    for k, v in n.fsrc: foot[k] = v

# ---- source text ----
raw = open(SRC).read()
fi = raw.find('\n1\n\nEven now')
main, fn = raw[:fi], raw[fi:]
lines = [l for l in main.split('\n') if l.strip() not in ('•', '') and 'INDIAN POLIY' not in l and not re.fullmatch(r'\s*\d{3}\s*', l)]
main = ' '.join(lines)
if '--all' not in sys.argv:
    # only compare up to the end of what the given parts cover
    pass
S = toks(main)
M = toks(' '.join(body))
sm = difflib.SequenceMatcher(None, S, M, autojunk=False)
ops = [o for o in sm.get_opcodes() if o[0] != 'equal']
covered = max((b for t, a, b, c, d in sm.get_opcodes() if t == 'equal'), default=0)
print(f'notes={len(notes)} source_tokens={len(S)} note_tokens={len(M)} matched_upto={covered}')
for t, a, b, c, d in ops:
    if a >= covered and t == 'delete':
        print(f'  [rest of source not yet written: {b-a} tokens]')
        continue
    print(f'  {t:8s} SRC:{" ".join(S[max(a-3,0):b+3])!r:.160}\n           NOTE:{" ".join(M[max(c-3,0):d+3])!r:.160}')

# ---- footnotes ----
fparts = re.split(r'\n(\d+[ab]?)\n', fn)
src_f = {}
for i in range(1, len(fparts) - 1, 2):
    txt = re.sub(r'\n\d{3}\n?.*$', '', fparts[i+1].strip(), flags=re.S) if False else fparts[i+1]
    txt = '\n'.join(l for l in txt.split('\n') if not re.fullmatch(r'\s*\d{3}\s*', l) and 'INDIAN POLIY' not in l)
    src_f[fparts[i]] = txt
for k, v in foot.items():
    a, b = toks(src_f.get(k, '')), toks(v)
    if a != b:
        print(f'  FOOTNOTE {k} differs:', [o for o in difflib.SequenceMatcher(None, a, b).get_opcodes() if o[0] != "equal"][:3], a[:12], b[:12])
missing = [k for k in src_f if k not in foot and len(k)<3]
print('footnotes done:', len(foot), 'missing:', missing)
