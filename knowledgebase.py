from datetime import timedelta

class KnowledgeBase:

    checkouts = None
    categories = None

    def __init__(self):
        self.checkouts = {}
        self.categories = {}


    def addBuyEvent(self, item, day, category):
        if item in self.checkouts:
            self.checkouts[item].append(day)

        if category in self.categories:
            self.categories[category].append(day)


    def addSessionEvent(self, itemId, category):
        self.checkouts[itemId] = []
        self.categories[category] = []


    def getCountOfBuysForItemWithinDays(self, item, days, endDay):
        startDay = endDay - timedelta(days=days)

        numberOfBuys = 0

        for day in self.checkouts[item]:
            if startDay <= day <= endDay:
                numberOfBuys += 1

        return numberOfBuys


    def getCountOfCategoryBuys(self, category, days, endDay):
        startDay = endDay - timedelta(days=days)

        numberOfBuys = 0

        for day in self.categories[category]:
            if startDay <= day <= endDay:
                numberOfBuys += 1

        return numberOfBuys




