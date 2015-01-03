from session import Session
from datetime import datetime

class FileManager:

    directory = ""

    def __init__(self, directory):
        if not directory.endswith('/'):
            directory += "/"

        self.directory = directory


    def readSessionFile(self, filename, repository, items):
        sessionManager = None

        with open(self.directory + filename, 'r', encoding='utf-8') as f:
            for line in f:

                data = line.split(',')
                items.addItem(int(data[2]))

                if sessionManager is None:
                    sessionManager = SessionManager(data)
                elif sessionManager.id != int(data[0]):
                    repository.add(sessionManager.getSession())
                    sessionManager = SessionManager(data)
                else:
                    sessionManager.updateSession(data)

            repository.add(sessionManager.getSession())

        return repository



    def readBuyFile(self, filename, repository, items):
        with open(self.directory + filename, 'r', encoding='utf-8') as f:
            for line in f:
                data = line.split(',')
                items.addBuyingEvent(int(data[2]), datetime.strptime(data[1], "%Y-%m-%dT%H:%M:%S.%fZ").date())
                session = repository.getById(int(data[0]))
                if session is not None:
                    session.buy = True
                    repository.update(session)

        return repository


    def getBoughtItemList(self, sessionId):
        boughtItems = []
        with open(self.directory + 'yoochoose-buys.dat', 'r', encoding='utf-8') as f:
            for line in f:
                data = line.split(',')
                if(sessionId == int(data[0])):
                    boughtItems.append(data[2])
        return boughtItems


class SessionManager:

    id = 0
    numberOfClicks = 0
    buy = False

    startTime = None
    endTime = None
    items = {}

    def __init__(self, data):
        self.id = int(data[0])
        self.numberOfClicks += 1
        self.duration = 0

        self.startTime = data[1]
        self.endTime = self.startTime

        self.items = {}
        self.items[int(data[2])] = self.isSpecial(data[2])


    def updateSession(self, data):
        self.numberOfClicks += 1
        self.updateEndTime(data[1])
        self.updateItems(int(data[2]), data[3])


    def updateItems(self, itemId, special):
        if self.items.get(itemId) is None:
            self.items[itemId] = self.isSpecial(special)


    def updateEndTime(self, timestamp):
        self.endTime = timestamp

    def isSpecial(self, category):
        if category.strip() == "S":
            return True
        else:
            return False

    def getElapsedTime(self):
        pattern = "%Y-%m-%dT%H:%M:%S.%fZ"
        startTime = datetime.strptime(self.startTime, pattern)
        endTime = datetime.strptime(self.endTime, pattern)
        return (endTime - startTime).total_seconds()


    def getSession(self):
        startTime = datetime.strptime(self.startTime, "%Y-%m-%dT%H:%M:%S.%fZ").date()
        return Session(self.id, startTime, self.getElapsedTime(), self.numberOfClicks, self.items, self.buy)