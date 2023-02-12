from project.beverage.beverage import Beverage


class HotBeverage(Beverage):

    def __init__(self, name: str, price: float, milliliters: float):
        super().__init__(name, price, milliliters)
