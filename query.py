from utils import Timer
from rank import RankUtils
from rank import RankedResult
from rank import RankedResultItem

class QueryExecutor:

    index = None
    timer = None

    def __init__(self, index):
        self.index = index


    def executeQuery(self, queryList):
        self.timer = Timer()
        self.timer.start()

        matchedResultsList = []
        searchtokens = []

        for query in queryList:
            searchedTokens = query.getSearchTokens()
            excludedTokens = query.getExcludedTokens()

            searchedResult = QueryResult()
            for token in searchedTokens:
                searchtokens.append(token)
                postingsList = self.index.getDictionary().getPostingsList(token)
                searchedResult.addPostingList(token, postingsList)

            excludedResult = QueryResult()
            for token in excludedTokens:
                postingsList = self.index.getDictionary().getPostingsList(token)
                excludedResult.addPostingList(token, postingsList)

            if(len(excludedResult.getItems()) > 0):
                matchedResults = QueryResult.mergeWithExclusions(searchedResult, excludedResult)
            else:
                matchedResults = searchedResult

            matchedResultsList.append(matchedResults)

        matchedResults = QueryResult.mergeWithIntersection(matchedResultsList)
        queryVector = self.index.getVectorProvider().createVectorForQuery(searchtokens, self.index.getNumberOfIndexDocuments())

        rankedResult = RankedResult()
        for document, queryResultItem in matchedResults.getItems().items():
            rank = RankUtils.calculateVectorSpaceRank(queryVector, self.index.getVectorSpace().getDocumentVector(document))
            rankedResultItem = RankedResultItem(document, rank, queryResultItem)
            rankedResult.addRankedResultItem(rankedResultItem)

        sortedResult = rankedResult.getSortedResult()

        self.timer.stop()

        return sortedResult


    def getTimer(self):
        return self.timer


class Query:

    searchTokens = []
    excludedTokens = []


    def __init__(self, searchTokens, excludedTokens):
        self.searchTokens = searchTokens
        self.excludedTokens = excludedTokens


    def getSearchTokens(self):
        return self.searchTokens


    def getExcludedTokens(self):
        return self.excludedTokens



class QueryResultItem:

    matches = None

    def __init__(self):
        self.matches = {}


    def addMatch(self, term, count):
        self.matches[term] = count


    def getMatches(self):
        return self.matches


    @staticmethod
    def mergeQueryResultItems(queryResultItems):
        result = QueryResultItem()

        for resultItem in queryResultItems:
            for term, count in resultItem.getMatches().items():
                result.addMatch(term, count)

        return result



class QueryResult:

    items = None

    def __init__(self):
        self.items = {}


    def addPostingList(self, term, postingList):
        for posting in postingList.getPostings():
            self.addPosting(term, posting)


    def addPosting(self, term, posting):
        document = posting.getDocument()

        if(not document in self.items):
            self.items[document] = QueryResultItem()

        self.items[document].addMatch(term, posting.getCount())


    def addResultItem(self, doc, resultItem):
        self.items[doc] = resultItem


    def getItems(self):
        return self.items


    @staticmethod
    def mergeWithExclusions(searchQueryResult, excludedQueryResult):
        queryResult = QueryResult()

        for document, searchResultItem in searchQueryResult.getItems().items():
            if(not document in excludedQueryResult.getItems()):
                queryResult.addResultItem(document, searchResultItem)

        return queryResult


    @staticmethod
    def mergeWithIntersection(queryMatchingList):
        queryResult = QueryResult()

        if(len(queryMatchingList) == 0):
            return queryResult
        elif(len(queryMatchingList) == 1):
            return queryMatchingList[0]

        for document, resultItem in queryMatchingList[0].getItems().items():
            tempResultItemList = [resultItem]
            exists = True

            for i in range(1, len(queryMatchingList)):
                if(not document in queryMatchingList[i].getItems()):
                    exists = False
                    break

                tempResultItemList.append(queryMatchingList[i].getItems()[document])

            if(exists):
                finalQueryResultItem = QueryResultItem.mergeQueryResultItems(tempResultItemList)
                queryResult.addResultItem(document, finalQueryResultItem)

        return queryResult
