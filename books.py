from os import walk

class Storage:

    directory = ""

    def __init__(self, directory):
        self.directory = directory
    
    def getBooks(self):
        books = []

        for (dirpath, dirnames, filenames) in walk(self.directory):
            books.extend(filenames)

        path = self.directory

        if not path.endswith('/'):
            path += "/"

        for index in range(len(books)):
            books[index] = path + books[index]

        return books