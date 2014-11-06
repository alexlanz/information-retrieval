import pickle
import os

class Storage:

    STORAGE_DIRECTORY = "storage/"


    def saveDictionary(self, dictionary):
        self.checkDirectory()

        dictionaryFileName = self.getDictionaryFileName()
        
        file = open(dictionaryFileName, "wb+")
        pickle.dump(dictionary, file)
        file.close()


    def saveNGrams(self, ngrams):
        self.checkDirectory()

        ngramsFileName = self.getNGramsFileName()

        file = open(ngramsFileName, "wb+")
        pickle.dump(ngrams, file)
        file.close()


    def loadDictionary(self):
        fileName = self.getDictionaryFileName()

        if not os.path.exists(fileName):
            raise ValueError("No dictionary is stored")

        file = open(fileName, "rb")
        dictionary = pickle.load(file)
        file.close()

        return dictionary


    def loadNGrams(self):
        fileName = self.getNGramsFileName()

        if not os.path.exists(fileName):
            raise ValueError("No ngrams are stored")

        file = open(fileName, "rb")
        dictionary = pickle.load(file)
        file.close()

        return dictionary


    def checkDirectory(self):
        if not os.path.isdir(self.STORAGE_DIRECTORY):
            os.mkdir(self.STORAGE_DIRECTORY)

    def getDictionaryFileName(self):
        return self.STORAGE_DIRECTORY + "dictionary"


    def getNGramsFileName(self):
        return self.STORAGE_DIRECTORY + "ngrams"