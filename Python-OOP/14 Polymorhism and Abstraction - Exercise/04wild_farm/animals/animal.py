from abc import ABC, abstractmethod

from project.food import Food


class Animal(ABC):

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eat = 0

    @staticmethod
    @abstractmethod
    def make_sound():
        ...

    @property
    @abstractmethod
    def food_type(self):
        ...

    @property
    @abstractmethod
    def gained_weight(self):
        ...

    def feed(self, food: Food):
        if type(food) not in self.food_type:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eat += food.quantity
        self.weight += self.gained_weight * food.quantity


class Bird(Animal, ABC):

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        message = f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eat}]"
        return message


class Mammal(Animal, ABC):

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        message = f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eat}]"
        return message
