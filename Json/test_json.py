import json


class Person:

    def __init__(self) -> None:
        self.name = ""
        self.firstname = ""




if __name__ == "__main__":

    p1 = Person()
    p1.name = "Vercoutere"
    p1.firstname = "Wesley"

    p2 = Person()
    p2.name = "De Letter"
    p2.firstname = "Vanessa"

    out = json.dumps(p1.__dict__)
    print(out)

    persons = list()
    persons.append(p1)
    persons.append(p2)

    out2 = json.dumps([p.__dict__ for p in persons])
    print(out2)
