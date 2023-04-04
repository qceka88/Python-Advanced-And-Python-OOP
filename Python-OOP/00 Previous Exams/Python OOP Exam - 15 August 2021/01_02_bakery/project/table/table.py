from abc import ABC, abstractmethod
from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):

    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders: [BakedFood] = []
        self.drink_orders: [Drink] = []
        self.number_of_people: int = 0
        self.is_reserved: bool = False
        self.bill = 0

    @staticmethod
    @abstractmethod
    def allowed_numbers():
        ...

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value: int):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")

        self.__capacity = value

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        min_value, max_value = self.allowed_numbers()[0], self.allowed_numbers()[1]
        if not (min_value <= value <= max_value):
            name = self.__class__.__name__.replace("Table", "")
            raise ValueError(f"{name} table's number must be between {min_value} and {max_value} inclusive!")

        self.__table_number = value

    def reserve(self, number_of_people: int):
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)
        self.bill += baked_food.price

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)
        self.bill += drink.price

    def get_bill(self):
        return self.bill

    def clear(self):
        self.drink_orders.clear()
        self.food_orders.clear()
        self.number_of_people = 0
        self.bill = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}\nType: {self.__class__.__name__}\nCapacity: {self.capacity}"
