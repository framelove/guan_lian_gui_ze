# import pandas as pd
# data = pd.ExcelFile('data/data1.xlsx').parse('Sheet2')
# data1 =data.dropna()
# jine = pd.ExcelFile('data/data2.xlsx').parse('Sheet1')
#
# data2 = data1.pivot_table(index='客户编号',columns='categories',values = '一年内消费次数',aggfunc=sum)
# data2 = data2.fillna(0)
#
# data3 = data1[['客户编号','客户名称','客户等级']]
# data3 = data3.drop_duplicates(['客户编号','客户等级'])
# data4 = pd.merge(data2,data3,left_on=data2.index,right_on='客户编号')
# data5 = pd.merge(data4,jine)
# files = pd.ExcelWriter('shuchu.xlsx')
# data5.to_excel(files)
# files.save()
################################################### #########################
# df1 = pd.ExcelFile('汇总数据.xlsx').parse('Sheet1')
# df2 = pd.ExcelFile('data_didian.xlsx').parse('Sheet1')
# df3 = pd.merge(df1,df2,how='left')
# files = pd.ExcelWriter('数据汇总2.0.xlsx')
# df3.to_excel(files)
# files.save()

#######################################################################
# import re
# chengshi = ['北京','东莞','佛山','广州','杭州','深圳','武汉','中山','珠海']
#
# df1 = pd.ExcelFile('城市数据汇总.xlsx').parse('Sheet1')
# files = pd.ExcelWriter('城市.xlsx')
# for i in range(len(chengshi)):
#     a = chengshi[i]
#
#     df2 = pd.ExcelFile('城市数据推荐.xlsx').parse('Sheet{}'.format(i+1))
#
#     a2 = []
#     for i in df2['推荐套餐']:
#         a2.append(re.sub('frozenset', '套餐', i))
#     df2['推荐套餐']=a2
#     df3 = pd.merge(df1,df2,how='inner')
#     print(a)
#     df3.to_excel(files,sheet_name=a)
# files.save()
######################################################################################
import pandas as pd
data1 = pd.ExcelFile('data/全国数据（处理前）.xlsx').parse('Sheet2')
data2 = pd.ExcelFile('data/用户信息.xlsx').parse('Sheet1')
df = pd.merge(data1,data2,how='inner')
files = pd.ExcelWriter('a.xlsx')
df.to_excel(files)
files.save()
