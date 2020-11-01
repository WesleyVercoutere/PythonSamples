from tkinter import *
import threading

dummyroot = Tk()
dummyroot.title("Raspberry Pi dummy GPIO")
dummyroot.geometry("400x200")

# frameInput = LabelFrame(dummyroot, text="Inputs")
# frameOutput = LabelFrame(dummyroot, text="Outputs")

# frameInput.pack()
# frameOutput.pack()

test = Label(dummyroot, text="test")
test.pack()


def runDummyLoop():
    dummyroot.mainloop()

threading.Thread(target=runDummyLoop).start()

