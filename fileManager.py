from session import Session
from datetime import datetime

class FileManager:

    directory = ""

    def __init__(self, directory):
        if not directory.endswith('/'):
            directory += "/"

        self.directory = directory


    def readSessionFile(self, filename, repository):
        sessionManager = None

        with open(self.directory + filename, 'r', encoding='utf-8') as f:
            for line in f:
                data = line.split(',')
                if(sessionManager == None):
                    sessionManager = SessionManager(data)
                elif(sessionManager.id != int(data[0])):
                    repository.add(sessionManager.getSession())
                    sessionManager = SessionManager(data)
                else:
                    sessionManager.updateSession(data)

        return repository



    def readBuyFile(self, filename, repository):
        with open(self.directory + filename, 'r', encoding='utf-8') as f:
            for line in f:
                data = line.split(',')
                session = repository.getById(int(data[0]))
                if(session != None):
                    session.buy = True
                    repository.update(session)

        return repository





class SessionManager:

    id = 0
    numberOfClicks = 0
    special = False
    buy = False

    startTime = None
    endTime = None
    items = []

    def __init__(self, data):
        self.id = int(data[0])
        self.numberOfClicks += 1
        self.duration = 0

        self.startTime = data[1]
        self.endTime = self.startTime

        self.items = [data[2]]
        self.updateSpecial(data[3])


    def updateSession(self, data):
        self.numberOfClicks += 1
        self.updateEndTime(data[1])
        self.updateItems(data[2])
        self.updateSpecial(data[3])


    def updateItems(self, item):
        if(item not in self.items):
            self.items.append(item)


    def updateEndTime(self, timestamp):
        self.endTime = timestamp


    def updateSpecial(self, category):
        if category.strip() == "S":
            self.special = True

    def getElapsedTime(self):
        pattern = "%Y-%m-%dT%H:%M:%S.%fZ"
        startTime = datetime.strptime(self.startTime, pattern)
        endTime = datetime.strptime(self.endTime, pattern)
        return (endTime - startTime).total_seconds()


    def getSession(self):
        return Session(self.id, self.getElapsedTime(), self.numberOfClicks, len(self.items), self.special, self.buy)








