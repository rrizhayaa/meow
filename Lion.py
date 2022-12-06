class Lion:

    def __init__(self, name, age, volumeFood):
        self.Name = name
        self.Age = age
        self.VolumeFood = volumeFood
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
