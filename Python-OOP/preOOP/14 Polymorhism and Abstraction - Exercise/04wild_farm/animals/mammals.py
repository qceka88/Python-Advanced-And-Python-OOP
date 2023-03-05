from project.food import Meat, Vegetable, Fruit, Seed
from project.animals.animal import Mammal


class Mouse(Mammal):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def specific_food_type(self):
        return [Vegetable, Fruit]

    def gained_weight(self):
        return 0.10


class Dog(Mammal):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def specific_food_type(self):
        return [Meat]

    def gained_weight(self):
        return 0.40


class Cat(Mammal):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def specific_food_type(self):
        return [Vegetable, Meat]

    def gained_weight(self):
        return 0.30


class Tiger(Mammal):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def specific_food_type(self):
        return [Meat]

    def gained_weight(self):
        return 1.00
