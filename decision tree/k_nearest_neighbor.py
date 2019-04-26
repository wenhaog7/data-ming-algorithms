#K-NN functions
def get_distance(point):
    dists = []
    for x in L:
        dist_sq = 0
        for i in range(1, len(L[0])):
            temp_train = float(x[i][1])
            temp_test = float(point[i][1])
            diff = (temp_test - temp_train)**2
            dist_sq = dist_sq + diff
        dist = [math.sqrt(dist_sq), x[0]]
        dists.append(dist)
    return(dists)
