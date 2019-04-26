#closed pattern
clo_p = {}
for key in Lk_sup2:
    support = Lk_sup2[key]
    a = set(key.split(' '))
    if support not in clo_p:
        clo_p[support] = [a]
    else:
        cnt = 0
        minus = []
        q = clo_p[support]
        for w in q:
            if w >= a:
                cnt += 1
                break
            if w < a:
                minus.append(w)
        if len(minus) > 0:
            for attr in minus:
                q.remove(attr)
        if cnt == 0:
            q.append(a)
clo2 = {}
for x in clo_p:
    for y in clo_p[x]:
        q = list(y)
        q.sort()
        stt = ' '.join(q)
        clo2[stt] = x

#max pattern
max_p = []
for item in clo2:
    max_p.append(item)
ll = set()
for i in max_p:
    for j in max_p:
        if set(i.split(' ')) > set(j.split(' ')):
            ll.add(j)

for item in ll:
    max_p.remove(item)

#print result3
print()
dic_maxp ={}
for item in max_p:
    dic_maxp[item] = Lk_sup2[item]
dic_maxp = sorted(dic_maxp.items(), key=lambda kv: (-kv[1], kv[0]))
for i in range(len(dic_maxp)):
    s = str(dic_maxp[i][1]) + ' [' +dic_maxp[i][0] + ']'
    print(s)
