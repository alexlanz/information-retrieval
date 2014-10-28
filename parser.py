from enum import Enum
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from query import Query


class ParserType(Enum):
    simple = 1
    wordprocessing = 2


class Parser:

    type = None
    stemmer = None
    lemmatizer = None
    stopWords = None

    def __init__(self, type):
        self.type = type

        if self.type == ParserType.wordprocessing:
            self.stemmer = PorterStemmer()
            self.lemmatizer = WordNetLemmatizer()
            self.stopWords = stopwords.words("english")


    def parseTokensFromText(self, text):
        tokenList = nltk.word_tokenize(text)

        if self.type == ParserType.wordprocessing:
            parsedTokenList = [self.applyTextProcessing(token.lower()) for token in tokenList if (token.isalpha()) and (not token.lower() in self.stopWords)]
        else:
            parsedTokenList = [token.lower() for token in tokenList if token.isalpha()]

        return parsedTokenList


    def parseQuery(self, query):
        rawQueries = query.split(sep="+")
        parsedQueries = []

        for rawQuery in rawQueries:
            searchedTokens = []
            excludedTokens = []

            for token in rawQuery.strip().split(sep=" "):
                token = token.lower()

                if self.type == ParserType.wordprocessing:
                    if not token in self.stopWords:
                        
                        if(token.startswith('-')):
                            excludedToken = self.applyTextProcessing(token[1:])
                            excludedTokens.append(excludedToken)
                        else:
                            searchedTokens.append(self.applyTextProcessing(token))
                else:
                    if(token.startswith('-')):
                        excludedTokens.append(token[1:])
                    else:
                        searchedTokens.append(token)

            parsedQueries.append(Query(searchedTokens, excludedTokens))

        return parsedQueries


    def applyTextProcessing(self, token):
        stemmedToken = self.applyStemming(token)
        lemmatizedToken = self.applyLemmatization(stemmedToken)
        return lemmatizedToken

    def applyStemming(self, token):
        return self.stemmer.stem(token)

    def applyLemmatization(self, token):
        return self.lemmatizer.lemmatize(token)
