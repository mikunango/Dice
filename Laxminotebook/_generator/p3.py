from nb import Note

def notes():
    out = []

    # ---------------- 13 Allocation of taxing powers ----------------
    n = Note('Financial Relations – Allocation of Taxing Powers')
    n.section('FINANCIAL RELATIONS')
    n.para('{r:Articles 268 to 293} in {r:Part XII} of the Constitution deal with {b:Centre–state financial relations}. Besides these, there are other provisions dealing with the same subject. These together can be studied under the following heads:')
    n.sub('1. Allocation of Taxing Powers')
    n.para('The Constitution divides the taxing powers between the Centre and the states in the following way:')
    n.bullets(['The {r:Parliament} has {r:exclusive power} to levy taxes on subjects enumerated in the {r:Union List} ({b:which are 13 in number⁸}).',
               'The {r:state legislature} has {r:exclusive power} to levy taxes on subjects enumerated in the {r:State List} ({b:which are 18 in number⁹}).',
               'There are {r:no tax entries in the Concurrent List}. In other words, the concurrent jurisdiction is {b:not available with respect to tax legislation}. But, the {r:101st Amendment Act of 2016} has made an {r:exception} by making a special provision with respect to {r:goods and services tax}. This Amendment has conferred {b:concurrent power upon the Parliament and State Legislatures} to make laws governing goods and services tax¹⁰.',
               'The {r:residuary power of taxation} (that is, the power to impose taxes not enumerated in any of the three lists) is vested in the {r:Parliament}. Under this provision, the Parliament has imposed {b:gift tax, wealth tax and expenditure tax}.'], orig=True)
    n.boxes([['{R:Union List}', '{r:13} tax entries', 'Parliament'], ['{R:State List}', '{r:18} tax entries', 'State legislature'],
             ['{R:Concurrent List}', '{r:no} tax entries', '{b:except GST (101st Amdt)}'], ['{R:Residuary}', 'Parliament', '{b:gift, wealth, expenditure tax}']])
    n.para('The Constitution also draws a distinction between the {r:power to levy and collect a tax} and the {r:power to appropriate the proceeds} of the tax so levied and collected. For example, the {b:income-tax is levied and collected by the Centre} but its proceeds are {b:distributed between the Centre and the states}.')
    n.flow(['{r:Income tax}: levied & collected by Centre', 'proceeds shared {b:Centre + states}'])
    n.sub('2. Restrictions on states’ taxing powers', src=False)
    n.para('Further, the Constitution has placed the following {r:restrictions on the taxing powers of the states}:')
    n.items([('(i)', 'A state legislature can impose {r:taxes on professions, trades, callings and employments}. But, the total amount of such taxes payable by any person should {r:not exceed ₹2,500 per annum}.¹¹'),
             ('(ii)', 'A state legislature is {r:prohibited} from imposing a tax on the {r:supply of goods or services or both} in the following two cases: (a) where such supply takes place {b:outside the state}; and (b) where such supply takes place in the course of {b:import or export}. Further, the Parliament is empowered to formulate the principles for determining when a supply of goods or services or both takes place outside the state, or in the course of import or export¹².'),
             ('(iii)', 'A state legislature can impose tax on the {r:consumption or sale of electricity}. But, no tax can be imposed on the consumption or sale of electricity which is (a) {b:consumed by the Centre or sold to the Centre}; or (b) {b:consumed in the construction, maintenance or operation of any railway} by the Centre or by the concerned railway company or sold to the Centre or the railway company for the same purpose.'),
             ('(iv)', 'A state legislature can impose a tax in respect of any {r:water or electricity} stored, generated, consumed, distributed or sold by any {b:authority established by Parliament} for regulating or developing any {b:inter-state river or river valley}. But, such a law, to be effective, should be {r:reserved for the president’s consideration} and receive his/her assent.')])
    n.boxes([['{R:Profession tax}', 'max {r:₹2,500}/year'], ['{R:Supply tax}', '✘ outside state', '✘ import/export'], ['{R:Electricity}', '✘ Centre / railways'], ['{R:Inter-state river}', '{b:reserve for President}']])
    n.footnote('8', 'Entries—82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92A, 92B and 96.')
    n.footnote('9', 'Entries—45, 46, 47, 48, 49, 50, 51, 53, 54, 56, 57, 58, 59, 60, 61, 62, 63 and 66.')
    n.footnote('10', 'In this regard, the 101st Amendment Act of 2016 inserted Article 246-A in the Constitution.')
    n.footnote('11', 'Originally, this limit was only ₹250 per annum. The 60th Amendment Act of 1988 raised it to ₹2,500 per annum.')
    n.footnote('12', 'These provisions are contained in Article 286, as amended by the 101st Amendment Act of 2016.')
    out.append(('13_notes_fin_allocation_of_taxing_powers', n))

    # ---------------- 14 80th & 101st amendments ----------------
    n = Note('Distribution of Tax Revenues – 80th and 101st Amendments')
    n.sub('2. Distribution of Tax Revenues')
    n.para('The {r:80th Amendment Act of 2000} and the {r:101st Amendment Act of 2016} have introduced {b:major changes} in the scheme of the distribution of tax revenues between the centre and the states.')
    n.subsub('80th Amendment', src=False)
    n.para('The 80th Amendment was enacted to give effect to the recommendations of the {r:10th Finance Commission}. The Commission recommended that out of the total income obtained from certain central taxes and duties, {r:29%} should go to the states. This is known as the ‘{r:Alternative Scheme of Devolution}’ and came into effect {b:retrospectively from April 1, 1996}. This amendment has brought several central taxes and duties like {b:Corporation Tax and Customs Duties} at par with {b:Income Tax (taxes on income other than agricultural income)} as far as their constitutionally mandated sharing with the states is concerned.¹³')
    n.flow(['{r:10th Finance Commission}', '{r:29%} to states', '{R:Alternative Scheme of Devolution}', 'from {b:1 April 1996}'])
    n.subsub('101st Amendment – GST', src=False)
    n.para('The 101st Amendment has paved the way for the introduction of a {r:new tax regime (i.e., goods and services tax – GST)} in the country. Accordingly, the Amendment conferred {r:concurrent taxing powers} upon the Parliament and the State Legislatures to make laws for levying GST on {b:every transaction of supply of goods or services or both}. The GST replaced a number of indirect taxes levied by the Union and the State Governments and is intended to {r:remove the cascading effect of taxes} and provide for a {r:common national market} for goods and services.')
    n.listpara('The Amendment provided for subsuming of various {r:central indirect taxes} and levies such as',
               [('(i)', '{b:Central Excise Duty},'), ('(ii)', '{b:Additional Excise Duties},'), ('(iii)', '{b:Excise Duty levied under the Medicinal and Toilet Preparations (Excise Duties) Act, 1955},'),
                ('(iv)', '{b:Service Tax},'), ('(v)', '{b:Additional Customs Duty commonly known as Countervailing Duty},'), ('(vi)', '{b:Special Additional Duty of Customs}, and'),
                ('(vii)', '{b:Central Surcharges and Cesses}')], 'so far as they related to the supply of goods and services.')
    n.listpara('Similarly, the Amendment provided for subsuming of',
               [('(i)', '{b:State Value Added Tax / Sales Tax},'), ('(ii)', '{b:Entertainment Tax (other than the tax levied by the local bodies)},'),
                ('(iii)', '{b:Central Sales Tax (levied by the Centre and collected by the States)},'), ('(iv)', '{b:Octroi and Entry Tax},'), ('(v)', '{b:Purchase Tax},'),
                ('(vi)', '{b:Luxury Tax},'), ('(vii)', '{b:Taxes on lottery, betting and gambling}, and'), ('(viii)', '{b:State Surcharges and Cesses}')],
               'in so far as they related to the supply of goods and services.')
    n.para('Further, the Amendment {r:deleted Article 268-A} as well as {r:Entry 92-C} in the Union List, both were dealing with {r:service tax}. They were added earlier by the {r:88th Amendment Act of 2003}. The service tax was {b:levied by the Centre but collected and appropriated by both the Centre and the States}.')
    n.compare([('{R:Central taxes subsumed (7)}', ['Central Excise Duty', 'Additional Excise Duties', 'Medicinal & Toilet Prep. excise', 'Service Tax', 'Countervailing Duty', 'Special Addl. Duty of Customs', 'Central surcharges & cesses']),
               ('{R:State taxes subsumed (8)}', ['State VAT / Sales Tax', 'Entertainment Tax', 'Central Sales Tax', 'Octroi & Entry Tax', 'Purchase Tax', 'Luxury Tax', 'Lottery, betting, gambling', 'State surcharges & cesses'])])
    n.flow(['{r:88th Amdt 2003}: Art. 268-A + Entry 92-C', '{r:101st Amdt 2016}: deleted'])
    n.para('After the above two amendments ({b:i.e., 80th Amendment and 101st Amendment}), the present position with respect to the distribution of tax revenues between the centre and the states is as follows:')
    n.tree(['{r:A. Art. 268}', '{r:B. Art. 269}', '{r:C. Art. 269-A}', '{r:D. Art. 270}', '{r:E. Art. 271}', '{r:F. State taxes}'], size=13)
    n.footnote('13', 'This amendment deleted Article 272 (Taxes which are levied and collected by the Centre and may be distributed between the Centre and the states).')
    out.append(('14_notes_fin_tax_revenue_80th_101st_amendments', n))

    # ---------------- 15 A–E ----------------
    n = Note('Distribution of Tax Revenues – Articles 268 to 271')
    n.subsub('A. Taxes Levied by the Centre but Collected and Appropriated by the States (Article 268):')
    n.para('This category includes the {r:stamp duties} on {b:bills of exchange, cheques, promissory notes, policies of insurance, transfer of shares} and others.')
    n.para('The proceeds of these duties levied within any state {r:do not form a part of the Consolidated Fund of India}, but are {r:assigned to that state}.')
    n.flow(['levied: {R:Centre}', 'collected: {R:State}', 'appropriated: {R:State}'])
    n.subsub('B. Taxes Levied and Collected by the Centre but Assigned to the States (Article 269):')
    n.para('The following taxes fall under this category:')
    n.items([('(i)', 'Taxes on the {r:sale or purchase of goods} ({b:other than newspapers}) in the course of {r:inter-state trade or commerce}.'),
             ('(ii)', 'Taxes on the {r:consignment of goods} in the course of {r:inter-state trade or commerce}.')])
    n.para('The net proceeds of these taxes {r:do not form a part of the Consolidated Fund of India}. They are {r:assigned to the concerned states} in accordance with the principles laid down by the {b:Parliament}.')
    n.flow(['levied: {R:Centre}', 'collected: {R:Centre}', 'assigned: {R:States}'])
    n.subsub('C. Levy and Collection of Goods and Services Tax in Course of Inter-State Trade or Commerce (Article 269-A):')
    n.para('The {r:Goods and Services Tax (GST)} on supplies in the course of {r:inter-state trade or commerce} are {r:levied and collected by the Centre}. But, this tax is {r:divided between the Centre and the States} in the manner provided by Parliament on the recommendations of the {r:GST Council}. Further, the Parliament is also authorized to formulate the principles for determining the {b:place of supply}, and when a supply of goods or services or both takes place in the course of inter-state trade or commerce.')
    n.flow(['inter-state {r:GST (IGST)}', 'levied & collected: {R:Centre}', 'divided: {R:Centre + States}', '{b:as per GST Council}'])
    n.subsub('D. Taxes Levied and Collected by the Centre but Distributed between the Centre and the States (Article 270):')
    n.para('This category includes {r:all taxes and duties referred to in the Union List} {r:except} the following:')
    n.items([('(i)', 'Duties and taxes referred to in {r:Articles 268, 269 and 269-A} (mentioned above);'),
             ('(ii)', '{r:Surcharge} on taxes and duties referred to in {r:Article 271} (mentioned below); and'),
             ('(iii)', 'Any {r:cess} levied for specific purposes.')])
    n.para('The manner of distribution of the net proceeds of these taxes and duties is prescribed by the {r:President} on the recommendation of the {r:Finance Commission}.')
    n.flow(['all Union List taxes', '{b:minus 268, 269, 269-A, surcharge, cess}', 'shared as per {R:Finance Commission}'])
    n.subsub('E. Surcharge on Certain Taxes and Duties for Purposes of the Centre (Article 271):')
    n.para('The Parliament can at any time levy the {r:surcharges} on taxes and duties referred to in {r:Articles 269 and 270} (mentioned above). The proceeds of such surcharges go to the {r:Centre exclusively}. In other words, the {b:states have no share} in these surcharges.')
    n.para('However, the {r:Goods and Services Tax (GST) is exempted} from this surcharge. In other words, this surcharge {r:can not be imposed on the GST}.')
    n.flow(['{r:Surcharge} (Art. 271)', '{R:Centre only}', '{b:not on GST}'])
    out.append(('15_notes_fin_tax_revenue_articles_268_to_271', n))

    # ---------------- 16 F + non-tax ----------------
    n = Note('State Taxes and Non-tax Revenues')
    n.subsub('F. Taxes Levied and Collected and Retained by the States:')
    n.para('These are the taxes belonging to the {r:states exclusively}. They are enumerated in the {r:state list} and are {r:18 in number}. These are¹⁴:')
    n.items([('(i)', 'land revenue;'), ('(ii)', 'taxes on agricultural income;'), ('(iii)', 'duties in respect of succession to agricultural land;'),
             ('(iv)', 'estate duty in respect of agricultural land;'), ('(v)', 'taxes on lands and buildings;'), ('(vi)', 'taxes on mineral rights;'),
             ('(vii)', 'Duties of excise on {r:alcoholic liquors for human consumption}; {r:opium, Indian hemp and other narcotic drugs and narcotics}, but {b:not including medicinal and toilet preparations containing alcohol or narcotics};'),
             ('(viii)', 'taxes on the consumption or sale or electricity;'),
             ('(ix)', 'taxes on the sale of {r:petroleum crude, high speed diesel, motor spirit (commonly known as petrol), natural gas, aviation turbine fuel and alcoholic liquor for human consumption}, but {b:not including sale in the course of inter-state trade or commerce or sale in the course of international trade or commerce of such goods};'),
             ('(x)', 'taxes on goods and passengers carried by road or inland waterways;'), ('(xi)', 'taxes on vehicles;'), ('(xii)', 'taxes on animals and boats;'),
             ('(xiii)', 'tolls;'), ('(xiv)', 'taxes on professions, trades, callings and employments;'), ('(xv)', 'capitation taxes;'),
             ('(xvi)', 'taxes on {r:entertainments and amusements} to the extent levied and collected by a {b:Panchayat or a Municipality or a Regional Council or a District Council};'),
             ('(xvii)', 'stamp duty on documents ({b:except those specified in the Union List}); and'),
             ('(xviii)', 'fees on the matters enumerated in the State List ({b:except court fees}).')])
    n.flow(['levied: {R:State}', 'collected: {R:State}', 'retained: {R:State}'])
    n.sub('3. Distribution of Non-tax Revenues')
    n.subsub('A. The Centre')
    n.listpara('The receipts from the following form the major sources of {r:non-tax revenues of the Centre}:',
               [('(i)', '{b:posts and telegraphs};'), ('(ii)', '{b:railways};'), ('(iii)', '{b:banking};'), ('(iv)', '{b:broadcasting}'), ('(v)', '{b:coinage and currency};'),
                ('(vi)', '{b:central public sector enterprises};'), ('(vii)', '{b:escheat and lapse}; and'), ('(viii)', 'others.')])
    n.subsub('B. The States')
    n.listpara('The receipts from the following form the major sources of {r:non-tax revenues of the states}:',
               [('(i)', '{b:irrigation};'), ('(ii)', '{b:forests};'), ('(iii)', '{b:fisheries};'), ('(iv)', '{b:state public sector enterprises};'), ('(v)', '{b:escheat and lapse}; and'), ('(vi)', 'others.')])
    n.compare([('{R:Centre – non-tax}', ['posts & telegraphs', 'railways', 'banking', 'broadcasting', 'coinage & currency', 'central PSEs', '{r:escheat & lapse}', 'others']),
               ('{R:States – non-tax}', ['irrigation', 'forests', 'fisheries', 'state PSEs', '{r:escheat & lapse}', 'others'])])
    n.footnote('14', 'Entry 52 (taxes on the entry of goods into a local area for consumption, use or sale therein) and entry 55 (taxes on advertisements other than advertisements published in the newspapers and advertisements broadcast by radio or television) were omitted by the 101st Amendment Act of 2016.')
    out.append(('16_notes_fin_state_taxes_non_tax_revenues', n))

    # ---------------- 17 Grants-in-aid ----------------
    n = Note('Grants-in-Aid to the States')
    n.sub('4. Grants-in-Aid to the States')
    n.para('Besides sharing of taxes between the Centre and the states, the Constitution provides for {r:grants-in-aid} to the states from the Central resources. There are {r:two types} of grants-in-aid, viz, {r:statutory grants} and {r:discretionary grants}:')
    n.tree(['{R:A. Statutory} (Art. 275)', '{R:B. Discretionary} (Art. 282)', '{R:C. Other} (temporary)'])
    n.subsub('A. Statutory Grants')
    n.para('{r:Article 275} empowers the {r:Parliament} to make grants to the states which are {r:in need of financial assistance} and {b:not to every state}. Also, {b:different sums may be fixed for different states}. These sums are {r:charged on the Consolidated Fund of India} every year.')
    n.para('Apart from this general provision, the Constitution also provides for {r:specific grants} for promoting the {b:welfare of the scheduled tribes} in a state or for raising the level of administration of the {b:scheduled areas} in a state including the State of {r:Assam}.')
    n.para('The statutory grants under Article 275 ({b:both general and specific}) are given to the states on the recommendation of the {r:Finance Commission}.')
    n.compare([('{R:General}', ['states in need', 'different sums']), ('{R:Specific}', ['welfare of STs', 'scheduled areas (incl. Assam)'])])
    n.arrow('both on recommendation of {r:Finance Commission} · charged on {b:Consolidated Fund of India}', x=340)
    n.subsub('B. Discretionary Grants')
    n.para('{r:Article 282} empowers {r:both the Centre and the states} to make any grants for any {r:public purpose}, even if it is {b:not within their respective legislative competence}. Under this provision, the Centre makes grants to the states.')
    n.quote('“These grants are also known as {r:discretionary grants}, the reason being that the Centre is {r:under no obligation} to give these grants and the matter lies within its discretion. These grants have a {r:two-fold purpose}: to help the state financially to {b:fulfil plan targets}; and to give some leverage to the Centre to {b:influence and coordinate state action} to effectuate the national plan.”¹⁵')
    n.tree(['{b:fulfil plan targets}', '{b:leverage to Centre}'])
    n.subsub('C. Other Grants')
    n.para('The Constitution also provided for a {r:third type} of grants-in-aid, but for a {r:temporary period}. Thus, a provision was made for {r:grants in lieu of export duties on jute and jute products} to the States of {b:Assam, Bihar, Orissa and west Bengal}. These grants were to be given for a period of {r:ten years} from the commencement of the Constitution. These sums were charged on the Consolidated Fund of India and were made to the states on the recommendation of the {r:Finance Commission}.')
    n.footnote('15', 'M.P. Jain: Indian Constitutional Law, Wadhwa, Fourth Edition, pp. 342–43.')
    out.append(('17_notes_fin_grants_in_aid', n))

    # ---------------- 18 GST Council, Finance Commission ----------------
    n = Note('GST Council and Finance Commission')
    n.sub('5. Goods and Services Tax Council')
    n.para('The smooth and efficient administration of the {r:goods and services tax (GST)} requires a {b:co-operation and co-ordination} between the Centre and the States. In order to facilitate this consultation process, the {r:101st Amendment Act of 2016} provided for the establishment of a {r:Goods and Services Tax Council or the GST Council}.')
    n.para('{r:Article 279-A} empowered the {r:President} to constitute a GST Council {r:by an order¹⁶}. The Council is a {r:joint forum of the Centre and the States}. It is required to make recommendations to the Centre and the States on the following matters:')
    n.items([('(a)', 'The {r:taxes, cesses and surcharges} levied by the Centre, the States and the local bodies that would get {b:merged in GST}.'),
             ('(b)', 'The {r:goods and services} that may be {b:subjected to GST or exempted from GST}.'),
             ('(c)', '{r:Model GST Laws}, principles of levy, apportionment of GST levied on supplies in the course of inter-state trade or commerce and the principles that govern the {b:place of supply}.'),
             ('(d)', 'The {r:threshold limit of turnover} below which goods and services may be exempted from GST.'),
             ('(e)', 'The {r:rates} including {b:floor rates with bands} of GST.'),
             ('(f)', 'Any {r:special rate or rates} for a specified period to raise additional resources during any {b:natural calamity or disaster}.')])
    n.flow(['{r:101st Amdt 2016}', '{R:Art. 279-A}', 'President’s order', '{R:GST Council}', '{b:joint forum}'])
    n.sub('6. Finance Commission')
    n.para('{r:Article 280} provides for a {r:Finance Commission} as a {r:quasi-judicial body}. It is constituted by the {r:President} {r:every fifth year} or even earlier. It is required to make recommendations to the President on the following matters:')
    n.bullets(['The {r:distribution of the net proceeds of taxes} to be shared between the Centre and the states, and the allocation between the states, the respective shares of such proceeds.',
               'The {r:principles which should govern the grants-in-aid} to the states by the Centre ({b:i.e., out of the Consolidated Fund of India}).',
               'The measures needed to {r:augment the Consolidated fund of a state} to supplement the resources of the {b:panchayats and the municipalities} in the state on the basis of the recommendations made by the {r:State Finance Commission}.¹⁷',
               'Any other matter referred to it by the President in the interests of {b:sound finance}.'], orig=True)
    n.para('Till {r:1960}, the Commission also suggested the amounts paid to the States of {b:Assam, Bihar, Orissa and West Bengal} in lieu of assignment of any share of the net proceeds in each year of {r:export duty on jute and jute products}.')
    n.para('The Constitution envisages the Finance Commission as the {R:balancing wheel of fiscal federalism} in India.')
    n.flow(['{R:Finance Commission}', '{r:balancing wheel of fiscal federalism}'])
    n.footnote('16', 'Article 279-A(1) says that the President shall, within sixty days from the commencement of the Constitution (One Hundred and First Amendment) Act, 2016, by order, constitute a Council to be called the Goods and Services Tax Council.')
    n.footnote('17', 'This function was added by the 73rd and 74th Amendment Acts of 1992 which have granted constitutional status on the panchayats and the municipalities respectively.')
    out.append(('18_notes_fin_gst_council_finance_commission', n))

    # ---------------- 19 Protection of states, borrowing ----------------
    n = Note('Protection of States’ Interest and Borrowing')
    n.sub('7. Protection of the States’ Interest')
    n.para('To protect the interest of states in the financial matters, the Constitution lays down that the following bills can be introduced in the Parliament only on the {r:recommendation of the President}:')
    n.bullets(['A bill which {r:imposes or varies any tax or duty} in which {b:states are interested};',
               'A bill which varies the meaning of the expression ‘{r:agricultural income}’ as defined for the purposes of the enactments relating to Indian income tax;',
               'A bill which affects the {r:principles on which moneys are or may be distributable to states}; and',
               'A bill which imposes any {r:surcharge} on any specified tax or duty for the purpose of the Centre.'], orig=True)
    n.arrow('all 4 bills → only with {r:President’s recommendation}')
    n.para('The expression “{r:tax or duty in which states are interested}” means: (a) a tax or duty the whole or part of the net proceeds whereof are {b:assigned to any state}; or (b) a tax or duty by reference to the net proceeds whereof sums are for the time being {b:payable, out of the Consolidated Fund of India to any state}.')
    n.para('The phrase ‘{r:net proceeds}’ means the {r:proceeds of a tax or a duty minus the cost of collection}. The net proceeds of a tax or a duty in any area is to be ascertained and certified by the {r:Comptroller and Auditor-General of India}. His/her certificate is {r:final}.')
    n.flow(['proceeds of tax', '{b:minus cost of collection}', '{R:net proceeds}', 'certified by {r:CAG} (final)'])
    n.sub('8. Borrowing by the Centre and the States')
    n.para('The Constitution makes the following provisions with regard to the {r:borrowing powers} of the Centre and the states:')
    n.bullets(['The {r:Central government} can borrow {r:either within India or outside} upon the security of the {b:Consolidated Fund of India} or can give guarantees, but both within the limits fixed by the {r:Parliament}. So far, {b:no such law has been enacted} by the Parliament.',
               'Similarly, a {r:state government} can borrow {r:within India (and not abroad)} upon the security of the {b:Consolidated Fund of the State} or can give guarantees, but both within the limits fixed by the {r:legislature of that state}.',
               'The Central government can {r:make loans to any state} or give guarantees in respect of loans raised by any state. Any sums required for the purpose of making such loans are to be {b:charged on the Consolidated Fund of India}.',
               'A state {r:cannot raise any loan without the consent of the Centre}, if there is still {b:outstanding any part of a loan} made to the state by the Centre or in respect of which a guarantee has been given by the Centre.'], orig=True)
    n.compare([('{R:Centre}', ['India {r:+ abroad}', 'security: CFI', 'limits: Parliament (no law yet)']), ('{R:State}', ['{r:only within India}', 'security: CF of State', 'limits: state legislature', '{b:Centre’s consent if loan outstanding}'])])
    out.append(('19_notes_fin_protection_of_states_borrowing', n))

    # ---------------- 20 Tax immunities, emergencies ----------------
    n = Note('Inter-Governmental Tax Immunities and Emergencies')
    n.sub('9. Inter-Governmental Tax Immunities')
    n.para('Like any other federal Constitution, the Indian Constitution also contain the rule of ‘{r:immunity from mutual taxation}’ and makes the following provisions in this regard:')
    n.subsub('A. Exemption of Central Property from State Taxation')
    n.para('The {r:property of Centre} is {r:exempted from all taxes imposed by a state} or any authority within a state like {b:municipalities, district boards, panchayats} and so on. But, the {r:Parliament is empowered to remove this ban}. The word ‘{r:property}’ includes {b:lands, buildings, chattels, shares, debts, everything that has a money value}, and every kind of property—{b:movable or immovable and tangible or intangible}. Further, the property may be used for {b:sovereign (like armed forces) or commercial purposes}.')
    n.para('The {r:corporations or the companies} created by the Central government are {r:not immune} from state taxation or local taxation. The reason is that a corporation or a company is a {b:separate legal entity}.')
    n.subsub('B. Exemption of State Property or Income from Central Taxation')
    n.para('The {r:property and income of a state} is {r:exempted from Central taxation}. Such income may be derived from {b:sovereign functions or commercial functions}. But the {r:Centre can tax the commercial operations} of a state if {b:Parliament so provides}. However, the Parliament can declare any particular trade or business as {b:incidental to the ordinary functions of the government} and it would then {r:not be taxable}.')
    n.para('Notably, the property and income of {r:local authorities} situated within a state are {r:not exempted} from the Central taxation. Similarly, the property or income of {r:corporations and companies owned by a state} can be taxed by the Centre.')
    n.para('The {r:Supreme Court}, in an {r:advisory opinion¹⁸ (1963)}, held that the immunity granted to a state in respect of Central taxation {r:does not extend to the duties of customs or duties of excise}. In other words, the Centre can impose {b:customs duty on goods imported or exported by a state}, or an {b:excise duty on goods produced or manufactured by a state}.')
    n.compare([('{R:Central property}', ['✔ exempt from state taxes', '{b:Parliament can remove ban}', '✘ Central corporations / companies']),
               ('{R:State property / income}', ['✔ exempt from Central taxes', '✘ commercial ops (if Parliament provides)', '✘ local authorities, state companies', '✘ customs & excise (1963)'])])
    n.sub('10. Effects of Emergencies')
    n.para('The Centre–state financial relations in normal times (described above) undergo changes during {r:emergencies}. These are as follows:')
    n.subsub('A. National Emergency')
    n.para('While the proclamation of {r:national emergency} (under {r:Article 352}) is in operation, the {r:President can modify the constitutional distribution of revenues} between the Centre and the states. This means that the President can either {r:reduce or cancel the transfer of finances} ({b:both tax sharing and grants-in-aid}) from the Centre to the states. Such modification continues {r:till the end of the financial year} in which the emergency ceases to operate.')
    n.subsub('B. Financial Emergency')
    n.listpara('While the proclamation of {r:financial emergency} (under {r:Article 360}) is in operation, the Centre can give directions to the states:',
               [('(i)', 'to observe the specified {b:canons of financial propriety};'), ('(ii)', 'to {b:reduce the salaries and allowances} of all class of persons serving in the state; and'),
                ('(iii)', 'to {b:reserve all money bills and other financial bills} for the consideration of the President.')])
    n.boxes([['{R:Art. 352}', 'reduce / cancel transfers', '{b:till end of financial year}'], ['{R:Art. 360}', 'financial propriety · salary cut', '{b:reserve money bills}']])
    n.footnote('18', 'In Re. Sea Customs Act (1963).')
    out.append(('20_notes_fin_tax_immunities_emergencies', n))
    return out
