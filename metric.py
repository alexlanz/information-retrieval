from parser import Parser

class Metric:
    
    SL = None
    S = None
    Sb = None
    
    fileManager = None
    
    def __init__(self, SL, S):
        self.SL = SL
        self.S = S
        self.Sb = S.getAllBuyingSessions()
        self.fileManager = Parser()
        
    def calculateScore(self):
        score = 0
        scoreValue = len(self.Sb) / self.S.getNumberOfSessions()
        
        for s in self.SL:
            if self.sessionContainedInBuyingEvents(s.getId(), self.Sb):
                As = s.getPredictedBoughtItems()
                Bs = self.getActualBoughtItems(s.getId())
                score = score + scoreValue + (len(As.intersection(Bs)) / len(As.union(Bs)))
            else:
                score = score - scoreValue
                
        return score

    def sessionContainedInBuyingEvents(self, sId, Sb):
        for buyingSession in Sb:
            if buyingSession.getId() == sId:
                return True
        return False

    def getActualBoughtItems(self, sId):
        boughtItems = self.fileManager.getBoughtItemList(sId)
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
    
    