import time

class Timer:

    startTime = 0
    endTime = 0

    def __init__(self):
        self.startTime = 0
        self.endTime = 0


    def start(self):
        self.startTime = time.time()


    def stop(self):
        self.endTime = time.time()


    def getElapsedTime(self):
        return self.endTime - self.startTime


    def getElapsedTimeInMilliseconds(self):
        seconds = self.getElapsedTime()
        milliseconds = seconds * 1000
        return milliseconds


    def getElapsedSecondsString(self):
        time = self.getElapsedTime()
        return "{0:.4f} s".format(time)


    def getElapsedMillisecondsString(self):
        time = self.getElapsedTimeInMilliseconds()
        return "{0:.4f} ms".format(time)