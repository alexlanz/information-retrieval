import pickle
import os

class Storage:

    STORAGE_DIRECTORY = "storage/"


    def storeDictionary(self, dictionary):
        fileName = self.getDictionaryFileName()
        self.store(fileName, dictionary)


    def storeNGrams(self, ngrams):
        fileName = self.getNGramsFileName()
        self.store(fileName, ngrams)


    def store(self, fileName, object):
        if not os.path.isdir(self.STORAGE_DIRECTORY):
            os.mkdir(self.STORAGE_DIRECTORY)

        file = open(fileName, "wb+")
        pickle.dump(object, file)
        file.close()


    def loadDictionary(self):
        fileName = self.getDictionaryFileName()
        return self.load(fileName)


    def loadNGrams(self):
        fileName = self.getNGramsFileName()
        return self.load(fileName)


    def load(self, fileName):
        if not os.path.exists(fileName):
            raise ValueError("File " + fileName + " does not exist.")

        file = open(fileName, "rb")
        object = pickle.load(file)
        file.close()

        return object


    def getDictionaryFileName(self):
        return self.STORAGE_DIRECTORY + "dictionary"


    def getNGramsFileName(self):
        return self.STORAGE_DIRECTORY + "ngrams"