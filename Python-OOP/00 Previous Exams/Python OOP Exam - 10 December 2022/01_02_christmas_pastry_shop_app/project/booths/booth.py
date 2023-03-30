from abc import ABC, abstractmethod


class Booth(ABC):

    def __init__(self, booth_number: int, capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders = []
        self.price_for_reservation: float = 0
        self.is_reserved: bool = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Capacity cannot be a negative number!")
        self.__capacity = value

    @property
    @abstractmethod
    def single_price(self):
        ...

    def reserve(self, number_of_people: int):
        self.price_for_reservation = self.single_price * number_of_people
        self.is_reserved = True
