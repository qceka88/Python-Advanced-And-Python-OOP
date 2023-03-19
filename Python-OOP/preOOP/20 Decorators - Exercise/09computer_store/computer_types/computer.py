from math import sqrt
from abc import ABC, abstractmethod


class Computer(ABC):

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '':
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == '':
            raise ValueError("Model name cannot be empty.")

        self.__model = value

    @property
    @abstractmethod
    def valid_processors(self):
        ...

    @property
    @abstractmethod
    def max_ram(self):
        ...

    @staticmethod
    def valid_ram_sizes(ram_value):
        return {2 ** i: i * 100 for i in range(1, int(sqrt(ram_value))) if 2 ** i <= ram_value}

    @property
    @abstractmethod
    def type_of_the_machine(self):
        ...

    def configure_computer(self, processor: str, ram: int):
        ram_catalogue = self.valid_ram_sizes(self.max_ram)
        if processor not in self.valid_processors:
            raise ValueError(
                f"{processor} is not compatible with {self.type_of_the_machine} {self.manufacturer} {self.model}!")
        if ram > self.max_ram or ram not in ram_catalogue:
            raise ValueError(
                f"{ram}GB RAM is not compatible with {self.type_of_the_machine} {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price += self.valid_processors[self.processor] + ram_catalogue[ram]

        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
