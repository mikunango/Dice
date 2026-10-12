import json, html, collections
from cls import C, THEMES
from clusters import CL
Q = {int(y): qs for y, qs in json.load(open('gs2.json')).items()}
CH = {int(k): v.replace('STATE JUDICIARY','State Judiciary').replace('Lok Adalat’s','Lok Adalats') for k, v in json.load(open('chap.json')).items()}
DONE = {15, 23, 26, 33, 39, 90, 91, 92}
YEARS = list(range(2017, 2027))
e = html.escape
def qtext(y, n): return next(q for q in Q[y] if q['n'] == n)
def ref(y, n): return f"{y}-Q{n}"

# --- chapter stats
link = collections.defaultdict(list); prim = collections.Counter()
for (y, n), (t, chs, s) in C.items():
    for i, c in enumerate(chs):
        link[c].append((y, n))
        if i == 0: prim[c] += 1
chap_rows = sorted(link, key=lambda c: (-len(link[c]), -prim[c], c))

# --- theme × year grid
tcount = {t: collections.Counter() for t in THEMES}
for (y, n), (t, chs, s) in C.items(): tcount[t][y] += 1
torder = sorted(THEMES, key=lambda t: (t == 'IR', -sum(tcount[t].values())))

pol = [k for k, v in C.items() if v[0] != 'IR']
inlax = [k for k in pol if C[k][1]]
marks_lax = sum(qtext(*k)['marks'] for k in inlax)

