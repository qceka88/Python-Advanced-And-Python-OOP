from project.supply.supply import Supply


class Drink(Supply):
    # TODO: check is energy  implemented correctly
    def __init__(self, name: str, energy: int = 15):
        super().__init__(name, energy)

    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"
