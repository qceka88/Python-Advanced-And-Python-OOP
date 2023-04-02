from abc import ABC, abstractmethod


class Car(ABC):

    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken: bool = False

    @property
    @abstractmethod
    def limits(self):
        ...

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")

        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if not (self.limits[0] <= value <= self.limits[1]):
            raise ValueError(f"Invalid speed limit! Must be between {self.limits[0]} and {self.limits[1]}!")

        self.__speed_limit = value


