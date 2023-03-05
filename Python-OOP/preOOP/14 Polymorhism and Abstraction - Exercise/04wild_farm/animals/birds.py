from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):

    def __int__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def specific_food_type(self):
        return [Meat]

    def gained_weight(self):
        return 0.25


class Hen(Bird):

    def __int__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def specific_food_type(self):
        return [Meat, Seed, Fruit, Vegetable]

    def gained_weight(self):
        return 0.35