css = """
:root{--ink:#1d2433;--mut:#5b6475;--line:#d9dee7;--bg:#ffffff;--soft:#f4f6fa;--acc:#1f5fbf;--red:#c0392b;--grn:#1e7d4f;--amb:#b7791f}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:13.5px/1.5 'Segoe UI',system-ui,-apple-system,Roboto,Arial,sans-serif}
main{max-width:980px;margin:0 auto;padding:28px 16px 40px}
h1{font-size:26px;margin:0 0 4px}h2{font-size:19px;margin:30px 0 8px;padding-bottom:5px;border-bottom:2px solid var(--acc);break-after:avoid}
h3{font-size:15px;margin:18px 0 6px;break-after:avoid}.mut{color:var(--mut)}p{margin:6px 0}
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:16px 0}
.kpi{background:var(--soft);border:1px solid var(--line);border-radius:8px;padding:10px 12px}.kpi b{display:block;font-size:22px}
.kpi span{color:var(--mut);font-size:12px}
table{border-collapse:collapse;width:100%;margin:8px 0}th,td{border:1px solid var(--line);padding:5px 7px;vertical-align:top;text-align:left}
th{background:var(--soft);font-weight:600}tr{break-inside:avoid}
.grid td,.grid th{text-align:center;padding:4px 3px;font-size:12px}.grid td:first-child,.grid th:first-child{text-align:left;padding-left:7px}
.c0{color:#c4cad4}.c1{background:#dbe7f8}.c2{background:#a9c6ef}.c3{background:#6f9fe0;color:#fff}.c4{background:#2f6fcf;color:#fff;font-weight:700}
.tag{display:inline-block;border-radius:4px;padding:0 5px;font-size:11.5px;font-weight:600;white-space:nowrap}
.t3{background:#fde2df;color:var(--red)}.t2{background:#fdf0d5;color:var(--amb)}.t1{background:#e3f1e9;color:var(--grn)}
.done{background:#e3f1e9;color:var(--grn)}.ch{font-weight:600;color:var(--acc)}
.yr{font-variant-numeric:tabular-nums;color:var(--mut);font-size:12px}
.q td:nth-child(1){width:46px;white-space:nowrap}.q td:nth-child(3){width:150px}
.note{background:#fff8e6;border-left:4px solid var(--amb);padding:8px 12px;margin:10px 0;border-radius:4px}
ul{margin:4px 0 8px 18px;padding:0}li{margin:2px 0}
@media (max-width:640px){.kpis{grid-template-columns:repeat(2,1fr)}table{font-size:12px}.q td:nth-child(3){width:auto}}
@media print{main{padding:0}h2{break-before:auto}}
@page{size:A4;margin:14mm 12mm}
"""
o = []
o.append(f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>GS2 Mains PYQ Analysis</title><style>{css}</style></head><body><main>
<h1>UPSC CSE Mains GS Paper II – 10-Year PYQ Analysis (2017–2026)</h1>
<p class="mut">Polity &amp; Governance perspective · every question mapped to Laxmikanth, <i>Indian Polity</i> (8th ed.) chapters · repeated and one-time topics both covered</p>
<div class="kpis">
<div class="kpi"><b>200</b><span>questions (20 × 10 years, 2,500 marks)</span></div>
<div class="kpi"><b>{len(pol)}</b><span>Polity, Governance &amp; Social Justice (rest = IR)</span></div>
<div class="kpi"><b>{len(inlax)}</b><span>directly linked to a Laxmikanth chapter</span></div>
<div class="kpi"><b>{marks_lax}</b><span>marks from Laxmikanth-linked questions (≈{marks_lax/25:.0f}/yr of 250)</span></div>
</div>
<div class="note"><b>How to read:</b> <span class="tag t3">★★★ Must</span> = linked to 5+ questions, <span class="tag t2">★★ High</span> = 3–4, <span class="tag t1">★ Normal</span> = 1–2.
<span class="tag done">✓ done</span> = chapter you already converted to notebook notes. Question references are written as <i>Year-Q no.</i> (Q1–10 = 10 marks/150 words, Q11–20 = 15 marks/250 words).</div>
""")

# 1. theme grid
o.append("<h2>1. Topic frequency – year by year</h2><p class='mut'>Number of questions per topic in each year. Darker = more questions.</p><table class='grid'><tr><th>Topic</th>" + ''.join(f"<th>{str(y)[2:]}</th>" for y in YEARS) + "<th>Total</th></tr>")
for t in torder:
    tot = sum(tcount[t].values())
    o.append(f"<tr><td>{e(THEMES[t])}</td>" + ''.join(f"<td class='c{min(tcount[t][y],4)}'>{tcount[t][y] or '·'}</td>" for y in YEARS) + f"<td><b>{tot}</b></td></tr>")
o.append("</table>")
o.append("""<h3>Key patterns</h3><ul>
<li><b>Asked in all 10 years:</b> Federalism / Centre–State (incl. GST, UTs, Finance Commission), Constitutional &amp; statutory bodies, and governance (civil services / e-governance / Citizens’ Charter).</li>
<li><b>Asked every year since 2018:</b> Comparative constitutions – India vs USA / UK / France (10 questions in 9 years).</li>
<li><b>Almost every year:</b> Local government (8 of 10 years), Elections / RPA / ECI (8 of 10 years), Pressure groups &amp; civil society (9 of 10 years).</li>
<li><b>Exact topic repeats:</b> CAG (2018, 2024), Attorney General (2019, 2025), GST/101st Amendment (2017, 2023), Citizens’ Charter (2018, 2024), ONOE (2017, 2024), Constitutional morality (2021, 2025), RPwD Act (2017, 2022), Privacy/Art. 21 (2017, 2023, 2024, 2026), RPA corrupt practices (2020, 2025).</li>
<li><b>Recent trend (2024–26):</b> more 15-mark questions with “compare with USA”, “cite case laws”, and judgements (privacy, euthanasia, collegium, Governor’s assent).</li>
<li>Questions are almost never pure facts – they ask <i>Examine / Critically examine / Discuss</i>. Laxmikanth gives the base (provisions, articles, cases); add analysis (issues, committees, way forward).</li></ul>""")

# 2. chapter priority
o.append("<h2>2. Laxmikanth chapter priority list</h2><p class='mut'>Every chapter linked to at least one GS2 question in 10 years, ranked by number of questions. “Main” = questions where this chapter is the primary source.</p>")
o.append("<table><tr><th>Ch.</th><th>Chapter</th><th>Qs</th><th>Main</th><th>Priority</th><th>Asked in (Year-Q)</th></tr>")
for c in chap_rows:
    k = len(link[c]); tier = ('t3', '★★★ Must') if k >= 5 else (('t2', '★★ High') if k >= 3 else ('t1', '★ Normal'))
    dn = " <span class='tag done'>✓ done</span>" if c in DONE else ''
    o.append(f"<tr><td class='ch'>{c}</td><td>{e(CH[c])}{dn}</td><td><b>{k}</b></td><td>{prim[c]}</td><td><span class='tag {tier[0]}'>{tier[1]}</span></td><td class='yr'>{', '.join(ref(*x) for x in sorted(link[c]))}</td></tr>")
o.append("</table>")
zero = [c for c in range(1, 96) if c not in link]
o.append(f"<p class='mut'><b>Chapters not directly asked in GS2 Mains (2017–26):</b> " + ', '.join(f"{c} {e(CH[c])}" for c in zero) + ". These still matter for Prelims and as supporting points (e.g. Preamble, DPSP, Emergency in answers).</p>")

# 3. clusters
o.append("<h2>3. Repeated topics – with the exact questions</h2><p class='mut'>Same idea asked again (wording changes). These are the safest areas to prepare deeply.</p>")
for name, lst in sorted(CL, key=lambda x: -len(x[1])):
    chs = []
    for k in lst:
        for c in C[k][1]:
            if c not in chs: chs.append(c)
    chs_txt = ', '.join(f"Ch {c}" for c in chs) if chs else 'Not in Laxmikanth'
    o.append(f"<h3>{e(name)} <span class='tag {'t3' if len(lst)>=5 else 't2' if len(lst)>=3 else 't1'}'>{len(lst)}×</span> <span class='mut' style='font-weight:400;font-size:12.5px'>→ {chs_txt}</span></h3><table class='q'>")
    for (y, n) in lst:
        q = qtext(y, n)
        o.append(f"<tr><td class='yr'>{y}<br>Q{n}</td><td>{e(q['q'])}</td><td class='yr'>{q['marks']} marks</td></tr>")
    o.append("</table>")

# 4. single
used = {k for _, l in CL for k in l}
single = sorted(k for k, v in C.items() if k not in used and v[0] != 'IR')
o.append("<h2>4. Asked once only (not repeated yet) – still prepare</h2><table class='q'><tr><th>Ref</th><th>Question</th><th>Laxmikanth</th></tr>")
for (y, n) in single:
    q = qtext(y, n); chs = C[(y, n)][1]
    o.append(f"<tr><td class='yr'>{y}<br>Q{n}</td><td>{e(q['q'])}</td><td>{', '.join(f'<span class=ch>Ch {c}</span> {e(CH[c])}' for c in chs) if chs else '<span class=mut>Not in Laxmikanth</span>'}</td></tr>")
o.append("</table>")

# 5. year-wise full list
o.append("<h2>5. Full year-wise list – all 200 questions with chapter mapping</h2>")
for y in YEARS:
    o.append(f"<h3>GS Paper II – {y}</h3><table class='q'><tr><th>Q</th><th>Question</th><th>Topic → Chapter</th></tr>")
    for q in Q[y]:
        t, chs, s = C[(y, q['n'])]
        m = ', '.join(f"<span class=ch>Ch {c}</span>" for c in chs) if chs else ('<span class=mut>IR</span>' if t == 'IR' else '<span class=mut>Not in Laxmikanth</span>')
        o.append(f"<tr><td class='yr'>Q{q['n']}<br>{q['marks']}m</td><td>{e(q['q'])}</td><td><span class='mut'>{e(THEMES[t])}</span><br>{m}</td></tr>")
    o.append("</table>")

# 6. outside Laxmikanth
o.append("""<h2>6. Topics outside Laxmikanth – what to use</h2><table><tr><th>Area</th><th>Asked</th><th>Source to use</th></tr>
<tr><td>Civil services, Citizens’ Charter, e-Governance, transparency</td><td>every year</td><td>2nd ARC reports – 10th (Personnel Administration), 11th (e-Governance), 12th (Citizen-Centric Administration), 4th (Ethics in Governance); Laxmikanth Ch 75 for constitutional base</td></tr>
<tr><td>Poverty, hunger, malnutrition, health, education, skills</td><td>every year</td><td>Economic Survey, NFHS-5, MPI reports, NEP 2020, scheme facts (PIB / India Year Book)</td></tr>
<tr><td>Vulnerable sections – disabled, transgender, tribals, women, children</td><td>most years</td><td>The Acts themselves (RPwD 2016, Transgender 2019, RTE 2009, FRA 2006), Ministry annual reports; Laxmikanth Ch 8, 9, 42, 48–50, 59–60 for constitutional base</td></tr>
<tr><td>SHGs, NGOs, civil society, trusts, donor agencies</td><td>8 times</td><td>2nd ARC, NITI Aayog papers; Laxmikanth Ch 87 only for pressure groups</td></tr>
<tr><td>International relations (Q9–10 and Q19–20 every year)</td><td>40 Qs</td><td>MEA briefs, current affairs – not Laxmikanth (Ch 89 Foreign Policy only gives basics)</td></tr></table>
<div class="note"><b>Bottom line for GS2:</b> about half of every paper (≈125 of 250 marks) can be written from Laxmikanth + judgements. Finish the ★★★ and ★★ chapters first, keep the case laws of Ch 91–92 ready, and practise “India vs USA/UK” comparisons from Ch 95.</div>
<p class='mut' style='font-size:11.5px'>Question text compiled from published GS Paper II papers (2017–2026); verify wording against the official UPSC question papers at upsc.gov.in if needed. Chapter numbers from Laxmikanth, Indian Polity, 8th edition.</p>
</main></body></html>""")
open('GS2_PYQ_Analysis.html', 'w').write('\n'.join(o))
print('chapters linked', len(link), 'zero', len(zero))
for c in chap_rows[:25]: print(c, CH[c], len(link[c]), prim[c])
