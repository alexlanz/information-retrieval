from parser import Parser
from session import Session
from sessionRepository import SessionRepository
from utils import Timer
from sklearn.neighbors import KNeighborsClassifier
from itemRepository import ItemRepository

timer = Timer()

###############################################################
# Loading files
###############################################################
timer.start()


parser = Parser('data')
parser.readSessionFile('yoochoose-clicks-aa.dat')
#parser.readSessionFile('yoochoose-clicks-ab.dat')
#parser.readSessionFile('yoochoose-clicks-ac.dat')
#parser.readSessionFile('yoochoose-clicks-ad.dat')
#parser.readSessionFile('yoochoose-clicks-ae.dat')
#parser.readSessionFile('yoochoose-clicks-af.dat')

sessionRepository = parser.readBuyFile('yoochoose-buys.dat')

sessionRepository = parser.getSessionRepository()
itemRepository = parser.getItemRepository()

timer.stop()
print("Time for loading files: " + timer.getElapsedSecondsString())

#sessions = sessionRepository.getAllSessions()
#session = sessionRepository.getById(327676)
#print(session.getVector(items))

#for session in sessions:
#    print(str(session.id) + ', ' + str(session.duration) + " sec, " + str(session.numberOfClicks) + " clicks, BUY: " + str(session.buy))


###############################################################
# Training
###############################################################
timer.start()

X = sessionRepository.getAllVectors(itemRepository)
y = sessionRepository.getBuyingEventsVector()

neigh = KNeighborsClassifier(n_neighbors=1)
neigh.fit(X, y)

timer.stop()
print("Time for training: " + timer.getElapsedSecondsString())


###############################################################
# Predicting
###############################################################
timer.start()

parserTest = Parser('data')
parserTest.readSessionFile('yoochoose-clicks-ax.dat')

sessionRepositoryTest = parserTest.getSessionRepository()
X = sessionRepositoryTest.getAllVectors(itemRepository)

predictions = neigh.predict(X)

timer.stop()
print("Time for predicting: " + timer.getElapsedSecondsString())

print("Predictions:")
print("------------")
print(predictions)