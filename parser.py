import nltk
from nltk.util import ngrams
from utils import Timer
from query import Query
from nltk.corpus import wordnet as wn

class IndexParser:

    def parse(self, text):
        tokenList = nltk.word_tokenize(text)
        parsedTokenList = [token.lower() for token in tokenList if token.isalpha() and self.is_ascii(token)]
        return parsedTokenList

    def is_ascii(self, string):
        return all(ord(c) < 128 for c in string)


class QueryParser:

    ngrams = None
    timer = None

    def __init__(self, ngrams):
        self.ngrams = ngrams


    def parse(self, query):
        self.timer = Timer()
        self.timer.start()

        rawQueries = query.split(sep="+")
        parsedQueries = []

        for rawQuery in rawQueries:
            searchedTokens = []
            excludedTokens = []

            for token in rawQuery.strip().split(sep=" "):
                token = token.lower()

                if token.startswith('-'):
                    excludedTokens.append(token[1:])
                elif self.isWildcardToken(token):
                    wildcardTokens = self.getTokensForWildcardToken(token)
                    searchedTokens.extend(wildcardTokens)
                else:
                    searchedTokens.append(token)
                    searchedTokens.extend(self.getSynonymsForToken(token))

            parsedQueries.append(Query(searchedTokens, excludedTokens))

        self.timer.stop()

        return parsedQueries


    def getTimer(self):
        return self.timer


    def isWildcardToken(self, token):
        return '*' in token


    def getTokensForWildcardToken(self, token):
        wildcardParts = self.getSplitWildcardTokenParts(token)

        bigramParser = NGramParser(2)
        bigramsOfParts = []

        for part in wildcardParts:
            bigramsOfParts.append(bigramParser.parseNGramsWithoutPadSymbol(part))

        matchedNGramParts = []
        for bigrams in bigramsOfParts:
            matchedNGramParts.append(self.getMatchedNgramParts(bigrams))

        finalNGramParts = self.combineMatchedNgramParts(matchedNGramParts)

        tokens = []
        for part in finalNGramParts:
            tokens.append(part.getTerm())

        return tokens

    def getSplitWildcardTokenParts(self, token):
        if token.startswith('*'):
            token = token[1:]
        else:
            token = '$' + token

        if token.endswith('*'):
            token = token[:len(token)-1]
        else:
            token += '$'

        return token.split('*')

    def getMatchedNgramParts(self, ngrams):
        results = self.ngrams.getList(ngrams[0])

        for i in range(1, len(ngrams)):
            ngram = ngrams[i]
            occurrenceList = self.ngrams.getList(ngram)

            roundResult = []

            for result in results:
                termFound = False

                for occurrence in occurrenceList:
                    if result.getTerm() == occurrence.getTerm():
                        termFound = True

                        if (result.getPosition() + 1) == occurrence.getPosition():
                            roundResult.append(occurrence)
                            break
                    else:
                        if termFound:
                            break

            results = roundResult


        return results

    def combineMatchedNgramParts(self, ngramParts):
        results = ngramParts[0]

        for i in range(1, len(ngramParts)):
            ngramPart = ngramParts[i]

            roundResult = []

            for result in results:
                termFound = False

                for occurrence in ngramPart:
                    if result.getTerm() == occurrence.getTerm():
                        termFound = True

                        if (result.getPosition()) <= occurrence.getPosition():
                            roundResult.append(occurrence)
                            break
                    else:
                        if termFound:
                            break

            results = roundResult


        return results


    def getSynonymsForToken(self, token):
        synonymes = []
        synset = wn.synsets(token)
        if synset: #emptyness check
            return synset[0].lemma_names()
        return []


class NGramParser:

    n = 2

    def __init__(self, n):
        self.n = n

    def parseNGramsWithPadSymbol(self, term):
        ngramsGenerator = ngrams(term, self.n, pad_left=True, pad_right=True, pad_symbol='$')
        ngramsList = list(ngramsGenerator)

        ngramsListJoined = []

        for ngram in ngramsList:
            ngramsListJoined.append(''.join(ngram))

        return ngramsListJoined

    def parseNGramsWithoutPadSymbol(self, term):
        ngramsGenerator = ngrams(term, self.n, pad_left=False, pad_right=False)
        ngramsList = list(ngramsGenerator)

        ngramsListJoined = []

        for ngram in ngramsList:
            ngramsListJoined.append(''.join(ngram))

        return ngramsListJoined