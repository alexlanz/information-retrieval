from session import Session
from sessionRepository import SessionRepository
from knowledgebase import KnowledgeBase
from datetime import datetime
from item import Item

class Parser:

    directory = ""
    knowledgeBase = None
    sessionRepository = None

    def __init__(self, directory):
        if not directory.endswith('/'):
            directory += "/"

        self.directory = directory
        self.knowledgeBase = KnowledgeBase()
        self.sessionRepository = SessionRepository()


    def readSessionFile(self, filename):
        currentSession = None

        with open(self.directory + filename, 'r', encoding='utf-8') as f:

            for line in f:

                data = line.split(',')

                id = int(data[0])
                day = datetime.strptime(data[1], "%Y-%m-%dT%H:%M:%S.%fZ")
                item = int(data[2])
                category = data[3].strip()

                self.knowledgeBase.addSessionEvent(item, category)

                if currentSession is None:
                    currentSession = SessionCreator(id, item, day, category)

                elif currentSession.id != id:
                    self.sessionRepository.add(currentSession.getSession())
                    currentSession = SessionCreator(id, item, day, category)

                else:
                    currentSession.updateItems(item, category)

            self.sessionRepository.add(currentSession.getSession())



    def readBuyFile(self, filename):
        with open(self.directory + filename, 'r', encoding='utf-8') as f:
            for line in f:
                data = line.split(',')

                id = int(data[0])
                time = datetime.strptime(data[1], "%Y-%m-%dT%H:%M:%S.%fZ")
                item = int(data[2])

                self.sessionRepository.addBuyEvent(id, item)
                if id in self.sessionRepository.sessions:
                    self.knowledgeBase.addBuyEvent(item, time, self.sessionRepository.getById(id).getItems()[item].category)


    def getBoughtItemList(self, sessionId):

        with open(self.directory + 'yoochoose-buys.dat', 'r', encoding='utf-8') as f:
            for line in f:
                data = line.split(',')
                if(sessionId == int(data[0])):
                    boughtItems.append(data[2])
        return boughtItems


    def getSessionRepository(self):
        return self.sessionRepository


    def getKnowledgeBase(self):
        return self.knowledgeBase



class SessionCreator:

    id = 0
    day = None
    items = {}

    def __init__(self, id, item, day, category):
        self.id = id
        self.day = day
        self.items = {}
        self.updateItems(item, category)


    def updateItems(self, item, category):
        if self.items.get(item) is None:
            self.items[item] = Item(item, category, 0, False, 0)

        self.items[item].incrementViews()


    def getSession(self):
        return Session(self.id, self.day, self.items)