class Session:

    id = None
    date = None
    duration = 0
    numberOfClicks = 0
    viewedItems = {}
    buy = False
    
    trendingWeightedValue = 3
    buyingThreashold = 50
    predictedPurchases = []

    def __init__(self, id, date, duration, numberOfClicks, viewedItems, buy):
        self.id = id
        self.date = date
        self.duration = duration
        self.numberOfClicks = numberOfClicks
        self.viewedItems = viewedItems
        self.buy = buy


    def getId(self):
        return self.id


    def isBuyingEvent(self):
        return self.buy


    def getVector(self, itemRepository):
        vector = [self.duration, self.numberOfClicks, len(self.viewedItems)]

        vector.extend(self.getWeightedItemVector(itemRepository))

        return vector

    
    def getWeightedItemVector(self, itemRepository):
        vector = [0] * itemRepository.getCountOfItems()

        for item, trending in self.viewedItems.items():
            pos = itemRepository.getPositionOfItem(item)

            if pos is None:
                continue

            vector[pos] = itemRepository.getCountOfViewsForItemWithin7Days(item, self.date)

            if(trending):
                vector[pos] = vector[pos] + self.trendingWeightedValue

            if vector[pos] > self.buyingThreashold:
                self.predictedPurchases.append(item)

        return vector


    def setViewedItems(self, viewedItems):
        self.viewedItems = viewedItems


    def getPredictedBoughtItems(self):
        return set(self.predictedPurchases)