
#scan once-> L1: frequent 1-item set
for num in range(0, len(dataset)):
    for attr in dataset[num]:
        if attr in Lk_sup.keys():
            Lk_sup[attr] += 1
        else:
            Lk_sup[attr] = 1
for key, value in Lk_sup.items():
    if value >= min_sup:
        L1.insert(0, key)
        Lk_sup2[key] = value

#calculate support and filter
def scanD(D, Ck, min_sup):
    Lk = []
    ssCnt = {}
    sup_Cnt = {}
    for tid in D:
        for item in Ck:
            ss = item.split(' ')
            item2 = set()
            for str in ss:
                item2.add(str)
            if item2.issubset(tid):
                item2 = list(item2)
                item2.sort()
                newkey = ' '.join(item2)
                if newkey not in ssCnt:
                    ssCnt[newkey] = 1
                else:
                    ssCnt[newkey] += 1
    for key in ssCnt:
        if ssCnt[key] >= min_sup:
            Lk.insert(0, key)
            sup_Cnt[key] = ssCnt[key]
    return Lk, sup_Cnt
#generate candidate
def can_gen(Lk, k):
    Ck = set()
    for i in range(len(Lk)):
        for j in range(len(Lk)):
            listi = Lk[i].split(' ')
            listj = Lk[j].split(' ')
            listi.sort()
            listj.sort()
            newlist = []
            if(listi[k - 1] == listj[k - 1]):
                continue
            for m in range(k - 1):
                if listi[m] != listj[m]:
                    break
                newlist.append(listi[m])
            newlist.append(listi[k - 1])
            newlist.append(listj[k - 1])
            newlist.sort()
            if (len(newlist) > k):
                Ck.add(' '.join(newlist))      
    #join
    return Ck

#main fuction:
L1.sort()
L = [L1]
k = 1
while len(L[k - 1])>0:
    Ck = can_gen(L[k - 1], k)
    Lk, k_sup = scanD(dataset, Ck, min_sup)
    Lk.sort()
    Lk_sup2.update(k_sup)
    L.append(Lk)
    k += 1
