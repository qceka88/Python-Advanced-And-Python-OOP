from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):

    def __init__(self, name: str, oxygen: int = 90):
        super().__init__(name, oxygen)


    @staticmethod
    def breathe_amount():
        return 15

    def increase_oxygen(self, amount: int):
        self.oxygen += amount


