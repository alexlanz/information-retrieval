import numpy

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
    index = None

    def __init__(self, sortedTerms, index):
        self.sortedTerms = sortedTerms
        self.index = index


    def createVectorForDocument(self, document):
        return []


    def calculateWeightedTermFrequency(self, term, document):
        postingsList = self.index.getDictionary().getPostingsList(term)

        tf = 0
        for posting in postingsList.getPostings():
            if posting.getDocument() == document:
                tf = posting.getCount()
                break

        return numpy.log10(1 + tf)


    def calculateWeightedIdf(self, term, totalDocs):

        df = len(self.index.getDictionary().getPostingsList(term).getPostings())

        return numpy.log10(totalDocs/df)


    def calcualateTfIdfWeighting(self, term, document, totalDocs):
        return self.calculateWeightedTermFrequency(term, document) * self.calculateWeightedIdf(term, totalDocs)
