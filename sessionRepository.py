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


    def getAllVectors(self):
        vectors = []

        for id, session in self.sessions.items():
            vectors.append(session.getVector())

        return vectors


    def getAllBuyingLabels(self):
        labels = []

        for id, session in self.sessions.items():
            labels.append((1 if session.isBuyingEvent() else 0))

        return labels
    
    
    def getAllBuyingSessions(self):
        buyingSessions = []     
        for session in self.sessions.values():
            if session.isBuyingEvent():
                buyingSessions.append(session)
        return buyingSessions
    
    
    def getNumberOfSessions(self):
        return len(self.sessions.keys())