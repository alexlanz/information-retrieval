from enum import Enum
from nltk.util import ngrams
from utils import Timer
from parser import Parser
from documents import DocumentManager
from storage import Storage


class IndexSource(Enum):
    new = 1
    stored = 2


class Index:

    source = None
    parser = None
    timer = None
    dictionary = None
    ngrams = None
    parserType = None

    def __init__(self, source, parser):
        self.source = source
        self.parser = parser
        self.dictionary = Dictionary()
        self.ngrams = {}

        self.timer = Timer()
        self.timer.start()

        self.setup()

        self.timer.stop()


    def setup(self):
        if self.source == IndexSource.new:
            self.createNewIndex()
        elif self.source == IndexSource.stored:
            self.loadStoredIndex()
        else:
            raise ValueError("Invalid index source")


    def createNewIndex(self):
        docCoordinator = DocumentManager("documents")
        documents = docCoordinator.loadDocuments()

        for document in documents:
            text = docCoordinator.getDocumentText(document)
            tokens = self.parser.parseTokensFromText(text)

            for position, token in enumerate(tokens):
                if not self.dictionary.existsPostingsList(token):
                    postingList = self.dictionary.createPostingsList(token)

                    bigrams = ngrams(token, 2, pad_left=True, pad_right=True, pad_symbol='$')
                    bigramsList = list(bigrams)

                    for i in range(0, len(bigramsList)):
                        bigram = ''.join(bigramsList[i])
                        self.ngrams[bigram] = NGramWord(token, i)

                else:
                    postingList = self.dictionary.getPostingsList(token)

                postingList.addPosting(document, position)



    def loadStoredIndex(self):
        storage = Storage()
        self.dictionary = storage.loadDictionary()
        self.ngrams = storage.loadNGrams()


    def storeIndex(self):
        self.timer = Timer()
        self.timer.start()

        storage = Storage()
        storage.storeDictionary(self.dictionary)
        storage.storeNGrams(self.ngrams)

        self.timer.stop()


    def getDictionary(self):
        return self.dictionary


    def getTimer(self):
        return self.timer


    def getParserType(self):
        return self.parserType


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


class NGramWord:

    term = None
    position = None

    def __init__(self, term, position):
        self.term = term
        self.position = position

    def getTerm(self):
        return self.term

    def getPosition(self):
        return self.position