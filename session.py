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



