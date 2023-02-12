class Topping:

    def __init__(self, topping_type: str, weight: float):
        self.topping_type = topping_type
        self.weight = weight

    @property
    def topping_type(self):
        return self.__topping_type

    @topping_type.setter
    def topping_type(self, current_topping):
        if not current_topping:
            raise ValueError("The topping type cannot be an empty string")
        self.__topping_type = current_topping

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, current_weight: float):
        if current_weight <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self.__weight = current_weight
