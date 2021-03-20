class Test1:

    def __init__(self, test2):
        self.test2 = test2

    def doSomething(self):
        print("Call method from Test2")
        test2.method(self.endSomething)

    def endSomething(self, arg):
        print(f"Called from Test 2 as callback with param : {arg}")


class Test2:

    def __init__(self):
        self.callback = None

    def method(self, callback):
        print("Execute method in Test 2")
        self.callback = callback

        self.method2()

    def method2(self):
        self.callback("Ook gelukt!")

if __name__ == "__main__":

    test2 = Test2()
    test1 = Test1(test2)
    test1.doSomething()