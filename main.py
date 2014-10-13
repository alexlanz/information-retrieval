from books import BookStorage
from index import Index
from output import Output

# Books
storage = BookStorage("books")
books = storage.getBooks()

# Index
index = Index()

for book in books:
    text = storage.getBookText(book)
    tokensInTheBook = index.parseTokensFromText(text)

# Variables for output
numberOfTerms = index.getNumberOfTerms()
numberOfUniqueTerms = index.getNumberOfUniqueTerms()
mostFrequentTerms = index.getMostFrequentTerms(50)

# Output
output = Output()
output.outputText("Number of terms: " + str(numberOfTerms))
output.outputText("Number of unique terms: " + str(numberOfUniqueTerms))
output.outputNewLine()
output.outputText("50 most frequent terms:")
output.outputTermsWithFrequency(mostFrequentTerms)

print("Results are written to 'results.txt'.")
