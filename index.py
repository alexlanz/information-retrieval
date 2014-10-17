class Posting:

    document = None
    count = 0

    def __init__(self, document):
        self.document = document
        self.count = 1

    def getDocument(self):
        return self.document


    def incrementCount(self):
        self.count += 1


    def getCount(self):
        return self.count


class PostingsList:

    postings = []

    def __init__(self):
        self.postings = []


    def addPosting(self, document):
        length = len(self.postings)

        if length == 0:
            self.addNewPosting(document)
            return

        posting = self.postings[length - 1]
        postingDocument = posting.getDocument()

        if postingDocument.getPath() == document.getPath():
            posting.incrementCount()
        else:
            self.addNewPosting(document)


    def getPostings(self):
        return self.postings


    def addNewPosting(self, document):
        posting = Posting(document)
        self.postings.append(posting)


class Dictionary:

    terms = {}

    def __init__(self):
        self.terms = {}


    def getTerms(self):
        return self.terms


    def getPostingsList(self, term):
        if term in self.terms:
            return self.terms[term]

        postingList = PostingsList()
        self.terms[term] = postingList
        return postingList
