#import matplotlib.pyplot as plot

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
        #relevantInstances = QuerySet.getRelevantInstances(queryIndex) #file-namensliste
        if len(queryResult) == 0:
            return (0, 0)

        precisionAtK = []
        for k in self.k:
            relevant = 0
            for item in queryResult[:k]:
                if item.getRank() >= self.relevantThreshold:
                    relevant += 1
            precisionAtK.append((k,(relevant / k)))
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


    '''def plotRecallPrecision(self, recallList, precisionList):
        plot.plot([r[0] for r in recallList], [r[1] for r in recallList], "bs-")
        plot.ylabel("recall")
        plot.xlabel("top-k recommendations")

        plot.figure()
        plot.ylabel("precision")
        plot.xlabel("top-k recommendations")
        plot.plot([p[0] for p in precisionList], [p[1] for p in precisionList], 'rs-')

        plot.show()'''



