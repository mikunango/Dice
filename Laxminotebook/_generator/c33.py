from nb import Note

OUT = '/home/user/Dice/Laxminotebook/Ch33_State_Legislature'
SKIP = [('Table 33.2 Strength of Legislative Assemblies', None)]   # 33.2, 33.3, 33.4 skipped

def notes():
    out = []

    # ---------------- 01 Intro & organisation ----------------
    n = Note('CHAPTER 33 State Legislature', 'Intro and organisation of state legislatures.')
    n.reg('CHAPTER 33 State Legislature')
    n.para('[[Constitutional basis (Arts. 168–212)]] The state legislature occupies a {r:pre-eminent and central position} in the political system of a state. {r:Articles 168 to 212} in {r:Part VI} of the Constitution deal with the {b:organisation, composition, duration, officers, procedures, privileges, powers} and so on of the state legislature. Though these are {r:similar to that of Parliament}, there are some differences as well.')
    n.section('ORGANISATION OF STATE LEGISLATURE')
    n.para('[[Six bicameral states]] There is {r:no uniformity} in the organisation of state legislatures. Most of the states have an {r:unicameral system}, while others have a {r:bicameral system}. At present, {r:only six states have two Houses} (bicameral). These are {r:Andhra Pradesh, Telangana, Uttar Pradesh, Bihar, Maharashtra and Karnataka}. The {b:Jammu and Kashmir Legislative Council was abolished} by the Jammu and Kashmir Reorganisation Act, 2019.¹ The {b:Tamil Nadu Legislative Council Act, 2010 has not come into force}. The Legislative Council in {b:Andhra Pradesh was revived} by the Andhra Pradesh Legislative Council Act, 2005. The {r:7th Amendment Act of 1956} provided for a Legislative Council in {r:Madhya Pradesh}. However, a notification to this effect has to be made by the President. So far, {b:no such notification has been made}. Hence, Madhya Pradesh continues to have one House only.')
    n.tree(['{r:Andhra Pradesh}', '{r:Telangana}', '{r:Uttar Pradesh}', '{r:Bihar}', '{r:Maharashtra}', '{r:Karnataka}'], size=13)
    n.para('[[Unicameral vs bicameral]] The {r:twenty-two states} have a {r:unicameral system}. Here, the state legislature consists of the {b:governor and the legislative assembly}. In the states having {r:bicameral system}, the state legislature consists of the {b:governor, the legislative council and the legislative assembly}. The {r:legislative council (Vidhan Parishad)} is the {b:upper house (second chamber or house of elders)}, while the {r:legislative assembly (Vidhan Sabha)} is the {b:lower house (first chamber or popular house)}.')
    n.compare([('{R:Unicameral (22 states)}', ['Governor', '+ Legislative Assembly']), ('{R:Bicameral (6 states)}', ['Governor', '+ Legislative Council (upper)', '+ Legislative Assembly (lower)'])])
    n.para('[[Creation / abolition of councils (Art. 169)]] The Constitution ({r:Article 169}) provides for the {r:abolition or creation of legislative councils} in states. Accordingly, the {r:Parliament} can abolish a legislative council (where it already exists) or create it (where it does not exist), if the {r:legislative assembly} of the concerned state passes a {r:resolution} to that effect. Such a specific resolution must be passed by the state assembly by a {r:special majority}, that is, {b:a majority of the total membership of the assembly and a majority of not less than two-thirds of the members of the assembly present and voting}. This Act of Parliament is {r:not to be deemed as an amendment of the Constitution} for the purposes of {r:Article 368} and is passed like an ordinary piece of legislation ({b:ie, by simple majority}).')
    n.flow(['Assembly resolution ({r:special majority})', 'Parliament law ({r:simple majority})', 'council created / abolished', '{b:not Art. 368 amendment}'])
    n.footnote('1', 'The erstwhile state of Jammu and Kashmir had adopted a bicameral legislature by its own state Constitution, which was separate from the Indian Constitution.')
    out.append(('01_notes_ch33_intro_organisation', n))

    # ---------------- 02 Council history ----------------
    n = Note('Second Chamber in States – Rationale and History')
    n.quote('[[Constituent Assembly criticism]] “The idea of having a {r:second chamber in the states} was criticised in the Constituent Assembly on the ground that it was {r:not representative of the people}, that it {r:delayed legislative process} and that it was an {r:expensive institution}².”')
    n.para('[[Optional council – state’s choice]] Consequently the provision was made for the abolition or creation of a legislative council to enable a state to have a second chamber or not according to its own {r:willingness and financial strength}. For example, {r:Andhra Pradesh} got the legislative council {b:created in 1957} and got the same {b:abolished in 1985}. The Legislative Council in Andhra Pradesh was again {b:revived in 2007}, after the enactment of the Andhra Pradesh Legislative Council Act, 2005. The legislative council of {r:Tamil Nadu} had been {b:abolished in 1986} and that of {r:Punjab and West Bengal in 1969}.')
    n.flow(['AP: created {r:1957}', 'abolished {r:1985}', 'revived {r:2007}'])
    n.para('[[Tamil Nadu case]] In {r:2010}, the Legislative Assembly of {r:Tamil Nadu} passed a resolution for the {r:revival} of the Legislative Council in the state. Accordingly, the Parliament enacted the {b:Tamil Nadu Legislative Council Act, 2010} which provided for the creation of Legislative Council in the state. However, before this Act was enforced, the Legislative Assembly of Tamil Nadu passed another resolution in {r:2011} seeking the {r:abolition} of the proposed Legislative Council.')
    n.flow(['TN abolished {r:1986}', '2010: revival resolution + Act', '2011: {r:abolition resolution}'])
    n.para('[[Laws under Art. 169]] The various laws made by the Parliament (under {r:Article 169} of the constitution) for the abolition or creation of State Legislative Councils are mentioned in {r:Table 33.4}.')
    n.footnote('2', 'M.P. Jain, Indian Constitutional Law, Wadhwa Fourth edition, p. 159.')
    out.append(('02_notes_second_chamber_history', n))

    # ---------------- 03 Composition of Assembly ----------------
    n = Note('Composition of Legislative Assembly')
    n.section('COMPOSITION OF TWO HOUSES')
    n.subsub('Composition of Assembly')
    n.para('[[!Strength]] The legislative assembly consists of representatives {r:directly elected} by the people on the basis of {r:universal adult franchise}. Its {r:maximum strength is fixed at 500} and {r:minimum strength at 60}. It means that its strength varies from 60 to 500 depending on the {b:population size} of the state. However, in case of {r:Arunachal Pradesh, Sikkim and Goa}, the minimum number is fixed at {r:30} and in case of {r:Mizoram and Nagaland}, it is {r:40 and 46} respectively. Further, some members of the legislative assemblies in {b:Sikkim and Nagaland} are also {b:elected indirectly}.')
    n.boxes([['{R:Max 500}'], ['{R:Min 60}'], ['{r:30}', 'Arunachal, Sikkim, Goa'], ['{r:40 / 46}', 'Mizoram / Nagaland']])
    n.para('[[Table 33.2 reference]] The strength of legislative assemblies is indicated in {r:Table 33.2}.')
    n.para('[[!Nominated Member]] Before {r:2020}, the {r:Governor} nominated {r:one member from the Anglo-Indian community³} to the assembly, if the community was not adequately represented. Originally, this provision was to operate for {b:ten years (i.e., upto 1960)} only. Later, this duration has been extended continuously since then by ten years each time. The last extension upto 2020 was made by the {r:95th Amendment Act, 2009}. But, the {r:104th Amendment Act, 2019}, has {r:not extended} further the operation of this provision. In other words, the Amendment {b:discontinued this provision} of special representation of the Anglo-Indian community in the Assembly by nomination. Consequently, this provision {r:ceased to have effect on the 25th January, 2020}.')
    n.flow(['1950: 10 years', 'extended every 10 years', '{r:95th Amdt} → 2020', '{r:104th Amdt}: ended {r:25 Jan 2020}'])
    n.para('[[!Territorial Constituencies]] For the purpose of holding direct elections to the assembly, each state is divided into {r:territorial constituencies}. The demarcation of these constituencies is done in such a manner that the {r:ratio between the population of each constituency and the number of seats} allotted to it is the {r:same throughout the state}. In other words, the Constitution ensures that there is {r:uniformity of representation} between different constituencies in the state. The expression ‘{r:population}’ means, the population as ascertained at the {b:last preceding census} of which the relevant figures have been published.')
    n.para('[[!Readjustment after each census]] After each census, a readjustment is to be made in the (a) {b:total number of seats} in the assembly of each state and (b) the {b:division of each state into territorial constituencies}. The {r:Parliament} is empowered to determine the authority and the manner in which it is to be made. Accordingly, Parliament has enacted the {r:Delimitation Commission Acts in 1952, 1962, 1972 and 2002} for this purpose.')
    n.para('[[Freeze till 2026]] The {r:42nd Amendment Act of 1976} had {r:frozen} total number of seats in the assembly of each state and the division of such state into territorial constituencies {r:till the year 2000 at the 1971 level}. This ban on readjustment has been extended for another years ({r:i.e., upto year 2026}) by the {r:84th Amendment Act of 2001} with the same objective of {b:encouraging population limiting measures}.')
    n.para('[[Delimitation on 2001 census]] The 84th Amendment Act of 2001 also empowered the government to undertake {r:readjustment and rationalisation} of territorial constituencies in a state on the basis of the population figures of {r:1991 census}. Later, the {r:87th Amendment Act of 2003} provided for the delimitation of constituencies on the basis of {r:2001 census} and not 1991 census. However, this can be done {b:without altering the total number of seats} in the assembly of each state.')
    n.flow(['{r:42nd Amdt 1976}: freeze at 1971 till 2000', '{r:84th Amdt 2001}: till 2026 (1991 census)', '{r:87th Amdt 2003}: 2001 census'])
    n.para('[[!Reservation of seats for SCs and STs]] The Constitution provided for the reservation of seats for {r:scheduled castes and scheduled tribes} in the assembly of each state on the basis of {r:population ratios}.⁴')
    n.para('[[Reservation till 2030]] Originally, this reservation was to operate for {b:ten years (i.e., up to 1960)}. But this duration has been extended continuously since then by 10 years each time. Now, under the {r:104th Amendment Act of 2019}, this reservation is to last {r:until 2030}.')
    n.para('[[Reserved seats – Table 33.2]] The seats reserved for SCs and STs in the legislative assemblies is indicated in {r:Table 33.2}.')
    n.footnote('3', 'An Anglo-Indian means a person whose father or any other male progenitor in the male line is or was of European descent, but who is domiciled within the territory of India and is or was born within such territory of parents habitually resident therein and not established there for temporary purposes only.')
    n.footnote('4', 'This means that the number of assembly seats reserved in a state for such castes and tribes is to bear the same proportion to the total number of seats in the assembly as the population of such castes and tribes in the concerned state bears to the total population of the state.')
    out.append(('03_notes_composition_of_assembly', n))

    # ---------------- 04 Composition of Council + duration ----------------
    n = Note('Composition of Council and Duration of Houses')
    n.subsub('Composition of Council')
    n.para('[[!Strength]] Unlike the members of the legislative assembly, the members of the legislative council are {r:indirectly elected}. The {r:maximum strength} of the council is fixed at {r:one-third of the total strength of the assembly} and the {r:minimum strength is fixed at 40}. It means that the size of the council depends on the size of the assembly of the concerned state. This is done to ensure the {b:predominance of the directly elected House (assembly)} in the legislative affairs of the state. Though the Constitution has fixed the maximum and the minimum limits, the {r:actual strength of a Council is fixed by Parliament}.')
    n.boxes([['{R:Max}', '1/3 of Assembly'], ['{R:Min}', '40'], ['{R:Actual}', 'fixed by Parliament']])
    n.para('[[Council strength – Table 33.2]] The strength of legislature councils is indicated in {r:Table 33.2}.')
    n.para('[[!Manner of Election]] Of the total number of members of a legislative council:')
    n.items([('1.', '[[Local bodies – 1/3]] {r:1/3} are elected by the members of {r:local bodies} in the state like municipalities, district boards, etc.,'),
             ('2.', '[[Graduates – 1/12]] {r:1/12} are elected by {r:graduates} of three years standing and residing within the state,'),
             ('3.', '[[Teachers – 1/12]] {r:1/12} are elected by {r:teachers} of three years standing in the state, not lower in standard than secondary school,'),
             ('4.', '[[MLAs – 1/3]] {r:1/3} are elected by the {r:members of the legislative assembly} of the state from amongst persons who are not members of the assembly, and'),
             ('5.', '[[Governor’s nominees – 1/6]] the {r:remainder are nominated by the governor} from amongst persons who have a special knowledge or practical experience of {b:literature, science, art, cooperative movement and social service}.')])
    n.boxes([['{r:1/3}', 'local bodies'], ['{r:1/12}', 'graduates'], ['{r:1/12}', 'teachers'], ['{r:1/3}', 'MLAs'], ['{r:1/6}', 'Governor nominates']], size=13)
    n.para('[[5/6 elected, 1/6 nominated – STV]] Thus, {r:5/6} of the total number of members of a legislative council are {r:indirectly elected} and {r:1/6 are nominated by the governor}. The members are elected in accordance with the system of {r:proportional representation by means of a single transferable vote}.')
    n.para('[[Tentative scheme]] This scheme of composition of a legislative council as laid down in the Constitution is {r:tentative and not final}. The {r:Parliament is authorised to modify or replace} the same. However, it has {b:not enacted any such law so far}.')
    n.section('DURATION OF TWO HOUSES')
    n.subsub('Duration of Assembly')
    n.para('[[Assembly – five years, dissolvable]] Like the {r:Lok Sabha}, the legislative assembly is {r:not a continuing chamber}. Its normal term is {r:five years} from the date of its first meeting after the general elections. The expiration of the period of five years operates as {b:automatic dissolution} of the assembly. However, the {r:governor is authorised to dissolve} the assembly at any time (i.e., even before the completion of five years) to pave the way for fresh elections. Further, the term of the assembly can be {r:extended during the period of national emergency} by a law of Parliament for {r:one year at a time} (for any length of time). However, this extension cannot continue beyond a period of {r:six months after the emergency} has ceased to operate. This means that the assembly should be re-elected within six months after the revocation of emergency.')
    n.subsub('Duration of Council')
    n.para('[[Council – permanent body]] Like the {r:Rajya Sabha}, the legislative council is a {r:continuing chamber}, that is, it is a {r:permanent body} and is {r:not subject to dissolution}. But, {r:one-third of its members retire on the expiration of every second year}. So, a member continues as such for {r:six years}. The vacant seats are filled up by fresh elections and nominations (by governor) at the beginning of every third year. The retiring members are also eligible for {b:re-election and re-nomination any number of times}.')
    n.compare([('{R:Assembly}', ['not continuing', '{r:5 years}', 'Governor can dissolve', '{b:+1 year in emergency}']), ('{R:Council}', ['{r:permanent}', 'not dissolved', '{r:1/3 retire every 2 years}', '{b:6-year term}'])])
    out.append(('04_notes_composition_of_council_duration', n))

    # ---------------- 05 Membership: qualifications, disqualifications ----------------
    n = Note('Membership – Qualifications and Disqualifications')
    n.section('MEMBERSHIP OF STATE LEGISLATURE')
    n.sub('1. Qualifications')
    n.para('[[Constitutional qualifications]] The Constitution lays down the following qualifications for a person to be chosen a member of the state legislature.')
    n.items([('1.', '[[Citizenship]] He/she must be a {r:citizen of India}.'),
             ('2.', '[[Oath before ECI-authorised person]] He/she must make and subscribe to an {r:oath or affirmation} before the person authorised by the {r:Election Commission} for this purpose. In his/her oath or affirmation, he/she swears – 1. To bear true faith and allegiance to the Constitution of India 2. To uphold the sovereignty and integrity of India'),
             ('3.', '[[Age – 30 / 25]] He/she must be not less than {r:30 years} of age in the case of the {r:legislative council} and not less than {r:25 years} of age in the case of the {r:legislative assembly}.'),
             ('4.', '[[Other qualifications by Parliament]] He/she must possess {r:other qualifications prescribed by Parliament}.')])
    n.para('[[RPA 1951 – additional qualifications]] Accordingly, the Parliament has laid down the following additional qualifications in the {r:Representation of People Act (1951)}:')
    n.items([('1.', '[[Council – elector + resident]] A person to be elected to the {r:legislative council} must be an {r:elector for an assembly constituency} in the concerned state and to be qualified for the governor’s nomination, he/she must be a {r:resident in the concerned state}.'),
             ('2.', '[[Assembly – elector]] A person to be elected to the {r:legislative assembly} must be an {r:elector for an assembly constituency} in the concerned state.'),
             ('3.', '[[Reserved seats]] He/she must be a member of a {r:scheduled caste or scheduled tribe} if he/she wants to contest a seat reserved for them. However, a member of scheduled castes or scheduled tribes {b:can also contest a seat not reserved} for them.')])
    n.sub('2. Disqualifications')
    n.para('[[Constitutional disqualifications]] Under the Constitution, a person shall be disqualified for being chosen as and for being a member of the legislative assembly or legislative council of a state:')
    n.items([('1.', '[[Office of profit]] if he/she holds any {r:office of profit} under the Union or state government ({b:except that of a minister or any other office exempted by state legislature⁵}),'),
             ('2.', '[[Unsound mind]] if he/she is of {r:unsound mind} and stands so declared by a court,'),
             ('3.', '[[Insolvency]] if he/she is an {r:undischarged insolvent},'),
             ('4.', '[[Foreign allegiance]] if he/she is {r:not a citizen of India} or has voluntarily acquired the citizenship of a foreign state or is under any acknowledgement of allegiance to a foreign state, and'),
             ('5.', '[[Law of Parliament]] if he/she is so disqualified under {r:any law made by Parliament}.')])
    n.para('[[RPA 1951 – additional disqualifications]] Accordingly, the Parliament has prescribed a number of additional disqualifications in the {r:Representation of People Act (1951)}. These are {b:similar to those for Parliament}. These are mentioned here:')
    n.items([('1.', '[[Electoral offences]] He/she must not have been found guilty of certain {r:electoral offences or corrupt practices} in the elections.'),
             ('2.', '[[Conviction – 2 years]] He/she must not have been {r:convicted for any offence resulting in imprisonment for two or more years}. But, the detention of a person under a {b:preventive detention law is not a disqualification}.'),
             ('3.', '[[Election expenses]] He/she must not have failed to {r:lodge an account of his/her election expenses} within the time.'),
             ('4.', '[[Government contracts]] He/she must not have any {r:interest in government contracts}, works or services.'),
             ('5.', '[[Government corporations – 25%]] He/she must not be a director or managing agent nor hold an office of profit in a corporation in which the government has {r:at least 25 per cent share}.'),
             ('6.', '[[Dismissal for corruption]] He/she must not have been {r:dismissed from government service for corruption or disloyalty} to the state.'),
             ('7.', '[[Enmity / bribery]] He/she must not have been convicted for {r:promoting enmity between different groups} or for the offence of {r:bribery}.'),
             ('8.', '[[Social crimes]] He/she must not have been punished for preaching and practicing {r:social crimes} such as {b:untouchability, dowry and sati}.')])
    n.para('[[Governor decides – on ECI opinion]] On the question whether a member has become subject to any of the above disqualifications, the {r:governor’s decision is final}. However, he/she should obtain the {r:opinion of the Election Commission} and act accordingly.')
    n.flow(['disqualification question', 'opinion of {r:Election Commission}', '{R:Governor decides (final)}'])
    n.footnote('5', 'A minister in the union or state government is not considered as holding an office of profit. Also, the state legislature can declare that a particular office of profit will not disqualify its holder from its membership.')
    out.append(('05_notes_membership_qualifications_disqualifications', n))

    # ---------------- 06 Defection, oath, vacation ----------------
    n = Note('Defection, Oath and Vacation of Seats')
    n.subsub('Disqualification on Ground of Defection')
    n.para('[[Tenth Schedule]] The Constitution also lays down that a person shall be disqualified for being a member of either House of state legislature if he/she is so disqualified on the ground of {r:defection} under the provisions of the {r:Tenth Schedule}.')
    n.para('[[Speaker/Chairman decides – Kihoto Hollohan]] The question of disqualification under the Tenth Schedule is decided by the {r:Chairman}, in the case of legislative council and, {r:Speaker}, in the case of legislative assembly ({b:and not by the governor}). In {r:Kihoto Hollohan case⁶ (1992)}, the Supreme Court ruled that the decision of Chairman/Speaker in this regard is {r:subject to judicial review}.')
    n.compare([('{R:General disqualification}', ['decided by {r:Governor}', 'on {b:ECI opinion}']), ('{R:Defection (Tenth Schedule)}', ['decided by {r:Speaker / Chairman}', '{b:judicial review – Kihoto (1992)}'])])
    n.sub('3. Oath or Affirmation')
    n.para('[[Oath before Governor]] Every member of either House of state legislature, before taking his/her seat in the House, has to make and subscribe an {r:oath or affirmation before the governor} or some person appointed by him/her for this purpose.')
    n.para('[[Contents of oath]] In this oath, a member of the state legislature swears:')
    n.items([('1.', 'to bear {r:true faith and allegiance to the Constitution} of India;'), ('2.', 'to uphold the {r:sovereignty and integrity} of India; and'), ('3.', 'to {r:faithfully discharge the duty} of his/her office.')])
    n.para('[[No oath – no vote]] Unless a member takes the oath, he/she {r:cannot vote and participate} in the proceedings of the House and does not become eligible to the {b:privileges and immunities} of the state legislature.')
    n.para('[[Penalty ₹500 per day]] A person is liable to a {r:penalty of ₹500 for each day} he/she sits or votes as a member in a House:')
    n.items([('1.', '[[Without oath]] {r:before taking and subscribing the prescribed oath} or affirmation; or'),
             ('2.', '[[Knowingly unqualified]] when he/she knows that he/she is {r:not qualified or that he/she is disqualified} for its membership; or'),
             ('3.', '[[Prohibited by law]] when he/she knows that he/she is {r:prohibited from sitting or voting} in the House by virtue of any law made by the Parliament or the state legislature.')])
    n.para('[[Salaries by state legislature]] The members of a state legislature are entitled to receive such {r:salaries and allowances} as may from time to time be determined by the {r:state legislature}.')
    n.sub('4. Vacation of Seats')
    n.para('[[Vacation of seats]] In the following cases, a member of the state legislature vacates his/her seat:')
    n.items([('1.', '[[!Double Membership:]] A person {r:cannot be a member of both Houses} of state legislature at one and the same time. If a person is elected to both the Houses, his/her seat in one of the Houses falls vacant as per the provisions of a {b:law made by the state legislature}.'),
             ('2.', '[[!Disqualification:]] If a member of the state legislature becomes subject to any of the {r:disqualifications}, his/her seat becomes vacant.'),
             ('3.', '[[!Resignation:]] A member may {r:resign} from his/her seat by writing to the {b:Chairman of legislative council or Speaker of legislative assembly}, as the case may be. The seat falls vacant when the {r:resignation is accepted⁷}.'),
             ('4.', '[[!Absence:]] A House of the state legislature can declare the seat of a member vacant if he/she absents himself/herself from all its meeting for a period of {r:sixty days without its permission}.'),
             ('5.', '[[!Other Cases:]] A member has to vacate his/her seat in the either House of state legislature, 1. if his/her {r:election is declared void} by the court, 2. if he/she is {r:expelled by the House}, 3. if he/she is elected to the office of {r:president or office of vice-president}, and 4. if he/she is appointed to the office of {r:governor} of a state.')])
    n.boxes([['{r:double membership}'], ['{r:disqualification}'], ['{r:resignation}'], ['{r:absence 60 days}'], ['{r:other cases}']], size=13)
    n.footnote('6', 'Kihoto Hollohan vs. Zachillhu (1992).')
    n.footnote('7', 'However, the Chairman/Speaker need not accept the resignation if he/she is satisfied that it is not voluntary or genuine.')
    out.append(('06_notes_defection_oath_vacation', n))

    # ---------------- 07 Speaker, Deputy Speaker ----------------
    n = Note('Presiding Officers – Speaker and Deputy Speaker')
    n.section('PRESIDING OFFICERS OF STATE LEGISLATURE')
    n.para('[[Four presiding officers]] Each House of state legislature has its own presiding officer. There is a {r:Speaker and a Deputy Speaker} for the legislative assembly and a {r:Chairman and a Deputy Chairman} for the legislative council. A {b:panel of chairman for the assembly} and a {b:panel of vice-chairman for the council} is also appointed.')
    n.compare([('{R:Assembly}', ['Speaker', 'Deputy Speaker', '{b:panel of chairman}']), ('{R:Council}', ['Chairman', 'Deputy Chairman', '{b:panel of vice-chairman}'])])
    n.para('[[Salaries charged on CFS]] The salaries and allowances of the Speaker and the Deputy Speaker of the assembly and the Chairman and the Deputy Chairman of the council are {r:fixed by the state legislature}. They are {r:charged on the Consolidated Fund of the State} and thus are {b:not subject to the annual vote} of the state legislature.')
    n.subsub('Speaker of Assembly')
    n.para('[[Election of Speaker]] The Speaker is {r:elected by the assembly itself} from amongst its members.')
    n.para('[[Vacation of Speaker’s office]] Usually, the Speaker remains in office during the {r:life of the assembly}. However, he/she vacates his/her office earlier in any of the following three cases:')
    n.items([('1.', 'if he/she {r:ceases to be a member} of the assembly;'), ('2.', 'if he/she {r:resigns by writing to the deputy speaker}; and'),
             ('3.', 'if he/she is {r:removed by a resolution} passed by a {r:majority of all the then members} of the assembly ({b:i.e., an effective majority}). Such a resolution can be moved only after giving {r:14 days advance notice}.')], kw=False)
    n.para('[[Powers of Speaker]] The Speaker has the following powers and duties:')
    n.items([('1.', '[[Order and decorum]] He/she maintains {r:order and decorum} in the assembly for conducting its business and regulating its proceedings. This is his/her {b:primary responsibility} and he/she has {r:final power} in this regard.'),
             ('2.', '[[Final interpreter]] He/she is the {r:final interpreter} of the provisions of (a) the Constitution of India, (b) the rules of procedure and conduct of business of assembly, and (c) the legislative precedents, within the assembly.'),
             ('3.', '[[Quorum]] He/she {r:adjourns the assembly or suspends the meeting} in the absence of a quorum.'),
             ('4.', '[[Casting vote]] He/she {r:does not vote in the first instance}. But, he/she can exercise a {r:casting vote} in the case of a tie.'),
             ('5.', '[[Secret sitting]] He/she can allow a ‘{r:secret}’ sitting of the House at the request of the {b:leader of the House}.'),
             ('6.', '[[Money Bill certification]] He/she {r:decides whether a bill is a Money Bill} or not and his/her decision on this question is {r:final}.'),
             ('7.', '[[Anti-defection authority]] He/she decides the questions of {r:disqualification} of a member of the assembly, arising on the ground of {r:defection} under the provisions of the Tenth Schedule.'),
             ('8.', '[[Committees]] He/she {r:appoints the chairman of all the committees} of the assembly and supervises their functioning. He/she is the chairman of the {b:Business Advisory Committee, the Rules Committee and the General Purpose Committee}.')])
    n.subsub('Deputy Speaker of Assembly')
    n.para('[[Election of Deputy Speaker]] Like the Speaker, the Deputy Speaker is also {r:elected by the assembly itself} from amongst its members. He/she is elected {b:after the election of the Speaker} has taken place.')
    n.para('[[Vacation of Deputy Speaker’s office]] Like the Speaker, the Deputy Speaker remains in office usually during the life of the assembly. However, he/she also vacates his/her office earlier in any of the following three cases:')
    n.items([('1.', 'if he/she {r:ceases to be a member} of the assembly;'), ('2.', 'if he/she {r:resigns by writing to the speaker}; and'),
             ('3.', 'if he/she is {r:removed by a resolution} passed by a majority of all the then members of the assembly ({b:i.e., an effective majority}). Such a resolution can be moved only after giving {r:14 days’ advance notice}.')], kw=False)
    n.para('[[Acts as Speaker]] The Deputy Speaker performs the duties of the Speaker’s office when it is {r:vacant}. He/she also acts as the Speaker when the latter is {r:absent} from the sitting of assembly. In both the cases, he/she has {r:all the powers of the Speaker}.')
    n.para('[[Panel of chairman]] The {r:Speaker nominates} from amongst the members a {r:panel of chairman}. Any one of them can preside over the assembly in the absence of the Speaker or the Deputy Speaker. He/she has the {b:same power as the speaker} when so presiding. He/she holds office until a new panel of chairman is nominated.')
    out.append(('07_notes_speaker_deputy_speaker', n))

    # ---------------- 08 Chairman, Deputy Chairman, sessions ----------------
    n = Note('Chairman, Deputy Chairman and Sessions')
    n.subsub('Chairman of Council')
    n.para('[[Election of Chairman]] The Chairman is {r:elected by the council itself} from amongst its members.')
    n.para('[[Vacation of Chairman’s office]] The Chairman vacates his/her office in any of the following three cases:')
    n.items([('1.', 'if he/she {r:ceases to be a member} of the council;'), ('2.', 'if he/she {r:resigns by writing to the deputy chairman}; and'),
             ('3.', 'if he/she is {r:removed by a resolution} passed by a majority of all the then members of the council ({b:i.e., an effective majority}). Such a resolution can be moved only after giving {r:14 days advance notice}.')], kw=False)
    n.para('[[Speaker’s special power]] As a presiding officer, the power and functions of the Chairman in the council are {r:similar to those of the Speaker} in the assembly. However, the Speaker has {r:one special power} which is not enjoyed by the Chairman. The Speaker decides whether a bill is a {r:Money Bill} or not and his/her decision on this question is final.')
    n.subsub('Deputy Chairman of Council')
    n.para('[[Election of Deputy Chairman]] Like the Chairman, the Deputy Chairman is also {r:elected by the council itself} from amongst its members.')
    n.para('[[Vacation of Deputy Chairman’s office]] The deputy chairman vacates his/her office in any of the following three cases:')
    n.items([('1.', 'if he/she {r:ceases to be a member} of the council;'), ('2.', 'if he/she {r:resigns by writing to the Chairman}; and'),
             ('3.', 'if he/she is {r:removed by a resolution} passed by a majority of all the then members of the council ({b:i.e., an effective majority}). Such a resolution can be moved only after giving {r:14 days advance notice}.')], kw=False)
    n.para('[[Acts as Chairman]] The Deputy Chairman performs the duties of the Chairman’s office when it is {r:vacant}. He/she also acts as the Chairman when the latter is {r:absent} from the sitting of the council. In both the cases, he/she has {r:all the powers of the Chairman}.')
    n.para('[[Panel of vice-chairman]] The {r:Chairman nominates} from amongst the members a {r:panel of vice-chairman}. Any one of them can preside over the council in the absence of the Chairman or the Deputy Chairman. He/she has the {b:same powers as the chairman} when so presiding. He/she holds office until a new panel of vice-chairman is nominated.')
    n.table(['{R:Officer}', '{R:Resigns to}', '{R:Removal}'],
            [['Speaker', 'Deputy Speaker', '{r:effective majority} · 14 days notice'], ['Deputy Speaker', 'Speaker', '{r:effective majority} · 14 days notice'],
             ['Chairman', 'Deputy Chairman', '{r:effective majority} · 14 days notice'], ['Deputy Chairman', 'Chairman', '{r:effective majority} · 14 days notice']], [170, 170, 260], src=False)
    n.section('SESSIONS OF STATE LEGISLATURE')
    n.subsub('Summoning')
    n.para('[[Summoning – six-month gap]] The {r:governor} from time to time {r:summons} each House of state legislature to meet. The {r:maximum gap between the two sessions} of state legislature cannot be more than {r:six months}, ie, the state legislature should meet {r:at least twice a year}. A session of the state legislature consists of many sittings.')
    n.subsub('Adjournment')
    n.para('[[Adjournment]] An {r:adjournment} suspends the work in a sitting for a {r:specified time} which may be hours, days or weeks.')
    n.para('[[Adjournment sine die]] {r:Adjournment sine die} means terminating a sitting of the state legislature for an {r:indefinite period}. The power of the adjournment as well as adjournment sine die lies with the {r:presiding officer} of the House.')
    n.subsub('Prorogation')
    n.para('[[Prorogation by Governor]] The presiding officer (Speaker or Chairman) declares the House adjourned sine die, when the business of the session is completed. Within the next few days, the {r:governor} issues a notification for {r:prorogation} of the session.')
    n.para('[[Prorogation ends session]] However, the governor can also prorogue the House which is in session. Unlike an adjournment, a {r:prorogation terminates a session} of the House.')
    n.flow(['{r:Summoning} (Governor)', 'sittings', '{r:Adjournment} (presiding officer)', '{r:Prorogation} (Governor)', '{r:Dissolution} (assembly only)'])
    n.subsub('Dissolution')
    n.para('[[Dissolution ends the House]] The {r:legislative council}, being a permanent house, is {r:not subject to dissolution}. Only the {r:legislative assembly} is subject to dissolution. Unlike a prorogation, a dissolution {r:ends the very life of the existing House}, and a new House is constituted after the general elections are held.')
    n.para('[[Lapsing of bills]] The position with respect to {r:lapsing of bills} on the dissolution of the assembly is mentioned below:')
    n.items([('1.', '[[Pending in assembly – lapses]] A Bill {r:pending in the assembly lapses} (whether originating in the assembly or transmitted to it by the council).'),
             ('2.', '[[Passed by assembly, pending in council – lapses]] A Bill {r:passed by the assembly but pending in the council lapses}.'),
             ('3.', '[[Pending in council only – survives]] A Bill {r:pending in the council but not passed by the assembly does not lapse}.'),
             ('4.', '[[Pending assent – survives]] A Bill passed by the assembly (in a unicameral state) or passed by both the houses (in a bicameral state) but {r:pending assent of the governor or the President does not lapse}.'),
             ('5.', '[[Returned by President – survives]] A Bill passed by the assembly (in a unicameral state) or passed by both the Houses (in a bicameral state) but {r:returned by the president for reconsideration} of House (s) {r:does not lapse}.')])
    n.compare([('{R:Lapses ✘}', ['pending in assembly', 'passed by assembly, pending in council']), ('{R:Does not lapse ✔}', ['pending in council only', 'pending assent', 'returned by President'])])
    out.append(('08_notes_chairman_deputy_chairman_sessions', n))

    # ---------------- 09 Quorum, voting, language, ministers ----------------
    n = Note('Quorum, Voting, Language and Rights of Ministers')
    n.subsub('Quorum')
    n.para('[[Quorum – 10 or 1/10]] {r:Quorum} is the minimum number of members required to be present in the House before it can transact any business. It is {r:ten members or one-tenth} of the total number of members of the House ({b:including the presiding officer}), {r:whichever is greater}. If there is no quorum during a meeting of the House, it is the duty of the presiding officer either to {b:adjourn the House or to suspend the meeting} until there is a quorum.')
    n.subsub('Voting in House')
    n.para('[[Simple majority & casting vote]] All matters at any sitting of either House are decided by a {r:majority of votes of the members present and voting} excluding the presiding officer. Only a few matters which are specifically mentioned in the Constitution, require either {b:effective majority or special majority}, not simple majority. The presiding officer (i.e., Speaker in the case of assembly or chairman in the case of council or the person acting as such) {r:does not vote in the first instance}, but exercises a {r:casting vote} in the case of an equality of votes.')
    n.subsub('Language in State Legislature')
    n.para('[[Official language, Hindi or English]] The Constitution has declared the {r:official language(s) of the state or Hindi or English}, to be the languages for transacting business in the state legislature. However, the presiding officer can permit a member to address the House in his/her {r:mother-tongue}.')
    n.para('[[English after 15 years]] The state legislature is authorised to decide whether to continue or discontinue {r:English as a floor language} after the completion of {r:fifteen years} from the commencement of the Constitution ({b:i.e., from 1965}). In case of {r:Himachal Pradesh, Manipur, Meghalaya and Tripura}, this time limit is {r:twenty-five years} and that of {r:Arunachal Pradesh, Goa and Mizoram}, it is {r:forty years}.')
    n.boxes([['{r:15 years}', 'general (1965)'], ['{r:25 years}', 'HP, Manipur, Meghalaya, Tripura'], ['{r:40 years}', 'Arunachal, Goa, Mizoram']])
    n.subsub('Rights of Ministers and Advocate General')
    n.para('[[Right to speak, not vote]] In addition to the members of a House, every {r:minister and the advocate general} of the state have the {r:right to speak and take part} in the proceedings of either House or any of its committees of which he/she is named a member, {r:without being entitled to vote}. There are two reasons underlying this constitutional provision:')
    n.items([('1.', '[[Non-member House]] A minister can participate in the proceedings of a {r:House, of which he/she is not a member}.'),
             ('2.', '[[Non-member minister]] A minister, who is {r:not a member of either House}, can participate in the proceedings of both the Houses⁸.')])
    n.footnote('8', 'A person can remain a minister for six months, without being a member of either house of the state legislature.')
    out.append(('09_notes_quorum_voting_language_ministers', n))

    # ---------------- 10 Ordinary bills ----------------
    n = Note('Legislative Procedure – Ordinary Bills')
    n.section('LEGISLATIVE PROCEDURE IN STATE LEGISLATURE')
    n.subsub('Ordinary Bills')
    n.para('[[!Bill in the Originating House]] An ordinary bill can originate in {r:either House} of the state legislature (in case of a bicameral legislature). Such a bill can be introduced either by a {r:minister or by any other member}. The bill passes through {r:three stages} in the originating House, viz,')
    n.items([('1.', 'First reading,'), ('2.', 'Second reading, and'), ('3.', 'Third reading.')])
    n.para('[[Passage by both Houses]] After the bill is passed by the originating House, it is transmitted to the second House for consideration and passage. A bill is deemed to have been passed by the state legislature only when {r:both the Houses have agreed} to it, either with or without amendments. In case of a {r:unicameral legislature}, a bill passed by the legislative assembly is {r:sent directly to the governor} for his/her assent.')
    n.para('[[!Bill in the Second House]] In the second House also, the bill passes through all the three stages, that is, first reading, second reading and third reading.')
    n.para('[[Council’s four options]] When a bill is passed by the legislative assembly and transmitted to the legislative council, the latter has {r:four alternatives} before it:')
    n.items([('1.', 'it may {r:pass the bill} as sent by the assembly (i.e., without amendments);'), ('2.', 'it may {r:pass the bill with amendments} and return it to the assembly for reconsideration;'),
             ('3.', 'it may {r:reject} the bill altogether; and'), ('4.', 'it may {r:not take any action} and thus keep the bill pending.')], kw=False)
    n.para('[[Assembly overrides council – 3 + 1 months]] If the council passes the bill without amendments or the assembly accepts the amendments suggested by the council, the bill is deemed to have been passed by both the Houses and the same is sent to the the governor for his/her assent. On the other hand, if the assembly rejects the amendments suggested by the council or the council rejects the bill altogether or the council does not take any action for {r:three months}, then the {r:assembly may pass the bill again} and transmit the same to the council. If the council rejects the bill again or passes the bill with amendments not acceptable to the assembly or does not pass the bill within {r:one month}, then the bill is {r:deemed to have been passed} by both the Houses in the form in which it was passed by the assembly for the second time.')
    n.flow(['Assembly passes', 'Council: reject / amend / {r:3 months} silence', 'Assembly passes {r:again}', 'Council: {r:1 month}', '{R:deemed passed}'])
    n.para('[[Council only a delaying chamber]] Therefore, the {r:ultimate power} of passing an ordinary bill is vested in the {r:assembly}. At the most, the council can {r:detain or delay the bill for a period of four months}—three months in the first instance and one month in the second instance. The Constitution {r:does not provide for the mechanism of joint sitting} of both the Houses to resolve the disagreement between the two Houses over a bill. On the other hand, there is a provision for joint sitting of the Lok Sabha and the Rajya Sabha to resolve a disagreement between the two over an ordinary bill. Moreover, when a bill, which has originated in the council and was sent to the assembly, is {r:rejected by the assembly, the bill ends and becomes dead}.')
    n.para('[[Council weaker than Rajya Sabha]] Thus, the council has been given {r:much lesser significance, position and authority} than that of the {r:Rajya Sabha} at the Centre.')
    n.subsub('Assent of the Governor')
    n.para('[[Governor’s four options]] Every bill, after it is passed by the assembly or by both the Houses in case of a bicameral legislature, is presented to the {r:governor for his/her assent}. There are {r:four alternatives} before the governor:')
    n.items([('1.', 'he/she may {r:give his/her assent} to the bill;'), ('2.', 'he/she may {r:withhold his/her assent} to the bill;'),
             ('3.', 'he/she may {r:return the bill for reconsideration} of the House or Houses; and'), ('4.', 'he/she may {r:reserve the bill for the consideration of the President}.')], kw=False)
    n.tree(['{r:assent}', '{r:withhold}', '{r:return}', '{r:reserve for President}'])
    n.para('[[Suspensive veto]] If the governor gives his/her assent to the bill, the bill becomes an {r:Act} and is placed on the Statute Book. If the governor withholds his/her assent to the bill, the bill ends and does not become an Act. If the governor returns the bill for reconsideration and if the bill is passed by the House or both the Houses again, with or without amendments, and presented to the governor for his/her assent, the governor {r:must give his/her assent} to the bill. Thus, the governor enjoys only a {r:suspensive veto}. The position is {b:same at the Central level} also.')
    n.subsub('Assent of the President')
    n.para('[[President on reserved bills – six months]] When a bill is {r:reserved by the governor} for the consideration of the President, the President may either {r:give his/her assent} to the bill or {r:withhold his/her assent} to the bill or {r:return the bill for reconsideration} of the House or Houses of the state legislature. When a bill is so returned, the House or Houses have to reconsider it within a period of {r:six months}. The bill is presented again to the presidential assent after it is passed by the House or Houses with or without amendments. It is {r:not mentioned in the Constitution} whether it is obligatory on the part of the president to give his/her assent to such a bill or not.')
    out.append(('10_notes_ordinary_bills_assent', n))

    # ---------------- 11 Money bills, reserved bills ----------------
    n = Note('Money Bills and Bills Reserved for President')
    n.subsub('Money Bills')
    n.para('[[Special procedure]] The Constitution lays down a {r:special procedure} for the passing of Money Bills in the state legislature. This is as follows:')
    n.para('[[Assembly only – Governor’s recommendation]] A Money Bill {r:cannot be introduced in the legislative council}. It can be introduced in the {r:legislative assembly only} and that too on the {r:recommendation of the governor}. Every such bill is considered to be a {r:government bill} and can be introduced {r:only by a minister}.')
    n.para('[[Council – 14 days, recommendations only]] After a Money Bill is passed by the legislative assembly, it is transmitted to the legislative council for its consideration. The legislative council has {r:restricted powers} with regard to a Money Bill. It {r:cannot reject or amend} a Money Bill. It can only {r:make recommendations} and must return the bill to the legislative assembly {r:within 14 days}. The legislative assembly can either {b:accept or reject all or any} of the recommendations of the legislative council.')
    n.para('[[Deemed passed]] If the legislative assembly accepts any recommendation, the bill is then deemed to have been passed by both the Houses in the {r:modified form}. If the legislative assembly does not accept any recommendation, the bill is then deemed to have been passed by both the Houses in the {r:form originally passed} by the legislative assembly without any change.')
    n.para('[[Delay of 14 days only]] If the legislative council {r:does not return the bill} to the legislative assembly {r:within 14 days}, the bill is {r:deemed to have been passed} by both Houses at the expiry of the said period in the form originally passed by the legislative assembly. Thus, the legislative assembly has {r:more powers} than legislative council with regard to a money bill. At the most, the legislative council can detain or delay a money bill for a period of {r:14 days}.')
    n.flow(['Assembly ({r:Governor’s recommendation})', 'Council: recommend within {r:14 days}', 'Assembly accepts / rejects', '{R:deemed passed}'])
    n.para('[[Governor cannot return money bill]] Finally, when a Money Bill is presented to the governor, he/she may either {r:give his/her assent, withhold his/her assent or reserve} the bill for presidential assent but {r:cannot return the bill for reconsideration} of the state legislature. Normally, the governor gives his/her assent to a money bill as it is introduced in the state legislature with his/her {b:prior permission}.')
    n.para('[[President cannot return money bill]] When a money bill is reserved for consideration of the President, the President may either {r:give his/her assent} to the bill or {r:withhold his/her assent} to the bill but {r:cannot return the bill} for reconsideration of the state legislature.')
    n.section('BILLS RESERVED FOR PRESIDENT’S CONSIDERATION')
    n.para('[[Sarkaria – three categories]] The {r:Sarkaria Commission} on Centre-State Relations (1983–88) classified the State Bills reserved for President’s consideration under the Constitution in the following {r:three categories}:')
    n.items([('1.', '[[!Bills which must be reserved for President’s consideration:]] In this category, come Bills— 1. which so {r:derogate from the powers of the High Court}, as to endanger the position which that Court is under the Constitution designed to fill ({r:Article 200}); 2. which relate to imposition of {r:taxes on water or electricity} in certain cases, and attract the provisions of {r:Article 288}; and 3. which fall within {r:Article 360}, during a {r:financial emergency}.'),
             ('2.', '[[!Bills which may be reserved for President’s consideration and assent for specific purposes:]] In this category, the following Bills come— 1. To secure {r:immunity from operation of Articles 14 and 19}. These are Bills for— 1. {b:acquisition of estates, etc. (Article 31A)}; 2. {b:giving effect to certain Directive Principles of State Policy (Article 31C)}. 2. A Bill relating to a subject enumerated in the {r:Concurrent List}, to ensure operation of its provisions despite their {r:repugnancy} to a Union law or an existing law, by securing President’s assent in terms of {r:Article 254}. 3. A bill imposing {r:restrictions on trade and commerce} requiring prior Presidential sanction which was not obtained under {r:Article 304}.'),
             ('3.', '[[Residuary category]] Bills which may not specifically fall under any of the above categories, yet {r:may be reserved by the Governor} for President’s consideration under {r:Article 200}.')])
    n.tree(['{R:Must reserve}', '{R:May reserve – specific purposes}', '{R:May reserve – others}'])
    n.boxes([['Art. 200 (HC powers)', 'Art. 288 (water/electricity)', 'Art. 360 (fin. emergency)'], ['Arts. 31A, 31C', 'Art. 254 (repugnancy)', 'Art. 304 (trade)'], ['Art. 200', '(Governor’s discretion)']], size=13)
    out.append(('11_notes_money_bills_reserved_bills', n))

    # ---------------- 12 Table 33.1 ----------------
    n = Note('Legislative Procedure Compared')
    n.section('LEGISLATIVE PROCEDURE COMPARED')
    n.para('[[Parliament vs State Legislature]] A comparison of the legislature procedure in the {r:Parliament} and {r:State Legislature} is given in {r:Table 33.1}.')
    A = [
        ['1. It can be introduced in {r:either House} of the Parliament.', '1. It can be introduced in {r:either House} of the state legislature.'],
        ['2. It can be introduced either by a minister or by a private member.', '2. It can be introduced either by a minister or by private member.'],
        ['3. It passes through first reading, second reading and third reading in the originating House.', '3. It passes through first reading, second reading and third reading in the originating House.'],
        ['4. It is deemed to have been passed by the Parliament only when both the Houses have agreed to it, either with or without amendments.', '4. It is deemed to have been passed by the state legislature only when both the Houses have agreed to it, either with or without amendments.'],
        ['5. A deadlock between the two Houses takes place when the second House, after receiving a bill passed by the first House, rejects the bill or proposes amendments that are not acceptable to the first House or does not pass the bill within {r:six months}.', '5. A deadlock between the two Houses takes place when the legislative council, after receiving a bill passed by the legislative assembly, rejects the bill or proposes amendments that are not acceptable to the legislative assembly or does not pass the bill within {r:three months}.'],
        ['6. The Constitution {r:provides for the mechanism of joint sitting} of two Houses of the Parliament to resolve a deadlock between them over the passage of a bill.', '6. The Constitution {r:does not provide for the mechanism of joint sitting} of two Houses of the state legislature to resolve a deadlock between them over the passage of a bill.'],
        ['7. The Lok Sabha {r:cannot override} the Rajya Sabha by passing the bill for the second time and vice versa. A joint sitting is the only way to resolve a deadlock between the two Houses.', '7. The legislative assembly {r:can override} the legislative council by passing the bill for the second time and not vice versa. When a bill is passed by the assembly for the second time and transmitted to the legislative council, if the legislative council rejects the bill again, or proposes amendments that are not acceptable to the legislative assembly, or does not pass the bill within {r:one month}, then the bill is deemed to have been passed by both the Houses in the form in which it was passed by the legislative assembly for the second time.'],
        ['8. The mechanism of joint sitting for resolving a deadlock applies to a bill whether originating in the Lok Sabha or the Rajya Sabha. If a joint sitting is not summoned by the president, the bill ends and becomes dead.', '8. The mechanism of passing the bill for the second time to resolve a deadlock applies to a bill originating in the legislative assembly only. When a bill, which has originated in the legislative council and sent to the legislative assembly, is rejected by the latter, the bill ends and becomes dead.'],
        ['B. With Regard to Money Bills', ''],
        ['1. It can be introduced only in the {r:Lok Sabha} and not in the Rajya Sabha.', '1. It can be introduced only in the {r:legislative assembly} and not in the legislative council.'],
        ['2. It can be introduced only on the recommendation of the {r:president}.', '2. It can be introduced only on the recommendation of the {r:governor}.'],
        ['3. It can be introduced only by a minister and not by a private member.', '3. It can be introduced only by a minister and not by a private member.'],
        ['4. It cannot be rejected or amended by the Rajya Sabha. It should be returned to the Lok Sabha within {r:14 days}, either with or without recommendations.', '4. It cannot be rejected or amended by the legislative council. It should be returned to the legislative assembly within {r:14 days}, either with or without amendments.'],
        ['5. The Lok Sabha can either accept or reject all or any of the recommendations of the Rajya Sabha.', '5. The legislative assembly can either accept or reject all or any of the recommendations of the legislative council.'],
        ['6. If the Lok Sabha accepts any recommendation, the bill is then deemed to have been passed by both the Houses in the modified form.', '6. If the legislative assembly accepts any recommendation, the bill is then deemed to have been passed by both the Houses in the modified form.'],
        ['7. If the Lok Sabha does not accept any recommendation, the bill is then deemed to have been passed by both the Houses in the form originally passed by the Lok Sabha without any change.', '7. If the legislative assembly does not accept any recommendation, the bill is then deemed to have been passed by both the Houses in the form originally passed by the legislative assembly without any change.'],
        ['8. If the Rajya Sabha does not return the bill to the Lok Sabha within 14 days, the bill is deemed to have been passed by both the Houses at the expiration of the said period in the form originally passed by the Lok Sabha.', '8. If the legislative council does not return the bill to the legislative assembly within 14 days, the bill is deemed to have been passed by both the Houses at the expiration of the said period in the form originally passed by the legislative assembly.'],
        ['9. The Constitution does not provide for the resolution of any deadlock between the two Houses. This is because, the will of the Lok Sabha is made to prevail over that of the Rajya Sabha, if the latter does not agree to the bill passed by the former.', '9. The Constitution does not provide for the resolution of any deadlock between the two Houses. This is because, the will of the legislative assembly is made to prevail over that of legislative council, if the latter does not agree to the bill passed by the former.'],
    ]
    rows = [['A. With Regard to Ordinary Bills', '']] + A
    n.table(['{R:Parliament}', '{R:State Legislature}'], rows, [300, 300], caption='Table 33.1 Comparing Legislative Procedure in the Parliament and State Legislature', group_rows=(0, 9))
    out.append(('12_notes_table_33_1_procedure_compared', n))

    # ---------------- 13 Position of council ----------------
    n = Note('Position of Legislative Council')
    n.section('POSITION OF LEGISLATIVE COUNCIL')
    n.para('[[Two angles]] The constitutional position of the council (as compared with the assembly) can be studied from two angles:')
    n.items([('A.', 'Spheres where council is equal to assembly.'), ('B.', 'Spheres where council is unequal to assembly.')])
    n.subsub('Equal with Assembly')
    n.para('[[Spheres of equality]] In the following matters, the powers and status of the council are {r:broadly equal} to that of the assembly:')
    n.items([('1.', '[[Ordinary bills]] Introduction and passage of {r:ordinary bills}. However, in case of disagreement between the two Houses, the {b:will of the assembly prevails} over that of the council.'),
             ('2.', '[[Ordinances]] Approval of {r:ordinances} issued by the governor.'),
             ('3.', '[[Selection of ministers]] Selection of {r:ministers including the chief minister}. Under the Constitution the, ministers including the chief minister can be members of either House of the state legislature. However, irrespective of their membership, they are {b:responsible only to the assembly}.'),
             ('4.', '[[Reports of constitutional bodies]] Consideration of the {r:reports of the constitutional bodies} like State Finance Commission, state public service commission and Comptroller and Auditor General of India.'),
             ('5.', '[[SPSC jurisdiction]] Enlargement of the {r:jurisdiction of the state public service commission}.')])
    n.subsub('Unequal with Assembly')
    n.para('[[Spheres of inequality]] In the following matters, the powers and status of the council are {r:unequal} to that of the assembly:')
    n.items([('1.', '[[Money Bill – assembly only]] A {r:Money Bill} can be introduced {r:only in the assembly} and not in the council.'),
             ('2.', '[[No rejection of money bill]] The council {r:cannot amend or reject a money bill}. It should return the bill to the assembly within {r:14 days}, either with recommendations or without recommendations.'),
             ('3.', '[[Assembly decides recommendations]] The assembly can either {r:accept or reject} all or any of the recommendation of the council. In both the cases, the money bill is deemed to have been passed by the two Houses.'),
             ('4.', '[[Speaker certifies money bill]] The final power to decide whether a particular bill is a money bill or not is vested in the {r:Speaker of the assembly}.'),
             ('5.', '[[Dilatory chamber]] The final power of passing an ordinary bill also lies with the {r:assembly}. At the most, the council can {r:detain or delay the bill for the period of four months}—three months in the first instance and one month in the second instance. In other words, the council is {r:not even a revising body} like the Rajya Sabha; it is only a {r:dilatory chamber or an advisory body}.'),
             ('6.', '[[Budget – no vote on grants]] The council can only {r:discuss the budget} but {r:cannot vote on the demands for grants} (which is the exclusive privilege of the assembly).'),
             ('7.', '[[No no-confidence motion]] The council {r:cannot remove the council of ministers} by passing a no-confidence motion. This is because, the council of ministers is {b:collectively responsible only to the assembly}. But, the council can discus and criticise the policies and activities of the Government.'),
             ('8.', '[[Council bills can die]] When an ordinary bill, which has originated in the council and was sent to the assembly, is {r:rejected by the assembly, the bill ends} and becomes dead.'),
             ('9.', '[[No role in Presidential / RS elections]] The council does {r:not participate in the election of the president} of India and {r:representatives of the state in the Rajya Sabha}.'),
             ('10.', '[[Constitutional amendments]] The council has {r:no effective say in the ratification of a constitutional amendment bill}. In this respect also, the will of the assembly prevails over that of the council⁹.'),
             ('11.', '[[Existence depends on assembly]] Finally, the {r:very existence of the council depends on the will of the assembly}. The council can be abolished by the Parliament on the recommendation of the assembly.')])
    n.para('[[Subordinate to assembly]] From the above, it is clear that the position of the council vis-a-vis the assembly is {r:much weaker} than the position of the Rajya Sabha vis-a-vis the Lok Sabha. The Rajya Sabha has {b:equal powers with the Lok Sabha in all spheres except financial matters and with regard to the control over the Government}. On the other hand, the council is {r:subordinate to the assembly in all respects}. Thus, the {r:predominance of the assembly} over the council is fully established.')
    n.compare([('{R:Rajya Sabha vs Lok Sabha}', ['equal except finance', 'and control over Govt']), ('{R:Council vs Assembly}', ['{r:subordinate in all respects}'])])
    n.footnote('9', 'The position, in this regard, is very well analysed by J.C. Johari in the following way: ‘The Constitution is not clear on this point whether a bill of constitutional amendment referred to the states for ratification by their legislatures shall include the Vidhan Parishad or not. In practice, it may be understood that the will of the Vidhan Sabha has to prevail. In case the Vidhan Parishad concurs with the view of the Vidhan Sabha, it is all right; in case it differs, the Vidhan Sabha may pass it again and thereby ignore the will of the Vidhan Parishad as it can do in case of a non-money bill’. (Indian Government and Politics, Vishal, Thirteenth Edition, 2001, p. 441).')
    out.append(('13_notes_position_of_council', n))

    # ---------------- 14 Why council weaker; critics; utility ----------------
    n = Note('Council vs Rajya Sabha – Reasons, Criticism and Utility')
    n.para('[[Why council is weaker than Rajya Sabha]] Even though both the council and the Rajya Sabha are {r:second chambers}, the Constitution has given the council {r:much lesser importance} than the Rajya Sabha due to the following reasons:')
    n.items([('1.', '[[Federal character]] The {r:Rajya Sabha consists of the representatives of the states} and thus reflect the {r:federal element} of the polity. It maintains the {b:federal equilibrium} by protecting the interests of the states against the undue interference of the Centre. Therefore, it has to be an effective revising body and not just an advisory body or dilatory body like that of the council. On the other hand, the {r:issue of federal significance does not arise} in the case of a council.'),
             ('2.', '[[Heterogeneous composition]] The council is {r:heterogeneously constituted}. It represents different interests and consists of differently elected members and also include some nominated members. Its very composition makes its position weak and reduces its utility as an effective revising body. On the other hand, the Rajya Sabha is {r:homogeneously constituted}. It represents the states and union territories and consists of mainly elected members ({b:only 12 out of 250 are nominated}).'),
             ('3.', '[[Democratic principle – British model]] The position accorded to the council is in accordance with the {r:principles of democracy}. The council should {r:yield to the assembly}, which is a popular house. This pattern of relationship between the two Houses of the state legislature is adopted from the {r:British model}. In Britain, the {b:House of Lords} (Upper House) cannot oppose and obstruct the {b:House of Commons} (Lower House). The House of Lords is only a {r:dilatory chamber}—it can delay an ordinary bill for a maximum period of {r:one year} and a money bill for {r:one month}.')])
    n.tree(['{r:no federal role}', '{r:heterogeneous}', '{r:democratic / British model}'])
    n.para('[[Criticism – ‘white elephant’]] Keeping in view its weak, powerless and insignificant position and role, the critics have described the council as a ‘{r:secondary chamber}’, ‘{r:costly ornamental luxury}’, ‘{r:white elephant}’, etc. The critics have opined that the council has served as a {r:refuge for those who are defeated} in the assembly elections. It enabled the unpopular, rejected and ambitious politicians to occupy the post of a chief minister or a minister or a member of the state legislature.')
    n.boxes([['‘{r:secondary chamber}’'], ['‘{r:costly ornamental luxury}’'], ['‘{r:white elephant}’'], ['{r:refuge of defeated}']], size=13)
    n.para('[[Utility of council]] Even though the council has been given less powers as compared with the assembly, its {r:utility} is supported on the following grounds:')
    n.items([('1.', '[[Check on hasty legislation]] It {r:checks the hasty, defective, careless and ill-considered legislation} made by the assembly by making provision for {b:revision and thought}.'),
             ('2.', '[[Representation of experts]] It facilitates {r:representation of eminent professionals and experts} who cannot face direct elections. The governor nominates {r:one-sixth members} of the council to provide representation to such people.')])
    out.append(('14_notes_council_vs_rajya_sabha_criticism_utility', n))

    # ---------------- 15 Privileges ----------------
    n = Note('Privileges of State Legislature')
    n.section('PRIVILEGES OF STATE LEGISLATURE')
    n.para('[[Meaning of privileges]] {r:Privileges} of a state legislature are a sum of {r:special rights, immunities and exemptions} enjoyed by the Houses of state legislature, their committees and their members. They are necessary in order to secure the {b:independence and effectiveness} of their actions. Without these privileges, the Houses can neither maintain their {b:authority, dignity and honour} nor can protect their members from any obstruction in the discharge of their legislative responsibilities.')
    n.para('[[Extended to AG and ministers]] The Constitution has also extended the privileges of the state legislature to those persons who are entitled to speak and take part in the proceedings of a House of the state legislature or any of its committees. These include {r:advocate-general of the state and state ministers}.')
    n.para('[[Not to Governor]] It must be clarified here that the privileges of the state legislature {r:do not extend to the governor} who is also an integral part of the state legislature.')
    n.para('[[Two categories]] The privileges of a state legislature can be classified into two broad categories—those that are enjoyed by each House of the state legislature {r:collectively}, and those that are enjoyed by the members {r:individually}.')
    n.tree(['{R:Collective privileges}', '{R:Individual privileges}'])
    n.subsub('Collective Privileges')
    n.para('[[House privileges]] The privileges belonging to each House of the state legislature collectively are:')
    n.items([('1.', '[[Publication]] It has the right to {r:publish its reports, debates and proceedings} and also the right to prohibit others from publishing the same¹⁰.'),
             ('2.', '[[Secret sittings]] It can {r:exclude strangers} from its proceedings and hold {r:secret sittings} to discuss some important matters.'),
             ('3.', '[[Own procedure]] It can make {r:rules to regulate its own procedure} and the conduct of its business and to adjudicate upon such matters.'),
             ('4.', '[[Punish for contempt]] It can {r:punish members as well as outsiders} for breach of its privileges or its contempt by {b:reprimand, admonition or imprisonment} (also suspension or expulsion, in case of members).'),
             ('5.', '[[Information on arrest]] It has the right to receive {r:immediate information of the arrest}, detention, conviction, imprisonment and release of a member.'),
             ('6.', '[[Inquiries]] It can {r:institute inquiries} and order the attendance of witnesses and send for relevant papers and records.'),
             ('7.', '[[No court inquiry]] The {r:courts are prohibited to inquire} into the proceedings of a House or its Committees.'),
             ('8.', '[[No arrest in precincts]] No person (either a member or outsider) can be arrested, and no legal process (civil or criminal) can be served {r:within the precincts of the House} without the permission of the presiding officer.')])
    n.subsub('Individual Privileges')
    n.para('[[Members’ privileges]] The privileges belonging to the members individually are:')
    n.items([('1.', '[[Freedom from arrest – civil cases]] They {r:cannot be arrested during the session} of the state legislature and {r:40 days before} the beginning and {r:40 days after} the end of such session. This privilege is available {r:only in civil cases} and not in criminal cases or preventive detention cases.'),
             ('2.', '[[Freedom of speech]] They have {r:freedom of speech} in the state legislature. No member is liable to any proceedings in any court for anything said or any vote given by him/her in the state legislature or its committees. This freedom is subject to the provisions of the Constitution and to the rules and standing orders regulating the procedure of the state legislature¹¹.'),
             ('3.', '[[Jury & witness exemption]] They are {r:exempted from jury service}. They can refuse to give evidence and appear as a witness in a case pending in a court when the state legislature is in session.')])
    n.footnote('10', 'The 44th Amendment Act of 1978 restored the freedom of the press to publish true reports of state legislature without its prior permission. But, this is not applicable in the case of a secret sitting of the House.')
    n.footnote('11', 'Article 211 of the Constitution says that no discussion shall take place in the legislature of a state with respect to the conduct of any judge of the Supreme Court or of a high court in the discharge of his/her duties. Under the rules of a House(s) of the state legislature, use of unparliamentary language or unparliamentary conduct of a member is prohibited.')
    n.footnote('12', 'The Andhra Pradesh Reorganisation (Amendment) Act, 2015, increased the number of seats in the Legislative Council of Andhra Pradesh from 50 to 58.')
    n.footnote('13', 'Under the Jammu and Kashmir Reorganisation Act, 2019, the total number of seats fixed for the Legislative Assembly of the Union territory of Jammu and Kashmir is 107. But, 24 seats fall in the Pakistan-occupied-Kashmir (PoK). These seats are vacant and are not to be taken into account for reckoning the total membership of the Assembly.')
    out.append(('15_notes_privileges', n))
    return out
