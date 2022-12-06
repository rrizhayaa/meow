class Lion:

    def __init__(self, name, age):
        self.__Name = name
        self.__Age = age
        self.VolumeFood = 25
        self.Type = ["Лев"]
        self.Biome = ["Саванна"]
        self.Square = 25
        self.FoodTypes = ["Рыба", "Мясо"]
        self.Sign = ["Хищник"]
        self.Sound = ["Ррр"]
        self.Happiness = 50

    def DoSound(self, quantity):
        for i in range(quantity):
            print(self.Name, self.Sound)

    def Eat(self, foodType):
        if (foodType in self.FoodTypes):
            print(self.Name, ": Я покушал", foodType)
        else:
            print(self.Name, ": Я не ем", foodType)

    def Play(self):
        if self.Happiness <= 70:
            self.Happiness += 30
            print(self.Name, ": Я поиграл :З", self.Sound)
        else:
            print(self.Name, ": Я уже наигрался")

    @property
    def Age(self):
        return self.__Age

    @Age.setter
    def Age(self,value):
        if(value is int) and (value>=0):
            self.__Age = value
            print("Теперь мой возраст", self.__Age)
        else:
            print("Нельзя ввести такой возраст")

    @property
    def Name(self):
        return self.__Name
