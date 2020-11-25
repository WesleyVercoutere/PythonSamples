from SingletonNew import *


class TestSingleton():

    def __init__(self):
        
        self.singleton1 = SingletonNew()
        self.singleton1.add()
        print(self.singleton1.counter == 1)
        self.singleton1.add()
        print(self.singleton1.counter == 2)

        self.singleton2 = SingletonNew()
        self.singleton2.add()
        print(self.singleton2.counter == 3)
        self.singleton2.add()
        print(self.singleton2.counter == 4)
        







if __name__ == '__main__':
    t = TestSingleton()