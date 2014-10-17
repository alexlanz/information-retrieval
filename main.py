from documents import DocBase
from index import Dictionary
from parser import Parser
from utils import Timer
from output import Output

# Documents
docBase = DocBase("documents")
documents = docBase.loadDocuments()

# Index
timerForIndex = Timer()
timerForIndex.start()

dictionary = Dictionary()
parser = Parser()

for document in documents:
    text = docBase.getDocumentText(document)
    tokens = parser.parseTokensFromText(text)

    for position, token in enumerate(tokens):
        postingList = dictionary.getPostingsList(token)
        postingList.addPosting(document, position)

    break

timerForIndex.stop()
print("Time for creating index: " + timerForIndex.getElapsedMillisecondsString())

# Output
#for term, postingList in dictionary.getTerms().items():
#    print("Term: " + term + " PostingList: " + str(postingList.getPostings()[0].getCount()))


postingList = dictionary.getPostingsList('either')

print("Positions for either")
for posting in postingList.getPostings():
    for position in posting.getPositions():
        print(str(position))