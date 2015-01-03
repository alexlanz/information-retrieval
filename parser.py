from session import Session
from sessionRepository import SessionRepository
from itemRepository import ItemRepository
from datetime import datetime

class Parser:

    directory = ""
    sessionRepository = None
    itemRepository = None

    def __init__(self, directory):
        if not directory.endswith('/'):
            directory += "/"

        self.directory = directory
        self.sessionRepository = SessionRepository()
        self.itemRepository = ItemRepository()


    def getSessionRepository(self):
        return self.sessionRepository


    def getItemRepository(self):
        return self.itemRepository


    def readSessionFile(self, filename):
        currentSession = None

        with open(self.directory + filename, 'r', encoding='utf-8') as f:
            for line in f:

                data = line.split(',')

                id = int(data[0])
                time = datetime.strptime(data[1], "%Y-%m-%dT%H:%M:%S.%fZ")
                item = int(data[2])
                special = True if (data[3]).strip() == "S" else False

                # ItemRepository
                if self.itemRepository is not None:
                    self.itemRepository.addItem(item)

                # SessionRepository
                if currentSession is None:
                    currentSession = SessionCreator(id, time, item, special)

                elif currentSession.id != id:
                    self.sessionRepository.add(currentSession.getSession())
                    currentSession = SessionCreator(id, time, item, special)

                else:
                    currentSession.updateSession(time, item, special)

            self.sessionRepository.add(currentSession.getSession())


    def readBuyFile(self, filename):
        with open(self.directory + filename, 'r', encoding='utf-8') as f:
            for line in f:
                data = line.split(',')

                id = int(data[0])
                time = datetime.strptime(data[1], "%Y-%m-%dT%H:%M:%S.%fZ")
                item = int(data[2])

                self.itemRepository.addBuyingEvent(item, time.date())
                session = self.sessionRepository.getById(id)

                if session is not None:
                    session.buy = True
                    self.sessionRepository.update(session)


    def getBoughtItemList(self, sessionId):
        boughtItems = []
        with open(self.directory + 'yoochoose-buys.dat', 'r', encoding='utf-8') as f:
            for line in f:
                data = line.split(',')
                if(sessionId == int(data[0])):
                    boughtItems.append(data[2])
        return boughtItems



class SessionCreator:

    id = 0
    numberOfClicks = 0
    buy = False

    startTime = None
    endTime = None
    items = {}

    def __init__(self, id, time, item, special):
        self.id = id
        self.numberOfClicks = 1
        self.duration = 0

        self.startTime = time
        self.endTime = time

        self.items = {}
        self.updateItems(item, special)


    def updateSession(self, time, item, special):
        self.numberOfClicks += 1
        self.updateEndTime(time)
        self.updateItems(item, special)


    def updateItems(self, item, special):
        if self.items.get(item) is None:
            self.items[item] = special


    def updateEndTime(self, time):
        self.endTime = time


    def getElapsedTime(self):
        return (self.endTime - self.startTime).total_seconds()


    def getSession(self):
        return Session(self.id, self.startTime.date(), self.getElapsedTime(), self.numberOfClicks, self.items, self.buy)