# Keyword bulletpoints joined at the start of each line (per note, in order).
LABELS = {
'CHAPTER 15 Centre–State Relations': [
    'Federal division of powers', 'No judicial division', 'Harmony needed', 'Elaborate provisions', 'Three heads',
    'Arts. 245–255, Part XI', 'Other articles', 'Territory & subjects', 'Five situations + control', 'Four aspects'],
'Territorial Extent of Central and State Legislation': [
    'Territorial limits', 'Territory of India', 'Sufficient nexus', 'Extra-territorial reach',
    'Restrictions on Parliament', 'Laws not applicable', 'Puducherry', 'Force of regulation', 'Repeal/amend power',
    'President – NE tribal areas'],
'Distribution of Legislative Subjects': [
    'Seventh Schedule – 3 lists', 'Union List 98', 'State List 59', 'Concurrent List 52', '42nd Amendment 1976',
    'UTs / acquired territories', 'GST – both', 'Inter-state GST – Parliament', 'Residuary taxes'],
'Scheme of Lists and Predominance': [
    'Union List logic', 'State List logic', 'Concurrent List logic', 'Diversity + uniformity',
    'US model', 'Australia', 'Canada', 'GoI Act 1935', 'One difference', 'Canadian precedent',
    'Predominance', 'Union > State', 'Union > Concurrent', 'Concurrent > State',
    'Central law prevails', 'Exception', 'President’s assent', 'Parliament can override'],
'Parliamentary Legislation in the State Field – I': [
    'Normal times', 'Abnormal times', 'Five circumstances',
    'RS resolution – national interest', '2/3 majority', '1 year validity', '6 months after',
    'State power intact', 'Parliament prevails',
    'Emergency power', '6 months after emergency', 'State power intact', 'Parliament prevails'],
'Parliamentary Legislation in the State Field – II': [
    'Two or more states', 'Only those states', 'Others may adopt', 'Amend only by Parliament',
    'Parliament gains', 'State loses', 'Abdication / surrender', 'Examples (C)',
    'International treaties', 'International obligations', 'Examples (D)',
    'President’s Rule', 'Operative after PR', 'Not coterminous', 'State can repeal'],
'Centre’s Control Over State Legislation': [
    'Four ways of control', 'Absolute veto', 'Centre superior', 'Sarkaria view',
    'Federal supremacy', 'Deleterious results', 'Legal chaos', 'Policy stymied', 'Unity in diversity', 'Indispensable rule'],
'Administrative Relations – I': [
    'Arts. 256–263, Part XI', 'Other articles', 'Executive follows legislative', 'Centre – whole of India',
    'State executive power', 'Concurrent – states execute', 'Executed by states',
    'Two restrictions', 'Comply & not impede', 'General vs specific',
    'Centre’s directions', 'Coercive sanction', 'Article 365', 'President’s Rule – Art. 356',
    'Four more directions', 'Art. 365 applies'],
'Administrative Relations – II': [
    'Rigid legislative division', 'No legislative delegation', 'Executive follows legislative', 'Possible conflicts',
    'Executive delegation', 'President → State', 'Governor → Centre', 'Conditional / unconditional',
    'Without state consent', 'By Parliament only', 'Union List law', 'Not by state legislature',
    'Agreement or legislation', 'Centre both, state one',
    'Cooperation provisions', 'ISC set up 1990', 'No authority yet'],
'All-India Services': [
    'Central & State Services', 'AIS – IAS, IPS, IFoS', 'Key posts by turns', 'Recruited by Centre',
    'Joint control', 'Ultimate vs immediate', '1947 – IAS & IPS', '1966 – IFoS', 'Art. 312 – new AIS',
    'Single service', 'Grounds of support', 'Ambedkar’s view',
    'Dual polity, dual service', 'Federal & State service', 'One exception', 'Strategic posts', 'Calibre of servants', 'All-India service'],
'Administrative Relations – III': [
    'PSC relations', 'JSPSC appointment',
    'No dual justice', 'Integrated judiciary', 'Single court system', 'Uniform remedy',
    'HC judges appointed', 'Transfer & removal', 'Common high court', 'Examples',
    'Complete control'],
'Administrative Relations – IV': [
    'Other control provisions', 'Pleasure of President', 'Agent of Centre', 'Periodical reports',
    'Extra-constitutional devices', 'Bodies & conferences', 'Advisory bodies', 'Conferences'],
'Financial Relations – Allocation of Taxing Powers': [
    'Arts. 268–293, Part XII', 'Other provisions', 'Heads',
    'Taxing powers divided', 'Levy vs appropriate', 'Income tax example',
    'Restrictions on states', '₹2,500 cap', 'Parliament fixes principles', 'Electricity exemption', 'President’s assent'],
'Distribution of Tax Revenues – 80th and 101st Amendments': [
    'Two amendments', '80th Amdt – 10th FC', '29% to states', 'Alternative Scheme', 'Corporation tax & customs',
    '101st Amdt – GST', 'Concurrent taxing power', 'GST purpose',
    'Central taxes subsumed', 'State taxes subsumed',
    'Art. 268-A deleted', '88th Amdt 2003', 'Service tax',
    'Present position'],
'Distribution of Tax Revenues – Articles 268 to 271': [
    'Stamp duties', 'Not in CFI',
    'Art. 269 taxes', 'Not in CFI', 'Assigned to states',
    'IGST levied by Centre', 'Shared via GST Council', 'Place of supply',
    'Art. 270 – all Union taxes', 'Finance Commission formula',
    'Art. 271 surcharge', 'Centre exclusively', 'No state share', 'GST exempted', 'No surcharge on GST'],
'State Taxes and Non-tax Revenues': [
    'States exclusively', '18 in number', 'List of 18',
    'Centre’s non-tax', 'States’ non-tax'],
'Grants-in-Aid to the States': [
    'Grants-in-aid', 'Two types',
    'Art. 275 – needy states', 'Different sums', 'Charged on CFI', 'Specific grants', 'On FC recommendation',
    'Art. 282 – any public purpose', 'Centre to states',
    'Discretionary – no obligation', 'Two-fold purpose',
    'Third type – temporary', 'Jute export grants', 'Ten years', 'Charged on CFI'],
'GST Council and Finance Commission': [
    'Need for co-ordination', '101st Amdt 2016', 'Art. 279-A', 'Joint forum', 'Recommendations on',
    'Art. 280 – quasi-judicial', 'Every 5 years', 'Recommends to President',
    'Till 1960 – jute', 'Balancing wheel'],
'Protection of States’ Interest and Borrowing': [
    'President’s recommendation', 'States interested – meaning',
    'Net proceeds', 'CAG certifies', 'Final certificate',
    'Borrowing powers'],
'Inter-Governmental Tax Immunities and Emergencies': [
    'Immunity from mutual taxation',
    'Central property exempt', 'Parliament can remove', 'Property – meaning', 'Sovereign or commercial',
    'Central PSUs not immune', 'Separate legal entity',
    'State property exempt', 'Sovereign or commercial', 'Commercial ops taxable', 'Incidental – not taxable',
    'Local authorities', 'State companies', 'Advisory opinion 1963', 'Customs & excise',
    'Changes in emergency', 'Two effects',
    'Art. 352 – modify revenues', 'Reduce or cancel', 'Till end of FY',
    'Art. 360 – directions'],
'Trends in Centre–State Relations': [
    'Till 1967 smooth', '1967 – nine states', 'New era', 'Opposed centralisation', 'State autonomy', 'Tensions',
    'Tension areas', 'Since mid 1960s', 'Developments'],
'Administrative Reforms Commission and Rajamannar Committee': [
    'ARC 1966', 'Terms of reference', 'Setalvad study team', 'Report 1969', '22 recommendations', 'Key recommendations',
    'No action',
    'Rajamannar 1969 (TN)', 'Report 1971', 'Unitary trends', 'Reasons', 'Recommendations', 'Completely ignored'],
'Anandpur Sahib Resolution and West Bengal Memorandum': [
    'Akali Dal 1973', 'Centre only 4 subjects', 'Truly federal',
    'West Bengal 1977', 'Suggestions', 'Not accepted'],
'Sarkaria Commission': [
    'Sarkaria 1983', 'Mandate', 'Report 1988',
    'No structural change', 'Functional changes', 'Co-operative action', 'Strong Centre', 'Not centralisation', 'BP & anaemia',
    '247 recommendations', 'Important ones', 'Consult states',
    '180 implemented', 'ISC 1990'],
'Punchhi Commission – I': [
    'Punchhi 2007', 'Sea-changes', 'Report 2010', '1,456 pages', 'Differed from Sarkaria',
    'Cooperative federalism', 'Practical guide', '310+ recommendations', 'Important ones',
    'Flexibility to states', 'Not absolute'],
'Punchhi Commission – II (Governors)': [
    'Limited discretion', 'Reasoned choice', 'Guidelines', 'Constitutional role only'],
'Punchhi Commission – III (Emergency and Coordination)': [
    'Removes misgivings', 'Localised emergency', 'Constitutional basis',
    'Common secretariat', 'Institutionalise models', 'CM forum',
    'RS potential', 'Equal seats', 'Amend existing laws', 'Compensation'],
'Punchhi Commission – IV (Finance and Planning)': [
    'Refer to FC / experts', 'States in ToR', 'Synchronise periods', 'Coordination role',
    'Final & binding', 'Appeal to SC',
    'ISC Standing Committee', 'Circulated to states'],
}
