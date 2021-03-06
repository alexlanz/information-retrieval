from datetime import date, timedelta

class ItemRepository:

    items = None
    itemPositions = None

    def __init__(self):
        self.items = {}
        self.itemPositions = None


    def addItem(self, item):
        self.itemPositions = None

        if item not in self.items:
            self.items[item] = []


    def addBuyingEvent(self, item, day):
        if item in self.items:
            self.items[item].append(day)


    def getCountOfItems(self):
        self.lockItemPositions()
        return len(self.itemPositions)


    def getPositionOfItem(self, item):
        self.lockItemPositions()

        if item not in self.itemPositions:
            return None

        return self.itemPositions.index(item)


    def getCountOfViewsForItemWithin7Days(self, item, endDay):
        startDay = endDay - timedelta(days=7)

        numberOfViews = 0

        for day in self.items[item]:
            if startDay <= day <= endDay:
                numberOfViews += 1

        return numberOfViews


    def lockItemPositions(self):
        if self.itemPositions is None:
            self.itemPositions = list(self.items)