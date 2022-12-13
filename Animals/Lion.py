from Animals.BaseAnimal import *

class Lion(BaseAnimal):

    def __init__(self, Name, Age, FoodTypes, Biome, Square, Type, VolumeFood, Sigh, Sound):
        super().__init__(Name, Age, ["Мясо", "Рыба"], "Саванна", '30', "Лев", '100', "Хищник", "Ррррр")