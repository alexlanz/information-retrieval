class Session:

    id = None
    date = None
    duration = 0               # Integer in seconds
    numberOfClicks = 0
    viewedItems = {}
    buy = False
    
    trendingWeightedValue = 3

    def __init__(self, id, date, duration, numberOfClicks, viewedItems, buy):
        self.id = id
        self.date = date
        self.duration = duration
        self.numberOfClicks = numberOfClicks
        self.viewedItems = viewedItems
        self.buy = buy

    def getVector(self, items):
        return [self.duration, self.numberOfClicks, self.numberOfItems] + self.getWeightedItemVector(items)
    
    def getWeightedItemVector(self, items):
        arr = [0] * items.getCountOfItems();
        for itemId, trending in self.viewedItems:
            pos = items.getPositionOfItem(itemId)
            arr[pos] = items.getCountOfViewsForItemWithin7Days(itemId, self.date)
            if(trending):
                arr[pos] = arr[pos] + self.trendingWeightedValue
        return arr

    def isBuyingEvent(self):
        return self.buy
    
    def getId(self):
        return self.id
    
    def setViewedItems(self, viewedItems):
        self.viewedItems = viewedItems