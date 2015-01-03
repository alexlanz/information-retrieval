class Session:

    id = None
    date = None
    duration = 0               # Integer in seconds
    numberOfClicks = 0
    viewedItems = []
    buy = False

    def __init__(self, id, date, duration, numberOfClicks, buy):
        self.id = id
        self.date = date
        self.duration = duration
        self.numberOfClicks = numberOfClicks
        self.buy = buy

    def getVector(self):
        return [self.duration, self.numberOfClicks, self.numberOfItems, (1 if self.special else 0)] + self.getWeightedItemVector()
    
    def getWeightedItemVector(self):
        arr = []
        #todo
        return arr

    def isBuyingEvent(self):
        return self.buy
    
    def getId(self):
        return self.id
    
    def setViewedItems(self, viewedItems):
        self.viewedItems = viewedItems