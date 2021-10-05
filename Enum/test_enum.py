from enum import Enum


class Resource(Enum):

    HTML = ("html", "test 1")
    PNG = ("png", "test 2")
    JPG = ("jpg", "test 3")

    def __init__(self, type, type2) -> None:
        self.type = type
        self.type2 = type2

    def get_type(self) -> str:
        return self.type

    def get_type2(self) -> str:
        return self.type2
        
resource1 = Resource.HTML
print(resource1.get_type())


print(Resource.HTML.value)


resource2 = Resource["PNG"]
print(resource2.get_type())

resource3 = Resource("jpg")
print(resource3.get_type())
