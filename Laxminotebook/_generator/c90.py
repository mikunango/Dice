from nb import Note

OUT = '/home/user/Dice/Laxminotebook/Ch90_NCRWC'
SKIP = []

def L(n, pairs, indent=0):
    """items from (label, keyword, text) triples"""
    n.items([(a, f'[[{k}]] {t}' if k else t) for a, k, t in pairs], indent=indent)

def notes():
    out = []

    # ---------------- 01 Intro, ToR, areas of study ----------------
    n = Note('CHAPTER 90 National Commission to Review the Working of the Constitution', 'NCRWC: setting up, terms of reference and eleven areas of study.')
    n.reg('CHAPTER 90 National Commission to Review the Working of the Constitution')
    n.para('[[NCRWC – Venkatachaliah Commission (2000)]] The {r:National Commission to Review the Working of the Constitution (NCRWC)} was set up by a {r:resolution of the Government of India in 2000}. It was an {r:11-member Commission} headed by {r:M.N. Venkatachaliah}, the {b:former Chief Justice of India}¹. It submitted its report in {r:2002}.')
    n.flow(['set up {r:2000} (Govt resolution)', '{r:11 members}', 'Chair: {r:M.N. Venkatachaliah}', 'report {r:2002}'])
    n.sub('Terms of Reference')
    n.para('[[Within basic structure]] According to the terms of reference, the commission was required to examine, in the light of the {r:experience of the past fifty years}, as to how far the existing provisions of the Constitution are capable of responding to the needs of {b:efficient, smooth and effective system of governance and socio-economic development} of modern India and to recommend changes, if any. The terms of reference clearly specified that the commission should recommend changes that are required to be made in the Constitution {r:within the framework of parliamentary democracy} and {r:without interfering with the ‘basic structure’} or ‘basic features’ of the Constitution.')
    n.para('[[Review, not rewrite]] The commission clarified that its task was to {r:review the working of the Constitution and not to rewrite it} and its function was only {r:recommendatory and advisory} in nature. It was left to the {r:Parliament to accept or reject} any of the recommendations.')
    n.para('[[Eleven areas of study]] The commission had {r:no agenda} before it. On its own, it identified the {r:eleven areas of study} and proposed to examine them. They included the following²:')
    L(n, [('1.', '', 'Strengthening the institutions of {r:parliamentary democracy} (working of the Legislature, the Executive and the Judiciary; their accountability; problems of administrative, social and economic cost of political instability; exploring the possibilities of stability within the discipline of parliamentary democracy).'),
          ('2.', '', '{r:Electoral reforms}; standards in political life.'),
          ('3.', '', 'Pace of {r:socio-economic change and development} under the Constitution (assurance of social and economic rights: how fair? how fast? how equal?).'),
          ('4.', '', 'Promoting {r:literacy}; generating {r:employment}; ensuring {r:social security}; alleviation of {r:poverty}.'),
          ('5.', '', '{r:Union-State relations}.'),
          ('6.', '', '{r:Decentralization and devolution}; empowerment and strengthening of Panchayati Raj Institutions.'),
          ('7.', '', 'Enlargement of {r:Fundamental Rights}.'),
          ('8.', '', 'Effectuation of {r:Fundamental Duties}.'),
          ('9.', '', 'Effectuation of {r:Directive Principles} and achievement of the Preambular objectives of the Constitution.'),
          ('10.', '', 'Legal control of {r:fiscal and monetary policies}; public audit mechanism.'),
          ('11.', '', '{r:Administrative system} and standards in public life.')])
    n.footnote('1', 'The other members of the Commission were: B.P. Jeevan Reddy (Chairman of the Law Commission), R.S. Sarkaria (former judge of the Supreme Court), K. Punnayya (former judge of the Andhra Pradesh High Court), Soli Sorabjee (Attorney–General of India), K. Parasaran (former Attorney–General of India), Subhash Kashyap (former Secretary–General of Lok Sabha), C.R. Irani (Chief Editor and MD of the Statesman), Abid Hussain (former Ambassador of India to the USA), Smt. Sumitra Kulkarni (former MP) and P.A. Sangma (former Speaker of the Lok Sabha). P.A. Sangma resigned three months before the submission of the report by the Commission.')
    n.footnote('2', 'Report of the Commission, Volume I, Chapter 1.')
    out.append(('01_notes_ch90_ncrwc_intro_terms', n))

    # ---------------- 02 Areas of concern 1–9 ----------------
    n = Note('NCRWC – Areas of Concern I')
    n.sub('Areas of Concern')
    n.para('[[Commission’s perception]] The following are the important {r:areas of concern} according to the perception of the Commission³:')
    L(n, [('1.', 'Breach of constitutional faith', 'There is a {r:fundamental breach of the constitutional faith} on the part of Governments and their method of governance lies in the {b:neglect of the people} who are the ultimate source of all political authority. Public servants and institutions are not alive to the basic imperative that they are {b:servants of the people} meant to serve them. The {r:dignity of the individual} enshrined in the Constitution has remained an {r:unredeemed pledge}. There is, thus, a {r:loss of faith in the Governments and governance}. Citizens see their Governments besieged by uncontrollable events and are losing faith in institutions. Society is unable to cope up with current events.'),
          ('2.', 'Unprepared Indian State', 'The foremost area of concern is the present {r:nature of the Indian State} and its {r:inability to anticipate} and provide for the great {b:global forces of change} ushered in by the pace of scientific and technological developments.'),
          ('3.', 'Cost of government & fiscal deficits', 'The next and equally important dimension is the {r:increasing cost of government and fiscal deficits} which are alarming.'),
          ('4.', 'Criminalisation of politics', 'There is a pervasive {r:impurity of the political climate} and of political activity. {r:Criminalisation of politics, political-corruption and the politician-criminal-bureaucratic nexus} have reached unprecedented levels of needing strong systemic changes.'),
          ('5.', 'National security & disaster management', 'Issues of {r:national integrity and security} have not received adequate and thoughtful attention. Mechanisms for the assessment of {b:early warning symptoms of social unrest} are absent. Mechanisms for adequate and immediate state responses to {r:emergencies and disaster management} are wholly inadequate. Administration, as a system for anticipating coming events and planning responses in advance, has failed. It has become {r:un-coordinated and directionless} amalgam of different departments often with over-lapping and even mutually conflicting jurisdictions, powers and responsibilities which merely acts as a reaction to problems. There are {b:no clear-cut standards or basis for fixing responsibilities}.'),
          ('6.', 'Fault-lines in democratic institutions', 'Though India’s overall record and experience as a {b:working democracy} (despite many centrifugal forces) are worthy to mention and though the bases of democratic debate have widened with the {b:73rd and 74th Constitutional amendments}, the working of the institutions of parliamentary democracy, however, have thrown-up {r:serious fault-lines}, which might, if unattended, prove destructive of the basic democratic values.'),
          ('7.', 'Misuse of electoral process', 'There is {r:pervasive misuse of the electoral process} and the electoral system is unable to prevent the {r:entry of persons with criminal record} into the portal of law-making institutions.'),
          ('8.', 'Weak representative character', 'The Parliament and the State Legislatures, owing to the inherent weakness of the electoral system, have {r:failed to acquire adequate representative character}.'),
          ('9.', 'Political instability', 'The increasing {r:instability of the elected governments} is attributable to {r:opportunistic politics and unprincipled defections}. The economic and administrative costs of political instability are unaffordably high and their impact on the polity is not clearly comprehended and realized. Though just {b:four Prime Ministers ruled the country for 40 years out of the 54 years} of independence and one political party alone was in power for 45 years, however, {r:1989 onwards the country saw five General Elections} to the Lok Sabha. Costs of this political instability are simply {r:colossal}.')])
    n.footnote('3', 'Report of the Commission, Volume I, Chapter 2.')
    out.append(('02_notes_areas_of_concern_1', n))

    # ---------------- 03 Areas of concern 10–18 ----------------
    n = Note('NCRWC – Areas of Concern II')
    L(n, [('10.', 'Debt-trap & parallel economy', 'The state of the {r:Indian economy is disturbing}. The economy is gradually sinking into a {r:debt-trap}. Economic, fiscal and monetary policies, coupled with administrative inefficiency, corruption and wasteful expenditure are increasingly pushing the society into {b:extra-legal systems, crime-syndicates, mob-rule and hoodlum out-fits}. {r:Black-money, parallel economy and even parallel governments} are the overarching economic and social realities. Legitimate governments will, in due course, find it increasingly difficult to confront them. In course of time these illegal criminal out-fits will dictate terms to the legitimate governments.'),
          ('11.', 'Urbanisation & unemployment', '{r:Rural de-population, urbanization, urban-congestion and social unrest} need immediate attention and solutions. Increasing {r:unemployment} will prove a serious threat to orderly government.'),
          ('12.', 'Educational disarmament', 'Future of society is increasingly {r:knowledge-based and knowledge-driven}. The quality of {r:education and the higher research} need urgent repair. The country is engaged in a {r:unilateral and unthinking educational disarmament}.'),
          ('13.', 'Justice delivery', 'System of {r:administration of justice} in the country is another area of concern.'),
          ('14.', 'Criminal justice collapse', '{r:Criminal justice system is on the verge of collapse}. The quality of investigations and prosecutions requires a strong second look. {r:Law’s delay and costs of litigation} have become proverbial. {b:Victimology, victim-protection and protection of witnesses} in sensitive criminal-trials need institutional arrangements. Recruitment, training, refresher and continuing legal education for lawyers, judges and judicial administrators need immediate attention. The increasing utilization of {r:alternative dispute resolution} mechanisms such as {b:mediation, conciliation and arbitration} as well as mechanisms of auxiliary adjudicative services need to be stressed.'),
          ('15.', 'Communal riots', '{r:Communal and other inter-group riots} in a country like India with its religious, social and cultural diversity cannot be treated as merely law and order problem. They are manifestations of {r:collective behavioural disorders}. Legal and administrative measures are required to be taken to remove the {b:insecurity felt by the minorities} and for bringing them into the mainstream of the national fabric.'),
          ('16.', 'Social infrastructure', 'The state of {r:social infrastructure is disturbing}. There are {r:380 million children below the age of 14}. The arrangements for their education, health and well-being are wholly inadequate both qualitatively and quantitatively. {r:96.4 per cent of the primary education budget goes for salaries} alone.'),
          ('17.', 'Health indicators', 'Rates of {r:infant mortality, blindness, maternal mortality, maternal-anemia, child malnutrition and child-immunization}, despite significant progress achieved, yet remain at high and disconcerting levels.'),
          ('18.', 'Public health', '{r:Public health and hygiene} have not received adequate attention. There is an alarming increase in {r:infectious diseases} such as Tuberculosis, Malaria, Hepatitis, HIV etc.')])
    n.boxes([['{r:governance}', 'loss of faith'], ['{r:politics}', 'criminalisation'], ['{r:economy}', 'debt-trap'], ['{r:justice}', 'near collapse'], ['{r:society}', 'education, health']], size=13)
    out.append(('03_notes_areas_of_concern_2', n))

    # ---------------- 04 Recommendations: count, FRs, property ----------------
    n = Note('NCRWC Recommendations – Fundamental Rights and Property')
    n.sub('Recommendations')
    n.para('[[249 recommendations]] In all, the commission made {r:249 recommendations}. Of them, {r:58} recommendations involve {r:amendments to the Constitution}, {r:86} involve {r:legislative measures} and the remaining {r:105} recommendations could be accomplished through {r:executive action}.')
    n.boxes([['{R:58}', 'constitutional amendments'], ['{R:86}', 'legislative measures'], ['{R:105}', 'executive action']])
    n.propbar([(58/249, '{R:58} amendments'), (86/249, '{R:86} legislative'), (105/249, '{R:105} executive action')], caption='{b:249 recommendations of the NCRWC drawn to scale}')
    n.para('[[Area-wise recommendations]] The various recommendations of the commission are mentioned below in an area-wise manner⁴:')
    n.subsub('1. On Fundamental Rights')
    L(n, [('1.', 'Wider non-discrimination', 'The scope of prohibition against discrimination ({r:under Articles 15 and 16}) should be extended to include ‘{r:ethnic or social origin, political or other opinion, property or birth}’.'),
          ('2.', 'Press freedom explicit', 'The freedom of speech and expression ({r:under Article 19}) should be expanded to include explicitly ‘{r:the freedom of the press and other media}, the freedom to hold opinions and to seek, receive and impart information and ideas’.'),
          ('3.', 'New Fundamental Rights', 'The following should be added as {r:new Fundamental Rights}:')])
    n.items([('(a)', 'Right against {r:torture, cruelty and inhuman treatment} or punishment.'), ('(b)', 'Right to {r:compensation} if a person is illegally deprived of his/her right to life or liberty.'),
             ('(c)', 'Right to {r:leave and to return to India}.'), ('(d)', 'Right to {r:privacy and family life}.'), ('(e)', 'Right to {r:rural wage employment} for a minimum of 80 days in a year.'),
             ('(f)', 'Right to {r:access to courts and tribunals and speedy justice}.'), ('(g)', 'Right to {r:equal justice and free legal aid}⁵.'),
             ('(h)', 'Right to {r:care and assistance and protection} (in case of children).'), ('(i)', 'Right to {r:safe drinking water, prevention of pollution, conservation of ecology} and sustainable development.')], indent=40, kw=False)
    L(n, [('4.', 'Right to education till 18 for girls, SC/ST', 'The right to education ({r:under Article 21-A}) should be enlarged to read as: ‘Every child shall have the right to free education until he completes the age of {r:fourteen years}; and in the case of {r:girls and members of the SCs and STs} until they complete the age of {r:eighteen years}’.'),
          ('5.', 'Preventive detention reforms', 'Two changes should be made with respect to {r:preventive detention} (under Article 22), namely, (i) the maximum period of preventive detention should be {r:six months}; and (ii) the {r:advisory board} should consist of a chairman and two other members and they should be {b:serving judges of any high court}.'),
          ('6.', 'Sikhism, Jainism, Buddhism separate', '{r:Sikhism, Jainism and Buddhism} should be treated as religions {r:separate from Hinduism} and the provisions grouping them together (under {r:Article 25}) should be deleted. At present, the word ‘Hindu’ is defined to include these religions also.'),
          ('7.', 'Ninth Schedule restricted', 'The protection from judicial review afforded by {r:Article 31-B} to the Acts and Regulations specified in the {r:Ninth Schedule} should be restricted to only those which relate to (i) {b:agrarian reforms}, (ii) {b:reservations}, and (iii) the {b:implementation of Directive Principles specified in clause (b) or (c) of Article 39}.'),
          ('8.', 'Non-suspendable rights in emergency', 'No suspension of the enforcement of the Fundamental Rights under {r:Articles 17, 23, 24, 25 and 32} in addition to those under {r:Articles 20 and 21} during the operation of a {r:national emergency} (under Article 352).')])
    n.subsub('2. On Right to Property')
    n.para('[[Recasting Article 300-A]] {r:Article 300-A} should be recast as follows:')
    L(n, [('1.', 'Public purpose', 'Deprivation or acquisition of property shall be by {r:authority of law} and only for a {r:public purpose}.'),
          ('2.', 'No arbitrariness', 'There shall be {r:no arbitrary deprivation} or acquisition of property.'),
          ('3.', 'Rehabilitation for SC/ST land', 'No deprivation or acquisition of {r:agricultural, forest and non-urban homestead land} belonging to or customarily used by the {r:SCs and STs} shall take place except by authority of law which provides for suitable {r:rehabilitation scheme} before taking possession of such land. In brief, a right to ‘{r:suitable rehabilitation}’ for the SCs and STs if their land is to be acquired.')])
    n.footnote('4', 'Chapters 3 to 10 in Volume I of the Report of the Commission contains the detailed area-wise recommendations. The summary of recommendations is given in Chapter 11 of the Report.')
    n.footnote('5', 'At present, it is a Directive Principle under Article 39-A.')
    out.append(('04_notes_recommendations_fr_property', n))

    # ---------------- 05 DPSP, FD, Parliament ----------------
    n = Note('NCRWC Recommendations – DPSP, Duties and Legislatures')
    n.subsub('3. On Directive Principles')
    L(n, [('1.', 'DPSP and Action', 'The heading of {r:Part-IV} of the Constitution should be amended to read as ‘{r:Directive Principles of State Policy and Action}’.'),
          ('2.', 'Population control', 'A new Directive Principle on {r:control of population} should be added.'),
          ('3.', 'National Education Commission', 'An independent {r:National Education Commission} should be set-up every {r:five years}.'),
          ('4.', 'Inter-Faith Commission', 'An {r:Inter-Faith Commission} should be established to promote {b:inter-religious harmony and social solidarity}.'),
          ('5.', 'Review body for DPSP', 'There must be a {r:body of high status} to review the level of implementation of the Directive Principles.'),
          ('6.', 'Employment plan', 'A strategic {r:Plan of Action} should be initiated to create a large number of {r:employment opportunities in five years}.'),
          ('7.', 'Statistical reforms', 'Implementation of the recommendations contained in the Report of the {r:National Statistical Commission (2001)}.')])
    n.subsub('4. On Fundamental Duties')
    L(n, [('1.', 'Popularise duties', 'Consideration should be given to the ways and means by which {r:Fundamental Duties could be popularized and made effective}.'),
          ('2.', 'Justice Verma Committee', 'The recommendations of the {r:Justice Verma Committee} on operationalisation of Fundamental Duties should be implemented at the earliest⁶.'),
          ('3.', 'New duties', 'The following {r:new fundamental duties} should be included in {r:Article 51-A}:')])
    n.items([('(a)', 'Duty to {r:vote at elections}, actively participate in the democratic process of governance and to {r:pay taxes}.'),
             ('(b)', 'To foster a spirit of {r:family values and responsible parenthood} in the matter of education, physical and moral well-being of children.'),
             ('(c)', 'Duty of {r:industrial organizations to provide education} to children of their employees.')], indent=40, kw=False)
    n.subsub('5. On Parliament and State Legislatures')
    L(n, [('1.', 'Codify privileges', 'The {r:privileges of legislators should be defined and delimited} for the free and independent functioning of Parliament and state legislatures.'),
          ('2.', 'No immunity for corruption', '{r:Article 105} may be amended to clarify that the immunity enjoyed by members under parliamentary privileges {r:does not cover corrupt acts} committed by them in connection with their duties in the House or otherwise. Further, no court would take cognizance of any offence arising out of a member’s action in the House without {b:prior sanction of the Speaker/Chairman}. {r:Article 194} may also be similarly amended in relation to the members of state legislatures.'),
          ('3.', 'Domicile for Rajya Sabha', 'The {r:domiciliary requirement} for eligibility to contest elections to {r:Rajya Sabha} from the concerned state should be maintained. This is essential to ensure the {b:federal character} of the Rajya Sabha.'),
          ('4.', 'End MPLADS', 'The {r:MP local area development scheme should be discontinued}.'),
          ('5.', 'ECI on office of profit', 'The {r:Election Commission} should be empowered to identify and declare the various offices under the central and state governments to be ‘{r:offices of profit}’ for the purposes of being chosen, and for being, a member of the appropriate legislature.'),
          ('6.', 'Committee on National Economy', 'Immediate steps be taken to set up a {r:Nodal Standing Committee on National Economy}.'),
          ('7.', 'Standing Constitution Committee', 'A {r:Standing Constitution Committee} of the two Houses of Parliament for {b:a priori scrutiny of constitutional amendment proposals} should be set up.'),
          ('8.', 'Legislation Committee', 'A new {r:Legislation Committee} of Parliament to oversee and coordinate legislative planning should be constituted.'),
          ('9.', 'Drop some committees', 'The existing Parliamentary Committees on {r:Estimates, Public Undertakings and Subordinate Legislation} may not be continued.'),
          ('10.', 'Parliamentary ombudsman', 'The Parliamentarians must voluntarily place themselves open to public scrutiny through a {r:parliamentary ombudsman}.'),
          ('11.', 'Minimum sitting days', 'The State Legislatures with less than {r:70 members} should meet for at least {r:50 days} in a year and other State Legislatures for at least {r:90 days}. Similarly, the minimum number of days for sittings of {r:Rajya Sabha and Lok Sabha} should be fixed at {r:100 and 120 days} respectively.'),
          ('12.', 'Procedural reform study group', 'A {r:Study Group outside Parliament} for study of procedural reforms should be set up.')])
    n.boxes([['{r:< 70 members}', '50 days'], ['{r:other states}', '90 days'], ['{r:Rajya Sabha}', '100 days'], ['{r:Lok Sabha}', '120 days']], size=13)
    n.footnote('6', 'The Government of India appointed the committee “to operationalise the suggestions to teach Fundamental Duties to the citizens of India” in the year 1998 under the chairmanship of Justice J.S. Verma. The Committee submitted its report in October 1999.')
    out.append(('05_notes_recommendations_dpsp_duties_legislatures', n))

    # ---------------- 06 Executive, Centre-State ----------------
    n = Note('NCRWC Recommendations – Executive and Centre-State')
    n.subsub('6. On Executive and Administration')
    L(n, [('1.', 'Lok Sabha elects PM (hung House)', 'In case of {r:hung Parliament}, the {r:Lok Sabha may elect the leader of the House}. He/she may then be appointed as the prime minister by the President. The same procedure could be followed at the state level also.'),
          ('2.', 'Constructive vote of no-confidence', 'A motion of no-confidence against a prime minister must be accompanied by a {r:proposal of alternative leader} to be voted simultaneously. This is called as the ‘{r:system of constructive vote of no confidence}’.'),
          ('3.', '20% for no-confidence notice', 'For a motion of no-confidence to be brought out against the government, at least {r:20 per cent} of the total number of members of the House should give notice.'),
          ('4.', 'Ministry ceiling – 10%', 'The practice of having {r:oversized Council of Ministers} should be prohibited by law. A ceiling on the number of Ministers in any State or the Union government be fixed at the maximum of {r:10 per cent} of the total strength of the popular house of the legislature.'),
          ('5.', 'Political offices – 2%', 'The practice of creating a number of {r:political offices} with the position, perks and privileges of a minister should be discouraged. Their number should be limited to {r:2 per cent} of the total strength of the lower house.'),
          ('6.', 'Lokpal & Lokayuktas', 'The Constitution should provide for appointment of {r:Lokpal} keeping the {b:prime minister outside its purview} and the institution of {r:lokayuktas} in the states.'),
          ('7.', 'Lateral entry', '{r:Lateral entry} into government jobs above {r:joint secretary level} should be allowed.'),
          ('8.', 'Amend Article 311', '{r:Article 311} should be amended to ensure not only {b:protection to the honest public servants} but {r:penalisation to dishonest ones}.'),
          ('9.', 'Civil Service Boards', 'The questions of personnel policy including placements, promotions, transfers and fast-track advancements should be managed by {r:autonomous Civil Service Boards} constituted under statutory provisions.'),
          ('10.', 'Oath of good governance', 'Officials, before starting their career, in addition to the taking of an oath of loyalty to the Constitution, should swear to abide by the {r:principles of good governance}.'),
          ('11.', 'Oath of transparency', '{r:Right to information} should be guaranteed and the traditional insistence on secrecy should be discarded. In fact, there should be an {r:oath of transparency in place of an oath of secrecy}.'),
          ('12.', 'Whistle-blower Acts', '{r:Public Interest Disclosure Acts} (which are popularly called the {r:Whistle-blower Acts}) may be enacted to fight corruption and mal-administration.'),
          ('13.', 'Forfeit benami property', 'A law should be enacted to provide for {r:forfeiture of benami property} of corrupt public servants as well as non-public servants.')])
    n.subsub('7. On Centre-State and Inter-State Relations')
    L(n, [('1.', 'ISC consultation matters', 'The {r:Inter-State Council Order of 1990} may clearly specify the matters that should form the parts of consultations.'),
          ('2.', 'Disasters in Concurrent List', '{r:Management of disasters and emergencies} (both natural and manmade) should be included in the {r:List III (Concurrent List)} of the Seventh Schedule.'),
          ('3.', 'Inter-State Trade Commission', 'A statutory body called the {r:Inter-State Trade and Commerce Commission} should be established.'),
          ('4.', 'CM consultation on Governor', 'The President should appoint the {r:governor} of a state only after {r:consultation with the chief minister} of that state.'),
          ('5.', 'Art. 356 – last resort', '{r:Article 356 should not be deleted}, but it must be used {r:sparingly and only as a remedy of the last resort}.'),
          ('6.', 'Floor test', 'The question whether the ministry in a state has lost the confidence of the assembly or not should be tested {r:only on the floor of the House}. The Governor should not be allowed to dismiss the ministry, so long as it enjoys the confidence of the House.'),
          ('7.', 'PR beyond one year', 'Even without the state being under a proclamation of emergency, {r:President’s Rule may be continued if elections cannot be held}. Article 356 should be amended to this effect.'),
          ('8.', 'No dissolution before Parliament’s approval', 'The {r:State Assembly should not be dissolved} before the proclamation issued under Article 356 has been {r:laid before Parliament}. Article 356 should be amended to ensure this.'),
          ('9.', 'River disputes – larger SC bench', '{r:River water disputes} between States and/ or the Centre should be heard and disposed by a bench of {r:not less than three judges} and if necessary, a bench of {r:five judges} of the Supreme Court for the final disposal of the suit.'),
          ('10.', 'Replace River Boards Act', 'Parliament should replace the {r:River Boards Act of 1956} with another comprehensive enactment after consultation with all the states.'),
          ('11.', 'Time-limit on reserved bills', 'When the state bill is {r:reserved for consideration of the President}, there should be a {r:time-limit (say three months)} within which the President should take a decision whether to give his/her assent or to return the bill.')])
    out.append(('06_notes_recommendations_executive_centre_state', n))

    # ---------------- 07 Judiciary, socio-economic ----------------
    n = Note('NCRWC Recommendations – Judiciary and Socio-Economic Change')
    n.subsub('8. On Judiciary')
    L(n, [('1.', 'National Judicial Commission', 'A {r:National Judicial Commission} under the Constitution should be established to recommend the appointment of judges of the Supreme Court. It should comprise the {b:chief justice of India (as chairman), two senior most Judges of the Supreme Court, the Union law minister and one person nominated by the President}.'),
          ('2.', 'Judicial accountability', 'A committee of the National Judicial Commission should examine {r:complaints of deviant behaviour} of the Supreme Court and high court judges.'),
          ('3.', 'Retirement age 65 / 68', 'The {r:retirement age} of the judges of high courts and Supreme Court should be increased to {r:65 and 68} respectively.'),
          ('4.', 'Contempt power limited', 'No court other than the {r:Supreme Court and the High Courts} should have the power to {r:punish for contempt} of itself.'),
          ('5.', 'Judicial review limited to SC/HC', 'Except for the Supreme Court and the High Courts, no other court should have the power to {r:declare the Acts of Parliament and State Legislatures as being unconstitutional} or beyond legislative competence and so ultra-vires.'),
          ('6.', 'Judicial Councils for budgets', 'A {r:National Judicial Council and Judicial Councils in States} should be set up for the preparation of plans and annual budget proposals.'),
          ('7.', 'Judgement within 90 days', 'In the Supreme Court and the High Courts, judgements should ordinarily be delivered {r:within 90 days} from the conclusion of the case.'),
          ('8.', 'Exemplary costs', 'An award of {r:exemplary costs} should be given in appropriate cases of {b:abuse of process of law}.'),
          ('9.', 'Arrears – one-year limit', 'Each High Court should prepare a {r:strategic plan for time-bound clearance of arrears} in courts within its jurisdiction. {r:No case to remain pending for more than one year}.'),
          ('10.', 'Plea-bargaining', 'The system of {r:plea-bargaining} should be introduced as part of the process of {b:decriminalization}.'),
          ('11.', 'Two-tier subordinate judiciary', 'The hierarchy of the subordinate courts in the country should be brought down to a {r:two-tier subordinate judiciary} under the High Court.')])
    n.subsub('9. On Pace of Socio-Economic Change and Development')
    L(n, [('1.', 'Diversity in higher judiciary', 'A way could and should be found to bring a reasonable number of {r:SCs, STs and BCs on to the benches} of the Supreme Court and high courts.'),
          ('2.', 'Equal competition', 'Social policy should aim at enabling the SCs, STs and BCs and with particular attention to the {r:girls} to {r:compete on equal terms} with the general category.'),
          ('3.', 'Optimal use of resources', 'Appropriate new institutions should be established to ensure that the {r:resources earmarked for the weaker sections are optimally used}.'),
          ('4.', 'Citizens’ Charters', 'The {r:Citizens’ Charters} be prepared by every service providing department/ agency to enumerate the {b:entitlements of the citizens} specifically those of the SCs, STs and other deprived classes.'),
          ('5.', 'Reservation statute – Arakshan Nyaya Adalats', '{r:Reservation} for SCs, STs and BCs should be brought under a {r:statute} covering all aspects of reservation including setting up of {r:Arakshan Nyaya Adalats} to adjudicate upon all disputes pertaining to reservation.'),
          ('6.', 'Residential schools', '{r:Residential schools} for SCs, STs and BCs should be established {r:in every district} in the country.'),
          ('7.', 'Fifth to Sixth Schedule', 'All tribal areas governed by the {r:Fifth Schedule} of the Constitution should be {r:transferred to the Sixth Schedule}. Other tribal areas should also be brought under the Sixth Schedule.'),
          ('8.', 'Special atrocity courts', '{r:Special courts} exclusively to try offences under the {r:SCs and STs (Prevention of Atrocities) Act, 1989}, should be established.'),
          ('9.', 'Enforce PCR Act', 'Prevention of {r:untouchability} requires, inter alia, effective punitive action under the {r:Protection of Civil Rights Act, 1955}.'),
          ('10.', 'End manual scavenging', 'The {r:Employment of Manual Scavengers and Construction of Dry Latrines (Prohibition) Act, 1993}, should be strictly enforced.'),
          ('11.', 'Minorities – education & representation', 'Steps should be taken for improvement of {r:educational standards} as well as for increasing the {r:political representation of the minority communities}.'),
          ('12.', 'Bonded labour authority', 'A fully empowered {r:National Authority for the Liberation and Rehabilitation of bonded labour} should be set up. Similar authorities should also be established at the state level.'),
          ('13.', 'Women’s empowerment', 'As regards {r:women}, actions covering {b:reservations, development, empowerment, health and protection against violence} should be taken.')])
    out.append(('07_notes_recommendations_judiciary_socio_economic', n))

    # ---------------- 08 Decentralisation, NE, electoral ----------------
    n = Note('NCRWC Recommendations – Local Bodies, North East and Elections')
    n.subsub('10. On Decentralisation (Panchayats and Municipalities)')
    L(n, [('1.', 'Separate fiscal domain', 'The {r:Eleventh and Twelfth Schedules} of the Constitution should be restructured in a manner that creates a {r:separate fiscal domain} for panchayats and municipalities.'),
          ('2.', 'State panchayat council', '{r:State panchayat council} should be established under the chairmanship of the {r:chief minister}.'),
          ('3.', 'Institutions of self-government', 'Panchayats and Municipalities should be categorically declared to be ‘{r:institutions of self-government}’ and {r:exclusive functions} be assigned to them. For this purpose, {b:Articles 243-G and 243-W} should be suitably amended.'),
          ('4.', 'ECI over SECs', 'The {r:Election Commission of India} should have the power to {r:issue directions to the State Election Commission} for the discharge of its functions. The State Election Commission should submit its annual or special reports to the Election Commission of India and to the Governor. This requires the amendment of {b:Articles 243-K and 243-ZA}.'),
          ('5.', 'Hearing before dissolution', '{r:Article 243-E} should be amended to the effect that a {r:reasonable opportunity of being heard} shall be given to a Panchayat before it is dissolved.'),
          ('6.', 'CAG audit of panchayats', 'To ensure uniformity in the practice relating to audit of accounts, the {r:CAG of India} should be empowered to conduct the audit or lay down {r:accounting standards for Panchayats}.'),
          ('7.', 'Report on supersession', 'Whenever a {r:Municipality is superseded}, a {r:report stating the grounds} for such dissolution should be placed before the State Legislature.'),
          ('8.', 'Single law on eligibility', 'All provisions regarding {r:qualifications and disqualifications} for elections to local authorities should be consolidated in a {r:single law}.'),
          ('9.', 'Delimitation Commission for local bodies', 'The functions of {r:delimitation, reservation and rotation of seats} should be vested in a {r:Delimitation Commission} and not in the State Election Commission.'),
          ('10.', 'Municipal tax domain', 'The concept of a {r:distinct and separate tax domain for municipalities} should be recognized.')])
    n.subsub('11. On Institutions in North East India')
    L(n, [('1.', '73rd/74th benefits for NE', 'Efforts are to be made to give all the States in this region the opportunities provided under the {r:73rd and 74th Constitutional Amendments}. However, this should be done with due regard to the {b:unique political traditions} of the region.'),
          ('2.', 'Empower ADCs', 'The subjects given under the {r:Sixth Schedule} and those mentioned in the {r:Eleventh Schedule} could be entrusted to the {r:Autonomous District Councils (ADCs)}.'),
          ('3.', 'Traditional governance', '{r:Traditional forms of governance} should be associated with self-governance because of the present dissatisfaction.'),
          ('4.', 'National Immigration Council', 'A {r:National Immigration Council} should be set up to examine a range of issues including a review of the {b:Citizenship Act, the Illegal Migrants Determination by Tribunal Act, the Foreigners Act} and so on.')])
    n.subsub('12. On Electoral Processes')
    L(n, [('1.', 'Disqualify on charges (5+ years)', 'Any person {r:charged with any offence punishable with imprisonment for a maximum term of five years or more}, should be {r:disqualified} from being chosen as or for being a member of Parliament or Legislature of a State.'),
          ('2.', 'Permanent bar for heinous crimes', 'Any person convicted for any {r:heinous crime} like murder, rape, smuggling, dacoity, etc., should be {r:permanently debarred} from contesting for any political office.'),
          ('3.', 'Special courts for politicians', '{r:Criminal cases against politicians} pending before Courts either for trial or in appeal must be disposed of speedily, if necessary, by appointing {r:Special Courts}.'),
          ('4.', 'Election benches', 'The {r:election petitions} should also be decided by {r:special courts}. In the alternative, {b:special election benches} may be constituted in the High Courts and earmarked exclusively for the disposal of election petitions and election disputes.'),
          ('5.', 'State funding deferred', 'Any system of {r:State funding of elections} bears a close nexus to the regulation of working of political parties by law and to the creation of a foolproof mechanism under law with a view to implementing the financial limits strictly. Therefore, proposals for State funding should be {r:deferred} till these regulatory mechanisms are firmly in position.'),
          ('6.', 'One constituency only', 'Candidates should {r:not be allowed to contest election simultaneously} for the same office from {r:more than one constituency}.'),
          ('7.', 'Statutory code of conduct', 'The {r:election code of conduct} should be given the {r:sanctity of law} and its violation should attract penal action.'),
          ('8.', '50% + 1 vote', 'The Commission while recognizing the beneficial potential of the system of {r:run off contest} electing the representative winning on the basis of {r:50 per cent plus one vote} polled, as against the present {b:first-past-the-post system}, for a more representative democracy, recommends that the Government and the Election Commission of India should examine this issue of prescribing a minimum of 50 per cent plus one vote for election in all its aspects.'),
          ('9.', 'Bar on serial losers', 'An {r:independent candidate who loses election three times consecutively} should be {r:permanently debarred} from contesting election to the same office.'),
          ('10.', 'Deposit threshold 25%', 'The minimum number of valid votes polled should be increased to {r:25 per cent} from the current {r:16.67 per cent} as a condition for the {b:deposit not being forfeited}.'),
          ('11.', 'Foreign-born in high offices', 'The issue of eligibility of {r:non-Indian born citizens} or those whose parents or grandparents were citizens of India to hold {r:high offices} in the realm such as President, Vice-President, Prime Minister and Chief Justice of India should be examined in depth through a political process after a {b:national dialogue}⁷.'),
          ('12.', 'Collegium for Election Commissioners', 'The {r:Chief Election Commissioner and the other Election Commissioners} should be appointed on the recommendation of a body consisting of the {b:Prime Minister, Leader of the Opposition in the Lok Sabha, Leader of the Opposition in the Rajya Sabha, the Speaker of the Lok Sabha and the Deputy Chairman of the Rajya Sabha}. Similar procedure should be adopted in the case of appointment of {r:State Election Commissioners}.')])
    n.footnote('7', 'The Commission was deeply divided on this issue and because of this, P.A. Sangma left the Commission.')
    out.append(('08_notes_recommendations_local_northeast_electoral', n))

    # ---------------- 09 Political parties, anti-defection ----------------
    n = Note('NCRWC Recommendations – Political Parties and Anti-Defection')
    n.subsub('13. On Political Parties')
    L(n, [('1.', 'Law on political parties', 'A {r:comprehensive law regulating the registration and functioning of political parties} or alliances of parties should be made. The proposed law should–')])
    n.items([('(a)', 'provide that political party or alliance should keep its {r:doors open to all citizens} irrespective of any distinctions of caste, community or the like.'),
             ('(b)', 'make it compulsory for the parties to {r:maintain accounts} of the receipt of funds and expenditure in a systematic and regular way.'),
             ('(c)', 'make it compulsory for the political parties requiring their candidates to {r:declare their assets and liabilities} at the time of filing their nomination.'),
             ('(d)', 'provide that {r:no political party should provide ticket to a candidate} if he/she was convicted by any court for any criminal offence or if the courts have framed criminal charges against him/her.'),
             ('(e)', 'specifically provide that if any party violates the above provision, the candidate involved should be liable to be {r:disqualified and the party deregistered and derecognized}.')], indent=40, kw=False)
    L(n, [('2.', 'Higher recognition threshold', 'The Election Commission should {r:progressively increase the threshold criterion for eligibility for recognition} so that the {b:proliferation of smaller political parties is discouraged}.'),
          ('3.', 'Political funding law', 'A {r:comprehensive legislation providing for regulation of contributions} to the political parties and towards election expenses should be enacted by consolidating such laws. This new law should:')])
    n.items([('(a)', 'aim at bringing {r:transparency into political funding};'), ('(b)', 'permit {r:corporate donations} within higher prescribed limits;'),
             ('(c)', 'make donations up to a specified limit {r:tax exempt};'), ('(d)', 'make both {r:donors and donees} of political funds accountable;'),
             ('(e)', 'provide that {r:audited political party accounts} should be published yearly; and'),
             ('(f)', 'provide for {r:de-recognition of the party} and enforcement of penalties for filing false election returns.')], indent=40, kw=False)
    n.subsub('14. On Anti-Defection Law')
    n.para('[[Amend Tenth Schedule]] The provisions of the {r:Tenth Schedule} of the Constitution should be amended to provide the following:')
    L(n, [('1.', 'Defectors must re-contest', 'All persons {r:defecting} (whether individually or in groups) from the party or the alliance of parties, on whose ticket they had been elected, {r:must resign} from their parliamentary or assembly seats and {r:must contest fresh elections}.'),
          ('2.', 'No office for defectors', 'The defectors should be {r:debarred to hold any public office} of a minister or any other remunerative political post for at least the duration of the remaining term of the existing legislature or until the next elections whichever is earlier.'),
          ('3.', 'Defector’s vote invalid', 'The {r:vote cast by a defector to topple a government should be treated as invalid}.'),
          ('4.', 'ECI to decide defection', 'The power to decide questions regarding {r:disqualification on ground of defection} should vest in the {r:Election Commission} instead of in the Speaker/Chairman of the House concerned.')])
    n.flow(['defect', '{r:resign + re-contest}', '{r:no office}', '{r:vote invalid}', 'decided by {R:ECI}'])
    out.append(('09_notes_recommendations_parties_anti_defection', n))
    return out
