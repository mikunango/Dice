import re
from nb import Note
import parse91 as P

OUT = '/home/user/Dice/Laxminotebook/Ch91_Landmark_Judgements'
SKIP = []

# exam keywords: (judgement, impact) per case, in book order
KW = {
 'Romesh Thappar': ('Freedom of circulation', 'Public order – 1st Amendment'),
 'A.K. Gopalan': ('Personal liberty = physical body', 'Textualist approach – no due process'),
 'Champakam Dorairajan': ('DPSP subsidiary to FRs', 'Article 15(4) – 1st Amendment'),
 'Shankari Prasad': ('FRs amendable', 'Legislative vs constituent law'),
 'Berubari Union': ('Cession needs Art. 368 amendment', '9th Amendment – Berubari transfer'),
 'K.M. Nanavati': ('Conviction upheld', 'End of jury trials'),
 'GOLAK NATH': ('FRs not amendable – prospective overruling', '24th Amendment response'),
 'Kesavananda Bharati': ('Basic structure doctrine', 'Limit on amending power'),
 'Indira Nehru Gandhi': ('Art. 329A(4) struck down', '42nd Amendment – Art. 368(4), (5)'),
 'A.D.M. Jabalpur': ('Habeas corpus suspended', '44th Amendment – Art. 21 non-suspendable'),
 'Maneka Gandhi': ('Just, fair and reasonable procedure', 'Due process & golden triangle'),
 'Bachan Singh': ('Death penalty valid', 'Rarest of rare doctrine'),
 'Minerva Mills': ('Limited amending power is basic structure', '42nd Amendment dilution nullified'),
 'Waman Rao': ('Ninth Schedule – 24 April 1973 cut-off', None),
 'Shah Bano': ('Maintenance under Sec. 125 CrPC', 'Muslim Women Act 1986'),
 'D.C. Wadhwa': ('Re-promulgation is fraud on Constitution', 'Check on ordinance raj'),
 'M.C. Mehta': ('Article 32 – remedial power', 'Absolute (no-fault) liability'),
 'Kihoto Hollohan': ('Paragraph 7 invalid – rest of Tenth Schedule upheld', None),
 'Indra Sawhney': ('27% OBC quota – with conditions', 'Creamy layer & National Commission for BCs'),
 'Mohini Jain': ('Right to education under Art. 21', 'Basis for Unni Krishnan'),
 'Unni Krishnan': ('Free education till 14', '86th Amendment – Art. 21A'),
 'Advocates-on-Record Association Case (1993)': ('Collegium – CJI primacy', 'Memorandum of Procedure'),
 'S.R. Bommai': ('Judicial review of President’s Rule', 'Check on misuse of Art. 356'),
 'Vishaka': ('Sexual harassment violates Arts. 15 & 21', 'Vishaka Guidelines'),
 'Vineet Narain': ('CVC supervision of CBI', 'CVC Act 2003'),
 'Association for Democratic Reforms': ('Voters’ right to know', 'Candidate disclosure order (2003)'),
 'T.M.A. PAI': ('Minority institutions’ autonomy', '93rd Amendment – Art. 15(5)'),
 'Naveen Jindal': ('Flag hoisting – Art. 19(1)(a)', None),
 'Prakash Singh': ('Police reforms – seven directives', 'Partial police reforms'),
 'M. Nagaraj': ('Promotion quota amendments upheld', None),
 'I.R. Coelho': ('Ninth Schedule laws reviewable', None),
 'Aruna Ramachandra Shanbaug': ('Passive euthanasia allowed', None),
 'People’s Union for Civil Liberties': ('Right not to vote – secrecy', 'NOTA option'),
 'LILY THOMAS': ('Sec. 8(4) RPA struck down', 'Immediate disqualification of convicted legislators'),
 'T.S.R. Subramanian': ('Civil service reforms', 'Cadre Rules amended (2014)'),
 'NATIONAL LEGAL SERVICES AUTHORITY': ('Third gender recognised', 'Transgender Persons Act 2019'),
 'Shreya Singhal': ('Section 66A struck down', None),
 'ADVOCATES-ON-RECORD ASSOCIATION CASE (2015)': ('NJAC unconstitutional', 'Collegium revived'),
 'Shayara Bano': ('Triple talaq void', 'Triple Talaq Act 2019'),
 'PUTTASWAMY': ('Privacy a fundamental right', 'Overruled M.P. Sharma & Kharak Singh'),
 'INDIAN YOUNG LAWYERS': ('Sabarimala – women’s entry', 'Protests and resistance'),
 'JOSEPH SHINE': ('Adultery decriminalised', 'Adultery only a civil wrong'),
 'Navtej Singh Johar': ('Section 377 read down', 'Overruled Suresh Kumar Koushal'),
 'M. Siddiq': ('Disputed land to Ram Lalla', 'End of Ayodhya dispute – temple trust'),
 'Anuradha Bhasin': ('Internet & proportionality', 'Right to internet access'),
 'Rambabu Singh Thakur': ('Disclose criminal antecedents', 'Form C-7'),
 'INTERNET AND MOBILE ASSOCIATION': ('Crypto ban struck down', 'Crypto trading resumed'),
}

