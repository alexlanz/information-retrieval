class Item:

    id = None
    category = None
    views = 0
    buy = False
    score = 0

    def __init__(self, id, category, views, buy, score):
        self.id = id
        self.category = category
        self.views = views
        self.buy = buy
        self.score = score


    def incrementViews(self):
        self.views += 1





