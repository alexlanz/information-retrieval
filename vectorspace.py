import numpy
from scipy.stats import itemfreq

class VectorSpace:

    documentVectors = {}

    def __init__(self):
        self.documentVectors = {}


    def addDocumentVector(self, document, vector):
        self.documentVectors[document] = vector


    def getDocumentVector(self, document):
        return self.documentVectors[document]



class VectorProvider:

    sortedTerms = []

    def __init__(self, sortedTerms):
        self.sortedTerms = sortedTerms


    def createVectorForDocument(self, index, document, totalDocuments):
        vector = []
        for term in self.sortedTerms:
            postingsList = index.getDictionary().getPostingsList(term)
            vector.append(self.calcualateTfIdfWeighting(postingsList, document, totalDocuments))

        return vector


    def createVectorForQuery(self, index, terms, totalDocs):
        vector = []
        for term in self.sortedTerms:
            if term in terms:
                postingsList = index.getDictionary().getPostingsList(term)
                vector.append(self.calculateTfIdfWeightingQuery(term, postingsList, terms, totalDocs))
            else:
                vector.append(0)

        return vector


    def calculateWeightedTermFrequency(self, postingsList, document):
        tf = 0
        for posting in postingsList.getPostings():
            if posting.getDocument() == document:
                tf = posting.getCount()
                break

        return numpy.log10(1 + tf)


    def calculateWeightedQueryTermFrequency(self, term, terms):
        tf = 0;
        for term in terms:
            if term in terms:
                tf += 1

        return numpy.log10(1 + tf)


    def calculateWeightedIdf(self, postingsList, totalDocs):

        df = len(postingsList.getPostings())

        return numpy.log10(totalDocs/df)


    def calcualateTfIdfWeighting(self, postingsList, document, totalDocs):
        return self.calculateWeightedTermFrequency(postingsList, document) * self.calculateWeightedIdf(postingsList, totalDocs)


    def calculateTfIdfWeightingQuery(self, term, postingsList, terms, totalDocs):
        return self.calculateWeightedQueryTermFrequency(term, terms) * self.calculateWeightedIdf(postingsList, totalDocs)

