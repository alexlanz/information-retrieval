from enum import Enum
from utils import Timer
from parser import NGramParser
from documents import DocumentManager
from vectorspace import VectorProvider
from vectorspace import VectorSpace


class Index:

    parser = None
    timer = None
    dictionary = None
    ngrams = None
    documents = None
    vectorSpace = None
    vectorProvider = None

    def __init__(self, indexParser):
        self.parser = indexParser
        self.dictionary = Dictionary()
        self.ngrams = NGrams()
        self.documents = []
        self.vectorSpace = VectorSpace()
        self.vectorProvider = None

        self.timer = Timer()
        self.timer.start()

        self.setup()

        self.timer.stop()


    def setup(self):
        self.createNewIndex()



    def createNewIndex(self):
        docCoordinator = DocumentManager("documents")
        self.documents = docCoordinator.loadDocuments()

        bigramParser = NGramParser(2)

        for document in self.documents:
            text = docCoordinator.getDocumentText(document)
            tokens = self.parser.parse(text)

            for position, token in enumerate(tokens):

                if not self.dictionary.existsPostingsList(token):
                    postingList = self.dictionary.createPostingsList(token)

                    bigrams = bigramParser.parseNGramsWithPadSymbol(token)

                    for i in range(0, len(bigrams)):
                        bigram = bigrams[i]
                        self.ngrams.addPart(bigram, NGramPart(token, i))

                else:
                    postingList = self.dictionary.getPostingsList(token)

                postingList.addPosting(document, position)

        # VectorSpace
        self.calculateVectorSpace()


    def getDictionary(self):
        return self.dictionary

    def getNGrams(self):
        return self.ngrams

    def getTimer(self):
        return self.timer


    def getParserType(self):
        return self.parserType


    def getVectorSpace(self):
        return self.vectorSpace


    def getVectorProvider(self):
        return self.vectorProvider


    def getNumberOfDocuments(self):
        return len(self.documents)


    def calculateVectorSpace(self):
        self.vectorProvider = VectorProvider(self.getDictionary().getSortedTerms())

        for document in self.documents:
            vector = self.vectorProvider.createVectorForDocument(self, document, self.getNumberOfDocuments())
            self.vectorSpace.addDocumentVector(document, vector)


class Posting:

    document = None
    count = 0
    positions = []

    def __init__(self, document):
        self.document = document
        self.count = 0
        self.positions = []


    def getDocument(self):
        return self.document


    def addOccurrence(self, position):
        self.count += 1
        self.positions.append(position)


    def getCount(self):
        return self.count


    def getPositions(self):
        return self.positions


class PostingsList:

    postings = []

    def __init__(self):
        self.postings = []


    def addPosting(self, document, position):
        length = len(self.postings)

        if length == 0:
            self.addNewPosting(document, position)
            return

        posting = self.postings[length - 1]
        postingDocument = posting.getDocument()

        if postingDocument.getPath() == document.getPath():
            posting.addOccurrence(position)
        else:
            self.addNewPosting(document, position)


    def getPostings(self):
        return self.postings


    def addNewPosting(self, document, position):
        posting = Posting(document)
        posting.addOccurrence(position)
        self.postings.append(posting)


    def getSortedPostingsList(self):
        return sorted(self.postings, key=lambda posting: posting.getDocument().getPath())


class Dictionary:

    terms = {}

    def __init__(self):
        self.terms = {}


    def getTerms(self):
        return self.terms

    def existsPostingsList(self, term):
        return (term in self.terms)

    def createPostingsList(self, term):
        postingList = PostingsList()
        self.terms[term] = postingList
        return postingList

    def getPostingsList(self, term):
        return self.terms[term]

    def getSortedTerms(self):
        return sorted(self.terms.keys())


class NGramPart:

    term = None
    position = None

    def __init__(self, term, position):
        self.term = term
        self.position = position

    def getTerm(self):
        return self.term

    def getPosition(self):
        return self.position


class NGrams:

    ngrams = None

    def __init__(self):
        self.ngrams = {}

    def addPart(self, ngram, part):
        if not ngram in self.ngrams.keys():
            self.ngrams[ngram] = []

        self.ngrams[ngram].append(part)

    def getList(self, ngram):
        return self.ngrams[ngram]

    def pr(self):
        bigrams = self.ngrams['he']

        for bigramPart in bigrams:
            print("Position: " + str(bigramPart.getPosition()) + "\tTerm: " + bigramPart.getTerm())
