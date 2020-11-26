from Callback import *

class TestCallback:

    def __init__(self):
        cb = Callback()
        cb.add_event_detect(1, callback=self.update)
        cb.add_event_detect(2, callback=self.update)
        cb.add_event_detect(5, callback=self.update)
        cb.add_event_detect(10, callback=self.update)

    
    def update(self, time):
        print(f"updating {time} sec loop")
    


if __name__ == "__main__":
    tc = TestCallback()
