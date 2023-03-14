from project.animals.animal import Mammal
from project.food import Seed, Meat, Fruit, Vegetable


class Mouse(Mammal):

    @staticmethod
    def make_sound():
        return "Squeak"

    @property
    def food_type(self):
        return Vegetable, Fruit

    @property
    def gained_weight(self):
        return .1


class Dog(Mammal):

    @staticmethod
    def make_sound():
        return "Woof!"

    @property
    def food_type(self):
        return (Meat,)

    @property
    def gained_weight(self):
        return .4


class Cat(Mammal):

    @staticmethod
    def make_sound():
        return "Meow"

    @property
    def food_type(self):
        return Vegetable, Meat

    @property
    def gained_weight(self):
        return .3


class Tiger(Mammal):

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    @property
    def food_type(self):
        return (Meat,)

    @property
    def gained_weight(self):
        return 1
