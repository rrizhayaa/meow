class Goose:

    def __init__(self, name, age, volumeFood):
        self.__Name = name
        self.__Age = age
        self.VolumeFood = volumeFood
        self.Type = ["Гусь"]
        self.Biome = ["Луг"]
        self.Square = 10
        self.FoodTypes = ["Трава", "Семена", "Ягоды"]
        self.Sign = ["Травоядное"]
        self.Sound = ["Га-га-га"]
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
            print(self.Name, ": Я поиграл :З")
        else:
            print(self.Name, ": Я уже наигрался")

    @property
    def Age(self):
        return self.__Age

    @Age.setter
    def Age(self,value):
        if(value is int) and (value>=0):
            self.__Age = value
        else:
            print("Нельзя ввести такой возраст")

    @property
    def Name(self):
        return self.__Name
