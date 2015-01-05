class Session:

    id = None
    day = None
    items = None
    buy = False

    def __init__(self, id, day, items):
        self.id = id
        self.day = day
        self.items = items
        self.buy = False


    def getId(self):
        return self.id


    def getItems(self):
        return self.items


    def getBoughtItems(self):
        boughtItems = []
        for itemId, item in self.items.items():
            if item.buy:
                boughtItems.append(itemId)

        return boughtItems


    def setItems(self, items):
        self.items = items


    def getPredictedBoughtItems(self):
        return set(self.predictedPurchases)


    def addBuyEvent(self, item):
        self.buy = True
        self.items[item].buy = True


    def updateItem(self, item):
        self.items[item.id] = item