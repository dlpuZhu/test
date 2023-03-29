long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""
import re
lists = re.split('\d+\. ',long_text)
name_lei = lists[0].strip().split('\n')
dicts = {'name':name_lei[0],'lei':name_lei[1]}
lists_total = []
for i in lists[1:]:
    lists1 = i.strip().split('\n')
    dicts1 = {'title':lists1[0],'isin':lists1[1:]}
    lists_total.append(dicts1)
dicts['sub_fund'] = lists_total
print(dicts)    