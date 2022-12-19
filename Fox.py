from Animals.BaseAnimal import *

class Fox(BaseAnimal):

    def __init__(self, Name, Age, FoodTypes, Biome, Square, Type, VolumeFood, Sigh, Sound):
        super().__init__(Name, Age, ["Ягоды", "Мясо", "Рыба"], "Лес", '20', "Лиса", '100', "Хищник", "Фыр-фыр")