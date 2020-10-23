from tkinter import *

class View():

    def __init__(self, root):
        self._root = root
        self._setButton()

    def _setButton(self):
        self.button = Button(self._root)
        self.button.config(text = 'Click')
        self.button.pack()