class SingletonNew:

    __instance = None
    counter = 0

    def __new__(self):
        if SingletonNew.__instance == None:

            print('Create new instance')
            SingletonNew.__instance = object.__new__(self)

        return SingletonNew.__instance


    def add(self):
        self.counter += 1
