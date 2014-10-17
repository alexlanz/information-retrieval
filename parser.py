import nltk

class Parser:

    def parseTokensFromText(self, text):
        tokenList = nltk.word_tokenize(text)
        parsedTockenList = [token.lower() for token in tokenList if token.isalpha()]
        return parsedTockenList


'''    def getNumberOfTerms(self):
        return len(self.terms)


    def getNumberOfUniqueTerms(self):
        return len(set(self.terms))


    def getMostFrequentTerms(self, numberOfTerms):
        mostFrequentTerms = nltk.FreqDist(self.terms)
        return mostFrequentTerms.most_common(numberOfTerms)'''