class SessionRepository:

    sessions = {}

    def __init__(self):
        self.sessions = {}


    def add(self, session):
        self.sessions[session.id] = session
        return self.sessions[session.id]


    def update(self, session):
        return self.add(session)


    def getAllSessions(self):
        return self.sessions.values()


    def getById(self, id):
        return self.sessions.get(id)


    def getAllVectors(self, itemRepository):
        vectors = []

        for id, session in self.sessions.items():
            vector = session.getVector(itemRepository)
            vectors.append(vector)

        return vectors


    def getBuyingEventsVector(self):
        vector = []

        for id, session in self.sessions.items():
            vector.append((1 if session.isBuyingEvent() else 0))

        return vector
    
    
    def getAllBuyingSessions(self):
        buyingSessions = []     
        for session in self.sessions.values():
            if session.isBuyingEvent():
                buyingSessions.append(session)
        return buyingSessions
    
    
    def getNumberOfSessions(self):
        return len(self.sessions.keys())