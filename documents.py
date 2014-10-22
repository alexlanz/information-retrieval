from os import walk

class Document:

    path = ""

    def __init__(self, path):
        self.path = path

    def getPath(self):
        return self.path


class DocumentCoordinator:

    directory = ""
    files = []
    documents = []

    def __init__(self, directory):
        if not directory.endswith('/'):
            directory += "/"

        self.directory = directory
    

    def loadDocuments(self):
        for (dirpath, dirnames, filenames) in walk(self.directory):
            self.files.extend(filenames)

        for index in range(len(self.files)):
            document = Document(self.directory + self.files[index])
            self.documents.append(document)

        return self.documents


    def getDocumentText(self, document):
        fp = open(document.getPath(), 'r', encoding='utf-8')
        text = fp.read()
        fp.close()
        
        return text