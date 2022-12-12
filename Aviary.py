class Aviary:
    def __init__(self,name,biome,square):
        self.__name = name
        self.__biome = biome
        self.__square = square
        self.howMuchFood = 0
        self.food = "Рыба", "Мясо","Ягоды","Семена","Трава"

    @property
    def Biome(self):
        return self.__biome

    @property
    def Square(self):
        return self.__square
    
    @property
    def NameAviary(self):
        return self.__name

    def PourFood(self):
        if self.howMuchFood >= 0 and self.howMuchFood <=200:
            self.howMuchFood+=100
            print("В", self.__name, "насыпали еду")

    def HowMuchFood(self):


