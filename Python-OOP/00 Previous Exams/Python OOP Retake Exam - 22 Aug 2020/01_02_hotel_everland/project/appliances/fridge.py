from project.appliances.appliance import Appliance


class Fridge(Appliance):
    COST = 1.2

    def __init__(self):
        super().__init__(Fridge.COST)

