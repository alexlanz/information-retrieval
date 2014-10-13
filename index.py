import nltk

class Index:

    terms = []


    def parseTokensFromText(self, text):
        tokenList = nltk.word_tokenize(text)
        modifiedTokenList = [token.lower() for token in tokenList if token.isalpha()]
        self.terms.extend(modifiedTokenList)
        return modifiedTokenList


    def getNumberOfTerms(self):
        return len(self.terms)


    def getNumberOfUniqueTerms(self):
        return len(set(self.terms))


    def getMostFrequentTerms(self, numberOfTerms):
        mostFrequentTerms = nltk.FreqDist(self.terms)
        return mostFrequentTerms.most_common(numberOfTerms)