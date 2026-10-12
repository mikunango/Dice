from nb import Note

def notes():
    out = []

    # ---------------- 01 Intro ----------------
    n = Note('CHAPTER 15 Centre–State Relations', 'Intro of Centre-State relations, three heads and four aspects of legislative relations.')
    n.reg('CHAPTER 15 Centre–State Relations')
    n.para('The {r:Constitution of India}, being {b:federal in structure}, divides all powers ({r:legislative, executive and financial}) between the {r:Centre} and the {r:states}. However, there is {r:no division of judicial power} as the Constitution has established an {b:integrated judicial system} to enforce both the {r:Central laws} as well as {r:state laws}.')
    n.tree(['{r:Legislative}', '{r:Executive}', '{r:Financial}', '{b:Judicial} – not divided'], size=14)
    n.arrow('{b:integrated judicial system} enforces both {r:Central laws} + {r:state laws}', x=565)
    n.para('Though the Centre and the states are {r:supreme in their respective fields}, the {b:maximum harmony and coordination} between them is essential for the {b:effective operation of the federal system}. Hence, the Constitution contains {r:elaborate provisions} to regulate the various dimensions of the relations between the Centre and the states.')
    n.bullets(['The {r:Centre-state relations} can be studied under {r:three heads}:'])
    n.tree(['• {r:Legislative relations.}', '• {r:Administrative relations.}', '• {r:Financial relations.}'], size=14, src=True)
    n.rule()
    n.section('LEGISLATIVE RELATIONS')
    n.para('{r:Articles 245 to 255} in {r:Part XI} of the Constitution deal with the {b:legislative relations} between the Centre and the states. Besides these, there are some {b:other articles} dealing with the same subject.')
    n.para('Like any other {b:Federal Constitution}, the Indian Constitution also divides the legislative powers between the Centre and the states with respect to both the {r:territory} and the {r:subjects of legislation}. Further, the Constitution provides for the {r:parliamentary legislation in the state field} under {r:five extraordinary situations} as well as the {r:centre’s control over state legislation} in certain cases. Thus, there are {r:four aspects} in the Centre–states legislative relations, viz.,')
    four = ['Territorial extent of Central and state legislation;', 'Distribution of legislative subjects;', 'Parliamentary legislation in the state field; and', 'Centre’s control over state legislation.']
    n.boxes([['{r:%d.}' % (i+1), '{K:' + t + '}'] for i, t in enumerate(four)])
    for t in four: n.reg(t)
    out.append(('01_notes_ch15_intro_legislative_relations', n))

    # ---------------- 02 Territorial extent ----------------
    n = Note('Territorial Extent of Central and State Legislation')
    n.sub('1. Territorial Extent of Central and State Legislation')
    n.para('The Constitution defines the {r:territorial limits} of the legislative powers vested in the Centre and the states in the following way:')
    n.items([('(i)', 'The {r:Parliament} can make laws for the {r:whole or any part of the territory of India}. The territory of India includes the {b:states}, the {b:union territories}, and {b:any other area} for the time being included in the territory of India.'),
             ('(ii)', 'A {r:state legislature} can make laws for the {r:whole or any part of the state}. The laws made by a state legislature are {b:not applicable outside the state}, except when there is a {r:sufficient nexus} between the state and the object.'),
             ('(iii)', 'The {r:Parliament alone} can make ‘{r:extra-territorial legislation}’. Thus, the laws of the Parliament are also applicable to the {b:Indian citizens and their property in any part of the world}.')])
    n.compare([('{R:Parliament}', ['whole or any part of {r:India}', '{b:states + UTs + other areas}', '{r:extra-territorial} also ✔']),
               ('{R:State legislature}', ['whole or any part of the {r:state}', 'not outside the state', 'except {r:sufficient nexus}'])])
    n.para('However, the Constitution places {r:certain restrictions} on the {b:plenary territorial jurisdiction} of the Parliament. In other words, the laws of Parliament are {r:not applicable} in the following areas:')
    n.items([('(i)', 'The {r:President} can make {r:regulations} for the {b:peace, progress and good government} of the Union Territories of the {r:Andaman and Nicobar Islands, Lakshadweep, Dadra and Nagar Haveli and Daman and Diu and Ladakh}. In the case of {r:Puducherry} also, the President can legislate by making regulations but only when the {b:Assembly is suspended or dissolved}. A regulation so made has the {r:same force and effect as an act of Parliament}. It may also {b:repeal or amend any act of Parliament} in relation to these union territories.'),
             ('(ii)', 'The {r:governor} is empowered to direct that an act of Parliament {b:does not apply} to a {r:scheduled area} in the state or apply with {b:specified modifications and exceptions}.'),
             ('(iii)', 'The {r:Governor of Assam} may likewise direct that an act of Parliament does not apply to a {r:tribal area (autonomous district)} in the state or apply with specified modifications and exceptions. The {r:President} enjoys the same power with respect to tribal areas (autonomous districts) in {r:Meghalaya, Tripura and Mizoram}.')])
    n.tree(['{R:President}', '{R:Governor}', '{R:Governor of Assam / President}'], size=14)
    n.raw('', 0)
    n.boxes([['{r:regulations for UTs}', '{b:A&N, Lakshadweep, DNH & DD, Ladakh}', '{b:Puducherry – only if Assembly suspended/dissolved}'],
             ['{r:scheduled area}', '{b:act not to apply / apply with modifications}'],
             ['{r:tribal areas}', '{b:Assam (Governor)}', '{b:Meghalaya, Tripura, Mizoram (President)}']])
    out.append(('02_notes_territorial_extent', n))

    # ---------------- 03 Distribution of subjects ----------------
    n = Note('Distribution of Legislative Subjects')
    n.sub('2. Distribution of Legislative Subjects')
    n.para('The Constitution provides for a {r:three-fold distribution} of legislative subjects between the Centre and the states, viz., {r:List-I (the Union List)}, {r:List-II (the State List)} and {r:List-III (the Concurrent List)} in the {r:Seventh Schedule}:')
    n.boxes([['{R:List-I Union List}', '{r:98 subjects}', '{b:originally 97}', 'Parliament – exclusive'],
             ['{R:List-II State List}', '{r:59 subjects}', '{b:originally 66}', 'State – exclusive (normal times)'],
             ['{R:List-III Concurrent List}', '{r:52 subjects}', '{b:originally 47}', 'Both']])
    n.items([('(i)', 'The {r:Parliament} has {r:exclusive powers} to make laws with respect to any of the matters enumerated in the {r:Union List}. This list has at present {r:98 subjects} ({b:originally 97¹ subjects}) like {b:defence, banking, foreign affairs, currency, atomic energy, insurance, communication, inter-state trade and commerce, census, audit} and so on.'),
             ('(ii)', 'The {r:state legislature} has “{r:in normal circumstances}” exclusive powers to make laws with respect to any of the matters enumerated in the {r:State List}. This has at present {r:59 subjects} ({b:originally 66² subjects}) like {b:public order, police, public health and sanitation, agriculture, prisons, local government, fisheries, markets, theaters, gambling} and so on.'),
             ('(iii)', '{r:Both}, the Parliament and state legislature can make laws with respect to any of the matters enumerated in the {r:Concurrent List}. This list has at present {r:52 subjects} ({b:originally 47³ subjects}) like {b:criminal law and procedure, civil procedure, marriage and divorce, population control and family planning, electricity, labour welfare, economic and social planning, drugs, newspapers, books and printing press}, and others. The {r:42nd Amendment Act of 1976} transferred {r:five subjects} to Concurrent List from State List, that is, (a) {b:education}, (b) {b:forests}, (c) {b:weights and measures}, (d) {b:protection of wild animals and birds}, and (e) {b:administration of justice; constitution and organisation of all courts except the Supreme Court and the high courts}.')])
    n.flow(['{R:State List}', '{r:42nd Amendment, 1976}', '{R:Concurrent List}'])
    n.tree(['{b:education}', '{b:forests}', '{b:weights & measures}', '{b:wild animals & birds}', '{b:administration of justice}'], size=13)
    n.items([('(iv)', 'The Parliament has power to make laws with respect to any matter for any part of the territory of India {r:not included in a state} even though that matter is one which is enumerated in the {r:State List}. This provision has reference to the {b:Union Territories} or the {b:Acquired Territories (if any)}.'),
             ('(v)', 'The {r:101st Amendment Act of 2016} has made a special provision with respect to {r:goods and services tax}. Accordingly, the {b:Parliament and the state legislature} have power to make laws with respect to goods and services tax imposed by the Union or by the State. Further, the {r:parliament has exclusive power} to make laws with respect to goods and services tax where the supply of goods or services or both takes place in the course of {r:inter-state trade or commerce}.'),
             ('(vi)', 'The power to make laws with respect to {r:residuary subjects} (i.e., the matters which are not enumerated in any of the three lists) is vested in the {r:Parliament}. This residuary power of legislation includes the power to levy {r:residuary taxes}.')])
    n.flow(['{r:Residuary subjects}', '{R:Parliament}', '{b:incl. residuary taxes}'])
    n.footnote('1', 'Even now, the last entry is numbered as 97 but the total number of entries is 98. The entries numbered as 2A, 92A and 92B have been added and entries 33, 92 and 92C have been omitted.')
    n.footnote('2', 'Even now, the last entry is numbered as 66 but the total number of entries is 59. The entries numbered as 11, 19, 20, 29, 36, 52 and 55 have been omitted.')
    n.footnote('3', 'Even now, the last entry is numbered as 47 but the total number of entries is 52. The entries numbered as 11A, 17A, 17B, 20A and 33A have been added.')
    out.append(('03_notes_distribution_of_subjects', n))

    # ---------------- 04 Scheme, comparison, predominance ----------------
    n = Note('Scheme of Lists and Predominance')
    n.para('From the above scheme, it is clear that the matters of {r:national importance} and the matters which require {b:uniformity of legislation nationwide} are included in the {r:Union List}. The matters of {r:regional and local importance} and the matters which permit {b:diversity of interest} are specified in the {r:State List}. The matters on which uniformity of legislation throughout the country is {b:desirable but not essential} are enumerated in the {r:concurrent list}. Thus, it permits {r:diversity along with uniformity}.')
    n.compare([('{R:Union List}', ['national importance', '{b:uniformity nationwide}']),
               ('{R:State List}', ['regional & local importance', '{b:diversity of interest}']),
               ('{R:Concurrent List}', ['uniformity desirable', '{b:but not essential}'])])
    n.para('In {r:US}, only the powers of the {b:Federal Government} are enumerated in the Constitution and the {r:residuary powers are left to the states}. The {r:Australian Constitution} followed the American pattern of {b:single enumeration} of powers. In {r:Canada}, on the other hand, there is a {b:double enumeration}—Federal and Provincial, and the {r:residuary powers are vested in the Centre}.')
    n.para('The {r:Government of India Act of 1935} provided for a {r:three-fold enumeration}, viz., {b:federal, provincial and concurrent}. The present Constitution follows the scheme of this act but with {r:one difference}, that is, under this act, the residuary powers were given neither to the federal legislature nor to the provincial legislature but to the {r:Governor-General of India}. In this respect, India follows the {r:Canadian precedent}.')
    n.table(['{R:Country / Act}', '{R:Enumeration}', '{R:Residuary powers}'],
            [['USA', 'single (federal only)', '{r:states}'], ['Australia', 'single (American pattern)', '{r:states}'],
             ['Canada', 'double (federal + provincial)', '{r:Centre}'], ['GoI Act 1935', 'three-fold', '{r:Governor-General}'],
             ['India', 'three-fold (7th Schedule)', '{r:Parliament (Centre)}']], [170, 240, 190], src=False)
    n.para('The Constitution expressly secures the {r:predominance of the Union List} over the State List and the Concurrent List and that of the {r:Concurrent List over the State List}. Thus, in case of overlapping between the Union List and the State List, the {b:former should prevail}. In case of overlapping between the Union List and the Concurrent List, it is again the {b:former which should prevail}. Where there is a conflict between the Concurrent List and the State List, it is the {b:former that should prevail}.')
    n.flow(['{R:Union List}', '{R:Concurrent List}', '{R:State List}'], sep='>')
    n.para('In case of a conflict between the {r:Central law} and the {r:state law} on a subject enumerated in the {r:Concurrent List}, the {r:central law prevails} over the state law. But, there is an {r:exception}. If the state law has been {b:reserved for the consideration of the President} and has {b:received his/her assent}, then the {r:state law prevails in that state}. But, it would still be competent for the {r:Parliament to override} such a law by subsequently making a law on the same matter.')
    n.flow(['Conflict on Concurrent subject', '{r:Central law prevails}'])
    n.flow(['{b:Exception}: State law reserved + President’s assent', '{r:State law prevails in that state}', 'Parliament can still {r:override} later'])
    out.append(('04_notes_scheme_predominance', n))

    # ---------------- 05 Parliamentary legislation A, B ----------------
    n = Note('Parliamentary Legislation in the State Field – I')
    n.sub('3. Parliamentary Legislation in the State Field')
    n.para('The above scheme of distribution of legislative powers between the Centre and the states is to be maintained in {r:normal times}. But, in {r:abnormal times}, the scheme of distribution is either {b:modified or suspended}. In other words, the Constitution empowers the Parliament to make laws on any matter enumerated in the {r:State List} under the following {r:five extraordinary circumstances}:')
    n.tree(['{r:A. Rajya Sabha resolution}', '{r:B. National Emergency}', '{r:C. States’ request}', '{r:D. International agreements}', '{r:E. President’s Rule}'], size=13)
    n.subsub('A. When Rajya Sabha Passes a Resolution')
    n.para('If the {r:Rajya Sabha} declares that it is necessary in the {r:national interest} that Parliament should make laws with respect to {b:goods and services tax³ᵃ} or a matter in the {r:State List}, then the Parliament becomes competent to make laws on that matter. Such a resolution must be supported by {r:two-thirds of the members present and voting}. The resolution remains in force for {r:one year}; it can be {b:renewed any number of times} but not exceeding one year at a time. The laws cease to have effect on the {r:expiration of six months} after the resolution has ceased to be in force.')
    n.flow(['RS resolution ({r:2/3 present & voting})', 'in force {r:1 year}', '{b:renew any times}', 'laws end {r:6 months} after'])
    n.para('This provision does {r:not restrict} the power of a state legislature to make laws on the same matter. But, in case of {b:inconsistency} between a state law and a parliamentary law, the {r:latter is to prevail}.')
    n.subsub('B. During a National Emergency')
    n.para('The Parliament acquires the power to legislate with respect to {b:goods and services tax³ᵇ} or matters in the {r:State List}, while a proclamation of {r:national emergency} is in operation. The laws become inoperative on the {r:expiration of six months} after the emergency has ceased to operate.')
    n.flow(['{r:National emergency} in operation', 'Parliament legislates on State List', 'laws end {r:6 months} after emergency'])
    n.para('Here also, the power of a state legislature to make laws on the same matter is {r:not restricted}. But, in case of {b:repugnancy} between a state law and a parliamentary law, the {r:latter is to prevail}.')
    n.footnote('3a', 'The provision for goods and services tax was added by the 101st Amendment Act of 2016.')
    n.footnote('3b', 'Ibid.')
    out.append(('05_notes_parl_legislation_state_field_A_B', n))

    # ---------------- 06 C, D, E ----------------
    n = Note('Parliamentary Legislation in the State Field – II')
    n.subsub('C. When States Make a Request')
    n.para('When the legislatures of {r:two or more states} pass {r:resolutions} requesting the Parliament to enact laws on a matter in the {r:State List}, then the Parliament can make laws for regulating that matter. A law so enacted applies {r:only to those states} which have passed the resolutions. However, {b:any other state may adopt it afterwards} by passing a resolution to that effect in its legislature. Such a law can be {r:amended or repealed only by the Parliament} and not by the legislatures of the concerned states.')
    n.flow(['{r:2+ states} pass resolutions', 'Parliament makes law', 'applies {r:only to those states}', '{b:others may adopt later}'])
    n.para('The effect of passing a resolution under the above provision is that the Parliament becomes {r:entitled to legislate} with respect to a matter for which it has no power to make a law. On the other hand, the state legislature {r:ceases to have the power} to make a law with respect to that matter. The resolution operates as {r:abdication or surrender} of the power of the state legislature with respect to that matter and it is placed {b:entirely in the hands of Parliament} which alone can then legislate with respect to it.')
    n.compare([('{R:Parliament}', ['{r:gains} power on that matter', 'alone can amend / repeal']),
               ('{R:State legislature}', ['{r:loses} power on that matter', '{b:abdication / surrender}'])])
    n.para('Some examples of laws passed under the above provision are {b:Prize Competition Act, 1955}; {b:Wild Life (Protection) Act, 1972}; {b:Water (Prevention and Control of Pollution) Act, 1974}; {b:Urban Land (Ceiling and Regulation) Act, 1976}; and {b:Transplantation of Human Organs Act, 1994}.')
    n.subsub('D. To Implement International Agreements')
    n.para('The Parliament can make laws on any matter in the {r:State List} for implementing the {r:international treaties, agreements or conventions}. This provision enables the Central government to fulfil its {b:international obligations and commitments}.')
    n.para('Some examples of laws enacted under the above provision are {b:United Nations (Privileges and Immunities) Act, 1947}; {b:Geneva Convention Act, 1960}; {b:Anti-Hijacking Act, 1982} and legislations relating to {b:environment and TRIPS}.')
    n.subsub('E. During President’s Rule')
    n.para('When the {r:President’s rule} is imposed in a state, the Parliament becomes empowered to make laws with respect to any matter in the {r:State List} in relation to that state. A law made so by the Parliament {r:continues to be operative even after the president’s rule}. This means that the period for which such a law remains in force is {b:not coterminous} with the duration of the President’s rule. But, such a law can be {r:repealed or altered or re-enacted by the state legislature}.')
    n.flow(['President’s rule', 'Parliament law on State List', '{r:operative even after}', '{b:state may repeal/alter/re-enact}'])
    out.append(('06_notes_parl_legislation_state_field_C_D_E', n))

    # ---------------- 07 Centre's control ----------------
    n = Note('Centre’s Control Over State Legislation')
    n.sub('4. Centre’s Control Over State Legislation')
    n.para('Besides the Parliament’s power to legislate directly on the state subjects under the {b:exceptional situations}, the Constitution empowers the Centre to exercise {r:control over the state’s legislative matters} in the following ways:')
    n.items([('(i)', 'The {r:Governor} can {r:reserve a bill} passed by the state legislature for the consideration of the President. It must be noted here that the President enjoys {r:absolute veto} over such a bill ({r:Articles 200 and 201}).'),
             ('(ii)', 'A state bill imposing restrictions on the {b:freedom of trade, commerce and intercourse} with that state or within that state can be introduced in the legislature of the state only with the {r:previous sanction of the President} ({r:Article 304}).'),
             ('(iii)', 'The Centre can direct the states to {r:reserve money bills and other financial bills} passed by the state legislature for the President’s consideration during a {r:financial emergency} ({r:Article 360}).'),
             ('(iv)', 'The Governor {r:cannot make an ordinance} without the {b:instructions from the President} in certain cases ({r:Article 213}).')])
    n.boxes([['{r:Art. 200 & 201}', 'reserved bill', '{b:absolute veto}'], ['{r:Art. 304}', 'trade restriction bill', '{b:previous sanction}'],
             ['{r:Art. 360}', 'money/financial bills', '{b:financial emergency}'], ['{r:Art. 213}', 'ordinance', '{b:President’s instructions}']])
    n.para('From the above, it is clear that the Constitution has assigned a {r:position of superiority to the Centre} in the legislative sphere. In this context, the {r:Sarkaria Commission on Centre– State Relations (1983–88)} observed:')
    n.quote('“The rule of {r:federal supremacy} is a technique to {b:avoid absurdity, resolve conflict and ensure harmony} between the Union and state laws. If this principle of union supremacy is excluded, it is not difficult to imagine its {b:deleterious results}. There will be every possibility of our {b:two-tier political system} being stultified by {r:interference, strife, legal chaos and confusion} caused by a host of conflicting laws, much to the bewilderment of the common citizen. Integrated legislative policy and uniformity on basic issues of common Union–state concern will be stymied. The federal principle of {r:unity in diversity} will be very much a casualty. This rule of federal supremacy, therefore, is {r:indispensable} for the successful functioning of the federal system”.⁴')
    n.flow(['federal supremacy', 'avoids absurdity / conflict', '{r:harmony}', '{b:unity in diversity}'])
    n.footnote('4', 'Report of the Commission on centre-state Relations, Part I (Government of India, 1988) pp. 28–29.')
    out.append(('07_notes_centre_control_over_state_legislation', n))
    return out
