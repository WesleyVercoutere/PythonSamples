import json


class Person:

    def __init__(self) -> None:
        self.name = ""
        self.firstname = ""



if __name__ == "__main__":

    p1 = Person()
    p1.name = "Vercoutere"
    p1.firstname = "Wesley"

    out = json.dumps(p1.__dict__)
    print(out)
