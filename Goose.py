class Goose:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.volumeFood = 15
        self.type = ["Гусь"]
        self.biome = ["Луг"]
        self.square = 10
        self.foodTypes = ["Трава", "Семена", "Ягоды"]
        self.sign = ["Травоядное"]
        self.sound = ["Га-га-га"]
        self.satiety = 50
        self.happiness = 50

    def DoSound(self, quantity):
        for i in range(quantity):
            print(self.name, self.sound)

    def Eat(self, foodType):
        if (foodType in self.foodTypes):
            print(self.name, ": Я покушал", foodType)
        else:
            print(self.name, ": Я не ем", foodType)

    def Play(self):
        if self.happiness <= 70:
            self.happiness += 30
            print(self.name, ": Я поиграл :З", self.sound)
        else:
            print(self.name, ": Я уже наигрался")

    @property
    def Age(self):
        return self.__age

    @Age.setter
    def Age(self,value):
        if(value is int) and (value>=0):
            self.__age = value
            print("Теперь мой возраст", self.__age)
        else:
            print("Нельзя ввести такой возраст")

    @property
    def Name(self):
        return self.__name
