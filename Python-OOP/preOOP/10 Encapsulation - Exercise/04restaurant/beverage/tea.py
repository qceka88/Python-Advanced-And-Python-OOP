from project.beverage.hot_beverage import HotBeverage


class Tea(HotBeverage):

    def __init__(self, name: str, price: float, milliliters: float):
        super().__init__(name, price, milliliters)
