from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.stolen import Stolen
from project.delicacies.gingerbread import Gingerbread


class ChristmasPastryShopApp:

    def __init__(self):
        self.booths: [OpenBooth, PrivateBooth] = []
        self.delicacies: [Stolen, Gingerbread] = []
        self.income: float = 0

    @property
    def delicacy_menu(self):
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

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        try:
            delicacy = next(filter(lambda d: d.name == name, self.delicacies))
            raise Exception(f"{delicacy.name} already exists!")

        except StopIteration:
            if type_delicacy not in self.delicacy_menu:
                raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy = self.delicacy_menu[type_delicacy](name, price)
        self.delicacies.append(delicacy)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        try:
            booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
            raise Exception(f"Booth number {booth_number} already exists!")
        except StopIteration:
            if type_booth not in self.valid_booth:
                raise Exception(f"{type_booth} is not a valid booth!")

        booth = self.valid_booth[type_booth](booth_number, capacity)
        self.booths.append(booth)

        return f"Added booth number {booth_number} in the pastry shop."



    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        else:
            raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        try:
            booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")

        try:
            delicacy = next(filter(lambda d: d.name == delicacy_name, self.delicacies))
        except StopIteration:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)

        return f"Booth {booth.booth_number} ordered {delicacy.name}."

    def leave_booth(self, booth_number: int):
        booth = [b for b in self.booths if b.booth_number == booth_number][0]

        total_price = sum([d.price for d in booth.delicacy_orders]) + booth.price_for_reservation
        self.income += total_price
        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0

        return f"Booth {booth_number}:\nBill: {total_price:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

