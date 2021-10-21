
class Led:

    Id = 0

    def __init__(self, pin, color) -> None:
        Led.Id += 1
        
        self.id = Led.Id
        self.pin = pin
        self.color = color

    def __str__(self) -> str:
        return (f"{Led.Id} - {self.id} - {self.pin} - {self.color}")


if __name__ == "__main__":
    
    led1 = Led(10, "Rood")
    print(led1)

    led2 = Led(20, "blauw")
    print(led2)
    print(led1)
