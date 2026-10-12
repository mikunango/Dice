from nb import Note

def notes():
    out = []

    # ---------------- 21 Trends, tension areas ----------------
    n = Note('Trends in Centre–State Relations')
    n.section('TRENDS IN CENTRE–STATE RELATIONS')
    n.para('Till {r:1967}, the centre–state relations by and large were {r:smooth} due to {b:one-party rule at the Centre and in most of the states}. In {r:1967 elections}, the {r:Congress party was defeated in nine states} and its position at the Centre became weak. This changed political scenario heralded a {r:new era} in the Centre–state relations. The {b:non-Congress Governments} in the states opposed the increasing {r:centralisation and intervention} of the Central government. They raised the issue of {r:state autonomy} and demanded {b:more powers and financial resources} to the states. This caused {r:tensions and conflicts} in Centre–state relations.')
    n.flow(['till 1967: {r:smooth}', '{b:one-party rule}', '1967: Congress lost {r:9 states}', 'non-Congress states', 'demand {r:state autonomy}', '{R:tensions}'])
    n.sub('Tension Areas in Centre-State Relations')
    n.para('The issues which created {r:tensions and conflicts} between the Centre and states are:')
    n.items([('(1)', 'Mode of {r:appointment and dismissal of governor};'), ('(2)', '{r:Discriminatory and partisan role of governors};'),
             ('(3)', 'Imposition of {r:President’s Rule for partisan interests};'), ('(4)', 'Deployment of {r:Central forces} in the states to maintain law and order;'),
             ('(5)', '{r:Reservation of state bills} for the consideration of the President;'), ('(6)', '{r:Discrimination in financial allocations} to the states;'),
             ('(7)', 'Role of {r:Planning Commission} in approving state projects; ({b:till its replacement by the NITI Aayog in 2015});'),
             ('(8)', 'Management of {r:All-India Services} ({b:IAS, IPS, and IFoS});'), ('(9)', 'Use of {r:electronic media} for political purposes;'),
             ('(10)', 'Appointment of {r:enquiry commissions} against the chief ministers;'), ('(11)', '{r:Sharing of finances} (between Centre and states);'),
             ('(12)', '{r:Encroachment by the Centre on the State List};'), ('(13)', 'Implementation of the {r:Centrally sponsored schemes} by the states; and'),
             ('(14)', 'Modus operandi of the {r:central agencies} like {b:CBI, ED} and so on.')])
    n.boxes([['{R:Governor}', '(1) (2)'], ['{R:Emergency / forces}', '(3) (4)'], ['{R:Legislative}', '(5) (12)'], ['{R:Financial}', '(6) (7) (11) (13)'], ['{R:Administrative}', '(8) (9) (10) (14)']], size=13)
    n.para('The issues in Centre-State relations have been under consideration since the {r:mid 1960s}. In this direction, the following developments have taken place:')
    n.flow(['{r:ARC} 1966', '{r:Rajamannar} 1969', '{r:Anandpur Sahib} 1973', '{r:West Bengal} 1977', '{r:Sarkaria} 1983', '{r:Punchhi} 2007'])
    out.append(('21_notes_trends_tension_areas', n))

    # ---------------- 22 ARC, Rajamannar ----------------
    n = Note('Administrative Reforms Commission and Rajamannar Committee')
    n.sub('Administrative Reforms Commission')
    n.para('The Central government appointed a {r:six-member First Administrative Reforms Commission (ARC)} of India in {r:1966} under the chairmanship of {r:Morarji Desai} ({b:followed by K Hanumanthayya}). Its terms of references included, among others, the examination of Centre–State relations. In order to examine thoroughly the various issues in Centre–state relations, the ARC constituted a {r:study team under M.C. Setalvad}. On the basis of the report of this study team, the ARC finalised its own report and submitted it to the Central government in {r:1969}. It made {r:22 recommendations} for improving the Centre–state relations. The important recommendations are:')
    n.flow(['ARC {r:1966}', 'Morarji Desai → {b:K Hanumanthayya}', 'study team: {r:M.C. Setalvad}', 'report {r:1969}', '{r:22} recommendations'])
    n.bullets(['Establishment of an {r:Inter-State Council under Article 263} of the Constitution.',
               'Appointment of persons having {r:long experience in public life and administration} and {b:nonpartisan attitude} as {r:governors}.',
               '{r:Delegation of powers} to the maximum extent to the states.',
               'Transferring of {r:more financial resources} to the states to reduce their dependency upon the Centre.',
               'Deployment of {r:Central armed forces} in the states either on their request or otherwise.'], orig=True)
    n.para('{r:No action was taken} by the Central government on the recommendations of the ARC.')
    n.sub('Rajamannar Committee')
    n.para('In {r:1969}, the {r:Tamil Nadu Government (DMK)} appointed a {r:three-member committee} under the chairmanship of {r:Dr. P.V. Rajamannar} to examine the entire question of Centre–state relations and to suggest amendments to the Constitution so as to secure {r:utmost autonomy to the states}.¹⁹ The committee submitted its report to the Tamil Nadu Government in {r:1971}.')
    n.bullets(['The Committee identified the reasons for the prevailing {r:unitary trends (tendencies of centralisation)} in the country.'])
    n.listpara('They include:', [('(i)', 'certain provisions in the Constitution which confer {b:special powers on the Centre};'), ('(ii)', '{b:one-party rule} both at the Centre and in the states;'),
               ('(iii)', '{b:inadequacy of states’ fiscal resources} and consequent dependence on the Centre for financial assistance; and'), ('(iv)', 'the institution of {b:Central planning} and the role of the Planning Commission.')])
    n.tree(['{b:special powers to Centre}', '{b:one-party rule}', '{b:weak state finances}', '{b:Central planning}'])
    n.listpara('The important recommendations of the committee are as follows:',
               [('(i)', 'An {r:Inter-State Council} should be set up immediately;'), ('(ii)', '{r:Finance Commission} should be made a {r:permanent body};'),
                ('(iii)', '{r:Planning Commission should be disbanded} and its place should be taken by a statutory body;'),
                ('(iv)', '{r:Articles 356, 357 and 365} (dealing with President’s Rule) should be {r:totally omitted};'),
                ('(v)', 'The provision that the state ministry holds office during the {b:pleasure of the governor} should be omitted;'),
                ('(vi)', 'Certain subjects of the Union List and the Concurrent List should be {b:transferred to the State List};'),
                ('(vii)', 'the {r:residuary powers should be allocated to the states}; and'), ('(viii)', '{r:All-India services (IAS, IPS and IFoS) should be abolished}.')])
    n.para('The Central government {r:completely ignored} the recommendations of the Rajamannar Committee.')
    n.footnote('19', 'The other two members of the committee were Dr. Lakshmanswamy Mudaliar and P.C. Chandra Reddy.')
    out.append(('22_notes_arc_rajamannar_committee', n))

    # ---------------- 23 Anandpur Sahib, West Bengal ----------------
    n = Note('Anandpur Sahib Resolution and West Bengal Memorandum')
    n.sub('Anandpur Sahib Resolution')
    n.para('In {r:1973}, the {r:Akali Dal} adopted a resolution containing both {b:political and religious demands} in a meeting held at {r:Anandpur Sahib in Punjab}. The resolution, generally known as {r:Anandpur Sahib Resolution}, demanded that the {r:Centre’s jurisdiction should be restricted only to defence, foreign affairs, communications, and currency} and the {r:entire residuary powers should be vested in the states}. It stated that the Constitution should be made {b:federal in the real sense} and should ensure {b:equal authority and representation to all the states} at the Centre.')
    n.tree(['{r:defence}', '{r:foreign affairs}', '{r:communications}', '{r:currency}'])
    n.arrow('only these 4 with the Centre · residuary → {r:states}', x=340)
    n.sub('West Bengal Memorandum')
    n.para('In {r:1977}, the {r:West Bengal Government (led by the Communists)} published a memorandum on Centre–state relations and sent it to the Central government.')
    n.listpara('The memorandum inter alia suggested the following:',
               [('(i)', 'The word ‘{r:union}’ in the Constitution should be replaced by the word ‘{r:federal}’;'),
                ('(ii)', 'The jurisdiction of the Centre should be confined to {b:defence, foreign affairs, currency, communications and economic co-ordination};'),
                ('(iii)', 'All other subjects including the {r:residuary} should be vested in the states;'),
                ('(iv)', '{r:Articles 356 and 357 (President’s Rule) and 360 (financial emergency) should be repealed};'),
                ('(v)', '{r:State’s consent} should be made obligatory for formation of new states or reorganisation of existing states;'),
                ('(vi)', 'Of the total revenue raised by the Centre from all sources, {r:75 per cent} should be allocated to the states;'),
                ('(vii)', '{r:Rajya Sabha should have equal powers} with that of the Lok Sabha; and'),
                ('(viii)', 'There should be only Central and state services and the {r:All-India Services should be abolished}.')])
    n.flow(['‘union’ → {r:‘federal’}', '{r:75%} revenue to states', 'repeal {r:356, 357, 360}', 'abolish {r:AIS}'])
    n.para('The Central government {r:did not accept} the demands made in the memorandum.')
    n.table(['{R:Body}', '{R:Year}', '{R:By}', '{R:Fate}'],
            [['ARC', '1966–69', 'Central govt', '{r:no action}'], ['Rajamannar Committee', '1969–71', 'Tamil Nadu (DMK)', '{r:completely ignored}'],
             ['Anandpur Sahib Resolution', '1973', 'Akali Dal', '—'], ['West Bengal Memorandum', '1977', 'West Bengal govt', '{r:not accepted}']],
            [210, 100, 160, 130], src=False)
    out.append(('23_notes_anandpur_sahib_west_bengal_memorandum', n))

    # ---------------- 24 Sarkaria ----------------
    n = Note('Sarkaria Commission')
    n.sub('Sarkaria Commission')
    n.para('In {r:1983}, the Central government appointed a {r:three-member Commission} on Centre–state relations under the chairmanship of {r:R.S. Sarkaria}, a {b:retired judge of the Supreme Court}.²⁰ The commission was asked to examine and review the working of existing arrangements between the Centre and states in all spheres and recommend appropriate changes and measures. It submitted it’s report in {r:1988}.')
    n.para('The Commission {r:did not favour structural changes} and regarded the existing constitutional arrangements and principles relating to the institutions {b:basically sound}. But, it emphasised on the need for changes in the {r:functional or operational aspects}. It observed that federalism is more a {r:functional arrangement for co-operative action} than a static institutional concept. It outrightly {r:rejected the demand for curtailing the powers of the Centre} and stated that a {r:strong Centre} is essential to safeguard the {b:national unity and integrity} which is being threatened by the {b:fissiparous tendencies} in the body politic. However, it did {r:not equate strong Centre with centralisation of powers}. It observed that {r:over-centralisation leads to blood pressure at the centre and anaemia at the periphery}.')
    n.compare([('{R:✘ Not favoured}', ['structural changes', 'curtailing Centre’s powers']), ('{R:✔ Favoured}', ['functional / operational changes', '{r:strong Centre} ≠ centralisation'])])
    n.flow(['over-centralisation', '{r:blood pressure} at centre', '{b:anaemia} at periphery'])
    n.para('The Commission made {r:247 recommendations} to improve Centre–state relations. The important recommendations are mentioned below:')
    recs = ['A permanent Inter-State Council called the {r:Inter-Governmental Council} should be set up under {r:Article 263}.',
            '{r:Article 356 (President’s Rule)} should be used {r:very sparingly}, in extreme cases as a {b:last resort} when all the available alternatives fail.',
            'The institution of {r:All-India Services} should be {b:further strengthened} and more of such services should be created.',
            'The {r:residuary powers of taxation} should continue to remain with the {r:Parliament}, while the other residuary powers should be placed in the {r:Concurrent List}.',
            'When the President {r:withholds his/her assent} to the state bills, the {b:reasons should be communicated} to the state government.',
            'The {r:National Development Council (NDC)} should be renamed and reconstituted as the {r:National Economic and Development Council (NEDC)}.',
            'The {r:zonal councils} should be constituted afresh and reactivated to promote the spirit of federalism.',
            'The Centre should have powers to {r:deploy its armed forces}, even without the consent of states. However, it is desirable that the {b:states should be consulted}.',
            'The Centre should {r:consult the states} before making a law on a subject of the {r:Concurrent List}.',
            'The procedure of {r:consulting the chief minister in the appointment of the state governor} should be prescribed in the Constitution itself.',
            'The net proceeds of the {r:corporation tax} may be made permissibly {b:shareable with the states}.',
            'The governor {r:cannot dismiss the council of ministers} so long as it commands a majority in the assembly.',
            'The {r:governor’s term of five years} in a state should not be disturbed except for some extremely compelling reasons.',
            'No {r:commission of enquiry} should be set up against a state minister unless a demand is made by the {b:Parliament}.',
            'The {r:surcharge on income tax} should not be levied by the Centre except for a specific purpose and for a strictly limited period.',
            'The present division of functions between the {r:Finance Commission} and the {r:Planning Commission} is reasonable and should continue.',
            'Steps should be taken to uniformly implement the {r:three language formula} in its true spirit.',
            '{r:No autonomy for radio and television} but {b:decentralisation in their operations}.',
            '{r:No change in the role of Rajya Sabha} and Centre’s power to reorganise the states.',
            'The {r:commissioner for linguistic minorities} should be activated.']
    n.items([(f'{i+1}.', r) for i, r in enumerate(recs)])
    n.para('The Central government has implemented {r:180 (out of 247)} recommendations of the Sarkaria Commission. The most important is the establishment of the {r:Inter-State Council in 1990}.')
    n.flow(['{r:1983} appointed', 'report {r:1988}', '{r:247} recommendations', '{r:180} implemented', '{R:Inter-State Council 1990}'])
    n.footnote('20', 'B. Sivaraman and S.R. Sen were two other members of the Commission.')
    out.append(('24_notes_sarkaria_commission', n))

    # ---------------- 25 Punchhi I ----------------
    n = Note('Punchhi Commission – I')
    n.sub('Punchhi Commission')
    n.para('The {r:Second commission on Centre-State Relations} was set-up by the Government of India in {r:2007} under the Chairmanship of {r:Madan Mohan Punchhi}, {b:former Chief Justice of India}.²¹ It was required to look into the issues of Centre-State relations keeping in view the {b:sea-changes} that have taken place in the polity and economy of India since the Sarkaria Commission had last looked at the issue of Centre-State relations over two decades ago.')
    n.para('The Commission submitted its report to the government in {r:2010}. In finalising the {r:1,456 page report, in seven volumes}, the Commission took extensive help from the {b:Sarkaria Commission report}, the {b:National Commission to Review the Working of the Constitution (NCRWC) report} and the {b:Second Administrative Reforms Commission report}. However, in a number of areas, the Commission report {r:differed from the Sarkaria Commission} recommendations.')
    n.flow(['set up {r:2007}', 'report {r:2010}', '{r:1,456 pages · 7 volumes}', '{r:310+} recommendations'])
    n.tree(['{b:Sarkaria report}', '{b:NCRWC report}', '{b:2nd ARC report}'])
    n.para('After examining at length the issues raised in its Terms of Reference and the related aspects in all their hues and shades, the Commission came to the conclusion that ‘{R:cooperative federalism}’ will be the key for sustaining India’s {b:unity, integrity and social and economic development} in future. The principles of cooperative federalism thus may have to act as a {b:practical guide} for Indian polity and governance.')
    n.para('In all, the Commission made {r:over 310 recommendations}, touching upon several significant areas in the working of Centre-state relations. The important recommendations are mentioned below:')
    recs = [
        'To facilitate effective implementation of the laws on {r:List III subjects}, it is necessary that some {r:broad agreement} is reached between the Union and states before introducing legislation in Parliament on matters in the {r:Concurrent List}.',
        'The Union should be {r:extremely restrained in asserting Parliamentary supremacy} in matters assigned to the states. {b:Greater flexibility to states} in relation to subjects in the State List and “{b:transferred items}” in the Concurrent List is the key for better Centre-state relations.',
        'The Union should occupy only that many of subjects in concurrent or overlapping jurisdiction which are {r:absolutely necessary} to achieve uniformity of policy in {b:demonstrable national interest}.',
        'There should be a {r:continuing auditing role for the Inter-state Council} in the management of matters in concurrent or overlapping jurisdiction.',
        'The period of {r:six months} prescribed in {r:Article 201} for State Legislature to act when the bill is returned by the President can be made applicable for the {r:President also} to decide on assenting or withholding assent to a state bill reserved for consideration of the President.',
        'Parliament should make a law on the subject of {r:Entry 14 of List I} ({b:treaty making and implementing it through Parliamentary legislation}) to streamline the procedures involved. The exercise of the power obviously cannot be absolute or unchartered in view of the federal structure of legislative and executive powers.',
        'Financial obligations and its implications on state finances arising out of {r:treaties and agreements} should be a {r:permanent term of reference to the Finance Commissions} constituted from time to time.',
    ]
    n.items([(f'{i+1}.', r) for i, r in enumerate(recs)])
    n.footnote('21', 'The other four Members of the Commission were Dhirendra Singh (Former Secretary to the Government of India), Vinod Kumar Duggal (Former Secretary to the Government of India), Prof. N.R. Madhava Menon (Former Director, National Judicial Academy, Bhopal and National Law School of India, Bangalore) and Dr. Amaresh Bagchi (Emeritus Professor, National Institute of Public Finance and Policy, New Delhi). With the passing away of Dr. Bagchi in February 2008, Vijay Shanker (Former Director, Central Bureau of Investigation, Government of India) was appointed in his place as a Member of the Commission in October 2008.')
    out.append(('25_notes_punchhi_commission_1', n))

    # ---------------- 26 Punchhi II: governors ----------------
    n = Note('Punchhi Commission – II (Governors)')
    n.items([('8.', 'While {r:selecting Governors}, the Central Government should adopt the following {r:strict guidelines} as recommended in the {b:Sarkaria Commission report} and follow its mandate in letter and spirit:')])
    n.items([('(i)', 'He/she should be {r:eminent in some walk of life}'),
             ('(ii)', 'He/she should be a {r:person from outside the state}'),
             ('(iii)', 'He/she should be a {r:detached figure} and not too intimately connected with the local politics of the state'),
             ('(iv)', 'He/she should be a person who has {r:not taken too great a part in politics} generally and particularly in the recent past')], indent=30)
    n.boxes([['{r:eminent}'], ['{r:outsider}'], ['{r:detached}'], ['{r:not too political}']])
    recs = [
        ('9.', '{r:Governors should be given a fixed tenure of five years} and their removal should {b:not be at the sweet will} of the Government at the Centre.'),
        ('10.', 'The procedure laid down for {r:impeachment of President}, {b:mutatis mutandis} can be made applicable for {r:impeachment of Governors} as well.'),
        ('11.', '{r:Article 163} does {r:not give the Governor a general discretionary power} to act against or without the advice of his/her Council of Ministers. In fact, the area for the exercise of discretion is {b:limited} and even in this limited area, his/her choice of action should not be arbitrary or fanciful. It must be a choice {b:dictated by reason, activated by good faith and tempered by caution}.'),
        ('12.', 'In respect of bills passed by the Legislative Assembly of a state, the Governor should take the decision {r:within six months} whether to grant assent or to reserve it for consideration of the President.'),
        ('13.', 'On the question of Governor’s role in {r:appointment of Chief Minister} in the case of an {r:hung assembly}, it is necessary to lay down certain clear guidelines to be followed as {b:Constitutional conventions}. These guidelines may be as follows:'),
    ]
    n.items(recs)
    n.items([('(i)', 'The party or combination of parties which commands the {r:widest support} in the Legislative Assembly should be called upon to form the Government.'),
             ('(ii)', 'If there is a {r:pre-poll alliance or coalition}, it should be treated as {r:one political party} and if such coalition obtains a majority, the leader of such coalition shall be called by the Governor to form the Government.'),
             ('(iii)', 'In case no party or pre-poll coalition has a clear majority, the Governor should select the Chief Minister in the {r:order of preference} indicated here.')], indent=30)
    n.items([('(a)', 'The group of parties which had {r:pre-poll alliance} commanding the largest number'),
             ('(b)', 'The {r:largest single party} staking a claim to form the government with the support of others'),
             ('(c)', 'A {r:post-electoral coalition} with all partners joining the government'),
             ('(d)', 'A {r:post-electoral alliance} with some parties joining the government and the remaining including independents supporting the government from outside')], indent=60)
    n.flow(['(a) pre-poll alliance', '(b) largest single party', '(c) post-poll coalition (all join)', '(d) post-poll alliance (some outside)'])
    n.items([('14.', 'On the question of {r:dismissal of a Chief Minister}, the Governor should invariably insist on the Chief Minister {r:proving his/her majority on the floor of the House} for which he/she should prescribe a {b:time limit}.'),
             ('15.', 'The Governor should have the right to {r:sanction for prosecution of a state minister} against the advice of the Council of Ministers, if the Cabinet decision appears to the Governor to be {b:motivated by bias} in the face of overwhelming material.'),
             ('16.', 'The convention of {r:Governors acting as Chancellors of Universities} and holding other statutory positions should be {r:done away with}. His/her role should be confined to the {b:Constitutional provisions only}.')])
    out.append(('26_notes_punchhi_commission_2_governors', n))

    # ---------------- 27 Punchhi III: emergency, councils ----------------
    n = Note('Punchhi Commission – III (Emergency and Coordination)')
    n.items([
        ('17.', 'When an {r:external aggression or internal disturbance} paralyses the state administration creating a situation of a potential break down of the Constitutional machinery of the state, {r:all alternative courses} available to the Union for discharging its paramount responsibility under {r:Article 355} should be exhausted to contain the situation and the exercise of the power under {r:Article 356} should be limited strictly to rectifying a “{b:failure of the Constitutional machinery in the state}”.'),
        ('18.', 'On the question of invoking {r:Article 356} in case of failure of Constitutional machinery in states, suitable amendments are required to incorporate the guidelines set forth in the landmark judgement of the Supreme Court in {r:S.R. Bommai case²² (1994)}. This would remove possible misgivings in this regard on the part of states and help in smoothening Centre-state relations.'),
        ('19.', 'Given the strict parameters now set for invoking the emergency provisions under {r:Articles 352 and 356} to be used only as a measure of “{r:last resort}”, and the duty of the Union to protect states under {r:Article 355}, it is necessary to provide a Constitutional or legal framework to deal with situations which require Central intervention but do not warrant invoking the extreme steps under Articles 352 and 356. Providing the framework for “{R:localised emergency}” would ensure that the state government can continue to function and the Assembly would not have to be dissolved while providing a mechanism to let the Central Government respond to the issue {b:specifically and locally}. The imposition of local emergency is fully justified under the mandate of {r:Article 355} read with {r:Entry 2A of List I} and {r:Entry 1 of List II} of the Seventh Schedule.'),
    ])
    n.flow(['crisis in a state', 'Art. 355 {b:alternatives first}', '{R:localised emergency}', 'Art. 356 only {r:last resort}'])
    n.items([
        ('20.', 'Suitable amendments to {r:Article 263} are required to make the {r:Inter-State Council} a {b:credible, powerful and fair mechanism} for management of inter-state and Centre-state differences.'),
        ('21.', 'The {r:Zonal Councils} should meet {r:at least twice a year} with an agenda proposed by states concerned to maximise co-ordination and promote harmonisation of policies and action having inter-state ramification. The Secretariat of a strengthened Inter-State Council can function as the {b:Secretariat of the Zonal Councils} as well.'),
        ('22.', 'The {r:Empowered Committee of Finance Ministers of States} proved to be a successful experiment in inter-state co-ordination on fiscal matters. There is need to institutionalise similar models in other sectors as well. A {r:forum of Chief Ministers}, Chaired by one of the Chief Minister {b:by rotation} can be similarly thought about particularly to co-ordinate policies of sectors like {b:energy, food, education, environment and health}.'),
        ('23.', '{r:New all-India services} in sectors like {b:health, education, engineering and judiciary} should be created.'),
        ('24.', 'Factors inhibiting the composition and functioning of the {r:Second Chamber} as a representative forum of states should be removed or modified even if it requires amendment of the Constitutional provisions. In fact, {r:Rajya Sabha} offers immense potential to negotiate acceptable solutions to the friction points which emerge between Centre and states in fiscal, legislative and administrative relations.'),
        ('25.', 'A balance of power between states inter se is desirable and this is possible by {r:equality of representation in the Rajya Sabha}. This requires amendment of the relevant provisions to give {r:equality of seats to states} in the Rajya Sabha, {b:irrespective of their population size}.'),
        ('26.', 'The scope of {r:devolution of powers to local bodies} to act as institutions of self-government should be {b:constitutionally defined} through appropriate amendments.'),
        ('27.', 'All future Central legislations involving states’ involvement should provide for {r:cost sharing} as in the case of the {r:RTE Act}. Existing Central legislations where the states are entrusted with the responsibility of implementation should be suitably amended providing for {b:sharing of costs by the Central Government}.'),
        ('28.', 'The {r:royalty rates on major minerals} should be revised {r:at least every three years} without any delay. States should be properly compensated for any delay in the revision of royalty beyond three years.'),
    ])
    n.boxes([['{r:Inter-State Council}', 'Art. 263 amend'], ['{r:Zonal Councils}', '2×/year'], ['{r:CM forum}', 'by rotation'], ['{r:RS equality}', 'equal seats']])
    n.footnote('22', 'S.R. Bommai vs. Union of India (1994).')
    out.append(('27_notes_punchhi_commission_3_emergency_coordination', n))

    # ---------------- 28 Punchhi IV: finance ----------------
    n = Note('Punchhi Commission – IV (Finance and Planning)')
    n.items([
        ('29.', 'The current {r:ceiling on profession tax} should be {r:completely done away with} by a Constitutional amendment.'),
        ('30.', 'The scope for raising more revenue from the {r:taxes mentioned in article 268} should be examined afresh. This issue may be either referred to the {b:next Finance Commission} or an {b:expert committee} be appointed to look into the matter.'),
        ('31.', 'To bring greater accountability, all {r:fiscal legislations} should provide for an {r:annual assessment by an independent body} and the reports of these bodies should be laid in both Houses of Parliament/state legislature.'),
        ('32.', 'Considerations specified in the {r:Terms of Reference (ToR) of the Finance Commission} should be {r:even handed} as between the Centre and the states. There should be an effective mechanism to involve the states in the finalisation of the ToR of the Finance Commissions.'),
        ('33.', 'The Central Government should {r:review all the existing cesses and surcharges} with a view to bringing down their share in the gross tax revenue.'),
        ('34.', 'Because of the close linkages between the {r:plan and non-plan expenditure}, an {b:expert committee} may be appointed to look into the issue of distinction between the plan and non-plan expenditure.'),
        ('35.', 'There should be much better {r:coordination between the Finance Commission and the Planning Commission}. The {b:synchronisation of the periods} covered by the Finance Commission and the Five-Year Plan will considerably improve such coordination.'),
        ('36.', 'The {r:Finance Commission division} in the Ministry of Finance should be converted into a {r:full-fledged department}, serving as the {b:permanent secretariat for the Finance Commissions}.'),
        ('37.', 'The {r:Planning Commission} has a crucial role in the current situation. But its role should be that of {r:coordination} rather that of {b:micro managing sectoral plans} of the Central ministries and the states.'),
        ('38.', 'Steps should be taken for the setting up of an {r:Inter-State Trade and Commerce Commission} under {r:Article 307} read with {r:Entry 42 of List-I}. This Commission should be vested with both {b:advisory and executive roles} with decision making powers. As a Constitutional body, the decisions of the Commission should be {r:final and binding} on all states as well as the Union of India. Any party aggrieved with the decision of the Commission may prefer an {r:appeal to the Supreme Court}.'),
    ])
    n.flow(['{R:Inter-State Trade & Commerce Commission}', 'Art. 307 + Entry 42 List-I', 'decisions {r:final & binding}', 'appeal → {r:Supreme Court}'])
    n.para('The recommendations contained in the Report of the Punchhi Commission have been considered by the {r:Standing Committee of the Inter-State Council} in its meetings held in {r:2017 and 2018}. The recommendations of the Commission along with the recommendations of the Standing Committee thereon, have been {b:circulated to the state governments for comments²³}.')
    n.flow(['Punchhi report', 'ISC Standing Committee ({r:2017, 2018})', '{b:circulated to states}'])
    n.footnote('23', 'Annual Report 2021-22, Ministry of Home Affairs, Government of India, p. 246.')
    out.append(('28_notes_punchhi_commission_4_finance_planning', n))
    return out
