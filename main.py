from fileManager import FileManager
from sessionRepository import SessionRepository
from utils import Timer

fileManager = FileManager('data')
timer = Timer()

timer.start()

print("Start loading clicks file ... ")
sessionRepository = SessionRepository()
sessionRepository = fileManager.readSessionFile('yoochoose-clicks-aa.dat', sessionRepository)
sessionRepository = fileManager.readBuyFile('yoochoose-buys.dat', sessionRepository)

timer.stop()

sessions = sessionRepository.getAll()
#session = sessionRepository.getById(11299813)

for key, session in sessions.items():
    print(str(session.id) + ', ' + str(session.duration) + " sec, " + str(session.numberOfItems) + " items, " + str(session.numberOfClicks) + " clicks, SPECIAL: " + str(session.special) + ", BUY: " + str(session.buy))

print("Done loading clicks file in " + timer.getElapsedSecondsString())
