class Statistic:

    k = []
    relevantThreshold = 0.01

    def __init__(self):
        self.k = [5, 7, 9, 12]


    def numberOfRelevantItems(self, queryResult):
        if len(queryResult) == 0:
            return 0
        relevant = 0
        for item in queryResult:
            if item.getRank() >= self.relevantThreshold:
                relevant += 1

        return relevant

    def getPrecisionAtk(self, queryResult):
        if len(queryResult) == 0:
            return (0, 0)

        precisionAtK = []
        for k in self.k:
            relevant = 0
            for item in queryResult[:k]:
                if item.getRank() >= self.relevantThreshold:
                    relevant += 1
            precisionAtK.append((k, (relevant / k)))
        return precisionAtK


    def getRecallAtk(self, queryResult):
        if len(queryResult) == 0:
            return (0,0)

        numberOfRelevantItems = self.numberOfRelevantItems(queryResult)
        recallAtk = []
        for k in self.k:
            relevant = 0
            for item in queryResult[:k]:
                if item.getRank() >= self.relevantThreshold:
                    relevant += 1

            recallAtk.append((k, (relevant / numberOfRelevantItems)))

        return recallAtk


    def printRecall(self, recallList):
        for item in recallList:
            print("Recall at k: " + str(item[0]) + "\t value: " + str(item[1]))


    def printPrecision(self, precisionList):
        for item in precisionList:
            print("Precision at k: " + str(item[0]) + "\t value: " + str(item[1]))


