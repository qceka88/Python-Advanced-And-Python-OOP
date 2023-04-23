from project.appliances.appliance import Appliance


class Stove(Appliance):
    COST = 0.7

    def __init__(self):
        super().__init__(Stove.COST)

