from nb import Note

OUT = '/home/user/Dice/Laxminotebook/Ch92_Article_21_Judgements'
SKIP = []

R = [
 ('Satwant Singh Sawhney vs. D. Ramarathnam, Assistant Passport Officer, New Delhi', '1967', 'Right to travel abroad'),
 ('Sunil Batra vs. Delhi Administration', '1978', 'Right against solitary confinement'),
 ('Charles Sobhraj vs. Superintendent, Central Jail, New Delhi', '1978', 'Right against bar fetters'),
 ('M.H. Hoskot vs. State of Maharashtra', '1978', 'Right to free legal aid'),
 ('Hussainara Khatoon vs. Home Secretary, State of Bihar', '1979', 'Right to speedy trial'),
 ('Prem Shankar Shukla vs. Delhi Administration', '1980', 'Right against handcuffing'),
 ('Kishore Singh Ravinder Dev vs. State of Rajasthan', '1980', 'Right against inhuman treatment by the police (use of “third degree” method)'),
 ('Francis Coralie Mullin vs. Administrator, Union Territory of Delhi', '1981', 'Right to live with human dignity & Right of prisoner to have necessities of life.'),
 ('Board of Trustees of Port of Bombay vs. Dilip Kumar R. Nadkarni', '1982', 'Right to reputation'),
 ('T.V. Vatheeswaran vs. State of Tamil Nadu', '1983', 'Right against delayed execution'),
 ('Sheela Barse vs. State of Maharashtra', '1983', 'Right against custodial violence'),
 ('Bandhua Mukti Morcha vs. Union of India', '1983', 'Right against bonded labour'),
 ('Rural Litigation and Entitlement Kendra vs. State of U.P. (popularly known as the Dehradun Quarrying case)', '1985', 'Right to decent environment (Right to a clean and healthy environment)'),
 ('Attorney General of India vs. Lachma Devi', '1985', 'Right against public hanging'),
 ('Olga Tellis vs. Bombay Municipal Corporation (popularly known as the Pavement Dwellers case)', '1985', 'Right to livelihood'),
 ('State of H.P. vs. Umed Ram Sharma', '1986', 'Right to road in hilly areas'),
 ('Parmanand Katara vs. Union of India', '1989', 'Right to emergency medical aid (Right to Doctor’s assistance)'),
 ('Shantistar Builders vs. N.K. Totame', '1990', 'Right to shelter'),
 ('Unni Krishnan, J.P. vs. State of Andhra Pradesh', '1993', 'Right to free education upto 14 years of age'),
 ('Consumer Education and Research Centre vs. Union of India', '1995', 'Right to health'),
 ('L.I.C. of India vs. Consumer Education and Research Centre', '1995', 'Right to appropriate life insurance policy'),
 ('National Human Rights Commission vs. State of Arunachal Pradesh (popularly known as the Chakmas Migrants case)', '1996', 'Right not to be driven out of a state'),
 ('Paschim Banga Khet Mazdoor Samity vs. State of West Bengal', '1996', 'Right to timely medical treatment in Government Hospital'),
 ('Police Commissioner, Delhi vs. Registrar, Delhi High Court', '1996', 'Right to fair trial'),
 ('Vellore Citizens Welfare Forum vs. Union of India', '1996', 'Protection against hazardous industries'),
 ('Dr. B.L. Wadhera vs. Union of India', '1996', 'Pollution-free water and air'),
 ('Ashok Kumar Gupta vs. State of U.P.', '1997', 'Right to social and economic justice and empowerment'),
 ('S.K. Mastan Bee vs. G.M., South Central Railway', '2002', 'Right to family pension'),
 ('N.D. Jayal vs. Union of India', '2003', 'Right to sustainable development'),
 ('Noise Pollution, In Re.', '2005', 'Right to freedom from noise pollution'),
 ('Reliance Energy vs. M.S.R.D.C.', '2007', 'Right to opportunity'),
 ('Dilip s. Dahanukar vs. Kotak Mahindra', '2007', 'Right of appeal from a judgement of conviction'),
 ('Ramlila Maidan Incident, In Re.', '2012', 'Right to sleep'),
 ('K.S. Puttaswamy vs. Union of India', '2017', 'Right to privacy'),
 ('Common Cause (A Regd. Society) vs. Union of India', '2018', 'Right to die with dignity (Passive euthanasia)'),
 ('M.K. Ranjitsinh vs. Union of India', '2024', 'Right against the adverse effects of climate change'),
]
HEAD = ['{R:Sl. No.}', '{R:Name of the Case}', '{R:Year of Judgement}', '{R:Right declared by the Supreme Court as an integral part of Article 21}']
W = [45, 290, 70, 195]

def rows(a, b):
    return [[f'{i+1}.', c, '{r:' + y + '}', '{R:' + r + '}'] for i, (c, y, r) in enumerate(R) if a <= i < b]

def notes():
    out = []
    n = Note('CHAPTER 92 Judgements Expanding the Scope of Article 21', 'Table 92.1 – rights read into Article 21, part 1.')
    n.reg('CHAPTER 92 Judgements Expanding the Scope of Article 21')
    n.text('{b:Article 21 – “No person shall be deprived of his life or personal liberty except according to procedure established by law” – has been widened by the Supreme Court into a source of many unenumerated rights:}', size=14, src=False)
    n.tree(['{r:Prisoners & accused}', '{r:Dignity & livelihood}', '{r:Health & education}', '{r:Environment}', '{r:Privacy & dignity in death}'], size=13)
    n.table(HEAD, rows(0, 18), W, caption='Table 92.1: Judgements declaring various rights as integral parts of the protection of life and personal liberty under Article 21')
    out.append(('01_notes_ch92_table_92_1_part1', n))
    n = Note('Article 21 Judgements – continued')
    n.table(HEAD, rows(18, 36), W, src=True)
    n.flow(['1967 travel abroad', '1978–83 prisoners’ rights', '1985 livelihood, environment', '2017 privacy', '2018 die with dignity', '2024 climate change'])
    out.append(('02_notes_table_92_1_part2', n))
    return out
