import re
SRC = '/tmp/claude-0/-home-user-Dice/2a2c16e4-87a0-5601-91af-b35abdcd531c/scratchpad/ch91.txt'
raw = open(SRC).read()
m = list(re.finditer(r'\n1\n\n(?=\S)', raw)); fi = m[-1].start()
body, fn = raw[:fi], raw[fi:]
lines = [l for l in body.split('\n') if not re.fullmatch(r'\s*\d{3}\s*', l)]
HEAD = re.compile(r'^[A-Z][^:]*(Case|case|CASE) \([0-9]{4}\)$')
cases, cur = [], None
for l in lines[2:]:
    if HEAD.match(l.strip()):
        cur = {'title': l.strip(), 'lines': []}; cases.append(cur)
    elif cur is not None:
        cur['lines'].append(l)
SUPMAP = str.maketrans('0123456789abc', '⁰¹²³⁴⁵⁶⁷⁸⁹ᵃᵇᶜ')
def sup(t):
    return re.sub(r'(?<=[A-Za-z\)])(\d{1,2}[ab]?)(?=[\s,.;:)]|$)', lambda m: m.group(1).translate(SUPMAP), t)
def join(ls):
    t = ' '.join(x.strip() for x in ls if x.strip())
    return re.sub(r'\s+', ' ', t).strip()
for c in cases:
    t = join(c['lines'])
    f = {}
    for key, pat in [('name', r'Name of the Case\s*:\s*'), ('year', r'Year of Judgement\s*:\s*'), ('pop', r'Popular Name\s*:\s*'),
                     ('topic', r'Related Topic/ ?Issue\s*:\s*'), ('art', r'Related Article/ ?Schedule\s*:\s*'), ('jud', r'Supreme Court Judgement\s*:\s*'), ('imp', r'Impact of the Judgement\s*:\s*')]:
        mm = re.search(pat, t)
        f[key] = mm
    keys = [k for k in f if f[k]]
    keys.sort(key=lambda k: f[k].start())
    for i, k in enumerate(keys):
        end = f[keys[i+1]].start() if i + 1 < len(keys) else len(t)
        c[k] = sup(t[f[k].end():end].strip())
    c['order'] = keys
# footnotes
fparts = re.split(r'\n(\d+[ab]?)\n', fn)
FOOT = {}
for i in range(1, len(fparts) - 1, 2):
    FOOT[fparts[i]] = join([l for l in fparts[i+1].split('\n') if not re.fullmatch(r'\s*\d{3}\s*', l)])
if __name__ == '__main__':
    print(len(cases))
    for c in cases:
        print(c['title'], '|', c.get('year'), '|', c.get('pop'), '|', c.get('art'), '| order', ''.join(k[0] for k in c['order']), len(c.get('jud','')), len(c.get('imp','')))
    print(sorted(FOOT, key=lambda k:(int(re.match(r'\d+',k).group()),k)))
    import re as _r
    for c in cases:
        for k in ('jud','imp'):
            for s in _r.findall(r'\S*[⁰¹²³⁴⁵⁶⁷⁸⁹ᵃᵇ]+\S*', c.get(k,'')): print('  SUP', c['title'][:20], s)
