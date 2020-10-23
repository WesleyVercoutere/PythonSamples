from tkinter import * 
from View import *

root = Tk()
root.title("Test maximize screen")
root.state('zoomed')

v = View(root)

def main():
    root.mainloop()

if __name__ == "__main__":
    main()