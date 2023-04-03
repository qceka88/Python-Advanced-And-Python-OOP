from abc import ABC, abstractmethod


class Astronaut(ABC):

    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Astronaut name cannot be empty string or whitespace!")

        self.__name = value

    @staticmethod
    @abstractmethod
    def breathe_amount():
        ...

    def breathe(self):
        self.oxygen -= self.breathe_amount()


    @abstractmethod
    def increase_oxygen(self, amount: int):
        ...
