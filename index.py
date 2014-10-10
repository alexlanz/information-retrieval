class Term:
    
    name = ""
    frequency = 0
    hits = []

    def __init__(self, name):
        self.name = name
        self.hits = []


    def addHit(self, document, rank):
        hit = Hit(document, rank)
        self.hits.append(hit)


class Hit:
    
    document = ""
    rank = None

    def __init__(self, document, rank):
        self.document = document
        self.rank = rank