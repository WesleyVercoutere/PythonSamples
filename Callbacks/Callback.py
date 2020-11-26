import threading
import time

class Callback:

    def __init__(self):
        pass

    def add_event_detect(self, time, callback):
        threading.Thread(target=self.runEvent, args=(time, callback)).start()


    def runEvent(self, *args):
        loopTime = args[0]
        callback = args[1]

        startTime = time.time()

        while True:
            currentTime = time.time()

            if currentTime >= startTime + loopTime:
                startTime = time.time()
                callback(loopTime)
