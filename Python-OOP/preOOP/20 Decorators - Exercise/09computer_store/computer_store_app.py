from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:

    def __init__(self):
        self.warehouse = []
        self.profits = 0

    @property
    def valid_types(self):
        VALID_TYPES = {
            "Laptop": Laptop,
            "Desktop Computer": DesktopComputer}

        return VALID_TYPES

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.valid_types:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        computer = self.valid_types[type_computer](manufacturer, model)
        computer_configuration = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)

        return computer_configuration

    def find_computer(self, client_budget, wanted_processor, wanted_ram):
        for computer in self.warehouse:
            if computer.price <= client_budget and computer.ram >= wanted_ram and wanted_processor == computer.processor:
                return computer

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        computer = self.find_computer(client_budget, wanted_processor, wanted_ram)

        if computer is None:
            raise Exception("Sorry, we don't have a computer for you.")

        self.profits += client_budget - computer.price
        self.warehouse.remove(computer)

        return f"{computer} sold for {client_budget}$."

# computer_store = ComputerStoreApp()
# print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 6))
# print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 65))
# print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Intel Core i9-11900H", 32))
# print(computer_store.build_computer("Desktop Computer", "Dell", "AlienWare", "AMD Ryzen 7 5700G", 128))
# print(computer_store.build_computer("Desktop Computer", "Dell", "AlienWare", "AMD Ryzen 7 5700G", 123))
# print(computer_store.build_computer("Desktop Computer", "Dell", "AlienWare", "AMD Ryzen 7 5700G", 256))
# print(computer_store.sell_computer(14300, "Apple M1 Pro", 10))
# print(computer_store.sell_computer(1, "Intel Core i5-12600K", 11))
