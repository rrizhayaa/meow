class Aviary:

    def __init__(self, Name, Biome, Square):
        self.__name = Name
        self.__biome = Biome
        self.__square = Square
        self.__animals = []
        self.__vegan = 0
        self.__food = []
        self.__amountOfFood = 100
        self.__type = 0

    @property
    def name(self):
        return self.__name

    @property
    def biome(self):
        return self.__biome

    @property
    def square(self):
        return self.__square

    @property
    def animals(self):
        return self.__animals

    @property
    def food(self):
        return self.__food

    def type(self, Animal):
        if Animal.Type == "Мирный" and self.__animals[0].Type == "Мирный":
            self.__type = "Мирный"
        else:
            print("Животные не являются одним типом")

        if Animal.Type == "Хищник" and self.__animals[0].Type == "Хищник":
            self.__type = "Хищник"
        else:
            print("Животные не являются одним типом")

    def isVegan(self, Animal):
        if Animal.isVegan and self.__animals[0].isVegan:
            self.__vegan = "Травоядные"
        else:
            self.__vegan = "Не травоядные"

    def addAnimal(self, Animal):
        if Animal.Aviary:
            print (Animal, "уже находится в вольере", self.__name)

        if not(Animal.Biome == self.__biome):
            print("Вольер", self.__name, "не подходит для животного:", Animal.Type)

        if not(self.__square >= Animal.Square):
            print("В вольере", self.__name, "не хватает места для животного", Animal.Type)

        if (not(Animal.isVegan) and (self.__animals[0].isVegan)):
            print("Животное", Animal.Type, "не сочетается с животными в вольере")

        if (Animal.Type == "Хищник") and not(self.__animals[0].Type == "Хищник"):
            print("Животное", Animal.Type, "не сочетается с животными в вольере", self.__name)


        self.__animals.append(Animal)
        self.__square -= Animal.square
        Animal.aviary = self
        print(Animal.name, "добавлен в вольер", self.__name)

    def removeAnimal(self, Animal):
        if not(Animal.aviary == self):
            print(Animal.name, "не находится в вольере", self.__name)

        self.__animals.remove(Animal)
        Animal.aviary = 0
        self.__square += Animal.square
        print(Animal.name, "больше не находится в вольере", self.__name)

    def doSound(self, Animal):
        if len(self.__animals) == 0:
            print("В вольере", self.__name, "нет животных, чтобы издать звук")

        for Animal in self.__animals:
            print(Animal.name, "издает звук", Animal.doSound)

    def amountOfFood1(self, value):
        if self.__amountOfFood > 200:
            self.__amountOfFood = 200
        elif self.__amountOfFood < 0:
            self.__amountOfFood = 0
        else:
            self.__amountOfFood = value

    def food1(self, food, Animal):
        if (not (Animal.isVegan) and (not(self.__animals[0].isVegan))):
            if ((food == "Рыба") or (food == "Мясо") or (food == "Ягоды")):
                self.__food.append(food)
                print("Теперь список доступной еды для вольера такой:", self.__food)
            else:
                print("Указанную еду нельзя добавить, так как она не подходит Хищникам")
        else:
            print("Не все животные являются одним типом, а именно Хищниками")

        if (Animal.sigh == "Мирный" and self.__animals[0].sigh == "Мирный"):
            if ((food == "Ягоды") or (food == "Семена") or (food == "Трава")):
                self.__food.append(food)
                print("Теперь список доступной еды для вольера такой:", self.__food)
            else:
                print("Указанную еду нельзя добавить, так как она не подходит Мирным")
        else:
            print("Не все животные являются одним типом, а именно Мирными")


    def feedAnimals(self, amountOfFood):
        if (self.__amountOfFood >= amountOfFood) and (amountOfFood > 0) and (self.__amountOfFood >0):
            self.__amountOfFood -= amountOfFood
            print("Животным в вольер насыпали:", self.__food)
            print("Теперь количество запасов еды вольера составляет:",  self.__amountOfFood)
        elif (self.__amountOfFood < amountOfFood) or (self.__amountOfFood <0):
            print("Запасов еды вольера недостаточно, чтобы покормить животных")
        elif amountOfFood <= 0:
            print("Ты пытаешься покормить животных ничем")
