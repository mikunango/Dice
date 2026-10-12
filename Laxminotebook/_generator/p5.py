from nb import Note

T1 = [('245.', 'Extent of laws made by Parliament and by the legislatures of states'),
      ('246.', 'Subject-matter of laws made by Parliament and by the legislatures of states'),
      ('246A.', 'Special provision with respect to goods and services tax'),
      ('247.', 'Power of Parliament to provide for the establishment of certain additional courts'),
      ('248.', 'Residuary powers of legislation'),
      ('249.', 'Power of Parliament to legislate with respect to a matter in the state list in the national interest'),
      ('250.', 'Power of Parliament to legislate with respect to any matter in the state list if a Proclamation of Emergency is in operation'),
      ('251.', 'Inconsistency between laws made by Parliament under articles 249 and 250 and laws made by the legislatures of states'),
      ('252.', 'Power of Parliament to legislate for two or more states by consent and adoption of such legislation by any other state'),
      ('253.', 'Legislation for giving effect to international agreements'),
      ('254.', 'Inconsistency between laws made by Parliament and laws made by the legislatures of states'),
      ('255.', 'Requirements as to recommendations and previous sanctions to be regarded as matters of procedure only')]
T2 = [('256.', 'Obligation of states and the Union'),
      ('257.', 'Control of the Union over states in certain cases'),
      ('257A.', 'Assistance to states by deployment of armed forces or other forces of the Union (Repealed)'),
      ('258.', 'Power of the Union to confer powers, etc., on states in certain cases'),
      ('258A.', 'Power of the states to entrust functions to the Union'),
      ('259.', 'Armed Forces in states in Part B of the First Schedule (Repealed)'),
      ('260.', 'Jurisdiction of the Union in relation to territories outside India'),
      ('261.', 'Public acts, records and judicial proceedings'),
      ('262.', 'Adjudication of disputes relating to waters of inter-state rivers or river valleys'),
      ('263.', 'Provisions with respect to an inter-state Council')]
T3 = [('#', 'Distribution of Revenues between the Union and the States'),
      ('268.', 'Duties levied by the Union but collected and appropriated by the states'),
      ('268A.', 'Service tax levied by the Union and collected and appropriated by the Union and the states (Repealed)'),
      ('269.', 'Taxes levied and collected by the Union but assigned to the states'),
      ('269A.', 'Levy and collection of goods and services tax in course of inter-state trade or commerce'),
      ('270.', 'Taxes levied and distributed between the Union and the states'),
      ('271.', 'Surcharge on certain duties and taxes for purposes of the Union'),
      ('272.', 'Taxes which are levied and collected by the Union and may be distributed between the Union and the states (Repealed)'),
      ('273.', 'Grants in lieu of export duty on jute and jute products'),
      ('274.', 'Prior recommendation of the President required to bills affecting taxation in which states are interested'),
      ('275.', 'Grants from the Union to certain states'),
      ('276.', 'Taxes on professions, trades, callings and employments'),
      ('277.', 'Savings'),
      ('278.', 'Agreement with states in Part B of the First Schedule with regard to certain financial matters (Repealed)'),
      ('279.', 'Calculation of “net proceeds”, etc.'),
      ('279A.', 'Goods and Services Tax Council'),
      ('280.', 'Finance Commission'),
      ('281.', 'Recommendations of the Finance Commission'),
      ('#', 'Miscellaneous Financial Provisions'),
      ('282.', 'Expenditure defrayable by the Union or a state out of its revenues'),
      ('283.', 'Custody, etc., of Consolidated Funds, Contingency Funds and moneys credited to the public accounts'),
      ('284.', 'Custody of suitors’ deposits and other moneys received by public servants and courts'),
      ('285.', 'Exemption of property of the Union from state taxation'),
      ('286.', 'Restrictions as to imposition of tax on the sale or purchase of goods'),
      ('287.', 'Exemption from taxes on electricity'),
      ('288.', 'Exemption from taxation by states in respect of water or electricity in certain cases'),
      ('289.', 'Exemption of property and income of a state from Union taxation'),
      ('290.', 'Adjustment in respect of certain expenses and pensions'),
      ('290A.', 'Annual payment to certain Devaswom Funds'),
      ('291.', 'Privy purse sums of Rulers (Repealed)'),
      ('#', 'Borrowing'),
      ('292.', 'Borrowing by the Government of India'),
      ('293.', 'Borrowing by States')]

def fmt(t):
    if '(Repealed)' in t:
        return t.replace('(Repealed)', '{b:(Repealed)}')
    return t

def rows(T):
    out, groups = [], []
    for a, s in T:
        if a == '#':
            groups.append(len(out)); out.append([s, ''])
        else:
            out.append(['{r:' + a + '}', fmt(s)])
    return out, groups

def notes():
    out = []
    n = Note('Articles at a Glance – Legislative and Administrative')
    r, g = rows(T1)
    n.table(['{R:Article No.}', '{R:Subject Matter}'], r, [110, 490], caption='Table 15.1 Articles Related to Centre-State Legislative Relations at a Glance', group_rows=g)
    n.gap(10)
    r, g = rows(T2)
    n.table(['{R:Article No.}', '{R:Subject Matter}'], r, [110, 490], caption='Table 15.2 Articles Related to Centre-State Administrative Relations at a Glance', group_rows=g)
    out.append(('29_notes_tables_15_1_15_2_articles', n))

    n = Note('Articles at a Glance – Financial Relations')
    r, g = rows(T3)
    n.table(['{R:Article No.}', '{R:Subject Matter}'], r, [110, 490], caption='Table 15.3 Articles Related to Centre-State Financial Relations at a Glance', group_rows=g)
    out.append(('30_notes_table_15_3_financial_articles', n))
    return out
