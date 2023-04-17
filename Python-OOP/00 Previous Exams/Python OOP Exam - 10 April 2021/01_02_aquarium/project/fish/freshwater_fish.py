from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    SIZE = 3

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, FreshwaterFish.SIZE, price)

    def eat(self):
        self.size += 3


