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
        self._impl.create_menus = lambda *x, **y: None

        self.main_box = toga.Box()

        btn = toga.Button('Click me', on_press=self.btnClicked)
        self.main_box.add(btn)

        self.main_window = toga.MainWindow(title=None)
        self.main_window.content = self.main_box
        self.main_window.show()
        
    def btnClicked(self, arg):
        self.main_window.info_dialog('Happiness', 'I know, right! :-)')


def main():
    return HelloWorld()
