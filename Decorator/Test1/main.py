from Server import Server


if __name__ == "__main__":

    

    app = Server()

    @app.route("/", "/home")
    def get_index():
        print("Serving index page")

    @app.route("/about")
    def get_about():
        print("Return about page")

    print()
    print(app.get_routes())
    print()


    app.request("/")
    app.request("/home")
    app.request("/about")
