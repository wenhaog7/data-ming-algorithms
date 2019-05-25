import sys
data = []
label = {}
for line in sys.stdin:
    if '\n' in line:
        a = line[:-1].strip().split(' ')
        data.append(a)
#all samples from data
num_c = int(data[0][1])
num_p = int(data[0][0])
sample = data[1:(num_p + 1)]
# #distance list
dic = []
dimen = len(sample[0])
for i in range(len(sample)):
    label[i] = []
    label[i].append(i)
    for j in range(i+1, len(sample)):
        coor = (i, j)
        dis = 0
        for m in range(dimen):
            temp = pow((float(sample[i][m]) - float(sample[j][m])), 2)
            dis += temp
        dic.append([coor, dis])
dist = sorted(dic,key=lambda x: (-x[1], -x[0][0], -x[0][1]))
#main function
def minpair(pair, label):
    for key, value in label.items():
        if value == pair[0]:
            a = key
        elif value == pair[1]:
            b = key
    return min(a, b)

def maxpair(pair, label):
    for key, value in label.items():
        if value == pair[0]:
            a = key
        elif value == pair[1]:
            b = key
    return max(a, b)
while len(label.keys()) > num_c:
    # a = min(dic, key=dic.get)
    if dist[-1][1] == dist[-2][1]:
        res = []
        for key, value in dic.items():
            if value == min(dic.values()):
                res.append(key)
        dic_min = {}
        
        for pair in res:
            dic_min[pair] = minpair(pair, label)
            
        if len(dic_min) == len(set(dic_min.values())):
            a = min(dic_min, key = dic_min.get)
        else:
            new_res = []
            dic_max = {}
            for key, value in dic_min.items():
                if value == min(dic_min.values()):
                    new_res.append(key)
            for pair in new_res:
                dic_max[pair] = maxpair(pair, label)
            a = min(dic_max, key = dic_max.get)
    else:
        a = dist.pop()
    x = y = 0
    for key in label.keys():
        if a[0][0] in label[key]:
            x = key
        if a[0][1] in label[key]:
            y = key
    if min(label[x]) < min(label[y]):
        label[x].extend(label[y])
        label[x].sort()
        del label[y]
    elif min(label[y]) < min(label[x]):
        label[y].extend(label[x])
        label[y].sort()
        del label[x]
# new_dict = {v:k for k,v in label.items()}

for i in range(len(sample)):
    for j in label.keys():
        if i in label[j]:
            print(j)
