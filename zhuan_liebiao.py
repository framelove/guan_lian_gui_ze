import pandas as pd
import numpy as np
# 数据格式的转换 ==>列表
data = pd.ExcelFile('data_zhuanhua.xlsx').parse('Sheet1')
data = data.drop(['客户编号'],axis=1)
data1 = np.array(data)

listdata = data1.tolist()
aa = []
for i in listdata:
    a=[]
    x =1
    for j in i:
        if j != 0:
            a.append(x)
        x+=1
    aa.append(a)


