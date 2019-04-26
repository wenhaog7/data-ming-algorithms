#build tree
class Tree:
    def __init__(self, value=None, leftBranch=None, rightBranch=None, results=None, col=0, data=None):
        self.value = value
        self.leftBranch = leftBranch
        self.rightBranch = rightBranch
        self.results = results
        self.col = col
        self.data = data

#decision tree functions
def calculateDiffCount(datas):
        results = {}
        for data in datas:
            if data[0] not in results:
                results[data[0]] = 1
            else:
                results[data[0]] += 1
        return results

def gini(rows):
        length = len(rows)
        results = calculateDiffCount(rows)
        imp = 0.0
        for i in results:
            imp += results[i] / length * results[i] / length
        return 1 - imp
    
def splitDatas(rows, value, col):
        list1 = []
        list2 = []
        for row in rows:
            if (row[col][1] >= value):
                list1.append(row)
            else:
                list2.append(row)
        return (list1, list2)
    
def buildDecisionTree(rows, level, evaluationFunction=gini):
        currentGain = evaluationFunction(rows)
        column_length = len(rows[0])
        rows_length = len(rows)
        best_gain = 0.0
        best_value = None
        best_set = None

        
        for col in range(1, column_length):
            col_value_set = set([x[col][1] for x in rows])
            col_value_list = []
            for value in col_value_set:
                col_value_list.append(value)
            col_value_list.sort()
            split_list = []
            for i in range(len(col_value_list) - 1):
                mid = (col_value_list[i] + col_value_list[i + 1]) / 2
                split_list.append(mid)
            for value in split_list:
                list1, list2 = splitDatas(rows, value, col)
                p = len(list1) / rows_length
                gain = currentGain-p*evaluationFunction(list1)-(1-p)*(evaluationFunction(list2))
                if gain > best_gain:
                    best_gain = gain
                    best_value = (col, value)
                    best_set = (list1, list2)
                    
        if  level < 2 and best_gain > 0:
            leftBranch = buildDecisionTree(best_set[0], level + 1, evaluationFunction)
            rightBranch = buildDecisionTree(best_set[1], level + 1, evaluationFunction)
            return Tree(col=best_value[0], value=best_value[1], leftBranch=leftBranch, rightBranch=rightBranch)
        else:
            return Tree(results=calculateDiffCount(rows), data=rows)

def classify(data, tree):
    if tree.results != None:
        return tree.results
    else:
        branch = None
        v = data[tree.col][1]
        if v >= tree.value:
            branch = tree.leftBranch
        else:
            branch = tree.rightBranch
        return classify(data, branch)
#L: dataset, level: tree's dense
level = 0
decisionTree = buildDecisionTree(L, level, evaluationFunction=gini)
