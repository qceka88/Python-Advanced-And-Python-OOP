from project.computer_types.computer import Computer


class DesktopComputer(Computer):

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    @property
    def valid_processors(self):
        return {"AMD Ryzen 7 5700G": 500,
                "Intel Core i5-12600K": 600,
                "Apple M1 Max": 1800,
                }

    @property
    def max_ram(self):
        return 128

    @property
    def type_of_the_machine(self):
        return "desktop computer"
