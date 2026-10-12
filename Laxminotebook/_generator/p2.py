from nb import Note

def notes():
    out = []

    # ---------------- 08 Admin: distribution, obligation, directions ----------------
    n = Note('Administrative Relations – I')
    n.section('ADMINISTRATIVE RELATIONS')
    n.para('{r:Articles 256 to 263} in {r:Part XI} of the Constitution deal with the {b:administrative relations} between the Centre and the states. In addition, there are various other articles pertaining to the same matter.')
    n.sub('1. Distribution of Executive Powers')
    n.bullets(['The {r:executive power} has been divided between the Centre and the states on the lines of the {b:distribution of legislative powers}, except in few cases.'])
    n.listpara('Thus, the executive power of the {r:Centre} extends to the {r:whole of India}:',
               [('(i)', 'to the matters on which the Parliament has exclusive power of legislation ({b:i.e., the subjects enumerated in the Union List}); and'),
                ('(ii)', 'to the exercise of rights, authority and jurisdiction conferred on it by any {r:treaty or agreement}.')], cont=True)
    n.cont('Similarly, the executive power of a {r:state} extends to its territory in respect of matters on which the state legislature has exclusive power of legislation ({b:i.e., the subjects enumerated in the State List}).')
    n.para('In respect of matters on which both the Parliament and the state legislatures have power of legislation ({b:i.e., the subjects enumerated in the Concurrent List}), the executive power {r:rests with the states} except when a {b:Constitutional provision or a parliamentary law} specifically confers it on the Centre. Therefore, a law on a concurrent subject, though enacted by the Parliament, is to be {r:executed by the states} except when the Constitution or the Parliament has directed otherwise.⁵')
    n.compare([('{R:Union List}', ['executive power → {r:Centre}', '{b:+ treaties / agreements}']),
               ('{R:State List}', ['executive power → {r:State}']),
               ('{R:Concurrent List}', ['executive power → {r:States}', '{b:unless Constitution / Parliament says Centre}'])])
    n.sub('2. Obligation of States and the Centre')
    n.para('The Constitution has placed {r:two restrictions} on the executive power of the states in order to give ample scope to the Centre for exercising its executive power in an {b:unrestricted manner}. Thus, the executive power of every state is to be exercised in such a way (a) as to {r:ensure compliance with the laws made by the Parliament} and any existing law which apply in the state; and (b) as {r:not to impede or prejudice} the exercise of executive power of the Centre in the state. While the former lays down a {b:general obligation} upon the state, the latter imposes a {b:specific obligation} on the state not to hamper the executive power of the Centre.')
    n.boxes([['{R:(a) general obligation}', 'comply with laws of Parliament + existing laws'], ['{R:(b) specific obligation}', 'not impede / prejudice Centre’s executive power']])
    n.para('In both the cases, the executive power of the Centre extends to giving of such {r:directions} to the state as are necessary for the purpose. The sanction behind these directions of the Centre is {r:coercive} in nature. Thus, {r:Article 365} says that where any state has {b:failed to comply with (or to give effect to) any directions} given by the Centre, it will be lawful for the President to hold that a situation has arisen in which the government of the state cannot be carried on in accordance with the provisions of the Constitution. It means that, in such a situation, the {r:President’s rule} can be imposed in the state under {r:Article 356}.')
    n.flow(['Centre gives {r:directions}', 'State fails to comply', '{r:Art. 365}', '{R:President’s rule (Art. 356)}'])
    n.sub('3. Centre’s Directions to the States')
    n.para('In addition to the above two cases, the Centre is empowered to give {r:directions} to the states with regard to the exercise of their executive power in the following matters:')
    n.items([('(i)', 'the construction and maintenance of {r:means of communication} ({b:declared to be of national or military importance}) by the state;'),
             ('(ii)', 'the measures to be taken for the {r:protection of the railways} within the state;'),
             ('(iii)', 'the provision of adequate facilities for {r:instruction in the mother-tongue} at the {b:primary stage of education} to children belonging to {r:linguistic minority groups} in the state; and'),
             ('(iv)', 'the drawing up and execution of the specified schemes for the {r:welfare of the Scheduled Tribes} in the state.')])
    n.para('The {r:coercive sanction} behind the Central directions under {r:Article 365} (mentioned above) is also applicable in these cases.')
    n.footnote('5', 'For example, under the Essential Commodities Act, made by the Parliament on a concurrent subject, the executive power is vested in the Centre.')
    out.append(('08_notes_admin_executive_powers_obligations_directions', n))

    # ---------------- 09 Mutual delegation, cooperation ----------------
    n = Note('Administrative Relations – II')
    n.sub('4. Mutual Delegation of Functions')
    n.para('The distribution of legislative powers between the Centre and the states is {r:rigid}. Consequently, the Centre {r:cannot delegate its legislative powers} to the states and a single state cannot request the Parliament to make a law on a state subject. The distribution of executive power in general follows the distribution of legislative powers. But, such a rigid division in the executive sphere may lead to {b:occasional conflicts} between the two. Hence, the Constitution provides for {r:inter-government delegation of executive functions} in order to {b:mitigate rigidity and avoid a situation of deadlock}.')
    n.para('Accordingly, the {r:President} may, with the {r:consent of the state government}, entrust to that government any of the executive functions of the Centre. Conversely, the {r:governor of a state} may, with the {r:consent of the Central government}, entrust to that government any of the executive functions of the state.⁶ This mutual delegation of administrative functions may be {b:conditional or unconditional}.')
    n.raw(f'<line class="ln" x1="200" y1="{n.y+40}" x2="476" y2="{n.y+40}" marker-end="url(#ah)"/><line class="ln" x1="476" y1="{n.y+58}" x2="200" y2="{n.y+58}" marker-end="url(#ah)"/>')
    n.raw(f'<rect class="bx" x="60" y="{n.y+24}" width="135" height="50" rx="3"/><text class="r" x="127" y="{n.y+54}" text-anchor="middle" style="font-weight:700">Centre</text>')
    n.raw(f'<rect class="bx" x="485" y="{n.y+24}" width="135" height="50" rx="3"/><text class="r" x="552" y="{n.y+54}" text-anchor="middle" style="font-weight:700">State</text>')
    n.raw(f'<text class="sm b" x="338" y="{n.y+34}" text-anchor="middle">President entrusts (with state’s consent)</text><text class="sm b" x="338" y="{n.y+76}" text-anchor="middle">Governor entrusts (with Centre’s consent)</text>', 84)
    n.para('The Constitution also makes a provision for the entrustment of the executive functions of the Centre to a state {r:without the consent of that state}. But, in this case, the delegation is by the {r:Parliament} and {b:not by the president}. Thus, a law made by the Parliament on a subject of the {r:Union List} can confer powers and impose duties on a state, or authorise the conferring of powers and imposition of duties by the Centre upon a state ({b:irrespective of the consent of the state concerned}). Notably, the same thing {r:cannot be done by the state legislature}.')
    n.para('From the above, it is clear that the mutual delegation of functions between the Centre and the state can take place either {r:under an agreement} or {r:by a legislation}. While the {b:Centre can use both} the methods, a {b:state can use only the first} method.')
    n.compare([('{R:By agreement}', ['Centre ✔', 'State ✔']), ('{R:By legislation}', ['Centre (Parliament) ✔', 'State ✘'])])
    n.sub('5. Cooperation Between the Centre and States')
    n.para('The Constitution contains the following provisions to secure {r:cooperation and coordination} between the Centre and the states:')
    n.items([('(i)', 'The Parliament can provide for the {r:adjudication of any dispute} or complaint with respect to the use, distribution and control of {b:waters of any inter-state river and river valley}.'),
             ('(ii)', 'The President can establish (under {r:Article 263}) an {r:Inter-State Council} to investigate and discuss subject of common interest between the Centre and the states. Such a council was set up in {r:1990}.'),
             ('(iii)', '{r:Full faith and credit} is to be given throughout the territory of India to {b:public acts, records and judicial proceedings} of the Centre and every state.'),
             ('(iv)', 'The Parliament can appoint an {r:appropriate authority} to carry out the purposes of the constitutional provisions relating to the {b:interstate freedom of trade, commerce and intercourse}. But, {r:no such authority has been appointed so far}.')])
    n.boxes([['{r:river water disputes}'], ['{r:Inter-State Council}', '{b:Art. 263 · 1990}'], ['{r:full faith & credit}'], ['{r:trade authority}', '{b:not appointed}']])
    n.footnote('6', 'This provision (the power of the states to entrust functions to the Centre) was added by the 7th Constitutional Amendment Act of 1956. Before that, only the Centre had the power.')
    out.append(('09_notes_admin_mutual_delegation_cooperation', n))

    # ---------------- 10 All-India Services ----------------
    n = Note('All-India Services')
    n.sub('6. All-India Services')
    n.para('Like in any other federation, the Centre and the states also have their separate public services called as the {r:Central Services} and the {r:State Services} respectively. In addition, there are {r:All-India Services—IAS, IPS and IFoS}. The members of these services occupy {b:top positions (or key posts)} under both the Centre and the states and serve them {b:by turns}. But, they are {r:recruited and trained by the Centre}.')
    n.tree(['{r:Central Services}', '{R:All-India Services}', '{r:State Services}'])
    n.tree(['{b:IAS}', '{b:IPS}', '{b:IFoS}'], root_x=340)
    n.para('These services are {r:controlled jointly} by the Centre and the states. The {r:ultimate control} lies with the {r:Central government} while the {r:immediate control} vests with the {r:state governments}.')
    n.compare([('{R:Ultimate control}', ['Central government']), ('{R:Immediate control}', ['State governments'])])
    n.para('In {r:1947}, {b:Indian Civil Service (ICS)} was replaced by {r:IAS} and the {b:Indian Police (IP)} was replaced by {r:IPS} and were recognised by the Constitution as All-India Services. In {r:1966}, the {r:Indian Forest Service (IFoS)} was created as the {b:third All-India Service}. {r:Article 312} of the Constitution authorises the Parliament to create {r:new All-India Services} on the basis of a {r:Rajya Sabha resolution} to that effect.')
    n.flow(['ICS → {r:IAS} (1947)', 'IP → {r:IPS} (1947)', '{r:IFoS} (1966)', 'new: Art. 312 + {r:RS resolution}'])
    n.para('Each of these three All-India Services, irrespective of their division among different states, form a {r:single service} with {b:common rights and status} and {b:uniform scales of pay} throughout the country.')
    n.listpara('Though the All-India Services {r:violate the principle of federalism} under the Constitution by restricting the {b:autonomy and patronage of the states}, they are supported on the ground that',
               [('(i)', 'they help in maintaining {r:high standard of administration} in the Centre as well as in the states;'),
                ('(ii)', 'they help to ensure {r:uniformity of the administrative system} throughout the country; and'),
                ('(iii)', 'they facilitate {r:liaison, cooperation, coordination and joint action} on the issues of common interest between the Centre and the states.')])
    n.tree(['{r:(i) high standard}', '{r:(ii) uniformity}', '{r:(iii) liaison & coordination}'])
    n.para('While justifying the institution of all-India services in the Constituent Assembly, {r:Dr. B.R. Ambedkar} observed that:')
    n.quote('“The {r:dual polity} which is inherent in a federal system is followed in all federations by a {r:dual service}. In all federations, there is a Federal Civil Service and a State Civil Service. The Indian federation, though a dual polity, will have a dual service, but with {r:one exception}. It is recognised that in every country there are certain posts in its administrative set up which might be called {r:strategic} from the point of view of maintaining the standard of administration. There can be no doubt that the standard of administration depends upon the {b:calibre of the civil servants} who are appointed to the strategic posts. The Constitution provides that without depriving the states of their rights to form their own civil services, there shall be an {r:all-India service}, recruited on an all-India basis with {b:common qualifications}, with {b:uniform scale of pay} and members of which alone could be appointed to those strategic posts throughout the Union”.⁷')
    n.footnote('7', 'Constituent Assembly Debates, Volume VII, pp. 41-42.')
    out.append(('10_notes_admin_all_india_services', n))

    # ---------------- 11 PSC, judiciary, emergencies ----------------
    n = Note('Administrative Relations – III')
    n.sub('7. Public Service Commissions')
    n.para('In the field of {r:public service commissions}, the Centre–state relations are as follows:')
    n.items([('(i)', 'The {r:Chairman and members of a state public service commission}, though {b:appointed by the governor} of the state, can be {r:removed only by the President}.'),
             ('(ii)', 'The Parliament can establish a {r:Joint State Public Service Commission (JSPSC)} for two or more states on the {b:request of the state legislatures} concerned. The chairman and members of the JSPSC are {r:appointed by the President}.'),
             ('(iii)', 'The {r:Union Public Service Commission (UPSC)} can serve the needs of a state on the {b:request of the state governor} and with the {b:approval of the President}.'),
             ('(iv)', 'The UPSC assists the states ({b:when requested by two or more states}) in framing and operating schemes of {r:joint recruitment} for any services for which candidates possessing special qualifications are required.')])
    n.compare([('{R:SPSC}', ['appointed: {r:Governor}', 'removed: {r:President}']), ('{R:JSPSC}', ['created: Parliament', 'appointed: {r:President}']), ('{R:UPSC}', ['serves a state', '{b:Governor’s request + President’s approval}'])])
    n.sub('8. Integrated Judicial System')
    n.para('Though India has a {r:dual polity}, there is {r:no dual system of administration of justice}. The Constitution, on the other hand, established an {r:integrated judicial system} with the {b:Supreme Court at the top} and the {b:state high courts below it}. This {r:single system of courts} enforces both the Central laws as well as the state laws. This is done to {b:eliminate diversities in the remedial procedure}.')
    n.flow(['{R:Supreme Court}', '{R:High Courts}', '{b:Central + state laws}'])
    n.para('The judges of a state high court are {r:appointed by the President} in consultation with the {b:Chief Justice of India} and the {b:governor of the state}. They can also be {r:transferred and removed by the President}.')
    n.para('The Parliament can establish a {r:common high court for two or more states}. For example, {b:Maharashtra and goa} or {b:Punjab and Haryana} have a common high court.')
    n.sub('9. Relations During Emergencies')
    n.items([('(i)', 'During the operation of a {r:national emergency} (under {r:Article 352}), the Centre becomes entitled to give executive directions to a state on ‘{r:any}’ matter. Thus, the state governments are brought under the {r:complete control of the Centre}, though they are {b:not suspended}.'),
             ('(ii)', 'When the {r:President’s Rule} is imposed in a state (under {r:Article 356}), the President can assume to himself/herself the {b:functions of the state government} and powers vested in the Governor or any other executive authority in the state.'),
             ('(iii)', 'During the operation of a {r:financial emergency} (under {r:Article 360}), the Centre can direct the states to observe {b:canons of financial propriety} and can give other necessary directions including the {r:reduction of salaries} of persons serving in the state.')])
    n.boxes([['{R:Art. 352}', 'directions on {r:any} matter', '{b:state govt not suspended}'], ['{R:Art. 356}', 'President assumes', '{b:state functions}'], ['{R:Art. 360}', 'financial propriety', '{b:cut salaries}']])
    out.append(('11_notes_admin_psc_judiciary_emergencies', n))

    # ---------------- 12 Other provisions, extra-constitutional ----------------
    n = Note('Administrative Relations – IV')
    n.sub('10. Other Provisions')
    n.para('The Constitution contains the following other provisions which enable the Centre to exercise {r:control over the state administration}:')
    n.items([('(i)', '{r:Article 355} imposes {r:two duties} on the Centre: (a) to {b:protect every state against external aggression and internal disturbance}; and (b) to {b:ensure that the government of every state is carried on in accordance with the provisions of the Constitution}.'),
             ('(ii)', 'The {r:governor} of a state is {r:appointed by the President}. He/she holds office during the {r:pleasure of the President}. In addition to the Constitutional head of the state, the governor acts as an {r:agent of the Centre} in the state. He/she submits {b:periodical reports} to the Centre about the administrative affairs of the state.'),
             ('(iii)', 'The {r:state election commissioner}, though {b:appointed by the governor} of the state, can be {r:removed only by the President}.')])
    n.tree(['{R:Art. 355} – 2 duties', '{R:Governor} – agent of Centre', '{R:SEC} – removed by President'])
    n.sub('11. Extra-Constitutional Devices')
    n.para('In addition to the above-mentioned constitutional devices, there are {r:extra-constitutional devices} to promote cooperation and coordination between the Centre and the states. These include a number of {r:advisory bodies} and {r:conferences} held at the Central level.')
    n.tree(['{R:Advisory bodies}', '{R:Conferences}'])
    n.para('The {r:non-constitutional advisory bodies} include the {b:NITI Ayog (which succeeded the planning commission)}, the {b:National Integration Council}, the {b:Central Council of Health and Family Welfare}, the {b:Central Council of Local Government}, the {b:Zonal Councils}, the {b:North-Eastern Council}, the {b:Central Council of Indian Medicine}, the {b:Central Council of Homoeopathy}, the {b:Transport Development Council}, the {b:University Grants Commission} and so on.')
    n.para('The important {r:conferences} held either annually or otherwise to facilitate Centre–state consultation on a wide range of matters are as follows:')
    n.items([('(i)', 'The {r:governors’ conference} (presided over by the {b:President}).'),
             ('(ii)', 'The {r:chief ministers’ conference} (presided over by the {b:prime minister}).'),
             ('(iii)', 'The {r:chief secretaries’ conference} (presided over by the {b:cabinet secretary}).'),
             ('(iv)', 'The {r:conference of inspector-general of police}.'),
             ('(v)', 'The {r:chief justices’ conference} (presided over by the {b:chief justice of India}).'),
             ('(vi)', 'The {r:conference of vice-chancellors}.'),
             ('(vii)', 'The {r:home ministers’ conference} (presided over by the {b:Central home minister}).'),
             ('(viii)', 'The {r:law ministers’ conference} (presided over by the {b:Central law minister}).')])
    n.table(['{R:Conference}', '{R:Presided over by}'],
            [['Governors', '{r:President}'], ['Chief ministers', '{r:Prime minister}'], ['Chief secretaries', '{r:Cabinet secretary}'],
             ['Chief justices', '{r:Chief justice of India}'], ['Home ministers', '{r:Central home minister}'], ['Law ministers', '{r:Central law minister}']],
            [300, 300], src=False)
    out.append(('12_notes_admin_other_provisions_extra_constitutional', n))
    return out
