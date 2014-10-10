import string
import nltk
import sklearn
from books import Storage
from index import Term
from output import Output

# Books
storage = Storage("books")
books = storage.getBooks()


# Create Index
terms = {}
numberOfTerms = 0

punctuationsList = list(string.punctuation)
punctuationsString = "".join(punctuationsList)

for book in books:
    with open(book) as fp:
        rank = 0

        for line in fp:
            tokens = [i.strip(punctuationsString).lower() for i in nltk.word_tokenize(line) if i not in punctuationsList]
            
            for token in tokens:
                
                if token in terms:
                    term = terms[token]
                else:
                    term = Term(token)
                    terms[token] = term

                term.frequency += 1
                term.addHit(book, rank)

                rank += 1
                numberOfTerms += 1

# Output
output = Output()
output.outputText("Number of terms: " + str(numberOfTerms))
output.outputText("Number of unique terms: " + str(len(terms)))
output.outputText("\n")
output.outputTermsWithFrequency(terms)
output.outputText("\n")
output.outputTermsWithRanksInDocuments(terms)

print("Results are written to 'results.txt'.")