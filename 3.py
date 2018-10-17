
def generateRules(L, supportData, minConf=0.7):
    bigRuleList = []  # 规则存放在bigRuleList列表中
    for i in range(1, len(L)):
        for freqSet in L[i]:  # L0是频繁1项集，没关联规则
            H1 = [frozenset([item]) for item in freqSet]  # H1存放频繁i项集的某个频繁项集的单个元素集合，频繁3项集的{0,1,2}的{{0},{1},{2}
            if i > 1:
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)  # 从频繁3项集开始，从置信度算出关联规则
            else:
                calcConf(freqSet, H1, supportData, bigRuleList, minConf)  # 对频繁2项集，计算置信度
    return bigRuleList


def calcConf(freqSet, H, supportData, br1, minConf=0.7):  # 计算置信度函数，
    prunedH = []
    for conseq in H:
        conf = supportData[freqSet] / supportData[freqSet - conseq]  # conf({2}) = s({{0},{1},{2}})/s({{0},{1},{2}}-{2})
        if conf >= minConf:
            print(freqSet - conseq, "——>", conseq, "conf:", conf)  # 那么有{{0},{1}}——>{{2}}
            br1.append((freqSet - conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH


def rulesFromConseq(freqSet, H, supportData, br1, minConf=0.7):
    m = len(H[0])  # m,频繁m项集
    if (len(freqSet)) > (m + 1):
        Hmp1 = aprioriGen(H, m + 1)  # 由H，创建m+1项集
        Hmp1 = calcConf(freqSet, Hmp1, supportData, br1, minConf)  # 保留符合置信度的m+1项集，Hmp1 = prunedH
        if (len(Hmp1) > 1):
            rulesFromConseq(freqSet, Hmp1, supportData, br1, minConf)


L, suppData = apriori(dataSet, minSupport=0.5)
rules = generateRules(L, suppData, minConf=0.7)
print(rules)

rules = generateRules(L, suppData, minConf=0.5)
print(rules)


