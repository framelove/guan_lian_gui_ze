import pandas as pd
import numpy as np
data = pd.ExcelFile('data/深圳.xlsx').parse('Sheet2')
jiage = [12800,18800,29900,29800,33800,13800]

data1 = data[['C1','C2','C3','C4','C5','C6']]
data2 = np.array(data1)
data3 = data['卡内余额']
yue = np.array(data3)
yue1 = yue.tolist()
listdata = data2.tolist()
def lishituijian(lists,yue):
    a = lists
    x = max(a)
    list1 = []
    list2 = []
    list3 = []
    # 选出最大值的索引+1，并把最大值赋值为0.
    for i, j in enumerate(a):
        if j == max(a):
            list1.append(i + 1)
            a[i] = 0
            break
    # 选出最大值的索引+1，多个最大值的按余额来选择
    for i ,j in enumerate(a):
        if max(a) == 0:
            list2.append(0)
            break
        elif j == max(a):
            list2.append(i+1)
    if len(list2) == 1:
        list1.append(list2[0])
    else:
        for i in list2:
            x = abs(jiage[i-1]-yue)
            list3.append(x)
        list1.append(list2[list3.index(min(list3))])
    return list1
qq = []
for i,j in enumerate(listdata):

    jieguo1 = lishituijian(j,yue1[i])
    qq.append(jieguo1)

files = pd.ExcelWriter('深圳.xlsx')
df = np.array(qq)
df1 = pd.DataFrame(df)
df1.to_excel(files)
files.save()
