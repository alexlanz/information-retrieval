from sessionRepository import SessionRepository
from fileManager import FileManager

#input: the repository containing the predictions from Alex
repository = SessionRepository()
SL = repository.getAllSessions()

#use importer from Martin to import test sessions from file
S = SessionRepository() 
fileManager = FileManager('data')
S = fileManager.readSessionFile('yoochoose-test.dat', S)
Sb = S.getAllBuyingSessions()

scoreValue = len(Sb) / S.getNumberOfSessions()
score = 0

def sessionContainedInBuyingEvents(sID, Sb):
    for buyingSession in Sb:
        if buyingSession.getId() == s.getId():
            return True
    return False


#calculate score
for s in SL:
    if sessionContainedInBuyingEvents(s.getId(), Sb):
        As = s.getPredictedBoughtItems()
        
        #todo woher bekomme ich die actualBought Items ??
        Bs = s.getActualBoughtItems()
        score = score + scoreValue + (len(As.intersection(Bs)) / len(As.union(Bs)))
    else:
        score = score - scoreValue
        
print(score)