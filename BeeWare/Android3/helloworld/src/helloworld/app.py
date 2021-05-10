"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class HelloWorld(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        label = toga.Label('Hello World')
        label2 = toga.Label('Hello World again')

        btn1 = toga.Button('Testje')

        main_box.add(label)
        main_box.add(label2)
        main_box.add(btn1)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return HelloWorld()
