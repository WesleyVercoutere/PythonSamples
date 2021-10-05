from Server import Server
from Service import Service


class Controller:

    def __init__(self, app: Server, service: Service) -> None:
        self.app = app
        self.service = service

        self._register_routes()

    def _register_routes(self):
        
        @self.app.route("/", "/home")
        def get_index():
            self.service.get_index()

        @self.app.route("/about")
        def get_about():
            self.service.get_about()
