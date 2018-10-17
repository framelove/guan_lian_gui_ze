import pandas as pd
import numpy as np
data = pd.ExcelFile('data/武汉.xlsx').parse('Sheet2')
jiage = [12800,18800,29900,29800,33800,13800]
#data = data.drop(['客户编号'],axis=1)
data1 = data[['C1','C2','C3','C4','C5','C6']]
data2 = np.array(data1)
listdata = data2.tolist()
def lishituijian(lists,yue):
    a = lists
    x = max(a)
    list1 = []
    list2 = []
    for i, j in enumerate(a):
        if j == x:
            list1.append(i + 1)
            a[i] = 0
    return list1,a
qq = []
for i in listdata:
    q = []
    jieguo1 = set(lishituijian(i)[0])
    q.append(jieguo1)
    jieguo2 = set(lishituijian(lishituijian(i)[1])[0])
    q.append(jieguo2)
    qq.append(q)
print(qq)
