from project.meals.meal import Meal


class Starter(Meal):

    def __init__(self, name: str, price: float, quantity: int = 60):
        super().__init__(name, price, quantity)

    @property
    def type_of_meal(self):
        return "Starter"
