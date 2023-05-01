from abc import ABC, abstractmethod
from math import log2


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
        if not value.strip():
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError("Model name cannot be empty.")

        self.__model = value

    @property
    @abstractmethod
    def type(self):
        ...

    @property
    @abstractmethod
    def valid_processors(self):
        ...

    @property
    @abstractmethod
    def max_ram(self):
        ...

    @property
    def ram_price_and_size(self):
        return {2 ** n: n * 100 for n in range(1, int(log2(self.max_ram) + 1))}

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.valid_processors:
            raise ValueError(
                f"{processor} is not compatible with {self.type.lower()} {self.manufacturer} {self.model}!")

        if ram not in self.ram_price_and_size:
            raise ValueError(
                f"{ram}GB RAM is not compatible with {self.type.lower()} {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price = self.valid_processors[processor] + self.ram_price_and_size[ram]

        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
