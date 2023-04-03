from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):

    def __init__(self, name: str, oxygen: int = 50):
        super().__init__(name, oxygen)

    @staticmethod
    def breathe_amount():
        return 10

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

