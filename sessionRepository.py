class SessionRepository:

    sessions = {}

    def __init__(self):
        self.sessions = {}


    def add(self, session):
        self.sessions[session.id] = session
        return self.sessions[session.id]


    def update(self, session):
        return self.add(session)


    def getAll(self):
        return self.sessions


    def getById(self, id):
        return self.sessions[id]





