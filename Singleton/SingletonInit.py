class SingletonInit:

    __instance = False
    __counter = 0

    def __init__(self):
        if not self.__instance:
            self.__instance = True
            self.__instance = SingletonInit()

    
    def get_instance(self):
        return self.__instance

    def add(self):
        self.__counter += 1

        return self.__counter
