class ScoreBroker:

    knowledgeBase = None
    buyWeight = 100
    categoryWeight = 0.1

    def __init__(self, knowledgeBase):
        self.knowledgeBase = knowledgeBase

    def calculateScore(self, item, session):
        buyCount = self.knowledgeBase.getCountOfBuysForItemWithinDays(item.id, 7, session.day) * self.buyWeight
        categoryCount = self.knowledgeBase.getCountOfCategoryBuys(item.category, 7, session.day) * self.categoryWeight
        score = buyCount * categoryCount * item.views
        return score

