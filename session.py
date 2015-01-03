class Session:

    id = None
    duration = 0               # Integer in seconds
    numberOfClicks = 0
    numberOfItems = 0
    special = False
    buy = False

    def __init__(self, id, duration, numberOfClicks, numberOfItems, special, buy):
        self.id = id
        self.duration = duration
        self.numberOfClicks = numberOfClicks
        self.numberOfItems = numberOfItems
        self.special = special
        self.buy = buy

    def getVector(self):
        return [self.duration, self.numberOfClicks, self.numberOfItems, (1 if self.special else 0)]

    def isBuyingEvent(self):
        return self.buy
    
    def getId(self):
        return self.id