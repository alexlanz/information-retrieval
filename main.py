from parser import Parser
from utils import Timer
from scoreBroker import ScoreBroker

timer = Timer()

###############################################################
# Loading files
###############################################################
timer.start()


parser = Parser('data')
parser.readSessionFile('yoochoose-clicks-bg.dat')
parser.readBuyFile('yoochoose-buys.dat')

knowledgeBase = parser.getKnowledgeBase()
scoreBroker = ScoreBroker(knowledgeBase)


testParser = Parser('data')
testParser.readSessionFile('yoochoose-clicks-bh.dat')
testSessions = testParser.getSessionRepository()

print()
print("T E S T ---------------------------------")
print()

for session in testSessions.getAllSessions():

    for itemId, item in session.getItems().items():
        item.score = scoreBroker.calculateScore(item, session)
        if item.score > 100000000:
            item.buy = True
            session.buy = True
            session.updateItem(item)

    testSessions.update(session)

print(str(len(testSessions.getAllBuyingSessions())))

for session in testSessions.getAllBuyingSessions():
    print(session.id)


solutionParser = Parser('data')
solutionParser.readSessionFile('yoochoose-clicks-bh.dat')
solutionParser.readBuyFile('yoochoose-buys.dat')
solutionSessions = solutionParser.getSessionRepository()

print()
print("S O L U T I O N ---------------------------------")
print()

print(str(len(solutionSessions.getAllBuyingSessions())))

for session in solutionSessions.getAllBuyingSessions():
    print(session.id)