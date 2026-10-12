from nb import Note

OUT = '/home/user/Dice/Laxminotebook/Ch39_Panchayati_Raj'
SKIP = [('Table 39.2 Articles Related to Panchayats', 'Table 39.3 Committees Related')]   # only 39.2 skipped

def notes():
    out = []

    # ---------------- 01 Intro + Balwantrai Mehta ----------------
    n = Note('CHAPTER 39 Panchayati Raj', 'Meaning of Panchayati Raj and the Balwantrai Mehta Committee.')
    n.reg('CHAPTER 39 Panchayati Raj')
    n.para('[[Rural local self-government]] The term {r:Panchayati Raj} in India signifies the system of {r:rural local self-government}. It has been established in all the states of India by the {b:Acts of the state legislatures} to build {r:democracy at the grass root level}. It is entrusted with {r:rural development}. It was {r:constitutionalised} through the {r:73rd Constitutional Amendment Act of 1992}.')
    n.para('[[Local government – State List (Entry 5)]] In the scheme of division of powers between the Centre and the states in the Indian federal system, the item of ‘{r:local Government}’ is given to the {r:states}. Thus, the {r:fifth entry of the State List} of the Seventh Schedule to the Constitution of India deals with ‘local government’.')
    n.sub('Evolution of Panchayati Raj')
    n.subsub('Balwantrai Mehta Committee')
    n.para('[[Democratic decentralisation (1957)]] In {r:January 1957}, the Government of India appointed a committee to examine the working of the {b:Community Development Programme (1952)} and the {b:National Extension Service (1953)} and to suggest measures for their better working. The chairman of this committee was {r:Balwantrai G Mehta}. The committee submitted its report in {r:November 1957} and recommended the establishment of the scheme of ‘{r:democratic decentralisation}’, which ultimately came to be known as {r:Panchayati Raj}. The specific recommendations made by it are:')
    n.items([('1.', '[[Three-tier system]] Establishment of a {r:three-tier panchayati raj system}—{b:gram panchayat at the village level, panchayat samiti at the block level and zila parishad at the district level}. These tiers should be {r:organically linked} through a device of {r:indirect elections}.'),
             ('2.', '[[Direct + indirect elections]] The {r:village panchayat} should be constituted with {r:directly elected} representatives, whereas the {r:panchayat samiti and zila parishad} should be constituted with {r:indirectly elected} members.'),
             ('3.', '[[Planning & development]] All {r:planning and development activities} should be entrusted to these bodies.'),
             ('4.', '[[Samiti executive, parishad advisory]] The {r:panchayat samiti should be the executive body} while the {r:zila parishad should be the advisory, coordinating and supervisory body}.'),
             ('5.', '[[Collector as chairman]] The {r:district collector} should be the {r:chairman of the zila parishad}.'),
             ('6.', '[[Genuine transfer of power]] There should be a {r:genuine transfer of power and responsibility} to these democratic bodies.'),
             ('7.', '[[Adequate resources]] {r:Adequate resources} should be transferred to these bodies to enable them to discharge their functions and fulfil their responsibilities.'),
             ('8.', '[[Further devolution]] A system should be evolved to effect {r:further devolution of authority} in future.')])
    n.flow(['{R:Zila Parishad} (district) – advisory', '{R:Panchayat Samiti} (block) – executive', '{R:Gram Panchayat} (village) – direct election'])
    out.append(('01_notes_ch39_intro_balwantrai_mehta', n))

    # ---------------- 02 Adoption + study teams ----------------
    n = Note('Adoption of Panchayati Raj and Study Teams')
    n.para('[[NDC acceptance (1958)]] These recommendations of the committee were accepted by the {r:National Development Council in January 1958}. The council {r:did not insist on a single rigid pattern} and left it to the states to evolve their own patterns suitable to local conditions. But the {b:basic principles and broad fundamentals should be identical} throughout the country.')
    n.para('[[Rajasthan first (1959)]] {r:Rajasthan was the first state} to establish Panchayati Raj. The scheme was inaugurated by the {r:prime minister on October 2, 1959}, in {r:Nagaur district}. Rajasthan was followed by {r:Andhra Pradesh}, which also adopted the system in {r:1959}. Thereafter, most of the states adopted the system.')
    n.flow(['Mehta report {r:Nov 1957}', 'NDC {r:Jan 1958}', 'Rajasthan – Nagaur {r:2 Oct 1959}', 'Andhra Pradesh {r:1959}'])
    n.para('[[Variations among states]] Though most of the states created Panchayati Raj institutions by the {r:mid 1960s}, there were {r:differences} from one state to another with regard to the {b:number of tiers, relative position of samiti and parishad, their tenure, composition, functions, finances} and so on. For example, {r:Rajasthan adopted the three-tier} system while {r:Tamil Nadu adopted the two-tier} system. {r:West Bengal}, on the other hand, adopted the {r:four-tier} system. Further, in the {r:Rajasthan–Andhra Pradesh pattern}, {b:panchayat samiti was powerful} as the block was the unit of planning and development, while in {r:Maharashtra–Gujarat pattern}, {b:zila parishad was powerful} as the district was the unit of planning and development. Some states also established {r:nyaya panchayats}, that is, {b:judicial panchayats} to try petty civil and criminal cases.')
    n.compare([('{R:Rajasthan–AP pattern}', ['block = unit', '{r:samiti powerful}']), ('{R:Maharashtra–Gujarat pattern}', ['district = unit', '{r:zila parishad powerful}'])])
    n.subsub('Study Teams and Committees')
    n.para('[[Study teams since 1960]] Since {r:1960}, many {r:study teams, committees and working groups} have been appointed to examine the various aspects of functioning of Panchayati Raj system. They are mentioned in {r:Table 39.1}.')
    rows = [['1.', '1960', 'Committee on Rationalisation of Panchayat Statistics', 'V.R. Rao'],
            ['2.', '1961', 'Working Group on Panchayats and Cooperatives', 'S.D. Mishra'],
            ['3.', '1961', 'Study Team on Panchayati Raj Administration', 'V. Iswaran'],
            ['4.', '1962', 'Study Team on Nyaya Panchayats', 'G.R. Rajgopal'],
            ['5.', '1963', 'Study Team on the Position of Gram Sabha in Panchayati Raj Movement', 'R.R. Diwakar'],
            ['6.', '1963', 'Study Group on Budgeting and Accounting Procedure of Panchayati Raj Institutions', 'M. Rama Krishnayya'],
            ['7.', '1963', 'Study Team on Panchayati Raj Finances', 'K. Santhanam'],
            ['8.', '1965', 'Committee on Panchayati Raj Elections', 'K. Santhanam'],
            ['9.', '1965', 'Study Team on the Audit and Accounts of Panchayati Raj Bodies', 'R.K. Khanna'],
            ['10.', '1966', 'Committee on Panchayati Raj Training Centres', 'G. Ramachandran'],
            ['11.', '1969', 'Study Team on Involvement of Community Development Agency and Panchayati Raj Institutions in the Implementation of Basic Land Reform Measures', 'V. Ramanathan'],
            ['12.', '1972', 'Working Group for Formulation of Fifth Five Year Plan on Community Development and Panchayati Raj', 'N. Ramakrishnayya'],
            ['13.', '1976', 'Committee on Community Development and Panchayati Raj', 'Smt. Daya Choubey']]
    rows = [[a, '{r:' + b + '}', c, '{b:' + d + '}'] for a, b, c, d in rows]
    n.table(['{R:Sl. No.}', '{R:Year}', '{R:Name of the study Team / Committee}', '{R:Chairman}'], rows, [50, 60, 340, 150], caption='Table 39.1 Study Teams and Committees on Panchayati Raj')
    out.append(('02_notes_adoption_study_teams', n))

    # ---------------- 03 Ashok Mehta ----------------
    n = Note('Ashok Mehta Committee')
    n.subsub('Ashok Mehta Committee')
    n.para('[[Janata Government (1977)]] In {r:December 1977}, the {r:Janata Government} appointed a committee on panchayati raj institutions under the chairmanship of {r:Ashok Mehta}. It submitted its report in {r:August 1978} and made {r:132 recommendations} to {b:revive and strengthen the declining panchayati raj system} in the country. Its main recommendations were:')
    n.items([('1.', '[[Two-tier system]] The {r:three-tier system} of panchayati raj should be {r:replaced by the two-tier system}, that is, {b:zila parishad at the district level}, and below it, the {b:mandal panchayat} consisting of a group of villages with a total population of {r:15,000 to 20,000}.'),
             ('2.', '[[District as first point]] A {r:district should be the first point for decentralisation} under popular supervision below the state level.'),
             ('3.', '[[Zila parishad executive]] {r:Zila parishad should be the executive body} and made responsible for {b:planning at the district level}.'),
             ('4.', '[[Political parties]] There should be an {r:official participation of political parties} at all levels of panchayat elections.'),
             ('5.', '[[Compulsory taxation]] The panchayati raj institutions should have {r:compulsory powers of taxation} to mobilise their own financial resources.'),
             ('6.', '[[Social audit]] There should be a regular {r:social audit} by a district level agency and by a committee of legislators to check whether the funds allotted for the vulnerable social and economic groups are actually spent on them.'),
             ('7.', '[[No supersession – elections in 6 months]] The state government {r:should not supersede} the panchayati raj institutions. In case of an imperative supersession, {r:elections should be held within six months} from the date of supersession.'),
             ('8.', '[[Separate nyaya panchayats]] The {r:nyaya panchayats should be kept as separate bodies} from that of development panchayats. They should be presided over by a {b:qualified judge}.'),
             ('9.', '[[Elections by CEO]] The {r:chief electoral officer of a state} in consultation with the chief election commissioner should organise and conduct the panchayati raj elections.'),
             ('10.', '[[Development to zila parishad]] {r:Development functions should be transferred to the zila parishad} and all development staff should work under its control and supervision.'),
             ('11.', '[[Voluntary agencies]] The {r:voluntary agencies} should play an important role in mobilising the support of the people for panchayati raj.'),
             ('12.', '[[Minister for PR]] A {r:minister for panchayati raj} should be appointed in the state council of ministers to look after the affairs of the panchayati raj institutions.'),
             ('13.', '[[SC/ST reservation]] Seats for {r:SCs and STs should be reserved} on the basis of their population.'),
             ('14.', '[[Constitutional recognition]] A {r:constitutional recognition} should be accorded to the Panchayati Raj institutions. This would give them the requisite status ({b:sanctity and stature}) and an assurance of continuous functioning.')])
    n.flow(['{R:Zila Parishad} (executive)', '{R:Mandal Panchayat} (15,000–20,000)'])
    n.para('[[No action at Centre – 3 states acted]] Due to the {r:collapse of the Janata Government} before the completion of its term, {r:no action} could be taken on the recommendations of the Ashok Mehta Committee at the central level. However, the three states of {r:Karnataka, West Bengal and Andhra Pradesh} took steps to revitalise the panchayati raj, keeping in view some of the recommendations of the Ashok Mehta Committee.')
    n.compare([('{R:Balwantrai Mehta (1957)}', ['three-tier', 'samiti executive', 'collector chairs ZP']), ('{R:Ashok Mehta (1978)}', ['two-tier', 'ZP executive', 'party participation, constitutional status'])])
    out.append(('03_notes_ashok_mehta_committee', n))

    # ---------------- 04 GVK Rao ----------------
    n = Note('G.V.K. Rao Committee')
    n.subsub('G.V.K. Rao Committee')
    n.para('[[‘Grass without roots’ (1985)]] The Committee to review the existing {b:Administrative Arrangements for Rural Development and Poverty Alleviation Programmes} under the chairmanship of {r:G.V.K. Rao} was appointed by the erstwhile {r:Planning Commission in 1985}. The Committee came to the conclusion that the developmental process was gradually {r:bureaucratised and divorced from the Panchayati Raj}. This phenomena of {b:bureaucratisation of development administration as against the democratisation} weakened the Panchayati Raj institutions resulting in what is aptly called as ‘{r:grass without roots}’. Hence, the Committee made the following recommendations to strengthen and revitalise the Panchayati Raj system:')
    n.items([('(i)', '[[Zila Parishad pivotal]] The district level body, that is, the {r:Zila Parishad should be of pivotal importance} in the scheme of democratic decentralisation. It stated that “{b:the district is the proper unit for planning and development and the Zila Parishad should become the principal body for management of all development programmes which can be handled at that level.}”'),
             ('(ii)', '[[Role in rural development]] The Panchayati Raj institutions at the district and lower levels should be assigned an important role with respect to {r:planning, implementation and monitoring} of rural development programmes.'),
             ('(iii)', '[[District planning]] Some of the {r:planning functions at the state level should be transferred to the district level} planning units for effective decentralized district planning.'),
             ('(iv)', '[[District Development Commissioner]] A post of {r:District Development Commissioner} should be created. He/she should act as the {b:chief executive officer of the Zila Parishad} and should be in charge of all the development departments at the district level.'),
             ('(v)', '[[Regular elections]] {r:Elections} to the Panchayati Raj institutions should be {r:held regularly}. It found that elections became overdue for one or more tiers in {r:11 states}.')])
    n.para('[[GVK Rao vs Dantwala & Hanumantha Rao]] Thus the committee, in its scheme of decentralised system of field administration, assigned a {r:leading role to the Panchayati Raj} in local planning and development. It is in this respect that the recommendations of the {r:G.V.K. Rao Committee Report (1986)} differed from those of the {r:Dantwala Committee Report on Block-Level Planning (1978)} and the {r:Hanumantha Rao Committee Report on District Planning (1984)}. Both the committees have suggested that the basic decentralised planning function should be done at the {r:district level}. The Hanumantha Rao Committee advocated {r:separate district planning bodies} under either the {b:District Collector or a minister}. In both the models, the {r:Collector should play a significant role} in the decentralised planning though the Committee stated that Panchayati Raj institutions would also be associated with this process (of decentralised planning). The committee recommended that the {r:Collector should be the coordinator}, at the district level, of all developmental and planning activities. Thus, the Hanumantha Rao Committee differed in this respect from those of the {b:Balwantrai Mehta Committee, the First Administrative Reforms Commission of India, the Ashok Mehta Committee and finally the G.V.K. Rao Committee} which recommended {r:reduction in the developmental role of the District Collector} and which assigned a {r:major role to the Panchayati Raj} in development administration.')
    n.compare([('{R:Hanumantha Rao (1984)}', ['separate district planning body', '{r:Collector} as coordinator']), ('{R:Mehta, ARC, Ashok Mehta, GVK Rao}', ['reduce Collector’s role', '{r:PRIs} lead development'])])
    out.append(('04_notes_gvk_rao_committee', n))

    # ---------------- 05 Singhvi + Thungon ----------------
    n = Note('L.M. Singhvi and Thungon Committees')
    n.subsub('L M Singhvi Committee')
    n.para('[[Singhvi Committee (1986)]] In {r:1986}, {r:Rajiv Gandhi government} appointed a committee to prepare a concept paper on ‘{b:Revitalisation of Panchayati Raj Institutions for Democracy and Development}’ under the chairmanship of {r:L.M. Singhvi}. It made the following recommendations.')
    n.items([('(i)', '[[Constitutional recognition – new chapter]] The Panchayati Raj institutions should be {r:constitutionally recognised, protected and preserved}. For this purpose, a {r:new chapter should be added in the Constitution} of India. This will make their identity and integrity reasonably and substantially inviolate. It also suggested constitutional provisions to ensure {r:regular, free and fair elections} to the Panchayati Raj bodies.'),
             ('(ii)', '[[Nyaya panchayats]] {r:Nyaya Panchayats} should be established for a {b:cluster of villages}.'),
             ('(iii)', '[[Gram Sabha – direct democracy]] The villages should be reorganised to make {r:Gram Panchayats more viable}. It also emphasised the importance of the {r:Gram Sabha} and called it as the {r:embodiment of direct democracy}.'),
             ('(iv)', '[[More finances]] The Village Panchayats should have {r:more financial resources}.'),
             ('(v)', '[[Judicial tribunals]] The {r:judicial tribunals} should be established in each state to adjudicate controversies about election to the Panchayati Raj institutions, their dissolution and other matters related to their functioning.')])
    n.subsub('Thungon Committee')
    n.para('[[Thungon Committee (1988)]] In {r:1988}, a {r:sub-committee of the Consultative Committee of Parliament} was constituted under the chairmanship of {r:P.K. Thungon} to examine the political and administrative structure in the district for the purpose of {b:district planning}. This committee suggested for the strengthening of the Panchayati Raj system. It made the following recommendations:')
    n.items([('1.', '[[Constitutional recognition]] The Panchayati Raj bodies should be {r:constitutionally recognized}.'),
             ('2.', '[[Three-tier]] A {r:three-tier system} of Panchayati Raj with panchayats at the village, block and district levels.'),
             ('3.', '[[Zilla Parishad as pivot]] {r:Zilla Parishad should be the pivot} of the Panchayati Raj system. It should act as the planning and development agency in the district.'),
             ('4.', '[[Five-year tenure]] The Panchayati Raj bodies should have a {r:fixed tenure of five years}.'),
             ('5.', '[[Supersession – 6 months]] The maximum period of {r:super session} of a body should be {r:six months}.'),
             ('6.', '[[State planning committee]] A {r:planning and co-ordination committee} should be set-up at the state level under the chairmanship of the {b:minister for planning}. The presidents of Zilla Parishads should be its members.'),
             ('7.', '[[List of subjects]] A {r:detailed list of subjects} for Panchayati Raj should be prepared and incorporated in the Constitution.'),
             ('8.', '[[Reservation incl. women]] {r:Reservation of seats} in all the three-tiers should be on the basis of population. There should also be {r:reservation for women}.'),
             ('9.', '[[State Finance Commission]] A {r:state finance commission} should be set-up in each state. It would lay down the criteria and guidelines for the devolution of finances to the Panchayati Raj institutions.'),
             ('10.', '[[Collector as CEO]] The {r:district collector should be the chief executive officer} of the Zilla Parishad.')])
    out.append(('05_notes_singhvi_thungon_committees', n))

    # ---------------- 06 Gadgil + constitutionalisation ----------------
    n = Note('Gadgil Committee and Constitutionalisation')
    n.subsub('Gadgil Committee')
    n.para('[[Gadgil Committee (1988)]] The {r:Committee on Policy and Programmes} was constituted in {r:1988} by the {r:Congress party} under the chairmanship of {r:V.N. Gadgil}. This committee was asked to consider the question of “{b:how best Panchayati Raj institutions could be made effective}”. In this context, the committee made the following recommendations:')
    n.items([('1.', '[[Constitutional status]] A {r:constitutional status} should be bestowed on the Panchayati Raj institutions.'),
             ('2.', '[[Three-tier]] A {r:three-tier system} of Panchayati Raj with panchayats at the village, block and district levels.'),
             ('3.', '[[Five-year term]] The term of Panchayati Raj institutions should be fixed at {r:five years}.'),
             ('4.', '[[Direct elections]] The members of the Panchayats at all the three levels should be {r:directly elected}.'),
             ('5.', '[[Reservation]] {r:Reservation for SCs, STs and women}.'),
             ('6.', '[[Planning role – list of subjects]] The Panchayati Raj bodies should have the responsibility of {r:preparation and implementation of plans} for socio-economic development. For this purpose, a {r:list of subjects should be specified in the constitution}.'),
             ('7.', '[[Taxation powers]] The Panchayat Raj bodies should be empowered to {r:levy, collect and appropriate taxes} and duties.'),
             ('8.', '[[State Finance Commission]] Establishment of a {r:State Finance Commission} for the allocation of finances to the Panchayats.'),
             ('9.', '[[State Election Commission]] Establishment of a {r:State Election Commission} for the conduction of elections to the panchayats.')])
    n.para('[[Basis of the amendment bill]] The above recommendations of the {r:Gadgil Committee} became the {r:basis for drafting an amendment bill} aimed at conferring the constitutional status and protection to the Panchayati Raj institutions.')
    n.sub('Constitutionalisation')
    n.para('[[!Rajiv Gandhi Government]] The Rajiv Gandhi Government introduced the {r:64th Constitutional Amendment Bill} in the Lok Sabha in {r:July 1989} to constitutionalise panchayati raj institutions and make them more powerful and broad based. Although, the {b:Lok Sabha passed the bill in August 1989}, it was {r:not approved by the Rajya Sabha}. The bill was vehemently opposed by the Opposition on the ground that it sought to {b:strengthen centralisation} in the federal system.')
    n.para('[[!V.P. Singh Government]] The {r:National Front Government}, soon after assuming office in {r:November 1989} under the Prime Ministership of V.P. Singh, announced that it would take steps to strengthen the panchayati raj institutions. In {r:June 1990}, a two-day {r:conference of the state chief ministers} under the chairmanship of V.P. Singh was held to discuss the issues relating to the strengthening of the panchayati raj bodies. The conference approved the proposals for the introduction of a fresh constitutional amendment bill. Consequently, a constitutional amendment bill was introduced in the Lok Sabha in {r:September 1990}. However, the {r:fall of the government resulted in the lapse of the bill}.')
    n.para('[[!Narasimha Rao Government]] The Congress Government under the prime ministership of {r:P.V. Narasimha Rao} once again considered the matter of the constitutionalisation of panchayati raj bodies. It drastically modified the proposals in this regard to {b:delete the controversial aspects} and introduced a constitutional amendment bill in the Lok sabha in {r:September, 1991}. This bill finally emerged as the {r:73rd Constitutional Amendment Act, 1992} and came into force on {r:24 April, 1993¹}.')
    n.flow(['{r:64th Bill} 1989 – failed in RS', 'V.P. Singh bill {r:1990} – lapsed', 'Narasimha Rao bill {r:1991}', '{R:73rd Amdt 1992 · in force 24 Apr 1993}'])
    n.footnote('1', 'This bill was passed by the Lok Sabha on 22 December, 1992, and by the Rajya Sabha on 23 December, 1992. Later, it was approved by the 17 state assemblies and received the assent of the President on 20 April, 1993.')
    out.append(('06_notes_gadgil_constitutionalisation', n))

    # ---------------- 07 73rd Act significance ----------------
    n = Note('73rd Amendment Act – Significance')
    n.sub('73rd Constitutional Amendment Act of 1992')
    n.subsub('Significance of the Act')
    n.para('[[Part IX & Eleventh Schedule]] This act has added a new {r:Part-IX} to the Constitution of India. This part is entitled as ‘{r:The Panchayats}’ and consists of provisions from {r:Articles 243 to 243-O}. In addition, the act has also added a new {r:Eleventh Schedule} to the Constitution. This schedule contains {r:29 functional items} of the panchayats. It deals with {r:Article 243-G}.')
    n.boxes([['{R:Part IX}', '‘The Panchayats’', 'Arts. 243 – 243-O'], ['{R:Eleventh Schedule}', '29 functional items', 'Art. 243-G']])
    n.para('[[Article 40 (DPSP) given shape]] The act has given a practical shape to {r:Article 40} of the Constitution which says that, “{b:The State shall take steps to organise village panchayats and endow them with such powers and authority as may be necessary to enable them to function as units of self-government.}” This article forms a part of the {r:Directive Principles of State Policy}.')
    n.para('[[Justiciable constitutional status]] The act gives a {r:constitutional status} to the panchayati raj institutions. It has brought them under the purview of the {r:justiciable part of the Constitution}. In other words, the state governments are under {r:constitutional obligation} to adopt the new panchayati raj system in accordance with the provisions of the act. Consequently, neither the formation of panchayats nor the holding of elections at regular intervals {r:depend on the will of the state government} any more.')
    n.para('[[Compulsory vs voluntary provisions]] The provisions of the act can be grouped into two categories—{r:compulsory and voluntary}. The {r:compulsory} (mandatory or obligatory) provisions of the act {b:have to be included} in the state laws creating the new panchayati raj system. The {r:voluntary} provisions, on the other hand, may be included at the {b:discretion of the states}. Thus the voluntary provisions of the act ensures the right of the states to take local factors like geographical, politico–administrative and others, into consideration while adopting the new panchayati raj system.')
    n.para('[[Participatory democracy]] The act is a {r:significant landmark} in the evolution of grassroot democratic institutions in the country. It transfers the {r:representative democracy into participatory democracy}. It is a {r:revolutionary concept} to build democracy at the grassroot level in the country.')
    n.flow(['representative democracy', '{R:participatory democracy}'])
    out.append(('07_notes_73rd_act_significance', n))

    # ---------------- 08 Salient features I ----------------
    n = Note('73rd Amendment Act – Salient Features I')
    n.subsub('Salient Features')
    n.para('[[Salient features]] The salient features of the act are:')
    n.para('[[!Gram Sabha]] The act provides for a {r:Gram Sabha} as the {r:foundation of the panchayati raj system}. It is a body consisting of persons {b:registered in the electoral rolls} of a village comprised within the area of Panchayat at the village level. Thus, it is a {r:village assembly consisting of all the registered voters} in the area of a panchayat. It may exercise such powers and perform such functions at the village level as the {r:legislature of a state determines}.')
    n.para('[[!Three-Tier System]] The act provides for a {r:three-tier system} of panchayati raj in every state, that is, panchayats at the {b:village, intermediate, and district levels} ². Thus, the act brings about {r:uniformity in the structure} of panchayati raj throughout the country. However, a state having a population {r:not exceeding 20 lakh} may not constitute panchayats at the {r:intermediate level}.')
    n.flow(['{R:District panchayat}', '{R:Intermediate panchayat}', '{R:Village panchayat}', '{b:Gram Sabha}'])
    n.para('[[!Election of Members and Chairpersons]] All the {r:members} of panchayats at the village, intermediate and district levels shall be {r:elected directly} by the people. Further, the {r:chairperson of panchayats at the intermediate and district levels} shall be {r:elected indirectly}—by and from amongst the elected members thereof. However, the {r:chairperson of a panchayat at the village level} shall be elected in such manner as the {r:state legislature determines}.')
    n.para('[[Right to vote]] The chairperson of a panchayat and other members of a panchayat elected directly or indirectly shall have the {r:right to vote} in the meetings of the panchayats.')
    n.para('[[!Reservation of Seats]] The act provides for the reservation of seats for {r:scheduled castes and scheduled tribes} in every panchayat ({b:i.e., at all the three levels}) in {r:proportion of their population} to the total population in the panchayat area. Further, the state legislature shall provide for the reservation of offices of {r:chairperson} in the panchayat at the village or any other level for the SCs and STs.')
    n.para('[[One-third for women]] The act provides for the reservation of {r:not less than one-third} of the total number of seats for {r:women} ({b:including the number of seats reserved for women belonging the SCs and STs}). Further, not less than one-third of the total number of offices of {r:chairpersons} in the panchayats at each level shall be reserved for women.')
    n.nested('{R:Seats for women} – not less than 1/3 of total seats', '{R:Seats of SC/ST women} – counted within', caption='{b:same rule for offices of chairpersons: not less than one-third reserved for women at each level}')
    n.para('[[Backward classes – optional]] The act also authorises the legislature of a state to make any provision for reservation of seats in any panchayat or offices of chairperson in the panchayat at any level in favour of {r:backward classes}.')
    n.para('[[SC/ST reservation till 2030]] The reservation of seats as well as the reservation of offices of chairpersons in the panchayats for the scheduled castes and scheduled tribes shall cease to have effect after the expiration of the period specified in {r:Article 334} ({b:which is presently eighty years, that is, till 2030}).')
    n.para('[[Arunachal – no SC reservation]] It must be noted here that the above provision relating to the reservation of seats in panchayats (both members and chairpersons) for the scheduled castes is {r:not applicable to the state of Arunachal Pradesh}. This is because the state is inhabited fully by {b:indigenous tribal people} and there are {r:no scheduled castes}. This provision was added later by the {r:83rd Constitutional Amendment Act of 2000}.')
    n.boxes([['{R:SC/ST}', 'by population', 'till 2030'], ['{R:Women}', '≥ 1/3 seats', '+ chairpersons'], ['{R:Backward classes}', 'optional (state)']])
    n.footnote('2', 'The Act defines all these terms in the following manner: (a) Panchayat means an institution (by whatever name called) of self-government for rural areas. (b) Village means a village specified by the governor by public notification to be a village for this purpose, and includes a group of villages so specified. (c) Intermediate level means a level between the village and district levels specified by the governor by public notification for this purpose. (d) District means a district in a state.')
    out.append(('08_notes_salient_features_1', n))

    # ---------------- 09 Salient features II ----------------
    n = Note('73rd Amendment Act – Salient Features II')
    n.para('[[!Duration of Panchayats]] The act provides for a {r:five-year term} of office to the panchayat at every level from the date of it’s first meeting. However, it {r:can be dissolved} before the completion of its term. Further, fresh elections to constitute a panchayat shall be completed (a) {b:before the expiry of its duration of five years}; or (b) in case of dissolution, {r:before the expiry of a period of six months} from the date of its dissolution.')
    n.para('[[No election if < 6 months left]] But, where the {r:remainder of the period} (for which the dissolved panchayat would have continued) is {r:less than six months}, it shall {r:not be necessary to hold any election} for constituting the new panchayat for such period.')
    n.para('[[Reconstituted – remainder only]] Moreover, a panchayat constituted upon the dissolution of a panchayat before the expiration of its duration shall continue {r:only for the remainder of the period} for which the dissolved panchayat would have continued had it not been so dissolved. In other words, a panchayat reconstituted after premature dissolution {b:does not enjoy the full period of five years} but remains in office only for the remainder of the period.')
    n.flow(['5-year term', 'dissolved early', 'election within {r:6 months}', 'new body: {r:remainder only}'])
    n.timeline([('first meeting', ''), ('premature dissolution', ''), ('fresh election', ''), ('original 5-year term ends', '')], segs=['', 'within {r:6 months}', '{r:only the remainder}'], caption='{b:if the remainder is less than six months, no election is necessary for that period}')
    n.para('[[!Disqualifications]] A person shall be disqualified for being chosen as or for being a member of panchayat if he/she is so disqualified, (a) under any law for the time being in force for the purpose of {b:elections to the legislature of the state} concerned, or (b) under any {b:law made by the state legislature}. However, no person shall be disqualified on the ground that he/she is less than 25 years of age if he/she has attained the {r:age of 21 years}. Further, all questions of disqualifications shall be referred to such authority as the {r:state legislature determines}.')
    n.para('[[!State Election Commission]] The superintendence, direction and control of the preparation of electoral rolls and the conduct of all elections to the panchayats shall be vested in the {r:state election commission}. It consists of a {r:state election commissioner} to be {r:appointed by the governor}. His/her conditions of service and tenure of office shall also be determined by the governor. He/she shall {r:not be removed} from the office except in the manner and on the grounds prescribed for the {r:removal of a judge of the state high court} ³. His/her conditions of service shall {b:not be varied to his/her disadvantage} after his/her appointment.')
    n.para('[[Election law by state]] The {r:state legislature} may make provision with respect to all matters relating to {r:elections to the panchayats}.')
    n.para('[[!Powers and Functions]] The state legislature may endow the Panchayats with such powers and authority as may be necessary to enable them to function as {r:institutions of self-government}. Such a scheme may contain provisions for the {r:devolution of powers and responsibilities} upon Panchayats at the appropriate level with respect to (a) the {b:preparation of plans for economic development and social justice} and (b) the {b:implementation of schemes for economic development and social justice} as may be entrusted to them, including those in relation to the {r:29 matters listed in the Eleventh Schedule}.')
    n.para('[[!Finances]] The state legislature may (a) {r:authorise a panchayat to levy, collect and appropriate} taxes, duties, tolls and fees; (b) {r:assign to a panchayat} taxes, duties, tolls and fees levied and collected by the state government; (c) provide for making {r:grants-in-aid} to the panchayats from the consolidated fund of the state; and (d) provide for {r:constitution of funds} for crediting all moneys of the panchayats.')
    n.tree(['{r:own taxes}', '{r:assigned taxes}', '{r:grants-in-aid}', '{r:panchayat funds}'])
    n.para('[[!Finance Commission]] The {r:governor} of a state shall, {r:after every five years}, constitute a {r:finance commission} to review the financial position of the panchayats. It shall make the following recommendations to the Governor:')
    n.items([('1.', '[[Principles of devolution]] The principles that should govern: (a) The {r:distribution between the state and the panchayats} of the net proceeds of the taxes, duties, tolls and fees levied by the state and allocation of shares amongst the panchayats at all levels. (b) The {r:determination of taxes}, duties, tolls and fees that may be assigned to the panchayats. (c) The {r:grants-in-aid} to the panchayats from the consolidated fund of the state.'),
             ('2.', '[[Improve finances]] The {r:measures needed to improve the financial position} of the panchayats.'),
             ('3.', '[[Other matters]] Any other matter referred to it by the governor in the interests of {r:sound finance} of the panchayats.')])
    n.para('[[Composition by state law]] The {r:state legislature} may provide for the {r:composition of the commission}, the required qualifications of its members and the manner of their selection.')
    n.para('[[Action taken report]] The {r:governor shall place the recommendations} of the commission along with the {r:action taken report} before the state legislature.')
    n.para('[[Central Finance Commission role]] The {r:Central Finance Commission} shall also suggest the measures needed to {r:augment the consolidated fund of a state} to supplement the resources of the panchayats in the states ({b:on the basis of the recommendations made by the finance commission of the state}).')
    n.footnote('3', 'A judge of a high court can be removed from his/her office by the President on the recommendation of the Parliament. This means that a state election commissioner cannot be removed by the governor, though appointed by him/her.')
    out.append(('09_notes_salient_features_2', n))

    # ---------------- 10 Salient features III + Eleventh Schedule ----------------
    n = Note('73rd Amendment Act – Salient Features III and Eleventh Schedule')
    n.para('[[!Audit of Accounts]] The {r:state legislature} may make provisions with respect to the {r:maintenance of accounts} by the panchayats and the {r:auditing} of such accounts.')
    n.para('[[!Application to Union Territories]] The provisions of this Part are {r:applicable to the Union territories}. But, the {r:President} may direct that they would apply to a Union territory subject to such {b:exceptions and modifications} as he/she may specify.')
    n.para('[[!Exempted States and Areas]] The act {r:does not apply to the states of Nagaland, Meghalaya and Mizoram} and certain other areas. These areas include, (a) the {r:scheduled areas and the tribal areas} in the states⁴; (b) the {r:hill areas of Manipur} for which district councils exist; and (c) {r:Darjeeling district of West Bengal} for which Darjeeling Gorkha Hill Council exists.')
    n.boxes([['{R:States}', 'Nagaland, Meghalaya, Mizoram'], ['{R:Areas}', 'scheduled & tribal areas'], ['{R:Manipur}', 'hill areas'], ['{R:West Bengal}', 'Darjeeling']], size=13)
    n.para('[[PESA extension]] However, the {r:Parliament may extend} the provisions of this Part to the scheduled areas and tribal areas subject to such exceptions and modifications as it may specify. Under this provision, the Parliament has enacted the “{r:Provisions of the Panchayats (Extension to the Scheduled Areas) Act}”, {r:1996}, popularly known as the {r:PESA Act or the Extension Act}.')
    n.para('[[!Continuance of Existing Laws and Panchayats]] All the state laws relating to panchayats shall continue to be in force until the {r:expiry of one year} from the commencement of this act. In other words, the states have to adopt the new panchayati raj system based on this act within the maximum period of one year from {r:24 April, 1993}, which was the date of the commencement of this act. However, all the panchayats existing immediately before the commencement of act shall {b:continue till the expiry of their term}, unless dissolved by the state legislature sooner.')
    n.para('[[State acts 1993–94]] Consequently, majority of states passed the panchayati raj acts in {r:1993 and 1994} to adopt the new system in accordance with the 73rd Constitutional Amendment Act of 1992.')
    n.para('[[!Bar to Interference by Courts in Electoral Matters]] The act {r:bars the interference by courts} in the electoral matters of panchayats. It declares that the validity of any law relating to the {r:delimitation of constituencies} or the {r:allotment of seats} to such constituencies {r:cannot be questioned in any court}. It further lays down that no election to any panchayat is to be questioned except by an {r:election petition} presented to such authority and in such manner as provided by the state legislature.')
    n.para('[[!Eleventh Schedule]] It contains the following {r:29 functional items} placed within the purview of panchayats:')
    items = ['Agriculture, including agricultural extension', 'Land improvement, implementation of land reforms, land consolidation and soil conservation',
             'Minor irrigation, water management and watershed development', 'Animal husbandry, dairying and poultry', 'Fisheries', 'Social forestry and farm forestry',
             'Minor forest produce', 'Small-scale industries, including food processing industries', 'Khadi, village and cottage industries', 'Rural housing',
             'Drinking water', 'Fuel and fodder', 'Roads, culverts, bridges, ferries, waterways and other means of communication',
             'Rural electrification, including distribution of electricity', 'Non-conventional energy sources', 'Poverty alleviation programme',
             'Education, including primary and secondary schools', 'Technical training and vocational education', 'Adult and non-formal education', 'Libraries',
             'Cultural activities', 'Markets and fairs', 'Health and sanitation including hospitals, primary health centres and dispensaries', 'Family welfare',
             'Women and child development', 'Social welfare, including welfare of the handicapped and mentally retarded',
             'Welfare of the weaker sections, and in particular, of the scheduled castes and the scheduled tribes', 'Public distribution system',
             'Maintenance of community assets.']
    n.items([(f'{i+1}.', t) for i, t in enumerate(items)], kw=False, size=14)
    n.footnote('4', 'At present, ten states of India have scheduled areas. These are: Andhra Pradesh, Telangana, Jharkhand, Chhatisgarh, Gujarat, Himachal Pradesh, Madhya Pradesh, Maharashtra, Odisha and Rajasthan. Presently, there are a total of ten tribal areas (autonomous districts) in the four states of Assam (3), Meghalaya (3), Tripura (1) and Mizoram (3).')
    out.append(('10_notes_salient_features_3_eleventh_schedule', n))

    # ---------------- 11 Compulsory and voluntary ----------------
    n = Note('Compulsory and Voluntary Provisions')
    n.sub('Compulsory and Voluntary Provisions')
    n.para('[[Mandatory vs discretionary features]] Now, we will identify separately the {r:compulsory} (obligatory or mandatory) and {r:voluntary} (discretionary or optional) provisions (features) of the 73rd Constitutional Amendment Act (1992) or the Part IX of the Constitution:')
    n.subsub('A. Compulsory Provisions')
    n.items([('1.', 'Organisation of {r:Gram Sabha} in a village or group of villages.'),
             ('2.', 'Establishment of panchayats at the {r:village, intermediate and district levels}.'),
             ('3.', '{r:Direct elections} to all seats in panchayats at the village, intermediate and district levels.'),
             ('4.', '{r:Indirect elections} to the post of chairperson of panchayats at the intermediate and district levels.'),
             ('5.', '{r:Voting rights} of the chairperson and other members of a panchayat elected directly or indirectly.'),
             ('6.', '{r:21 years} to be the minimum age for contesting elections to panchayats.'),
             ('7.', 'Reservation of seats (both members and chairpersons) for {r:SCs and STs} in panchayats at all the three levels.'),
             ('8.', 'Reservation of {r:one-third seats} (both members and chairpersons) for {r:women} in panchayats at all the three levels.'),
             ('9.', 'Fixing {r:tenure of five years} for panchayats at all levels and holding fresh elections within {r:six months} in the event of supersession of any panchayat.'),
             ('10.', 'Establishment of a {r:State Election Commission} for conducting elections to the panchayats.'),
             ('11.', 'Constitution of a {r:State Finance Commission} after every five years to review the financial position of the panchayats.')], kw=False)
    n.subsub('B. Voluntary Provisions')
    n.items([('1.', 'Endowing the {r:Gram Sabha with powers} and functions at the village level.'),
             ('2.', 'Determining the {r:manner of election of the chairperson of the village panchayat}.'),
             ('3.', 'Giving {r:representation to the chairpersons of the village panchayats} in the intermediate panchayats or in the case of a state not having intermediate panchayats, in the district panchayats.'),
             ('4.', 'Giving representation to the {r:chairpersons of the intermediate panchayats} in the district panchayats.'),
             ('5.', 'Giving representation to {r:members of the Parliament} (both the Houses) and the {r:state legislature} (both the Houses) in the panchayats at different levels falling within their constituencies.'),
             ('6.', 'Providing reservation of seats (both members and chairpersons) for {r:backward classes} in panchayats at any level.'),
             ('7.', 'Granting {r:powers and authority} to the panchayats to enable them to function as institutions of self-government (in brief, making them {b:autonomous bodies}).'),
             ('8.', '{r:Devolution of powers and responsibilities} upon panchayats to prepare plans for economic development and social justice; and to perform some or all of the {r:29 functions} listed in the Eleventh Schedule of the Constitution.'),
             ('9.', 'Granting {r:financial powers} to the panchayats, that is, authorizing them to levy, collect and appropriate taxes, duties, tolls and fees.'),
             ('10.', '{r:Assigning to a panchayat the taxes}, duties, tolls and fees levied and collected by the state government.'),
             ('11.', 'Making the {r:grants-in-aid} to the panchayats from the consolidated fund of the state.'),
             ('12.', 'Providing for {r:constitution of funds} for crediting all moneys of the panchayats.')], kw=False)
    n.compare([('{R:Compulsory}', ['structure, elections', 'reservation SC/ST/women', 'tenure, SEC, SFC']), ('{R:Voluntary}', ['powers, functions, finances', 'OBC reservation', 'MP/MLA representation'])])
    out.append(('11_notes_compulsory_voluntary_provisions', n))

    # ---------------- 12 PESA intro + objectives ----------------
    n = Note('PESA Act of 1996 – Objectives')
    n.sub('Pesa Act of 1996 (Extension Act)')
    n.para('[[Fifth Schedule areas]] The provisions of {r:Part IX} of the constitution relating to the Panchayats are {r:not applicable to the Fifth Schedule areas}. However, the {r:Parliament may extend} these provisions to such areas, subject to such exceptions and modifications as it may specify. Under this provision, the Parliament has enacted the “{r:Provisions of the Panchayats (Extension to the Scheduled Areas) Act}”, {r:1996}, popularly known as the {r:PESA Act or the Extension Act}.')
    n.para('[[Ten Fifth Schedule states]] At present, {r:ten states have Fifth Schedule Areas}. These are: {b:Andhra Pradesh, Telangana, Chhatisgarh, Gujarat, Himachal Pradesh, Jharkhand, Madhya Pradesh, Maharashtra, Odisha and Rajasthan}. All the ten states have enacted requisite {r:compliance legislations} by amending the respective Panchayati Raj Acts.')
    n.subsub('Objectives of the Act')
    n.para('[[Objectives]] The objectives of the PESA Act are as follows⁵:')
    n.items([('1.', '[[Extend Part IX]] To {r:extend the provisions of Part IX} of the Constitution relating to the panchayats to the scheduled areas with certain modifications'),
             ('2.', '[[Tribal self-rule]] To provide {r:self-rule} for the bulk of the {r:tribal population}'),
             ('3.', '[[Gram sabha as nucleus]] To have {r:village governance with participatory democracy} and to make the {r:gram sabha a nucleus} of all activities'),
             ('4.', '[[Traditional framework]] To evolve a suitable {r:administrative framework consistent with traditional practices}'),
             ('5.', '[[Preserve customs]] To {r:safeguard and to preserve the traditions and customs} of tribal communities'),
             ('6.', '[[Tribal-specific powers]] To {r:empower panchayats} at the appropriate levels with specific powers conducive to {r:tribal requirements}'),
             ('7.', '[[No usurpation from above]] To {r:prevent panchayats at the higher level from assuming the powers} and authority of panchayats at the lower level of the gram sabha')])
    n.footnote('5', 'S.K. Singh, Panchayats in Scheduled Areas, Kurukshetra, May 2001, p. 26.')
    out.append(('12_notes_pesa_objectives', n))

    # ---------------- 13 PESA features ----------------
    n = Note('PESA Act of 1996 – Features')
    n.subsub('Features of the Act')
    n.para('[[Features of PESA]] The features (or the provisions) of the PESA Act are as follows:')
    n.items([('1.', '[[Customary law]] A state legislation on the Panchayats in the Scheduled Areas shall be in consonance with the {r:customary law, social and religious practices and traditional management practices} of community resources.'),
             ('2.', '[[Village as habitation]] A {r:village} shall ordinarily consist of a {r:habitation or a group of habitations or a hamlet} or a group of hamlets comprising a community and managing its affairs in accordance with traditions and customs.'),
             ('3.', '[[Gram Sabha in every village]] Every village shall have a {r:Gram Sabha} consisting of persons whose names are included in the electoral rolls for the Panchayat at the village level.'),
             ('4.', '[[Gram Sabha preserves culture]] Every Gram Sabha shall be competent to {r:safeguard and preserve the traditions and customs} of the people, their cultural identity, community resources and the customary mode of dispute resolution.'),
             ('5.', '[[Approves plans, identifies beneficiaries]] Every Gram Sabha shall— (i) {r:approve of the plans, programmes and projects} for social and economic development before they are taken up for implementation by the Panchayat at the village level; and (ii) be responsible for the {r:identification of beneficiaries} under the poverty alleviation and other programmes.'),
             ('6.', '[[Utilisation certificate]] Every Panchayat at the village level shall be required to obtain from the Gram Sabha a {r:certification of utilisation of funds} for the above plans, programmes and projects.'),
             ('7.', '[[ST reservation ≥ 1/2, all chairpersons]] The reservation of seats in the Scheduled Areas in every Panchayat shall be in proportion to the population of the communities for whom reservation is sought to be given under Part IX of the Constitution. However, the reservation for the {r:Scheduled Tribes shall not be less than one-half} of the total number of seats. Further, {r:all seats of Chairpersons} of Panchayats at all levels shall be {r:reserved for the Scheduled Tribes}.'),
             ('8.', '[[Nomination ≤ 1/10]] The state government may {r:nominate} such Scheduled Tribes which have no representation in the Panchayat at the intermediate level or the Panchayat at the district level. But such nomination shall {r:not exceed one-tenth} of the total members to be elected in that Panchayat.'),
             ('9.', '[[Consultation on land acquisition]] The Gram Sabha or the Panchayats at the appropriate level shall be {r:consulted before making the acquisition of land} in the Scheduled Areas for development projects and before {r:resettling or rehabilitating} persons affected by such projects in the Scheduled Areas. However, the actual planning and implementation of the projects in the Scheduled Areas shall be coordinated at the {b:state level}.'),
             ('10.', '[[Minor water bodies]] Planning and management of {r:minor water bodies} in the Scheduled Areas shall be entrusted to Panchayats at the appropriate level.'),
             ('11.', '[[Mining lease – recommendation mandatory]] The recommendations of the Gram Sabha or the Panchayats at the appropriate level shall be {r:mandatory for grant of prospecting licence or mining lease for minor minerals} in the Scheduled Areas.'),
             ('12.', '[[Auction of minor minerals]] The {r:prior recommendation} of the Gram Sabha or the Panchayats at the appropriate level shall be mandatory for grant of {r:concession for the exploitation of minor minerals by auction}.'),
             ('13.', '[[Specific powers to Gram Sabha]] While endowing Panchayats in the Scheduled Areas with such powers and authority as may be necessary to enable them to function as institutions of self-government, a State Legislature shall ensure that the Panchayats at the appropriate level and the Gram Sabha are endowed specifically with— (i) the power to {r:enforce prohibition} or to regulate or restrict the sale and consumption of any intoxicant (ii) the {r:ownership of minor forest produce} (iii) the power to {r:prevent alienation of land} in the Scheduled Areas and to take appropriate action to restore any unlawfully alienated land of a Scheduled Tribe (iv) the power to {r:manage village markets} (v) the power to exercise {r:control over money lending} to the Scheduled Tribes (vi) the power to exercise {r:control over institutions and functionaries} in all social sectors (vii) the power to {r:control local plans and resources} for such plans including tribal sub-plans'),
             ('14.', '[[No usurpation]] The State Legislations shall contain {r:safeguards} to ensure that Panchayats at the higher level {r:do not assume the powers} and authority of any Panchayat at the lower level or of the Gram Sabha.'),
             ('15.', '[[Sixth Schedule pattern]] The State Legislature shall endeavour to follow the {r:pattern of the Sixth Schedule} to the Constitution while designing the administrative arrangements in the Panchayats at district levels in the Scheduled Areas.'),
             ('16.', '[[Inconsistent laws lapse in one year]] Any provision of any law (relating to Panchayats in the Scheduled Areas) which is {r:inconsistent} with the provisions of this Act shall {r:cease to be in force at the expiry of one year} from the date on which this Act receives the assent of the President ⁶. However, all the Panchayats existing immediately before such date shall continue till the expiry of their term, unless dissolved by the State Legislature sooner.')])
    n.boxes([['{r:prohibition}'], ['{r:minor forest produce}'], ['{r:land alienation}'], ['{r:village markets}']], size=13)
    n.boxes([['{r:money lending}'], ['{r:social sector institutions}'], ['{r:local plans & tribal sub-plans}']], size=13)
    n.footnote('6', 'This Act received the assent of the President on 24 December, 1996.')
    out.append(('13_notes_pesa_features', n))

    # ---------------- 14 Finances ----------------
    n = Note('Finances of Panchayati Raj')
    n.sub('Finances of Panchayati Raj')
    n.para('[[2nd ARC on PRI finances]] The {r:Second Administrative Reforms Commission} of India (2005–2009) has summarized the {r:sources of revenue} of the Panchayati Raj Institutions (PRIs) and their {r:financial problems} in the following way⁷:')
    n.items([('1.', '[[Sources of funds]] A major portion of Part IX of the Constitution deals with {r:structural empowerment} of the PRIs but the real strength in terms of both {b:autonomy and efficiency} of these institutions is dependent on their {r:financial position} (including their capacity to generate own resources). In general, Panchayats in our country receive funds in the following ways: (i) {r:Grants from the Union Government} based on the recommendations of the {b:Central Finance Commission} as per {r:Article 280} of the Constitution. (ii) {r:Devolution from the State Government} based on the recommendations of the {b:State Finance Commission} as per {r:Article 243-I}. (iii) {r:Loans / grants} from the State Government. (iv) {r:Programme-specific allocation} under Centrally Sponsored Schemes and Additional Central Assistance. (v) {r:Internal Resource Generation} (tax and non-tax).'),
             ('2.', '[[Weak fiscal empowerment]] Across the country, States have {r:not given adequate attention to fiscal empowerment} of the Panchayats. The Panchayats own resources are {r:meager}. {b:Kerala, Karnataka and Tamil Nadu} are the states which are considered to be progressive in PRIs empowerment but even there, the Panchayats are {r:heavily dependent on government grants}. One can draw the following broad conclusions: (i) {r:Internal resource generation} at the Panchayat level is {r:weak}. This is partly due to a {b:thin tax domain} and partly due to Panchayats own {b:reluctance in collecting revenue}. (ii) Panchayats are {r:heavily dependent on grants} from Union and State Governments. (iii) A major portion of the grants both from Union as well as the State Governments is {r:scheme specific}. Panchayats have {b:limited discretion and flexibility} in incurring expenditure. (iv) In view of their own tight fiscal position, State Governments are {r:not keen to devolve funds} to Panchayats. (v) In most of the critical Eleventh Schedule matters like {b:primary education, healthcare, water supply, sanitation and minor irrigation} even now, it is the {r:State Government which is directly responsible} for implementation of these programmes and hence expenditure. (vi) Overall, a situation has been created where Panchayats have {r:responsibility but grossly inadequate resources}.'),
             ('3.', '[[Own resources – the soul]] Though, in absolute terms, the quantum of funds the Union/State Government transfers to a Panchayat forms the major component of its receipt, the {r:PRI’s own resource generation is the soul} behind its financial standing. It is not only a question of resources; it is the existence of a {r:local taxation system} which ensures {b:people’s involvement} in the affairs of an elected body. It also makes the institution {r:accountable to its citizens}.'),
             ('4.', '[[Gram Panchayats better placed]] In terms of own resource collection, the {r:Gram Panchayats are comparatively in a better position} because they have a {r:tax domain of their own}, while the other two tiers are dependent only on {b:tolls, fees and non-tax revenue} for generating internal resources.'),
             ('5.', '[[Taxation mostly with village level]] State Panchayati Raj Acts have given {r:most of the taxation powers to Village Panchayats}. The revenue domain of the intermediate and District Panchayats (both tax as well as non-tax) has been kept {r:much smaller} and remains confined to secondary areas like {b:ferry services, markets, water and conservancy services, registration of vehicles, cess on stamp duty} and a few others.'),
             ('6.', '[[Village Panchayat taxes]] A study of various State Legislations indicates that a number of taxes, duties, tolls and fees come under the jurisdiction of the {r:Village Panchayats}. These interalia include {b:property/house tax, profession tax, land tax/cess, taxes/tolls on vehicles, entertainment tax/fees, license fees, tax on non-agriculture land, fee on registration of cattle, sanitation/drainage/conservancy tax, water rate/ tax, lighting rate/tax, education cess and tax on fairs and festivals}.')])
    n.tree(['{r:Union (Art. 280)}', '{r:State (Art. 243-I)}', '{r:loans / grants}', '{r:CSS / ACA}', '{r:own resources}'], size=13)
    n.footnote('7', 'Second Administrative Reforms Commission, Government of India, Report on Local Governance, 2007, pp. 151–154.')
    out.append(('14_notes_finances_of_panchayati_raj', n))

    # ---------------- 15 Reasons for ineffective performance ----------------
    n = Note('Reasons for Ineffective Performance')
    n.sub('Reasons for Ineffective Performance')
    n.para('[[Sub-optimal performance]] Even after conferring the constitutional status and protection through the 73rd Amendment Act (1992), the performance of the Panchayati Raj Institutions (PRIs) has {r:not been satisfactory} and not upto the expected level. The various reasons for this {r:sub-optimal performance} are as follows⁸:')
    n.items([('1.', '[[!Lack of adequate devolution:]] Many States have not taken adequate steps to devolve {r:3Fs (i.e., functions, funds and functionaries)} to the PRIs to enable them to discharge their constitutionally stipulated function. Further, it is imperative that the PRIs have {b:resources to match the responsibilities} entrusted to them. While SFCs (state finance commissions) have submitted their recommendations, {r:not many few States have implemented} these or taken steps to ensure the fiscal viability of the PRIs.'),
             ('2.', '[[!Excessive control by bureaucracy:]] In some States, the Gram Panchayats have been placed in a {r:position of subordination}. Hence, the Gram Panchayat Sarpanches have to spend extraordinary amount of time visiting {b:Block Offices for funds and/or technical approval}. These interactions with the Block staff office {r:distort the role of Sarpanches} as elected representatives.'),
             ('3.', '[[!Tied nature of funds:]] This has two implications. The activities stated under a certain scheme are {r:not always appropriate for all parts of the district}. This results in {r:unsuitable activities being promoted or an under-spend} of the funds.'),
             ('4.', '[[!Overwhelming dependency on government funding:]] A review of money received and own source funds shows the {r:overwhelming dependence of Panchayats on government funding}. When Panchayats do not raise resources and instead receive funds from outside, people are {r:less likely to request a social audit}.'),
             ('5.', '[[!Reluctance to use fiscal powers:]] An important power devolved to GP (Gram Panchayat) is the right to {b:levy tax on property, business, markets, fairs} and also for services provided, like street lighting or public toilets, etc. {r:Very few Panchayats use their fiscal power} to levy and collect taxes. The argument pushed by Panchayat heads is that it is {r:difficult to levy tax on your own constituency}, especially when you live in the community.'),
             ('6.', '[[!Status of the Gram Sabha:]] Empowering the Gram Sabhas could have been a powerful weapon for {b:transparency, accountability and for involvement of the marginalized sections}. However, a number of the State Acts have {r:not spelt the powers of Gram Sabhas} nor have any procedures been laid down for the functioning of these bodies or penalties for the officials.'),
             ('7.', '[[!Creation of Parallel Bodies:]] Often, {r:Parallel Bodies (PBs)} are created for supposedly speedy implementation and greater accountability. However, there is little evidence to show that such PBs have avoided the evils including that of {b:partisan politics, sharing of spoils, corruption and elite capture}. Missions (in particular) often bypassing mainstream programmes, create {r:disconnect, duality, and alienation} between the existing and the new structures and functions. PBs {r:usurp the legitimate space of PRIs} and demoralize the PRIs by virtue of their superior resource endowments.'),
             ('8.', '[[!Poor Infrastructure:]] A number of Gram Panchayats in the country do not have even {r:full time Secretary and also basic office buildings}. The {r:database for planning, monitoring} etc., are lacking in most of the cases.')])
    n.venn3(['{R:Functions}', '{R:Funds}', '{R:Functionaries}'], '{K:3Fs}', caption='{b:lack of adequate devolution of the 3Fs to PRIs – the first reason for sub-optimal performance}')
    n.para('[[Capacity deficit of representatives]] A large number of elected representatives of PRIs are {r:semi-literate or illiterate} and know little about their roles & responsibilities, programmes, procedures, systems. Often for want of {r:good, relevant and periodic training}, they are not able to perform their functions properly.')
    n.boxes([['{r:3Fs not devolved}'], ['{r:bureaucratic control}'], ['{r:tied funds}'], ['{r:grant dependence}']], size=13)
    n.boxes([['{r:no own taxes}'], ['{r:weak Gram Sabha}'], ['{r:parallel bodies}'], ['{r:poor infrastructure}']], size=13)
    n.footnote('8', 'Ministry of Panchayati Raj, Government of India, Roadmap for the Panchayati Raj (2011–16), pp. 11–12, 23 and 7–8.')
    out.append(('15_notes_reasons_ineffective_performance', n))

    # ---------------- 16 Table 39.3 ----------------
    n = Note('Committees After Constitutionalisation')
    rows = [['1.', 'Task Force on Devolution of Powers and Functions to Panchayati Raj Institutions', '{b:Lalit Mathur}', '{r:2001}', '{r:2001}'],
            ['2.', 'Expert Group on Planning at the Grassroots Level', '{b:V. Ramachandran}', '{r:2005}', '{r:2006}'],
            ['3.', 'Task Force for Preparation of a Manual for District Planning', '{b:Smt. Rajwant Sandhu}', '{r:2008}', '{r:2008}'],
            ['4.', 'Committee on Restructuring of DRDA (District Rural Development Agency)', '{b:V. Ramachandran}', '{r:2010}', '{r:2012}'],
            ['5.', 'Expert Committee on Leveraging Panchayats for Efficient Delivery of Public Goods and Services', '{b:Mani Shankar Aiyar}', '{r:2013}', '{r:2012}']]
    n.table(['{R:Sl. No.}', '{R:Name of the Committee}', '{R:Chairman}', '{R:Appointed in}', '{R:Reported in}'], rows, [50, 300, 120, 65, 65],
            caption='Table 39.3 Committees Related to Panchayati Raj (After Constitutionalisation)')
    out.append(('16_notes_table_39_3_committees', n))
    return out
