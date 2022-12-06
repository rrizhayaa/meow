class BaseAviary:
    def __init__(self,name,biome,square):
        self.__name = ""
        self.__biome = biome
        self.__square = square
        self.howMuchFood = 0
        self.feederSize = ''

    @property
    def Biome(self):
        return self.__biome

    @property
    def Square(self):
        return self.__square

    def NameAviary(self):
        if self.__square <= 15:
            self.__name = "Маленький вольер"
        if self.__square >=16 and self.__square <=30:
            self.__name = "Средний вольер"
        if self.__square >=30 and self.__square <=50:
            self.__name = "Большой вольер"

    def PourFood(self):
        if self.howMuchFood <=
        self.howMuchFood+=100
        print("В", self.__name, "насыпали еду")

    def HowMuchFood(self):


