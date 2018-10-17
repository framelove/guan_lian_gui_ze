import pandas as pd
import re
data = pd.ExcelFile('数据汇总2.0.xlsx').parse('Sheet2')
print(data.columns)
a1 = []
for i in data['已选套餐']:
    a1.append(re.sub('frozenset','套餐',i))
data['已选套餐'] = a1
a2 = []
for i in data['已消费推荐套餐']:
    a2.append(re.sub('frozenset', '套餐', i))
data['已消费推荐套餐']=a2
a3 = []

for i in data['未消费推荐套餐']:
    a3.append(re.sub('frozenset', '套餐', i))
data['未消费推荐套餐']=a3
files = pd.ExcelWriter('数据汇总3.0.xlsx')
data.to_excel(files)
files.save()

