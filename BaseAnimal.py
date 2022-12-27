class BaseAnimal:
    def __init__(self, Name, Age, FoodTypes, Biome, Square, Type, VolumeFood, Sigh, Sound):
        self.__name = Name
        self.__age = Age
        self.__foodTypes = FoodTypes
        self.__type = Type
        self.__biome = Biome
        self.__square = Square
        self.__vegan = isVegan
        self.__volumeFood = VolumeFood
        self.__sound = Sound
        self.__aviary = 0
        self.__happiness = 50
        self.__satiety = 50

    @property
    def name(self):
        return self.__name

    @property
    def square(self):
        return self.__square

    @property
    def age(self):
        return self.__age

    @property
    def isVegan(self):
        return self.__vegan

    @age.setter
    def age(self, value):
        if (value is int) and (value >= 0):
            self.__age = value
            print("Теперь возраст",self.__name, self.__age)
        else:
            print("Нельзя ввести такой возраст")

    @property
    def type(self):
        return self.__type

    @property
    def foodTypes(self):
        return self.__foodTypes

    @property
    def biome(self):
        return self.__biome

    @property
    def volumeFood(self):
        return self.__volumeFood

    @property
    def aviary(self):
        return self.__aviary

    @aviary.setter
    def aviary(self, aviary):
        self.__aviary = aviary

    @property
    def square(self):
        return self.__square

    @square.setter
    def square(self, value):
        self.__square = value

    @property
    def happiness(self):
        return self.__happiness

    @happiness.setter
    def happiness(self, value):
        if self.__happiness > 100:
            self.__happiness = 100
        elif self.__happiness < 0:
            self.__happiness = 0
        else:
            self.__happiness = value

    @property
    def satiety(self):
        return self.__satiety

    @satiety.setter
    def satiety(self, value):
        if self.__satiety > 100:
            self.__satiety = 100
        elif self.__satiety < 0:
            self.__satiety = 0
        else:
            self.__satiety = value

    def Eat(self, foodType, value):
        variable = value/self.__volumeFood * 100
        if (foodType in self.__foodTypes) and (variable + self.__satiety <= 100):
            self.__satiety += variable
            print("Я покушал", foodType)
            print("Теперь моя сытость:", self.__satiety)
        elif not(foodType in self.__foodTypes):
            print(self.__name, ": Я не ем", foodType)
        elif variable + self.__satiety > 100:
            remainsSatiety = 100 - self.__satiety
            self.__satiety += remainsSatiety
            remainsValue = ((variable - remainsSatiety)/100) * self.__volumeFood
            print("Я наелся, теперь моя сытость:", self.__satiety)
            print("Остаток добавленной еды:", remainsValue)

    def Play(self):
        if self.__happiness <= 70:
            self.__happiness += 30
            print(self.__name, ": Я поиграл :З", self.__sound)
        else:
            print(self.__name, ": Я уже наигрался")

    def DoSound(self, quantity):
        for i in range(quantity):
            print(self.__name, self.__sound)
