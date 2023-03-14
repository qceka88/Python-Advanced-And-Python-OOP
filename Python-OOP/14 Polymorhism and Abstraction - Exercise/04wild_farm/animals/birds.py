from project.animals.animal import Bird
from project.food import Seed, Meat, Fruit, Vegetable


class Owl(Bird):

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    @property
    def food_type(self):
        return (Meat,)

    @property
    def gained_weight(self):
        return .25


class Hen(Bird):

    @staticmethod
    def make_sound():
        return "Cluck"

    @property
    def food_type(self):
        return Vegetable, Fruit, Meat, Seed

    @property
    def gained_weight(self):
        return .35
