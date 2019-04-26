#judge function
def judge(a, b, i):
    if (i + len(a)) <= len(b):
        c = b[i:i+len(a)]
        for j in range(len(a)):
            if c[j] != a[j]:
                return False
        return True
    return False
#calcaulate support and filter
def scanD(D, dic, Ck):
    Lk = []
    ssCnt = {}
    sup_Cnt = {}
    for line in D:
        for item in Ck:
            if item in line:
                a = item.split(' ')
                b = line.split(' ')
                for i in range(len(b)):
                    if b[i] == a[0]:
                        if judge(a, b, i):
                            if item in ssCnt:
                                ssCnt[item] += 1
                            else:
                                ssCnt[item] = 1
    for key in ssCnt:
        if ssCnt[key] >= min_sup:
            Lk.insert(0, key)
            sup_Cnt[key] = ssCnt[key]
    return Lk, sup_Cnt
            
#generage cadidate
def gen_can(dic, dic2, L1, Lk, k):
    Ck = []
    for i in range(len(Lk)):
            listi = Lk[i].split(' ')
            newlist = []
            last_word = listi[k - 1]
            for value in dic2[last_word]:
                a = value[0]
                b = value[1]
                try:
                    if dic[a, b + 1] in sup_f2.keys():
                        newlist.extend(listi)
                        newlist.append(dic[a, b + 1])
                        if len(newlist) == k + 1 and len(newlist) <= 5:
                            Ck.append(' '.join(newlist))
                except:
                    IndexError
    return Ck

#main function 
Lk_sup = {}
L = [L1]
k = 1
while len(L[k - 1]) > 0:
    Ck = gen_can(dic, dic2, L1, L[k - 1], k)
    Lk, k_sup = scanD(dataset, dic, Ck)
    Lk_sup.update(k_sup)
    L.append(Lk)
    k += 1
