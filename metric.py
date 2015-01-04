from parser import Parser

class Metric:
    
    # SL ... sessions in solution file
    # S  ... sessions in test set
    # s  ... single session in the test set
    # Sb ... sessions in the test set which end with buy
    # As ... predicted bought items in session s
    # Bs ... actual bought items in session s
    
    SL = None
    S = None
    Sb = None
    parser = None
    
    def __init__(self, SL, S):
        self.SL = SL
        self.S = S
        self.Sb = S.getAllBuyingSessions()
        self.parser = Parser()
        
    def calculateScore(self):
        score = 0
        scoreValue = len(self.Sb) / self.S.getNumberOfSessions()
        
        for s in self.SL:
            if self.sessionContainedInBuyingEvents(s.getId()):
                As = s.getPredictedBoughtItems()
                Bs = self.getActualBoughtItems(s.getId())
                score = score + scoreValue + (len(As.intersection(Bs)) / len(As.union(Bs)))
            else:
                score = score - scoreValue
                
        return score

    def sessionContainedInBuyingEvents(self, sId):
        for buyingSession in self.Sb:
            if buyingSession.getId() == sId:
                return True
        return False

    def getActualBoughtItems(self, sId):
        boughtItems = self.parser.getBoughtItemList(sId)
        return set(boughtItems)

    def getRecallScore(self):
        relevantInstances = 0
        allRelevantInstances = 0
        for s in self.SL:
            if self.sessionContainedInBuyingEvents(s.getId(), self.Sb):
                As = s.getPredictedBoughtItems()
                Bs = self.getActualBoughtItems(s.getId())
                relevantInstances = relevantInstances + len(As.intersection(Bs))
                allRelevantInstances = allRelevantInstances + len(Bs)
        return (relevantInstances / allRelevantInstances)
    
    def getPrecisionScore(self):
        relevantInstances = 0
        foundInstances = 0
        for s in self.SL:
            if self.sessionContainedInBuyingEvents(s.getId(), self.Sb):
                As = s.getPredictedBoughtItems()
                Bs = self.getActualBoughtItems(s.getId())
                relevantInstances = relevantInstances + len(As.intersection(Bs))
                foundInstances = foundInstances + len(As)
        return (relevantInstances / foundInstances)
    
    