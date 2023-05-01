from project.computer_types.computer import Computer


class Laptop(Computer):
    _max_ram = 64

    @property
    def valid_processors(self):
        return {"AMD Ryzen 9 5950X": 900,
                "Intel Core i9-11900H": 1050,
                "Apple M1 Pro": 1200,
                }

    @property
    def max_ram(self):
        return Laptop._max_ram

    @property
    def type(self):
        return "Laptop"


