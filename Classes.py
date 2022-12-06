class BaseAnimal:
    def __init__(self,type,name):
        self.__type = type
        self.name = name
        self.__sound = ""

    @property
    def Type(self):
        return self.__type

    def DoSound(self):
        print (self.name, "сказал", self.__sound)