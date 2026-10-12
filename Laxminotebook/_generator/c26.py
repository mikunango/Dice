from nb import Note

OUT = '/home/user/Dice/Laxminotebook/Ch26_Supreme_Court'
SKIP = [('Table 26.2 Acts Relating to the Composition', None)]   # 26.2 (+note) and 26.3 skipped

def notes():
    out = []

    # ---------------- 01 Intro ----------------
    n = Note('CHAPTER 26 Supreme Court', 'Integrated judiciary, inauguration and constitutional provisions.')
    n.reg('CHAPTER 26 Supreme Court')
    n.para('[[Integrated judicial system]] Unlike the {r:American Constitution}, the Indian Constitution has established an {r:integrated judicial system} with the {b:Supreme Court at the top} and the {b:high courts below it}. Under a high court (and below the state level), there is a hierarchy of {r:subordinate courts}, that is, {b:district courts and other lower courts}. This {r:single system of courts}, adopted from the {r:Government of India Act of 1935}, enforces both {b:Central laws as well as the state laws}. In {r:USA}, on the other hand, the federal laws are enforced by the federal judiciary and the state laws are enforced by the state judiciary. There is thus a {r:double system of courts} in USA—one for the centre and the other for the states. To sum up, India, although a federal country like the USA, has a {r:unified judiciary} and {b:one system of fundamental law and justice}.')
    n.flow(['{R:Supreme Court}', '{R:High Courts}', '{R:District courts}', '{R:Lower courts}'])
    n.compare([('{R:India – single system}', ['one hierarchy of courts', 'enforces {r:Central + state} laws', '{b:from GoI Act 1935}']),
               ('{R:USA – double system}', ['federal courts → federal laws', 'state courts → state laws'])])
    n.para('[[Successor of Federal Court & Privy Council]] The Supreme Court of India was {r:inaugurated on January 28, 1950}. It succeeded the {r:Federal Court of India}, established under the {b:Government of India Act of 1935}. However, the jurisdiction of the Supreme Court is {r:greater than that of its predecessor}. This is because, the Supreme Court has replaced the {r:British Privy Council} as the {b:highest court of appeal}.¹')
    n.flow(['Federal Court (1935)', '{R:Supreme Court – 28 Jan 1950}', '{b:replaced Privy Council}'])
    n.para('[[Constitutional basis (Arts. 124–147)]] {r:Articles 124 to 147} in {r:Part V} of the Constitution deal with the {b:organisation, independence, jurisdiction, powers, procedures} and so on of the Supreme Court. The {r:Parliament} is also authorised to regulate them.')
    n.footnote('1', 'Before 1950, the British Privy Council had the jurisdiction to hear appeals from India.')
    out.append(('01_notes_ch26_intro_supreme_court', n))

    # ---------------- 02 Composition & appointment ----------------
    n = Note('Composition and Appointment')
    n.section('COMPOSITION AND APPOINTMENT')
    n.para('[[Strength – 34 judges]] At present, the Supreme Court consists of {r:thirty-four judges} ({b:one chief justice and thirty three other judges}). Originally, the strength of the Supreme Court was fixed at {r:eight} ({b:one chief justice and seven other judges}). The {r:Parliament} has increased this number of other judges progressively to {r:ten in 1956}, to {r:thirteen in 1960}, to {r:seventeen in 1977}, to {r:twenty-five in 1986}, to {r:thirty in 2008} and to {r:thirty-three in 2019}.')
    n.flow(['1950: {r:7}', '1956: {r:10}', '1960: {r:13}', '1977: {r:17}', '1986: {r:25}', '2008: {r:30}', '2019: {r:33}'])
    n.arrow('other judges (excluding CJI) · today {r:33 + CJI = 34}', x=340)
    n.para('[[Acts on strength]] The various Acts relating to the composition of the Supreme Court are summarised in {r:Table 26.2}.')
    n.subsub('Appointment of Judges')
    n.para('[[Appointment by President]] The judges of the Supreme Court are {r:appointed by the President}. The {r:chief justice} is appointed by the President after consultation with such judges of the Supreme Court and high courts as he/she deems necessary. The {r:other judges} are appointed by President after consultation with the {b:chief justice} and such other judges of the Supreme Court and the high courts as he/she deems necessary. The consultation with the chief justice is {r:obligatory} in the case of appointment of a judge other than Chief justice.')
    n.subsub('Controversy over Consultation')
    n.para('[[Judges cases – meaning of ‘consultation’]] The Supreme Court has given different interpretation of the word ‘{r:consultation}’ in the above provision. In the {r:First Judges case¹ᵃ (1981)}, the Court held that consultation {b:does not mean concurrence} and it only implies {b:exchange of views}. But, in the {r:Second Judges case¹ᵇ (1993)}, the Court reversed its earlier ruling and changed the meaning of the word consultation to {r:concurrence}. Hence, it ruled that the advice tendered by the Chief Justice of India is {r:binding on the President} in the matters of appointment of the judges of the Supreme Court. But, the Chief Justice would tender his/her advice on the matter after consulting {b:two of his/her seniormost colleagues}. Similarly, in the {r:Third Judges case² (1998)}, the Court opined that the consultation process to be adopted by the Chief justice of India requires ‘{r:consultation of plurality judges}’. The sole opinion of the chief justice of India does not constitute the consultation process. He/she should consult a {r:collegium of four seniormost judges} of the Supreme Court and even if {b:two judges give an adverse opinion}, he/she should not send the recommendation to the government. The court held that the recommendation made by the chief justice of India without complying with the norms and requirements of the consultation process are {r:not binding} on the government.')
    n.flow(['{R:1st Judges (1981)}: consultation ≠ concurrence', '{R:2nd Judges (1993)}: concurrence · CJI + 2', '{R:3rd Judges (1998)}: collegium CJI + 4', '{R:4th Judges (2015)}: NJAC struck down'])
    n.para('[[NJAC and Fourth Judges case]] The {r:99th Constitutional Amendment Act of 2014} and the {r:National Judicial Appointments Commission Act of 2014} have replaced the {b:collegium system} of appointing judges to the Supreme Court and High Courts with a new body called the {r:National Judicial Appointments Commission (NJAC)}. However, in {r:2015}, the Supreme Court has declared both the 99th Constitutional Amendment as well as the NJAC Act as {r:unconstitutional and void}. Consequently, the earlier {r:collegium system became operative again}. This verdict was delivered by the Supreme Court in the {r:Fourth Judges case²ᵃ (2015)}. The court opined that the new system (i.e., NJAC) would affect the {b:independence of the judiciary}.')
    n.subsub('Appointment of Chief Justice')
    n.para('[[Seniority convention for CJI]] From {r:1950 to 1973}, the practice has been to appoint the {r:seniormost judge} of the Supreme Court as the chief justice of India. This established convention was violated in {r:1973} when {r:A.N. Ray} was appointed as the Chief Justice of India by {b:superseding three senior judges}.³ Again in {r:1977}, {r:M.U. Beg} was appointed as the chief justice of India by {b:superseding the then senior-most judge}.⁴ This discretion of the government was curtailed by the Supreme Court in the {r:Second Judges case (1993)}, in which the Supreme Court ruled that the {r:seniormost judge} of the Supreme Court should alone be appointed to the office of the chief justice of India.')
    n.flow(['1950–73: {r:seniority}', '1973: {r:A.N. Ray} (3 superseded)', '1977: {r:M.U. Beg} (1 superseded)', '1993: {R:seniority binding}'])
    n.footnote('1a', 'S.P. Gupta vs. Union of India (1981).')
    n.footnote('1b', 'Supreme Court Advocates-on-Record Association vs. Union of India (1993).')
    n.footnote('2', 'In Re-Presidential Reference (1998). The President sought the Supreme Court’s opinion (under Article 143) on certain doubts over the Consultation process to be adopted by the chief justice of India as stipulated in the 1993 case.')
    n.footnote('2a', 'Supreme Court Advocates-on-Record Association vs. Union of India (2015).')
    n.footnote('3', 'A.N. Ray was fourth in seniority. The three superseded judges were J.M. Shelat, K.S. Hegde and A.N. Grover. All the three judges resigned from the Supreme Court. They were superseded due to their judgement in Kesavananda Bharati case (1973), which was not favourable to the Government.')
    n.footnote('4', 'He was H.R. Khanna and he too resigned. His dissenting judgement upholding the right to life even during emergency in the ADM Jabalpur vs. Shivkant Shukla case (1976) was not appreciated by the Government.')
    out.append(('02_notes_composition_appointment', n))

    # ---------------- 03 Qualifications, oath, salaries ----------------
    n = Note('Qualifications, Oath and Salaries')
    n.section('QUALIFICATIONS, OATH AND SALARIES')
    n.subsub('Qualifications of Judges')
    n.para('[[Eligibility of SC judge]] A person to be appointed as a judge of the Supreme Court should have the following qualifications:')
    n.items([('1.', '[[Citizenship]] He/she should be a {r:citizen of India}.'),
             ('2.', '[[Judicial / legal experience]] (a) He/she should have been a {r:judge of a High Court} (or high courts in succession) for {r:five years}; or (b) He/she should have been an {r:advocate of a High Court} (or High Courts in succession) for {r:ten years}; or (c) He/she should be a {r:distinguished jurist} in the opinion of the President.')])
    n.tree(['{r:HC judge – 5 years}', '{r:HC advocate – 10 years}', '{r:distinguished jurist}'])
    n.para('[[No minimum age]] From the above, it is clear that the Constitution has {r:not prescribed a minimum age} for appointment as a judge of the Supreme Court.')
    n.subsub('Oath or Affirmation')
    n.para('[[Oath before President]] A person appointed as a judge of the Supreme Court, before entering upon his/her Office, has to make and subscribe an {r:oath or affirmation before the President}, or some person appointed by him/her for this purpose. In his/her oath, a judge of the Supreme Court swears:')
    n.items([('1.', '[[Allegiance to Constitution]] to bear {r:true faith and allegiance to the Constitution} of India;'),
             ('2.', '[[Sovereignty and integrity]] to uphold the {r:sovereignty and integrity} of India;'),
             ('3.', '[[Impartial duty]] to duly and faithfully and to the best of his/her ability, knowledge and judgement perform the duties of the Office {r:without fear or favour, affection or ill-will}; and'),
             ('4.', '[[Uphold Constitution and laws]] to {r:uphold the Constitution and the laws}.')])
    n.subsub('Salaries and Allowances')
    n.para('[[Salaries fixed by Parliament]] The {r:salaries, allowances, privileges, leave and pension} of the judges of the Supreme Court are determined from time to time by the {r:Parliament}. They {r:cannot be varied to their disadvantage} after their appointment except during a {r:financial emergency}. In {r:2018}, the salary of the {r:chief justice} was increased from ₹1 lakh to {r:₹2.80 lakh} per month and that of a {r:judge} from ₹90,000 to {r:₹2.50 lakh} per month⁵. They are also paid {b:sumptuary allowance} and provided with {b:free accommodation} and other facilities like medical, car, telephone, etc.')
    n.compare([('{R:Chief Justice}', ['₹1 lakh → {r:₹2.80 lakh}/month (2018)']), ('{R:Judge}', ['₹90,000 → {r:₹2.50 lakh}/month (2018)'])])
    n.para('[[Pension – 50%]] The retired chief justice and judges are entitled to {r:50 per cent of their last drawn salary} as monthly pension.')
    n.footnote('5', 'In 1950, their salaries were fixed at ₹5,000 per month and ₹4,000 per month respectively. In 1986, their salaries were raised to ₹10,000 per month and ₹9,000 per month respectively. In 1998, their salaries were raised to ₹33,000 per month and ₹30,000 per month respectively. In 2009, their salaries were raised to ₹1 lakh per month and ₹90,000 per month respectively.')
    out.append(('03_notes_qualifications_oath_salaries', n))

    # ---------------- 04 Tenure and removal ----------------
    n = Note('Tenure and Removal')
    n.section('TENURE AND REMOVAL')
    n.subsub('Tenure of Judges')
    n.para('[[No fixed tenure]] The Constitution has {r:not fixed the tenure} of a judge of the Supreme Court. However, it makes the following three provisions in this regard:')
    n.items([('1.', '[[Age 65]] He/she holds office until he/she attains the {r:age of 65 years}. Any question regarding his/her age is to be determined by such authority and in such manner as provided by {b:Parliament}.'),
             ('2.', '[[Resignation]] He/she can {r:resign} from his/her office by writing to the {r:President}.'),
             ('3.', '[[Removal]] He/she can be {r:removed} from his/her office by the President on the {r:recommendation of the Parliament}.')])
    n.subsub('Removal of Judges')
    n.para('[[Removal by special majority]] A judge of the Supreme Court can be removed from his/her Office by an {r:order of the President}. The President can issue the removal order only after an {r:address by Parliament} has been presented to him/her in the {b:same session} for such removal. The address must be supported by a {r:special majority of each House} of Parliament ({b:ie, a majority of the total membership of that House and a majority of not less than two-thirds of the members of that House present and voting}). The grounds of removal are two—{r:proved misbehaviour or incapacity}.')
    n.para('[[Judges Enquiry Act, 1968]] The {r:Judges Enquiry Act (1968)} regulates the procedure relating to the removal of a judge of the Supreme Court by the process of {r:impeachment⁶}:')
    n.items([('1.', '[[Removal motion – 100 LS / 50 RS]] A removal motion signed by {r:100 members} (in the case of Lok Sabha) or {r:50 members} (in the case of Rajya Sabha) is to be given to the {b:Speaker/Chairman}.'),
             ('2.', '[[Admission of motion]] The Speaker/Chairman may {r:admit the motion or refuse} to admit it.'),
             ('3.', '[[Three-member inquiry committee]] If it is admitted, then the Speaker/Chairman is to constitute a {r:three-member committee} to investigate into the charges.'),
             ('4.', '[[Composition of committee]] The committee should consist of (a) the {b:chief justice or a judge of the Supreme Court}, (b) a {b:chief justice of a high court}, and (c) a {b:distinguished jurist}.'),
             ('5.', '[[Finding of guilt]] If the committee finds the judge to be {r:guilty of misbehaviour or suffering from an incapacity}, the House can take up the consideration of the motion.'),
             ('6.', '[[Special majority in both Houses]] After the motion is passed by each House of Parliament by {r:special majority}, an address is presented to the President for removal of the judge.'),
             ('7.', '[[President’s removal order]] Finally, the {r:President passes an order} removing the judge.')])
    n.flow(['motion: {r:100 LS / 50 RS}', 'Speaker/Chairman admits', '{r:3-member committee}', 'guilty?', '{r:special majority} both Houses', '{R:President’s order}'])
    n.para('[[No judge impeached – Ramaswami case]] It is interesting to know that {r:no judge of the Supreme Court has been impeached so far}. The first case of impeachment is that of {r:Justice V. Ramaswami} of the Supreme Court ({r:1991–1993}). Though the enquiry Committee found him/her guilty of misbehaviour, he/she could not be removed as the impeachment motion was {r:defeated in the Lok Sabha}. The {b:Congress Party abstained from voting}.')
    n.footnote('6', 'The word ‘impeachment’ is not used in the constitution in relation to the removal of judges. However, it is used only in the case of the removal of the President.')
    out.append(('04_notes_tenure_removal', n))

    # ---------------- 05 Acting, ad hoc, retired; seat & procedure ----------------
    n = Note('Acting, Ad hoc and Retired Judges; Seat and Procedure')
    n.section('ACTING, ADHOC AND RETIRED JUDGES')
    n.subsub('Acting Chief Justice')
    n.para('[[Acting CJI]] The {r:President} can appoint a judge of the Supreme Court as an {r:acting Chief Justice of India} when:')
    n.items([('1.', '[[Vacancy]] the office of Chief Justice of India is {r:vacant}; or'), ('2.', '[[Temporary absence]] the Chief Justice of India is {r:temporarily absent}; or'),
             ('3.', '[[Inability]] the Chief Justice of India is {r:unable to perform} the duties of his/her office.')])
    n.subsub('Ad hoc Judge')
    n.para('[[Ad hoc judge – lack of quorum]] When there is a {r:lack of quorum} of the permanent judges to hold or continue any session of the Supreme Court, the {r:Chief Justice of India} can appoint a {r:judge of a High Court} as an {r:ad hoc judge} of the Supreme Court for a {b:temporary period}. He/she can do so only after consultation with the {b:chief justice of the High Court concerned} and with the {r:previous consent of the President}. The judge so appointed should be {b:qualified for appointment as a judge of the Supreme Court}. It is the duty of the judge so appointed to attend the sittings of the Supreme Court, {b:in priority to other duties} of his/her office. While so attending, he/she enjoys all the jurisdiction, powers and privileges (and discharges the duties) of a judge of the Supreme Court.')
    n.subsub('Retired Judge')
    n.para('[[Retired judge on request]] At any time, the {r:chief justice of India} can request a {r:retired judge of the Supreme Court} or a {r:retired judge of a high court} (who is duly qualified for appointment as a judge of the Supreme Court) to act as a judge of the Supreme Court for a {b:temporary period}. He/she can do so only with the {r:previous consent of the President} and also of the {r:person to be so appointed}. Such a judge is entitled to such allowances as the President may determine. He/she will also enjoy all the jurisdiction, powers and privileges of a judge of Supreme Court. But, he/she will {r:not otherwise be deemed to be a judge} of the Supreme Court.')
    n.table(['{R:Type}', '{R:Appointed by}', '{R:Condition / consent}'],
            [['Acting CJI', '{r:President}', 'CJI post vacant / absent / unable'],
             ['Ad hoc judge', '{r:CJI}', 'lack of quorum · consult HC CJ · {b:President’s consent}'],
             ['Retired judge', '{r:CJI}', '{b:President’s consent} + person’s consent']], [150, 150, 300], src=False)
    n.section('SEAT AND PROCEDURE')
    n.subsub('Seat of Supreme Court')
    n.para('[[Seat – Delhi]] The Constitution declares {r:Delhi as the seat} of the Supreme Court. But, it also authorises the {r:chief justice of India} to appoint {b:other place or places} as seat of the Supreme Court. He/she can take decision in this regard only with the {r:approval of the President}. This provision is only {r:optional and not compulsory}. This means that no court can give any direction either to the President or to the Chief Justice to appoint any other place as a seat of the Supreme Court.')
    n.subsub('Procedure of the Court')
    n.para('[[Rules and benches]] The Supreme Court can, with the {r:approval of the President}, make rules for regulating generally the practice and procedure of the Court. The {r:Constitutional cases} or references made by the President under {r:Article 143} are decided by a Bench consisting of {r:at least five judges}. All other cases are decided by {b:single judges and division benches}. The judgements are delivered by the {r:open court}. All judgements are by {r:majority vote} but if differing, then judges can give {b:dissenting judgements or opinions}.')
    out.append(('05_notes_acting_adhoc_retired_seat_procedure', n))

    # ---------------- 06 Independence ----------------
    n = Note('Independence of Supreme Court')
    n.section('INDEPENDENCE OF SUPREME COURT')
    n.para('[[Need for judicial independence]] The Supreme Court has been assigned a very significant role in the Indian democratic political system. It is a {r:federal court}, the {r:highest court of appeal}, the {r:guarantor of the fundamental rights} of the citizens and {r:guardian of the Constitution}. Therefore, its {r:independence} becomes very essential for the effective discharge of the duties assigned to it. It should be free from the encroachments, pressures and interferences of the {b:executive (council of ministers)} and the {b:Legislature (Parliament)}. It should be allowed to do justice {r:without fear or favour}.')
    n.tree(['{r:federal court}', '{r:highest court of appeal}', '{r:guarantor of FRs}', '{r:guardian of Constitution}'])
    n.para('[[Safeguards of independence]] The Constitution has made the following provisions to safeguard and ensure the {r:independent and impartial functioning} of the Supreme Court:')
    n.items([
        ('1.', '[[!Mode of Appointment]] The judges of the Supreme Court are appointed by the {r:President (which means the cabinet)} in consultation with the {r:members of the judiciary itself} (ie, judges of the Supreme Court and the high courts). This provision {b:curtails the absolute discretion of the executive} as well as ensures that the judicial appointments are not based on any political or practical considerations.'),
        ('2.', '[[!Security of Tenure]] The judges of the Supreme Court are provided with the {r:Security of Tenure}. They can be removed from office by the President only in the manner and on the grounds mentioned in the Constitution. This means that they {r:do not hold their office during the pleasure of the President}, though they are appointed by him/her. This is obvious from the fact that {b:no judge of the Supreme Court has been removed (or impeached) so far}.'),
        ('3.', '[[!Fixed Service Conditions]] The salaries, allowances, privileges, leave and pension of the judges of the Supreme Court are determined from time to time by the Parliament. They {r:cannot be changed to their disadvantage} after their appointment except during a {r:financial emergency}. Thus, the conditions of service of the judges of the Supreme Court remain same during their term of Office.'),
        ('4.', '[[!Expenses Charged on Consolidated Fund]] The salaries, allowances and pensions of the judges and the staff as well as all the administrative expenses of the Supreme Court are {r:charged on the Consolidated Fund of India}. Thus, they are {r:non-votable} by the Parliament ({b:though they can be discussed by it}).'),
        ('5.', '[[!Conduct of Judges cannot be Discussed]] The Constitution {r:prohibits any discussion} in Parliament or in a State Legislature with respect to the conduct of the judges of the Supreme Court in the discharge of their duties, except when an {r:impeachment motion} is under consideration of the Parliament.'),
        ('6.', '[[!Ban on Practice after Retirement]] The retired judges of the Supreme Court are {r:prohibited from pleading or acting in any Court} or before any authority within the territory of India. This ensures that they do not favour any one in the hope of future favour.'),
        ('7.', '[[!Power to Punish for its Contempt]] The Supreme Court can {r:punish any person for its contempt}. Thus, its actions and decisions cannot be criticised and opposed by any body. This power is vested in the Supreme Court to maintain its {b:authority, dignity and honour}.'),
        ('8.', '[[!Freedom to Appoint its Staff]] The {r:Chief Justice of India} can appoint officers and servants of the Supreme Court {r:without any interference from the executive}. He/she can also prescribe their conditions of service.'),
        ('9.', '[[!Its Jurisdiction cannot be Curtailed]] The Parliament is {r:not authorised to curtail} the jurisdiction and powers of the Supreme Court. The Constitution has guaranteed to the Supreme Court, jurisdiction of various kinds. However, the {r:Parliament can extend the same}.')])
    n.boxes([['{r:appointment}', 'with judiciary'], ['{r:tenure}', 'not at pleasure'], ['{r:service}', 'no adverse change'], ['{r:expenses}', 'charged on CFI'], ['{r:conduct}', 'no discussion']], size=13)
    n.boxes([['{r:no practice}', 'after retirement'], ['{r:contempt}', 'power to punish'], ['{r:staff}', 'CJI appoints'], ['{r:jurisdiction}', 'cannot be curtailed']], size=13)
    out.append(('06_notes_independence_of_supreme_court', n))

    # ---------------- 07 Jurisdiction overview + original ----------------
    n = Note('Jurisdiction – Overview and Original Jurisdiction')
    n.section('JURISDICTION AND POWERS OF SUPREME COURT')
    n.para('[[Most powerful Supreme Court]] The Constitution has conferred a very {r:extensive jurisdiction and vast powers} on the Supreme Court. It is not only a {r:Federal Court} like the {b:American Supreme Court} but also a {r:final court of appeal} like the {b:British House of Lords} (the Upper House of the British Parliament). It is also the {r:final interpreter and guardian of the Constitution} and {r:guarantor of the fundamental rights} of the citizens. Further, it has {r:advisory and supervisory powers}. Therefore, {r:Alladi Krishnaswamy Ayyar}, a member of the Drafting Committee of the Constituent Assembly, rightly remarked: “{b:The Supreme Court of India has more powers than any other Supreme Court in any part of the world.}” The jurisdiction and powers of the Supreme Court can be classified into the following:')
    n.items([('1.', 'Original Jurisdiction.'), ('2.', 'Writ Jurisdiction.'), ('3.', 'Appellate Jurisdiction.'), ('4.', 'Advisory Jurisdiction.'),
             ('5.', 'A Court of Record.'), ('6.', 'Power of Judicial Review.'), ('7.', 'Constitutional Interpretation'), ('8.', 'Other Powers.')])
    n.boxes([['{r:Original}'], ['{r:Writ}'], ['{r:Appellate}'], ['{r:Advisory}']], size=13)
    n.boxes([['{r:Court of Record}'], ['{r:Judicial Review}'], ['{r:Interpretation}'], ['{r:Other}']], size=13)
    n.sub('1. Original Jurisdiction')
    n.para('[[Federal disputes]] As a {r:federal court}, the Supreme Court decides the {r:disputes between different units of the Indian Federation}. More elaborately, any dispute:')
    n.items([('(a)', '[[Centre vs state(s)]] Between the {r:Centre and one or more states}; or'),
             ('(b)', '[[Centre & states vs states]] Between the {r:Centre and any state or states on one side} and {r:one or more other states} on the other side; or'),
             ('(c)', '[[Inter-state dispute]] Between {r:two or more states}.')])
    n.tree(['{r:Centre vs state(s)}', '{r:Centre + state(s) vs state(s)}', '{r:state vs state}'])
    n.para('[[Exclusive original jurisdiction]] In the above federal disputes, the Supreme Court has {r:exclusive original jurisdiction}. {b:Exclusive} means, no other court can decide such disputes and {b:original} means, the power to hear such disputes in the first instance, not by way of appeal.')
    n.para('[[Legal right, not political]] With regard to the exclusive original jurisdiction of the Supreme Court, two points should be noted. One, the dispute must involve a question ({b:whether of law or fact}) on which the existence or extent of a {r:legal right} depends. Thus, the {r:questions of political nature are excluded} from it. Two, any suit brought before the Supreme Court by a {r:private citizen against the Centre or a state cannot be entertained} under this.')
    n.para('[[Exclusions from original jurisdiction]] Further, this jurisdiction of the Supreme Court does not extend to the following:')
    n.items([('(a)', '[[Pre-constitution treaties]] A dispute arising out of any {r:treaty, agreement, covenant, engagement, sanad} or other similar instrument which, having been entered into or executed {b:before the commencement of the constitution}, continues in operation after such commencement, or which provides that the said jurisdiction shall not extend to such a dispute.'),
             ('(b)', '[[River water disputes (Art. 262)]] {r:Inter-state river water disputes}.⁷'),
             ('(c)', '[[Finance Commission matters]] Matters referred to the {r:Finance Commission}.'),
             ('(d)', '[[Expenses & pensions]] {r:Adjustment of certain expenses and pensions} between the Centre and the states.')])
    n.para('[[First suit – West Bengal vs Centre (1961)]] In {r:1961}, the {r:first suit}, under the original jurisdiction of the Supreme Court, was brought by {r:West Bengal against the Centre}. The State Government challenged the Constitutional validity of the {b:Coal Bearing Areas (Acquisition and Development) Act, 1957}, passed by the Parliament. However, the Supreme Court {r:dismissed the suit} by upholding the validity of the Act.')
    n.footnote('7', 'The Inter-State River Water Disputes Act of 1956 has excluded the original jurisdiction of the Supreme Court in disputes between states with respect to the use, distribution or control of the water of inter-state river or river valley.')
    out.append(('07_notes_jurisdiction_original', n))

    # ---------------- 08 Writ jurisdiction ----------------
    n = Note('Writ Jurisdiction')
    n.sub('2. Writ Jurisdiction')
    n.para('[[Guarantor of Fundamental Rights]] The Constitution has constituted the Supreme Court as the {r:guarantor and defender of the fundamental rights} of the citizens. The Supreme Court is empowered to issue {r:writs} including {b:habeas corpus, mandamus, prohibition, quo warranto and certiorari} for the enforcement of the fundamental rights of an aggrieved citizen. In this regard, the Supreme Court has {r:original jurisdiction} in the sense that an aggrieved citizen can {b:directly go to the Supreme Court}, not necessarily by way of appeal. However, the writ jurisdiction of the Supreme Court is {r:not exclusive}. The {r:high courts} are also empowered to issue writs for the enforcement of the Fundamental Rights. It means, when the Fundamental Rights of a citizen are violated, the aggrieved party has the {b:option of moving either the high court or the Supreme Court directly}.')
    n.tree(['{b:habeas corpus}', '{b:mandamus}', '{b:prohibition}', '{b:quo warranto}', '{b:certiorari}'], size=13)
    n.para('[[Exclusive vs concurrent original jurisdiction]] Therefore, the original jurisdiction of the Supreme Court with regard to {r:federal disputes} is different from its original jurisdiction with regard to disputes relating to {r:fundamental rights}. In the first case, it is {r:exclusive} and in the second case, it is {r:concurrent with high courts} jurisdiction. Moreover, the parties involved in the first case are {b:units of the federation (Centre and states)} while the dispute in the second case is between a {b:citizen and the Government (Central or state)}.')
    n.compare([('{R:Federal disputes}', ['{r:exclusive}', 'Centre vs states']), ('{R:Fundamental Rights}', ['{r:concurrent} with HCs', 'citizen vs Government'])])
    n.para('[[SC vs HC writ jurisdiction]] There is also a difference between the writ jurisdiction of the Supreme Court and that of the high court. The Supreme Court can issue writs {r:only for the enforcement of the Fundamental Rights} and not for other purposes. The high court, on the other hand, can issue writs not only for the enforcement of the fundamental rights but also {r:for other purposes}. It means that the writ jurisdiction of the {r:high court is wider} than that of the Supreme Court. But, the {b:Parliament can confer on the Supreme Court, the power to issue writs for other purposes also}.')
    n.compare([('{R:Supreme Court writs}', ['only Fundamental Rights', '{b:Parliament may widen}']), ('{R:High Court writs}', ['FRs {r:+ other purposes}', '{r:wider}'])])
    out.append(('08_notes_writ_jurisdiction', n))

    # ---------------- 09 Appellate ----------------
    n = Note('Appellate Jurisdiction')
    n.sub('3. Appellate Jurisdiction')
    n.para('[[Highest court of appeal]] As mentioned earlier, the Supreme Court has not only succeeded the {r:Federal Court of India} but also replaced the {r:British Privy Council} as the {r:highest court of appeal}. The Supreme Court is primarily a {r:court of appeal} and hears appeals against the judgements of the High courts. It enjoys a wide appellate jurisdiction which can be classified under {r:four heads}:')
    n.items([('(a)', 'Appeals in constitutional matters.'), ('(b)', 'Appeals in civil matters.'), ('(c)', 'Appeals in criminal matters.'), ('(d)', 'Appeals by special leave.')])
    n.tree(['{r:Constitutional}', '{r:Civil}', '{r:Criminal}', '{r:Special leave}'])
    n.subsub('(a) Constitutional Matters')
    n.para('[[HC certificate – constitutional question]] In the constitutional cases, an appeal can be made to the Supreme Court against the judgement of a high court if the {r:high court certifies} that the case involves a {r:substantial question of law that requires the interpretation of the Constitution}. Based on the certificate, the party in the case can appeal to the Supreme Court on the ground that the question has been wrongly decided.')
    n.subsub('(b) Civil Matters')
    n.para('[[HC certificate – civil cases]] In civil cases, an appeal lies to the Supreme Court from any judgement of a high court if the high court certifies—')
    n.items([('(i)', '[[Question of general importance]] that the case involves a {r:substantial question of law of general importance}; and'), ('(ii)', '[[Needs SC decision]] that the question {r:needs to be decided by the Supreme Court}.')])
    n.para('[[30th Amendment – no monetary limit]] Originally, only those civil cases that involved a sum of {r:not less than ₹20,000} could be appealed before the Supreme Court. But this monetary limit was {r:removed by the 30th Constitutional Amendment Act of 1972}.')
    n.subsub('(c) Criminal Matters')
    n.para('[[Criminal appeals]] The Supreme Court hears appeals against the judgement in a criminal proceeding of a high court if the high court—')
    n.items([('(i)', '[[Acquittal reversed – death sentence]] has on appeal {r:reversed an order of acquittal} of an accused person and {r:sentenced him/her to death}; or'),
             ('(ii)', '[[Case withdrawn – death sentence]] has {r:taken before itself any case} from any subordinate court and convicted the accused person and {r:sentenced him/her to death}; or'),
             ('(iii)', '[[Fit case certificate]] {r:certifies} that the case is a fit one for appeal to the Supreme Court.')])
    n.para('[[Appeal as of right]] In the {r:first two cases}, an appeal lies to the Supreme Court {r:as a matter of right} (ie, without any certificate of the high court). But if the high court has {b:reversed the order of conviction and has ordered the acquittal} of the accused, there is {r:no right to appeal} to the Supreme Court.')
    n.para('[[1970 enlargement]] In {r:1970}, the Parliament had {r:enlarged the Criminal Appellate Jurisdiction} of the Supreme Court. Accordingly, an appeal lies to the Supreme Court from the judgement of a high court if the high court:')
    n.items([('(i)', '[[Acquittal reversed – life/10 years]] has on appeal, reversed an order of acquittal of an accused person and sentenced him/her to {r:imprisonment for life or for ten years}; or'),
             ('(ii)', '[[Case withdrawn – life/10 years]] has taken before itself any case from any subordinate court and convicted the accused person and sentenced him/her to {r:imprisonment for life or for ten years}.')])
    n.subsub('(d) Appeal by Special Leave')
    n.para('[[Special Leave Petition (Art. 136)]] The Supreme Court is authorised to grant in its {r:discretion special leave to appeal} from any judgement in any matter passed by {r:any court or tribunal} in the country ({b:except military tribunal and court martial}). This provision contains the four aspects as under:')
    n.items([('(i)', '[[Discretionary]] It is a {r:discretionary power} and hence, cannot be claimed as a matter of right.'),
             ('(ii)', '[[Final or interlocutory]] It can be granted in any judgement whether {r:final or interlocutory}.'),
             ('(iii)', '[[Any subject matter]] It may be related to {r:any matter}—constitutional, civil, criminal, income-tax, labour, revenue, advocates, etc.'),
             ('(iv)', '[[Any court or tribunal]] It can be granted against {r:any court or tribunal} and not necessarily against a high court ({b:of course, except a military court}).')])
    n.para('[[Plenary jurisdiction – used sparingly]] Thus, the scope of this provision is very wide and it vests the Supreme Court with a {r:plenary jurisdiction} to hear appeals. On the exercise of this power, the Supreme Court itself held that ‘{b:being an exceptional and overriding power, it has to be exercised sparingly and with caution and only in special extraordinary situations. Beyond that it is not possible to fetter the exercise of this power by any set formula or rule}’.')
    out.append(('09_notes_appellate_jurisdiction', n))

    # ---------------- 10 Advisory ----------------
    n = Note('Advisory Jurisdiction')
    n.sub('4. Advisory Jurisdiction')
    n.para('[[Article 143 – President’s reference]] The Constitution ({r:Article 143}) authorises the {r:President} to seek the {r:opinion of the Supreme Court} in the two categories of matters:')
    n.items([('(a)', '[[Question of public importance]] On any {r:question of law or fact of public importance} which has arisen or which is likely to arise.'),
             ('(b)', '[[Pre-constitution treaty disputes]] On any dispute arising out of any {r:pre-constitution treaty, agreement, covenant, engagement, sanad} or other similar instrument, which is excluded from the original jurisdiction of the Supreme Court.')])
    n.para('[[Opinion not binding]] In the first case, the Supreme Court {r:may tender or may refuse} to tender its opinion to the President. But, in the second case, the Supreme Court ‘{r:must}’ tender its opinion to the President. In both the cases, the opinion expressed by the Supreme Court is {r:only advisory and not a judicial pronouncement}. Hence, it is {r:not binding on the President}; he/she may follow or may not follow the opinion. However, it facilitates the government to have an {b:authoritative legal opinion} on a matter to be decided by it.')
    n.compare([('{R:(a) Question of law / fact}', ['SC {r:may} or may not answer']), ('{R:(b) Pre-constitution treaty dispute}', ['SC {r:must} answer'])])
    n.arrow('both: {r:advisory only} · {b:not binding on President}', x=340)
    n.para('[[Fifteen references so far]] So far, the President has made {r:fifteen references} to the Supreme Court under its advisory jurisdiction ({b:also known as consultative jurisdiction}). These are mentioned below in the chronological order.')
    n.items([('1.', 'Delhi Laws Act in {r:1951}'), ('2.', 'Kerala Education Bill in {r:1958}'), ('3.', 'Berubari Union in {r:1960}'), ('4.', 'Sea Customs Act in {r:1963}'),
             ('5.', 'Keshav Singh’s case relating to the privileges of the Legislature in {r:1964}'), ('6.', 'Presidential Election in {r:1974}'),
             ('7.', 'Special Courts Bill in {r:1978}'), ('8.', 'Jammu and Kashmir Resettlement Act in {r:1982}'), ('9.', 'Cauvery Water Disputes Tribunal in {r:1992}'),
             ('10.', 'Rama Janma Bhumi case in {r:1993}'), ('11.', 'Consultation process to be adopted by the chief justice of India in {r:1998}'),
             ('12.', 'Legislative competence of the Centre and States on the subject of natural gas and liquefied natural gas in {r:2001}'),
             ('13.', 'The constitutional validity of the Election Commission’s decision on deferring the Gujarat Assembly Elections in {r:2002}'),
             ('14.', 'Punjab Termination of Agreements Act in {r:2004}'),
             ('15.', '2G spectrum case verdict and the mandatory auctioning of natural resources across all sectors in {r:2012}')], kw=False)
    out.append(('10_notes_advisory_jurisdiction', n))

    # ---------------- 11 Court of record, contempt, judicial review ----------------
    n = Note('Court of Record, Contempt and Judicial Review')
    n.sub('5. A Court of Record')
    n.para('[[Two powers of a Court of Record]] As a {r:Court of Record}, the Supreme Court has {r:two powers}:')
    n.items([('(a)', '[[Records as precedents]] The judgements, proceedings and acts of the Supreme Court are {r:recorded for perpetual memory and testimony}. These records are admitted to be of {b:evidentiary value} and cannot be questioned when produced before any court. They are recognised as {r:legal precedents and legal references}.'),
             ('(b)', '[[Contempt power]] It has {r:power to punish for contempt of itself}. In {r:1991}, the Supreme Court has ruled that it has power to punish for contempt not only of itself but also of {r:high courts, subordinate courts and tribunals} functioning in the entire country.')])
    n.subsub('Contempt of Courts Act (1971)')
    n.para('[[Sanyal Committee → 1971 Act]] In {r:1961}, the government appointed a special committee under the chairmanship of {r:H.N. Sanyal}, the then Additional Solicitor General of India, to examine the law relating to the contempt of courts. This committee submitted its report in {r:1963}. Based on the recommendations made by the committee, the {r:Contempt of Courts Act, 1971} was enacted by the Parliament.')
    n.flow(['Sanyal Committee {r:1961}', 'report {r:1963}', '{R:Contempt of Courts Act 1971}'])
    n.para('[[Civil vs criminal contempt]] Under the Act, the contempt of court may be {r:civil or criminal}. The {r:civil contempt} means {b:wilful disobedience} to any judgement, order, writ or other process of a court or {b:wilful breach of an undertaking} given to a court. The {r:criminal contempt}, on the other hand, means the publication of any matter or doing an act which—(i) {b:scandalises or lowers the authority} of a court; or (ii) {b:prejudices or interferes} with the due course of a judicial proceeding; or (iii) {b:interferes or obstructs the administration of justice} in any other manner.')
    n.compare([('{R:Civil contempt}', ['wilful disobedience of order', 'wilful breach of undertaking']), ('{R:Criminal contempt}', ['scandalises / lowers authority', 'prejudices proceedings', 'obstructs justice'])])
    n.para('[[Not contempt]] However, {r:innocent publication} and distribution of matter, {r:fair and accurate report} of judicial proceedings and {r:fair criticism} of judicial acts {b:do not amount to contempt of court}.')
    n.para('[[Punishment]] Under the Act, a contempt of court is punishable with {r:simple imprisonment for a term upto six months} or with {r:fine upto ₹2,000} or with both.')
    n.para('[[Limitation – one year]] The Act also provides that no court shall initiate any proceedings of contempt after the {r:expiry of one year} from the date on which the contempt is alleged to have been committed.')
    n.para('[[Not for Nyaya Panchayats]] Further, this Act is {r:not applicable to contempt of Nyaya Panchayats} or other village courts which have been established for the administration of justice.')
    n.sub('6. Power of Judicial Review')
    n.para('[[Judicial review]] {r:Judicial review} is the power of the Supreme Court to examine the {r:constitutionality of legislative enactments and executive orders} of both the Central and state governments. On examination, if they are found to be violative of the Constitution ({r:ultra-vires}), they can be declared as {r:illegal, unconstitutional and invalid (null and void)} by the Supreme Court. Consequently, they cannot be enforced by the Government.')
    n.flow(['law / executive order', 'examined by SC', '{r:ultra-vires}?', '{R:null and void}'])
    out.append(('11_notes_court_of_record_contempt_judicial_review', n))

    # ---------------- 12 Review, interpretation, other powers ----------------
    n = Note('Review, Interpretation and Other Powers')
    n.sub('7. Review Jurisdiction')
    n.para('[[Review petition – 30 days]] The Supreme Court has power to {r:review any judgement} pronounced or order made by it. A review petition has to be filed {r:within thirty days} from the date of the judgement or order sought to be reviewed. Also, the review petition should be submitted to the {r:same judge or bench} that delivered the judgement or order. Further, a review petition is allowed on the following grounds:')
    n.items([('(i)', 'Discovery of {r:new and important matter or evidence}.'), ('(ii)', '{r:Mistake or error apparent} on the face of the record.'), ('(iii)', 'Any other {r:sufficient reason}.')])
    n.para('[[Curative petition]] The court may either dismiss the review petition or direct notice to the opposite party. However, even after the dismissal of the review petition, the court can still reconsider its final judgement or order by way of a {r:curative petition} on limited grounds like:')
    n.items([('(i)', 'Violation of the {r:principles of natural justice}.'), ('(ii)', 'To cure a {r:gross miscarriage of justice}.'), ('(iii)', 'To prevent {r:abuse of the process} of the court.'), ('(iv)', '{r:Bias} of the judge.')])
    n.flow(['judgement', '{r:review petition} (30 days, same bench)', 'dismissed', '{R:curative petition}'])
    n.sub('8. Constitutional Interpretation')
    n.para('[[Ultimate interpreter]] The Supreme Court is the {r:ultimate interpreter of the Constitution}. It can give final version to the {b:spirit and content} of the provisions of the constitution and the verbiage used in the constitution.')
    n.para('[[Doctrines of interpretation]] While interpreting the constitution, the Supreme Court is guided by a number of {r:doctrines}. In other words, the Supreme Court applies various doctrines in interpreting the constitution. The important doctrines are mentioned below:')
    n.items([('1.', 'Doctrine of Severability'), ('2.', 'Doctrine of Waiver'), ('3.', 'Doctrine of Eclipse'), ('4.', 'Doctrine of Territorial Nexus'),
             ('5.', 'Doctrine of Pith and Substance'), ('6.', 'Doctrine of Colourable Legislation'), ('7.', 'Doctrine of Implied Powers'),
             ('8.', 'Doctrine of Incidental and Ancillary Powers'), ('9.', 'Doctrine of Precedent'), ('10.', 'Doctrine of Occupied Field'),
             ('11.', 'Doctrine of Prospective Overruling'), ('12.', 'Doctrine of Harmonious Construction'), ('13.', 'Doctrine of Liberal Interpretation')])
    n.sub('9. Other Powers')
    n.para('[[Other powers]] Besides the above, the Supreme Court has numerous other powers:')
    n.items([('(a)', '[[Presidential election disputes]] It decides the disputes regarding the {r:election of the President and the vice-President}. In this regard, it has the {r:original, exclusive and final authority}.'),
             ('(b)', '[[PSC members’ conduct]] It enquires into the conduct and behaviour of the {r:chairman and members of the UPSC or SPSC or JSPSC} on a reference made by the President. If it finds them guilty of misbehaviour, it can recommend to the President for their removal. The advice tendered by the Supreme Court in this regard is {r:binding on the President}.'),
             ('(c)', '[[Transfer of cases]] It is authorised to {r:withdraw the cases pending before the high courts} and dispose them by itself. It can also {r:transfer a case or appeal} pending before one high court to another high court.'),
             ('(d)', '[[Law binding on all courts (Art. 141)]] Its {r:law is binding on all courts in India}. Its decree or order is {r:enforceable throughout the country}. All authorities (civil and judicial) in the country should {b:act in aid of the Supreme Court}.'),
             ('(e)', '[[Judicial superintendence]] It has power of {r:judicial superintendence and control} over all the courts and tribunals functioning in the entire territory of the country.')])
    n.para('[[Enlargement of jurisdiction]] The Supreme Court’s jurisdiction and powers with respect to matters in the {r:Union list} can be {r:enlarged by the Parliament}. Further, its jurisdiction and powers with respect to other matters can be enlarged by a {r:special agreement of the Centre and the states}.')
    out.append(('12_notes_review_interpretation_other_powers', n))

    # ---------------- 13 Indian vs American SC ----------------
    n = Note('Indian and American Supreme Courts Compared')
    n.section('INDIAN AND AMERICAN SUPREME COURTS COMPARED')
    n.para('[[India vs USA]] There are differences in the jurisdiction and powers of the {r:Supreme Court of India} and that of the {r:Supreme Court of USA}. These are summarised in {r:Table 26.1}.')
    rows = [
        ['1. Its original jurisdiction is {r:confined to federal cases}.', '1. Its original jurisdiction covers not only federal cases but also cases relating to {r:naval forces, maritime activities, ambassadors}, etc.'],
        ['2. Its appellate jurisdiction covers {r:constitutional, civil and criminal} cases.', '2. Its appellate jurisdiction is confined to {r:constitutional cases only}.'],
        ['3. It has a very wide discretion to grant {r:special leave to appeal} in any matter against the judgement of any court or tribunal (except military).', '3. It has {r:no such plenary power}.'],
        ['4. It has {r:advisory jurisdiction}.', '4. It has {r:no advisory jurisdiction}.'],
        ['5. Its scope of judicial review is {r:limited}.', '5. Its scope of judicial review is {r:very wide}.'],
        ['6. It defends rights of the citizen according to the ‘{r:procedure established by law}’.', '6. It defends rights of the citizen according to the ‘{r:due process of law}’.'],
        ['7. Its jurisdiction and powers {r:can be enlarged by Parliament}.', '7. Its jurisdiction and powers are {r:limited to that conferred by the Constitution}.'],
        ['8. It has power of judicial superintendence and control over state high courts due to {r:integrated judicial system}.', '8. It has no such power due to {r:double (or separated) judicial system}.'],
    ]
    n.table(['{R:Indian Supreme Court}', '{R:American Supreme Court}'], rows, [300, 300], caption='Table 26.1 Comparing Indian and American Supreme Courts')
    out.append(('13_notes_indian_vs_american_supreme_court', n))
    return out
