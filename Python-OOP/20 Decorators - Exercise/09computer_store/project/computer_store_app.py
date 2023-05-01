from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:

    def __init__(self):
        self.warehouse = []
        self.profits = 0

    @property
    def valid_computers(self):
        return {
            "Desktop Computer": DesktopComputer,
            "Laptop": Laptop
        }

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        try:
            new_computer = self.valid_computers[type_computer](manufacturer, model)
            result = new_computer.configure_computer(processor, ram)
            self.warehouse.append(new_computer)

            return result

        except KeyError:
            raise ValueError(f"{type_computer} is not a valid type computer!")

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for computer in self.warehouse:
            if computer.price <= client_budget and computer.processor == wanted_processor and wanted_ram <= computer.ram:
                self.profits += client_budget - computer.price
                self.warehouse.remove(computer)
                return f"{computer.__repr__()} sold for {client_budget}$."
        else:
            raise Exception("Sorry, we don't have a computer for you.")
