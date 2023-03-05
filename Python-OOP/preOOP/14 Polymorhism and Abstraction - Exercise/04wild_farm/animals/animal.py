from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @property
    @abstractmethod
    def make_sound(self):
        ...

    @property
    @abstractmethod
    def specific_food_type(self):
        ...

    @property
    @abstractmethod
    def gained_weight(self):
        ...

    def feed(self, food):
        allowed_foods = [f.__name__ for f in self.specific_food_type()]

        if food.__class__.__name__ not in allowed_foods:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * self.gained_weight()
        self.food_eaten += food.quantity


class Bird(Animal, ABC):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def make_sound(self):
        ...

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def make_sound(self):
        ...

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
