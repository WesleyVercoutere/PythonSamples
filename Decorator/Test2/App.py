from Server import Server
from Service import Service
from Controller import Controller


class App:

    def __init__(self) -> None:
        self.app = Server()
        service = Service()
        ctrl = Controller(self.app, service)

        print()
        print(self.app.get_routes())
        print()

    def run(self):
        self.app.request("/")
        self.app.request("/home")
        self.app.request("/about")
