from books import BookShelf
from index import Dictionary
from parser import Parser
from output import Output

# Books
bookShelf = BookShelf("books")
books = bookShelf.loadBooks()

# Index
dictionary = Dictionary()
parser = Parser()

for book in books:
    text = bookShelf.getBookText(book)
    tokensInTheBook = parser.parseTokensFromText(text)

    for token in tokensInTheBook:
        postingList = dictionary.getPostingsList(token)
        postingList.addPosting(book)

    break

# Output
for term, postingList in dictionary.getTerms().items():
    print("Term: " + term + " PostingList: " + str(postingList.getPostings()[0].getCount()))