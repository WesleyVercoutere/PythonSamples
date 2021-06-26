"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class HelloWorld(toga.App):

    def __init__(
            self,
            formal_name=None,
            app_id=None,
            app_name=None,
            id=None,
            icon=None,
            author=None,
            version=None,
            home_page=None,
            description=None,
            startup=None,
            on_exit=None,
            factory=None,
    ):
        super().__init__(formal_name, app_id, app_name, id, icon, author, version, home_page, description, startup,
                         on_exit, factory)
        self.name_input = None

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label(
            'Your name: ',
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            'Say Hello!',
            on_press=self.say_hello,
            style=Pack(padding=5)
        )

        main_box.add(name_box)
        main_box.add(button)

        label = toga.Label('Hello World')
        label2 = toga.Label('Hello World again')

        btn1 = toga.Button('Testje')

        main_box.add(label)
        main_box.add(label2)
        main_box.add(btn1)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, widget):
        print("Hello", self.name_input.value)


def main():
    return HelloWorld()
