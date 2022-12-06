from Classes import *

class DogAnimal(Classes):

    def __init__(self,name):
        super().__init__("Dog",name)
        self.__sound = "Гав-гав"
