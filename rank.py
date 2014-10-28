class RankedResult:

    rankedResult = None

    def __init__(self):
        self.rankedResult = []


    def addRankedResultItem(self, rankedResultItem):
        self.rankedResult.append(rankedResultItem)


    def getSortedResult(self):
        return sorted(self.rankedResult, key=lambda rankedResultItem: rankedResultItem.getRank(), reverse=True)


class RankedResultItem:

    document = None
    rank = None
    queryResultItem = None

    def __init__(self, document, rank, queryResultItem):
        self.document = document
        self.rank = rank
        self.queryResultItem = queryResultItem


    def getRank(self):
        return self.rank


    def getDocument(self):
        return self.document


class RankUtils:

    @staticmethod
    def calculateRank(queryResultItem, numberOfQueryTerms):
        return len(queryResultItem.getMatches()) / numberOfQueryTerms