def kw_for(title):
    for k, v in KW.items():
        if k.lower() in title.lower():
            return v
    raise KeyError(title)

def emph(t):
    """Light automatic highlighting (red = articles, amendments, sections, years; blue = quoted phrases)."""
    t = re.sub(r'(Articles? \d+[A-Z]?(?:\(\d+\))?(?:\([a-z]\))?(?:(?:,| and| &| or) \d+[A-Z]?(?:\(\d+\))?(?:\([a-z]\))?)*)', r'{r:\1}', t)
    t = re.sub(r'(\d+(?:st|nd|rd|th) (?:Constitutional )?Amendment Act(?: \(\d{4}\))?)', r'{r:\1}', t)
    t = re.sub(r'([Ss]ection \d+[A-Z]?(?:\(\d+[A-Z-]*\))?(?:\([a-z]\))?)', r'{r:\1}', t)
    t = re.sub(r'([‘“][^’”{}]{3,90}[’”])', r'{b:\1}', t)
    # avoid nested braces produced by overlapping rules
    out, depth = [], 0
    i = 0
    while i < len(t):
        if t[i] == '{' and i + 2 < len(t) and t[i+2] == ':':
            if depth:
                i += 3; continue
            depth += 1; out.append(t[i:i+3]); i += 3; continue
        if t[i] == '}' and depth:
            # close only the outermost
            depth -= 1
            if depth == 0: out.append('}')
            i += 1; continue
        out.append(t[i]); i += 1
    return ''.join(out)

FLOWS = {
 'K.M. Nanavati': None,
 'Kesavananda Bharati': ['Shankari Prasad 1951: {r:FRs amendable}', 'Sajjan Singh 1964', 'Golak Nath 1967: {r:not amendable}', '24th Amdt 1971', '{R:Kesavananda 1973: basic structure}'],
 'Maneka Gandhi': ['A.K. Gopalan 1950: {r:narrow Art. 21}', 'ADM Jabalpur 1976: {r:suspended}', '{R:Maneka 1978: due process}', '44th Amdt 1978'],
 'Minerva Mills': ['42nd Amdt: Art. 368(4),(5)', '{R:Minerva Mills 1980}: struck down', '{b:limited amending power = basic structure}'],
 'Indra Sawhney': ['27% OBC executive order', '{R:Indra Sawhney 1992}', 'creamy layer excluded · no promotion quota'],
 'ADVOCATES-ON-RECORD ASSOCIATION CASE (2015)': ['1st Judges 1981', '{R:2nd Judges 1993} collegium', '3rd Judges 1998', '99th Amdt NJAC 2014', '{R:4th Judges 2015} NJAC void'],
 'PUTTASWAMY': ['M.P. Sharma 1954 / Kharak Singh 1962', '{R:Puttaswamy 2017}', '{b:privacy = Art. 21 + Part III}'],
}

def card(n, c):
    rows = []
    for lab, key in [('Year of Judgement', 'year'), ('Popular Name', 'pop'), ('Related Topic/Issue', 'topic'), ('Related Article/Schedule', 'art')]:
        rows.append(['{K:' + lab + '}', '{r:' + c[key] + '}' if key in ('year', 'art') else c[key]])
    n.table(['{K:Name of the Case}', '{R:' + c['name'] + '}'], rows, [190, 410])

def notes():
    out = []
    cases = P.cases
    groups = [cases[i:i+3] for i in range(0, len(cases), 3)]
    for gi, grp in enumerate(groups):
        y0, y1 = grp[0]['year'], grp[-1]['year']
        if gi == 0:
            n = Note('CHAPTER 91 Landmark Judgements and Their Impact', 'Landmark Supreme Court judgements, their holdings and impact.')
            n.reg('CHAPTER 91 Landmark Judgements and Their Impact')
        else:
            n = Note(f'Landmark Judgements – {gi+1} ({y0}–{y1})' if y0 != y1 else f'Landmark Judgements – {gi+1} ({y0})')
        for c in grp:
            kj, ki = kw_for(c['title'])
            n.subsub(c['title'])
            card(n, c)
            n.para(f'[[{kj}]] {{K:Supreme Court Judgement:}} ' + emph(c['jud']))
            if 'imp' in c:
                n.para(f'[[{ki}]] {{K:Impact of the Judgement:}} ' + emph(c['imp']))
            for k, fl in FLOWS.items():
                if fl and k.lower() in c['title'].lower():
                    n.flow(fl)
            # footnotes referenced in this case
            txt = c.get('jud', '') + c.get('imp', '') + c.get('art', '') + c.get('name', '')
            for mk in re.findall(r'[⁰¹²³⁴⁵⁶⁷⁸⁹]+[ᵃᵇ]?', txt):
                key = mk.translate(str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹ᵃᵇ', '0123456789ab'))
                if key in P.FOOT and key not in [f[0] for f in n.fsrc]:
                    n.footnote(key, P.FOOT[key])
        slug = re.sub(r'[^a-z0-9]+', '_', grp[0]['title'].split(' (')[0].lower()).strip('_')
        out.append((f'{gi+1:02d}_notes_judgements_{y0}_{slug}', n))
    return out
