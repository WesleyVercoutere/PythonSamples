from tkinter import *
import time
import threading
import multiprocessing


class ThreadApp():

    def __init__(self):
        self.root = Tk()
        self.root.title("Test maximize screen")
        self.root.state('zoomed')

        self.counter1 = 0
        self.counter2 = 0

        self.lblCounter1 = Label(self.root, text=f"Counter 1 : {self.counter1}")
        self.lblCounter2 = Label(self.root, text=f"Counter 2 : {self.counter2}")

        self.lblCounter1.grid(row = 0, column = 0, padx = 20, pady = 20)
        self.lblCounter2.grid(row = 1, column = 0, padx = 20, pady = 20)

        threading.Thread(target=self.runCounter1).start()
        threading.Thread(target=self.runCounter2).start()

        self.root.mainloop()
    
    def runCounter1(self):
        while True:
            self.counter1 = self.updateCounter(self.counter1, 1)
            self.lblCounter1.config(text=self.counter1)

    def runCounter2(self):
        while True:
            self.counter2 = self.updateCounter(self.counter2, 5)
            self.lblCounter2.config(text=self.counter2)

    def updateCounter(self, counter, sleep):
        counter += 1
        time.sleep(sleep)

        return counter

if __name__ ==  '__main__':
    ThreadApp()
