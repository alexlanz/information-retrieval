from document import Document
from os import walk

class Book(Document):

    def __init__(self, path):
        Document.__init__(self, path)


class BookShelf:

    directory = ""
    files = []
    books = []

    def __init__(self, directory):
        if not directory.endswith('/'):
            directory += "/"

        self.directory = directory
    

    def loadBooks(self):
        for (dirpath, dirnames, filenames) in walk(self.directory):
            self.files.extend(filenames)

        for index in range(len(self.files)):
            book = Book(self.directory + self.files[index])
            self.books.append(book)

        return self.books


    def getBookText(self, book):
        fp = open(book.getPath(), 'rU')
        text = fp.read()
        fp.close()
        
        return text