import pickle
import os

class Storage:

    STORAGE_DIRECTORY = "storage/"


    def saveIndex(self, dictionary):
        if not os.path.isdir(self.STORAGE_DIRECTORY):
            os.mkdir(self.STORAGE_DIRECTORY)

        fileName = self.getIndexFileName()
        
        file = open(fileName, "wb+")
        pickle.dump(dictionary, file)
        file.close()


    def loadIndex(self):
        fileName = self.getIndexFileName()

        if not os.path.exists(fileName):
            raise ValueError("No index is stored")

        file = open(fileName, "rb")
        dictionary = pickle.load(file)
        file.close()

        return dictionary


    def getIndexFileName(self):
        return self.STORAGE_DIRECTORY + "index"