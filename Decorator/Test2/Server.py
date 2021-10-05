class Server:

    def __init__(self) -> None:
        self._routes = dict()

    def route(self, *routes):

        def wrapper(f):
            for route in routes:
                print(f"Register route: {route}")

                self._routes[route] = f
        
        return wrapper
        
    def request(self, route):
        print(f"Request : {route}")

        for path, handler in self._routes.items():
            if path == route:
                handler()

    def get_routes(self):
        return self._routes
