from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):

    def __init__(self, name: str, oxygen: int = 70):
        super().__init__(name, oxygen)


    @staticmethod
    def breathe_amount():
        return 5

    def increase_oxygen(self, amount: int):
        self.oxygen += amount


