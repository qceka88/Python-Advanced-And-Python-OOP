from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:

    def __init__(self):
        self.booths: [Booth] = []
        self.delicacies: [Delicacy] = []
        self.income = 0

    @property
    def valid_delicacy(self):
        return {
            "Gingerbread": Gingerbread,
            "Stolen": Stolen,
        }

    @property
    def valid_booth(self):
        return {
            "Open Booth": OpenBooth,
            "Private Booth": PrivateBooth,
        }

    @staticmethod
    def find_data(value, attribute, some_list):
        for obj in some_list:
            if getattr(obj, attribute) == value:
                return obj

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if self.find_data(name, "name", self.delicacies):
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self.valid_delicacy:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy = self.valid_delicacy[type_delicacy](name, price)
        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if self.find_data(booth_number, "booth_number", self.booths):
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.valid_booth:
            raise Exception(f"{type_booth} is not a valid booth!")

        booth = self.valid_booth[type_booth](booth_number, capacity)
        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and  booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        else:
            raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.find_data(booth_number, "booth_number", self.booths)
        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        delicacy = self.find_data(delicacy_name, "name", self.delicacies)
        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.find_data(booth_number, "booth_number", self.booths)

        bill = booth.price_for_reservation + sum([d.price for d in booth.delicacy_orders])
        booth.delicacy_orders = []
        booth.price_for_reservation = 0
        booth.is_reserved = False
        self.income += bill

        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
