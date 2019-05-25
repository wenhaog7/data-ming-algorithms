import sys
import copy
#import data
dataset = []
for line in sys.stdin:
    if "\n" in line:
        dataset.append(line[:-1])
    else:
        dataset.append(line)

N = int(dataset[0].split(" ")[0])
k = int(dataset[0].split(" ")[1])
tail = dataset[-1].split(" ")[-1]
if (tail == ""):
    D = len(dataset[-1].split(" ")) - 1
else:
    D = len(dataset[-1].split(" "))
samples = [[]] * N
centroids = {}

# get centroid
for i in range(N + 1, N + 1 + k):
    temp = []
    centroid = dataset[i].split(" ")
    for j in range(D):
        temp.append(float(centroid[j]))
    centroids[i - N - 1] = temp

# get point
for i in range(1, N + 1):
    temp = []
    sample = dataset[i].split(" ")
    for j in range(D):
        temp.append(float(sample[j]))
    temp.append(0)
    samples[i - 1] = temp
# define cluster
def Clustering(samples, centroids):
    for item in samples:
        dists = {}
        for attr in centroids:
            dist = 0
            for i in range(D):
                diff = (item[i] - centroids[attr][i]) ** 2
                dist += diff
            dists[attr] = dist
        Min = 0
        for num in dists:
            if (dists[num] < dists[Min]):
                Min = num
        for num in dists:
            if (dists[num] == dists[Min]):
                if (num < Min):
                    Min = num
        item[-1] = Min
    return samples

# re-define centroids
def recentroids(samples, centroids):
    Centroids = centroids
    for x in centroids:
        for i in range(D):
            din = 0
            n = 0
            for y in samples:
                if (y[-1] == x):
                    n += 1
                    din += y[i]
            if (n == 0):
                Centroids[x][i] = 0
            else:
                Centroids[x][i] = din / n
    return Centroids
#main function
example = True
while (example == True):
    temp = copy.deepcopy(centroids)
    samples = Clustering(samples, centroids)
    centroids = recentroids(samples, centroids)
    if (temp != centroids):
        example = True
    else:
        example = False
# print results
for item in samples:
    print(item[-1])
