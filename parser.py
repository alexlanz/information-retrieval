import nltk

class Parser:

    def parseTokensFromText(self, text):
        tokenList = nltk.word_tokenize(text)
        parsedTockenList = [token.lower() for token in tokenList if token.isalpha()]
        return parsedTockenList