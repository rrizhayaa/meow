from Animals.BaseAnimal import *

class Goose(BaseAnimal):

    def __init__(self, Name, Age, FoodTypes, Biome, Square, Type, VolumeFood, Sigh, Sound):
        super().__init__(Name, Age, ["Трава", "Семена", "Ягоды"], "Луг", '20', "Гусь", '100', "Хищник", "Га-га-га"]