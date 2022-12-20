class Aviary:

    def __init__(self, Name, Biome, Square):
        self.__name = Name
        self.__biome = Biome
        self.__square = Square
        self.__animals = []
        self.__food = "Рыба", "Мясо", "Ягоды", "Трава", "Семена"
        self.__amountOfFood = 100

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

    def addAnimal(self, Animal):
        if Animal.aviary:
            print (Animal, "уже находится в вольере", self.__name)

        if not(Animal.biome == self.__biome):
            print("Вольер", self.__name, "не подходит для животного:", Animal.type)

        if not(self.__square >= Animal.square):
            print("В вольере", self.__name, "не хватает места для животного", Animal.type)

        if (not(Animal.isVegan) and (self.__animals[0].isVegan)):
            print("Животное", Animal.type, "не сочетается с животными в вольере", self.__name)

        if (Animal.sigh == "Хищник") and not(self.__animals[0].sigh == "Хищник"):
            print("Животное", Animal.type, "не сочетается с животными в вольере", self.__name)

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
        if len(self.__animals)==0:
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

    def food1(self, food, Animal, amount):
        if (not (Animal.isVegan) and (not(self.__animals[0].isVegan)) and ((food == "Рыба") or (food == "Мясо") or (food == "Ягоды"))):
            self.__food.append([food])
        elif (Animal.sigh == "Мирный" and self.__animals[0].sigh == "Мирный") and (Animal.vegan.isVegan and self.__animals[0].vegan.isVegan) and ((food == "Ягоды") or (food == "Семена") or (food == "Трава")):
            self.__food.append([food])

    def feedAnimals(self, food, amountOfFood):
        if self.__amountOfFood >= 100:
            self.__amountOfFood -= 100
            print("Животные в вольере были покормлены этим:", food)
            print("Теперь количество еды составляет:",  amountOfFood
        elif 
            
